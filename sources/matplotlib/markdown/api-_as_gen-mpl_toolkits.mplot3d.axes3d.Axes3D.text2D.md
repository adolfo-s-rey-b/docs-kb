[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.text2D[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#mpl-toolkits-mplot3d-axes3d-axes3d-text2d "Link to this heading")

=========================================================================================================================================================================================================

Axes3D.text2D(_x_, _y_, _s_, _fontdict\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L652-L729)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text2D "Link to this definition")

Add text to the Axes.

Add the text _s_ to the Axes at location _x_, _y_ in data coordinates, with a default `horizontalalignment` on the `left` and `verticalalignment` at the `baseline`. See [Text alignment](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html)
.

Parameters:

**x, y**float

The position to place the text. By default, this is in data coordinates. The coordinate system can be changed using the _transform_ parameter.

**s**str

The text.

**fontdict**dict, default: None

Discouraged

The use of _fontdict_ is discouraged. Parameters should be passed as individual keyword arguments or using dictionary-unpacking `text(..., **fontdict)`.

A dictionary to override the default text properties. If fontdict is None, the defaults are determined by [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

Returns:

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The created [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance.

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

Other miscellaneous text parameters.

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "matplotlib.text.Text.set_antialiased") | bool |
| [`backgroundcolor`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "matplotlib.text.Text.set_backgroundcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox") | dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br> or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | unknown |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | unknown |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | unknown |
| [`color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")<br> or [`c`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`family`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily") | {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'} |
| [`fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "matplotlib.text.Text.set_fontfeatures") | list of str, or tuple of str, or None |
| [`fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font_properties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties") | [`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")<br> or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")<br> or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") |
| [`fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")<br> or [`size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize") | float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} |
| [`fontstretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch")<br> or [`stretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch") | {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'} |
| [`fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle")<br> or [`style`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle") | {'normal', 'italic', 'oblique'} |
| [`fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant")<br> or [`variant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant") | {'normal', 'small-caps'} |
| [`fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight")<br> or [`weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight") | {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'} |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")<br> or [`ha`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment") | {'left', 'center', 'right'} |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "matplotlib.text.Text.set_language") | str or None |
| [`linespacing`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing "matplotlib.text.Text.set_linespacing") | 'normal' or float, default: 'normal' |
| [`math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily") | str |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment")<br> or [`ma`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment") | {'left', 'right', 'center'} |
| [`parse_math`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math "matplotlib.text.Text.set_parse_math") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "matplotlib.text.Text.set_position") | (float, float) |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation") | float or {'vertical', 'horizontal'} |
| [`rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode") | {None, 'default', 'anchor', 'xtick', 'ytick'} |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text") | object |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text") | bool |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`usetex`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex "matplotlib.text.Text.set_usetex") | bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) |
| [`verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")<br> or [`va`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment") | {'baseline', 'bottom', 'center', 'center\_baseline', 'top'} |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`wrap`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap "matplotlib.text.Text.set_wrap") | bool |
| [`x`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x "matplotlib.text.Text.set_x") | float |
| [`y`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y "matplotlib.text.Text.set_y") | float |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Examples

Individual keyword arguments can be used to override any given parameter:

\>>> text(x, y, s, fontsize\=12)

The default transform specifies that text is in data coords, alternatively, you can specify text in axis coords ((0, 0) is lower-left and (1, 1) is upper-right). The example below places text in the center of the Axes:

\>>> text(0.5, 0.5, 'matplotlib', horizontalalignment\='center',
...      verticalalignment\='center', transform\=ax.transAxes)

You can put a rectangular box around the text instance (e.g., to set a background color) by using the keyword _bbox_. _bbox_ is a dictionary of [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 properties. For example:

\>>> text(x, y, s, bbox\=dict(facecolor\='red', alpha\=0.5))

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.text2D`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-text2d "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

On this page