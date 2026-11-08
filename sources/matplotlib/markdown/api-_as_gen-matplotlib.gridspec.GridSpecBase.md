[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#main-content)

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
    

matplotlib.gridspec.GridSpecBase[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib-gridspec-gridspecbase "Link to this heading")

=============================================================================================================================================================================

class matplotlib.gridspec.GridSpecBase(_nrows_, _ncols_, _height\_ratios\=None_, _width\_ratios\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L27-L301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A base class of GridSpec that specifies the geometry of the grid that a subplot will be placed.

Parameters:

**nrows, ncols**int

The number of rows and columns of the grid.

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height.

get\_geometry()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L75-L79)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.get_geometry "Link to this definition")

Return a tuple containing the number of rows and columns in the grid.

get\_grid\_positions(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L145-L190)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.get_grid_positions "Link to this definition")

Return the positions of the grid cells in figure coordinates.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure the grid should be applied to. The subplot parameters (margins and spacing between subplots) are taken from _fig_.

Returns:

**bottoms, tops, lefts, rights**array

The bottom, top, left, right positions of the grid cells in figure coordinates.

get\_height\_ratios()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L137-L143)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.get_height_ratios "Link to this definition")

Return the height ratios.

This is _None_ if no height ratios have been set explicitly.

get\_subplot\_params(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L81-L83)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.get_subplot_params "Link to this definition")

get\_width\_ratios()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L115-L121)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.get_width_ratios "Link to this definition")

Return the width ratios.

This is _None_ if no width ratios have been set explicitly.

property ncols[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.ncols "Link to this definition")

The number of columns in the grid.

new\_subplotspec(_loc_, _rowspan\=1_, _colspan\=1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L85-L99)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.new_subplotspec "Link to this definition")

Create and return a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance.

Parameters:

**loc**(int, int)

The position of the subplot in the grid as `(row_index, column_index)`.

**rowspan, colspan**int, default: 1

The number of rows and columns the subplot should span in the grid.

property nrows[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.nrows "Link to this definition")

The number of rows in the grid.

set\_height\_ratios(_height\_ratios_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L123-L135)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.set_height_ratios "Link to this definition")

Set the relative heights of the rows.

_height\_ratios_ must be of length _nrows_. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`.

set\_width\_ratios(_width\_ratios_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L101-L113)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.set_width_ratios "Link to this definition")

Set the relative widths of the columns.

_width\_ratios_ must be of length _ncols_. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`.

subplots(_\*_, _sharex\=False_, _sharey\=False_, _squeeze\=True_, _subplot\_kw\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L250-L301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.subplots "Link to this definition")

Add all subplots specified by this [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 to its parent figure.

See [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 for detailed documentation.

Examples using `matplotlib.gridspec.GridSpecBase`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#examples-using-matplotlib-gridspec-gridspecbase "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_customization_thumb.png)

[GridSpec with variable sizes and spacing](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_customization.html)

GridSpec with variable sizes and spacing

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_multicolumn_thumb.png)

[Gridspec for multi-column/row subplot layouts](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_multicolumn.html)

Gridspec for multi-column/row subplot layouts

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_thumb.png)

[Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)

Nested Gridspecs

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_imshow_extent_thumb.png)

[Positioning and orientation of imshow images](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html)

Positioning and orientation of imshow images

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page