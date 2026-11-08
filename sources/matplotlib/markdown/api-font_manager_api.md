[Skip to main content](https://matplotlib.org/stable/api/font_manager_api.html#main-content)

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
    

`matplotlib.font_manager`[#](https://matplotlib.org/stable/api/font_manager_api.html#module-matplotlib.font_manager "Link to this heading")

============================================================================================================================================

A module for finding, managing, and using fonts across platforms.

This module provides a single [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 instance, `fontManager`, that can be shared across backends and platforms. The [`findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
 function returns the best TrueType (TTF) font file in the local or system font path that matches the specified [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 instance. The [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 also handles Adobe Font Metrics (AFM) font files for use by the PostScript backend. The [`FontManager.addfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "matplotlib.font_manager.FontManager.addfont")
 function adds a custom font from a file without installing it into your operating system.

The design is based on the [W3C Cascading Style Sheet, Level 1 (CSS1) font specification](http://www.w3.org/TR/1998/REC-CSS2-19980512/)
. Future versions may implement the Level 2 or 2.1 specifications.

class matplotlib.font\_manager.FontManager(_size\=None_, _weight\='normal'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1195-L1717)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

On import, the [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 singleton instance creates a list of ttf and afm fonts and caches their [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
. The [`FontManager.findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.findfont "matplotlib.font_manager.FontManager.findfont")
 method does a nearest neighbor search to find the font that most closely matches the specification. If no good enough match is found, the default font is returned.

Fonts added with the [`FontManager.addfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "matplotlib.font_manager.FontManager.addfont")
 method will not persist in the cache; therefore, [`addfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "matplotlib.font_manager.FontManager.addfont")
 will need to be called every time Matplotlib is imported. This method should only be used if and when a font cannot be installed on your operating system by other means.

Notes

The [`FontManager.addfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "matplotlib.font_manager.FontManager.addfont")
 method must be called on the global [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 instance.

Example usage:

import matplotlib.pyplot as plt
from matplotlib import font\_manager

font\_dirs \= \["/resources/fonts"\]  \# The path to the custom font file.
font\_files \= font\_manager.findSystemFonts(fontpaths\=font\_dirs)

for font\_file in font\_files:
    font\_manager.fontManager.addfont(font\_file)

addfont(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1269-L1308)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.addfont "Link to this definition")

Cache the properties of the font at _path_ to make it available to the [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
. The type of font is inferred from the path suffix.

Parameters:

**path**str or path-like

Notes

This method is useful for adding a custom font without installing it in your operating system. See the [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 singleton instance for usage and caveats about this function.

property defaultFont[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.defaultFont "Link to this definition")

findfont(_prop_, _fontext\='ttf'_, _directory\=None_, _fallback\_to\_default\=True_, _rebuild\_if\_missing\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1462-L1532)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.findfont "Link to this definition")

Find the path to the font file most closely matching the given font properties.

Parameters:

**prop**str or [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

The font properties to search for. This can be either a [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 object or a string defining a [fontconfig patterns](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)
.

**fontext**{'ttf', 'afm'}, default: 'ttf'

The extension of the font file:

*   'ttf': TrueType and OpenType fonts (.ttf, .ttc, .otf)
    
*   'afm': Adobe Font Metrics (.afm)
    

**directory**str, optional

If given, only search this directory and its subdirectories. If [`MPL_IGNORE_SYSTEM_FONTS`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPL_IGNORE_SYSTEM_FONTS)
 is set, then this defaults to Matplotlib's internal font directory.

**fallback\_to\_default**bool

If True, will fall back to the default font family (usually "DejaVu Sans" or "Helvetica") if the first lookup hard-fails.

**rebuild\_if\_missing**bool

Whether to rebuild the font cache and search again if the first match appears to point to a nonexisting font (i.e., the font cache contains outdated entries).

Returns:

FontPath

The filename of the best matching font.

Notes

This performs a nearest neighbor search. Each font is given a similarity score to the target font properties. The first font with the highest score is returned. If no matches below a certain threshold are found, the default font (usually DejaVu Sans) is returned.

The result is cached, so subsequent lookups don't have to perform the O(n) nearest neighbor search.

See the [W3C Cascading Style Sheet, Level 1](http://www.w3.org/TR/1998/REC-CSS2-19980512/)
 documentation for a description of the font finding algorithm.

static get\_default\_size()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1323-L1328)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.get_default_size "Link to this definition")

Return the default font size.

get\_default\_weight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1317-L1321)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.get_default_weight "Link to this definition")

Return the default font weight.

get\_font\_names()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1534-L1536)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.get_font_names "Link to this definition")

Return the list of available fonts.

score\_family(_families_, _family2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1344-L1372)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.score_family "Link to this definition")

Return a match score between the list of font families in _families_ and the font family name _family2_.

An exact match at the head of the list returns 0.0.

A match further down the list will return between 0 and 1.

No match will return 1.0.

score\_size(_size1_, _size2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1438-L1460)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.score_size "Link to this definition")

Return a match score between _size1_ and _size2_.

If _size2_ (the size specified in the font file) is 'scalable', this function always returns 0.0, since any font size can be generated.

Otherwise, the result is the absolute distance between _size1_ and _size2_, normalized so that the usual range of font sizes (6pt - 72pt) will lie between 0.0 and 1.0.

score\_stretch(_stretch1_, _stretch2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1402-L1418)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.score_stretch "Link to this definition")

Return a match score between _stretch1_ and _stretch2_.

The result is the absolute value of the difference between the CSS numeric values of _stretch1_ and _stretch2_, normalized between 0.0 and 1.0.

score\_style(_style1_, _style2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1374-L1389)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.score_style "Link to this definition")

