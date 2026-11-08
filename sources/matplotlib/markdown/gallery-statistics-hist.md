[Skip to main content](https://matplotlib.org/stable/gallery/statistics/hist.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-download-gallery-statistics-hist-py)
 to download the full example code.

Histograms[#](https://matplotlib.org/stable/gallery/statistics/hist.html#histograms "Link to this heading")

============================================================================================================

How to plot histograms with Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import colors
from matplotlib.ticker import [PercentFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")

\# Create a random number generator with a fixed seed for reproducibility
[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(19680801)

Generate data and plot a simple histogram[#](https://matplotlib.org/stable/gallery/statistics/hist.html#generate-data-and-plot-a-simple-histogram "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To generate a 1D histogram we only need a single vector of numbers. For a 2D histogram we'll need a second vector. We'll generate both below, and show the histogram for each vector.

[N\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100000
[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 20

\# Generate two normal distributions
[dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
([N\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[dist2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.4 \* [rng.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
([N\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 5

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, sharey\=True, tight\_layout\=True)

\# We can set the number of bins with the \*bins\* keyword argument.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].[hist](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].[hist](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
([dist2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![hist](https://matplotlib.org/stable/_images/sphx_glr_hist_001_2_00x.png)

Updating histogram colors[#](https://matplotlib.org/stable/gallery/statistics/hist.html#updating-histogram-colors "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

The histogram method returns (among other things) a `patches` object. This gives us access to the properties of the objects drawn. Using this, we can edit the histogram to our liking. Let's change the color of each bar based on its y value.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, tight\_layout\=True)

\# N is the count in each bin, bins is the lower-limit of the bin
[N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [patches](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].[hist](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# We'll color code by height, but you could use any scalar
[fracs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / [N](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()

\# we need to normalize the data to 0..1 for the full range of the colormap
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 \= [colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
([fracs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [fracs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max())

\# Now, we'll loop through our objects and set the color of each accordingly
for [thisfrac](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [thispatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 in zip([fracs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [patches](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
):
    [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["viridis"\]([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
([thisfrac](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
))
    [thispatch.set\_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
([color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

\# We can also normalize our inputs by the total number of counts
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].[hist](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, density\=True)

\# Now we format the y-axis to display percentage
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].yaxis.set\_major\_formatter([PercentFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")
(xmax\=1))

![hist](https://matplotlib.org/stable/_images/sphx_glr_hist_002_2_00x.png)

Plot a 2D histogram[#](https://matplotlib.org/stable/gallery/statistics/hist.html#plot-a-2d-histogram "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

To plot a 2D histogram, one only needs two vectors of the same length, corresponding to each axis of the histogram.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(tight\_layout\=True)
[hist](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [ax.hist2d](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [dist2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![hist](https://matplotlib.org/stable/_images/sphx_glr_hist_003_2_00x.png)

Customizing your histogram[#](https://matplotlib.org/stable/gallery/statistics/hist.html#customizing-your-histogram "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

Customizing a 2D histogram is similar to the 1D case, you can control visual components such as the bin size or color normalization.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(5, 15), sharex\=True, sharey\=True,
                        tight\_layout\=True)

\# We can increase the number of bins on each axis
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].hist2d([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [dist2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=40)

\# As well as define normalization of the colors
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].hist2d([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [dist2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=40, [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[colors.LogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
())

\# We can also define custom numbers of bins for each axis
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].hist2d([dist1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [dist2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=(80, 10), [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[colors.LogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
())

![hist](https://matplotlib.org/stable/_images/sphx_glr_hist_004_2_00x.png)

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [plot-type: histogram2d](https://matplotlib.org/stable/_tags/plot-type-histogram2d.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [component: normalization](https://matplotlib.org/stable/_tags/component-normalization.html)
 [component: patch](https://matplotlib.org/stable/_tags/component-patch.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     / [`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
    
*   [`matplotlib.pyplot.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html#matplotlib.pyplot.hist2d "matplotlib.pyplot.hist2d")
    
*   [`matplotlib.ticker.PercentFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")
    

**Total running time of the script:** (0 minutes 2.982 seconds)

[`Download Jupyter notebook: hist.ipynb`](https://matplotlib.org/stable/_downloads/3521362dc0e73684626f9a6f0a9ec8a0/hist.ipynb)

[`Download Python source code: hist.py`](https://matplotlib.org/stable/_downloads/2abff75c7d5b7683b4b3246fb3d41d44/hist.py)

[`Download zipped: hist.zip`](https://matplotlib.org/stable/_downloads/618e44fb789ddc42bfeeb4f7bffa1cff/hist.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page