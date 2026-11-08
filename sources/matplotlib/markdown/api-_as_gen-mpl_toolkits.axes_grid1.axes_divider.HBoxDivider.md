[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_divider.HBoxDivider[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl-toolkits-axes-grid1-axes-divider-hboxdivider "Link to this heading")

================================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_divider.HBoxDivider(_fig_, _\*args_, _horizontal\=None_, _vertical\=None_, _aspect\=None_, _anchor\='C'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L516-L554)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider "Link to this definition")

Bases: [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")

A [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")
 for laying out axes horizontally, while ensuring that they have equal heights.

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/7dda8d80f7ab2eb363200a94cb280c4d/demo_axes_hbox_divider.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/8b555365bd17a89e1b5cec57bdb55c5e/demo_axes_hbox_divider_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/654946690332b8fcfb381114daa33668/demo_axes_hbox_divider_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-demo_axes_hbox_divider_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-demo_axes_hbox_divider_00_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/b4f8293d039be29a2fc95cc6a43954b8/demo_axes_hbox_divider_01_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8f82a8bdbff4eea69bbd4bff6f6541a2/demo_axes_hbox_divider_01_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-demo_axes_hbox_divider_01_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-demo_axes_hbox_divider_01_00.2x.png)

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

new\_locator(_nx_, _nx1\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L526-L538)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.new_locator "Link to this definition")

Create an axes locator callable for the specified cell.

Parameters:

**nx, nx1**int

Integers specifying the column-position of the cell. When _nx1_ is None, a single _nx_\-th column is specified. Otherwise, location of columns spanning between _nx_ to _nx1_ (but excluding _nx1_\-th column) is specified.

Examples using `mpl_toolkits.axes_grid1.axes_divider.HBoxDivider`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#examples-using-mpl-toolkits-axes-grid1-axes-divider-hboxdivider "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_thumb.png)

[HBoxDivider and VBoxDivider demo](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html)

HBoxDivider and VBoxDivider demo

On this page