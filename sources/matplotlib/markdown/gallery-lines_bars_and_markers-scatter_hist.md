[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-download-gallery-lines-bars-and-markers-scatter-hist-py)
 to download the full example code.

Scatter plot with histograms[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#scatter-plot-with-histograms "Link to this heading")

====================================================================================================================================================================

Add histograms to the x-axes and y-axes margins of a scatter plot.

This layout features a central scatter plot illustrating the relationship between x and y, a histogram at the top displaying the distribution of x, and a histogram on the right showing the distribution of y.

For a nice alignment of the main Axes with the marginals, two options are shown below:

While [`Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 may be a bit more complex, it allows correct handling of main Axes with a fixed aspect ratio.

Let us first define a function that takes x and y data as input, as well as three Axes, the main Axes for the scatter, and two marginal Axes. It will then create the scatter and histograms inside the provided Axes.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# some random data
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)

def scatter\_hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax\_histx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax\_histy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    \# no labels
    [ax\_histx.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\="x", labelbottom\=False)
    [ax\_histy.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\="y", labelleft\=False)

    \# the scatter plot:
    [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    \# now determine nice limits by hand:
    binwidth \= 0.25
    xymax \= max([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)))
    lim \= (int(xymax/binwidth) + 1) \* binwidth

    bins \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-lim, lim + binwidth, binwidth)
    [ax\_histx.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=bins)
    [ax\_histy.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=bins, orientation\='horizontal')

[Defining the Axes positions using subplot\_mosaic](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#id1)
[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#defining-the-axes-positions-using-subplot-mosaic "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We use the [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 function to define the positions and names of the three axes; the empty axes is specified by `'.'`. We manually specify the size of the figure, and can make the different axes have different sizes by specifying the _width\_ratios_ and _height\_ratios_ arguments. The _layout_ argument is set to `'constrained'` to optimize the spacing between the axes.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['histx', '.'\],\
                               \['scatter', 'histy'\]\],
                              figsize\=(6, 6),
                              width\_ratios\=(4, 1), height\_ratios\=(1, 4),
                              layout\='constrained')
scatter\_hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['scatter'\], [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['histx'\], [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['histy'\])

![scatter hist](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_001_2_00x.png)

[Defining the Axes positions using inset\_axes](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#id2)
[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#defining-the-axes-positions-using-inset-axes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 can be used to position marginals _outside_ the main Axes. The advantage of doing so is that the aspect ratio of the main Axes can be fixed, and the marginals will always be drawn relative to the position of the Axes.

\# Create a Figure, which doesn't have to be square.
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\='constrained')
\# Create the main Axes.
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
()
\# The main Axes' aspect can be fixed.
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
('equal')
\# Create marginal Axes, which have 25% of the size of the main Axes.  Note that
\# the inset Axes are positioned \*outside\* (on the right and the top) of the
\# main Axes, by specifying axes coordinates greater than 1.  Axes coordinates
\# less than 0 would likewise specify positions on the left and the bottom of
\# the main Axes.
[ax\_histx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.inset\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
(\[0, 1.05, 1, 0.25\], sharex\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax\_histy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.inset\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
(\[1.05, 0, 0.25, 1\], sharey\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
\# Draw the scatter plot and marginals.
scatter\_hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax\_histx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax\_histy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scatter hist](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_002_2_00x.png)

While we recommend using one of the two methods described above, there are number of other ways to achieve a similar layout:

*   The Axes can be positioned manually in relative coordinates using [`add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
    .
    
*   A gridspec can be used to create the layout ([`add_gridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
    ) and adding only the three desired axes ([`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
    ).
    
*   Four subplots can be created using [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    , and the unused axes in the upper right can be removed manually.
    
*   The `axes_grid1` toolkit can be used, as shown in [Align histogram to scatter plot using locatable Axes](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html)
    .
    

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.figure.Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
    
*   [`matplotlib.pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
    
*   [`matplotlib.figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
    
*   [`matplotlib.axes.Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
    
*   [`matplotlib.axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
    
*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
    

Tags: [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 1.780 seconds)

[`Download Jupyter notebook: scatter_hist.ipynb`](https://matplotlib.org/stable/_downloads/0f50c93f4242dd7f7ed7a31b064465e6/scatter_hist.ipynb)

[`Download Python source code: scatter_hist.py`](https://matplotlib.org/stable/_downloads/3e1134ffd2662d0ad0c453c6dfb7882d/scatter_hist.py)

[`Download zipped: scatter_hist.zip`](https://matplotlib.org/stable/_downloads/c52b5e2b7018c74ee3bcfd193a535c6a/scatter_hist.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page