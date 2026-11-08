[Skip to main content](https://matplotlib.org/stable/api/dviread.html#main-content)

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
    

`matplotlib.dviread`[#](https://matplotlib.org/stable/api/dviread.html#module-matplotlib.dviread "Link to this heading")

=========================================================================================================================

A module for reading dvi files output by TeX. Several limitations make this not (currently) useful as a general-purpose dvi preprocessor, but it is currently used by the pdf backend for processing usetex text.

Interface:

with Dvi(filename, 72) as dvi:
    \# iterate over pages:
    for page in dvi:
        w, h, d \= page.width, page.height, page.descent
        for x, y, font, glyph, width in page.text:
            fontname \= font.texname
            pointsize \= font.size
            ...
        for x, y, height, width in page.boxes:
            ...

class matplotlib.dviread.Dvi(_filename_, _dpi_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L219-L628)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Dvi "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A reader for a dvi ("device-independent") file, as produced by TeX.

The current implementation can only iterate through pages in order, and does not even attempt to verify the postamble.

This class can be used as a context manager to close the underlying file upon exit. Pages can be read via iteration. Here is an overly simple way to extract text without trying to detect whitespace:

\>>> with matplotlib.dviread.Dvi('input.dvi', 72) as dvi:
...     for page in dvi:
...         print(''.join(chr(t.glyph) for t in page.text))

Read the data from the file named _filename_ and convert TeX's internal units to units of _dpi_ per inch. _dpi_ only sets the units and does not limit the resolution. Use None to return TeX's internal units.

close()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L281-L284)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Dvi.close "Link to this definition")

Close the underlying file if it is open.

class matplotlib.dviread.DviFont(_scale_, _metrics_, _texname_, _vf_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L631-L824)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Encapsulation of a font that a DVI file can refer to.

This class holds a font's texname and size, supports comparison, and knows the widths of glyphs in the same units as the AFM file. There are also internal attributes (for use by dviread.py) that are _not_ used for comparison.

The size is in Adobe points (converted from TeX points).

Parameters:

**scale**float

Factor by which the font is scaled from its natural size.

**metrics**Tfm | TtfMetrics

TeX font metrics for this font

**texname**bytes

Name of the font as used internally in the DVI file, as an ASCII bytestring. This is usually very different from any external font names; [`PsfontsMap`](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsfontsMap "matplotlib.dviread.PsfontsMap")
 can be used to find the external name of the font.

**vf**Vf

A TeX "virtual font" file, or None if this font is not virtual.

Attributes:

**texname**bytes

[`fname`](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.fname "matplotlib.dviread.DviFont.fname")
str

A fake filename

**size**float

Size of the font in Adobe points, converted from the slightly smaller TeX points.

property effects[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.effects "Link to this definition")

property face\_index[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.face_index "Link to this definition")

property fname[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.fname "Link to this definition")

A fake filename

classmethod from\_luatex(_scale_, _texname_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L675-L698)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.from_luatex "Link to this definition")

classmethod from\_xetex(_scale_, _texname_, _subfont_, _effects_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L700-L709)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.from_xetex "Link to this definition")

resolve\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L770-L790)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.resolve_path "Link to this definition")

property size[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.size "Link to this definition")

property subfont[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.subfont "Link to this definition")

