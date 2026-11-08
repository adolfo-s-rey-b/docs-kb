### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/glossary.html "Glossary")
     |
*   [previous](https://docs.python.org/3/faq/installed.html "“Why is Python Installed on my Computer?” FAQ")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Deprecations](https://docs.python.org/3/deprecations/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Deprecations[¶](https://docs.python.org/3/deprecations/index.html#deprecations "Link to this heading")

=======================================================================================================

Pending removal in Python 3.16[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-16 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

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
        

Pending removal in Python 3.17[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-17 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

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
        

Pending removal in Python 3.18[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-18 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

*   No longer accept a boolean value when a file descriptor is expected. (Contributed by Serhiy Storchaka in [gh-82626](https://github.com/python/cpython/issues/82626)
    .)
    
*   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
    :
    
    *   The non-standard and undocumented [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
         format specifier `'N'`, which is only supported in the `decimal` module’s C implementation, has been deprecated since Python 3.13. (Contributed by Serhiy Storchaka in [gh-89902](https://github.com/python/cpython/issues/89902)
        .)
        
*   Deprecations defined by [**PEP 829**](https://peps.python.org/pep-0829/)
    :
    
    *   `import` lines in `_name_.pth` files are silently ignored.
        
    
    (Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)
    .)
    

Pending removal in Python 3.19[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-19 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

*   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
    :
    
    *   Implicitly switching to the MSVC-compatible struct layout by setting [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_")
         but not [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")
         on non-Windows platforms.
        
*   [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
    :
    
    *   In hash function constructors such as [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new")
         or the direct hash-named constructors such as [`md5()`](https://docs.python.org/3/library/hashlib.html#hashlib.md5 "hashlib.md5")
         and [`sha256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")
        , their optional initial data parameter could also be passed a keyword argument named `data=` or `string=` in various `hashlib` implementations.
        
        Support for the `string` keyword argument name is now deprecated and slated for removal in Python 3.19.
        
        Before Python 3.13, the `string` keyword parameter was not correctly supported depending on the backend implementation of hash functions. Prefer passing the initial data as a positional argument for maximum backwards compatibility.
        
*   [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).")
    :
    
    *   [`http.cookies.Morsel.js_output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.js_output "http.cookies.Morsel.js_output")
         is deprecated and will be removed in Python 3.19.
        
    *   [`http.cookies.BaseCookie.js_output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.js_output "http.cookies.BaseCookie.js_output")
         is deprecated and will be removed in Python 3.19.
        
*   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")
    :
    
    *   Altering [`IMAP4.file`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.file "imaplib.IMAP4.file")
         is now deprecated and slated for removal in Python 3.19. This property is now unused and changing its value does not automatically close the current file.
        
        Before Python 3.14, this property was used to implement the corresponding `read()` and `readline()` methods for [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4")
         but this is no longer the case since then.
        

Pending removal in Python 3.20[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-20 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

*   Calling the `__new__()` method of [`struct.Struct`](https://docs.python.org/3/library/struct.html#struct.Struct "struct.Struct")
     without the _format_ argument is deprecated and will be removed in Python 3.20. Calling [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
     method on initialized `Struct` objects is deprecated and will be removed in Python 3.20.
    
    (Contributed by Sergey B Kirpichev and Serhiy Storchaka in [gh-143715](https://github.com/python/cpython/issues/143715)
    .)
    
*   The `__version__`, `version` and `VERSION` attributes have been deprecated in these standard library modules and will be removed in Python 3.20. Use [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")
     instead.
    
    *   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
        
    *   [`csv`](https://docs.python.org/3/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.")
        
    *   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
        
    *   `ctypes.macholib`
        
    *   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
         (use [`decimal.SPEC_VERSION`](https://docs.python.org/3/library/decimal.html#decimal.SPEC_VERSION "decimal.SPEC_VERSION")
         instead)
        
    *   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
        
    *   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")
        
    *   [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")
        
    *   [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
        
    *   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
         (`__date__` also deprecated)
        
    *   [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
        
    *   [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
        
    *   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
        
    *   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
        
    *   [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")
        
    *   [`tabnanny`](https://docs.python.org/3/library/tabnanny.html#module-tabnanny "tabnanny: Tool for detecting white space related problems in Python source files in a directory tree.")
        
    *   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
        
    *   [`tkinter.font`](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "tkinter.font: Tkinter font-wrapping class")
        
    *   [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set")
        
    *   [`wsgiref.simple_server`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.simple_server "wsgiref.simple_server: A simple WSGI HTTP server.")
        
    *   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
        
    *   `xml.sax.expatreader`
        
    *   [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.")
        
    *   [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
        
    
    (Contributed by Hugo van Kemenade and Stan Ulbrych in [gh-76007](https://github.com/python/cpython/issues/76007)
    .)
    
*   Deprecations defined by [**PEP 829**](https://peps.python.org/pep-0829/)
    :
    
    *   Warnings are produced for `import` lines found in `_name_.pth` files.
        
    *   `_name_.pth` files are no longer decoded in the locale encoding by default. They **MUST** be encoded in `utf-8-sig`.
        
    
    (Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)
    .)
    
*   [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
    :
    
    *   Creating instances of abstract AST nodes (such as [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST")
         or `ast.expr`) is deprecated and will raise an error in Python 3.20.
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   It is deprecated to call [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
         and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
         checks on protocol classes that were not explicitly decorated with `runtime_checkable()` but that inherit from a runtime-checkable protocol class. This will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
         in Python 3.20.
        
        (Contributed by Bartosz Sławecki in [gh-132604](https://github.com/python/cpython/issues/132604)
        .)
        

Pending removal in future versions[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-future-versions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The following APIs will be removed in the future, although there is currently no date scheduled for their removal.

*   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
    :
    
    *   Nesting argument groups and nesting mutually exclusive groups are deprecated.
        
    *   Passing the undocumented keyword argument _prefix\_chars_ to [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group")
         is now deprecated.
        
    *   The [`argparse.FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType")
         type converter is deprecated.
        
*   [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
    :
    
    *   Generators: `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated: use `throw(exc)` and `athrow(exc)` instead, the single argument signature.
        
    *   Currently Python accepts numeric literals immediately followed by keywords, for example `0in x`, `1or x`, `0if 1else 2`. It allows confusing and ambiguous expressions like `[0x1for x in y]` (which can be interpreted as `[0x1 for x in y]` or `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords [`and`](https://docs.python.org/3/reference/expressions.html#and)
        , [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)
        , [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
        , [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
        , [`in`](https://docs.python.org/3/reference/expressions.html#in)
        , [`is`](https://docs.python.org/3/reference/expressions.html#is)
         and [`or`](https://docs.python.org/3/reference/expressions.html#or)
        . In a future release it will be changed to a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999)
        )
        
    *   Support for `__index__()` and `__int__()` method returning non-int type: these methods will be required to return an instance of a strict subclass of [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
        .
        
    *   Support for `__float__()` method returning a strict subclass of [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
        : these methods will be required to return an instance of `float`.
        
    *   Support for `__complex__()` method returning a strict subclass of [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
        : these methods will be required to return an instance of `complex`.
        
    *   Passing a complex number as the _real_ or _imag_ argument in the [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
         constructor is now deprecated; it should only be passed as a single positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218)
        .)
        
*   [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
    : `calendar.January` and `calendar.February` constants are deprecated and replaced by [`calendar.JANUARY`](https://docs.python.org/3/library/calendar.html#calendar.JANUARY "calendar.JANUARY")
     and [`calendar.FEBRUARY`](https://docs.python.org/3/library/calendar.html#calendar.FEBRUARY "calendar.FEBRUARY")
    . (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636)
    .)
    
*   [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
    : use [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
     instead of [`codecs.open()`](https://docs.python.org/3/library/codecs.html#codecs.open "codecs.open")
    . ([gh-133038](https://github.com/python/cpython/issues/133038)
    )
    
*   `codeobject.co_lnotab`: use the [`codeobject.co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines")
     method instead.
    
*   [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
    :
    
    *   [`utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "datetime.datetime.utcnow")
        : use `datetime.datetime.now(tz=datetime.UTC)`.
        
    *   [`utcfromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp "datetime.datetime.utcfromtimestamp")
        : use `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.
        
*   [`gettext`](https://docs.python.org/3/library/gettext.html#module-gettext "gettext: Multilingual internationalization services.")
    : Plural value must be an integer.
    
*   [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
    :
    
    *   [`cache_from_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source")
         _debug\_override_ parameter is deprecated: use the _optimization_ parameter instead.
        
*   [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata")
    :
    
    *   `EntryPoints` tuple interface.
        
    *   Implicit `None` on return values.
        
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
    : the `warn()` method has been deprecated since Python 3.3, use [`warning()`](https://docs.python.org/3/library/logging.html#logging.warning "logging.warning")
     instead.
    
*   [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
    : Use of StringIO input and text mode is deprecated, use BytesIO and binary mode instead.
    
*   [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
    : Calling [`os.register_at_fork()`](https://docs.python.org/3/library/os.html#os.register_at_fork "os.register_at_fork")
     in a multi-threaded process.
    
*   [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
    : [`os.path.commonprefix()`](https://docs.python.org/3/library/os.path.html#os.path.commonprefix "os.path.commonprefix")
     is deprecated, use [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath")
     for path prefixes. The `os.path.commonprefix()` function is being deprecated due to having a misleading name and module. The function is not safe to use for path prefixes despite being included in a module about path manipulation, meaning it is easy to accidentally introduce path traversal vulnerabilities into Python programs by using this function.
    
*   `pydoc.ErrorDuringImport`: A tuple value for _exc\_info_ parameter is deprecated, use an exception instance.
    
*   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
    : More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760)
    .)
    
*   [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
    : [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")
    ’s _onerror_ parameter is deprecated in Python 3.12; use the _onexc_ parameter instead.
    
*   [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     options and protocols:
    
    *   [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
         without protocol argument is deprecated.
        
    *   [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
        : [`set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols")
         and `selected_npn_protocol()` are deprecated: use ALPN instead.
        
    *   `ssl.OP_NO_SSL*` options
        
    *   `ssl.OP_NO_TLS*` options
        
    *   `ssl.PROTOCOL_SSLv3`
        
    *   `ssl.PROTOCOL_TLS`
        
    *   `ssl.PROTOCOL_TLSv1`
        
    *   `ssl.PROTOCOL_TLSv1_1`
        
    *   `ssl.PROTOCOL_TLSv1_2`
        
    *   `ssl.TLSVersion.SSLv3`
        
    *   `ssl.TLSVersion.TLSv1`
        
    *   `ssl.TLSVersion.TLSv1_1`
        
*   [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     methods:
    
    *   `threading.Condition.notifyAll()`: use [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all")
        .
        
    *   `threading.Event.isSet()`: use [`is_set()`](https://docs.python.org/3/library/threading.html#threading.Event.is_set "threading.Event.is_set")
        .
        
    *   `threading.Thread.isDaemon()`, [`threading.Thread.setDaemon()`](https://docs.python.org/3/library/threading.html#threading.Thread.setDaemon "threading.Thread.setDaemon")
        : use [`threading.Thread.daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon")
         attribute.
        
    *   `threading.Thread.getName()`, [`threading.Thread.setName()`](https://docs.python.org/3/library/threading.html#threading.Thread.setName "threading.Thread.setName")
        : use [`threading.Thread.name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name")
         attribute.
        
    *   `threading.currentThread()`: use [`threading.current_thread()`](https://docs.python.org/3/library/threading.html#threading.current_thread "threading.current_thread")
        .
        
    *   `threading.activeCount()`: use [`threading.active_count()`](https://docs.python.org/3/library/threading.html#threading.active_count "threading.active_count")
        .
        
*   [`typing.Text`](https://docs.python.org/3/library/typing.html#typing.Text "typing.Text")
     ([gh-92332](https://github.com/python/cpython/issues/92332)
    ).
    
*   The internal class `typing._UnionGenericAlias` is no longer used to implement [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")
    . To preserve compatibility with users using this private class, a compatibility shim will be provided until at least Python 3.17. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499)
    .)
    
*   [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase "unittest.IsolatedAsyncioTestCase")
    : it is deprecated to return a value that is not `None` from a test case.
    
*   [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.")
     deprecated functions: [`urlparse()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse "urllib.parse.urlparse")
     instead
    
    *   `splitattr()`
        
    *   `splithost()`
        
    *   `splitnport()`
        
    *   `splitpasswd()`
        
    *   `splitport()`
        
    *   `splitquery()`
        
    *   `splittag()`
        
    *   `splittype()`
        
    *   `splituser()`
        
    *   `splitvalue()`
        
    *   `to_bytes()`
        
*   [`wsgiref`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref "wsgiref: WSGI Utilities and Reference Implementation.")
    : `SimpleHandler.stdout.write()` should not do partial writes.
    
*   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
    : Testing the truth value of an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
     is deprecated. In a future release it will always return `True`. Prefer explicit `len(elem)` or `elem is not None` tests instead.
    
*   [`sys._clear_type_cache()`](https://docs.python.org/3/library/sys.html#sys._clear_type_cache "sys._clear_type_cache")
     is deprecated: use [`sys._clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches")
     instead.
    

Soft deprecations[¶](https://docs.python.org/3/deprecations/index.html#soft-deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

There are no plans to remove [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 APIs.

*   [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match")
     and [`re.Pattern.match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match")
     are now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     in favor of the new [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")
     and [`re.Pattern.prefixmatch()`](https://docs.python.org/3/library/re.html#re.Pattern.prefixmatch "re.Pattern.prefixmatch")
     APIs, which have been added as alternate, more explicit names. These are intended to be used to alleviate confusion around what _match_ means by following the Zen of Python’s _“Explicit is better than implicit”_ mantra. Most other language regular expression libraries use an API named _match_ to mean what Python has always called _search_.
    
    We **do not** plan to remove the older `match()` name, as it has been used in code for over 30 years. Code supporting older versions of Python should continue to use `match()`, while new code should prefer `prefixmatch()`. See [prefixmatch() vs. match()](https://docs.python.org/3/library/re.html#prefixmatch-vs-match)
    .
    
    (Contributed by Gregory P. Smith in [gh-86519](https://github.com/python/cpython/issues/86519)
     and Hugo van Kemenade in [gh-148100](https://github.com/python/cpython/issues/148100)
    .)
    
*   Using `'F'` and `'D'` format type codes of the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
     module now are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     in favor of two-letter forms `'Zf'` and `'Zd'`. (Contributed by Sergey B Kirpichev in [gh-121249](https://github.com/python/cpython/issues/121249)
    .)
    

C API deprecations[¶](https://docs.python.org/3/deprecations/index.html#c-api-deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

### Pending removal in Python 3.15[¶](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-15 "Link to this heading")

*   The `PyImport_ImportModuleNoBlock()`: Use [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
     instead.
    
*   `PyWeakref_GetObject()` and `PyWeakref_GET_OBJECT()`: Use [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")
     instead. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get `PyWeakref_GetRef()` on Python 3.12 and older.
    
*   `PyUnicode_AsDecodedObject()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
     instead.
    
*   `PyUnicode_AsDecodedUnicode()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
     instead; Note that some codecs (for example, “base64”) may return a type other than [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    , such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   `PyUnicode_AsEncodedObject()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
     instead.
    
*   `PyUnicode_AsEncodedUnicode()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
     instead; Note that some codecs (for example, “base64”) may return a type other than [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , such as [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    .
    
*   Python initialization functions, deprecated in Python 3.13:
    
    *   `Py_GetPath()`: Use [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        ) instead.
        
    *   `Py_GetPrefix()`: Use [`PyConfig_Get("base_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")
        ) instead. Use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)
         need to be handled.
        
    *   `Py_GetExecPrefix()`: Use [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix")
        ) instead. Use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)
         need to be handled.
        
    *   `Py_GetProgramFullPath()`: Use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
        ) instead.
        
    *   `Py_GetProgramName()`: Use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
        ) instead.
        
    *   `Py_GetPythonHome()`: Use [`PyConfig_Get("home")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         or the [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
         environment variable instead.
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     on Python 3.13 and older.
    
*   Functions to configure Python’s initialization, deprecated in Python 3.11:
    
    *   `PySys_SetArgvEx()`: Set [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
         instead.
        
    *   `PySys_SetArgv()`: Set [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
         instead.
        
    *   `Py_SetProgramName()`: Set [`PyConfig.program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")
         instead.
        
    *   `Py_SetPythonHome()`: Set [`PyConfig.home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
         instead.
        
    *   `PySys_ResetWarnOptions()`: Clear [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")
         and `warnings.filters` instead.
        
    
    The [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     API should be used with [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     instead.
    
*   Global configuration variables:
    
    *   [`Py_DebugFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_DebugFlag "Py_DebugFlag")
        : Use [`PyConfig.parser_debug`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parser_debug "PyConfig.parser_debug")
         or [`PyConfig_Get("parser_debug")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_VerboseFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_VerboseFlag "Py_VerboseFlag")
        : Use [`PyConfig.verbose`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.verbose "PyConfig.verbose")
         or [`PyConfig_Get("verbose")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_QuietFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_QuietFlag "Py_QuietFlag")
        : Use [`PyConfig.quiet`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.quiet "PyConfig.quiet")
         or [`PyConfig_Get("quiet")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_InteractiveFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InteractiveFlag "Py_InteractiveFlag")
        : Use [`PyConfig.interactive`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive")
         or [`PyConfig_Get("interactive")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_InspectFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InspectFlag "Py_InspectFlag")
        : Use [`PyConfig.inspect`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.inspect "PyConfig.inspect")
         or [`PyConfig_Get("inspect")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_OptimizeFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_OptimizeFlag "Py_OptimizeFlag")
        : Use [`PyConfig.optimization_level`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.optimization_level "PyConfig.optimization_level")
         or [`PyConfig_Get("optimization_level")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_NoSiteFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_NoSiteFlag "Py_NoSiteFlag")
        : Use [`PyConfig.site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")
         or [`PyConfig_Get("site_import")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_BytesWarningFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag "Py_BytesWarningFlag")
        : Use [`PyConfig.bytes_warning`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning")
         or [`PyConfig_Get("bytes_warning")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_FrozenFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FrozenFlag "Py_FrozenFlag")
        : Use [`PyConfig.pathconfig_warnings`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings")
         or [`PyConfig_Get("pathconfig_warnings")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag "Py_IgnoreEnvironmentFlag")
        : Use [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
         or [`PyConfig_Get("use_environment")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag "Py_DontWriteBytecodeFlag")
        : Use [`PyConfig.write_bytecode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.write_bytecode "PyConfig.write_bytecode")
         or [`PyConfig_Get("write_bytecode")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_NoUserSiteDirectory`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory "Py_NoUserSiteDirectory")
        : Use [`PyConfig.user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
         or [`PyConfig_Get("user_site_directory")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_UnbufferedStdioFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag "Py_UnbufferedStdioFlag")
        : Use [`PyConfig.buffered_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.buffered_stdio "PyConfig.buffered_stdio")
         or [`PyConfig_Get("buffered_stdio")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_HashRandomizationFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag "Py_HashRandomizationFlag")
        : Use [`PyConfig.use_hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_hash_seed "PyConfig.use_hash_seed")
         and [`PyConfig.hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.hash_seed "PyConfig.hash_seed")
         or [`PyConfig_Get("hash_seed")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_IsolatedFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsolatedFlag "Py_IsolatedFlag")
        : Use [`PyConfig.isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
         or [`PyConfig_Get("isolated")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag "Py_LegacyWindowsFSEncodingFlag")
        : Use [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
         or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag "Py_LegacyWindowsStdioFlag")
        : Use [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio")
         or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: Use [`PyConfig.filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
         or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_FileSystemDefaultEncodeErrors`: Use [`PyConfig.filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
         or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_UTF8Mode`: Use [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
         or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead. (see [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
        )
        
    
    The [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     API should be used with [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     to set these options. Or [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     can be used to get these options at runtime.
    

### Pending removal in Python 3.16[¶](https://docs.python.org/3/deprecations/index.html#id1 "Link to this heading")

*   The bundled copy of `libmpdec`.
    

### Pending removal in Python 3.18[¶](https://docs.python.org/3/deprecations/index.html#id2 "Link to this heading")

*   The following private functions are deprecated and planned for removal in Python 3.18:
    
    *   `_PyBytes_Join()`: use [`PyBytes_Join()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Join "PyBytes_Join")
        .
        
    *   `_PyDict_GetItemStringWithError()`: use [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef")
        .
        
    *   `_PyDict_Pop()`: use [`PyDict_Pop()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "PyDict_Pop")
        .
        
    *   `_PyLong_Sign()`: use [`PyLong_GetSign()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetSign "PyLong_GetSign")
        .
        
    *   `_PyLong_FromDigits()` and `_PyLong_New()`: use [`PyLongWriter_Create()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "PyLongWriter_Create")
        .
        
    *   `_PyThreadState_UncheckedGet()`: use [`PyThreadState_GetUnchecked()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetUnchecked "PyThreadState_GetUnchecked")
        .
        
    *   `_PyUnicode_AsString()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8 "PyUnicode_AsUTF8")
        .
        
    *   `_PyUnicodeWriter_Init()`: replace `_PyUnicodeWriter_Init(&writer)` with [`writer = PyUnicodeWriter_Create(0)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Create "PyUnicodeWriter_Create")
        .
        
    *   `_PyUnicodeWriter_Finish()`: replace `_PyUnicodeWriter_Finish(&writer)` with [`PyUnicodeWriter_Finish(writer)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Finish "PyUnicodeWriter_Finish")
        .
        
    *   `_PyUnicodeWriter_Dealloc()`: replace `_PyUnicodeWriter_Dealloc(&writer)` with [`PyUnicodeWriter_Discard(writer)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Discard "PyUnicodeWriter_Discard")
        .
        
    *   `_PyUnicodeWriter_WriteChar()`: replace `_PyUnicodeWriter_WriteChar(&writer, ch)` with [`PyUnicodeWriter_WriteChar(writer, ch)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteChar "PyUnicodeWriter_WriteChar")
        .
        
    *   `_PyUnicodeWriter_WriteStr()`: replace `_PyUnicodeWriter_WriteStr(&writer, str)` with [`PyUnicodeWriter_WriteStr(writer, str)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "PyUnicodeWriter_WriteStr")
        .
        
    *   `_PyUnicodeWriter_WriteSubstring()`: replace `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)` with [`PyUnicodeWriter_WriteSubstring(writer, str, start, end)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring "PyUnicodeWriter_WriteSubstring")
        .
        
    *   `_PyUnicodeWriter_WriteASCIIString()`: replace `_PyUnicodeWriter_WriteASCIIString(&writer, str, size)` with [`PyUnicodeWriter_WriteASCII(writer, str, size)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII "PyUnicodeWriter_WriteASCII")
        .
        
    *   `_PyUnicodeWriter_WriteLatin1String()`: replace `_PyUnicodeWriter_WriteLatin1String(&writer, str, size)` by decoding the string with [`PyUnicode_DecodeLatin1()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLatin1 "PyUnicode_DecodeLatin1")
        , writing the result with [`PyUnicodeWriter_WriteStr()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "PyUnicodeWriter_WriteStr")
        , and releasing the result with [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
        .
        
    *   `_PyUnicodeWriter_Prepare()`: (no replacement).
        
    *   `_PyUnicodeWriter_PrepareKind()`: (no replacement).
        
    *   `_Py_HashPointer()`: use [`Py_HashPointer()`](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Py_HashPointer")
        .
        
    *   `_Py_fopen_obj()`: use [`Py_fopen()`](https://docs.python.org/3/c-api/sys.html#c.Py_fopen "Py_fopen")
        .
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get these new public functions on Python 3.13 and older. (Contributed by Victor Stinner in [gh-128863](https://github.com/python/cpython/issues/128863)
    .)
    

### Pending removal in Python 3.19[¶](https://docs.python.org/3/deprecations/index.html#id3 "Link to this heading")

*   [**PEP 456**](https://peps.python.org/pep-0456/)
     embedders support for the string hashing scheme definition.
    

### Pending removal in Python 3.20[¶](https://docs.python.org/3/deprecations/index.html#id4 "Link to this heading")

*   `_PyObject_CallMethodId()`, `_PyObject_GetAttrId()` and `_PyUnicode_FromId()` are deprecated since 3.15 and will be removed in 3.20. Instead, use [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
     and cache the result in the module state, then call [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod")
     or [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
    . (Contributed by Victor Stinner in [gh-141049](https://github.com/python/cpython/issues/141049)
    .)
    
*   The `cval` field in [`PyComplexObject`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "PyComplexObject")
     ([gh-128813](https://github.com/python/cpython/issues/128813)
    ). Use [`PyComplex_AsCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_AsCComplex "PyComplex_AsCComplex")
     and [`PyComplex_FromCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromCComplex "PyComplex_FromCComplex")
     to convert a Python complex number to/from the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
     representation.
    
*   Macros `Py_MATH_PIl` and `Py_MATH_El`.
    

### Pending removal in future versions[¶](https://docs.python.org/3/deprecations/index.html#id5 "Link to this heading")

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

*   [`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE "Py_TPFLAGS_HAVE_FINALIZE")
    : Unneeded since Python 3.8.
    
*   [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
    : Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
     instead.
    
*   [`PyErr_NormalizeException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NormalizeException "PyErr_NormalizeException")
    : Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
     instead.
    
*   [`PyErr_Restore()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore")
    : Use [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
     instead.
    
*   [`PyModule_GetFilename()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilename "PyModule_GetFilename")
    : Use [`PyModule_GetFilenameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")
     instead.
    
*   [`PyOS_AfterFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork "PyOS_AfterFork")
    : Use [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
     instead.
    
*   [`PySlice_GetIndicesEx()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndicesEx "PySlice_GetIndicesEx")
    : Use [`PySlice_Unpack()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack")
     and [`PySlice_AdjustIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_AdjustIndices "PySlice_AdjustIndices")
     instead.
    
*   [`PyUnicode_READY()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READY "PyUnicode_READY")
    : Unneeded since Python 3.12
    
*   `PyErr_Display()`: Use [`PyErr_DisplayException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")
     instead.
    
*   `_PyErr_ChainExceptions()`: Use `_PyErr_ChainExceptions1()` instead.
    
*   `PyBytesObject.ob_shash` member: call [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash")
     instead.
    
*   Thread Local Storage (TLS) API:
    
    *   [`PyThread_create_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_create_key "PyThread_create_key")
        : Use [`PyThread_tss_alloc()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_alloc "PyThread_tss_alloc")
         instead.
        
    *   [`PyThread_delete_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key "PyThread_delete_key")
        : Use [`PyThread_tss_free()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_free "PyThread_tss_free")
         instead.
        
    *   [`PyThread_set_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_set_key_value "PyThread_set_key_value")
        : Use [`PyThread_tss_set()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_set "PyThread_tss_set")
         instead.
        
    *   [`PyThread_get_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_get_key_value "PyThread_get_key_value")
        : Use [`PyThread_tss_get()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_get "PyThread_tss_get")
         instead.
        
    *   [`PyThread_delete_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key_value "PyThread_delete_key_value")
        : Use [`PyThread_tss_delete()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_delete "PyThread_tss_delete")
         instead.
        
    *   [`PyThread_ReInitTLS()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_ReInitTLS "PyThread_ReInitTLS")
        : Unneeded since Python 3.7.
        

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Deprecations](https://docs.python.org/3/deprecations/index.html#)
    *   [Pending removal in Python 3.16](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-16)
        
    *   [Pending removal in Python 3.17](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-17)
        
    *   [Pending removal in Python 3.18](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-18)
        
    *   [Pending removal in Python 3.19](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-19)
        
    *   [Pending removal in Python 3.20](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-20)
        
    *   [Pending removal in future versions](https://docs.python.org/3/deprecations/index.html#pending-removal-in-future-versions)
        
    *   [Soft deprecations](https://docs.python.org/3/deprecations/index.html#soft-deprecations)
        
    *   [C API deprecations](https://docs.python.org/3/deprecations/index.html#c-api-deprecations)
        *   [Pending removal in Python 3.15](https://docs.python.org/3/deprecations/index.html#pending-removal-in-python-3-15)
            
        *   [Pending removal in Python 3.16](https://docs.python.org/3/deprecations/index.html#id1)
            
        *   [Pending removal in Python 3.18](https://docs.python.org/3/deprecations/index.html#id2)
            
        *   [Pending removal in Python 3.19](https://docs.python.org/3/deprecations/index.html#id3)
            
        *   [Pending removal in Python 3.20](https://docs.python.org/3/deprecations/index.html#id4)
            
        *   [Pending removal in future versions](https://docs.python.org/3/deprecations/index.html#id5)
            

#### Previous topic

[“Why is Python Installed on my Computer?” FAQ](https://docs.python.org/3/faq/installed.html "previous chapter")

#### Next topic

[Glossary](https://docs.python.org/3/glossary.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Deprecations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Findex.html&pagesource=deprecations%2Findex.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/index.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/glossary.html "Glossary")
     |
*   [previous](https://docs.python.org/3/faq/installed.html "“Why is Python Installed on my Computer?” FAQ")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Deprecations](https://docs.python.org/3/deprecations/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |