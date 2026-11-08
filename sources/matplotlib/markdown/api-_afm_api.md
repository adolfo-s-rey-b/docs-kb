[Skip to main content](https://matplotlib.org/stable/api/_afm_api.html#main-content)

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
    

`matplotlib._afm`[#](https://matplotlib.org/stable/api/_afm_api.html#module-matplotlib._afm "Link to this heading")

====================================================================================================================

A Python interface to Adobe Font Metrics Files.

Although a number of other Python implementations exist, and may be more complete than this, it was decided not to go with them because they were either:

1.  copyrighted or used a non-BSD compatible license
    
2.  had too many dependencies and a free standing lib was needed
    
3.  did more than needed and it was easier to write afresh rather than figure out how to get just what was needed.
    

It is pretty easy to use, and has no external dependencies:

\>>> import matplotlib as mpl
\>>> from pathlib import Path
\>>> afm\_path \= Path(mpl.get\_data\_path(), 'fonts', 'afm', 'ptmr8a.afm')
\>>>
\>>> from matplotlib.\_afm import AFM
\>>> with afm\_path.open('rb') as fh:
...     afm \= AFM(fh)
\>>> afm.get\_fontname()
'Times-Roman'

As in the Adobe Font Metrics File Format Specification, all dimensions are given in units of 1/1000 of the scale factor (point size) of the font being used.

class matplotlib.\_afm.AFM(_fh_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L377-L499)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Parse the AFM file in file object _fh_.

property family\_name[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.family_name "Link to this definition")

The font family name, e.g., 'Times'.

get\_angle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L477-L479)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_angle "Link to this definition")

Return the fontangle as float.

get\_ascender()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L481-L483)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_ascender "Link to this definition")

Return the ascent as float.

get\_capheight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L485-L487)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_capheight "Link to this definition")

Return the cap height as float.

get\_char\_index(_c_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L418-L425)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_char_index "Link to this definition")

Return the glyph index corresponding to a character code point.

Note, for AFM fonts, we treat the glyph index the same as the codepoint.

get\_descender()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L489-L491)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_descender "Link to this definition")

Return the descent as float.

get\_familyname()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L456-L466)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_familyname "Link to this definition")

Return the font family name, e.g., 'Times'.

get\_fontname()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L441-L443)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_fontname "Link to this definition")

Return the font name, e.g., 'Times-Roman'.

get\_fullname()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L449-L454)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_fullname "Link to this definition")

Return the font full name, e.g., 'Times-Roman'.

get\_glyph\_name(_glyph\_ind_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L413-L416)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_glyph_name "Link to this definition")

Get the name of the glyph, i.e., ord(';') is 'semicolon'.

get\_kern\_dist\_from\_name(_name1_, _name2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L435-L439)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_kern_dist_from_name "Link to this definition")

Return the kerning pair distance (possibly 0) for chars _name1_ and _name2_.

get\_str\_bbox\_and\_descent(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L385-L411)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_str_bbox_and_descent "Link to this definition")

Return the string bounding box and the maximal descent.

get\_underline\_thickness()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L497-L499)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_underline_thickness "Link to this definition")

Return the underline thickness as float.

get\_weight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L473-L475)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_weight "Link to this definition")

Return the font weight, e.g., 'Bold' or 'Roman'.

get\_width\_char(_c_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L427-L429)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_width_char "Link to this definition")

Get the width of the character code from the character metric WX field.

get\_width\_from\_char\_name(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L431-L433)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_width_from_char_name "Link to this definition")

Get the width of the character from a type1 character name.

get\_xheight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L493-L495)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.get_xheight "Link to this definition")

Return the xheight as float.

property postscript\_name[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.AFM.postscript_name "Link to this definition")

class matplotlib.\_afm.CharMetrics(_width_, _name_, _bbox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L180-L192)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CharMetrics "Link to this definition")

Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "(in Python v3.14)")

Represents the character metrics of a single character.

Notes

The fields do currently only describe a subset of character metrics information defined in the AFM standard.

Create new instance of CharMetrics(width, name, bbox)

bbox[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CharMetrics.bbox "Link to this definition")

The bbox of the character (B) as a tuple (_llx_, _lly_, _urx_, _ury_).

name[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CharMetrics.name "Link to this definition")

The character name (N).

width[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CharMetrics.width "Link to this definition")

The character width (WX).

class matplotlib.\_afm.CompositePart(_name_, _dx_, _dy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L287-L292)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CompositePart "Link to this definition")

Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "(in Python v3.14)")

Represents the information on a composite element of a composite char.

Create new instance of CompositePart(name, dx, dy)

dx[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CompositePart.dx "Link to this definition")

x-displacement of the part from the origin.

dy[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CompositePart.dy "Link to this definition")

y-displacement of the part from the origin.

name[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.CompositePart.name "Link to this definition")

Name of the part, e.g. 'acute'.

class matplotlib.\_afm.FontMetricsHeader[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_afm.py#L82-L108)
[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader "Link to this definition")

Bases: [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "(in Python v3.14)")

Ascender[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Ascender "Link to this definition")

CapHeight[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.CapHeight "Link to this definition")

Capheight[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Capheight "Link to this definition")

CharacterSet[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.CharacterSet "Link to this definition")

Characters[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Characters "Link to this definition")

Descender[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Descender "Link to this definition")

EncodingScheme[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.EncodingScheme "Link to this definition")

FamilyName[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.FamilyName "Link to this definition")

FontBBox[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.FontBBox "Link to this definition")

FontName[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.FontName "Link to this definition")

FullName[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.FullName "Link to this definition")

IsFixedPitch[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.IsFixedPitch "Link to this definition")

ItalicAngle[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.ItalicAngle "Link to this definition")

Notice[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Notice "Link to this definition")

StartCharMetrics[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.StartCharMetrics "Link to this definition")

StartFontMetrics[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.StartFontMetrics "Link to this definition")

StdHW[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.StdHW "Link to this definition")

StdVW[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.StdVW "Link to this definition")

UnderlinePosition[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.UnderlinePosition "Link to this definition")

UnderlineThickness[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.UnderlineThickness "Link to this definition")

Version[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Version "Link to this definition")

Weight[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.Weight "Link to this definition")

XHeight[#](https://matplotlib.org/stable/api/_afm_api.html#matplotlib._afm.FontMetricsHeader.XHeight "Link to this definition")

On this page