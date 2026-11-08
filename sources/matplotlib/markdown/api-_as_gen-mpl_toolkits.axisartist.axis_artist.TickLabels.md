[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#main-content)

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
    

mpl\_toolkits.axisartist.axis\_artist.TickLabels[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl-toolkits-axisartist-axis-artist-ticklabels "Link to this heading")

=========================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.axis\_artist.TickLabels(_\*_, _axis\_direction\='bottom'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L431-L620)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels "Link to this definition")

Bases: [`AxisLabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel "mpl_toolkits.axisartist.axis_artist.AxisLabel")

Tick labels. While derived from [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, this single artist draws all ticklabels. As in [`AxisLabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel "mpl_toolkits.axisartist.axis_artist.AxisLabel")
, the position of the text is updated in the fly, so changing text position has no effect. Otherwise, the properties can be changed as a normal [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
. Unlike the ticklabels of the mainline Matplotlib, properties of a single ticklabel alone cannot be modified.

To change the pad between ticks and ticklabels, use [`set_pad`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad")
.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L550-L571)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_ref\_artist()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L448-L450)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.get_ref_artist "Link to this definition")

Return the underlying artist that actually defines some properties (e.g., color) of this artist.

get\_texts\_widths\_heights\_descents(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L605-L620)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.get_texts_widths_heights_descents "Link to this definition")

Return a list of `(width, height, descent)` tuples for ticklabels.

Empty labels are left out.

get\_window\_extents(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L576-L603)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.get_window_extents "Link to this definition")

invert\_axis\_direction()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L480-L482)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.invert_axis_direction "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _axis\_direction\=<UNSET>_, _backgroundcolor\=<UNSET>_, _bbox\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _default\_alignment\=<UNSET>_, _default\_angle\=<UNSET>_, _fontfamily\=<UNSET>_, _fontfeatures\=<UNSET>_, _fontproperties\=<UNSET>_, _fontsize\=<UNSET>_, _fontstretch\=<UNSET>_, _fontstyle\=<UNSET>_, _fontvariant\=<UNSET>_, _fontweight\=<UNSET>_, _gid\=<UNSET>_, _horizontalalignment\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _language\=<UNSET>_, _linespacing\=<UNSET>_, _locs\_angles\_labels\=<UNSET>_, _math\_fontfamily\=<UNSET>_, _mouseover\=<UNSET>_, _multialignment\=<UNSET>_, _pad\=<UNSET>_, _parse\_math\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _rasterized\=<UNSET>_, _rotation\=<UNSET>_, _rotation\_mode\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _text\=<UNSET>_, _transform\=<UNSET>_, _transform\_rotates\_text\=<UNSET>_, _url\=<UNSET>_, _usetex\=<UNSET>_, _verticalalignment\=<UNSET>_, _visible\=<UNSET>_, _wrap\=<UNSET>_, _x\=<UNSET>_, _y\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.set "Link to this definition")

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
> | [`antialiased`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "matplotlib.text.Text.set_antialiased") | bool |
> | [`axis_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.set_axis_direction "mpl_toolkits.axisartist.axis_artist.TickLabels.set_axis_direction") | {"left", "bottom", "right", "top"} |
> | [`backgroundcolor`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "matplotlib.text.Text.set_backgroundcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox") | dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br> or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")<br> or [`c`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`default_alignment`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_default_alignment "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_default_alignment") | {"left", "bottom", "right", "top"} |
> | [`default_angle`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_default_angle "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_default_angle") | {"left", "bottom", "right", "top"} |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`family`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily") | {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'} |
> | [`fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "matplotlib.text.Text.set_fontfeatures") | list of str, or tuple of str, or None |
> | [`fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font_properties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties") | [`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")<br> or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")<br> or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") |
> | [`fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")<br> or [`size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize") | float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} |
> | [`fontstretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch")<br> or [`stretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch") | {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'} |
> | [`fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle")<br> or [`style`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle") | {'normal', 'italic', 'oblique'} |
> | [`fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant")<br> or [`variant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant") | {'normal', 'small-caps'} |
> | [`fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight")<br> or [`weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight") | {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'} |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")<br> or [`ha`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment") | {'left', 'center', 'right'} |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "matplotlib.text.Text.set_language") | str or None |
> | [`linespacing`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing "matplotlib.text.Text.set_linespacing") | 'normal' or float, default: 'normal' |
> | [`locs_angles_labels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.set_locs_angles_labels "mpl_toolkits.axisartist.axis_artist.TickLabels.set_locs_angles_labels") | unknown |
> | [`math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily") | str |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment")<br> or [`ma`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment") | {'left', 'right', 'center'} |
> | [`pad`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad") | float |
> | [`parse_math`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math "matplotlib.text.Text.set_parse_math") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "matplotlib.text.Text.set_position") | (float, float) |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation") | float or {'vertical', 'horizontal'} |
> | [`rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode") | {None, 'default', 'anchor', 'xtick', 'ytick'} |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text") | object |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text") | bool |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`usetex`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex "matplotlib.text.Text.set_usetex") | bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) |
> | [`verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")<br> or [`va`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment") | {'baseline', 'bottom', 'center', 'center\_baseline', 'top'} |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`wrap`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap "matplotlib.text.Text.set_wrap") | bool |
> | [`x`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x "matplotlib.text.Text.set_x") | float |
> | [`y`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y "matplotlib.text.Text.set_y") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_axis\_direction(_label\_direction_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L452-L478)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.set_axis_direction "Link to this definition")

Adjust the text angle and text alignment of ticklabels according to the Matplotlib convention.

The _label\_direction_ must be one of \[left, right, bottom, top\].

| Property | left | bottom | right | top |
| --- | --- | --- | --- | --- |
| ticklabel angle | 90  | 0   | \-90 | 180 |
| ticklabel va | center | baseline | center | baseline |
| ticklabel ha | right | center | right | center |

Note that the text angles are actually relative to (90 + angle of the direction to the ticklabel), which gives 0 for bottom axis.

Parameters:

**label\_direction**{"left", "bottom", "right", "top"}

set\_locs\_angles\_labels(_locs\_angles\_labels_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L573-L574)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.set_locs_angles_labels "Link to this definition")

On this page