Return a match score between _style1_ and _style2_.

An exact match returns 0.0.

A match between 'italic' and 'oblique' returns 0.1.

No match returns 1.0.

score\_variant(_variant1_, _variant2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1391-L1400)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.score_variant "Link to this definition")

Return a match score between _variant1_ and _variant2_.

An exact match returns 0.0, otherwise 1.0.

score\_weight(_weight1_, _weight2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1420-L1436)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.score_weight "Link to this definition")

Return a match score between _weight1_ and _weight2_.

The result is 0.0 if both weight1 and weight 2 are given as strings and have the same value.

Otherwise, the result is the absolute value of the difference between the CSS numeric values of _weight1_ and _weight2_, normalized between 0.05 and 1.0.

set\_default\_weight(_weight_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1330-L1334)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.set_default_weight "Link to this definition")

Set the default font weight. The initial value is 'normal'.

class matplotlib.font\_manager.FontPath(_path_, _face\_index_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L337-L389)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontPath "Link to this definition")

Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

A class to describe a path to a font with a face index.

Parameters:

**path**str

The path to a font.

**face\_index**int

The face index in the font.

property face\_index[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontPath.face_index "Link to this definition")

The face index in a font.

property path[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontPath.path "Link to this definition")

The path to a font.

class matplotlib.font\_manager.FontProperties(_family\=None_, _style\=None_, _variant\=None_, _weight\=None_, _stretch\=None_, _size\=None_, _fname\=None_, _math\_fontfamily\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L749-L1122)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A class for storing and manipulating font properties.

