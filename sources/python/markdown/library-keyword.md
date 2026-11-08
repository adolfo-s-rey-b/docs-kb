### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tokenize.html "tokenize — Tokenizer for Python source")
     |
*   [previous](https://docs.python.org/3/library/token.html "token — Constants used with Python parse trees")
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
*   [Python Language Services](https://docs.python.org/3/library/language.html)
     »
*   [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`keyword` — Testing for Python keywords[¶](https://docs.python.org/3/library/keyword.html#module-keyword "Link to this heading")

=================================================================================================================================

**Source code:** [Lib/keyword.py](https://github.com/python/cpython/tree/3.15/Lib/keyword.py)

* * *

This module allows a Python program to determine if a string is a [keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
 or [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
.

keyword.iskeyword(_s_)[¶](https://docs.python.org/3/library/keyword.html#keyword.iskeyword "Link to this definition")

Return `True` if _s_ is a Python [keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
.

keyword.kwlist[¶](https://docs.python.org/3/library/keyword.html#keyword.kwlist "Link to this definition")

Sequence containing all the [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
 defined for the interpreter. If any keywords are defined to only be active when particular [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
 statements are in effect, these will be included as well.

keyword.issoftkeyword(_s_)[¶](https://docs.python.org/3/library/keyword.html#keyword.issoftkeyword "Link to this definition")

Return `True` if _s_ is a Python [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
.

Added in version 3.9.

keyword.softkwlist[¶](https://docs.python.org/3/library/keyword.html#keyword.softkwlist "Link to this definition")

Sequence containing all the [soft keywords](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
 defined for the interpreter. If any soft keywords are defined to only be active when particular [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
 statements are in effect, these will be included as well.

Added in version 3.9.

#### Previous topic

[`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html "previous chapter")

#### Next topic

[`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=keyword+%E2%80%94+Testing+for+Python+keywords&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fkeyword.html&pagesource=library%2Fkeyword.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/keyword.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tokenize.html "tokenize — Tokenizer for Python source")
     |
*   [previous](https://docs.python.org/3/library/token.html "token — Constants used with Python parse trees")
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
*   [Python Language Services](https://docs.python.org/3/library/language.html)
     »
*   [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
    
*    
    
    |
*   Theme Auto Light Dark |