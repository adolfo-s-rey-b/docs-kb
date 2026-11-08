[Skip to main content](https://matplotlib.org/stable/api/table_api.html#main-content)

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
    

`matplotlib.table`[#](https://matplotlib.org/stable/api/table_api.html#module-matplotlib.table "Link to this heading")

=======================================================================================================================

Tables drawing.

Note

The table implementation in Matplotlib is lightly maintained. For a more featureful table implementation, you may wish to try [blume](https://github.com/swfiua/blume)
.

Use the factory function [`table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.table "matplotlib.table.table")
 to create a ready-made table from texts. If you need more control, use the [`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 class and its methods.

The table consists of a grid of cells, which are indexed by (row, column). The cell (0, 0) is positioned at the top left.

Thanks to John Gill for providing the class and table.

class matplotlib.table.Cell(_xy_, _width_, _height_, _\*_, _edgecolor\='k'_, _facecolor\='w'_, _fill\=True_, _text\=''_, _loc\='right'_, _fontproperties\=None_, _visible\_edges\='closed'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L39-L233)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "Link to this definition")

Bases: [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

A cell is a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 with some associated [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

As a user, you'll most likely not creates cells yourself. Instead, you should use either the [`table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.table "matplotlib.table.table")
 factory function or [`Table.add_cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.add_cell "matplotlib.table.Table.add_cell")
.

Parameters:

**xy**2-tuple

The position of the bottom left corner of the cell.

**width**float

The cell width.

**height**float

The cell height.

**edgecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'k'

The color of the cell border.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'w'

The cell facecolor.

**fill**bool, default: True

Whether the cell background is filled.

**text**str, optional

The cell text.

**loc**{'right', 'center', 'left'}

The alignment of the text within the cell.

**fontproperties**dict, optional

A dict defining the font properties of the text. Supported keys and values are the keyword arguments accepted by [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
.

**visible\_edges**{'closed', 'open', 'horizontal', 'vertical'} or substring of 'BRTL'

The cell edges to be drawn with a line: a substring of 'BRTL' (bottom, right, top, left), or one of 'open' (no edges drawn), 'closed' (all edges drawn), 'horizontal' (bottom and top), 'vertical' (right and left).

PAD \= 0.1[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.PAD "Link to this definition")

Padding between text and rectangle.

auto\_set\_font\_size(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L130-L139)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.auto_set_font_size "Link to this definition")

Shrink font size until the text fits into the cell width.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L141-L150)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_fontsize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L126-L128)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.get_fontsize "Link to this definition")

Return the cell fontsize.

get\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L221-L233)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.get_path "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for the [`visible_edges`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.visible_edges "matplotlib.table.Cell.visible_edges")
.

get\_required\_width(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L175-L178)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.get_required_width "Link to this definition")

Return the minimal required width for the cell.

get\_text()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L117-L119)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.get_text "Link to this definition")

Return the cell [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance.

get\_text\_bounds(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L167-L173)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.get_text_bounds "Link to this definition")

Return the text bounds as _(x, y, width, height)_ in table coordinates.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _angle\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _bounds\=<UNSET>_, _capstyle\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _edgegapcolor\=<UNSET>_, _facecolor\=<UNSET>_, _fill\=<UNSET>_, _fontsize\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _text\_props\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _x\=<UNSET>_, _xy\=<UNSET>_, _y\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set "Link to this definition")

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
> | [`angle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_angle "matplotlib.patches.Rectangle.set_angle") | unknown |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
> | [`bounds`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_bounds "matplotlib.patches.Rectangle.set_bounds") | (left, bottom, width, height) |
> | [`capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "matplotlib.patches.Patch.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | unknown |
> | [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "matplotlib.patches.Patch.set_fill") | bool |
> | [`fontsize`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set_fontsize "matplotlib.table.Cell.set_fontsize") | unknown |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "matplotlib.patches.Patch.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "matplotlib.patches.Patch.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' or None |
> | [`height`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_height "matplotlib.patches.Rectangle.set_height") | unknown |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "matplotlib.patches.Patch.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth") | float or None |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`text_props`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set_text_props "matplotlib.table.Cell.set_text_props") | unknown |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | unknown |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_width "matplotlib.patches.Rectangle.set_width") | unknown |
> | [`x`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_x "matplotlib.patches.Rectangle.set_x") | unknown |
> | [`xy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_xy "matplotlib.patches.Rectangle.set_xy") | (float, float) |
> | [`y`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_y "matplotlib.patches.Rectangle.set_y") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_figure(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L113-L115)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set_figure "Link to this definition")

Set the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 instance the artist belongs to.

Warning

This function should typically not be called by users.

This is a low-level API and only modifies the internal state of the Artist. Only modifying this is not enough and will typically lead to an inconsistent state, because the state of the figure has to be changed as well.

Users should typically instead call one of the high-level APIs, i.e. [`Figure.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
 or one of the Axes methods [Adding artists](https://matplotlib.org/stable/api/axes_api.html#axes-api-adding-artists)
.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

set\_fontsize(_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L121-L124)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set_fontsize "Link to this definition")

Set the text fontsize.

set\_text\_props(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L180-L190)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set_text_props "Link to this definition")

Update the text properties.

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

set\_transform(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L108-L111)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.set_transform "Link to this definition")

Set the artist transform.

Parameters:

**t**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

property visible\_edges[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.visible_edges "Link to this definition")

The cell edges to be drawn with a line.

Reading this property returns a substring of 'BRTL' (bottom, right, top, left').

When setting this property, you can use a substring of 'BRTL' or one of {'open', 'closed', 'horizontal', 'vertical'}.

matplotlib.table.CustomCell[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L39-L233)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.CustomCell "Link to this definition")

alias of [`Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")

class matplotlib.table.Table(_ax_, _loc\=None_, _bbox\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L239-L654)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

A table of cells.

Note

`table()` has some fundamental design limitations and will not be developed further. If you need more functionality, consider [blume](https://github.com/swfiua/blume)
.

The table consists of a grid of cells, which are indexed by (row, column).

For a simple table, you'll have a full grid of cells with indices from (0, 0) to (num\_rows-1, num\_cols-1), in which the cell (0, 0) is positioned at the top left. However, you can also add cells with negative indices. You don't have to add a cell to every grid position, so you can create tables that have holes.

_Note_: You'll usually not create an empty table from scratch. Instead use [`table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.table "matplotlib.table.table")
 to create a table from data.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to plot the table into.

**loc**str, optional

The position of the cell with respect to _ax_. This must be one of the [`codes`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.codes "matplotlib.table.Table.codes")
.

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or \[xmin, ymin, width, height\], optional

A bounding box to draw the table into. If this is not _None_, this overrides _loc_.

Other Parameters:

**\*\*kwargs**

[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 properties.

AXESPAD \= 0.02[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.AXESPAD "Link to this definition")

The border between the Axes and the table edge in Axes units.

FONTSIZE \= 10[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.FONTSIZE "Link to this definition")

add\_cell(_row_, _col_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L331-L353)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.add_cell "Link to this definition")

Create a cell and add it to the table.

Parameters:

**row**int

Row index.

**col**int

Column index.

**\*args, \*\*kwargs**

All other parameters are passed on to [`Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")
.

Returns:

[`Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")

The created cell.

auto\_set\_column\_width(_col_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L497-L512)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.auto_set_column_width "Link to this definition")

Automatically set the widths of given columns to optimal sizes.

Parameters:

**col**int or sequence of ints

The indices of the columns to auto-scale.

auto\_set\_font\_size(_value\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L522-L525)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.auto_set_font_size "Link to this definition")

Automatically set font size.

codes \= {'best': 0, 'bottom': 17, 'bottom left': 12, 'bottom right': 13, 'center': 9, 'center left': 5, 'center right': 6, 'left': 15, 'lower center': 7, 'lower left': 3, 'lower right': 4, 'right': 14, 'top': 16, 'top left': 11, 'top right': 10, 'upper center': 8, 'upper left': 2, 'upper right': 1}[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.codes "Link to this definition")

Possible values where to place the table relative to the Axes.

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L437-L451)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.contains "Link to this definition")

Test whether the artist contains the mouse event.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

An artist-specific dictionary of details of the event context, such as which points are contained in the pick radius. See the individual Artist subclasses for details.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L403-L423)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

property edges[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.edges "Link to this definition")

The default value of [`visible_edges`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.visible_edges "matplotlib.table.Cell.visible_edges")
 for newly added cells using [`add_cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.add_cell "matplotlib.table.Table.add_cell")
.

Notes

This setting does currently only affect newly created cells using [`add_cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.add_cell "matplotlib.table.Table.add_cell")
.

To change existing cells, you have to set their edges explicitly:

for c in tab.get\_celld().values():
    c.visible\_edges \= 'horizontal'

get\_celld()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L641-L654)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.get_celld "Link to this definition")

