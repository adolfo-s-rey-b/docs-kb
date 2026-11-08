### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules")
     |
*   [previous](https://docs.python.org/3/library/pkgutil.html "pkgutil — Package extension utility")
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
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
     »
*   [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`modulefinder` — Find modules used by a script[¶](https://docs.python.org/3/library/modulefinder.html#module-modulefinder "Link to this heading")

==================================================================================================================================================

**Source code:** [Lib/modulefinder.py](https://github.com/python/cpython/tree/3.15/Lib/modulefinder.py)

* * *

This module provides a [`ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder "modulefinder.ModuleFinder")
 class that can be used to determine the set of modules imported by a script. `modulefinder.py` can also be run as a script, giving the filename of a Python script as its argument, after which a report of the imported modules will be printed.

modulefinder.AddPackagePath(_pkg\_name_, _path_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.AddPackagePath "Link to this definition")

Record that the package named _pkg\_name_ can be found in the specified _path_.

modulefinder.ReplacePackage(_oldname_, _newname_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ReplacePackage "Link to this definition")

Allows specifying that the module named _oldname_ is in fact the package named _newname_.

class modulefinder.ModuleFinder(_path\=None_, _debug\=0_, _excludes\=\[\]_, _replace\_paths\=\[\]_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder "Link to this definition")

This class provides [`run_script()`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.run_script "modulefinder.ModuleFinder.run_script")
 and [`report()`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.report "modulefinder.ModuleFinder.report")
 methods to determine the set of modules imported by a script. _path_ can be a list of directories to search for modules; if not specified, `sys.path` is used. _debug_ sets the debugging level; higher values make the class print debugging messages about what it’s doing. _excludes_ is a list of module names to exclude from the analysis. _replace\_paths_ is a list of `(oldpath, newpath)` tuples that will be replaced in module paths.

report()[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.report "Link to this definition")

Print a report to standard output that lists the modules imported by the script and their paths, as well as modules that are missing or seem to be missing.

run\_script(_pathname_)[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.run_script "Link to this definition")

Analyze the contents of the _pathname_ file, which must contain Python code.

modules[¶](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder.modules "Link to this definition")

A dictionary mapping module names to modules. See [Example usage of ModuleFinder](https://docs.python.org/3/library/modulefinder.html#modulefinder-example)
.

Example usage of [`ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#modulefinder.ModuleFinder "modulefinder.ModuleFinder")
[¶](https://docs.python.org/3/library/modulefinder.html#example-usage-of-modulefinder "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The script that is going to get analyzed later on (bacon.py):

Copy

import re, itertools

try:
    import baconhameggs
except ImportError:
    pass

try:
    import guido.python.ham
except ImportError:
    pass

The script that will output the report of bacon.py:

Copy

from modulefinder import ModuleFinder

finder \= ModuleFinder()
finder.run\_script('bacon.py')

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end\='')
    print(','.join(list(mod.globalnames.keys())\[:3\]))

print('-'\*50)
print('Modules not imported:')
print('\\n'.join(finder.badmodules.keys()))

Sample output (may vary depending on the architecture):

Copy

Loaded modules:
\_types:
copyreg:  \_inverted\_registry,\_slotnames,\_\_all\_\_
re.\_compiler:  isstring,\_sre,\_optimize\_unicode
\_sre:
re.\_constants:  REPEAT\_ONE,makedict,AT\_END\_LINE
sys:
re:  \_\_module\_\_,finditer,\_expand
itertools:
\_\_main\_\_:  re,itertools,baconhameggs
re.\_parser:  \_PATTERNENDERS,SRE\_FLAG\_UNICODE
array:
types:  \_\_module\_\_,IntType,TypeType
\---------------------------------------------------
Modules not imported:
guido.python.ham
baconhameggs

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html#)
    *   [Example usage of `ModuleFinder`](https://docs.python.org/3/library/modulefinder.html#example-usage-of-modulefinder)
        

#### Previous topic

[`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html "previous chapter")

#### Next topic

[`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=modulefinder+%E2%80%94+Find+modules+used+by+a+script&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmodulefinder.html&pagesource=library%2Fmodulefinder.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/modulefinder.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules")
     |
*   [previous](https://docs.python.org/3/library/pkgutil.html "pkgutil — Package extension utility")
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
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
     »
*   [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
    
*    
    
    |
*   Theme Auto Light Dark |