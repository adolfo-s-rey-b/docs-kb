[Skip to main content](https://matplotlib.org/stable/api/mathtext_api.html#main-content)

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
    

`matplotlib.mathtext`[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib-mathtext "Link to this heading")

=========================================================================================================================

Inheritance diagram of matplotlib.mathtext

A module for parsing a subset of the TeX math syntax and rendering it to a Matplotlib backend.

For a tutorial of its usage, see [Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
. This document is primarily concerned with implementation details.

The module uses [pyparsing](https://pypi.org/project/pyparsing/)
 to parse the TeX expression.

The Bakoma distribution of the TeX Computer Modern fonts, and STIX fonts are supported. There is experimental support for using arbitrary fonts, but results may vary without proper tweaking and metrics for those fonts.

class matplotlib.mathtext.MathTextParser(_output_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mathtext.py#L37-L105)
[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.MathTextParser "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Create a MathTextParser for the given backend _output_.

Parameters:

**output**{"path", "agg"}

Whether to return a [`VectorParse`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse "matplotlib.mathtext.VectorParse")
 ("path") or a [`RasterParse`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse "matplotlib.mathtext.RasterParse")
 ("agg", or its synonym "macosx").

parse(_s_, _dpi\=72_, _prop\=None_, _\*_, _antialiased\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mathtext.py#L62-L86)
[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.MathTextParser.parse "Link to this definition")

Parse the given math expression _s_ at the given _dpi_. If _prop_ is provided, it is a [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 object specifying the "default" font to use in the math expression, used for all non-math text.

The results are cached, so multiple calls to [`parse`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.MathTextParser.parse "matplotlib.mathtext.MathTextParser.parse")
 with the same expression should be fast.

Depending on the _output_ type, this returns either a [`VectorParse`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse "matplotlib.mathtext.VectorParse")
 or a [`RasterParse`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse "matplotlib.mathtext.RasterParse")
.

class matplotlib.mathtext.RasterParse(_ox_, _oy_, _width_, _height_, _depth_, _image_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mathtext.py)
[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse "Link to this definition")

Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "(in Python v3.14)")

The namedtuple type returned by `MathTextParser("agg").parse(...)`.

Attributes:

**ox, oy**float

The offsets are always zero.

**width, height, depth**float

The global metrics.

**image**2D array of uint8

A raster image.

Create new instance of RasterParse(ox, oy, width, height, depth, image)

depth[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse.depth "Link to this definition")

Alias for field number 4

height[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse.height "Link to this definition")

Alias for field number 3

image[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse.image "Link to this definition")

Alias for field number 5

ox[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse.ox "Link to this definition")

Alias for field number 0

oy[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse.oy "Link to this definition")

Alias for field number 1

width[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.RasterParse.width "Link to this definition")

Alias for field number 2

class matplotlib.mathtext.VectorParse(_width_, _height_, _depth_, _glyphs_, _rects_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mathtext.py)
[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse "Link to this definition")

Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "(in Python v3.14)")

The namedtuple type returned by `MathTextParser("path").parse(...)`.

Attributes:

**width, height, depth**float

The global metrics.

**glyphs**list

The glyphs including their positions.

**rect**list

The list of rectangles.

Create new instance of VectorParse(width, height, depth, glyphs, rects)

depth[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse.depth "Link to this definition")

Alias for field number 2

glyphs[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse.glyphs "Link to this definition")

Alias for field number 3

height[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse.height "Link to this definition")

Alias for field number 1

rects[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse.rects "Link to this definition")

Alias for field number 4

width[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.VectorParse.width "Link to this definition")

Alias for field number 0

matplotlib.mathtext.get\_unicode\_index(_symbol_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_mathtext.py#L52-L71)
[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.get_unicode_index "Link to this definition")

Return the integer index (from the Unicode table) of _symbol_.

Parameters:

**symbol**str

A single (Unicode) character, a TeX command (e.g. r'pi') or a Type1 symbol name (e.g. 'phi').

matplotlib.mathtext.math\_to\_image(_s_, _filename\_or\_obj_, _prop\=None_, _dpi\=None_, _format\=None_, _\*_, _color\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mathtext.py#L108-L140)
[#](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.math_to_image "Link to this definition")

Given a math expression, renders it in a closely-clipped bounding box to an image file.

Parameters:

**s**str

A math expression. The math portion must be enclosed in dollar signs.

**filename\_or\_obj**str or path-like or file-like

Where to write the image data.

**prop**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, optional

The size and style of the text.

**dpi**float, optional

The output dpi. If not set, the dpi is determined as for [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

**format**str, optional

The output format, e.g., 'svg', 'pdf', 'ps' or 'png'. If not set, the format is determined as for [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

**color**str, optional

Foreground color, defaults to `[rcParams["text.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.color#rcparam-text-color) ` (default: `'black'`).

On this page