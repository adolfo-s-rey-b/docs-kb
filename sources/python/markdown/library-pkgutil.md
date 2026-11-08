### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/modulefinder.html "modulefinder — Find modules used by a script")
     |
*   [previous](https://docs.python.org/3/library/zipimport.html "zipimport — Import modules from Zip archives")
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
*   [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`pkgutil` — Package extension utility[¶](https://docs.python.org/3/library/pkgutil.html#module-pkgutil "Link to this heading")

===============================================================================================================================

**Source code:** [Lib/pkgutil.py](https://github.com/python/cpython/tree/3.15/Lib/pkgutil.py)

* * *

This module provides utilities for the import system, in particular package support.

class pkgutil.ModuleInfo(_module\_finder_, _name_, _ispkg_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.ModuleInfo "Link to this definition")

A namedtuple that holds a brief summary of a module’s info.

Added in version 3.6.

pkgutil.extend\_path(_path_, _name_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.extend_path "Link to this definition")

Extend the search path for the modules which comprise a package. Intended use is to place the following code in a package’s `__init__.py`:

Copy

from pkgutil import extend\_path
\_\_path\_\_ \= extend\_path(\_\_path\_\_, \_\_name\_\_)

For each directory on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 that has a subdirectory that matches the package name, add the subdirectory to the package’s [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__")
. This is useful if one wants to distribute different parts of a single logical package as multiple directories.

It also looks for `*.pkg` files beginning where `*` matches the _name_ argument. This feature is similar to `*.pth` files (see the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module for more information), except that it doesn’t special-case lines starting with `import`. A `*.pkg` file is trusted at face value: apart from skipping blank lines and ignoring comments, all entries found in a `*.pkg` file are added to the path, regardless of whether they exist on the filesystem (this is a feature).

If the input path is not a list (as is the case for frozen packages) it is returned unchanged. The input path is not modified; an extended copy is returned. Items are only appended to the copy at the end.

It is assumed that [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 is a sequence. Items of `sys.path` that are not strings referring to existing directories are ignored. Unicode items on `sys.path` that cause errors when used as filenames may cause this function to raise an exception (in line with [`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir "os.path.isdir")
 behavior).

pkgutil.get\_importer(_path\_item_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.get_importer "Link to this definition")

Retrieve a [finder](https://docs.python.org/3/glossary.html#term-finder)
 for the given _path\_item_.

The returned finder is cached in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache")
 if it was newly created by a path hook.

The cache (or part of it) can be cleared manually if a rescan of [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
 is necessary.

Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/)
 import emulation.

pkgutil.iter\_importers(_fullname\=''_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.iter_importers "Link to this definition")

Yield [finder](https://docs.python.org/3/glossary.html#term-finder)
 objects for the given module name.

If _fullname_ contains a `'.'`, the finders will be for the package containing _fullname_, otherwise they will be all registered top level finders (i.e. those on both [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
 and [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
).

If the named module is in a package, that package is imported as a side effect of invoking this function.

If no module name is specified, all top level finders are produced.

Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/)
 import emulation.

pkgutil.iter\_modules(_path\=None_, _prefix\=''_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.iter_modules "Link to this definition")

Yields [`ModuleInfo`](https://docs.python.org/3/library/pkgutil.html#pkgutil.ModuleInfo "pkgutil.ModuleInfo")
 for all submodules on _path_, or, if _path_ is `None`, all top-level modules on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

_path_ should be either `None` or a list of paths to look for modules in.

_prefix_ is a string to output on the front of every module name on output.

Note

Only works for a [finder](https://docs.python.org/3/glossary.html#term-finder)
 which defines an `iter_modules()` method. This interface is non-standard, so the module also provides implementations for [`importlib.machinery.FileFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "importlib.machinery.FileFinder")
 and [`zipimport.zipimporter`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter "zipimport.zipimporter")
.

Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/)
 import emulation.

pkgutil.walk\_packages(_path\=None_, _prefix\=''_, _onerror\=None_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.walk_packages "Link to this definition")

Yields [`ModuleInfo`](https://docs.python.org/3/library/pkgutil.html#pkgutil.ModuleInfo "pkgutil.ModuleInfo")
 for all modules recursively on _path_, or, if _path_ is `None`, all accessible modules.

_path_ should be either `None` or a list of paths to look for modules in.

_prefix_ is a string to output on the front of every module name on output.

Note that this function must import all _packages_ (_not_ all modules!) on the given _path_, in order to access the `__path__` attribute to find submodules.

_onerror_ is a function which gets called with one argument (the name of the package which was being imported) if any exception occurs while trying to import a package. If no _onerror_ function is supplied, [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
s are caught and ignored, while all other exceptions are propagated, terminating the search.

Examples:

Copy

\# list all modules python can access
walk\_packages()

\# list all submodules of ctypes
walk\_packages(ctypes.\_\_path\_\_, ctypes.\_\_name\_\_ + '.')

Note

Only works for a [finder](https://docs.python.org/3/glossary.html#term-finder)
 which defines an `iter_modules()` method. This interface is non-standard, so the module also provides implementations for [`importlib.machinery.FileFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "importlib.machinery.FileFinder")
 and [`zipimport.zipimporter`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter "zipimport.zipimporter")
.

Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/)
 import emulation.

pkgutil.get\_data(_package_, _resource_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.get_data "Link to this definition")

Get a resource from a package.

This is a wrapper for the [loader](https://docs.python.org/3/glossary.html#term-loader)
 [`get_data`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data")
 API. The _package_ argument should be the name of a package, in standard module format (`foo.bar`). The _resource_ argument should be in the form of a relative filename, using `/` as the path separator.

The function returns a binary string that is the contents of the specified resource.

This function uses the [loader](https://docs.python.org/3/glossary.html#term-loader)
 method [`get_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.get_data "importlib.abc.FileLoader.get_data")
 to support modules installed in the filesystem, but also in zip files, databases, or elsewhere.

For packages located in the filesystem, which have already been imported, this is the rough equivalent of:

Copy

d \= os.path.dirname(sys.modules\[package\].\_\_file\_\_)
data \= open(os.path.join(d, resource), 'rb').read()

Like the [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 function, `get_data()` can follow parent directories (`../`) and absolute paths (starting with `/` or `C:/`, for example). It can open compilation/installation artifacts like `.py` and `.pyc` files or files with [`reserved filenames`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved")
. To be compatible with non-filesystem loaders, avoid using these features.

Warning

This function is intended for trusted input. It does not verify that _resource_ “belongs” to _package_.

If you use a user-provided _resource_ path, consider verifying it. For example, require an alphanumeric filename with a known extension, or install and check a list of known resources.

If the package cannot be located or loaded, or it uses a [loader](https://docs.python.org/3/glossary.html#term-loader)
 which does not support [`get_data`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data")
, then `None` is returned. In particular, the loader for [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package)
 does not support `get_data`.

See also

The [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access")
 module provides structured access to module resources.

pkgutil.resolve\_name(_name_, _\*_, _strict\=False_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.resolve_name "Link to this definition")

Resolve a name to an object.

This functionality is used in numerous places in the standard library (see [bpo-12915](https://bugs.python.org/issue?@action=redirect&bpo=12915)
) - and equivalent functionality is also in widely used third-party packages such as setuptools, Django and Pyramid.

It is expected that _name_ will be a string in one of the following formats, where W is shorthand for a valid Python identifier and dot stands for a literal period in these pseudo-regexes:

*   `W(.W)*`
    
*   `W(.W)*:(W(.W)*)?`
    
*   `W(.W)*:(W(.W)*)`
    

The first form is intended for backward compatibility only. It assumes that some part of the dotted name is a package, and the rest is an object somewhere within that package, possibly nested inside other objects. Because the place where the package stops and the object hierarchy starts can’t be inferred by inspection, repeated attempts to import must be done with this form.

In the second form, the caller makes the division point clear through the provision of a single colon: the dotted name to the left of the colon is a package to be imported, and the dotted name to the right is the object hierarchy within that package. Only one import is needed in this form. If it ends with the colon, then a module object is returned.

The first two forms are accepted when `strict=False` (the default).

The third form requires both the module name and callable, separated by a colon. Only this form is accepted when `strict=True`.

The function will return an object (which might be a module), or raise one of the following exceptions:

[`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 – if _name_ isn’t in a recognised format.

[`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
 – if an import failed when it shouldn’t have.

[`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 – If a failure occurred when traversing the object hierarchy within the imported package to get to the desired object.

Added in version 3.9.

Changed in version 3.15: The optional keyword-only `strict` flag was added.

#### Previous topic

[`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html "previous chapter")

#### Next topic

[`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pkgutil+%E2%80%94+Package+extension+utility&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpkgutil.html&pagesource=library%2Fpkgutil.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/pkgutil.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/modulefinder.html "modulefinder — Find modules used by a script")
     |
*   [previous](https://docs.python.org/3/library/zipimport.html "zipimport — Import modules from Zip archives")
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
*   [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
    
*    
    
    |
*   Theme Auto Light Dark |