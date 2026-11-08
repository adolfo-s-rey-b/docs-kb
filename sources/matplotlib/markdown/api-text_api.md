[Skip to main content](https://matplotlib.org/stable/api/text_api.html#main-content)

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
    

`matplotlib.text`[#](https://matplotlib.org/stable/api/text_api.html#module-matplotlib.text "Link to this heading")

====================================================================================================================

Classes for including text in a figure.

class matplotlib.text.Text(_x\=0_, _y\=0_, _text\=''_, _\*_, _color\=None_, _verticalalignment\='baseline'_, _horizontalalignment\='left'_, _multialignment\=None_, _fontproperties\=None_, _rotation\=None_, _linespacing\=None_, _rotation\_mode\=None_, _usetex\=None_, _wrap\=False_, _transform\_rotates\_text\=False_, _parse\_math\=None_, _antialiased\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L134-L1602)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

Handle storing and drawing of text in window or data coordinates.

Create a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance at _x_, _y_ with string _text_.

The text is aligned relative to the anchor point (_x_, _y_) according to `horizontalalignment` (default: 'left') and `verticalalignment` (default: 'baseline'). See also [Text alignment](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html)
.

While Text accepts the 'label' keyword argument, by default it is not added to the handles of a legend.

Valid keyword arguments are:

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "matplotlib.text.Text.set_antialiased") | bool |
> | [`backgroundcolor`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "matplotlib.text.Text.set_backgroundcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox") | dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br> or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | unknown |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | unknown |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | unknown |
> | [`color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")<br> or [`c`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
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
> | [`math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily") | str |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment")<br> or [`ma`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment") | {'left', 'right', 'center'} |
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

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L271-L292)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.contains "Link to this definition")

Return whether the mouse event occurred inside the axis-aligned bounding-box of the text.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L840-L915)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_antialiased()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L396-L398)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_antialiased "Link to this definition")

Return whether antialiased rendering is used.

get\_bbox\_patch()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L650-L657)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_bbox_patch "Link to this definition")

Return the bbox Patch, or None if the [`patches.FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 is not made.

For more details see [`Text.set_bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox")
.

get\_c()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L917-L919)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_c "Link to this definition")

Alias for [`get_color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_color "matplotlib.text.Text.get_color")
.

get\_color()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L917-L919)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_color "Link to this definition")

Return the color of the text.

get\_family()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L925-L933)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_family "Link to this definition")

Alias for [`get_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontfamily "matplotlib.text.Text.get_fontfamily")
.

get\_font()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L921-L923)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_font "Link to this definition")

Alias for [`get_fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontproperties "matplotlib.text.Text.get_fontproperties")
.

get\_font\_properties()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L921-L923)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_font_properties "Link to this definition")

Alias for [`get_fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontproperties "matplotlib.text.Text.get_fontproperties")
.

get\_fontfamily()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L925-L933)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontfamily "Link to this definition")

Return the list of font families used for font lookup.

See also

[`font_manager.FontProperties.get_family`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_family "matplotlib.font_manager.FontProperties.get_family")

get\_fontfeatures()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L935-L939)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontfeatures "Link to this definition")

Return a tuple of font feature tags to enable.

get\_fontname()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L941-L949)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontname "Link to this definition")

Return the font name as a string.

See also

[`font_manager.FontProperties.get_name`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_name "matplotlib.font_manager.FontProperties.get_name")

get\_fontproperties()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L921-L923)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontproperties "Link to this definition")

Return the [`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
.

get\_fontsize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L961-L969)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontsize "Link to this definition")

Return the font size as an integer.

See also

[`font_manager.FontProperties.get_size_in_points`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_size_in_points "matplotlib.font_manager.FontProperties.get_size_in_points")

get\_fontstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L951-L959)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontstyle "Link to this definition")

Return the font style as a string.

See also

[`font_manager.FontProperties.get_style`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_style "matplotlib.font_manager.FontProperties.get_style")

get\_fontvariant()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L971-L979)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontvariant "Link to this definition")

Return the font variant as a string.

See also

[`font_manager.FontProperties.get_variant`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_variant "matplotlib.font_manager.FontProperties.get_variant")

get\_fontweight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L981-L989)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontweight "Link to this definition")

Return the font weight as a string or a number.

See also

[`font_manager.FontProperties.get_weight`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_weight "matplotlib.font_manager.FontProperties.get_weight")

get\_ha()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1001-L1006)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_ha "Link to this definition")

Alias for [`get_horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_horizontalalignment "matplotlib.text.Text.get_horizontalalignment")
.

get\_horizontalalignment()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1001-L1006)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_horizontalalignment "Link to this definition")

Return the horizontal alignment as a string. Will be one of 'left', 'center' or 'right'.

get\_language()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1568-L1570)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_language "Link to this definition")

Return the language this Text is in.

get\_linespacing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1179-L1181)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_linespacing "Link to this definition")

Get the line spacing.

get\_math\_fontfamily()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1288-L1298)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_math_fontfamily "Link to this definition")

Return the font family name for math text rendered by Matplotlib.

The default value is `[rcParams["mathtext.fontset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fontset#rcparam-mathtext-fontset) ` (default: `'dejavusans'`).

See also

[`set_math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily")

get\_name()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L941-L949)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_name "Link to this definition")

Alias for [`get_fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontname "matplotlib.text.Text.get_fontname")
.

get\_parse\_math()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1520-L1522)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_parse_math "Link to this definition")

Return whether mathtext parsing is considered for this [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

get\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1016-L1020)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_position "Link to this definition")

Return the (x, y) position of the text.

get\_rotation()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L339-L345)
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_rotation "Link to this definition")

