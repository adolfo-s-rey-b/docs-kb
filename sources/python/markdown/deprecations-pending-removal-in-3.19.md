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
*   [Pending removal in Python 3.19](https://docs.python.org/3/deprecations/pending-removal-in-3.19.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.19[¶](https://docs.python.org/3/deprecations/pending-removal-in-3.19.html#pending-removal-in-python-3-19 "Link to this heading")

=============================================================================================================================================================

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
        

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.19&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fpending-removal-in-3.19.html&pagesource=deprecations%2Fpending-removal-in-3.19.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/pending-removal-in-3.19.rst?plain=1)
    

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
*   [Pending removal in Python 3.19](https://docs.python.org/3/deprecations/pending-removal-in-3.19.html)
    
*    
    
    |
*   Theme Auto Light Dark |