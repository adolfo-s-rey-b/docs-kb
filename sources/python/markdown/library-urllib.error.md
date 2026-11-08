### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/urllib.robotparser.html "urllib.robotparser — Parser for robots.txt")
     |
*   [previous](https://docs.python.org/3/library/urllib.parse.html "urllib.parse — Parse URLs into components")
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
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
     »
*   [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`urllib.error` — Exception classes raised by urllib.request[¶](https://docs.python.org/3/library/urllib.error.html#module-urllib.error "Link to this heading")

===============================================================================================================================================================

**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.15/Lib/urllib/error.py)

* * *

The `urllib.error` module defines the exception classes for exceptions raised by [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
. The base exception class is [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError")
.

The following exceptions are raised by `urllib.error` as appropriate:

exception urllib.error.URLError[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "Link to this definition")

The handlers raise this exception (or derived exceptions) when they run into a problem. It is a subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

reason[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError.reason "Link to this definition")

The reason for this error. It can be a message string or another exception instance.

Changed in version 3.3: `URLError` used to be a subtype of [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
, which is now an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

exception urllib.error.HTTPError(_url_, _code_, _msg_, _hdrs_, _fp_)[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "Link to this definition")

Though being an exception (a subclass of [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError")
), an `HTTPError` can also function as a non-exceptional file-like return value (the same thing that [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen")
 returns). This is useful when handling exotic HTTP errors, such as requests for authentication.

url[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.url "Link to this definition")

Contains the request URL. An alias for _filename_ attribute.

code[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.code "Link to this definition")

An HTTP status code as defined in [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html)
. This numeric value corresponds to a value found in the dictionary of codes as found in [`http.server.BaseHTTPRequestHandler.responses`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses "http.server.BaseHTTPRequestHandler.responses")
.

reason[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.reason "Link to this definition")

This is usually a string explaining the reason for this error. An alias for _msg_ attribute.

headers[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.headers "Link to this definition")

The HTTP response headers for the HTTP request that caused the `HTTPError`. An alias for _hdrs_ attribute.

Added in version 3.4.

fp[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.fp "Link to this definition")

A file-like object where the HTTP error body can be read from.

exception urllib.error.ContentTooShortError(_msg_, _content_)[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError "Link to this definition")

This exception is raised when the [`urlretrieve()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve")
 function detects that the amount of the downloaded data is less than the expected amount (given by the _Content-Length_ header).

content[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError.content "Link to this definition")

The downloaded (and supposedly truncated) data.

#### Previous topic

[`urllib.parse` — Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html "previous chapter")

#### Next topic

[`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.error+%E2%80%94+Exception+classes+raised+by+urllib.request&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.error.html&pagesource=library%2Furllib.error.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/urllib.error.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/urllib.robotparser.html "urllib.robotparser — Parser for robots.txt")
     |
*   [previous](https://docs.python.org/3/library/urllib.parse.html "urllib.parse — Parse URLs into components")
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
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
     »
*   [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html)
    
*    
    
    |
*   Theme Auto Light Dark |