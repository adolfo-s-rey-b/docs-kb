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
*   [Pending removal in Python 3.16](https://docs.python.org/3/deprecations/pending-removal-in-3.16.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.16[¶](https://docs.python.org/3/deprecations/pending-removal-in-3.16.html#pending-removal-in-python-3-16 "Link to this heading")

=============================================================================================================================================================

*   The import system:
    
    *   Setting [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
         on a module while failing to set [`__spec__.loader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader "importlib.machinery.ModuleSpec.loader")
         is deprecated. In Python 3.16, `__loader__` will cease to be set or taken into consideration by the import system or the standard library.
        
*   [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
    :
    
    *   The `'u'` format code (`wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
        ) for Unicode characters instead.
        
*   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
    :
    
    *   `asyncio.iscoroutinefunction()` is deprecated and will be removed in Python 3.16; use [`inspect.iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction")
         instead. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875)
        .)
        
    *   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
         policy system is deprecated and will be removed in Python 3.16. In particular, the following classes and functions are deprecated:
        
        *   [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy")
            
        *   [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy "asyncio.DefaultEventLoopPolicy")
            
        *   [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy "asyncio.WindowsSelectorEventLoopPolicy")
            
        *   [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy "asyncio.WindowsProactorEventLoopPolicy")
            
        *   [`asyncio.get_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.get_event_loop_policy "asyncio.get_event_loop_policy")
            
        *   [`asyncio.set_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.set_event_loop_policy "asyncio.set_event_loop_policy")
            
        
        Users should use [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
         or [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")
         with _loop\_factory_ to use the desired event loop implementation.
        
        For example, to use [`asyncio.SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
         on Windows:
        
        Copy
        
        import asyncio
        
        async def main():
            ...
        
        asyncio.run(main(), loop\_factory\=asyncio.SelectorEventLoop)
        
        (Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949)
        .)
        
*   [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
    :
    
    *   Bitwise inversion on boolean types, `~True` or `~False` has been deprecated since Python 3.12, as it produces surprising and unintuitive results (`-2` and `-1`). Use `not x` instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to `int` explicitly (`~int(x)`).
        
*   [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
    :
    
    *   Calling the Python implementation of [`functools.reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce "functools.reduce")
         with _function_ or _sequence_ as keyword arguments has been deprecated since Python 3.14.
        
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
    :
    
    *   Support for custom logging handlers with the _strm_ argument is deprecated and scheduled for removal in Python 3.16. Define handlers with the _stream_ argument instead. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032)
        .)
        
*   [`mimetypes`](https://docs.python.org/3/library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types.")
    :
    
    *   Valid extensions start with a ‘.’ or are empty for [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.add_type "mimetypes.MimeTypes.add_type")
        . Undotted extensions are deprecated and will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
         in Python 3.16. (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223)
        .)
        
*   [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
    :
    
    *   The `ExecError` exception has been deprecated since Python 3.14. It has not been used by any function in `shutil` since Python 3.4, and is now an alias of [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
        .
        
*   [`symtable`](https://docs.python.org/3/library/symtable.html#module-symtable "symtable: Interface to the compiler's internal symbol tables.")
    :
    
    *   The [`Class.get_methods`](https://docs.python.org/3/library/symtable.html#symtable.Class.get_methods "symtable.Class.get_methods")
         method has been deprecated since Python 3.14.
        
*   [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
    :
    
    *   The [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding")
         function has been deprecated since Python 3.13. Use the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)
         environment variable instead.
        
*   [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
    :
    
    *   The `sysconfig.expand_makefile_vars()` function has been deprecated since Python 3.14. Use the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_paths "sysconfig.get_paths")
         instead.
        
*   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
    :
    
    *   The undocumented and unused `TarFile.tarfile` attribute has been deprecated since Python 3.13.
        

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.16&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fpending-removal-in-3.16.html&pagesource=deprecations%2Fpending-removal-in-3.16.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/pending-removal-in-3.16.rst?plain=1)
    

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
*   [Pending removal in Python 3.16](https://docs.python.org/3/deprecations/pending-removal-in-3.16.html)
    
*    
    
    |
*   Theme Auto Light Dark |