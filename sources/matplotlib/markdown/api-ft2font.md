[Skip to main content](https://matplotlib.org/stable/api/ft2font.html#main-content)

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
    

`matplotlib.ft2font`[#](https://matplotlib.org/stable/api/ft2font.html#module-matplotlib.ft2font "Link to this heading")

=========================================================================================================================

class matplotlib.ft2font.FT2Font(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _filename: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")
_, _hinting\_factor: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _\*_, _face\_index: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
 \= 0_, _\_fallback\_list: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")
\[[matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")\
\] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _\_kerning\_factor: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _\_warn\_if\_used: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "Link to this definition")

Bases:

An object representing a single font face.

Outside of the font itself and querying its properties, this object provides methods for processing text strings into glyph shapes.

Commonly, one will use [`FT2Font.set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")
 to load some glyph metrics and outlines. Then [`FT2Font.draw_glyphs_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap")
 and [`FT2Font.get_image`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_image "matplotlib.ft2font.FT2Font.get_image")
 may be used to get a rendered form of the loaded string.

For single characters, [`FT2Font.load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")
 or [`FT2Font.load_glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_glyph "matplotlib.ft2font.FT2Font.load_glyph")
 may be used, either directly for their return values, or to use [`FT2Font.draw_glyph_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap")
 or [`FT2Font.get_path`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_path "matplotlib.ft2font.FT2Font.get_path")
.

Useful metrics may be examined via the [`Glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "matplotlib.ft2font.Glyph")
 return values or [`FT2Font.get_kerning`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "matplotlib.ft2font.FT2Font.get_kerning")
. Most dimensions are given in 26.6 or 16.6 fixed-point integers representing subpixels. Divide these values by 64 to produce floating-point pixels.

Parameters:

**filename**str, bytes, os.PathLike, or io.BinaryIO

The source of the font data in a format (ttf or ttc) that FreeType can read.

**face\_index**int, optional

The index of the face in the font file to load.

**\_fallback\_list**list of FT2Font, optional

A list of FT2Font objects used to find missing glyphs.

Warning

This API is both private and provisional: do not use it directly.

**\_warn\_if\_used**bool, optional

Used to trigger missing glyph warnings.

Warning

This API is private: do not use it directly.

property ascender[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.ascender "Link to this definition")

Ascender in 26.6 units.

property bbox[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.bbox "Link to this definition")

Face global bounding box (xmin, ymin, xmax, ymax).

clear(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.clear "Link to this definition")

Clear all the glyphs, reset for a new call to [`set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")
.

property descender[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.descender "Link to this definition")

Descender in 26.6 units.

draw\_glyph\_to\_bitmap()[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap "Link to this definition")

Draw a single glyph to the bitmap at pixel locations x, y.

Note it is your responsibility to create the image manually with the correct size before this call is made.

If you want automatic layout, use [`set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")
 in combinations with [`draw_glyphs_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap")
. This function is instead intended for people who want to render individual glyphs (e.g., returned by [`load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")
) at precise locations.

Parameters:

**image**2d array of uint8

The image buffer on which to draw the glyph.

**x, y**int

The position of the glyph's top left corner.

**glyph**Glyph

The glyph to draw.

**antialiased**bool, default: True

Whether to render glyphs 8-bit antialiased or in pure black-and-white.

See also

[`draw_glyphs_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap")

draw\_glyphs\_to\_bitmap(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _\*_, _antialiased: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap "Link to this definition")

Draw the glyphs that were loaded by [`set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")
 to the bitmap.

The bitmap size will be automatically set to include the glyphs.

Parameters:

**antialiased**bool, default: True

Whether to render glyphs 8-bit antialiased or in pure black-and-white.

See also

[`draw_glyph_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap")

property face\_flags[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.face_flags "Link to this definition")

Face flags; see [`FaceFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
.

property face\_index[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.face_index "Link to this definition")

The index of the font in the file.

property family\_name[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.family_name "Link to this definition")

Face family name.

property fname[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.fname "Link to this definition")

The original filename for this object.

get\_bitmap\_offset(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")\
, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")\
\][#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_bitmap_offset "Link to this definition")

Get the (x, y) offset for the bitmap if ink hangs left or below (0, 0).

Since Matplotlib only supports left-to-right text, y is always 0.

Returns:

**x, y**float

The x and y offset in 26.6 subpixels of the bitmap. To get x and y in pixels, divide these values by 64.

See also

[`get_width_height`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_width_height "matplotlib.ft2font.FT2Font.get_width_height")

[`get_descent`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_descent "matplotlib.ft2font.FT2Font.get_descent")

get\_char\_index(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _codepoint: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_, _\*_, _\_fallback: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_char_index "Link to this definition")

Return the glyph index corresponding to a character code point.

Parameters:

**codepoint**int

A character code point in the current charmap (which defaults to Unicode.)

**\_fallback**bool

Whether to enable fallback fonts while searching for a character.

Returns:

int

The corresponding glyph index.

See also

[`set_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_charmap "matplotlib.ft2font.FT2Font.set_charmap")

[`select_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.select_charmap "matplotlib.ft2font.FT2Font.select_charmap")

[`get_glyph_name`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_glyph_name "matplotlib.ft2font.FT2Font.get_glyph_name")

[`get_name_index`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_name_index "matplotlib.ft2font.FT2Font.get_name_index")

get\_charmap(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_charmap "Link to this definition")

Return a mapping of character codes to glyph indices in the font.

The charmap is Unicode by default, but may be changed by [`set_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_charmap "matplotlib.ft2font.FT2Font.set_charmap")
 or [`select_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.select_charmap "matplotlib.ft2font.FT2Font.select_charmap")
.

Returns:

dict\[int, int\]

A dictionary of the selected charmap mapping character codes to their corresponding glyph indices.

get\_descent(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_descent "Link to this definition")

Get the descent of the current string set by [`set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")
.

The rotation of the string is accounted for.

Returns:

int

The descent in 26.6 subpixels of the bitmap. To get the descent in pixels, divide these values by 64.

See also

[`get_bitmap_offset`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_bitmap_offset "matplotlib.ft2font.FT2Font.get_bitmap_offset")

[`get_width_height`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_width_height "matplotlib.ft2font.FT2Font.get_width_height")

get\_glyph\_name(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _index: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_glyph_name "Link to this definition")

Retrieve the ASCII name of a given glyph _index_ in a face.

Due to Matplotlib's internal design, for fonts that do not contain glyph names (per `FT_FACE_FLAG_GLYPH_NAMES`), this returns a made-up name which does _not_ roundtrip through [`get_name_index`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_name_index "matplotlib.ft2font.FT2Font.get_name_index")
.

Parameters:

**index**int

The glyph number to query.

Returns:

str

The name of the glyph, or if the font does not contain names, a name synthesized by Matplotlib.

See also

[`get_name_index`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_name_index "matplotlib.ft2font.FT2Font.get_name_index")

get\_image(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → numpy.typing.NDArray\[numpy.uint8\][#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_image "Link to this definition")

Return the underlying image buffer for this font object.

Returns:

np.ndarray\[int\]

See also

[`get_path`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_path "matplotlib.ft2font.FT2Font.get_path")

get\_kerning(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _left: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_, _right: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_, _mode: [Kerning](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
 | [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "Link to this definition")

Get the kerning between two glyphs.

Parameters:

**left, right**int

The glyph indices. Note these are not characters nor character codes. Use [`get_char_index`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_char_index "matplotlib.ft2font.FT2Font.get_char_index")
 to convert character codes to glyph indices.

**mode**Kerning

A kerning mode constant:

*   `DEFAULT` - Return scaled and grid-fitted kerning distances.
    
*   `UNFITTED` - Return scaled but un-grid-fitted kerning distances.
    
*   `UNSCALED` - Return the kerning vector in original font units.
    

Changed in version 3.10: This now takes a [`ft2font.Kerning`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
 value instead of an [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
.

Returns:

int

The kerning adjustment between the two glyphs.

get\_name\_index(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
_) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_name_index "Link to this definition")

Return the glyph index of a given glyph _name_.

Parameters:

**name**str

The name of the glyph to query.

Returns:

int

The corresponding glyph index; 0 means 'undefined character code'.

See also

[`get_char_index`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_char_index "matplotlib.ft2font.FT2Font.get_char_index")

[`get_glyph_name`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_glyph_name "matplotlib.ft2font.FT2Font.get_glyph_name")

get\_num\_glyphs(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_num_glyphs "Link to this definition")

Return the number of loaded glyphs.

get\_path(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_path "Link to this definition")

Get the path data from the currently loaded glyph.

Returns:

**vertices**np.ndarray\[double\]

The (N, 2) array of vertices describing the current glyph.

**codes**np.ndarray\[np.uint8\]

The (N, ) array of codes corresponding to the vertices.

See also

[`get_image`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_image "matplotlib.ft2font.FT2Font.get_image")

[`load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")

[`load_glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_glyph "matplotlib.ft2font.FT2Font.load_glyph")

[`set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")

get\_ps\_font\_info(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_ps_font_info "Link to this definition")

Return the information in the PS Font Info structure.

For more information, see the [FreeType documentation on this structure](https://freetype.org/freetype2/docs/reference/ft2-type1_tables.html#ps_fontinforec)
.

Returns:

**version**str

**notice**str

**full\_name**str

**family\_name**str

**weight**str

**italic\_angle**int

**is\_fixed\_pitch**bool

**underline\_position**int

**underline\_thickness**int

get\_sfnt(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_sfnt "Link to this definition")

Load the entire SFNT names table.

Returns:

dict\[tuple\[int, int, int, int\], bytes\]

The SFNT names table; the dictionary keys are tuples of:

> (platform-ID, ISO-encoding-scheme, language-code, description)

and the values are the direct information from the font table.

get\_sfnt\_table(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
_) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_sfnt_table "Link to this definition")

Return one of the SFNT tables.

Parameters:

**name**{"head", "maxp", "OS/2", "hhea", "vhea", "post", "pclt"}

Which table to return.

Returns:

dict\[str, Any\]

The corresponding table; for more information, see [the FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-truetype_tables.html)
.

get\_width\_height(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
\[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")\
, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")\
\][#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_width_height "Link to this definition")

Get the dimensions of the current string set by [`set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")
.

The rotation of the string is accounted for.

Returns:

**width, height**float

The width and height in 26.6 subpixels of the current string. To get width and height in pixels, divide these values by 64.

See also

[`get_bitmap_offset`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_bitmap_offset "matplotlib.ft2font.FT2Font.get_bitmap_offset")

[`get_descent`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_descent "matplotlib.ft2font.FT2Font.get_descent")

property height[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.height "Link to this definition")

Height in 26.6 units; used to compute a default line spacing (baseline-to-baseline distance).

load\_char(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _charcode: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_, _flags: [LoadFlags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 | [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
 \= <LoadFlags.FORCE\_AUTOHINT: 32>_) → [matplotlib.ft2font.Glyph](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "matplotlib.ft2font.Glyph")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "Link to this definition")

Load character in current fontfile and set glyph.

Parameters:

**charcode**int

The character code to prepare rendering information for. This code must be in the charmap, or else a `.notdef` glyph may be returned instead.

**flags**LoadFlags, default: [`LoadFlags.FORCE_AUTOHINT`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT "matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT")

Any bitwise-OR combination of the [`LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 flags.

Changed in version 3.10: This now takes an [`ft2font.LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 instead of an int.

Returns:

Glyph

The glyph information corresponding to the specified character.

See also

[`load_glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_glyph "matplotlib.ft2font.FT2Font.load_glyph")

[`select_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.select_charmap "matplotlib.ft2font.FT2Font.select_charmap")

[`set_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_charmap "matplotlib.ft2font.FT2Font.set_charmap")

load\_glyph(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _glyph\_index: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_, _flags: [LoadFlags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 | [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
 \= <LoadFlags.FORCE\_AUTOHINT: 32>_) → [matplotlib.ft2font.Glyph](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "matplotlib.ft2font.Glyph")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_glyph "Link to this definition")

Load glyph index in current fontfile and set glyph.

Note that the glyph index is specific to a font, and not universal like a Unicode code point.

Parameters:

**glyph\_index**int

The glyph index to prepare rendering information for.

**flags**LoadFlags, default: [`LoadFlags.FORCE_AUTOHINT`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT "matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT")

Any bitwise-OR combination of the [`LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 flags.

Changed in version 3.10: This now takes an [`ft2font.LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 instead of an int.

Returns:

Glyph

The glyph information corresponding to the specified index.

See also

[`load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")

property max\_advance\_height[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.max_advance_height "Link to this definition")

Maximum vertical cursor advance for all glyphs.

property max\_advance\_width[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.max_advance_width "Link to this definition")

Maximum horizontal cursor advance for all glyphs.

property num\_charmaps[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_charmaps "Link to this definition")

Number of charmaps in the face.

property num\_faces[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_faces "Link to this definition")

Number of faces in file.

property num\_fixed\_sizes[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_fixed_sizes "Link to this definition")

Number of bitmap in the face.

property num\_glyphs[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_glyphs "Link to this definition")

Number of glyphs in the face.

property num\_named\_instances[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_named_instances "Link to this definition")

Number of named instances in the face.

property postscript\_name[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.postscript_name "Link to this definition")

PostScript name of the font.

property scalable[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.scalable "Link to this definition")

Whether face is scalable; attributes after this one are only defined for scalable faces.

select\_charmap(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _i: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.select_charmap "Link to this definition")

Select a charmap by its FT\_Encoding number.

For more details on character mapping, see the [FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-character_mapping.html)
.

Parameters:

**i**int

The charmap in the form defined by FreeType: [https://freetype.org/freetype2/docs/reference/ft2-character\_mapping.html#ft\_encoding](https://freetype.org/freetype2/docs/reference/ft2-character_mapping.html#ft_encoding)

See also

[`set_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_charmap "matplotlib.ft2font.FT2Font.set_charmap")

[`get_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_charmap "matplotlib.ft2font.FT2Font.get_charmap")

set\_charmap(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
_, _i: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")
_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_charmap "Link to this definition")

Make the i-th charmap current.

For more details on character mapping, see the [FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-character_mapping.html)
.

Parameters:

**i**int

The charmap number in the range \[0, [`num_charmaps`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_charmaps "matplotlib.ft2font.FT2Font.num_charmaps")\
).\
\
See also\
\
[`num_charmaps`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_charmaps "matplotlib.ft2font.FT2Font.num_charmaps")\
\
[`select_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.select_charmap "matplotlib.ft2font.FT2Font.select_charmap")\
\
[`get_charmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_charmap "matplotlib.ft2font.FT2Font.get_charmap")\
\
set\_size(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")\
_, _ptsize: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_, _dpi: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_size "Link to this definition")\
\
Set the size of the text.\
\
Parameters:\
\
**ptsize**float\
\
The size of the text in points.\
\
**dpi**float\
\
The DPI used for rendering the text.\
\
set\_text(_self: [matplotlib.ft2font.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")\
_, _string: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
_, _angle: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 \= 0.0_, _flags: [LoadFlags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")\
 | [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 \= <LoadFlags.FORCE\_AUTOHINT: 32>_, _\*_, _features: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")\
\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
\] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 \= None_, _language: collections.abc.Sequence\[tuple\[str_, _typing.SupportsInt | typing.SupportsIndex_, _typing.SupportsInt | typing.SupportsIndex\]\] | None | str\=None_) → numpy.typing.NDArray\[numpy.float64\][#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "Link to this definition")\
\
Set the text _string_ and _angle_.\
\
You must call this before [`draw_glyphs_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyphs_to_bitmap")\
.\
\
Parameters:\
\
**string**str\
\
The text to prepare rendering information for.\
\
**angle**float\
\
The angle at which to render the supplied text.\
\
**flags**LoadFlags, default: [`LoadFlags.FORCE_AUTOHINT`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT "matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT")\
\
Any bitwise-OR combination of the [`LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")\
 flags.\
\
Changed in version 3.10: This now takes an [`ft2font.LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")\
 instead of an int.\
\
**features**tuple\[str, ...\]\
\
The font feature tags to use for the font.\
\
Available font feature tags may be found at [https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist)\
\
Added in version 3.11.\
\
Returns:\
\
np.ndarray\[double\]\
\
A sequence of x,y glyph positions in 26.6 subpixels; divide by 64 for pixels.\
\
property style\_flags[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.style_flags "Link to this definition")\
\
Style flags; see [`StyleFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags "matplotlib.ft2font.StyleFlags")\
.\
\
property style\_name[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.style_name "Link to this definition")\
\
Style name.\
\
property underline\_position[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.underline_position "Link to this definition")\
\
Vertical position of the underline bar.\
\
property underline\_thickness[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.underline_thickness "Link to this definition")\
\
Thickness of the underline bar.\
\
property units\_per\_EM[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.units_per_EM "Link to this definition")\
\
Number of font units covered by the EM.\
\
class matplotlib.ft2font.FT2Image(_self: [matplotlib.ft2font.FT2Image](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image "matplotlib.ft2font.FT2Image")\
_, _width: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 | [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_, _height: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 | [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image "Link to this definition")\
\
Bases:\
\
An image buffer for drawing glyphs.\
\
Parameters:\
\
**width, height**int\
\
The dimensions of the image buffer.\
\
draw\_rect\_filled(_self: [matplotlib.ft2font.FT2Image](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image "matplotlib.ft2font.FT2Image")\
_, _x0: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 | [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_, _y0: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 | [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_, _x1: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 | [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_, _y1: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
 | [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.14)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.14)")\
_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image.draw_rect_filled "Link to this definition")\
\
Draw a filled rectangle to the image.\
\
Parameters:\
\
**x0, y0, x1, y1**float\
\
The bounds of the rectangle from (x0, y0) to (x1, y1).\
\
class matplotlib.ft2font.FaceFlags(_\*values_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "Link to this definition")\
\
Bases: [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "(in Python v3.14)")\
\
Flags returned by [`FT2Font.face_flags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.face_flags "matplotlib.ft2font.FT2Font.face_flags")\
.\
\
For more information, see [the FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-face_creation.html#ft_face_flag_xxx)\
.\
\
Added in version 3.10.\
\
CID\_KEYED \= 4096[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.CID_KEYED "Link to this definition")\
\
COLOR \= 16384[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.COLOR "Link to this definition")\
\
EXTERNAL\_STREAM \= 1024[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.EXTERNAL_STREAM "Link to this definition")\
\
FAST\_GLYPHS \= 128[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.FAST_GLYPHS "Link to this definition")\
\
FIXED\_SIZES \= 2[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.FIXED_SIZES "Link to this definition")\
\
FIXED\_WIDTH \= 4[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.FIXED_WIDTH "Link to this definition")\
\
GLYPH\_NAMES \= 512[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.GLYPH_NAMES "Link to this definition")\
\
HINTER \= 2048[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.HINTER "Link to this definition")\
\
HORIZONTAL \= 16[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.HORIZONTAL "Link to this definition")\
\
KERNING \= 64[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.KERNING "Link to this definition")\
\
MULTIPLE\_MASTERS \= 256[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.MULTIPLE_MASTERS "Link to this definition")\
\
SBIX \= 131072[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.SBIX "Link to this definition")\
\
SBIX\_OVERLAY \= 262144[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.SBIX_OVERLAY "Link to this definition")\
\
SCALABLE \= 1[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.SCALABLE "Link to this definition")\
\
SFNT \= 8[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.SFNT "Link to this definition")\
\
SVG \= 65536[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.SVG "Link to this definition")\
\
TRICKY \= 8192[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.TRICKY "Link to this definition")\
\
VARIATION \= 32768[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.VARIATION "Link to this definition")\
\
VERTICAL \= 32[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags.VERTICAL "Link to this definition")\
\
class matplotlib.ft2font.Glyph(_self: [matplotlib.ft2font.Glyph](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "matplotlib.ft2font.Glyph")\
_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "Link to this definition")\
\
Bases:\
\
Information about a single glyph.\
\
You cannot create instances of this object yourself, but must use [`FT2Font.load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")\
 or [`FT2Font.load_glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_glyph "matplotlib.ft2font.FT2Font.load_glyph")\
 to generate one. This object may be used in a call to [`FT2Font.draw_glyph_to_bitmap`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap "matplotlib.ft2font.FT2Font.draw_glyph_to_bitmap")\
.\
\
For more information on the various metrics, see [the FreeType documentation](https://freetype.org/freetype2/docs/glyphs/glyphs-3.html)\
.\
\
property bbox[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.bbox "Link to this definition")\
\
The control box of the glyph.\
\
property height[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.height "Link to this definition")\
\
The glyph's height.\
\
property horiAdvance[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.horiAdvance "Link to this definition")\
\
Advance width for horizontal layout.\
\
property horiBearingX[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.horiBearingX "Link to this definition")\
\
Left side bearing for horizontal layout.\
\
property horiBearingY[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.horiBearingY "Link to this definition")\
\
Top side bearing for horizontal layout.\
\
property linearHoriAdvance[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.linearHoriAdvance "Link to this definition")\
\
The advance width of the unhinted glyph.\
\
property vertAdvance[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.vertAdvance "Link to this definition")\
\
Advance height for vertical layout.\
\
property vertBearingX[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.vertBearingX "Link to this definition")\
\
Left side bearing for vertical layout.\
\
property vertBearingY[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.vertBearingY "Link to this definition")\
\
Top side bearing for vertical layout.\
\
property width[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.width "Link to this definition")\
\
The glyph's width.\
\
class matplotlib.ft2font.Kerning(_\*values_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "Link to this definition")\
\
Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")\
\
Kerning modes for [`FT2Font.get_kerning`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "matplotlib.ft2font.FT2Font.get_kerning")\
.\
\
For more information, see [the FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html#ft_kerning_mode)\
.\
\
Added in version 3.10.\
\
DEFAULT \= 0[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning.DEFAULT "Link to this definition")\
\
UNFITTED \= 1[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning.UNFITTED "Link to this definition")\
\
UNSCALED \= 2[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning.UNSCALED "Link to this definition")\
\
class matplotlib.ft2font.LayoutItem(_self: [matplotlib.ft2font.LayoutItem](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem "matplotlib.ft2font.LayoutItem")\
_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem "Link to this definition")\
\
Bases:\
\
property char[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem.char "Link to this definition")\
\
The character code for the item.\
\
property ft\_object[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem.ft_object "Link to this definition")\
\
The FT\_Face of the item.\
\
property glyph\_index[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem.glyph_index "Link to this definition")\
\
The glyph index for the item.\
\
property prev\_kern[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem.prev_kern "Link to this definition")\
\
The kerning between this item and the previous one.\
\
property x[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem.x "Link to this definition")\
\
The x position of the item.\
\
property y[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LayoutItem.y "Link to this definition")\
\
The y position of the item.\
\
class matplotlib.ft2font.LoadFlags(_\*values_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "Link to this definition")\
\
Bases: [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "(in Python v3.14)")\
\
Flags for [`FT2Font.load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")\
, [`FT2Font.load_glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_glyph "matplotlib.ft2font.FT2Font.load_glyph")\
, and [`FT2Font.set_text`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_text "matplotlib.ft2font.FT2Font.set_text")\
.\
\
For more information, see [the FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html#ft_load_xxx)\
.\
\
Added in version 3.10.\
\
BITMAP\_METRICS\_ONLY \= 4194304[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.BITMAP_METRICS_ONLY "Link to this definition")\
\
COLOR \= 1048576[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.COLOR "Link to this definition")\
\
COMPUTE\_METRICS \= 2097152[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.COMPUTE_METRICS "Link to this definition")\
\
CROP\_BITMAP \= 64[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.CROP_BITMAP "Link to this definition")\
\
DEFAULT \= 0[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.DEFAULT "Link to this definition")\
\
FORCE\_AUTOHINT \= 32[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.FORCE_AUTOHINT "Link to this definition")\
\
IGNORE\_GLOBAL\_ADVANCE\_WIDTH \= 512[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.IGNORE_GLOBAL_ADVANCE_WIDTH "Link to this definition")\
\
IGNORE\_TRANSFORM \= 2048[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.IGNORE_TRANSFORM "Link to this definition")\
\
LINEAR\_DESIGN \= 8192[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.LINEAR_DESIGN "Link to this definition")\
\
MONOCHROME \= 4096[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.MONOCHROME "Link to this definition")\
\
NO\_AUTOHINT \= 32768[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.NO_AUTOHINT "Link to this definition")\
\
NO\_BITMAP \= 8[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.NO_BITMAP "Link to this definition")\
\
NO\_HINTING \= 2[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.NO_HINTING "Link to this definition")\
\
NO\_RECURSE \= 1024[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.NO_RECURSE "Link to this definition")\
\
NO\_SCALE \= 1[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.NO_SCALE "Link to this definition")\
\
NO\_SVG \= 16777216[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.NO_SVG "Link to this definition")\
\
PEDANTIC \= 128[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.PEDANTIC "Link to this definition")\
\
RENDER \= 4[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.RENDER "Link to this definition")\
\
TARGET\_LCD \= 196608[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.TARGET_LCD "Link to this definition")\
\
TARGET\_LCD\_V \= 262144[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.TARGET_LCD_V "Link to this definition")\
\
TARGET\_LIGHT \= 65536[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.TARGET_LIGHT "Link to this definition")\
\
TARGET\_MONO \= 131072[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.TARGET_MONO "Link to this definition")\
\
TARGET\_NORMAL \= 0[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.TARGET_NORMAL "Link to this definition")\
\
VERTICAL\_LAYOUT \= 16[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags.VERTICAL_LAYOUT "Link to this definition")\
\
class matplotlib.ft2font.RenderMode(_\*values_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode "Link to this definition")\
\
Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")\
\
Render modes.\
\
For more information, see [the FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html#ft_render_mode)\
.\
\
Added in version 3.10.\
\
LCD \= 3[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode.LCD "Link to this definition")\
\
LCD\_V \= 4[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode.LCD_V "Link to this definition")\
\
LIGHT \= 1[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode.LIGHT "Link to this definition")\
\
MONO \= 2[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode.MONO "Link to this definition")\
\
NORMAL \= 0[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode.NORMAL "Link to this definition")\
\
SDF \= 5[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.RenderMode.SDF "Link to this definition")\
\
class matplotlib.ft2font.StyleFlags(_\*values_)[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags "Link to this definition")\
\
Bases: [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "(in Python v3.14)")\
\
Flags returned by [`FT2Font.style_flags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.style_flags "matplotlib.ft2font.FT2Font.style_flags")\
.\
\
For more information, see [the FreeType documentation](https://freetype.org/freetype2/docs/reference/ft2-face_creation.html#ft_style_flag_xxx)\
.\
\
Added in version 3.10.\
\
BOLD \= 2[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags.BOLD "Link to this definition")\
\
ITALIC \= 1[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags.ITALIC "Link to this definition")\
\
NORMAL \= 0[#](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags.NORMAL "Link to this definition")\
\
On this page