[Skip to main content](https://matplotlib.org/stable/api/_type1font.html#main-content)

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
    

`matplotlib._type1font`[#](https://matplotlib.org/stable/api/_type1font.html#module-matplotlib._type1font "Link to this heading")

==================================================================================================================================

A class representing a Type 1 font.

This version reads pfa and pfb files and splits them for embedding in pdf files. It also supports SlantFont and ExtendFont transformations, similarly to pdfTeX and friends.

Usage:

font \= Type1Font(filename)
clear\_part, encrypted\_part, finale \= font.parts
slanted\_font \= font.transform({'slant': 0.167})
extended\_font \= font.transform({'extend': 1.2})
subset\_font \= font.subset(\[ord(c) for c in 'Hello World'\])

Sources:

*   Adobe Technical Note #5040, Supporting Downloadable PostScript Language Fonts.
    
*   Adobe Type 1 Font Format, Adobe Systems Incorporated, third printing, v1.1, 1993. ISBN 0-201-57044-0.
    

class matplotlib.\_type1font.Type1Font(_input_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_type1font.py#L326-L1019)
[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A class representing a Type-1 font, for use by backends.

Attributes:

**parts**tuple

A 3-tuple of the cleartext part, the encrypted part, and the finale of zeros.

**decrypted**bytes

The decrypted form of `parts[1]`.

**prop**dict\[str, Any\]

A dictionary of font properties. Noteworthy keys include:

*   FontName: PostScript name of the font
    
*   Encoding: dict from numeric codes to glyph names
    
*   FontMatrix: bytes object encoding a matrix
    
*   UniqueID: optional font identifier, dropped when modifying the font
    
*   CharStrings: dict from glyph names to byte code
    
*   Subrs: array of byte code subroutines
    
*   OtherSubrs: bytes object encoding some PostScript code
    

Initialize a Type-1 font.

Parameters:

**input**str or 3-tuple

Either a pfb file name, or a 3-tuple of already-decoded Type-1 font [`parts`](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.parts "matplotlib._type1font.Type1Font.parts")
.

decrypted[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.decrypted "Link to this definition")

parts[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.parts "Link to this definition")

prop[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.prop "Link to this definition")

subset(_characters_, _name\_prefix_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_type1font.py#L859-L913)
[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.subset "Link to this definition")

Return a new font that only defines the given characters.

Parameters:

**characters**sequence of bytes

The subset of characters to include. These are indices into the font's encoding array. The encoding array of a Type-1 font can only include 256 characters, but other glyphs may be accessed via the seac operator.

**name\_prefix**str

Prefix to prepend to the font name.

Returns:

[`Type1Font`](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font "matplotlib._type1font.Type1Font")

transform(_effects_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_type1font.py#L730-L796)
[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.transform "Link to this definition")

Return a new font that is slanted and/or extended.

Parameters:

**effects**dict

A dict with optional entries:

*   'slant'float, default: 0
    
    Tangent of the angle that the font is to be slanted to the right. Negative values slant to the left.
    
*   'extend'float, default: 1
    
    Scaling factor for the font width. Values less than 1 condense the glyphs.
    

Returns:

[`Type1Font`](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font "matplotlib._type1font.Type1Font")

with\_encoding(_encoding_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_type1font.py#L798-L819)
[#](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font.with_encoding "Link to this definition")

Change the encoding of the font.

Parameters:

**encoding**dict

A dictionary mapping character codes to glyph names.

Returns:

[`Type1Font`](https://matplotlib.org/stable/api/_type1font.html#matplotlib._type1font.Type1Font "matplotlib._type1font.Type1Font")

On this page