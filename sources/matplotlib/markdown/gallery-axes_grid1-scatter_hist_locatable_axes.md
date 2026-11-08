[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html#sphx-glr-download-gallery-axes-grid1-scatter-hist-locatable-axes-py)
 to download the full example code.

Align histogram to scatter plot using locatable Axes[#](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html#align-histogram-to-scatter-plot-using-locatable-axes "Link to this heading")

=======================================================================================================================================================================================================================

Show the marginal distributions of a scatter plot as histograms at the sides of the plot.

For a nice alignment of the main Axes with the marginals, the Axes positions are defined by a `Divider`, produced via [`make_axes_locatable`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable")
. Note that the `Divider` API allows setting Axes sizes and pads in inches, which is its main feature.

If one wants to set Axes sizes and pads relative to the main Figure, see the [Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)
 example.

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits.axes\_grid1 import [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# the random data
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.5, 5.5))

\# the scatter plot:
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Set aspect of the main Axes.
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
(1.)

\# create new Axes on the right and on the top of the current Axes
[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 \= [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
\# below height and pad are in inches
[ax\_histx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [divider.append\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
("top", 1.2, pad\=0.1, sharex\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax\_histy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [divider.append\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
("right", 1.2, pad\=0.1, sharey\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

\# make some labels invisible
[ax\_histx.xaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(labelbottom\=False)
[ax\_histy.yaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(labelleft\=False)

\# now determine nice limits by hand:
[binwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.25
[xymax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= max([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)))
[lim](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= (int([xymax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
/[binwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
) + 1)\*[binwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")

[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-[lim](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [lim](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [binwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [binwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[ax\_histx.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax\_histy.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, orientation\='horizontal')

\# the xaxis of ax\_histx and yaxis of ax\_histy are shared with ax,
\# thus there is no need to manually adjust the xlim and ylim of these
\# axis.

[ax\_histx.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[0, 50, 100\])
[ax\_histy.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[0, 50, 100\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scatter hist locatable axes](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_locatable_axes_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable")
    
*   [`matplotlib.axes.Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
    
*   [`matplotlib.axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
    
*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
    

[`Download Jupyter notebook: scatter_hist_locatable_axes.ipynb`](https://matplotlib.org/stable/_downloads/ce58e233c1662384003e44d9764e0860/scatter_hist_locatable_axes.ipynb)

[`Download Python source code: scatter_hist_locatable_axes.py`](https://matplotlib.org/stable/_downloads/51e912a5cf217f8c6647ebf9f5539d38/scatter_hist_locatable_axes.py)

[`Download zipped: scatter_hist_locatable_axes.zip`](https://matplotlib.org/stable/_downloads/810bafa4f7fbc07fb5d0033afb7651fc/scatter_hist_locatable_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)