Return the text angle in degrees in the range \[0, 360).\
\
get\_rotation\_mode()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L375-L377)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_rotation_mode "Link to this definition")\
\
Return the text rotation mode.\
\
get\_size()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L961-L969)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_size "Link to this definition")\
\
Alias for [`get_fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontsize "matplotlib.text.Text.get_fontsize")\
.\
\
get\_stretch()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L991-L999)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_stretch "Link to this definition")\
\
Return the font stretch as a string or a number.\
\
See also\
\
[`font_manager.FontProperties.get_stretch`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_stretch "matplotlib.font_manager.FontProperties.get_stretch")\
\
get\_style()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L951-L959)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_style "Link to this definition")\
\
Alias for [`get_fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontstyle "matplotlib.text.Text.get_fontstyle")\
.\
\
get\_text()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1022-L1024)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_text "Link to this definition")\
\
Return the text string.\
\
get\_tightbbox(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1082-L1091)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_tightbbox "Link to this definition")\
\
Get the artist's bounding box in display space, taking clipping into account.\
\
Parameters:\
\
**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")\
, optional\
\
Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).\
\
Returns:\
\
[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")\
 or None\
\
The enclosing bounding box (in figure pixel coordinates), or None if clipping results in no intersection.\
\
See also\
\
[`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")\
\
Get the artist bounding box, ignoring clipping.\
\
get\_transform\_rotates\_text()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L347-L351)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_transform_rotates_text "Link to this definition")\
\
Return whether rotations of the transform affect the text direction.\
\
get\_unitless\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1008-L1014)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_unitless_position "Link to this definition")\
\
Return the (x, y) unitless position of the text.\
\
get\_usetex()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1504-L1506)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_usetex "Link to this definition")\
\
Return whether this [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 object uses TeX for rendering.\
\
get\_va()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1026-L1031)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_va "Link to this definition")\
\
Alias for [`get_verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_verticalalignment "matplotlib.text.Text.get_verticalalignment")\
.\
\
get\_variant()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L971-L979)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_variant "Link to this definition")\
\
Alias for [`get_fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontvariant "matplotlib.text.Text.get_fontvariant")\
.\
\
get\_verticalalignment()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1026-L1031)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_verticalalignment "Link to this definition")\
\
Return the vertical alignment as a string. Will be one of 'top', 'center', 'bottom', 'baseline' or 'center\_baseline'.\
\
get\_weight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L981-L989)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_weight "Link to this definition")\
\
Alias for [`get_fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontweight "matplotlib.text.Text.get_fontweight")\
.\
\
get\_window\_extent(_renderer\=None_, _dpi\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1033-L1080)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_window_extent "Link to this definition")\
\
Return the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")\
 bounding the text, in display units.\
\
In addition to being used internally, this is useful for specifying clickable regions in a png file on a web page.\
\
Parameters:\
\
**renderer**Renderer, optional\
\
A renderer is needed to compute the bounding box. If the artist has already been drawn, the renderer is cached; thus, it is only necessary to pass this argument when calling [`get_window_extent`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_window_extent "matplotlib.text.Text.get_window_extent")\
 before the first draw. In practice, it is usually easier to trigger a draw first, e.g. by calling [`draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")\
 or `plt.show()`.\
\
**dpi**float, optional\
\
The dpi value for computing the bbox, defaults to `self.get_figure(root=True).dpi` (_not_ the renderer dpi); should be set e.g. if to match regions with a figure saved with a custom dpi value.\
\
get\_wrap()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L704-L706)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_wrap "Link to this definition")\
\
Return whether the text can be wrapped.\
\
set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _backgroundcolor\=<UNSET>_, _bbox\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _fontfamily\=<UNSET>_, _fontfeatures\=<UNSET>_, _fontproperties\=<UNSET>_, _fontsize\=<UNSET>_, _fontstretch\=<UNSET>_, _fontstyle\=<UNSET>_, _fontvariant\=<UNSET>_, _fontweight\=<UNSET>_, _gid\=<UNSET>_, _horizontalalignment\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _language\=<UNSET>_, _linespacing\=<UNSET>_, _math\_fontfamily\=<UNSET>_, _mouseover\=<UNSET>_, _multialignment\=<UNSET>_, _parse\_math\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _rasterized\=<UNSET>_, _rotation\=<UNSET>_, _rotation\_mode\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _text\=<UNSET>_, _transform\=<UNSET>_, _transform\_rotates\_text\=<UNSET>_, _url\=<UNSET>_, _usetex\=<UNSET>_, _verticalalignment\=<UNSET>_, _visible\=<UNSET>_, _wrap\=<UNSET>_, _x\=<UNSET>_, _y\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set "Link to this definition")\
\
Set multiple properties at once.\
\
a.set(a\=A, b\=B, c\=C)\
\
is equivalent to\
\
a.set\_a(A)\
a.set\_b(B)\
a.set\_c(C)\
\
In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.\
\
The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.\
\
Supported properties are\
\
> | Property | Description |\
> | --- | --- |\
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |\
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |\
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |\
> | [`antialiased`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "matplotlib.text.Text.set_antialiased") | bool |\
> | [`backgroundcolor`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "matplotlib.text.Text.set_backgroundcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |\
> | [`bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox") | dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br> or None |\
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | unknown |\
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | unknown |\
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | unknown |\
> | [`color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |\
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |\
> | [`fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily") | {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'} |\
> | [`fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "matplotlib.text.Text.set_fontfeatures") | list of str, or tuple of str, or None |\
> | [`fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties") | [`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")<br> or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")<br> or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") |\
> | [`fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize") | float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} |\
> | [`fontstretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch") | {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'} |\
> | [`fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle") | {'normal', 'italic', 'oblique'} |\
> | [`fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant") | {'normal', 'small-caps'} |\
> | [`fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight") | {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'} |\
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |\
> | [`horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment") | {'left', 'center', 'right'} |\
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |\
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |\
> | [`language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "matplotlib.text.Text.set_language") | str or None |\
> | [`linespacing`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing "matplotlib.text.Text.set_linespacing") | 'normal' or float, default: 'normal' |\
> | [`math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily") | str |\
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |\
> | [`multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment") | {'left', 'right', 'center'} |\
> | [`parse_math`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math "matplotlib.text.Text.set_parse_math") | bool |\
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |\
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |\
> | [`position`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "matplotlib.text.Text.set_position") | (float, float) |\
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |\
> | [`rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation") | float or {'vertical', 'horizontal'} |\
> | [`rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode") | {None, 'default', 'anchor', 'xtick', 'ytick'} |\
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |\
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |\
> | [`text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text") | object |\
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |\
> | [`transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text") | bool |\
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |\
> | [`usetex`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex "matplotlib.text.Text.set_usetex") | bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) |\
> | [`verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment") | {'baseline', 'bottom', 'center', 'center\_baseline', 'top'} |\
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |\
> | [`wrap`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap "matplotlib.text.Text.set_wrap") | bool |\
> | [`x`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x "matplotlib.text.Text.set_x") | float |\
> | [`y`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y "matplotlib.text.Text.set_y") | float |\
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |\
\
set\_antialiased(_antialiased_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L379-L394)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "Link to this definition")\
\
Set whether to use antialiased rendering.\
\
Parameters:\
\
**antialiased**bool\
\
Notes\
\
Antialiasing will be determined by `[rcParams["text.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.antialiased#rcparam-text-antialiased) ` (default: `True`) and the parameter _antialiased_ will have no effect if the text contains math expressions.\
\
set\_backgroundcolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1093-L1114)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "Link to this definition")\
\
Set the background color of the text.\
\
This is realized through the bbox (see [`set_bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox")\
), creating the bbox patch if needed.\
\
Parameters:\
\
**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)\
\
See also\
\
[`set_bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox")\
\
To change the position of the bounding box\
\
set\_bbox(_rectprops_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L603-L648)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "Link to this definition")\
\
Draw a box behind/around the text.\
\
This can be used to set a background and/or a frame around the text. It's realized through a [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")\
 behind the text (see also [`Text.get_bbox_patch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_bbox_patch "matplotlib.text.Text.get_bbox_patch")\
). The bbox patch is None by default and only created when needed.\
\
Parameters:\
\
**rectprops**dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")\
 or None\
\
The default boxstyle is 'square'. The mutation scale of the [`patches.FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")\
 is set to the fontsize.\
\
Pass `None` to remove the bbox patch completely.\
\
Examples\
\
t.set\_bbox(dict(facecolor\='red', alpha\=0.5))\
\
set\_c(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1116-L1129)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_c "Link to this definition")\
\
Alias for [`set_color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")\
.\
\
set\_clip\_box(_clipbox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L689-L692)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_clip_box "Link to this definition")\
\
Set the artist's clip [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")\
.\
\
Parameters:\
\
**clipbox**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")\
 or None\
\
Will typically be created from a [`TransformedBbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")\
. For instance, `TransformedBbox(Bbox([[0, 0], [1, 1]]), ax.transAxes)` is the default clipping for an artist added to an Axes.\
\
set\_clip\_on(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L699-L702)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_clip_on "Link to this definition")\
\
Set whether the artist uses clipping.\
\
When False, artists will be visible outside the Axes which can lead to unexpected results.\
\
Parameters:\
\
**b**bool\
\
set\_clip\_path(_path_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L694-L697)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_clip_path "Link to this definition")\
\
Set the artist's clip path.\
\
Parameters:\
\
**path**[`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
 or [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 or [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")\
 or None\
\
The clip path. If given a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
, _transform_ must be provided as well. If _None_, a previously set clip path is removed.\
\
**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
, optional\
\
Only used if _path_ is a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
, in which case the given [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 is converted to a [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")\
 using _transform_.\
\
Notes\
\
For efficiency, if _path_ is a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")\
 this method will set the clipping box to the corresponding rectangle and set the clipping path to `None`.\
\
For technical reasons (support of [`set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")\
), a tuple (_path_, _transform_) is also accepted as a single positional parameter.\
\
set\_color(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1116-L1129)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "Link to this definition")\
\
Set the foreground color of the text\
\
Parameters:\
\
**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)\
\
set\_family(_fontname_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1183-L1205)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_family "Link to this definition")\
\
Alias for [`set_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")\
.\
\
set\_font(_fp_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1478-L1490)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_font "Link to this definition")\
\
Alias for [`set_fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")\
.\
\
set\_font\_properties(_fp_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1478-L1490)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_font_properties "Link to this definition")\
\
Alias for [`set_fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")\
.\
\
set\_fontfamily(_fontname_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1183-L1205)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "Link to this definition")\
\
Set the font family. Can be either a single string, or a list of strings in decreasing priority. Each string may be either a real font name or a generic font class name. If the latter, the specific font names will be looked up in the corresponding rcParams.\
\
If a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 instance is constructed with `fontfamily=None`, then the font is set to `[rcParams["font.family"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.family#rcparam-font-family) ` (default: `['sans-serif']`), and the same is done when [`set_fontfamily()`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")\
 is called on an existing [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 instance.\
\
Parameters:\
\
**fontname**{FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}\
\
See also\
\
[`font_manager.FontProperties.set_family`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_family "matplotlib.font_manager.FontProperties.set_family")\
\
set\_fontfeatures(_features_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1207-L1238)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "Link to this definition")\
\
Set the feature tags to enable on the font.\
\
Parameters:\
\
**features**list of str, or tuple of str, or None\
\
A list of feature tags to be used with the associated font. These strings are eventually passed to HarfBuzz, and so all [string formats supported by hb\_feature\_from\_string()](https://harfbuzz.github.io/harfbuzz-hb-common.html#hb-feature-from-string)\
 are supported. Note though that subranges are not explicitly supported and behaviour may change in the future.\
\
For example, if your desired font includes Stylistic Sets which enable various typographic alternates including one that you do not wish to use (e.g., Contextual Ligatures), then you can pass the following to enable one and not the other:\
\
fp.set\_features(\[\
    'ss01',  \# Use Stylistic Set 1.\
    '-clig',  \# But disable Contextural Ligatures.\
\])\
\
Available font feature tags may be found at [https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist)\
\
set\_fontname(_fontname_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1524-L1540)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontname "Link to this definition")\
\
Alias for [`set_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")\
.\
\
One-way alias only: the getter differs.\
\
Parameters:\
\
**fontname**{FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}\
\
See also\
\
[`font_manager.FontProperties.set_family`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_family "matplotlib.font_manager.FontProperties.set_family")\
\
set\_fontproperties(_fp_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1478-L1490)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "Link to this definition")\
\
Set the font properties that control the text.\
\
Parameters:\
\
**fp**[`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")\
 or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")\
