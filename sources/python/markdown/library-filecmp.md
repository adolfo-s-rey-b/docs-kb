### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories")
     |
*   [previous](https://docs.python.org/3/library/stat.html "stat — Interpreting stat() results")
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
*   [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`filecmp` — File and Directory Comparisons[¶](https://docs.python.org/3/library/filecmp.html#module-filecmp "Link to this heading")

====================================================================================================================================

**Source code:** [Lib/filecmp.py](https://github.com/python/cpython/tree/3.15/Lib/filecmp.py)

* * *

The `filecmp` module defines functions to compare files and directories, with various optional time/correctness trade-offs. For comparing files, see also the [`difflib`](https://docs.python.org/3/library/difflib.html#module-difflib "difflib: Helpers for computing differences between objects.")
 module.

The `filecmp` module defines the following functions:

filecmp.cmp(_f1_, _f2_, _shallow\=True_)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "Link to this definition")

Compare the files named _f1_ and _f2_, returning `True` if they seem equal, `False` otherwise.

If _shallow_ is true and the [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 signatures (file type, size, and modification time) of both files are identical, the files are taken to be equal.

Otherwise, the files are treated as different if their sizes or contents differ.

Note that no external programs are called from this function, giving it portability and efficiency.

This function uses a cache for past comparisons and the results, with cache entries invalidated if the [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 information for the file changes. The entire cache may be cleared using [`clear_cache()`](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "filecmp.clear_cache")
.

filecmp.cmpfiles(_a_, _b_, _common_, _shallow\=True_)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.cmpfiles "Link to this definition")

Compare the files in the two directories _a_ and _b_ whose names are given by _common_.

Returns three lists of file names: _match_, _mismatch_, _errors_. _match_ contains the list of files that match, _mismatch_ contains the names of those that don’t, and _errors_ lists the names of files which could not be compared. Files are listed in _errors_ if they don’t exist in one of the directories, the user lacks permission to read them or if the comparison could not be done for some other reason.

The _shallow_ parameter has the same meaning and default value as for [`filecmp.cmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "filecmp.cmp")
.

For example, `cmpfiles('a', 'b', ['c', 'd/e'])` will compare `a/c` with `b/c` and `a/d/e` with `b/d/e`. `'c'` and `'d/e'` will each be in one of the three returned lists.

filecmp.clear\_cache()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "Link to this definition")

Clear the filecmp cache. This may be useful if a file is compared so quickly after it is modified that it is within the mtime resolution of the underlying filesystem.

Added in version 3.4.

The [`dircmp`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "filecmp.dircmp")
 class[¶](https://docs.python.org/3/library/filecmp.html#the-dircmp-class "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class filecmp.dircmp(_a_, _b_, _ignore\=None_, _hide\=None_, _\*_, _shallow\=True_)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "Link to this definition")

Construct a new directory comparison object, to compare the directories _a_ and _b_. _ignore_ is a list of names to ignore, and defaults to [`filecmp.DEFAULT_IGNORES`](https://docs.python.org/3/library/filecmp.html#filecmp.DEFAULT_IGNORES "filecmp.DEFAULT_IGNORES")
. _hide_ is a list of names to hide, and defaults to `[os.curdir, os.pardir]`.

The `dircmp` class compares files by doing _shallow_ comparisons as described for [`filecmp.cmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "filecmp.cmp")
 by default using the _shallow_ parameter.

Changed in version 3.13: Added the _shallow_ parameter.

The `dircmp` class provides the following methods:

report()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report "Link to this definition")

Print (to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
) a comparison between _a_ and _b_.

report\_partial\_closure()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report_partial_closure "Link to this definition")

Print a comparison between _a_ and _b_ and common immediate subdirectories.

report\_full\_closure()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report_full_closure "Link to this definition")

Print a comparison between _a_ and _b_ and common subdirectories (recursively).

The `dircmp` class offers a number of interesting attributes that may be used to get various bits of information about the directory trees being compared.

Note that via [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
 hooks, all attributes are computed lazily, so there is no speed penalty if only those attributes which are lightweight to compute are used.

left[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left "Link to this definition")

The directory _a_.

right[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right "Link to this definition")

The directory _b_.

left\_list[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left_list "Link to this definition")

Files and subdirectories in _a_, filtered by _hide_ and _ignore_.

right\_list[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right_list "Link to this definition")

Files and subdirectories in _b_, filtered by _hide_ and _ignore_.

common[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common "Link to this definition")

Files and subdirectories in both _a_ and _b_.

left\_only[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left_only "Link to this definition")

Files and subdirectories only in _a_.

right\_only[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right_only "Link to this definition")

Files and subdirectories only in _b_.

common\_dirs[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_dirs "Link to this definition")

Subdirectories in both _a_ and _b_.

common\_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_files "Link to this definition")

Files in both _a_ and _b_.

common\_funny[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_funny "Link to this definition")

Names in both _a_ and _b_, such that the type differs between the directories, or names for which [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 reports an error.

same\_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.same_files "Link to this definition")

Files which are identical in both _a_ and _b_, using the class’s file comparison operator.

diff\_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.diff_files "Link to this definition")

Files which are in both _a_ and _b_, whose contents differ according to the class’s file comparison operator.

funny\_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.funny_files "Link to this definition")

Files which are in both _a_ and _b_, but could not be compared.

subdirs[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.subdirs "Link to this definition")

A dictionary mapping names in [`common_dirs`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_dirs "filecmp.dircmp.common_dirs")
 to `dircmp` instances (or MyDirCmp instances if this instance is of type MyDirCmp, a subclass of `dircmp`).

Changed in version 3.10: Previously entries were always `dircmp` instances. Now entries are the same type as _self_, if _self_ is a subclass of `dircmp`.

filecmp.DEFAULT\_IGNORES[¶](https://docs.python.org/3/library/filecmp.html#filecmp.DEFAULT_IGNORES "Link to this definition")

Added in version 3.4.

List of directories ignored by [`dircmp`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "filecmp.dircmp")
 by default.

Here is a simplified example of using the `subdirs` attribute to search recursively through two directories to show common different files:

Copy

\>>> from filecmp import dircmp
\>>> def print\_diff\_files(dcmp):
...     for name in dcmp.diff\_files:
...         print("diff\_file %s found in %s and %s" % (name, dcmp.left,
...               dcmp.right))
...     for sub\_dcmp in dcmp.subdirs.values():
...         print\_diff\_files(sub\_dcmp)
...
\>>> dcmp \= dircmp('dir1', 'dir2')
\>>> print\_diff\_files(dcmp)

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html#)
    *   [The `dircmp` class](https://docs.python.org/3/library/filecmp.html#the-dircmp-class)
        

#### Previous topic

[`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html "previous chapter")

#### Next topic

[`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=filecmp+%E2%80%94+File+and+Directory+Comparisons&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffilecmp.html&pagesource=library%2Ffilecmp.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/filecmp.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories")
     |
*   [previous](https://docs.python.org/3/library/stat.html "stat — Interpreting stat() results")
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
*   [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
    
*    
    
    |
*   Theme Auto Light Dark |