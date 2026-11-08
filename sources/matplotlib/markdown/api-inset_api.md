[Skip to main content](https://matplotlib.org/stable/api/inset_api.html#main-content)

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
    

`matplotlib.inset`[#](https://matplotlib.org/stable/api/inset_api.html#module-matplotlib.inset "Link to this heading")

=======================================================================================================================

The inset module defines the InsetIndicator class, which draws the rectangle and connectors required for [`Axes.indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset")
 and [`Axes.indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom")
.

class matplotlib.inset.InsetIndicator(_bounds\=None_, _inset\_ax\=None_, _zorder\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L14-L290)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

An artist to highlight an area of interest.

An inset indicator is a rectangle on the plot at the position indicated by _bounds_ that optionally has lines that connect the rectangle to an inset Axes ([`Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
).

Added in version 3.10.

Parameters:

**bounds**\[x0, y0, width, height\], optional

Lower-left corner of rectangle to be marked, and its width and height. If not set, the bounds will be calculated from the data limits of inset\_ax, which must be supplied.

**inset\_ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

An optional inset Axes to draw connecting lines to. Two lines are drawn connecting the indicator box to the inset Axes on corners chosen so as to not overlap with the indicator box.

**zorder**float, default: 4.99

Drawing order of the rectangle and connector lines. The default, 4.99, is just below the default level of inset Axes.

**\*\*kwargs**

Other keyword arguments are passed on to the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 patch.

property axes[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.axes "Link to this definition")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance the artist resides in, or _None_.

property connectors[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.connectors "Link to this definition")

4-tuple of [`patches.ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 or None

The four connector lines connecting to (lower\_left, upper\_left, lower\_right upper\_right) corners of _inset\_ax_. Two lines are set with visibility to _False_, but the user can set the visibility to True if the automatic choice is not deemed correct.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L245-L281)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

property rectangle[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.rectangle "Link to this definition")

[`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
: the indicator frame.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set "Link to this definition")

Set multiple properties at once.

a.set(a\=A, b\=B, c\=C)

is equivalent to

a.set\_a(A)
a.set\_b(B)
a.set\_c(C)

In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.

The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.

Supported properties are

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | unknown |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_color "matplotlib.inset.InsetIndicator.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`edgecolor`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_edgecolor "matplotlib.inset.InsetIndicator.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_linestyle "matplotlib.inset.InsetIndicator.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_linewidth "matplotlib.inset.InsetIndicator.set_linewidth") | float or None |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L89-L91)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_alpha "Link to this definition")

Set the alpha value used for blending - not supported on all backends.

Parameters:

**alpha**float or None

_alpha_ must be within the 0-1 range, inclusive.

set\_color(_c_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L103-L113)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_color "Link to this definition")

Set the edgecolor of the rectangle and the connectors, and the facecolor for the rectangle.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_edgecolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L93-L101)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_edgecolor "Link to this definition")

Set the edge color of the rectangle and the connectors.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or None

set\_linestyle(_ls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L125-L164)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_linestyle "Link to this definition")

Set the linestyle of the rectangle and the connectors.

Parameters:

**ls**{'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)

Possible values:

*   A string:
    
    | linestyle | description |
    | --- | --- |
    | `'-'` or `'solid'` | solid line |
    | `'--'` or `'dashed'` | dashed line |
    | `'-.'` or `'dashdot'` | dash-dotted line |
    | `':'` or `'dotted'` | dotted line |
    | `''` or `'none'` (discouraged: `'None'`, `' '`) | draw nothing |
    
*   A tuple describing the start position and lengths of dashes and spaces:
    
    > (offset, onoffseq)
    
    where
    
    *   _offset_ is a float specifying the offset (in points); i.e. how much is the dash pattern shifted.
        
    *   _onoffseq_ is a sequence of on and off ink in points. There can be arbitrary many pairs of on and off values.
        
    
    Example: The tuple `(0, (10, 5, 1, 5))` means that the pattern starts at the beginning of the line. It draws a 10 point long dash, then a 5 point long space, then a 1 point long dash, followed by a 5 point long space, and then the pattern repeats.
    

For examples see [Linestyles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)
.

set\_linewidth(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/inset.py#L115-L123)
[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.set_linewidth "Link to this definition")

Set the linewidth in points of the rectangle and the connectors.

Parameters:

**w**float or None

zorder \= 4.99[#](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.zorder "Link to this definition")

On this page