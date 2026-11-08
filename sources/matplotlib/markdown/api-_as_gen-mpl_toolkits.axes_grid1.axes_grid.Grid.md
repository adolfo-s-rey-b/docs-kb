[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_grid.Grid[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl-toolkits-axes-grid1-axes-grid-grid "Link to this heading")

==================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_grid.Grid(_fig_, _rect_, _nrows\_ncols_, _n\_axes\=None_, _direction\='row'_, _axes\_pad\=0.02_, _\*_, _share\_all\=False_, _share\_x\=True_, _share\_y\=True_, _label\_mode\='L'_, _axes\_class\=None_, _aspect\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L27-L285)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A grid of Axes.

In Matplotlib, the Axes location (and size) is specified in normalized figure coordinates. This may not be ideal for images that needs to be displayed with a given aspect ratio; for example, it is difficult to display multiple images of a same size with some fixed padding between them. AxesGrid can be used in such case.

Attributes:

**axes\_all**list of Axes

A flat list of Axes. Note that you can also access this directly from the grid. The following is equivalent

grid\[i\] \== grid.axes\_all\[i\]
len(grid) \== len(grid.axes\_all)

**axes\_column**list of list of Axes

A 2D list of Axes where the first index is the column. This results in the usage pattern `grid.axes_column[col][row]`.

**axes\_row**list of list of Axes

A 2D list of Axes where the first index is the row. This results in the usage pattern `grid.axes_row[row][col]`.

**axes\_llc**Axes

The Axes in the lower left corner.

**n\_axes**int

Number of Axes in the grid.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The parent figure.

**rect**(float, float, float, float), (int, int, int), int, or [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")

The axes position, as a `(left, bottom, width, height)` tuple, as a three-digit subplot position code (e.g., `(1, 2, 1)` or `121`), or as a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
.

**nrows\_ncols**(int, int)

Number of rows and columns in the grid.

**n\_axes**int, optional

If given, only the first _n\_axes_ axes in the grid are created.

**direction**{"row", "column"}, default: "row"

Whether axes are created in row-major ("row by row") or column-major order ("column by column"). This also affects the order in which axes are accessed using indexing (`grid[index]`).

**axes\_pad**float or (float, float), default: 0.02

Padding or (horizontal padding, vertical padding) between axes, in inches.

**share\_all**bool, default: False

Whether all axes share their x- and y-axis. Overrides _share\_x_ and _share\_y_.

**share\_x**bool, default: True

Whether all axes of a column share their x-axis.

**share\_y**bool, default: True

Whether all axes of a row share their y-axis.

**label\_mode**{"L", "1", "all", "keep"}, default: "L"

Determines which axes will get tick labels:

*   "L": All axes on the left column get vertical tick labels; all axes on the bottom row get horizontal tick labels.
    
*   "1": Only the bottom left axes is labelled.
    
*   "all": All axes are labelled.
    
*   "keep": Do not do anything.
    

**axes\_class**subclass of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, default: [`mpl_axes.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")

The type of Axes to create.

**aspect**bool, default: False

Whether the axes aspect ratio follows the aspect ratio of the data limits.

get\_aspect()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L236-L238)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.get_aspect "Link to this definition")

Return the aspect of the SubplotDivider.

get\_axes\_locator()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L284-L285)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.get_axes_locator "Link to this definition")

get\_axes\_pad()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L220-L230)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.get_axes_pad "Link to this definition")

Return the axes padding.

Returns:

hpad, vpad

Padding (horizontal pad, vertical pad) in inches.

get\_divider()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L278-L279)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.get_divider "Link to this definition")

get\_geometry()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L202-L206)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.get_geometry "Link to this definition")

Return the number of rows and columns of the grid as (nrows, ncols).

property n\_axes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.n_axes "Link to this definition")

property ngrids[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.ngrids "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

set\_aspect(_aspect_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L232-L234)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.set_aspect "Link to this definition")

Set the aspect of the SubplotDivider.

set\_axes\_locator(_locator_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L281-L282)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.set_axes_locator "Link to this definition")

set\_axes\_pad(_axes\_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L208-L218)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.set_axes_pad "Link to this definition")

Set the padding between the axes.

Parameters:

**axes\_pad**(float, float)

The padding (horizontal pad, vertical pad) in inches.

set\_label\_mode(_mode_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L240-L276)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid.set_label_mode "Link to this definition")

Define which axes have tick labels.

Parameters:

**mode**{"L", "1", "all", "keep"}

The label mode:

*   "L": All axes on the left column get vertical tick labels; all axes on the bottom row get horizontal tick labels.
    
*   "1": Only the bottom left axes is labelled.
    
*   "all": All axes are labelled.
    
*   "keep": Do not do anything.
    

Examples using `mpl_toolkits.axes_grid1.axes_grid.Grid`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#examples-using-mpl-toolkits-axes-grid1-axes-grid-grid "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid_thumb.png)

[Demo Axes Grid](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html)

Demo Axes Grid

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid2_thumb.png)

[Axes Grid2](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid2.html)

Axes Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_demo_edge_colorbar_thumb.png)

[Per-row or per-column colorbars](https://matplotlib.org/stable/gallery/axes_grid1/demo_edge_colorbar.html)

Per-row or per-column colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_demo_imagegrid_aspect_thumb.png)

[ImageGrid cells with a fixed aspect ratio](https://matplotlib.org/stable/gallery/axes_grid1/demo_imagegrid_aspect.html)

ImageGrid cells with a fixed aspect ratio

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axesgrid_thumb.png)

[Simple ImageGrid](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid.html)

Simple ImageGrid

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axesgrid2_thumb.png)

[Simple ImageGrid 2](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid2.html)

Simple ImageGrid 2

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page