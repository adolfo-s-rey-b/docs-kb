### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/dis.html "dis — Disassembler for Python bytecode")
     |
*   [previous](https://docs.python.org/3/library/py_compile.html "py_compile — Compile Python source files")
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
*   [`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`compileall` — Byte-compile Python libraries[¶](https://docs.python.org/3/library/compileall.html#module-compileall "Link to this heading")

============================================================================================================================================

**Source code:** [Lib/compileall.py](https://github.com/python/cpython/tree/3.15/Lib/compileall.py)

* * *

This module provides some utility functions to support installing Python libraries. These functions compile Python source files in a directory tree. This module can be used to create the cached byte-code files at library installation time, which makes them available for use even by users who don’t have write permission to the library directories.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Command-line use[¶](https://docs.python.org/3/library/compileall.html#command-line-use "Link to this heading")

---------------------------------------------------------------------------------------------------------------

This module can work as a script (using **python -m compileall**) to compile Python sources.

directory ...[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-arg-directory "Link to this definition")

file ...[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-arg-file "Link to this definition")

Positional arguments are files to compile or directories that contain source files, traversed recursively. If no argument is given, behave as if the command line was `-l _<directories from sys.path>_`.

\-l[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-l "Link to this definition")

Do not recurse into subdirectories, only compile source code files directly contained in the named or implied directories.

\-f[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-f "Link to this definition")

Force rebuild even if timestamps are up-to-date.

\-q[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-q "Link to this definition")

Do not print the list of files compiled. If passed once, error messages will still be printed. If passed twice (`-qq`), all output is suppressed.

\-d destdir[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-d "Link to this definition")

Directory prepended to the path to each file being compiled. This will appear in compilation time tracebacks, and is also compiled in to the byte-code file, where it will be used in tracebacks and other messages in cases where the source file does not exist at the time the byte-code file is executed.

\-s strip\_prefix[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-s "Link to this definition")

Remove the given prefix from paths recorded in the `.pyc` files. Paths are made relative to the prefix.

This option can be used with `-p` but not with `-d`.

\-p prepend\_prefix[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-p "Link to this definition")

Prepend the given prefix to paths recorded in the `.pyc` files. Use `-p /` to make the paths absolute.

This option can be used with `-s` but not with `-d`.

\-x regex[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-x "Link to this definition")

regex is used to search the full path to each file considered for compilation, and if the regex produces a match, the file is skipped.

\-i list[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-i "Link to this definition")

Read the file `list` and add each line that it contains to the list of files and directories to compile. If `list` is `-`, read lines from `stdin`.

\-b[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-b "Link to this definition")

Write the byte-code files to their legacy locations and names, which may overwrite byte-code files created by another version of Python. The default is to write files to their [**PEP 3147**](https://peps.python.org/pep-3147/)
 locations and names, which allows byte-code files from multiple versions of Python to coexist.

\-r[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-r "Link to this definition")

Control the maximum recursion level for subdirectories. If this is given, then `-l` option will not be taken into account. **python -m compileall <directory> -r 0** is equivalent to **python -m compileall <directory> -l**.

\-j N[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-j "Link to this definition")

Use _N_ workers to compile the files within the given directory. If `0` is used, then the result of [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
 will be used.

\--invalidation-mode \[timestamp|checked-hash|unchecked-hash\][¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-invalidation-mode "Link to this definition")

Control how the generated byte-code files are invalidated at runtime. The `timestamp` value, means that `.pyc` files with the source timestamp and size embedded will be generated. The `checked-hash` and `unchecked-hash` values cause hash-based pycs to be generated. Hash-based pycs embed a hash of the source file contents rather than a timestamp. See [Cached bytecode invalidation](https://docs.python.org/3/reference/import.html#pyc-invalidation)
 for more information on how Python validates bytecode cache files at runtime. The default is `timestamp` if the `SOURCE_DATE_EPOCH` environment variable is not set, and `checked-hash` if the `SOURCE_DATE_EPOCH` environment variable is set.

\-o level[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-o "Link to this definition")

Compile with the given optimization level. May be used multiple times to compile for multiple levels at a time (for example, `compileall -o 1 -o 2`).

\-e dir[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-e "Link to this definition")

Ignore symlinks pointing outside the given directory.

\--hardlink-dupes[¶](https://docs.python.org/3/library/compileall.html#cmdoption-compileall-hardlink-dupes "Link to this definition")

If two `.pyc` files with different optimization level have the same content, use hard links to consolidate duplicate files.

Changed in version 3.2: Added the `-i`, `-b` and `-h` options.

Changed in version 3.5: Added the `-j`, `-r`, and `-qq` options. `-q` option was changed to a multilevel value. `-b` will always produce a byte-code file ending in `.pyc`, never `.pyo`.

Changed in version 3.7: Added the `--invalidation-mode` option.

Changed in version 3.9: Added the `-s`, `-p`, `-e` and `--hardlink-dupes` options. Raised the default recursion limit from 10 to [`sys.getrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit "sys.getrecursionlimit")
. Added the possibility to specify the `-o` option multiple times.

There is no command-line option to control the optimization level used by the [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 function, because the Python interpreter itself already provides the option: **python -O -m compileall**.

Similarly, the [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 function respects the [`sys.pycache_prefix`](https://docs.python.org/3/library/sys.html#sys.pycache_prefix "sys.pycache_prefix")
 setting. The generated bytecode cache will only be useful if `compile()` is run with the same `sys.pycache_prefix` (if any) that will be used at runtime.

Public functions[¶](https://docs.python.org/3/library/compileall.html#public-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------

compileall.compile\_dir(_dir_, _maxlevels\=sys.getrecursionlimit()_, _ddir\=None_, _force\=False_, _rx\=None_, _quiet\=0_, _legacy\=False_, _optimize\=\-1_, _workers\=1_, _invalidation\_mode\=None_, _\*_, _stripdir\=None_, _prependdir\=None_, _limit\_sl\_dest\=None_, _hardlink\_dupes\=False_)[¶](https://docs.python.org/3/library/compileall.html#compileall.compile_dir "Link to this definition")

Recursively descend the directory tree named by _dir_, compiling all `.py` files along the way. Return a true value if all the files compiled successfully, and a false value otherwise.

The _maxlevels_ parameter is used to limit the depth of the recursion; it defaults to `sys.getrecursionlimit()`.

If _ddir_ is given, it is prepended to the path to each file being compiled for use in compilation time tracebacks, and is also compiled in to the byte-code file, where it will be used in tracebacks and other messages in cases where the source file does not exist at the time the byte-code file is executed.

If _force_ is true, modules are re-compiled even if the timestamps are up to date.

If _rx_ is given, its `search` method is called on the complete path to each file considered for compilation, and if it returns a true value, the file is skipped. This can be used to exclude files matching a regular expression, given as a [re.Pattern](https://docs.python.org/3/library/re.html#re-objects)
 object.

If _quiet_ is `False` or `0` (the default), the filenames and other information are printed to standard out. Set to `1`, only errors are printed. Set to `2`, all output is suppressed.

If _legacy_ is true, byte-code files are written to their legacy locations and names, which may overwrite byte-code files created by another version of Python. The default is to write files to their [**PEP 3147**](https://peps.python.org/pep-3147/)
 locations and names, which allows byte-code files from multiple versions of Python to coexist.

_optimize_ specifies the optimization level for the compiler. It is passed to the built-in [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 function. Accepts also a sequence of optimization levels which lead to multiple compilations of one `.py` file in one call.

The argument _workers_ specifies how many workers are used to compile files in parallel. The default is to not use multiple workers. If the platform can’t use multiple workers and _workers_ argument is given, then sequential compilation will be used as a fallback. If _workers_ is 0, the number of cores in the system is used. If _workers_ is lower than `0`, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be raised.

_invalidation\_mode_ should be a member of the [`py_compile.PycInvalidationMode`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode "py_compile.PycInvalidationMode")
 enum and controls how the generated pycs are invalidated at runtime.

The _stripdir_, _prependdir_ and _limit\_sl\_dest_ arguments correspond to the `-s`, `-p` and `-e` options described above. They may be specified as `str` or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
.

If _hardlink\_dupes_ is true and two `.pyc` files with different optimization level have the same content, use hard links to consolidate duplicate files.

Changed in version 3.2: Added the _legacy_ and _optimize_ parameter.

Changed in version 3.5: Added the _workers_ parameter.

Changed in version 3.5: _quiet_ parameter was changed to a multilevel value.

Changed in version 3.5: The _legacy_ parameter only writes out `.pyc` files, not `.pyo` files no matter what the value of _optimize_ is.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: The _invalidation\_mode_ parameter was added.

Changed in version 3.7.2: The _invalidation\_mode_ parameter’s default value is updated to `None`.

Changed in version 3.8: Setting _workers_ to 0 now chooses the optimal number of cores.

Changed in version 3.9: Added _stripdir_, _prependdir_, _limit\_sl\_dest_ and _hardlink\_dupes_ arguments. Default value of _maxlevels_ was changed from `10` to `sys.getrecursionlimit()`

compileall.compile\_file(_fullname_, _ddir\=None_, _force\=False_, _rx\=None_, _quiet\=0_, _legacy\=False_, _optimize\=\-1_, _invalidation\_mode\=None_, _\*_, _stripdir\=None_, _prependdir\=None_, _limit\_sl\_dest\=None_, _hardlink\_dupes\=False_)[¶](https://docs.python.org/3/library/compileall.html#compileall.compile_file "Link to this definition")

Compile the file with path _fullname_. Return a true value if the file compiled successfully, and a false value otherwise.

If _ddir_ is given, it is prepended to the path to the file being compiled for use in compilation time tracebacks, and is also compiled in to the byte-code file, where it will be used in tracebacks and other messages in cases where the source file does not exist at the time the byte-code file is executed.

If _rx_ is given, its `search` method is passed the full path name to the file being compiled, and if it returns a true value, the file is not compiled and `True` is returned. This can be used to exclude files matching a regular expression, given as a [re.Pattern](https://docs.python.org/3/library/re.html#re-objects)
 object.

If _quiet_ is `False` or `0` (the default), the filenames and other information are printed to standard out. Set to `1`, only errors are printed. Set to `2`, all output is suppressed.

If _legacy_ is true, byte-code files are written to their legacy locations and names, which may overwrite byte-code files created by another version of Python. The default is to write files to their [**PEP 3147**](https://peps.python.org/pep-3147/)
 locations and names, which allows byte-code files from multiple versions of Python to coexist.

_optimize_ specifies the optimization level for the compiler. It is passed to the built-in [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 function. Accepts also a sequence of optimization levels which lead to multiple compilations of one `.py` file in one call.

_invalidation\_mode_ should be a member of the [`py_compile.PycInvalidationMode`](https://docs.python.org/3/library/py_compile.html#py_compile.PycInvalidationMode "py_compile.PycInvalidationMode")
 enum and controls how the generated pycs are invalidated at runtime.

The _stripdir_, _prependdir_ and _limit\_sl\_dest_ arguments correspond to the `-s`, `-p` and `-e` options described above. They may be specified as `str` or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
.

If _hardlink\_dupes_ is true and two `.pyc` files with different optimization level have the same content, use hard links to consolidate duplicate files.

Added in version 3.2.

Changed in version 3.5: _quiet_ parameter was changed to a multilevel value.

Changed in version 3.5: The _legacy_ parameter only writes out `.pyc` files, not `.pyo` files no matter what the value of _optimize_ is.

Changed in version 3.7: The _invalidation\_mode_ parameter was added.

Changed in version 3.7.2: The _invalidation\_mode_ parameter’s default value is updated to `None`.

Changed in version 3.9: Added _stripdir_, _prependdir_, _limit\_sl\_dest_ and _hardlink\_dupes_ arguments.

compileall.compile\_path(_skip\_curdir\=True_, _maxlevels\=0_, _force\=False_, _quiet\=0_, _legacy\=False_, _optimize\=\-1_, _invalidation\_mode\=None_)[¶](https://docs.python.org/3/library/compileall.html#compileall.compile_path "Link to this definition")

Byte-compile all the `.py` files found along `sys.path`. Return a true value if all the files compiled successfully, and a false value otherwise.

If _skip\_curdir_ is true (the default), the current directory is not included in the search. All other parameters are passed to the [`compile_dir()`](https://docs.python.org/3/library/compileall.html#compileall.compile_dir "compileall.compile_dir")
 function. Note that unlike the other compile functions, `maxlevels` defaults to `0`.

Changed in version 3.2: Added the _legacy_ and _optimize_ parameter.

Changed in version 3.5: _quiet_ parameter was changed to a multilevel value.

Changed in version 3.5: The _legacy_ parameter only writes out `.pyc` files, not `.pyo` files no matter what the value of _optimize_ is.

Changed in version 3.7: The _invalidation\_mode_ parameter was added.

Changed in version 3.7.2: The _invalidation\_mode_ parameter’s default value is updated to `None`.

To force a recompile of all the `.py` files in the `Lib/` subdirectory and all its subdirectories:

Copy

import compileall

compileall.compile\_dir('Lib/', force\=True)

\# Perform same compilation, excluding files in .svn directories.
import re
compileall.compile\_dir('Lib/', rx\=re.compile(r'\[/\\\\\]\[.\]svn'), force\=True)

\# pathlib.Path objects can also be used.
import pathlib
compileall.compile\_dir(pathlib.Path('Lib/'), force\=True)

See also

Module [`py_compile`](https://docs.python.org/3/library/py_compile.html#module-py_compile "py_compile: Generate byte-code files from Python source files.")

Byte-compile a single source file.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html#)
    *   [Command-line use](https://docs.python.org/3/library/compileall.html#command-line-use)
        
    *   [Public functions](https://docs.python.org/3/library/compileall.html#public-functions)
        

#### Previous topic

[`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html "previous chapter")

#### Next topic

[`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=compileall+%E2%80%94+Byte-compile+Python+libraries&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcompileall.html&pagesource=library%2Fcompileall.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/compileall.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/dis.html "dis — Disassembler for Python bytecode")
     |
*   [previous](https://docs.python.org/3/library/py_compile.html "py_compile — Compile Python source files")
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
*   [`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html)
    
*    
    
    |
*   Theme Auto Light Dark |