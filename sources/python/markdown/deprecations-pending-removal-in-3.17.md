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
*   [Pending removal in Python 3.17](https://docs.python.org/3/deprecations/pending-removal-in-3.17.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.17[¶](https://docs.python.org/3/deprecations/pending-removal-in-3.17.html#pending-removal-in-python-3-17 "Link to this heading")

=============================================================================================================================================================

*   [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
    :
    
    *   [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")
         calls using a format string containing `%e` (day of month) without a year. This has been deprecated since Python 3.15. (Contributed by Stan Ulbrych in [gh-70647](https://github.com/python/cpython/issues/70647)
        .)
        
*   [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")
    :
    
    *   [`collections.abc.ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString")
         is scheduled for removal in Python 3.17.
        
        Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
         at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")
         or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).
        
        `ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
         and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
        . However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
         were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).
        
        See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)
         for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896)
        .)
        
*   [`encodings`](https://docs.python.org/3/library/codecs.html#module-encodings "encodings: Encodings package")
    :
    
    *   Passing non-ascii _encoding_ names to [`encodings.normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding")
         is deprecated and scheduled for removal in Python 3.17. (Contributed by Stan Ulbrych in [gh-136702](https://github.com/python/cpython/issues/136702)
        .)
        
*   [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
    :
    
    *   The `profile` module is deprecated and will be removed in Python 3.17. Use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
         instead, which provides a compatible API. See [**PEP 799**](https://peps.python.org/pep-0799/)
         for details. (Contributed by Pablo Galindo and László Kiss Kollár in [gh-138122](https://github.com/python/cpython/issues/138122)
        .)
        
*   [`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.")
    :
    
    *   `webbrowser.MacOSXOSAScript` is deprecated in favour of `webbrowser.MacOS`. ([gh-137586](https://github.com/python/cpython/issues/137586)
        )
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   Before Python 3.14, old-style unions were implemented using the private class `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like [`typing.get_origin()`](https://docs.python.org/3/library/typing.html#typing.get_origin "typing.get_origin")
         and [`typing.get_args()`](https://docs.python.org/3/library/typing.html#typing.get_args "typing.get_args")
         instead of relying on private implementation details.
        
    *   [`typing.ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString "typing.ByteString")
        , deprecated since Python 3.9, is scheduled for removal in Python 3.17.
        
        Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
         at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")
         or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).
        
        `ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
         and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
        . However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
         were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).
        
        See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)
         for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896)
        .)
        
*   [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
    :
    
    *   The `tkinter.Variable` methods `trace_variable()`, `trace()` (an alias of `trace_variable()`), `trace_vdelete()` and `trace_vinfo()`, deprecated since Python 3.14, are scheduled for removal in Python 3.17. Use `trace_add()`, `trace_remove()` and `trace_info()` instead. (Contributed by Serhiy Storchaka in [gh-120220](https://github.com/python/cpython/issues/120220)
        .)
        

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.17&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fpending-removal-in-3.17.html&pagesource=deprecations%2Fpending-removal-in-3.17.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/pending-removal-in-3.17.rst?plain=1)
    

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
*   [Pending removal in Python 3.17](https://docs.python.org/3/deprecations/pending-removal-in-3.17.html)
    
*    
    
    |
*   Theme Auto Light Dark |