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
*   [Pending removal in Python 3.15](https://docs.python.org/3/deprecations/pending-removal-in-3.15.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.15[¶](https://docs.python.org/3/deprecations/pending-removal-in-3.15.html#pending-removal-in-python-3-15 "Link to this heading")

=============================================================================================================================================================

*   The import system:
    
    *   Setting `__cached__` on a module while failing to set [`__spec__.cached`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.cached "importlib.machinery.ModuleSpec.cached")
         is deprecated. In Python 3.15, `__cached__` will cease to be set or take into consideration by the import system or standard library. ([gh-97879](https://github.com/python/cpython/issues/97879)
        )
        
    *   Setting [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
         on a module while failing to set [`__spec__.parent`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent")
         is deprecated. In Python 3.15, `__package__` will cease to be set or take into consideration by the import system or standard library. ([gh-97879](https://github.com/python/cpython/issues/97879)
        )
        
*   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
    :
    
    *   The undocumented `ctypes.SetPointerType()` function has been deprecated since Python 3.13.
        
*   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
    :
    
    *   The obsolete and rarely used `CGIHTTPRequestHandler` has been deprecated since Python 3.13. No direct replacement exists. _Anything_ is better than CGI to interface a web server with a request handler.
        
    *   The `--cgi` flag to the **python -m http.server** command-line interface has been deprecated since Python 3.13.
        
*   [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
    :
    
    *   `load_module()` method: use `exec_module()` instead.
        
*   [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
    :
    
    *   `.PurePath.is_reserved()` has been deprecated since Python 3.13. Use [`os.path.isreserved()`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved")
         to detect reserved paths on Windows.
        
*   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
    :
    
    *   `platform.java_ver()` has been deprecated since Python 3.13. This function is only useful for Jython support, has a confusing API, and is largely untested.
        
*   [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
    :
    
    *   The _check\_home_ argument of [`sysconfig.is_python_build()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.is_python_build "sysconfig.is_python_build")
         has been deprecated since Python 3.12.
        
*   [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
    :
    
    *   [`RLock()`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock")
         will take no arguments in Python 3.15. Passing any arguments has been deprecated since Python 3.14, as the Python version does not permit any arguments, but the C version allows any number of positional or keyword arguments, ignoring every argument.
        
*   [`types`](https://docs.python.org/3/library/types.html#module-types "types: Names for built-in types.")
    :
    
    *   [`types.CodeType`](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType")
        : Accessing `codeobject.co_lnotab` was deprecated in [**PEP 626**](https://peps.python.org/pep-0626/)
         since 3.10 and was planned to be removed in 3.12, but it only got a proper [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
         in 3.12. May be removed in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866)
        .)
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   The undocumented keyword argument syntax for creating [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")
         classes (for example, `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
        
    *   When using the functional syntax of [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")
        s, failing to pass a value to the _fields_ parameter (`TD = TypedDict("TD")`) or passing `None` (`TD = TypedDict("TD", None)`) has been deprecated since Python 3.13. Use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})` to create a TypedDict with zero field.
        
    *   The `typing.no_type_check_decorator` decorator function has been deprecated since Python 3.13. After eight years in the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
         module, it has yet to be supported by any major type checker.
        
*   `sre_compile`, `sre_constants` and `sre_parse` modules.
    
*   [`wave`](https://docs.python.org/3/library/wave.html#module-wave "wave: Provide an interface to the WAV sound format.")
    :
    
    *   The `getmark()`, `setmark()` and `getmarkers()` methods of the [`Wave_read`](https://docs.python.org/3/library/wave.html#wave.Wave_read "wave.Wave_read")
         and [`Wave_write`](https://docs.python.org/3/library/wave.html#wave.Wave_write "wave.Wave_write")
         classes have been deprecated since Python 3.13.
        
*   [`zipimport`](https://docs.python.org/3/library/zipimport.html#module-zipimport "zipimport: Support for importing Python modules from ZIP archives.")
    :
    
    *   `zipimport.zipimporter.load_module()` has been deprecated since Python 3.10. Use [`exec_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module")
         instead. ([gh-125746](https://github.com/python/cpython/issues/125746)
        .)
        

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.15&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fpending-removal-in-3.15.html&pagesource=deprecations%2Fpending-removal-in-3.15.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/pending-removal-in-3.15.rst?plain=1)
    

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
*   [Pending removal in Python 3.15](https://docs.python.org/3/deprecations/pending-removal-in-3.15.html)
    
*    
    
    |
*   Theme Auto Light Dark |