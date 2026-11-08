[Skip to main content](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html#sphx-glr-download-gallery-statistics-time-series-histogram-py)
 to download the full example code.

Time Series Histogram[#](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html#time-series-histogram "Link to this heading")

===================================================================================================================================================

This example demonstrates how to efficiently visualize large numbers of time series in a way that could potentially reveal hidden substructure and patterns that are not immediately obvious, and display them in a visually appealing way.

In this example, we generate multiple sinusoidal "signal" series that are buried under a larger number of random walk "noise/background" series. For an unbiased Gaussian random walk with standard deviation of σ, the RMS deviation from the origin after n steps is σ\*sqrt(n). So in order to keep the sinusoids visible on the same scale as the random walks, we scale the amplitude by the random walk RMS. In addition, we also introduce a small random offset `phi` to shift the sines left/right, and some additive random noise to shift individual data points up/down to make the signal a bit more "realistic" (you wouldn't expect a perfect sine wave to appear in your data).

The first plot shows the typical way of visualizing multiple time series by overlaying them on top of each other with `plt.plot` and a small value of `alpha`. The second and third plots show how to reinterpret the data as a 2d histogram, with optional interpolation between data points, by using `np.histogram2d` and `plt.pcolormesh`.

import time

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3, figsize\=(6, 8), layout\='constrained')

\# Fix random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
\# Make some data; a 1D random walk + small fraction of sine waves
[num\_series](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 1000
[num\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[SNR](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.10  \# Signal to Noise Ratio
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 4 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [num\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
\# Generate unbiased Gaussian random walks
[Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
([num\_series](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [num\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
), axis\=-1)
\# Generate sinusoidal signals
[num\_signal](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= round([SNR](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [num\_series](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[phi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 8) \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
([num\_signal](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 1)  \# small random offset
[Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-[num\_signal](https://docs.python.org/3/library/functions.html#int "builtins.int")\
:\] \= (
    [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([num\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
))  \# random walk RMS scaling factor
    \* ([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [phi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
       + 0.05 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
([num\_signal](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [num\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
))  \# small random noise
)

\# Plot series using \`plot\` and a small value of \`alpha\`. With this view it is
\# very difficult to observe the sinusoidal behavior because of how many
\# overlapping series there are. It also takes a bit of time to run because so
\# many individual artists need to be generated.
[tic](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
[axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="C0", alpha\=0.1)
[toc](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
[axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title("Line plot with alpha")
print(f"{[toc](https://docs.python.org/3/library/functions.html#float "builtins.float")
\-[tic](https://docs.python.org/3/library/functions.html#float "builtins.float")
:.3f} sec. elapsed")

\# Now we will convert the multiple time series into a histogram. Not only will
\# the hidden signal be more visible, but it is also a much quicker procedure.
[tic](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
\# Linearly interpolate between the points in each time series
[num\_fine](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 800
[x\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max(), [num\_fine](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[[np.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")\
([x\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, y\_row) for y\_row in [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
[x\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.broadcast\_to](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")
([x\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ([num\_series](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [num\_fine](https://docs.python.org/3/library/functions.html#int "builtins.int")
)).ravel()

\# Plot (x, y) points in 2d histogram with log colorscale
\# It is pretty evident that there is some kind of structure under the noise
\# You can tune vmax to make signal more visible
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["plasma"\]
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [cmap.with\_extremes](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.with_extremes "matplotlib.colors.Colormap.with_extremes")
(bad\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(0))
[h](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [xedges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yedges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.histogram2d](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html#numpy.histogram2d "numpy.histogram2d")
([x\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y\_fine](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=\[400, 100\])
[pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].pcolormesh([xedges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yedges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [h.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
,
                         norm\="log", vmax\=1.5e2, rasterized\=True)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, ax\=[axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], label\="# points", pad\=0)
[axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title("2d histogram and log color scale")

\# Same data but on linear color scale
[pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].pcolormesh([xedges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yedges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [h.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
,
                         vmax\=1.5e2, rasterized\=True)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, ax\=[axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\], label\="# points", pad\=0)
[axes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_title("2d histogram and linear color scale")

[toc](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print(f"{[toc](https://docs.python.org/3/library/functions.html#float "builtins.float")
\-[tic](https://docs.python.org/3/library/functions.html#float "builtins.float")
:.3f} sec. elapsed")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Line plot with alpha, 2d histogram and log color scale, 2d histogram and linear color scale](https://matplotlib.org/stable/_images/sphx_glr_time_series_histogram_001_2_00x.png)

0.334 sec. elapsed
0.123 sec. elapsed

Tags: [plot-type: histogram2d](https://matplotlib.org/stable/_tags/plot-type-histogram2d.html)
 [plot-type: pcolormesh](https://matplotlib.org/stable/_tags/plot-type-pcolormesh.html)
 [purpose: storytelling](https://matplotlib.org/stable/_tags/purpose-storytelling.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [styling: colormap](https://matplotlib.org/stable/_tags/styling-colormap.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
     / [`matplotlib.pyplot.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh "matplotlib.pyplot.pcolormesh")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
    

**Total running time of the script:** (0 minutes 3.776 seconds)

[`Download Jupyter notebook: time_series_histogram.ipynb`](https://matplotlib.org/stable/_downloads/134e3c614df98c9ca81dbc9175fc02ec/time_series_histogram.ipynb)

[`Download Python source code: time_series_histogram.py`](https://matplotlib.org/stable/_downloads/8ccc27687e832118a85d3c746c15f6fa/time_series_histogram.py)

[`Download zipped: time_series_histogram.zip`](https://matplotlib.org/stable/_downloads/1b19aa0adfcc5d34c292cbbbae4cbd59/time_series_histogram.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)