\
If a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
, it is interpreted as a fontconfig pattern parsed by [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")\
. If a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")\
, it is interpreted as the absolute path to a font file.\
\
set\_fontsize(_fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1270-L1286)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "Link to this definition")\
\
Set the font size.\
\
Parameters:\
\
**fontsize**float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}\
\
If a float, the fontsize in points. The string values denote sizes relative to the default font size.\
\
See also\
\
[`font_manager.FontProperties.set_size`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_size "matplotlib.font_manager.FontProperties.set_size")\
\
set\_fontstretch(_stretch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1339-L1354)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "Link to this definition")\
\
Set the font stretch (horizontal condensation or expansion).\
\
Parameters:\
\
**stretch**{a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}\
\
See also\
\
[`font_manager.FontProperties.set_stretch`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_stretch "matplotlib.font_manager.FontProperties.set_stretch")\
\
set\_fontstyle(_fontstyle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1255-L1268)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "Link to this definition")\
\
Set the font style.\
\
Parameters:\
\
**fontstyle**{'normal', 'italic', 'oblique'}\
\
See also\
\
[`font_manager.FontProperties.set_style`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_style "matplotlib.font_manager.FontProperties.set_style")\
\
set\_fontvariant(_variant_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1240-L1253)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "Link to this definition")\
\
Set the font variant.\
\
Parameters:\
\
**variant**{'normal', 'small-caps'}\
\
See also\
\
[`font_manager.FontProperties.set_variant`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_variant "matplotlib.font_manager.FontProperties.set_variant")\
\
set\_fontweight(_weight_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1322-L1337)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "Link to this definition")\
\
Set the font weight.\
\
Parameters:\
\
**weight**{a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}\
\
See also\
\
[`font_manager.FontProperties.set_weight`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_weight "matplotlib.font_manager.FontProperties.set_weight")\
\
set\_ha(_align_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1131-L1143)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_ha "Link to this definition")\
\
Alias for [`set_horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")\
.\
\
set\_horizontalalignment(_align_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1131-L1143)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "Link to this definition")\
\
Set the horizontal alignment relative to the anchor point.\
\
See also [Text alignment](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html)\
.\
\
Parameters:\
\
**align**{'left', 'center', 'right'}\
\
set\_language(_language_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1572-L1602)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "Link to this definition")\
\
Set the language of the text.\
\
Parameters:\
\
**language**str or None\
\
The language of the text in a format accepted by libraqm, namely [a BCP47 language code](https://www.w3.org/International/articles/language-tags/)\
.\
\
If None, then defaults to `[rcParams["text.language"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.language#rcparam-text-language) ` (default: `None`).\
\
set\_linespacing(_spacing_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1161-L1177)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing "Link to this definition")\
\
Set the line spacing.\
\
Parameters:\
\
**spacing**'normal' or float, default: 'normal'\
\
If 'normal', then the line spacing is automatically determined by font metrics for each line individually.\
\
If a float, then line spacing will be fixed to this multiple of the font size for every line.\
\
set\_ma(_align_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1145-L1159)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_ma "Link to this definition")\
\
Alias for [`set_multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment")\
.\
\
set\_math\_fontfamily(_fontfamily_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1300-L1320)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "Link to this definition")\
\
Set the font family for math text rendered by Matplotlib.\
\
This does only affect Matplotlib's own math renderer. It has no effect when rendering with TeX (`usetex=True`).\
\
Parameters:\
\
**fontfamily**str\
\
The name of the font family.\
\
Available font families are defined in the [default matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)\
.\
\
See also\
\
[`get_math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_math_fontfamily "matplotlib.text.Text.get_math_fontfamily")\
\
set\_multialignment(_align_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1145-L1159)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "Link to this definition")\
\
Set the text alignment for multiline texts.\
\
The layout of the bounding box of all the lines is determined by the horizontalalignment and verticalalignment properties. This property controls the alignment of the text lines within that box.\
\
Parameters:\
\
**align**{'left', 'right', 'center'}\
\
set\_name(_fontname_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1524-L1540)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_name "Link to this definition")\
\
Alias for [`set_fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontname "matplotlib.text.Text.set_fontname")\
.\
\
set\_parse\_math(_parse\_math_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1508-L1518)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math "Link to this definition")\
\
Override switch to disable any mathtext parsing for this [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
.\
\
Parameters:\
\
**parse\_math**bool\
\
If False, this [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 will never use mathtext. If True, mathtext will be used if there is an even number of unescaped dollar signs.\
\
set\_position(_xy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1356-L1365)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "Link to this definition")\
\
Set the (_x_, _y_) position of the text.\
\
Parameters:\
\
**xy**(float, float)\
\
set\_rotation(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1389-L1408)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "Link to this definition")\
\
Set the rotation of the text.\
\
Parameters:\
\
**s**float or {'vertical', 'horizontal'}\
\
The rotation angle in degrees in mathematically positive direction (counterclockwise). 'horizontal' equals 0, 'vertical' equals 90.\
\
set\_rotation\_mode(_m_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L353-L373)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "Link to this definition")\
\
Set text rotation mode.\
\
Parameters:\
\
**m**{None, 'default', 'anchor', 'xtick', 'ytick'}\
\
If `"default"`, the text will be first rotated, then aligned according to their horizontal and vertical alignments. If `"anchor"`, then alignment occurs before rotation. "xtick" and "ytick" adjust the horizontal/vertical alignment so that the text is visually pointing towards its anchor point. This is primarily used for rotated tick labels and positions them nicely towards their ticks. Passing `None` will set the rotation mode to `"default"`.\
\
set\_size(_fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1270-L1286)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "Link to this definition")\
\
Alias for [`set_fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")\
.\
\
set\_stretch(_stretch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1339-L1354)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_stretch "Link to this definition")\
\
Alias for [`set_fontstretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch")\
.\
\
set\_style(_fontstyle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1255-L1268)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_style "Link to this definition")\
\
Alias for [`set_fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle")\
.\
\
set\_text(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1437-L1452)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "Link to this definition")\
\
Set the text string _s_.\
\
It may contain newlines (`\n`) or math in LaTeX syntax.\
\
Parameters:\
\
**s**object\
\
Any object gets converted to its [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 representation, except for `None` which is converted to an empty string.\
\
set\_transform\_rotates\_text(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1410-L1419)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "Link to this definition")\
\
Whether rotations of the transform affect the text direction.\
\
Parameters:\
\
**t**bool\
\
set\_usetex(_usetex_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1492-L1502)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex "Link to this definition")\
\
Parameters:\
\
**usetex**bool or None\
\
Whether to render using TeX, `None` means to use `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`).\
\
set\_va(_align_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1421-L1435)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_va "Link to this definition")\
\
Alias for [`set_verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")\
.\
\
set\_variant(_variant_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1240-L1253)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_variant "Link to this definition")\
\
Alias for [`set_fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant")\
.\
\
set\_verticalalignment(_align_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1421-L1435)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "Link to this definition")\
\
Set the vertical alignment relative to the anchor point.\
\
See also [Text alignment](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html)\
.\
\
Parameters:\
\
**align**{'baseline', 'bottom', 'center', 'center\_baseline', 'top'}\
\
set\_weight(_weight_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1322-L1337)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_weight "Link to this definition")\
\
Alias for [`set_fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight")\
.\
\
set\_wrap(_wrap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L708-L727)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap "Link to this definition")\
\
Set whether the text can be wrapped.\
\
Wrapping makes sure the text is confined to the (sub)figure box. It does not take into account any other artists.\
\
Parameters:\
\
**wrap**bool\
\
Notes\
\
Wrapping does not work together with `savefig(..., bbox_inches='tight')` (which is also used internally by `%matplotlib inline` in IPython/Jupyter). The 'tight' setting rescales the canvas to accommodate all content and happens before wrapping.\
\
set\_x(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1367-L1376)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x "Link to this definition")\
\
Set the _x_ position of the text.\
\
Parameters:\
\
**x**float\
\
set\_y(_y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1378-L1387)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y "Link to this definition")\
\
Set the _y_ position of the text.\
\
Parameters:\
\
**y**float\
\
update(_kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L249-L263)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.update "Link to this definition")\
\
\[_Discouraged_\] Update this artist's properties from the dictionary _props_.\
\
Discouraged\
\
This method exists for historic reasons. Please use [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")\
 instead. `artist.update(props)` is nowadays almost identical to `artist.set(**props)` with the only difference that `set` will additionally check that a property is not specified multiple times through aliases.\
\
Parameters:\
\
**props**dict\
\
Dictionary of properties (keys) and their new values.\
\
Returns:\
\
list\
\
A list of return values from the configured setters.\
\
update\_bbox\_position\_size(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L659-L680)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.update_bbox_position_size "Link to this definition")\
\
Update the location and the size of the bbox.\
\
This method should be used when the position and size of the bbox needs to be updated before actually drawing the bbox.\
\
update\_from(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L400-L414)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.update_from "Link to this definition")\
\
Copy properties from _other_ to _self_.\
\
zorder \= 3[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.zorder "Link to this definition")\
\
class matplotlib.text.Annotation(_text_, _xy_, _xytext\=None_, _xycoords\='data'_, _textcoords\=None_, _arrowprops\=None_, _annotation\_clip\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1850-L2251)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "Link to this definition")\
\
Bases: [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
, `_AnnotationBase`\
\
An [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 is a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 that can refer to a specific position _xy_. Optionally an arrow pointing from the text to _xy_ can be drawn.\
\
Attributes:\
\
**xy**\
\
The annotated position.\
\
**xycoords**\
\
The coordinate system for _xy_.\
\
**arrow\_patch**\
\
A [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
 to point from _xytext_ to _xy_.\
\
Annotate the point _xy_ with text _text_.\
\
In the simplest form, the text is placed at _xy_.\
\
Optionally, the text can be displayed in another position _xytext_. An arrow pointing from the text to the annotated point _xy_ can then be added by defining _arrowprops_.\
\
Parameters:\
\
**text**str\
\
The text of the annotation.\
\
**xy**(float, float)\
\
The point _(x, y)_ to annotate. The coordinate system is determined by _xycoords_.\
\
**xytext**(float, float), default: _xy_\
\
The position _(x, y)_ to place the text at. The coordinate system is determined by _textcoords_.\
\
**xycoords**single or two-tuple of str or [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
 or callable, default: 'data'\
\
The coordinate system that _xy_ is given in. The following types of values are supported:\
\
*   One of the following strings:\
    \
    | Value | Description |\
    | --- | --- |\
    | 'figure points' | Points from the lower left of the figure |\
    | 'figure pixels' | Pixels from the lower left of the figure |\
    | 'figure fraction' | Fraction of figure from lower left |\
    | 'subfigure points' | Points from the lower left of the subfigure |\
    | 'subfigure pixels' | Pixels from the lower left of the subfigure |\
    | 'subfigure fraction' | Fraction of subfigure from lower left |\
    | 'axes points' | Points from lower left corner of the Axes |\
    | 'axes pixels' | Pixels from lower left corner of the Axes |\
    | 'axes fraction' | Fraction of Axes from lower left |\
    | 'data' | Use the coordinate system of the object being annotated (default) |\
    | 'polar' | _(theta, r)_ if not native 'data' coordinates |\
    \
    Note that 'subfigure pixels' and 'figure pixels' are the same for the parent figure, so users who want code that is usable in a subfigure can use 'subfigure pixels'.\
    \
*   An [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
    : _xy_ is interpreted as a fraction of the artist's [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")\
    . E.g. _(0, 0)_ would be the lower left corner of the bounding box and _(0.5, 1)_ would be the center top of the bounding box.\
    \
*   A [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
     to transform _xy_ to screen coordinates.\
    \
*   A function with one of the following signatures:\
    \
    def transform(renderer) \-> Bbox\
    def transform(renderer) \-> Transform\
    \
    where _renderer_ is a [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")\
     subclass.\
    \
    The result of the function is interpreted like the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
     and [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
     cases above.\
    \
*   A tuple _(xcoords, ycoords)_ specifying separate coordinate systems for _x_ and _y_. _xcoords_ and _ycoords_ must each be of one of the above described types.\
    \
\
See [Advanced annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#plotting-guide-annotation)\
 for more details.\
\
**textcoords**single or two-tuple of str or [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
 or callable, default: value of _xycoords_\
\
The coordinate system that _xytext_ is given in.\
\
All _xycoords_ values are valid as well as the following strings:\
\
| Value | Description |\
| --- | --- |\
| 'offset points' | Offset, in points, from the _xy_ value |\
| 'offset pixels' | Offset, in pixels, from the _xy_ value |\
| 'offset fontsize' | Offset, relative to fontsize, from the _xy_ value |\
\
**arrowprops**dict, optional\
\
The properties used to draw a [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
 arrow between the positions _xy_ and _xytext_. Defaults to None, i.e. no arrow is drawn.\
\
For historical reasons there are two different ways to specify arrows, "simple" and "fancy":\
\
**Simple arrow:**\
\
If _arrowprops_ does not contain the key 'arrowstyle' the allowed keys are:\
\
| Key | Description |\
| --- | --- |\
| width | The width of the arrow in points |\
| headwidth | The width of the base of the arrow head in points |\
| headlength | The length of the arrow head in points |\
| shrink | Fraction of total length to shrink from both ends |\
| ?   | Any [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")<br> property |\
\
The arrow is attached to the edge of the text box, the exact position (corners or centers) depending on where it's pointing to.\
\
**Fancy arrow:**\
\
This is used if 'arrowstyle' is provided in the _arrowprops_.\
\
Valid keys are the following [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
 parameters:\
\
| Key | Description |\
| --- | --- |\
| arrowstyle | The arrow style |\
| connectionstyle | The connection style |\
| relpos | See below; default is (0.5, 0.5) |\
| patchA | Default is bounding box of the text |\
| patchB | Default is None |\
| shrinkA | In points. Default is 2 points |\
| shrinkB | In points. Default is 2 points |\
| mutation\_scale | Default is text size (in points) |\
| mutation\_aspect | Default is 1 |\
| ?   | Any [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")<br> property |\
\
The exact starting point position of the arrow is defined by _relpos_. It's a tuple of relative coordinates of the text box, where (0, 0) is the lower left corner and (1, 1) is the upper right corner. Values <0 and >1 are supported and specify points outside the text box. By default (0.5, 0.5), so the starting point is centered in the text box.\
\
**annotation\_clip**bool or None, default: None\
\
Whether to clip (i.e. not draw) the annotation when the annotation point _xy_ is outside the Axes area.\
\
*   If _True_, the annotation will be clipped when _xy_ is outside the Axes.\
    \
*   If _False_, the annotation will always be drawn.\
    \
*   If _None_, the annotation will be clipped when _xy_ is outside the Axes and _xycoords_ is 'data'.\
    \
\
**\*\*kwargs**\
\
Additional kwargs are passed to [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
.\
\
Returns:\
\
[`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
\
See also\
\
[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)\
\
property anncoords[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.anncoords "Link to this definition")\
\
The coordinate system to use for [`Annotation.xyann`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.xyann "matplotlib.text.Annotation.xyann")\
.\
\
contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2078-L2085)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.contains "Link to this definition")\
\
Return whether the mouse event occurred inside the axis-aligned bounding-box of the text.\
\
draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2204-L2222)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.draw "Link to this definition")\
\
Draw the Artist (and its children) using the given renderer.\
\
This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")\
 returns False).\
\
Parameters:\
\
**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")\
 subclass.\