property widths[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.DviFont.widths "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

class matplotlib.dviread.PsFont(_texname_, _psname_, _effects_, _encoding_, _filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsFont "Link to this definition")

Bases: [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

Create new instance of PsFont(texname, psname, effects, encoding, filename)

effects[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsFont.effects "Link to this definition")

Alias for field number 2

encoding[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsFont.encoding "Link to this definition")

Alias for field number 3

filename[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsFont.filename "Link to this definition")

Alias for field number 4

psname[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsFont.psname "Link to this definition")

Alias for field number 1

texname[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsFont.texname "Link to this definition")

Alias for field number 0

class matplotlib.dviread.PsfontsMap(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L1051-L1224)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.PsfontsMap "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A psfonts.map formatted file, mapping TeX fonts to PS fonts.

Parameters:

**filename**str or path-like

Notes

For historical reasons, TeX knows many Type-1 fonts by different names than the outside world. (For one thing, the names have to fit in eight characters.) Also, TeX's native fonts are not Type-1 but Metafont, which is nontrivial to convert to PostScript except as a bitmap. While high-quality conversions to Type-1 format exist and are shipped with modern TeX distributions, we need to know which Type-1 fonts are the counterparts of which native fonts. For these reasons a mapping is needed from internal font names to font file names.

A texmf tree typically includes mapping files called e.g. `psfonts.map`, `pdftex.map`, or `dvipdfm.map`. The file `psfonts.map` is used by **dvips**, `pdftex.map` by **pdfTeX**, and `dvipdfm.map` by **dvipdfm**. `psfonts.map` might avoid embedding the 35 PostScript fonts (i.e., have no filename for them, as in the Times-Bold example above), while the pdf-related files perhaps only avoid the "Base 14" pdf fonts. But the user may have configured these files differently.

Examples

\>>> map \= PsfontsMap(find\_tex\_file('pdftex.map'))
\>>> entry \= map\[b'ptmbo8r'\]
\>>> entry.texname
b'ptmbo8r'
\>>> entry.psname
b'Times-Bold'
\>>> entry.encoding
'/usr/local/texlive/2008/texmf-dist/fonts/enc/dvips/base/8r.enc'
\>>> entry.effects
{'slant': 0.16700000000000001}
\>>> entry.filename

class matplotlib.dviread.TexMetrics(_\*_, _tex\_width_, _tex\_height_, _tex\_depth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L956-L969)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.TexMetrics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Metrics of a glyph, with TeX semantics.

TeX metrics have different semantics from FreeType metrics: tex\_width corresponds to FreeType's `advance` (i.e., including whitespace padding); tex\_height to `bearingY` (how much the glyph extends over the baseline); tex\_depth to `height - bearingY` (how much the glyph extends under the baseline, as a positive number).

tex\_depth[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.TexMetrics.tex_depth "Link to this definition")

tex\_height[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.TexMetrics.tex_height "Link to this definition")

tex\_width[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.TexMetrics.tex_width "Link to this definition")

class matplotlib.dviread.Tfm(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L972-L1024)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Tfm "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A TeX Font Metric file.

This implementation covers only the bare minimum needed by the Dvi class.

Parameters:

**filename**str or path-like

Attributes:

**checksum**int

Used for verifying against the dvi file.

**design\_size**int

Design size of the font (in 12.20 TeX points); unused because it is overridden by the scale factor specified in the dvi file.

property depth[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Tfm.depth "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use get\_metrics instead.

get\_metrics(_idx_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L1015-L1017)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Tfm.get_metrics "Link to this definition")

Return a glyph's TexMetrics, or None if unavailable.

property height[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Tfm.height "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use get\_metrics instead.

property width[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Tfm.width "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use get\_metrics instead.

class matplotlib.dviread.TtfMetrics(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L1027-L1045)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.TtfMetrics "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

get\_metrics(_idx_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L1031-L1045)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.TtfMetrics.get_metrics "Link to this definition")

class matplotlib.dviread.Vf(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L827-L947)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Vf "Link to this definition")

Bases: [`Dvi`](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Dvi "matplotlib.dviread.Dvi")

A virtual font (\*.vf file) containing subroutines for dvi files.

Parameters:

**filename**str or path-like

Notes

The virtual font format is a derivative of dvi: [http://mirrors.ctan.org/info/knuth/virtual-fonts](http://mirrors.ctan.org/info/knuth/virtual-fonts)
 This class reuses some of the machinery of [`Dvi`](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.Dvi "matplotlib.dviread.Dvi")
 but replaces the `_read` loop and dispatch mechanism.

Examples

vf \= Vf(filename)
glyph \= vf\[code\]
glyph.text, glyph.boxes, glyph.width

Read the data from the file named _filename_ and convert TeX's internal units to units of _dpi_ per inch. _dpi_ only sets the units and does not limit the resolution. Use None to return TeX's internal units.

matplotlib.dviread.find\_tex\_file(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dviread.py#L1276-L1335)
[#](https://matplotlib.org/stable/api/dviread.html#matplotlib.dviread.find_tex_file "Link to this definition")

Find a file in the texmf tree using [kpathsea](https://www.tug.org/kpathsea/)
.

The kpathsea library, provided by most existing TeX distributions, both on Unix-like systems and on Windows (MikTeX), is invoked via a long-lived luatex process if luatex is installed, or via kpsewhich otherwise.

Parameters:

**filename**str or path-like

Raises:

FileNotFoundError

If the file is not found.

On this page