The font properties are the six properties described in the [W3C Cascading Style Sheet, Level 1](http://www.w3.org/TR/1998/REC-CSS2-19980512/)
 font specification and _math\_fontfamily_ for math fonts:

*   family: A list of font names in decreasing order of priority. The items may include a generic font family name, either 'sans-serif', 'serif', 'cursive', 'fantasy', or 'monospace'. In that case, the actual font to be used will be looked up from the associated rcParam during the search process in [`findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
    . Default: `[rcParams["font.family"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.family#rcparam-font-family) ` (default: `['sans-serif']`)
    
*   style: Either 'normal', 'italic' or 'oblique'. Default: `[rcParams["font.style"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.style#rcparam-font-style) ` (default: `'normal'`)
    
*   variant: Either 'normal' or 'small-caps'. Default: `[rcParams["font.variant"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.variant#rcparam-font-variant) ` (default: `'normal'`)
    
*   stretch: A numeric value in the range 0-1000 or one of 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded' or 'ultra-expanded'. Default: `[rcParams["font.stretch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.stretch#rcparam-font-stretch) ` (default: `'normal'`)
    
*   weight: A numeric value in the range 0-1000 or one of 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'. Default: `[rcParams["font.weight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.weight#rcparam-font-weight) ` (default: `'normal'`)
    
*   size: Either a relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 10. Default: `[rcParams["font.size"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.size#rcparam-font-size) ` (default: `10.0`)
    
*   math\_fontfamily: The family of fonts used to render math text. Supported values are: 'dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans' and 'custom'. Default: `[rcParams["mathtext.fontset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fontset#rcparam-mathtext-fontset) ` (default: `'dejavusans'`)
    

Alternatively, a font may be specified using the absolute path to a font file, by using the _fname_ kwarg. However, in this case, it is typically simpler to just pass the path (as a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")
, not a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
) to the _font_ kwarg of the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 object.

The preferred usage of font sizes is to use the relative values, e.g., 'large', instead of absolute font sizes, e.g., 12. This approach allows all text sizes to be made larger or smaller based on the font manager's default font size.

This class accepts a single positional string as [fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig/)
 [pattern](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)
, or alternatively individual properties as keyword arguments:

FontProperties(pattern)
FontProperties(\*, family\=None, style\=None, variant\=None, ...)

This support does not depend on fontconfig; we are merely borrowing its pattern syntax for use here.

Note that Matplotlib's internal font manager and fontconfig use a different algorithm to lookup fonts, so the results of the same pattern may be different in Matplotlib than in other applications that use fontconfig.

copy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1114-L1116)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.copy "Link to this definition")

Return a copy of self.

get\_family()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L870-L878)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_family "Link to this definition")

Return a list of individual font family names or generic family names.

The font families or generic font families (which will be resolved from their respective rcParams when searching for a matching font) in the order of preference.

get\_file()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L921-L925)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_file "Link to this definition")

Return the filename of the associated font.

get\_fontconfig\_pattern()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L927-L935)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_fontconfig_pattern "Link to this definition")

Get a [fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig/)
 [pattern](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)
 suitable for looking up the font as specified with fontconfig's `fc-match` utility.

This support does not depend on fontconfig; we are merely borrowing its pattern syntax for use here.

get\_math\_fontfamily()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1073-L1079)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_math_fontfamily "Link to this definition")

Return the name of the font family used for math text.

The default font is `[rcParams["mathtext.fontset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fontset#rcparam-mathtext-fontset) ` (default: `'dejavusans'`).

get\_name()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L880-L884)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_name "Link to this definition")

Return the name of the font that best matches the font properties.

get\_size()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L915-L919)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_size "Link to this definition")

Return the font size.

get\_size\_in\_points()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L915-L919)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_size_in_points "Link to this definition")

Return the font size.

get\_slant()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L886-L890)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_slant "Link to this definition")

Return the font style. Values are: 'normal', 'italic' or 'oblique'.

get\_stretch()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L907-L913)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_stretch "Link to this definition")

Return the font stretch or width. Options are: 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'.

get\_style()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L886-L890)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_style "Link to this definition")

Return the font style. Values are: 'normal', 'italic' or 'oblique'.

get\_variant()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L892-L896)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_variant "Link to this definition")

Return the font variant. Values are: 'normal' or 'small-caps'.

get\_weight()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L898-L905)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.get_weight "Link to this definition")

Get the font weight. Options are: A numeric value in the range 0-1000 or one of 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'

set\_family(_family_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L937-L948)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_family "Link to this definition")

Change the font family. Can be either an alias (generic name is CSS parlance), such as: 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace', a real font name or a list of real font names. Real font names are not supported when `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
. Default: `[rcParams["font.family"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.family#rcparam-font-family) ` (default: `['sans-serif']`)

set\_file(_file_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1053-L1058)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_file "Link to this definition")

Set the filename of the fontfile to use. In this case, all other properties will be ignored.

set\_fontconfig\_pattern(_pattern_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1060-L1071)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_fontconfig_pattern "Link to this definition")

Set the properties by parsing a [fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig/)
 _pattern_.

This support does not depend on fontconfig; we are merely borrowing its pattern syntax for use here.

set\_math\_fontfamily(_fontfamily_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1081-L1106)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_math_fontfamily "Link to this definition")

Set the font family for text in math mode.

If not set explicitly, `[rcParams["mathtext.fontset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fontset#rcparam-mathtext-fontset) ` (default: `'dejavusans'`) will be used.

Parameters:

**fontfamily**str

The name of the font family.

Available font families are defined in the [default matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
.

See also

[`text.Text.get_math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_math_fontfamily "matplotlib.text.Text.get_math_fontfamily")

set\_name(_family_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L937-L948)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_name "Link to this definition")

Change the font family. Can be either an alias (generic name is CSS parlance), such as: 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace', a real font name or a list of real font names. Real font names are not supported when `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
. Default: `[rcParams["font.family"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.family#rcparam-font-family) ` (default: `['sans-serif']`)

set\_size(_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1024-L1051)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_size "Link to this definition")

Set the font size.

Parameters:

**size**float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}, default: `[rcParams["font.size"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.size#rcparam-font-size) ` (default: `10.0`)

If a float, the font size in points. The string values denote sizes relative to the default font size.

set\_slant(_style_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L950-L960)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_slant "Link to this definition")

Set the font style.

Parameters:

**style**{'normal', 'italic', 'oblique'}, default: `[rcParams["font.style"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.style#rcparam-font-style) ` (default: `'normal'`)

set\_stretch(_stretch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L999-L1022)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_stretch "Link to this definition")

Set the font stretch or width.

Parameters:

**stretch**int or {'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}, default: `[rcParams["font.stretch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.stretch#rcparam-font-stretch) ` (default: `'normal'`)

If int, must be in the range 0-1000.

set\_style(_style_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L950-L960)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_style "Link to this definition")

Set the font style.

Parameters:

**style**{'normal', 'italic', 'oblique'}, default: `[rcParams["font.style"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.style#rcparam-font-style) ` (default: `'normal'`)

set\_variant(_variant_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L962-L972)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_variant "Link to this definition")

Set the font variant.

Parameters:

**variant**{'normal', 'small-caps'}, default: `[rcParams["font.variant"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.variant#rcparam-font-variant) ` (default: `'normal'`)

set\_weight(_weight_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L974-L997)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties.set_weight "Link to this definition")

Set the font weight.

Parameters:

**weight**int or {'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}, default: `[rcParams["font.weight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.weight#rcparam-font-weight) ` (default: `'normal'`)

If int, must be in the range 0-1000.

matplotlib.font\_manager.afmFontProperty(_fontpath_, _font_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L628-L695)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.afmFontProperty "Link to this definition")

Extract information from an AFM font file.

Parameters:

**fontpath**str

The filename corresponding to _font_.

**font**AFM

The AFM font file from which information will be extracted.

Returns:

[`FontEntry`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontEntry "matplotlib.font_manager.FontEntry")

The extracted font properties.

matplotlib.font\_manager.findSystemFonts(_fontpaths\=None_, _fontext\='ttf'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L278-L326)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findSystemFonts "Link to this definition")

Find fonts in a search path, system paths, or some other platform-specific method.

Parameters:

**fontpaths**list of str, optional

Search for fonts in these specified font paths. If no paths are given and the [`MPL_IGNORE_SYSTEM_FONTS`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPL_IGNORE_SYSTEM_FONTS)
 is not set, use a standard set of system paths, as well as the list of fonts tracked by fontconfig if fontconfig is installed and available.

**fontext**{'ttf', 'afm'}, default: 'ttf'

If 'ttf', search for TrueType fonts; if 'afm', search for with AFM fonts.

Returns:

list of str

A list of file paths with fonts of the given type.

matplotlib.font\_manager.findfont(_prop_, _fontext\='ttf'_, _directory\=None_, _fallback\_to\_default\=True_, _rebuild\_if\_missing\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1462-L1532)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "Link to this definition")

Find the path to the font file most closely matching the given font properties.

Parameters:

**prop**str or [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

The font properties to search for. This can be either a [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 object or a string defining a [fontconfig patterns](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)
.

**fontext**{'ttf', 'afm'}, default: 'ttf'

The extension of the font file:

*   'ttf': TrueType and OpenType fonts (.ttf, .ttc, .otf)
    
*   'afm': Adobe Font Metrics (.afm)
    

**directory**str, optional

If given, only search this directory and its subdirectories. If [`MPL_IGNORE_SYSTEM_FONTS`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPL_IGNORE_SYSTEM_FONTS)
 is set, then this defaults to Matplotlib's internal font directory.

**fallback\_to\_default**bool

If True, will fall back to the default font family (usually "DejaVu Sans" or "Helvetica") if the first lookup hard-fails.

**rebuild\_if\_missing**bool

Whether to rebuild the font cache and search again if the first match appears to point to a nonexisting font (i.e., the font cache contains outdated entries).

Returns:

FontPath

The filename of the best matching font.

Notes

This performs a nearest neighbor search. Each font is given a similarity score to the target font properties. The first font with the highest score is returned. If no matches below a certain threshold are found, the default font (usually DejaVu Sans) is returned.

The result is cached, so subsequent lookups don't have to perform the O(n) nearest neighbor search.

See the [W3C Cascading Style Sheet, Level 1](http://www.w3.org/TR/1998/REC-CSS2-19980512/)
 documentation for a description of the font finding algorithm.

matplotlib.font\_manager.get\_font(_font\_filepaths_, _hinting\_factor\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1787-L1831)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.get_font "Link to this definition")

Get an [`ft2font.FT2Font`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
 object given a list of file paths.

Parameters:

**font\_filepaths**Iterable\[str, bytes, os.PathLike, FontPath\], str, bytes, os.PathLike, FontPath

Relative or absolute paths to the font files to be used.

If a single string, bytes, or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
, then it will be treated as a list with that entry only.

If more than one filepath is passed, then the returned FT2Font object will fall back through the fonts, in the order given, to find a needed glyph.

Returns:

[`ft2font.FT2Font`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")

matplotlib.font\_manager.get\_font\_names()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1534-L1536)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.get_font_names "Link to this definition")

Return the list of available fonts.

matplotlib.font\_manager.get\_fontext\_synonyms(_fontext_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L178-L188)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.get_fontext_synonyms "Link to this definition")

Return a list of file extensions that are synonyms for the given file extension _fileext_.

matplotlib.font\_manager.is\_opentype\_cff\_font(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1720-L1731)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.is_opentype_cff_font "Link to this definition")

\[_Deprecated_\] Return whether the given font is a Postscript Compact Font Format Font embedded in an OpenType wrapper. Used by the PostScript and PDF backends that cannot subset these fonts.

Notes

Deprecated since version 3.11.

matplotlib.font\_manager.json\_dump(_data_, _filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1159-L1180)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_dump "Link to this definition")

Dump [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 _data_ as JSON to the file named _filename_.

See also

[`json_load`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_load "matplotlib.font_manager.json_load")

Notes

File paths that are children of the Matplotlib data path (typically, fonts shipped with Matplotlib) are stored relative to that data path (to remain valid across virtualenvs).

This function temporarily locks the output file to prevent multiple processes from overwriting one another's output.

matplotlib.font\_manager.json\_load(_filename_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L1183-L1192)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_load "Link to this definition")

Load a [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
 from the JSON file named _filename_.

See also

[`json_dump`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.json_dump "matplotlib.font_manager.json_dump")

matplotlib.font\_manager.list\_fonts(_directory_, _extensions_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L191-L201)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.list_fonts "Link to this definition")

Return a list of all fonts matching any of the extensions, found recursively under the directory.

matplotlib.font\_manager.ttfFontProperty(_font_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L424-L549)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.ttfFontProperty "Link to this definition")

Extract information from a TrueType font file.

Parameters:

**font**[`FT2Font`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")

The TrueType font file from which information will be extracted.

Returns:

[`FontEntry`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontEntry "matplotlib.font_manager.FontEntry")

The extracted font properties.

matplotlib.font\_manager.win32FontDirectory()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L204-L218)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.win32FontDirectory "Link to this definition")

Return the user-specified font directory for Win32. This is looked up from the registry key

\\\\HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders\\Fonts

If the key is not found, `%WINDIR%\Fonts` will be returned.

matplotlib.font\_manager.fontManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.fontManager "Link to this definition")

The global instance of [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
.

class matplotlib.font\_manager.FontEntry(_fname\=''_, _index\=0_, _name\=''_, _style\='normal'_, _variant\='normal'_, _weight\='normal'_, _stretch\='normal'_, _size\='medium'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/font_manager.py#L392-L421)
[#](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontEntry "Link to this definition")

A class for storing Font properties.

It is used when populating the font lookup dictionary.

On this page