\
Notes\
\
This method is overridden in the Artist subclasses.\
\
get\_anncoords()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2114-L2120)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_anncoords "Link to this definition")\
\
Return the coordinate system to use for [`Annotation.xyann`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.xyann "matplotlib.text.Annotation.xyann")\
.\
\
See also _xycoords_ in [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
.\
\
get\_tightbbox(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2247-L2251)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_tightbbox "Link to this definition")\
\
Get the artist's bounding box in display space, taking clipping into account.\
\
Parameters:\
\
**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")\
, optional\
\
Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).\
\
Returns:\
\
[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")\
 or None\
\
The enclosing bounding box (in figure pixel coordinates), or None if clipping results in no intersection.\
\
See also\
\
[`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")\
\
Get the artist bounding box, ignoring clipping.\
\
get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2224-L2245)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_window_extent "Link to this definition")\
\
Return the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")\
 bounding the text, in display units.\
\
In addition to being used internally, this is useful for specifying clickable regions in a png file on a web page.\
\
Parameters:\
\
**renderer**Renderer, optional\
\
A renderer is needed to compute the bounding box. If the artist has already been drawn, the renderer is cached; thus, it is only necessary to pass this argument when calling [`get_window_extent`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_window_extent "matplotlib.text.Annotation.get_window_extent")\
 before the first draw. In practice, it is usually easier to trigger a draw first, e.g. by calling [`draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")\
 or `plt.show()`.\
\
**dpi**float, optional\
\
The dpi value for computing the bbox, defaults to `self.get_figure(root=True).dpi` (_not_ the renderer dpi); should be set e.g. if to match regions with a figure saved with a custom dpi value.\
\
set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _anncoords\=<UNSET>_, _annotation\_clip\=<UNSET>_, _antialiased\=<UNSET>_, _backgroundcolor\=<UNSET>_, _bbox\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _fontfamily\=<UNSET>_, _fontfeatures\=<UNSET>_, _fontproperties\=<UNSET>_, _fontsize\=<UNSET>_, _fontstretch\=<UNSET>_, _fontstyle\=<UNSET>_, _fontvariant\=<UNSET>_, _fontweight\=<UNSET>_, _gid\=<UNSET>_, _horizontalalignment\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _language\=<UNSET>_, _linespacing\=<UNSET>_, _math\_fontfamily\=<UNSET>_, _mouseover\=<UNSET>_, _multialignment\=<UNSET>_, _parse\_math\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _rasterized\=<UNSET>_, _rotation\=<UNSET>_, _rotation\_mode\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _text\=<UNSET>_, _transform\=<UNSET>_, _transform\_rotates\_text\=<UNSET>_, _url\=<UNSET>_, _usetex\=<UNSET>_, _verticalalignment\=<UNSET>_, _visible\=<UNSET>_, _wrap\=<UNSET>_, _x\=<UNSET>_, _y\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.set "Link to this definition")\
\
Set multiple properties at once.\
\
a.set(a\=A, b\=B, c\=C)\
\
is equivalent to\
\
a.set\_a(A)\
a.set\_b(B)\
a.set\_c(C)\
\
In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.\
\
The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.\
\
Supported properties are\
\
> | Property | Description |\
> | --- | --- |\
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |\
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |\
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |\
> | [`anncoords`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.set_anncoords "matplotlib.text.Annotation.set_anncoords") | unknown |\
> | `annotation_clip` | bool or None |\
> | [`antialiased`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "matplotlib.text.Text.set_antialiased") | bool |\
> | [`backgroundcolor`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "matplotlib.text.Text.set_backgroundcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |\
> | [`bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox") | dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br> or None |\
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |\
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |\
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |\
> | [`color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")<br> or [`c`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |\
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | unknown |\
> | [`fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`family`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily") | {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'} |\
> | [`fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "matplotlib.text.Text.set_fontfeatures") | list of str, or tuple of str, or None |\
> | [`fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font_properties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties") | [`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")<br> or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")<br> or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") |\
> | [`fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")<br> or [`size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize") | float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} |\
> | [`fontstretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch")<br> or [`stretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch") | {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'} |\
> | [`fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle")<br> or [`style`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle") | {'normal', 'italic', 'oblique'} |\
> | [`fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant")<br> or [`variant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant") | {'normal', 'small-caps'} |\
> | [`fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight")<br> or [`weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight") | {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'} |\
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |\
> | [`horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")<br> or [`ha`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment") | {'left', 'center', 'right'} |\
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |\
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |\
> | [`language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "matplotlib.text.Text.set_language") | str or None |\
> | [`linespacing`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing "matplotlib.text.Text.set_linespacing") | 'normal' or float, default: 'normal' |\
> | [`math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily") | str |\
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |\
> | [`multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment")<br> or [`ma`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment") | {'left', 'right', 'center'} |\
> | [`parse_math`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math "matplotlib.text.Text.set_parse_math") | bool |\
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |\
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |\
> | [`position`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "matplotlib.text.Text.set_position") | (float, float) |\
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |\
> | [`rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation") | float or {'vertical', 'horizontal'} |\
> | [`rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode") | {None, 'default', 'anchor', 'xtick', 'ytick'} |\
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |\
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |\
> | [`text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text") | object |\
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |\
> | [`transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text") | bool |\
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |\
> | [`usetex`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex "matplotlib.text.Text.set_usetex") | bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) |\
> | [`verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")<br> or [`va`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment") | {'baseline', 'bottom', 'center', 'center\_baseline', 'top'} |\
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |\
> | [`wrap`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap "matplotlib.text.Text.set_wrap") | bool |\
> | [`x`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x "matplotlib.text.Text.set_x") | float |\
> | [`y`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y "matplotlib.text.Text.set_y") | float |\
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |\
\
set\_anncoords(_coords_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2122-L2128)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.set_anncoords "Link to this definition")\
\
Set the coordinate system to use for [`Annotation.xyann`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.xyann "matplotlib.text.Annotation.xyann")\
.\
\
See also _xycoords_ in [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
.\
\
set\_figure(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2133-L2137)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.set_figure "Link to this definition")\
\
Set the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")\
 instance the artist belongs to.\
\
Warning\
\
This function should typically not be called by users.\
\
This is a low-level API and only modifies the internal state of the Artist. Only modifying this is not enough and will typically lead to an inconsistent state, because the state of the figure has to be changed as well.\
\
Users should typically instead call one of the high-level APIs, i.e. [`Figure.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")\
 or one of the Axes methods [Adding artists](https://matplotlib.org/stable/api/axes_api.html#axes-api-adding-artists)\
.\
\
Parameters:\
\
**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")\
\
update\_positions(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L2139-L2202)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.update_positions "Link to this definition")\
\
Update the pixel positions of the annotation text and the arrow patch.\
\
property xyann[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.xyann "Link to this definition")\
\
The text position.\
\
See also _xytext_ in [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
.\
\
property xycoords[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.xycoords "Link to this definition")\
\
class matplotlib.text.OffsetFrom(_artist_, _ref\_coord_, _unit\='points'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1605-L1676)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "Link to this definition")\
\
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")\
\
Callable helper class for working with [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
.\
\
Parameters:\
\
**artist**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
 or [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")\
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
\
The object to compute the offset from.\
\
**ref\_coord**(float, float)\
\
If _artist_ is an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
 or [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")\
, this values is the location to of the offset origin in fractions of the _artist_ bounding box.\
\
If _artist_ is a transform, the offset origin is the transform applied to this value.\
\
**unit**{'points, 'pixels'}, default: 'points'\
\
The screen units to use (pixels or points) for the offset input.\
\
get\_unit()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1642-L1644)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom.get_unit "Link to this definition")\
\
Return the unit for input to the transform used by `__call__`.\
\
set\_unit(_unit_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/text.py#L1631-L1640)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom.set_unit "Link to this definition")\
\
Set the unit for input to the transform used by `__call__`.\
\
Parameters:\
\
**unit**{'points', 'pixels'}\
\
class matplotlib.text.TextPath(_xy_, _s_, _size\=None_, _prop\=None_, _\_interpolation\_steps\=1_, _usetex\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L272-L376)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "Link to this definition")\
\
Bases: [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
\
Create a path from the text.\
\
Create a path from the text. Note that it simply is a path, not an artist. You need to use the [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")\
 (or other artists) to draw this path onto the canvas.\
\
Parameters:\
\
**xy**tuple or array of two float values\
\
Position of the text. For no offset, use `xy=(0, 0)`.\
\
**s**str\
\
The text to convert to a path.\
\
**size**float, optional\
\
Font size in points. Defaults to the size specified via the font properties _prop_.\
\
**prop**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")\
, optional\
\
Font property. If not provided, will use a default [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")\
 with parameters from the [rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-dynamic-rc-settings)\
.\
\
**\_interpolation\_steps**int, optional\
\
(Currently ignored)\
\
**usetex**bool, default: False\
\
Whether to use tex rendering.\
\
Examples\
\
The following creates a path from the string "ABC" with Helvetica font face; and another path from the latex fraction 1/2:\
\
from matplotlib.text import TextPath\
from matplotlib.font\_manager import FontProperties\
\
fp \= FontProperties(family\="Helvetica", style\="italic")\
path1 \= TextPath((12, 12), "ABC", size\=12, prop\=fp)\
path2 \= TextPath((0, 0), r"$\\frac{1}{2}$", size\=12, usetex\=True)\
\
Also see [Using a text as a Path](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html)\
.\
\
property codes[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath.codes "Link to this definition")\
\
Return the codes\
\
get\_size()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L344-L346)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath.get_size "Link to this definition")\
\
Get the text size.\
\
set\_size(_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L339-L342)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath.set_size "Link to this definition")\
\
Set the text size.\
\
property vertices[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath.vertices "Link to this definition")\
\
Return the cached path after updating it if necessary.\
\
class matplotlib.text.TextToPath[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L20-L266)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath "Link to this definition")\
\
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")\
\
A class that converts strings to paths.\
\
DPI \= 72[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.DPI "Link to this definition")\
\
FONT\_SCALE \= 100.0[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.FONT_SCALE "Link to this definition")\
\
get\_glyphs\_mathtext(_prop_, _s_, _glyph\_map\=None_, _return\_new\_glyphs\_only\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L167-L216)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.get_glyphs_mathtext "Link to this definition")\
\
Parse mathtext string _s_ and convert it to a (vertices, codes) pair.\
\
get\_glyphs\_tex(_prop_, _s_, _glyph\_map\=None_, _return\_new\_glyphs\_only\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L218-L266)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.get_glyphs_tex "Link to this definition")\
\
Convert the string _s_ to vertices and codes using usetex mode.\
\
get\_glyphs\_with\_font(_font_, _s_, _glyph\_map\=None_, _return\_new\_glyphs\_only\=False_, _\*_, _features\=None_, _language\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L134-L165)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.get_glyphs_with_font "Link to this definition")\
\
Convert string _s_ to vertices and codes using the provided ttf font.\
\
get\_text\_path(_prop_, _s_, _ismath\=False_, _\*_, _features\=None_, _language\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L70-L132)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.get_text_path "Link to this definition")\
\
Convert text _s_ to path (a tuple of vertices and codes for matplotlib.path.Path).\
\
Parameters:\
\
**prop**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")\
\
The font properties for the text.\
\
**s**str\
\
The text to be converted.\
\
**ismath**{False, True, "TeX"}\
\
If True, use mathtext parser. If "TeX", use tex for rendering.\
\
**language**str, optional\
\
The language of the text in a format accepted by libraqm, namely [a BCP47 language code](https://www.w3.org/International/articles/language-tags/)\
.\
\
Returns:\
\
**verts**list\
\
A list of arrays containing the (x, y) coordinates of the vertices.\
\
**codes**list\
\
A list of path codes.\
\
Examples\
\
Create a list of vertices and codes from a text, and create a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 from those:\
\
from matplotlib.path import Path\
from matplotlib.text import TextToPath\
from matplotlib.font\_manager import FontProperties\
\
fp \= FontProperties(family\="Comic Neue", style\="italic")\
verts, codes \= TextToPath().get\_text\_path(fp, "ABC")\
path \= Path(verts, codes, closed\=False)\
\
Also see [`TextPath`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "matplotlib.text.TextPath")\
 for a more direct way to create a path from a text.\
\
get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/textpath.py#L46-L68)\
[#](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextToPath.get_text_width_height_descent "Link to this definition")\
\
On this page