[Skip to main content](https://matplotlib.org/stable/users/explain/text/fonts.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/users/explain/text/fonts.html#sphx-glr-download-users-explain-text-fonts-py)
 to download the full example code.

Fonts in Matplotlib[#](https://matplotlib.org/stable/users/explain/text/fonts.html#fonts-in-matplotlib "Link to this heading")

===============================================================================================================================

Matplotlib needs fonts to work with its text engine, some of which are shipped alongside the installation. The default font is [DejaVu Sans](https://dejavu-fonts.github.io/)
 which covers most European writing systems. However, users can configure the default fonts, and provide their own custom fonts. See [Customizing text properties](https://matplotlib.org/stable/users/explain/text/text_props.html#text-props)
 for details and [Text with non-latin glyphs](https://matplotlib.org/stable/users/explain/text/text_props.html#font-nonlatin)
 in particular for glyphs not supported by DejaVu Sans.

Matplotlib also provides an option to offload text rendering to a TeX engine (`usetex=True`), see [Text rendering with LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html#usetex)
.

Fonts in PDF and PostScript[#](https://matplotlib.org/stable/users/explain/text/fonts.html#fonts-in-pdf-and-postscript "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

Fonts have a long (and sometimes incompatible) history in computing, leading to different platforms supporting different types of fonts. In practice, Matplotlib supports three font specifications (in addition to pdf 'core fonts', which are explained later in the guide):

|     |     |     |
| --- | --- | --- |Types of Fonts[#](https://matplotlib.org/stable/users/explain/text/fonts.html#id2 "Link to this table")
| Type 1 (PDF with usetex) | Type 3 (PDF/PS) | TrueType (PDF) / Type 42 (PS) |
| --- | --- | --- |
| Old font types introduced by Adobe. |     | Newer font type introduced by Apple; commonly used today. |
| Restricted subset of PostScript, charstrings are in bytecode. | Full PostScript language, allows embedding arbitrary code. | Includes a virtual machine that can execute code. |
| Supports font hinting. | Does not support font hinting. | Supports font hinting, through the virtual machine. |
| Subsetted by code in [`matplotlib._type1font`](https://matplotlib.org/stable/api/_type1font.html#module-matplotlib._type1font "matplotlib._type1font")<br>. | Subsetted via external module [fontTools](https://github.com/fonttools/fonttools)<br>. |     |

Note

Adobe [disabled](https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-support.html)
 support for authoring with Type 1 fonts in January 2023. Matplotlib uses Type 1 fonts for compatibility with TeX; when the usetex feature is used with the PDF backend, Matplotlib reads the fonts used by the TeX engine, which are usually Type 1.

Matplotlib also provides limited support for OpenType fonts, a newer standard developed jointly by Adobe and Microsoft; such fonts generally contain a much larger character set.

### Font subsetting[#](https://matplotlib.org/stable/users/explain/text/fonts.html#font-subsetting "Link to this heading")

The PDF and PostScript formats support embedding fonts in files, allowing the display program to correctly render the text, independent of what fonts are installed on the viewer's computer and without the need to pre-rasterize the text. This ensures that if the output is zoomed or resized the text does not become pixelated. However, embedding full fonts in the file can lead to large output files, particularly with fonts with many glyphs such as those that support CJK (Chinese/Japanese/Korean).

To keep the output size reasonable while using vector fonts, Matplotlib embeds only the glyphs that are actually used in the document. This is known as font subsetting. Computing the font subset and writing the reduced font are both complex problems, which Matplotlib solves in most cases by using the [fontTools](https://fonttools.readthedocs.io/en/latest/)
 library.

### Core Fonts[#](https://matplotlib.org/stable/users/explain/text/fonts.html#core-fonts "Link to this heading")

In addition to the ability to embed fonts, as part of the [PostScript](https://en.wikipedia.org/wiki/PostScript_fonts#Core_Font_Set)
 and [PDF specification](https://docs.oracle.com/cd/E96927_01/TSG/FAQ/What%20are%20the%2014%20base%20fonts%20distributed%20with%20Acroba.html)
 there are 14 Core Fonts that compliant viewers must ensure are available. If you restrict your document to only these fonts you do not have to embed any font information in the document but still get vector text.

This is especially helpful to generate _really lightweight_ documents:

\# trigger core fonts for PDF backend
plt.rcParams\["pdf.use14corefonts"\] \= True
\# trigger core fonts for PS backend
plt.rcParams\["ps.useafm"\] \= True

chars \= "AFM ftw!"
fig, ax \= plt.subplots()
ax.text(0.5, 0.5, chars)

fig.savefig("AFM\_PDF.pdf", format\="pdf")
fig.savefig("AFM\_PS.ps", format\="ps")

Fonts in SVG[#](https://matplotlib.org/stable/users/explain/text/fonts.html#fonts-in-svg "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Text can output to SVG in two ways controlled by `[rcParams["svg.fonttype"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=svg.fonttype#rcparam-svg-fonttype) ` (default: `'path'`):

*   as a path (`'path'`) in the SVG
    
*   as string in the SVG with font styling on the element (`'none'`)
    

When saving via `'path'` Matplotlib will compute the path of the glyphs used as vector paths and write those to the output. The advantage of doing so is that the SVG will look the same on all computers independent of what fonts are installed. However the text will not be editable after the fact. In contrast, saving with `'none'` will result in smaller files and the text will appear directly in the markup. However, the appearance may vary based on the SVG viewer and what fonts are available.

Fonts in Agg[#](https://matplotlib.org/stable/users/explain/text/fonts.html#fonts-in-agg "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

To output text to raster formats via Agg, Matplotlib relies on [FreeType](https://www.freetype.org/)
. Because the exact rendering of the glyphs changes between FreeType versions we pin to a specific version for our image comparison tests.

How Matplotlib selects fonts[#](https://matplotlib.org/stable/users/explain/text/fonts.html#how-matplotlib-selects-fonts "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Internally, using a font in Matplotlib is a three step process:

1.  a [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
     object is created (explicitly or implicitly)
    
2.  based on the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
     object the methods on [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
     are used to select the closest "best" font Matplotlib is aware of (except for `'none'` mode of SVG).
    
3.  the Python proxy for the font object is used by the backend code to render the text -- the exact details depend on the backend via [`font_manager.get_font`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.get_font "matplotlib.font_manager.get_font")
    .
    

The algorithm to select the "best" font is a modified version of the algorithm specified by the [CSS1 Specifications](http://www.w3.org/TR/1998/REC-CSS2-19980512/)
 which is used by web browsers. This algorithm takes into account the font family name (e.g. "Arial", "Noto Sans CJK", "Hack", ...), the size, style, and weight. In addition to family names that map directly to fonts there are five "generic font family names" (serif, monospace, fantasy, cursive, and sans-serif) that will internally be mapped to any one of a set of fonts.

Currently the public API for doing step 2 is [`FontManager.findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.findfont "matplotlib.font_manager.FontManager.findfont")
 (and that method on the global [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 instance is aliased at the module level as [`font_manager.findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
), which will only find a single font and return the absolute path to the font on the filesystem.

Font fallback[#](https://matplotlib.org/stable/users/explain/text/fonts.html#font-fallback "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

There is no font that covers the entire Unicode space thus it is possible for the users to require a mix of glyphs that cannot be satisfied from a single font. While it has been possible to use multiple fonts within a Figure, on distinct [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instances, it was not previous possible to use multiple fonts in the same [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance (as a web browser does). As of Matplotlib 3.6 the Agg, SVG, PDF, and PS backends will "fallback" through multiple fonts in a single [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance:

fig, ax \= plt.subplots()
ax.text(
    .5, .5, "There are 几个汉字 in between!",
    family\=\['DejaVu Sans', 'Noto Sans CJK JP', 'Noto Sans TC'\],
    ha\='center'
)

([`Source code`](https://matplotlib.org/stable/_downloads/3866cf7a03a4b5b3f6c2377931b49f08/fonts-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9a9917ba30a1cd225f15e122512008cb/fonts-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/32438da1f3868e6b27e245cd13b17dc9/fonts-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-text-fonts-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-text-fonts-1.2x.png)

The string "There are 几个汉字 in between!" rendered with 2 fonts.

Internally this is implemented by setting The "font family" on [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 objects to a list of font families. A (currently) private API extracts a list of paths to all of the fonts found and then constructs a single [`ft2font.FT2Font`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
 object that is aware of all of the fonts. Each glyph of the string is rendered using the first font in the list that contains that glyph.

A majority of this work was done by Aitik Gupta supported by Google Summer of Code 2021.

[`Download Jupyter notebook: fonts.ipynb`](https://matplotlib.org/stable/_downloads/df0c615c283f2970ab5a7bb796e29754/fonts.ipynb)

[`Download Python source code: fonts.py`](https://matplotlib.org/stable/_downloads/d1dca66336d6b6aa99c62593a9314464/fonts.py)

[`Download zipped: fonts.zip`](https://matplotlib.org/stable/_downloads/93cffc04be0548530ac5d53646574c05/fonts.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page