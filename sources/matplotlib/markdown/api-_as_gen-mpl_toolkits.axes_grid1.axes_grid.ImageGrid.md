[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_grid.ImageGrid[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl-toolkits-axes-grid1-axes-grid-imagegrid "Link to this heading")

=================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_grid.ImageGrid(_fig_, _rect_, _nrows\_ncols_, _n\_axes\=None_, _direction\='row'_, _axes\_pad\=0.02_, _\*_, _share\_all\=False_, _aspect\=True_, _label\_mode\='L'_, _cbar\_mode\=None_, _cbar\_location\='right'_, _cbar\_pad\=None_, _cbar\_size\='5%'_, _cbar\_set\_cax\=True_, _axes\_class\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_grid.py#L288-L561)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "Link to this definition")

Bases: [`Grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.axes_grid.Grid")

A grid of Axes for Image display.

This class is a specialization of [`Grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.axes_grid.Grid")
 for displaying a grid of images. In particular, it forces all axes in a column to share their x-axis and all axes in a row to share their y-axis. It further provides helpers to add colorbars to some or all axes.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The parent figure.

**rect**(float, float, float, float) or int

The axes position, as a `(left, bottom, width, height)` tuple or as a three-digit subplot position code (e.g., "121").

**nrows\_ncols**(int, int)

Number of rows and columns in the grid.

**n\_axes**int, optional

If given, only the first _n\_axes_ axes in the grid are created.

**direction**{"row", "column"}, default: "row"

Whether axes are created in row-major ("row by row") or column-major order ("column by column"). This also affects the order in which axes are accessed using indexing (`grid[index]`).

**axes\_pad**float or (float, float), default: 0.02in

Padding or (horizontal padding, vertical padding) between axes, in inches.

**share\_all**bool, default: False

Whether all axes share their x- and y-axis. Note that in any case, all axes in a column share their x-axis and all axes in a row share their y-axis.

**aspect**bool, default: True

Whether the axes aspect ratio follows the aspect ratio of the data limits.

**label\_mode**{"L", "1", "all"}, default: "L"

Determines which axes will get tick labels:

*   "L": All axes on the left column get vertical tick labels; all axes on the bottom row get horizontal tick labels.
    
*   "1": Only the bottom left axes is labelled.
    
*   "all": all axes are labelled.
    

**cbar\_mode**{"each", "single", "edge", None}, default: None

Whether to create a colorbar for "each" axes, a "single" colorbar for the entire grid, colorbars only for axes on the "edge" determined by _cbar\_location_, or no colorbars. The colorbars are stored in the `cbar_axes` attribute.

**cbar\_location**{"left", "right", "bottom", "top"}, default: "right"

**cbar\_pad**float, default: None

Padding between the image axes and the colorbar axes.

Changed in version 3.10: `cbar_mode="single"` no longer adds _axes\_pad_ between the axes and the colorbar if the _cbar\_location_ is "left" or "bottom".

**cbar\_size**size specification (see `.Size.from_any`), default: "5%"

Colorbar size.

**cbar\_set\_cax**bool, default: True

If True, each axes in the grid has a _cax_ attribute that is bound to associated _cbar\_axes_.

**axes\_class**subclass of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, default: [`mpl_axes.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")

Examples using `mpl_toolkits.axes_grid1.axes_grid.ImageGrid`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#examples-using-mpl-toolkits-axes-grid1-axes-grid-imagegrid "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

On this page