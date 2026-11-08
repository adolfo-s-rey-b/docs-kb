### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.html "XML Processing Modules")
     |
*   [previous](https://docs.python.org/3/library/html.parser.html "html.parser — Simple HTML and XHTML parser")
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
*   [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html)
     »
*   [`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`html.entities` — Definitions of HTML general entities[¶](https://docs.python.org/3/library/html.entities.html#module-html.entities "Link to this heading")

============================================================================================================================================================

**Source code:** [Lib/html/entities.py](https://github.com/python/cpython/tree/3.15/Lib/html/entities.py)

* * *

This module defines four dictionaries, [`html5`](https://docs.python.org/3/library/html.entities.html#html.entities.html5 "html.entities.html5")
, [`name2codepoint`](https://docs.python.org/3/library/html.entities.html#html.entities.name2codepoint "html.entities.name2codepoint")
, [`codepoint2name`](https://docs.python.org/3/library/html.entities.html#html.entities.codepoint2name "html.entities.codepoint2name")
, and [`entitydefs`](https://docs.python.org/3/library/html.entities.html#html.entities.entitydefs "html.entities.entitydefs")
.

html.entities.html5[¶](https://docs.python.org/3/library/html.entities.html#html.entities.html5 "Link to this definition")

A dictionary that maps HTML5 named character references [\[1\]](https://docs.python.org/3/library/html.entities.html#id2)
 to the equivalent Unicode character(s), e.g. `html5['gt;'] == '>'`. Note that the trailing semicolon is included in the name (e.g. `'gt;'`), however some of the names are accepted by the standard even without the semicolon: in this case the name is present with and without the `';'`. See also [`html.unescape()`](https://docs.python.org/3/library/html.html#html.unescape "html.unescape")
.

Added in version 3.3.

html.entities.entitydefs[¶](https://docs.python.org/3/library/html.entities.html#html.entities.entitydefs "Link to this definition")

A dictionary mapping XHTML 1.0 entity definitions to their replacement text in ISO Latin-1.

html.entities.name2codepoint[¶](https://docs.python.org/3/library/html.entities.html#html.entities.name2codepoint "Link to this definition")

A dictionary that maps HTML4 entity names to the Unicode code points.

html.entities.codepoint2name[¶](https://docs.python.org/3/library/html.entities.html#html.entities.codepoint2name "Link to this definition")

A dictionary that maps Unicode code points to HTML4 entity names.

Footnotes

#### Previous topic

[`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html "previous chapter")

#### Next topic

[XML Processing Modules](https://docs.python.org/3/library/xml.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=html.entities+%E2%80%94+Definitions+of+HTML+general+entities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhtml.entities.html&pagesource=library%2Fhtml.entities.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/html.entities.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/xml.html "XML Processing Modules")
     |
*   [previous](https://docs.python.org/3/library/html.parser.html "html.parser — Simple HTML and XHTML parser")
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
*   [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html)
     »
*   [`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html)
    
*    
    
    |
*   Theme Auto Light Dark |