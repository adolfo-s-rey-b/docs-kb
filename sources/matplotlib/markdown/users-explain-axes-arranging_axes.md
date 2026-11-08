[Skip to main content](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#sphx-glr-download-users-explain-axes-arranging-axes-py)
 to download the full example code.

Arranging multiple Axes in a Figure[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-multiple-axes-in-a-figure "Link to this heading")

========================================================================================================================================================================

Often more than one Axes is wanted on a figure at a time, usually organized into a regular grid. Matplotlib has a variety of tools for working with grids of Axes that have evolved over the history of the library. Here we will discuss the tools we think users should use most often, the tools that underpin how Axes are organized, and mention some of the older tools.

Note

Matplotlib uses _Axes_ to refer to the drawing area that contains data, x- and y-axis, ticks, labels, title, etc. See [Parts of a Figure](https://matplotlib.org/stable/users/explain/quick_start.html#figure-parts)
 for more details. Another term that is often used is "subplot", which refers to an Axes that is in a grid with other Axes objects.

Overview[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#overview "Link to this heading")

------------------------------------------------------------------------------------------------------------------

### Create grid-shaped combinations of Axes[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#create-grid-shaped-combinations-of-axes "Link to this heading")

[`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

The primary function used to create figures and a grid of Axes. It creates and places all Axes on the figure at once, and returns an object array with handles for the Axes in the grid. See [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
.

or

[`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")

A simple way to create figures and a grid of Axes, with the added flexibility that Axes can also span rows or columns. The Axes are returned in a labelled dictionary instead of an array. See also [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 and [Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html#mosaic)
.

Sometimes it is natural to have more than one distinct group of Axes grids, in which case Matplotlib has the concept of [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
:

[`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

A virtual figure within a figure.

### Underlying tools[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#underlying-tools "Link to this heading")

Underlying these are the concept of a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 and a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
:

[`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

Specifies the geometry of the grid that a subplot will be placed. The number of rows and number of columns of the grid need to be set. Optionally, the subplot layout parameters (e.g., left, right, etc.) can be tuned.

[`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")

Specifies the location of the subplot in the given [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
.

### Adding single Axes at a time[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#adding-single-axes-at-a-time "Link to this heading")

The above functions create all Axes in a single function call. It is also possible to add Axes one at a time, and this was originally how Matplotlib used to work. Doing so is generally less elegant and flexible, though sometimes useful for interactive work or to place an Axes in a custom location:

[`add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")

Adds a single Axes at a location specified by `[left, bottom, width, height]` in fractions of figure width or height.

[`subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 or [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")

Adds a single subplot on a figure, with 1-based indexing (inherited from Matlab). Columns and rows can be spanned by specifying a range of grid cells.

[`subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")

Similar to [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
, but uses 0-based indexing and two-d python slicing to choose cells.

As a simple example of manually adding an Axes _ax_, lets add a 3 inch x 2 inch Axes to a 4 inch x 3 inch figure. Note that the location of the subplot is defined as \[left, bottom, width, height\] in figure-normalized units:

import matplotlib.pyplot as plt
import numpy as np

[w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [h](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 4, 3
[margin](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.5
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=([w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [h](https://docs.python.org/3/library/functions.html#int "builtins.int")
), facecolor\='lightblue')
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
(([margin](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [margin](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [h](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
                   ([w](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 2 \* [margin](https://docs.python.org/3/library/functions.html#float "builtins.float")
) / [w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, ([h](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 2 \* [margin](https://docs.python.org/3/library/functions.html#float "builtins.float")
) / [h](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

![arranging axes](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_001_2_00x.png)

High-level methods for making grids[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#high-level-methods-for-making-grids "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Basic 2x2 grid[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#basic-2x2-grid "Link to this heading")

We can create a basic 2-by-2 grid of Axes using [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
. It returns a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance and an array of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 objects. The Axes objects can be used to access methods to place artists on the Axes; here we use [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
, but other examples could be [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
, etc.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, nrows\=2, figsize\=(5.5, 3.5),
                        layout\="constrained")
\# add an artist, in this case a nice label in the middle...
for [row](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(2):
    for [col](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(2):
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[row](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [col](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].annotate(f'axs\[{[row](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}, {[col](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}\]', (0.5, 0.5),
                               transform\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[row](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [col](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].transAxes,
                               ha\='center', va\='center', fontsize\=18,
                               color\='darkgrey')
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('plt.subplots()')

![plt.subplots()](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_002_2_00x.png)

We will annotate a lot of Axes, so let's encapsulate the annotation, rather than having that large piece of annotation code every time we need it:

def annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, text, fontsize\=18):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, text, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            ha\="center", va\="center", fontsize\=fontsize, color\="darkgrey")

The same effect can be achieved with [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
, but the return type is a dictionary instead of an array, where the user can give the keys useful meanings. Here we provide two lists, each list representing a row, and each element in the list a key representing the column.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['upper left', 'upper right'\],\
                               \['lower left', 'lower right'\]\],
                              figsize\=(5.5, 3.5), layout\="constrained")
for [k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, f'axd\[{[k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
!r}\]', fontsize\=14)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('plt.subplot\_mosaic()')

![plt.subplot_mosaic()](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_003_2_00x.png)

### Grids of fixed-aspect ratio Axes[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#grids-of-fixed-aspect-ratio-axes "Link to this heading")

Fixed-aspect ratio Axes are common for images or maps. However, they present a challenge to layout because two sets of constraints are being imposed on the size of the Axes - that they fit in the figure and that they have a set aspect ratio. This leads to large gaps between Axes by default:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained",
                        figsize\=(5.5, 3.5), facecolor\='lightblue')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
(1)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Fixed aspect Axes')

![Fixed aspect Axes](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_004_2_00x.png)

One way to address this is to change the aspect of the figure to be close to the aspect ratio of the Axes, however that requires trial and error. Matplotlib also supplies `layout="compressed"`, which will work with simple grids to reduce the gaps between Axes. (The `mpl_toolkits` also provides [`ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
 to accomplish a similar effect, but with a non-standard Axes class).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="compressed", figsize\=(5.5, 3.5),
                        facecolor\='lightblue')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
(1)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Fixed aspect Axes: compressed')

![Fixed aspect Axes: compressed](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_005_2_00x.png)

### Axes spanning rows or columns in a grid[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#axes-spanning-rows-or-columns-in-a-grid "Link to this heading")

Sometimes we want Axes to span rows or columns of the grid. There are actually multiple ways to accomplish this, but the most convenient is probably to use [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 by repeating one of the keys:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['upper left', 'right'\],\
                               \['lower left', 'right'\]\],
                              figsize\=(5.5, 3.5), layout\="constrained")
for [k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, f'axd\[{[k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
!r}\]', fontsize\=14)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('plt.subplot\_mosaic()')

![plt.subplot_mosaic()](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_006_2_00x.png)

See below for the description of how to do the same thing using [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 or [`subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
.

### Variable widths or heights in a grid[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#variable-widths-or-heights-in-a-grid "Link to this heading")

Both [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 and [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 allow the rows in the grid to be different heights, and the columns to be different widths using the _gridspec\_kw_ keyword argument. Spacing parameters accepted by [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 can be passed to [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 and [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
:

[gs\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(width\_ratios\=\[1.4, 1\], height\_ratios\=\[1, 2\])
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['upper left', 'right'\],\
                               \['lower left', 'right'\]\],
                              gridspec\_kw\=[gs\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, figsize\=(5.5, 3.5),
                              layout\="constrained")
for [k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, f'axd\[{[k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
!r}\]', fontsize\=14)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('plt.subplot\_mosaic()')

![plt.subplot_mosaic()](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_007_2_00x.png)

### Nested Axes layouts[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#nested-axes-layouts "Link to this heading")

Sometimes it is helpful to have two or more grids of Axes that may not need to be related to one another. The most simple way to accomplish this is to use [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
. Note that the subfigure layouts are independent, so the Axes spines in each subfigure are not necessarily aligned. See below for a more verbose way to achieve the same effect with [`GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(1, 2, wspace\=0.07, width\_ratios\=\[1.5, 1.\])
[axs0](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].subplots(2, 2)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_facecolor('lightblue')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].suptitle('subfigs\[0\]\\nLeft side')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].supxlabel('xlabel for subfigs\[0\]')

[axs1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].subplots(3, 1)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].suptitle('subfigs\[1\]')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].supylabel('ylabel for subfigs\[1\]')

![arranging axes](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_008_2_00x.png)

It is also possible to nest Axes using [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 using nested lists. This method does not use subfigures, like above, so lacks the ability to add per-subfigure `suptitle` and `supxlabel`, etc. Rather it is a convenience wrapper around the [`subgridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.subgridspec "matplotlib.gridspec.SubplotSpec.subgridspec")
 method described below.

[inner](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\['innerA'\],\
         \['innerB'\]\]
[outer](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\['upper left',  [inner](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\],\
          \['lower left', 'lower right'\]\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
([outer](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, layout\="constrained")
for [k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, f'axd\[{[k](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
!r}\]')

![arranging axes](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_009_2_00x.png)

Low-level and advanced grid methods[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#low-level-and-advanced-grid-methods "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Internally, the arrangement of a grid of Axes is controlled by creating instances of [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 and [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
. _GridSpec_ defines a (possibly non-uniform) grid of cells. Indexing into the _GridSpec_ returns a SubplotSpec that covers one or more grid cells, and can be used to specify the location of an Axes.

The following examples show how to use low-level methods to arrange Axes using _GridSpec_ objects.

### Basic 2x2 grid[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#id2 "Link to this heading")

We can accomplish a 2x2 grid in the same manner as `plt.subplots(2, 2)`:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5.5, 3.5), layout\="constrained")
[spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(ncols\=2, nrows\=2)

[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 0\])
annotate\_axes([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax0')

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 1\])
annotate\_axes([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax1')

[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1, 0\])
annotate\_axes([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax2')

[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1, 1\])
annotate\_axes([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax3')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Manually added subplots using add\_gridspec')

![Manually added subplots using add_gridspec](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_010_2_00x.png)

### Axes spanning rows or grids in a grid[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#axes-spanning-rows-or-grids-in-a-grid "Link to this heading")

We can index the _spec_ array using [NumPy slice syntax](https://numpy.org/doc/stable/user/basics.indexing.html)
 and the new Axes will span the slice. This would be the same as `fig, axd = plt.subplot_mosaic([['ax0', 'ax0'], ['ax1', 'ax2']], ...)`:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5.5, 3.5), layout\="constrained")
[spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(2, 2)

[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, :\])
annotate\_axes([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax0')

[ax10](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1, 0\])
annotate\_axes([ax10](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax10')

[ax11](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([spec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1, 1\])
annotate\_axes([ax11](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax11')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Manually added subplots, spanning a column')

![Manually added subplots, spanning a column](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_011_2_00x.png)

### Manual adjustments to a _GridSpec_ layout[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#manual-adjustments-to-a-gridspec-layout "Link to this heading")

When a _GridSpec_ is explicitly used, you can adjust the layout parameters of subplots that are created from the _GridSpec_. Note this option is not compatible with _constrained layout_ or [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 which both ignore _left_ and _right_ and adjust subplot sizes to fill the figure. Usually such manual placement requires iterations to make the Axes tick labels not overlap the Axes.

These spacing parameters can also be passed to [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 and [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 as the _gridspec\_kw_ argument.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\=None, facecolor\='lightblue')
[gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(nrows\=3, ncols\=3, left\=0.05, right\=0.75,
                      hspace\=0.1, wspace\=0.05)
[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[:\-1, :\])
annotate\_axes([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax0')
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[\-1, :\-1\])
annotate\_axes([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax1')
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[\-1, \-1\])
annotate\_axes([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'ax2')
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Manual gridspec with right=0.75')

![Manual gridspec with right=0.75](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_012_2_00x.png)

### Nested layouts with SubplotSpec[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#nested-layouts-with-subplotspec "Link to this heading")

You can create nested layout similar to [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 using [`subgridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.subgridspec "matplotlib.gridspec.SubplotSpec.subgridspec")
. Here the Axes spines _are_ aligned.

Note this is also available from the more verbose [`gridspec.GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(1, 2)

[gs00](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0\].subgridspec(2, 2)
[gs01](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1\].subgridspec(3, 1)

for [a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(2):
    for [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(2):
        [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs00](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[[a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
        annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, f'axLeft\[{[a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}, {[b](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}\]', fontsize\=10)
        if [a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1 and [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1:
            [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('xlabel')
for [a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(3):
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs01](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[[a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
    annotate\_axes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, f'axRight\[{[a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}, {[b](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}\]')
    if [a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 2:
        [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('ylabel')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('nested gridspecs')

![nested gridspecs](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_013_2_00x.png)

Here's a more sophisticated example of nested _GridSpec_: We create an outer 4x4 grid with each cell containing an inner 3x3 grid of Axes. We outline the outer 4x4 grid by hiding appropriate spines in each of the inner 3x3 grids.

def squiggle\_xy([a](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [c](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [d](https://docs.python.org/3/library/functions.html#int "builtins.int")
, i\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.05)):
    return [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(i\*[a](https://docs.python.org/3/library/functions.html#int "builtins.int")
)\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(i\*[b](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(i\*[c](https://docs.python.org/3/library/functions.html#int "builtins.int")
)\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(i\*[d](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 8), layout\='constrained')
[outer\_grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(4, 4, wspace\=0, hspace\=0)

for [a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(4):
    for [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(4):
        \# gridspec inside gridspec
        [inner\_grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [outer\_grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[[a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].subgridspec(3, 3, wspace\=0, hspace\=0)
        [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [inner\_grid.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.subplots "matplotlib.gridspec.GridSpecBase.subplots")
()  \# Create all subplots for the inner grid.
        for ([c](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [d](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [np.ndenumerate](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")
([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
            [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\*squiggle\_xy([a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1, [c](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1, [d](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1))
            [ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xticks\=\[\], yticks\=\[\])

\# show only the outside spines
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [fig.get\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#matplotlib.figure.Figure.get_axes "matplotlib.figure.Figure.get_axes")
():
    [ss](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 \= [ax.get\_subplotspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_subplotspec.html#matplotlib.axes.Axes.get_subplotspec "matplotlib.axes.Axes.get_subplotspec")
()
    [ax.spines.top.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
([ss.is\_first\_row](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_first_row "matplotlib.gridspec.SubplotSpec.is_first_row")
())
    [ax.spines.bottom.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
([ss.is\_last\_row](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_last_row "matplotlib.gridspec.SubplotSpec.is_last_row")
())
    [ax.spines.left.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
([ss.is\_first\_col](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_first_col "matplotlib.gridspec.SubplotSpec.is_first_col")
())
    [ax.spines.right.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
([ss.is\_last\_col](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_last_col "matplotlib.gridspec.SubplotSpec.is_last_col")
())

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![arranging axes](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_014_2_00x.png)

More reading[#](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#more-reading "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

*   More details about [subplot mosaic](https://matplotlib.org/stable/users/explain/axes/mosaic.html#mosaic)
    .
    
*   More details about [constrained layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
    , used to align spacing in most of these examples.
    

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    
*   [`matplotlib.pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
    
*   [`matplotlib.figure.Figure.add_gridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
    
*   [`matplotlib.figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
    
*   [`matplotlib.gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
    
*   [`matplotlib.gridspec.SubplotSpec.subgridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.subgridspec "matplotlib.gridspec.SubplotSpec.subgridspec")
    
*   [`matplotlib.gridspec.GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
    

**Total running time of the script:** (0 minutes 19.196 seconds)

[`Download Jupyter notebook: arranging_axes.ipynb`](https://matplotlib.org/stable/_downloads/10a4c7d5138a53dac9a9668ec792c819/arranging_axes.ipynb)

[`Download Python source code: arranging_axes.py`](https://matplotlib.org/stable/_downloads/0b1d42ea8dfe97ee8541230cc369ed77/arranging_axes.py)

[`Download zipped: arranging_axes.zip`](https://matplotlib.org/stable/_downloads/fbdc4f7da3d340b2a30ba8ec9bb736c6/arranging_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page