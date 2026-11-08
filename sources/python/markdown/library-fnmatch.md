### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/linecache.html "linecache — Random access to text lines")
     |
*   [previous](https://docs.python.org/3/library/glob.html "glob — Unix style pathname pattern expansion")
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
*   [File and Directory Access](https://docs.python.org/3/library/filesys.html)
     »
*   [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`fnmatch` — Unix filename pattern matching[¶](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "Link to this heading")

====================================================================================================================================

**Source code:** [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.15/Lib/fnmatch.py)

* * *

This module provides support for Unix shell-style wildcards, which are _not_ the same as regular expressions (which are documented in the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
 module). The special characters used in shell-style wildcards are:

| Pattern | Meaning |
| --- | --- |
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in _seq_ |
| `[!seq]` | matches any character not in _seq_ |

For a literal match, wrap the meta-characters in brackets. For example, `'[?]'` matches the character `'?'`.

Note that the filename separator (`'/'` on Unix) is _not_ special to this module. See module [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.")
 for pathname expansion (`glob` uses [`filter()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "fnmatch.filter")
 to match pathname segments). Similarly, filenames starting with a period are not special for this module, and are matched by the `*` and `?` patterns.

Unless stated otherwise, “filename string” and “pattern string” either refer to [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `ISO-8859-1` encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects. Note that the functions documented below do not allow to mix a `bytes` pattern with a `str` filename, and vice-versa.

Finally, note that [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache")
 with a _maxsize_ of 32768 is used to cache the (typed) compiled regex patterns in the following functions: [`fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch")
, [`fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase")
, [`filter()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "fnmatch.filter")
, [`filterfalse()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filterfalse "fnmatch.filterfalse")
.

fnmatch.fnmatch(_name_, _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "Link to this definition")

Test whether the filename string _name_ matches the pattern string _pat_, returning `True` or `False`. Both parameters are case-normalized using [`os.path.normcase()`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase")
. [`fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase")
 can be used to perform a case-sensitive comparison, regardless of whether that’s standard for the operating system.

This example will print all file names in the current directory with the extension `.txt`:

Copy

import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '\*.txt'):
        print(file)

fnmatch.fnmatchcase(_name_, _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "Link to this definition")

Test whether the filename string _name_ matches the pattern string _pat_, returning `True` or `False`; the comparison is case-sensitive and does not apply [`os.path.normcase()`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase")
.

fnmatch.filter(_names_, _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "Link to this definition")

Construct a list from those elements of the [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 of filename strings _names_ that match the pattern string _pat_. It is the same as `[n for n in names if fnmatch(n, pat)]`, but implemented more efficiently.

fnmatch.filterfalse(_names_, _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.filterfalse "Link to this definition")

Construct a list from those elements of the [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 of filename strings _names_ that do not match the pattern string _pat_. It is the same as `[n for n in names if not fnmatch(n, pat)]`, but implemented more efficiently.

Added in version 3.14.

fnmatch.translate(_pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.translate "Link to this definition")

Return the shell-style pattern _pat_ converted to a regular expression for using with [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")
. The pattern is expected to be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
.

Example:

Copy

\>>> import fnmatch, re
\>>>
\>>> regex \= fnmatch.translate('\*.txt')
\>>> regex
'(?s:.\*\\\\.txt)\\\\z'
\>>> reobj \= re.compile(regex)
\>>> reobj.prefixmatch('foobar.txt')
<re.Match object; span=(0, 10), match='foobar.txt'>

See also

Module [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.")

Unix shell-style path expansion.

#### Previous topic

[`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html "previous chapter")

#### Next topic

[`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fnmatch+%E2%80%94+Unix+filename+pattern+matching&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffnmatch.html&pagesource=library%2Ffnmatch.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/fnmatch.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/linecache.html "linecache — Random access to text lines")
     |
*   [previous](https://docs.python.org/3/library/glob.html "glob — Unix style pathname pattern expansion")
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
*   [File and Directory Access](https://docs.python.org/3/library/filesys.html)
     »
*   [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
    
*    
    
    |
*   Theme Auto Light Dark |