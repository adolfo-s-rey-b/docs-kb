[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html#sphx-glr-download-gallery-shapes-and-collections-arrow-guide-py)
 to download the full example code.

Arrow guide[#](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html#arrow-guide "Link to this heading")

=================================================================================================================================

Adding arrow patches to plots.

Arrows are often used to annotate plots. This tutorial shows how to plot arrows that behave differently when the data limits on a plot are changed. In general, points on a plot can either be fixed in "data space" or "display space". Something plotted in data space moves when the data limits are altered - an example would be the points in a scatter plot. Something plotted in display space stays static when data limits are altered - an example would be a figure title or the axis labels.

Arrows consist of a head (and possibly a tail) and a stem drawn between a start point and end point, called 'anchor points' from now on. Here we show three use cases for plotting arrows, depending on whether the head or anchor points need to be fixed in data or display space:

1.  Head shape fixed in display space, anchor points fixed in data space
    
2.  Head shape and anchor points fixed in display space
    
3.  Entire patch fixed in data space
    

Below each use case is presented in turn.

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

[x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.1
[y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.5
[x\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.9
[y\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.8
[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [x\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- [x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
[dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [y\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")

Head shape fixed in display space and anchor points fixed in data space[#](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html#head-shape-fixed-in-display-space-and-anchor-points-fixed-in-data-space "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is useful if you are annotating a plot, and don't want the arrow to change shape or position if you pan or scale the plot.

In this case we use [`patches.FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
.

Note that when the axis limits are changed, the arrow shape stays the same, but the anchor points move.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2)
[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
(([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
), ([x\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                                 mutation\_scale\=100)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)

[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
(([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
), ([x\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                                 mutation\_scale\=100)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set(xlim\=(0, 2), ylim\=(0, 2))

![arrow guide](https://matplotlib.org/stable/_images/sphx_glr_arrow_guide_001_2_00x.png)

Head shape and anchor points fixed in display space[#](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html#head-shape-and-anchor-points-fixed-in-display-space "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is useful if you are annotating a plot, and don't want the arrow to change shape or position if you pan or scale the plot.

In this case we use [`patches.FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
, and pass the keyword argument `transform=ax.transAxes` where `ax` is the Axes we are adding the patch to.

Note that when the axis limits are changed, the arrow shape and location stay the same.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2)
[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
(([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
), ([x\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                                 mutation\_scale\=100,
                                 transform\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].transAxes)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)

[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
(([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
), ([x\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_head](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                                 mutation\_scale\=100,
                                 transform\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].transAxes)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set(xlim\=(0, 2), ylim\=(0, 2))

![arrow guide](https://matplotlib.org/stable/_images/sphx_glr_arrow_guide_002_2_00x.png)

Head shape and anchor points fixed in data space[#](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html#head-shape-and-anchor-points-fixed-in-data-space "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this case we use [`patches.Arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")
, or [`patches.FancyArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 (the latter is in orange).

Note that when the axis limits are changed, the arrow shape and location change.

[`FancyArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
's API is relatively awkward, and requires in particular passing `length_includes_head=True` so that the arrow _tip_ is `(dx, dy)` away from the arrow start. It is only included in this reference because it is the arrow class returned by [`Axes.arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.arrow.html#matplotlib.axes.Axes.arrow "matplotlib.axes.Axes.arrow")
 (in green).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2)

[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.Arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")
([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)
[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.FancyArrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- .4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
                            width\=.1, length\_includes\_head\=True, color\="C1")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + 1, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- .4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
             width\=.1, length\_includes\_head\=True, color\="C2")

[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.Arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")
([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)
[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
 \= [mpatches.FancyArrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- .4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
                            width\=.1, length\_includes\_head\=True, color\="C1")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].add\_patch([arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].[arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
([x\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + 1, [y\_tail](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- .4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
             width\=.1, length\_includes\_head\=True, color\="C2")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set(xlim\=(0, 2), ylim\=(0, 2))

![arrow guide](https://matplotlib.org/stable/_images/sphx_glr_arrow_guide_003_2_00x.png)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.517 seconds)

[`Download Jupyter notebook: arrow_guide.ipynb`](https://matplotlib.org/stable/_downloads/578d1f39fb2f856effcd9fa4221cee9b/arrow_guide.ipynb)

[`Download Python source code: arrow_guide.py`](https://matplotlib.org/stable/_downloads/c39f9f8d3e9365cef90ba58badb9c0be/arrow_guide.py)

[`Download zipped: arrow_guide.zip`](https://matplotlib.org/stable/_downloads/ccceb104f9680673035f7018ad2ddc5e/arrow_guide.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page