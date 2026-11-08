[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_divider.SubplotDivider[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl-toolkits-axes-grid1-axes-divider-subplotdivider "Link to this heading")

=========================================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_divider.SubplotDivider(_fig_, _\*args_, _horizontal\=None_, _vertical\=None_, _aspect\=None_, _anchor\='C'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L283-L332)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "Link to this definition")

Bases: [`Divider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.axes_divider.Divider")

The Divider class whose rectangle area is specified as a subplot geometry.

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

get\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L321-L323)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.get_position "Link to this definition")

Return the bounds of the subplot box.

get\_subplotspec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L325-L327)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.get_subplotspec "Link to this definition")

Get the SubplotSpec instance.

set\_subplotspec(_subplotspec_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L329-L332)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.set_subplotspec "Link to this definition")

Set the SubplotSpec instance.

Examples using `mpl_toolkits.axes_grid1.axes_divider.SubplotDivider`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#examples-using-mpl-toolkits-axes-grid1-axes-divider-subplotdivider "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_thumb.png)

[HBoxDivider and VBoxDivider demo](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html)

HBoxDivider and VBoxDivider demo

On this page