### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Soft deprecations](https://docs.python.org/3/deprecations/soft-deprecations.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Soft deprecations[¶](https://docs.python.org/3/deprecations/soft-deprecations.html#soft-deprecations "Link to this heading")

=============================================================================================================================

There are no plans to remove [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 APIs.

*   [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match")
     and [`re.Pattern.match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match")
     are now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     in favor of the new [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")
     and [`re.Pattern.prefixmatch()`](https://docs.python.org/3/library/re.html#re.Pattern.prefixmatch "re.Pattern.prefixmatch")
     APIs, which have been added as alternate, more explicit names. These are intended to be used to alleviate confusion around what _match_ means by following the Zen of Python’s _“Explicit is better than implicit”_ mantra. Most other language regular expression libraries use an API named _match_ to mean what Python has always called _search_.
    
    We **do not** plan to remove the older `match()` name, as it has been used in code for over 30 years. Code supporting older versions of Python should continue to use `match()`, while new code should prefer `prefixmatch()`. See [prefixmatch() vs. match()](https://docs.python.org/3/library/re.html#prefixmatch-vs-match)
    .
    
    (Contributed by Gregory P. Smith in [gh-86519](https://github.com/python/cpython/issues/86519)
     and Hugo van Kemenade in [gh-148100](https://github.com/python/cpython/issues/148100)
    .)
    
*   Using `'F'` and `'D'` format type codes of the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
     module now are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     in favor of two-letter forms `'Zf'` and `'Zd'`. (Contributed by Sergey B Kirpichev in [gh-121249](https://github.com/python/cpython/issues/121249)
    .)
    

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Soft+deprecations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fsoft-deprecations.html&pagesource=deprecations%2Fsoft-deprecations.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/soft-deprecations.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Soft deprecations](https://docs.python.org/3/deprecations/soft-deprecations.html)
    
*    
    
    |
*   Theme Auto Light Dark |