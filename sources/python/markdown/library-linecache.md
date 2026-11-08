### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/shutil.html "shutil — High-level file operations")
     |
*   [previous](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching")
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
*   [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`linecache` — Random access to text lines[¶](https://docs.python.org/3/library/linecache.html#module-linecache "Link to this heading")

=======================================================================================================================================

**Source code:** [Lib/linecache.py](https://github.com/python/cpython/tree/3.15/Lib/linecache.py)

* * *

The `linecache` module allows one to get any line from a Python source file, while attempting to optimize internally, using a cache, the common case where many lines are read from a single file. This is used by the [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")
 module to retrieve source lines for inclusion in the formatted traceback.

The [`tokenize.open()`](https://docs.python.org/3/library/tokenize.html#tokenize.open "tokenize.open")
 function is used to open files. This function uses [`tokenize.detect_encoding()`](https://docs.python.org/3/library/tokenize.html#tokenize.detect_encoding "tokenize.detect_encoding")
 to get the encoding of the file; in the absence of an encoding token, the file encoding defaults to UTF-8.

The `linecache` module defines the following functions:

linecache.getline(_filename_, _lineno_, _module\_globals\=None_)[¶](https://docs.python.org/3/library/linecache.html#linecache.getline "Link to this definition")

Get line _lineno_ from file named _filename_. This function will never raise an exception — it will return `''` on errors (the terminating newline character will be included for lines that are found).

If _filename_ indicates a frozen module (starting with `'<frozen '`), the function will attempt to get the real file name from `module_globals['__file__']` if _module\_globals_ is not `None`.

If a file named _filename_ is not found, the function first checks for a [**PEP 302**](https://peps.python.org/pep-0302/)
 `__loader__` in _module\_globals_. If there is such a loader and it defines a `get_source` method, then that determines the source lines (if `get_source()` returns `None`, then `''` is returned). Finally, if _filename_ is a relative filename, it is looked up relative to the entries in the module search path, `sys.path`.

Changed in version 3.14: Support _filename_ of frozen modules.

linecache.clearcache()[¶](https://docs.python.org/3/library/linecache.html#linecache.clearcache "Link to this definition")

Clear the cache. Use this function if you no longer need lines from files previously read using [`getline()`](https://docs.python.org/3/library/linecache.html#linecache.getline "linecache.getline")
.

linecache.checkcache(_filename\=None_)[¶](https://docs.python.org/3/library/linecache.html#linecache.checkcache "Link to this definition")

Check the cache for validity. Use this function if files in the cache may have changed on disk, and you require the updated version. If _filename_ is omitted, it will check all the entries in the cache.

linecache.lazycache(_filename_, _module\_globals_)[¶](https://docs.python.org/3/library/linecache.html#linecache.lazycache "Link to this definition")

Capture enough detail about a non-file-based module to permit getting its lines later via [`getline()`](https://docs.python.org/3/library/linecache.html#linecache.getline "linecache.getline")
 even if _module\_globals_ is `None` in the later call. This avoids doing I/O until a line is actually needed, without having to carry the module globals around indefinitely.

Added in version 3.5.

Example:

Copy

\>>> import linecache
\>>> linecache.getline(linecache.\_\_file\_\_, 8)
'import sys\\n'

#### Previous topic

[`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html "previous chapter")

#### Next topic

[`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=linecache+%E2%80%94+Random+access+to+text+lines&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flinecache.html&pagesource=library%2Flinecache.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/linecache.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/shutil.html "shutil — High-level file operations")
     |
*   [previous](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching")
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
*   [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
    
*    
    
    |
*   Theme Auto Light Dark |