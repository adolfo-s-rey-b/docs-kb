### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching")
     |
*   [previous](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories")
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
*   [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`glob` — Unix style pathname pattern expansion[¶](https://docs.python.org/3/library/glob.html#module-glob "Link to this heading")

==================================================================================================================================

**Source code:** [Lib/glob.py](https://github.com/python/cpython/tree/3.15/Lib/glob.py)

* * *

The `glob` module finds pathnames using pattern matching rules similar to the Unix shell. No tilde expansion is done, but `*`, `?`, and character ranges expressed with `[]` will be correctly matched. This is done by using the [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 and [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch")
 functions in concert, and not by actually invoking a subshell.

Note

The pathnames are returned in no particular order. If you need a specific order, sort the results.

By default, files beginning with a dot (`.`) can only be matched by patterns that also start with a dot, unlike [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch")
 or [`pathlib.Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob")
. For tilde and shell variable expansion, use [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser")
 and [`os.path.expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars")
.

For a literal match, wrap the meta-characters in brackets. For example, `'[?]'` matches the character `'?'`.

The `glob` module defines the following functions:

glob.glob(_pathname_, _\*_, _root\_dir\=None_, _dir\_fd\=None_, _recursive\=False_, _include\_hidden\=False_)[¶](https://docs.python.org/3/library/glob.html#glob.glob "Link to this definition")

Return a possibly empty list of path names that match _pathname_, which must be a string containing a path specification. _pathname_ can be either absolute (like `/usr/src/Python-1.5/Makefile`) or relative (like `../../Tools/*/*.gif`), and can contain shell-style wildcards. Broken symlinks are included in the results (as in the shell). Whether or not the results are sorted depends on the file system. If a file that satisfies conditions is removed or added during the call of this function, whether a path name for that file will be included is unspecified.

If _root\_dir_ is not `None`, it should be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 specifying the root directory for searching. It has the same effect on `glob()` as changing the current directory before calling it. If _pathname_ is relative, the result will contain paths relative to _root\_dir_.

This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 with the _dir\_fd_ parameter.

If _recursive_ is true, the pattern “`**`” will match any files and zero or more directories, subdirectories and symbolic links to directories. If the pattern is followed by an [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep")
 or [`os.altsep`](https://docs.python.org/3/library/os.html#os.altsep "os.altsep")
 then files will not match.

If _include\_hidden_ is true, wildcards can match path segments that begin with a dot (`.`).

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `glob.glob` with arguments `pathname`, `recursive`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

Note

Using the “`**`” pattern in large directory trees may consume an inordinate amount of time.

Note

This function may return duplicate path names if _pathname_ contains multiple “`**`” patterns and _recursive_ is true.

Note

Any [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exceptions raised from scanning the filesystem are suppressed. This includes [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
 when accessing directories without read permission.

Changed in version 3.5: Support for recursive globs using “`**`”.

Changed in version 3.10: Added the _root\_dir_ and _dir\_fd_ parameters.

Changed in version 3.11: Added the _include\_hidden_ parameter.

glob.iglob(_pathname_, _\*_, _root\_dir\=None_, _dir\_fd\=None_, _recursive\=False_, _include\_hidden\=False_)[¶](https://docs.python.org/3/library/glob.html#glob.iglob "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 which yields the same values as [`glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob")
 without actually storing them all simultaneously.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `glob.glob` with arguments `pathname`, `recursive`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

Note

This function may return duplicate path names if _pathname_ contains multiple “`**`” patterns and _recursive_ is true.

Note

Any [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exceptions raised from scanning the filesystem are suppressed. This includes [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
 when accessing directories without read permission.

Changed in version 3.5: Support for recursive globs using “`**`”.

Changed in version 3.10: Added the _root\_dir_ and _dir\_fd_ parameters.

Changed in version 3.11: Added the _include\_hidden_ parameter.

glob.escape(_pathname_)[¶](https://docs.python.org/3/library/glob.html#glob.escape "Link to this definition")

Escape all special characters (`'?'`, `'*'` and `'['`). This is useful if you want to match an arbitrary literal string that may have special characters in it. Special characters in drive/UNC sharepoints are not escaped, for example on Windows `escape('//?/c:/Quo vadis?.txt')` returns `'//?/c:/Quo vadis[?].txt'`.\
\
Added in version 3.4.\
\
glob.translate(_pathname_, _\*_, _recursive\=False_, _include\_hidden\=False_, _seps\=None_)[¶](https://docs.python.org/3/library/glob.html#glob.translate "Link to this definition")\
\
Convert the given path specification to a regular expression for use with [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")\
. The path specification can contain shell-style wildcards.\
\
For example:\
\
Copy\
\
\>>> import glob, re\
\>>>\
\>>> regex \= glob.translate('\*\*/\*.txt', recursive\=True, include\_hidden\=True)\
\>>> regex\
'(?s:(?:.+/)?\[^/\]\*\\\\.txt)\\\\z'\
\>>> reobj \= re.compile(regex)\
\>>> reobj.prefixmatch('foo/bar/baz.txt')\
<re.Match object; span=(0, 15), match='foo/bar/baz.txt'>\
\
Path separators and segments are meaningful to this function, unlike [`fnmatch.translate()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.translate "fnmatch.translate")\
. By default wildcards do not match path separators, and `*` pattern segments match precisely one path segment.\
\
If _recursive_ is true, the pattern segment “`**`” will match any number of path segments.\
\
If _include\_hidden_ is true, wildcards can match path segments that start with a dot (`.`).\
\
A sequence of path separators may be supplied to the _seps_ argument. If not given, [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep")\
 and [`altsep`](https://docs.python.org/3/library/os.html#os.altsep "os.altsep")\
 (if available) are used.\
\
See also\
\
[`pathlib.PurePath.full_match()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.full_match "pathlib.PurePath.full_match")\
 and [`pathlib.Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob")\
 methods, which call this function to implement pattern matching and globbing.\
\
Added in version 3.13.\
\
Examples[¶](https://docs.python.org/3/library/glob.html#examples "Link to this heading")\
\
-----------------------------------------------------------------------------------------\
\
Consider a directory containing the following files: `1.gif`, `2.txt`, `card.gif` and a subdirectory `sub` which contains only the file `3.txt`. [`glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob")\
 will produce the following results. Notice how any leading components of the path are preserved.\
\
Copy\
\
\>>> import glob\
\>>> glob.glob('./\[0-9\].\*')\
\['./1.gif', './2.txt'\]\
\>>> glob.glob('\*.gif')\
\['1.gif', 'card.gif'\]\
\>>> glob.glob('?.gif')\
\['1.gif'\]\
\>>> glob.glob('\*\*/\*.txt', recursive\=True)\
\['2.txt', 'sub/3.txt'\]\
\>>> glob.glob('./\*\*/', recursive\=True)\
\['./', './sub/'\]\
\
If the directory contains files starting with `.` they won’t be matched by default. For example, consider a directory containing `card.gif` and `.card.gif`:\
\
Copy\
\
\>>> import glob\
\>>> glob.glob('\*.gif')\
\['card.gif'\]\
\>>> glob.glob('.c\*')\
\['.card.gif'\]\
\
See also\
\
The [`fnmatch`](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching.")\
 module offers shell-style filename (not path) expansion.\
\
See also\
\
The [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")\
 module offers high-level path objects.\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html#)\
    *   [Examples](https://docs.python.org/3/library/glob.html#examples)\
        \
\
#### Previous topic\
\
[`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html "previous chapter")\
\
#### Next topic\
\
[`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=glob+%E2%80%94+Unix+style+pathname+pattern+expansion&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fglob.html&pagesource=library%2Fglob.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/glob.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching")\
     |\
*   [previous](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python standard library](https://docs.python.org/3/library/index.html)\
     »\
*   [File and Directory Access](https://docs.python.org/3/library/filesys.html)\
     »\
*   [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |