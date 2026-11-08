[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_divider.VBoxDivider[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl-toolkits-axes-grid1-axes-divider-vboxdivider "Link to this heading")

================================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_divider.VBoxDivider(_fig_, _\*args_, _horizontal\=None_, _vertical\=None_, _aspect\=None_, _anchor\='C'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L557-L591)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "Link to this definition")

Bases: [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")

A [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")
 for laying out axes vertically, while ensuring that they have equal widths.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

**\*args**tuple (_nrows_, _ncols_, _index_) or int

The array of subplots in the figure has dimensions `(nrows, ncols)`, and _index_ is the index of the subplot being created. _index_ starts at 1 in the upper left corner and increases to the right.

If _nrows_, _ncols_, and _index_ are all single digit numbers, then _args_ can be passed as a single 3-digit number (e.g. 234 for (2, 3, 4)).

**horizontal**list of [`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")
, optional

Sizes for horizontal division.

**vertical**list of [`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")
, optional

Sizes for vertical division.

**aspect**bool, optional

Whether overall rectangular area is reduced so that the relative part of the horizontal and vertical scales have the same scale.

**anchor**(float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', 'N', 'NW', 'W'}, default: 'C'

Placement of the reduced rectangle, when _aspect_ is True.

new\_locator(_ny_, _ny1\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L563-L575)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.new_locator "Link to this definition")

Create an axes locator callable for the specified cell.

Parameters:

**ny, ny1**int

Integers specifying the row-position of the cell. When _ny1_ is None, a single _ny_\-th row is specified. Otherwise, location of rows spanning between _ny_ to _ny1_ (but excluding _ny1_\-th row) is specified.

Examples using `mpl_toolkits.axes_grid1.axes_divider.VBoxDivider`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#examples-using-mpl-toolkits-axes-grid1-axes-divider-vboxdivider "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_thumb.png)

[HBoxDivider and VBoxDivider demo](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html)

HBoxDivider and VBoxDivider demo

On this page