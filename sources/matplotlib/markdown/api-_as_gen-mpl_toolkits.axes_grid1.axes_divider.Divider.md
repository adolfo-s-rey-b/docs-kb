[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_divider.Divider[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl-toolkits-axes-grid1-axes-divider-divider "Link to this heading")

====================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_divider.Divider(_fig_, _pos_, _horizontal_, _vertical_, _aspect\=None_, _anchor\='C'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L16-L280)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

An Axes positioning class.

The divider is initialized with lists of horizontal and vertical sizes ([`mpl_toolkits.axes_grid1.axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")
) based on which a given rectangular area will be divided.

The [`new_locator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator")
 method then creates a callable object that can be used as the _axes\_locator_ of the axes.

Parameters:

**fig**Figure

**pos**tuple of 4 floats

Position of the rectangle that will be divided.

**horizontal**list of [`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")

Sizes for horizontal division.

**vertical**list of [`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")

Sizes for vertical division.

**aspect**bool, optional

Whether overall rectangular area is reduced so that the relative part of the horizontal and vertical scales have the same scale.

**anchor**(float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', 'N', 'NW', 'W'}, default: 'C'

Placement of the reduced rectangle, when _aspect_ is True.

add\_auto\_adjustable\_area(_use\_axes_, _pad\=0.1_, _adjust\_dirs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L263-L280)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.add_auto_adjustable_area "Link to this definition")

Add auto-adjustable padding around _use\_axes_ to take their decorations (title, labels, ticks, ticklabels) into account during layout.

Parameters:

**use\_axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes whose decorations are taken into account.

**pad**float, default: 0.1

Additional padding in inches.

**adjust\_dirs**list of {"left", "right", "bottom", "top"}, optional

The sides where padding is added; defaults to all four sides.

append\_size(_position_, _size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L249-L261)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.append_size "Link to this definition")

get\_anchor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L100-L102)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_anchor "Link to this definition")

Return the anchor.

get\_aspect()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L141-L143)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_aspect "Link to this definition")

Return aspect.

get\_horizontal()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L116-L118)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_horizontal "Link to this definition")

Return horizontal sizes.

get\_horizontal\_sizes(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L59-L60)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_horizontal_sizes "Link to this definition")

get\_locator()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L148-L149)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_locator "Link to this definition")

get\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L76-L78)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_position "Link to this definition")

Return the position of the rectangle.

get\_position\_runtime(_ax_, _renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L151-L155)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_position_runtime "Link to this definition")

get\_subplotspec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L104-L105)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_subplotspec "Link to this definition")

get\_vertical()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L129-L131)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_vertical "Link to this definition")

Return vertical sizes.

get\_vertical\_sizes(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L62-L63)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_vertical_sizes "Link to this definition")

new\_locator(_nx_, _ny_, _nx1\=None_, _ny1\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L170-L200)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "Link to this definition")

Return an axes locator callable for the specified cell.

Parameters:

**nx, nx1**int

Integers specifying the column-position of the cell. When _nx1_ is None, a single _nx_\-th column is specified. Otherwise, location of columns spanning between _nx_ to _nx1_ (but excluding _nx1_\-th column) is specified.

**ny, ny1**int

Same as _nx_ and _nx1_, but for row positions.

set\_anchor(_anchor_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L80-L98)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_anchor "Link to this definition")

Parameters:

**anchor**(float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', 'N', 'NW', 'W'}

Either an (_x_, _y_) pair of relative coordinates (0 is left or bottom, 1 is right or top), 'C' (center), or a cardinal direction ('SW', southwest, is bottom left, etc.).

See also

[`Axes.set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor")

set\_aspect(_aspect\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L133-L139)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_aspect "Link to this definition")

Parameters:

**aspect**bool

set\_horizontal(_h_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L107-L114)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_horizontal "Link to this definition")

Parameters:

**h**list of [`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")

sizes for horizontal division

set\_locator(_\_locator_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L145-L146)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_locator "Link to this definition")

set\_position(_pos_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L65-L74)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_position "Link to this definition")

Set the position of the rectangle.

Parameters:

**pos**tuple of 4 floats

position of the rectangle that will be divided

set\_vertical(_v_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L120-L127)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_vertical "Link to this definition")

Parameters:

**v**list of [`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")

sizes for vertical division

Examples using `mpl_toolkits.axes_grid1.axes_divider.Divider`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#examples-using-mpl-toolkits-axes-grid1-axes-divider-divider "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_hbox_divider_thumb.png)

[HBoxDivider and VBoxDivider demo](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_hbox_divider.html)

HBoxDivider and VBoxDivider demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_fixed_size_axes_thumb.png)

[Axes with a fixed physical size](https://matplotlib.org/stable/gallery/axes_grid1/demo_fixed_size_axes.html)

Axes with a fixed physical size

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider1_thumb.png)

[Simple Axes Divider 1](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider1.html)

Simple Axes Divider 1

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider3_thumb.png)

[Simple axes divider 3](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider3.html)

Simple axes divider 3

On this page