[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#main-content)

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
    

matplotlib.gridspec.GridSpec[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib-gridspec-gridspec "Link to this heading")

=================================================================================================================================================================

class matplotlib.gridspec.GridSpec(_nrows_, _ncols_, _figure\=None_, _left\=None_, _bottom\=None_, _right\=None_, _top\=None_, _wspace\=None_, _hspace\=None_, _width\_ratios\=None_, _height\_ratios\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L304-L468)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "Link to this definition")

Bases: [`GridSpecBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase "matplotlib.gridspec.GridSpecBase")

A grid layout to place subplots within a figure.

The location of the grid cells is determined in a similar way to [`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
 using _left_, _right_, _top_, _bottom_, _wspace_ and _hspace_.

Indexing a GridSpec instance returns a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
.

Parameters:

**nrows, ncols**int

The number of rows and columns of the grid.

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, optional

Only used for constrained layout to create a proper layoutgrid.

**left, right, top, bottom**float, optional

Extent of the subplots as a fraction of figure width or height. Left cannot be larger than right, and bottom cannot be larger than top. If not given, the values will be inferred from a figure or rcParams at draw time. See also [`GridSpec.get_subplot_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.get_subplot_params "matplotlib.gridspec.GridSpec.get_subplot_params")
.

**wspace**float, optional

The amount of width reserved for space between subplots, expressed as a fraction of the average axis width. If not given, the values will be inferred from a figure or rcParams when necessary. See also [`GridSpec.get_subplot_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.get_subplot_params "matplotlib.gridspec.GridSpec.get_subplot_params")
.

**hspace**float, optional

The amount of height reserved for space between subplots, expressed as a fraction of the average axis height. If not given, the values will be inferred from a figure or rcParams when necessary. See also [`GridSpec.get_subplot_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.get_subplot_params "matplotlib.gridspec.GridSpec.get_subplot_params")
.

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height.

get\_subplot\_params(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L407-L428)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.get_subplot_params "Link to this definition")

Return the [`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
 for the GridSpec.

In order of precedence the values are taken from

*   non-_None_ attributes of the GridSpec
    
*   the provided _figure_
    
*   `[rcParams["figure.subplot.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.*#rcparam-figure-subplot-left) `
    

Note that the `figure` attribute of the GridSpec is always ignored.

locally\_modified\_subplot\_params()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L430-L437)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.locally_modified_subplot_params "Link to this definition")

Return a list of the names of the subplot parameters explicitly set in the GridSpec.

This is a subset of the attributes of [`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
.

tight\_layout(_figure_, _renderer\=None_, _pad\=1.08_, _h\_pad\=None_, _w\_pad\=None_, _rect\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L439-L468)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.tight_layout "Link to this definition")

Adjust subplot parameters to give specified padding.

Parameters:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure.

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass, optional

The renderer to be used.

**pad**float

Padding between the figure edge and the edges of subplots, as a fraction of the font-size.

**h\_pad, w\_pad**float, optional

Padding (height/width) between edges of adjacent subplots. Defaults to _pad_.

**rect**tuple (left, bottom, right, top), default: None

(left, bottom, right, top) rectangle in normalized figure coordinates that the whole subplots area (including labels) will fit into. Default (None) is the whole figure.

update(_\*_, _left\=<UNSET>_, _bottom\=<UNSET>_, _right\=<UNSET>_, _top\=<UNSET>_, _wspace\=<UNSET>_, _hspace\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L370-L405)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.update "Link to this definition")

Update the subplot parameters of the grid.

Parameters that are not explicitly given are not changed. Setting a parameter to _None_ resets it to `[rcParams["figure.subplot.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.*#rcparam-figure-subplot-left) `.

Parameters:

**left, right, top, bottom**float or None, optional

Extent of the subplots as a fraction of figure width or height.

**wspace, hspace**float or None, optional

Spacing between the subplots as a fraction of the average subplot width / height.

Examples using `matplotlib.gridspec.GridSpec`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#examples-using-matplotlib-gridspec-gridspec "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_customization_thumb.png)

[GridSpec with variable sizes and spacing](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_customization.html)

GridSpec with variable sizes and spacing

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_multicolumn_thumb.png)

[Gridspec for multi-column/row subplot layouts](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_multicolumn.html)

Gridspec for multi-column/row subplot layouts

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_thumb.png)

[Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)

Nested Gridspecs

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_thumb.png)

[Combine two subplots using subplots and GridSpec](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html)

Combine two subplots using subplots and GridSpec

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisartist1_thumb.png)

[Custom spines with axisartist](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html)

Custom spines with axisartist

![](https://matplotlib.org/stable/_images/sphx_glr_imshow_extent_thumb.png)

[Positioning and orientation of imshow images](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html)

Positioning and orientation of imshow images

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page