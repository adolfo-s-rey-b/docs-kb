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
*   [Pending removal in Python 3.20](https://docs.python.org/3/deprecations/pending-removal-in-3.20.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.20[¶](https://docs.python.org/3/deprecations/pending-removal-in-3.20.html#pending-removal-in-python-3-20 "Link to this heading")

=============================================================================================================================================================

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
        

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.20&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fpending-removal-in-3.20.html&pagesource=deprecations%2Fpending-removal-in-3.20.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/pending-removal-in-3.20.rst?plain=1)
    

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
*   [Pending removal in Python 3.20](https://docs.python.org/3/deprecations/pending-removal-in-3.20.html)
    
*    
    
    |
*   Theme Auto Light Dark |