Return a dict of cells in the table mapping _(row, column)_ to [`Cell`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell "matplotlib.table.Cell")
s.

Notes

You can also directly index into the Table object to access individual cells:

cell \= table\[row, col\]

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L453-L455)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.get_children "Link to this definition")

Return the Artists contained by the table.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L457-L464)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.get_window_extent "Link to this definition")

Get the artist's bounding box in display space, ignoring clipping.

The bounding box's width and height are non-negative.

Subclasses should override for inclusion in the bounding box "tight" calculation. Default is to return an empty bounding box at 0, 0.

Warning

The extent can change due to any changes in the transform stack, such as changing the Axes limits, the figure size, the canvas used (as is done when saving a figure), or the DPI.

Relying on a once-retrieved window extent can lead to unexpected behavior in various cases such as interactive figures being resized or moved to a screen with different dpi, or figures that look fine on screen render incorrectly when saved to file.

To get accurate results you may need to manually call [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 or [`draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
 to have Matplotlib compute the rendered size.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

See also

[`Artist.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "matplotlib.artist.Artist.get_tightbbox")

Get the artist bounding box, taking clipping into account.

scale(_xscale_, _yscale_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L545-L549)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.scale "Link to this definition")

Scale column widths by _xscale_ and row heights by _yscale_.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _fontsize\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.set "Link to this definition")

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
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fontsize`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.set_fontsize "matplotlib.table.Table.set_fontsize") | float |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
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

set\_fontsize(_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L551-L574)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.set_fontsize "Link to this definition")

Set the font size, in points, of the cell text.

Parameters:

**size**float

Notes

As long as auto font size has not been disabled, the value will be clipped such that the text fits horizontally into the cell.

You can disable this behavior using [`auto_set_font_size`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.auto_set_font_size "matplotlib.table.Table.auto_set_font_size")
.

\>>> the\_table.auto\_set\_font\_size(False)
\>>> the\_table.set\_fontsize(20)

However, there is no automatic scaling of the row height so that the text may exceed the cell boundary.

matplotlib.table.table(_ax_, _cellText\=None_, _cellColours\=None_, _cellLoc\='right'_, _colWidths\=None_, _rowLabels\=None_, _rowColours\=None_, _rowLoc\='left'_, _colLabels\=None_, _colColours\=None_, _colLoc\='center'_, _loc\='bottom'_, _bbox\=None_, _edges\='closed'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/table.py#L657-L859)
[#](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.table "Link to this definition")

Add a table to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

Note

`table()` has some fundamental design limitations and will not be developed further. If you need more functionality, consider [blume](https://github.com/swfiua/blume)
.

At least one of _cellText_ or _cellColours_ must be specified. These parameters must be 2D lists, in which the outer lists define the rows and the inner list define the column values per row. Each row must have the same number of elements.

The table can optionally have row and column headers, which are configured using _rowLabels_, _rowColours_, _rowLoc_ and _colLabels_, _colColours_, _colLoc_ respectively.

For finer grained control over tables, use the [`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 class and add it to the Axes with [`Axes.add_table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_table.html#matplotlib.axes.Axes.add_table "matplotlib.axes.Axes.add_table")
.

Parameters:

**cellText**2D list of str or pandas.DataFrame, optional

The texts to place into the table cells.

_Note_: Line breaks in the strings are currently not accounted for and will result in the text exceeding the cell boundaries.

**cellColours**2D list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The background colors of the cells.

**cellLoc**{'right', 'center', 'left'}

The alignment of the text within the cells.

**colWidths**list of float, optional

The column widths in units of the axes. If not given, all columns will have a width of _1 / ncols_.

**rowLabels**list of str, optional

The text of the row header cells.

**rowColours**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the row header cells.

**rowLoc**{'left', 'center', 'right'}

The text alignment of the row header cells.

**colLabels**list of str, optional

The text of the column header cells.

**colColours**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the column header cells.

**colLoc**{'center', 'left', 'right'}

The text alignment of the column header cells.

**loc**str, default: 'bottom'

The position of the cell with respect to _ax_. This must be one of the [`codes`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.codes "matplotlib.table.Table.codes")
.

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or \[xmin, ymin, width, height\], optional

A bounding box to draw the table into. If this is not _None_, this overrides _loc_.

**edges**{'closed', 'open', 'horizontal', 'vertical'} or substring of 'BRTL'

The cell edges to be drawn with a line. See also [`visible_edges`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.visible_edges "matplotlib.table.Cell.visible_edges")
.

Returns:

[`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")

The created table.

Other Parameters:

**\*\*kwargs**

[`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 properties.

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fontsize`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.set_fontsize "matplotlib.table.Table.set_fontsize") | float |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
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

On this page