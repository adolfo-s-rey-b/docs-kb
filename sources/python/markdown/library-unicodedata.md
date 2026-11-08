### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/stringprep.html "stringprep — Internet String Preparation")
     |
*   [previous](https://docs.python.org/3/library/textwrap.html "textwrap — Text wrapping and filling")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`unicodedata` — Unicode Database[¶](https://docs.python.org/3/library/unicodedata.html#module-unicodedata "Link to this heading")

==================================================================================================================================

* * *

This module provides access to the Unicode Character Database (UCD) which defines character properties for all Unicode characters. The data contained in this database is compiled from the [UCD version 17.0.0](https://www.unicode.org/Public/17.0.0/ucd)
.

The module uses the same names and symbols as defined by Unicode Standard Annex #44, [“Unicode Character Database”](https://www.unicode.org/reports/tr44/)
.

See also

The [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto)
 for more information about Unicode and how to use this module.

|     |     |
| --- | --- |
| **Lookup** |     |
| [`lookup(name)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.lookup "unicodedata.lookup") | Look up character by name |
| [`name(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.name "unicodedata.name") | Return the name assigned to a character |
| **Numeric values** |     |
| [`decimal(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.decimal "unicodedata.decimal") | Decimal value of a character |
| [`digit(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.digit "unicodedata.digit") | Digit value of a character |
| [`numeric(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.numeric "unicodedata.numeric") | Numeric value of a character |
| **Properties** |     |
| [`bidirectional(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.bidirectional "unicodedata.bidirectional") | Bidirectional class of a character |
| [`block(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.block "unicodedata.block") | Unicode block of a character |
| [`category(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.category "unicodedata.category") | General category of a character |
| [`combining(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.combining "unicodedata.combining") | Canonical combining class of a character |
| [`decomposition(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.decomposition "unicodedata.decomposition") | Character decomposition mapping |
| [`east_asian_width(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.east_asian_width "unicodedata.east_asian_width") | East Asian width of a character |
| [`extended_pictographic(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.extended_pictographic "unicodedata.extended_pictographic") | Check if a character has the Extended\_Pictographic property |
| [`grapheme_cluster_break(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.grapheme_cluster_break "unicodedata.grapheme_cluster_break") | Grapheme\_Cluster\_Break property of a character |
| [`indic_conjunct_break(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.indic_conjunct_break "unicodedata.indic_conjunct_break") | Indic\_Conjunct\_Break property of a character |
| [`isxidcontinue(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.isxidcontinue "unicodedata.isxidcontinue") | Check if a character is a valid identifier continuation |
| [`isxidstart(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.isxidstart "unicodedata.isxidstart") | Check if a character is a valid identifier start |
| [`mirrored(chr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.mirrored "unicodedata.mirrored") | Mirrored property of a character |
| **Normalization** |     |
| [`normalize(form, unistr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "unicodedata.normalize") | Return the normalized form of a string |
| [`is_normalized(form, unistr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.is_normalized "unicodedata.is_normalized") | Check if a Unicode string is normalized |
| **Text segmentation** |     |
| [`iter_graphemes(unistr)`](https://docs.python.org/3/library/unicodedata.html#unicodedata.iter_graphemes "unicodedata.iter_graphemes") | Iterate over grapheme clusters in a string |

unicodedata.lookup(_name_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.lookup "Link to this definition")

Look up character by name. If a character with the given name is found, return the corresponding character. If not found, [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised. For example:

Copy

\>>> unicodedata.lookup('LEFT CURLY BRACKET')
'{'

The characters returned by this function are the same as those produced by `\N` escape sequence in string literals. For example:

Copy

\>>> unicodedata.lookup('MIDDLE DOT') \== '\\N{MIDDLE DOT}'
True

Changed in version 3.3: Support for name aliases [\[1\]](https://docs.python.org/3/library/unicodedata.html#id4)
 and named sequences [\[2\]](https://docs.python.org/3/library/unicodedata.html#id5)
 has been added.

unicodedata.name(_chr_, _default\=None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.name "Link to this definition")

Returns the name assigned to the character _chr_ as a string. If no name is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. For example:

Copy

\>>> unicodedata.name('½')
'VULGAR FRACTION ONE HALF'
\>>> unicodedata.name('\\uFFFF', 'fallback')
'fallback'

unicodedata.decimal(_chr_, _default\=None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.decimal "Link to this definition")

Returns the decimal value assigned to the character _chr_ as integer. If no such value is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. For example:

Copy

\>>> unicodedata.decimal('\\N{ARABIC-INDIC DIGIT NINE}')
9
\>>> unicodedata.decimal('\\N{SUPERSCRIPT NINE}', \-1)
\-1

unicodedata.digit(_chr_, _default\=None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.digit "Link to this definition")

Returns the digit value assigned to the character _chr_ as integer. If no such value is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised:

Copy

\>>> unicodedata.digit('\\N{SUPERSCRIPT NINE}')
9

unicodedata.numeric(_chr_, _default\=None_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.numeric "Link to this definition")

Returns the numeric value assigned to the character _chr_ as float. If no such value is defined, _default_ is returned, or, if not given, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised:

Copy

\>>> unicodedata.numeric('½')
0.5

unicodedata.category(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.category "Link to this definition")

Returns the general category assigned to the character _chr_ as string. General category names consist of two letters. See the [General Category Values section of the Unicode Character Database documentation](https://www.unicode.org/reports/tr44/#General_Category_Values)
 for a list of category codes. For example:

Copy

\>>> unicodedata.category('A')  \# 'L'etter, 'u'ppercase
'Lu'

unicodedata.bidirectional(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.bidirectional "Link to this definition")

Returns the bidirectional class assigned to the character _chr_ as string. If no such value is defined, an empty string is returned. See the [Bidirectional Class Values section of the Unicode Character Database](https://www.unicode.org/reports/tr44/#Bidi_Class_Values)
 documentation for a list of bidirectional codes. For example:

Copy

\>>> unicodedata.bidirectional('\\N{ARABIC-INDIC DIGIT SEVEN}') \# 'A'rabic, 'N'umber
'AN'

unicodedata.combining(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.combining "Link to this definition")

Returns the canonical combining class assigned to the character _chr_ as integer. Returns `0` if no combining class is defined. See the [Canonical Combining Class Values section of the Unicode Character Database](https://www.unicode.org/reports/tr44/#Canonical_Combining_Class_Values)
 for more information.

unicodedata.east\_asian\_width(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.east_asian_width "Link to this definition")

Returns the east asian width assigned to the character _chr_ as string. For a list of widths and or more information, see the [Unicode Standard Annex #11](https://www.unicode.org/reports/tr11/)
.

unicodedata.block(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.block "Link to this definition")

Returns the [block](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G64189)
 assigned to the character _chr_. For example:

Copy

\>>> unicodedata.block('S')
'Basic Latin'

Added in version 3.15.

unicodedata.mirrored(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.mirrored "Link to this definition")

Returns the mirrored property assigned to the character _chr_ as integer. Returns `1` if the character has been identified as a “mirrored” character in bidirectional text, `0` otherwise. For example:

Copy

\>>> unicodedata.mirrored('>')
1

unicodedata.isxidstart(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.isxidstart "Link to this definition")

Return `True` if _chr_ is a valid identifier start per the [Unicode Standard Annex #31](https://www.unicode.org/reports/tr31/)
, that is, it has the `XID_Start` property. Return `False` otherwise. For example:

Copy

\>>> unicodedata.isxidstart('S')
True
\>>> unicodedata.isxidstart('0')
False

Added in version 3.15.

unicodedata.isxidcontinue(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.isxidcontinue "Link to this definition")

Return `True` if _chr_ is a valid identifier character per the [Unicode Standard Annex #31](https://www.unicode.org/reports/tr31/)
, that is, it has the `XID_Continue` property. Return `False` otherwise. For example:

Copy

\>>> unicodedata.isxidcontinue('S')
True
\>>> unicodedata.isxidcontinue(' ')
False

Added in version 3.15.

unicodedata.decomposition(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.decomposition "Link to this definition")

Returns the character decomposition mapping assigned to the character _chr_ as string. An empty string is returned in case no such mapping is defined. For example:

Copy

\>>> unicodedata.decomposition('Ã')
'0041 0303'

unicodedata.grapheme\_cluster\_break(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.grapheme_cluster_break "Link to this definition")

Returns the Grapheme\_Cluster\_Break property assigned to the character.

Added in version 3.15.

unicodedata.indic\_conjunct\_break(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.indic_conjunct_break "Link to this definition")

Returns the Indic\_Conjunct\_Break property assigned to the character.

Added in version 3.15.

unicodedata.extended\_pictographic(_chr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.extended_pictographic "Link to this definition")

Returns `True` if the character has the Extended\_Pictographic property, `False` otherwise.

Added in version 3.15.

unicodedata.normalize(_form_, _unistr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "Link to this definition")

Return the normal form _form_ for the Unicode string _unistr_. Valid values for _form_ are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

The Unicode standard defines various normalization forms of a Unicode string, based on the definition of canonical equivalence and compatibility equivalence. In Unicode, several characters can be expressed in various way. For example, the character U+00C7 (LATIN CAPITAL LETTER C WITH CEDILLA) can also be expressed as the sequence U+0043 (LATIN CAPITAL LETTER C) U+0327 (COMBINING CEDILLA).

For each character, there are two normal forms: normal form C and normal form D. Normal form D (NFD) is also known as canonical decomposition, and translates each character into its decomposed form. Normal form C (NFC) first applies a canonical decomposition, then composes pre-combined characters again.

In addition to these two forms, there are two additional normal forms based on compatibility equivalence. In Unicode, certain characters are supported which normally would be unified with other characters. For example, U+2160 (ROMAN NUMERAL ONE) is really the same thing as U+0049 (LATIN CAPITAL LETTER I). However, it is supported in Unicode for compatibility with existing character sets (for example, gb2312).

The normal form KD (NFKD) will apply the compatibility decomposition, that is, replace all compatibility characters with their equivalents. The normal form KC (NFKC) first applies the compatibility decomposition, followed by the canonical composition.

Even if two unicode strings are normalized and look the same to a human reader, if one has combining characters and the other doesn’t, they may not compare equal.

unicodedata.is\_normalized(_form_, _unistr_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.is_normalized "Link to this definition")

Return whether the Unicode string _unistr_ is in the normal form _form_. Valid values for _form_ are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

Added in version 3.8.

unicodedata.iter\_graphemes(_unistr_, _start\=0_, _end\=sys.maxsize_, _/_)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.iter_graphemes "Link to this definition")

Returns an iterator to iterate over grapheme clusters. With optional _start_, iteration begins at that position. With optional _end_, iteration stops at that position.

Converting an emitted item to string returns a substring corresponding to the grapheme cluster. Its `start` and `end` attributes denote the start and end of the grapheme cluster.

It uses extended grapheme cluster rules defined by Unicode Standard Annex #29, [“Unicode Text Segmentation”](https://www.unicode.org/reports/tr29/)
.

Added in version 3.15.

In addition, the module exposes the following constants:

unicodedata.unidata\_version[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.unidata_version "Link to this definition")

The version of the Unicode database used in this module.

unicodedata.ucd\_3\_2\_0[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.ucd_3_2_0 "Link to this definition")

This is an object that has most of the methods of the entire module, but uses the Unicode database version 3.2 instead, for applications that require this specific version of the Unicode database (such as IDNA).

Footnotes

#### Previous topic

[`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html "previous chapter")

#### Next topic

[`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unicodedata+%E2%80%94+Unicode+Database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funicodedata.html&pagesource=library%2Funicodedata.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/unicodedata.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/stringprep.html "stringprep — Internet String Preparation")
     |
*   [previous](https://docs.python.org/3/library/textwrap.html "textwrap — Text wrapping and filling")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
    
*    
    
    |
*   Theme Auto Light Dark |