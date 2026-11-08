[Skip to main content](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#main-content)

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
    

Introduction to Axes (or Subplots)[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#introduction-to-axes-or-subplots "Link to this heading")

================================================================================================================================================================

Matplotlib [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 are the gateway to creating your data visualizations. Once an Axes is placed on a figure there are many methods that can be used to add data to the Axes. An Axes typically has a pair of [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 Artists that define the data coordinate system, and include methods to add annotations like x- and y-labels, titles, and legends.

[![../../../_images/anatomy.png](https://matplotlib.org/stable/_images/anatomy.png)](https://matplotlib.org/stable/_images/anatomy.png)

Anatomy of a Figure[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#id1 "Link to this image")

In the picture above, the Axes object was created with `ax = fig.subplots()`. Everything else on the figure was created with methods on this `ax` object, or can be accessed from it. If we want to change the label on the x-axis, we call `ax.set_xlabel('New Label')`, if we want to plot some data we call `ax.plot(x, y)`. Indeed, in the figure above, the only Artist that is not part of the Axes is the Figure itself, so the [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 class is really the gateway to much of Matplotlib's functionality.

Note that Axes are so fundamental to the operation of Matplotlib that a lot of material here is duplicate of that in [Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start)
.

Creating Axes[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#creating-axes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

fig, axs \= plt.subplots(ncols\=2, nrows\=2, figsize\=(3.5, 2.5),
                        layout\="constrained")
\# for each Axes, add an artist, in this case a nice label in the middle...
for row in range(2):
    for col in range(2):
        axs\[row, col\].annotate(f'axs\[{row}, {col}\]', (0.5, 0.5),
                            transform\=axs\[row, col\].transAxes,
                            ha\='center', va\='center', fontsize\=18,
                            color\='darkgrey')
fig.suptitle('plt.subplots()')

([`Source code`](https://matplotlib.org/stable/_downloads/f2d4ea07c842d00504cf7d8cc8bf3bb7/axes_intro-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/bbb6bf8691277e56c55f78f84aceb0da/axes_intro-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/4dcecd440b629e6f2df95748b920275d/axes_intro-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-1.2x.png)

Axes are added using methods on [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 objects, or via the [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 interface. These methods are discussed in more detail in [Creating Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#creating-figures)
 and [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)
. However, for instance [`add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
 will manually position an Axes on the page. In the example above [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 put a grid of subplots on the figure, and `axs` is a (2, 2) array of Axes, each of which can have data added to them.

There are a number of other methods for adding Axes to a Figure:

*   [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
    : manually position an Axes. `fig.add_axes((0, 0, 1, 1))` makes an Axes that fills the whole figure.
    
*   [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
     and [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
    : add a grid of Axes as in the example above. The pyplot version returns both the Figure object and an array of Axes. Note that `fig, ax = plt.subplots()` adds a single Axes to a Figure.
    
*   [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
     and [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
    : add a grid of named Axes and return a dictionary of axes. For `fig, axs = plt.subplot_mosaic([['left', 'right'], ['bottom', 'bottom']])`, `axs['left']` is an Axes in the top row on the left, and `axs['bottom']` is an Axes that spans both columns on the bottom.
    

See [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)
 for more detail on how to arrange grids of Axes on a Figure.

Axes plotting methods[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-plotting-methods "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Most of the high-level plotting methods are accessed from the [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 class. See the API documentation for a full curated list, and [Plot types](https://matplotlib.org/stable/plot_types/index.html#plot-types)
 for examples. A basic example is [`axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
:

fig, ax \= plt.subplots(figsize\=(4, 3))
np.random.seed(19680801)
t \= np.arange(100)
x \= np.cumsum(np.random.randn(100))
lines \= ax.plot(t, x)

([`Source code`](https://matplotlib.org/stable/_downloads/1e916011d0f655ce1f872672bde21c5b/axes_intro-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/6fb20ea72c82ddd7f1b55e83233ed11a/axes_intro-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ec4917d89d6b2b1c8cba0e879560113d/axes_intro-2.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-2.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-2.2x.png)

Note that `plot` returns a list of _lines_ Artists which can subsequently be manipulated, as discussed in [Introduction to Artists](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#users-artists)
.

A very incomplete list of plotting methods is below. Again, see [Plot types](https://matplotlib.org/stable/plot_types/index.html#plot-types)
 for more examples, and [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 for the full list of methods.

|     |     |
| --- | --- |
| [Pairwise data](https://matplotlib.org/stable/plot_types/basic/index.html#basic-plots) | [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")<br>, [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")<br>, [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")<br>, [`step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#matplotlib.axes.Axes.step "matplotlib.axes.Axes.step")<br>, |
| [Array objects](https://numpy.org/doc/stable/reference/arrays.html#arrays "(in NumPy v2.5)") | [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")<br>, [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")<br>, [`quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")<br>, [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")<br>, [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow") |
| [Statistical distributions](https://matplotlib.org/stable/plot_types/stats/index.html#stats-plots) | [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")<br>, [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")<br>, [`hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")<br>, [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")<br>, [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")<br>, [`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot") |
| [Irregularly gridded data](https://matplotlib.org/stable/plot_types/unstructured/index.html#unstructured-plots) | [`tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")<br>, [`tripcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tripcolor.html#matplotlib.axes.Axes.tripcolor "matplotlib.axes.Axes.tripcolor") |

Axes labelling and annotation[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-labelling-and-annotation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Usually we want to label the Axes with an xlabel, ylabel, and title, and often we want to have a legend to differentiate plot elements. The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 class has a number of methods to create these annotations.

fig, ax \= plt.subplots(figsize\=(5, 3), layout\='constrained')
np.random.seed(19680801)
t \= np.arange(200)
x \= np.cumsum(np.random.randn(200))
y \= np.cumsum(np.random.randn(200))
linesx \= ax.plot(t, x, label\='Random walk x')
linesy \= ax.plot(t, y, label\='Random walk y')

ax.set\_xlabel('Time \[s\]')
ax.set\_ylabel('Distance \[km\]')
ax.set\_title('Random walk example')
ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/d75db428c36b6fe316b47ddd4345a698/axes_intro-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/3dcd3a755f9da6bfec6316d1fa2ee2e5/axes_intro-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ea4b042808c0cc0fa9640d7a79ca7d9b/axes_intro-3.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-3.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-3.2x.png)

These methods are relatively straight-forward, though there are a number of [Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html#text-props)
 that can be set on the text objects, like _fontsize_, _fontname_, _horizontalalignment_. Legends can be much more complicated; see [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for more details.

Note that text can also be added to axes using [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
, and [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
. This can be quite sophisticated: see [Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html#text-props)
 and [Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)
 for more information.

Axes limits, scales, and ticking[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-limits-scales-and-ticking "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Each Axes has two (or more) [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 objects, that can be accessed via `matplotlib.axes.Axes.xaxis` and `matplotlib.axes.Axes.yaxis` properties. These have substantial number of methods on them, and for highly customizable Axis-es it is useful to read the API at [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
. However, the Axes class offers a number of helpers for the most common of these methods. Indeed, the [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
, discussed above, is a helper for the [`set_label_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text "matplotlib.axis.Axis.set_label_text")
.

Other important methods set the extent on the axes ([`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
, [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
), or more fundamentally the scale of the axes. So for instance, we can make an Axis have a logarithmic scale, and zoom in on a sub-portion of the data:

fig, ax \= plt.subplots(figsize\=(4, 2.5), layout\='constrained')
np.random.seed(19680801)
t \= np.arange(200)
x \= 2\*\*np.cumsum(np.random.randn(200))
linesx \= ax.plot(t, x)
ax.set\_yscale('log')
ax.set\_xlim(20, 180)

([`Source code`](https://matplotlib.org/stable/_downloads/f992b64160cf41ec36c6f97f83b3fc23/axes_intro-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e65ede779da8d26ea0bba5c1fb9f54a1/axes_intro-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/87fcf307dfeb3796fa8a5565ade4c4b5/axes_intro-4.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-4.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-4.2x.png)

The Axes class also has helpers to deal with Axis ticks and their labels. Most straight-forward is [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
 and [`set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
 which manually set the tick locations and optionally their labels. Minor ticks can be toggled with [`minorticks_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_on.html#matplotlib.axes.Axes.minorticks_on "matplotlib.axes.Axes.minorticks_on")
 or [`minorticks_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_off.html#matplotlib.axes.Axes.minorticks_off "matplotlib.axes.Axes.minorticks_off")
.

Many aspects of Axes ticks and tick labeling can be adjusted using [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
. For instance, to label the top of the axes instead of the bottom,color the ticks red, and color the ticklabels green:

fig, ax \= plt.subplots(figsize\=(4, 2.5))
ax.plot(np.arange(10))
ax.tick\_params(top\=True, labeltop\=True, color\='red', axis\='x',
               labelcolor\='green')

([`Source code`](https://matplotlib.org/stable/_downloads/67dc3d4ccc4d59c0fbcdfd518480decc/axes_intro-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/28d1256a03514918125777f85bbe1e74/axes_intro-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/eda9f4760fb5d6c2c9da2e405f0d8a20/axes_intro-5.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-5.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-5.2x.png)

More fine-grained control on ticks, setting scales, and controlling the Axis can be highly customized beyond these Axes-level helpers.

Axes layout[#](https://matplotlib.org/stable/users/explain/axes/axes_intro.html#axes-layout "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Sometimes it is important to set the aspect ratio of a plot in data space, which we can do with [`set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
:

fig, axs \= plt.subplots(ncols\=2, figsize\=(7, 2.5), layout\='constrained')
np.random.seed(19680801)
t \= np.arange(200)
x \= np.cumsum(np.random.randn(200))
axs\[0\].plot(t, x)
axs\[0\].set\_title('aspect="auto"')

axs\[1\].plot(t, x)
axs\[1\].set\_aspect(3)
axs\[1\].set\_title('aspect=3')

([`Source code`](https://matplotlib.org/stable/_downloads/cc1c5feb3896c485fbbf490656268687/axes_intro-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e2c568c438c26d58e3442386002c8bdf/axes_intro-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/29c80a201c003c171fd0caa36aae9d29/axes_intro-6.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-6.2x.png)](https://matplotlib.org/stable/_images/users-explain-axes-axes_intro-6.2x.png)

On this page