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
*   [Pending removal in future versions](https://docs.python.org/3/deprecations/pending-removal-in-future.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in future versions[¶](https://docs.python.org/3/deprecations/pending-removal-in-future.html#pending-removal-in-future-versions "Link to this heading")

=======================================================================================================================================================================

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
    

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+future+versions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fpending-removal-in-future.html&pagesource=deprecations%2Fpending-removal-in-future.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/pending-removal-in-future.rst?plain=1)
    

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
*   [Pending removal in future versions](https://docs.python.org/3/deprecations/pending-removal-in-future.html)
    
*    
    
    |
*   Theme Auto Light Dark |