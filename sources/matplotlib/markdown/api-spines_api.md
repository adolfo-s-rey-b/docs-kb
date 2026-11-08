[Skip to main content](https://matplotlib.org/stable/api/spines_api.html#main-content)

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
    

`matplotlib.spines`[#](https://matplotlib.org/stable/api/spines_api.html#module-matplotlib.spines "Link to this heading")

==========================================================================================================================

class matplotlib.spines.Spine(_axes_, _spine\_type_, _path_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L14-L501)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "Link to this definition")

Bases: [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")

An axis spine -- the line noting the data area boundaries.

Spines are the lines connecting the axis tick marks and noting the boundaries of the data area. They can be placed at arbitrary positions. See [`set_position`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
 for more information.

The default position is `('outward', 0)`.

Spines are subclasses of [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
, and inherit much of their behavior.

Spines draw a line, a circle, or an arc depending on if [`set_patch_line`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_line "matplotlib.spines.Spine.set_patch_line")
, [`set_patch_circle`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_circle "matplotlib.spines.Spine.set_patch_circle")
, or [`set_patch_arc`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_arc "matplotlib.spines.Spine.set_patch_arc")
 has been called. Line-like is the default.

For examples see [Spines](https://matplotlib.org/stable/gallery/spines/index.html#spines-examples)
.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance containing the spine.

**spine\_type**str

The spine type.

**path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

The [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance used to draw the spine.

Other Parameters:

**\*\*kwargs**

Valid keyword arguments are:

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | unknown |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
| [`capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "matplotlib.patches.Patch.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "matplotlib.patches.Patch.set_fill") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
| [`hatch_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "matplotlib.patches.Patch.set_hatch_linewidth") | unknown |
| [`hatchcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "matplotlib.patches.Patch.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' or None |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "matplotlib.patches.Patch.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
| [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth") | float or None |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

classmethod arc\_spine(_axes_, _spine\_type_, _center_, _radius_, _theta1_, _theta2_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L468-L475)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.arc_spine "Link to this definition")

Create and return an arc [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
.

classmethod circular\_spine(_axes_, _center_, _radius_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L477-L484)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.circular_spine "Link to this definition")

Create and return a circular [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L220-L224)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.clear "Link to this definition")

Clear the current spine.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L309-L314)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_bounds()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L445-L447)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_bounds "Link to this definition")

Get the bounds of the spine.

get\_patch\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L135-L140)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_patch_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance mapping patch coordinates to data coordinates.

For example, one may define a patch of a circle which represents a radius of 5 by providing coordinates for a unit circle, and a transform which scales the coordinates (the patch coordinate) by 5.

get\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L200-L201)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_path "Link to this definition")

Return the path of this patch.

get\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L351-L354)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_position "Link to this definition")

Return the spine position.

get\_spine\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L356-L413)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_spine_transform "Link to this definition")

Return the spine transform.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L142-L198)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.get_window_extent "Link to this definition")

Return the window extent of the spines in display space, including padding for ticks (but not their labels)

See also

[`matplotlib.axes.Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox")

[`matplotlib.axes.Axes.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_window_extent.html#matplotlib.axes.Axes.get_window_extent "matplotlib.axes.Axes.get_window_extent")

classmethod linear\_spine(_axes_, _spine\_type_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L449-L466)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.linear_spine "Link to this definition")

Create and return a linear [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
.

register\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L209-L218)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.register_axis "Link to this definition")

Register an axis.

An axis should be registered with its corresponding spine from the Axes instance. This allows the spine to clear any axis properties when needed.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _bounds\=<UNSET>_, _capstyle\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _edgegapcolor\=<UNSET>_, _facecolor\=<UNSET>_, _fill\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _patch\_arc\=<UNSET>_, _patch\_circle\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
> | [`bounds`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_bounds "matplotlib.spines.Spine.set_bounds") | (low: float, high: float) |
> | [`capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "matplotlib.patches.Patch.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_color "matplotlib.spines.Spine.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "matplotlib.patches.Patch.set_fill") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "matplotlib.patches.Patch.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "matplotlib.patches.Patch.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' or None |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "matplotlib.patches.Patch.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth") | float or None |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`patch_arc`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_arc "matplotlib.spines.Spine.set_patch_arc") | unknown |
> | [`patch_circle`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_circle "matplotlib.spines.Spine.set_patch_circle") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position") | unknown |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_bounds(_low\=None_, _high\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L415-L443)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_bounds "Link to this definition")

Set the spine bounds.

Parameters:

**low**float or None, optional

The lower spine bound. Passing _None_ leaves the limit unchanged.

The bounds may also be passed as the tuple (_low_, _high_) as the first positional argument.

**high**float or None, optional

The higher spine bound. Passing _None_ leaves the limit unchanged.

set\_color(_c_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L486-L501)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_color "Link to this definition")

Set the edgecolor.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Notes

This method does not modify the facecolor (which defaults to "none"), unlike the [`Patch.set_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color")
 method defined in the parent class. Use [`Patch.set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
 to set the facecolor.

set\_patch\_arc(_center_, _radius_, _theta1_, _theta2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L88-L99)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_arc "Link to this definition")

Set the spine to be arc-like.

set\_patch\_circle(_center_, _radius_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L101-L109)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_circle "Link to this definition")

Set the spine to be circular.

set\_patch\_line()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L111-L114)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_patch_line "Link to this definition")

Set the spine to be linear.

set\_position(_position_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L316-L349)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "Link to this definition")

Set the position of the spine.

Spine position is specified by a 2 tuple of (position type, amount). The position types are:

*   'outward': place the spine out from the data area by the specified number of points. (Negative values place the spine inwards.)
    
*   'axes': place the spine at the specified Axes coordinate (0 to 1).
    
*   'data': place the spine at the specified data coordinate.
    

Additionally, shorthand notations define a special positions:

*   'center' -> `('axes', 0.5)`
    
*   'zero' -> `('data', 0.0)`
    

Examples

[Spine placement](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html)

class matplotlib.spines.Spines(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L539-L612)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "Link to this definition")

Bases: [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "(in Python v3.14)")

The container of all [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
s in an Axes.

The interface is dict-like mapping names (e.g. 'left') to [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
 objects. Additionally, it implements some pandas.Series-like features like accessing elements by attribute:

spines\['top'\].set\_visible(False)
spines.top.set\_visible(False)

Multiple spines can be addressed simultaneously by passing a list:

spines\[\['top', 'right'\]\].set\_visible(False)

Use an open slice to address all spines:

spines\[:\].set\_visible(False)

The latter two indexing methods will return a [`SpinesProxy`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.SpinesProxy "matplotlib.spines.SpinesProxy")
 that broadcasts all `set_*()` and `set()` calls to its members, but cannot be used for any other operation.

classmethod from\_dict(_d_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L565-L567)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines.from_dict "Link to this definition")

class matplotlib.spines.SpinesProxy(_spine\_dict_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/spines.py#L504-L536)
[#](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.SpinesProxy "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A proxy to broadcast `set_*()` and `set()` method calls to contained [`Spines`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
.

The proxy cannot be used for any other operations on its members.

The supported methods are determined dynamically based on the contained spines. If not all spines support a given method, it's executed only on the subset of spines that support it.

On this page