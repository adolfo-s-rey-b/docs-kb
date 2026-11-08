### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/http.html "http — HTTP modules")
     |
*   [previous](https://docs.python.org/3/library/urllib.error.html "urllib.error — Exception classes raised by urllib.request")
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
*   [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`urllib.robotparser` — Parser for robots.txt[¶](https://docs.python.org/3/library/urllib.robotparser.html#module-urllib.robotparser "Link to this heading")

============================================================================================================================================================

**Source code:** [Lib/urllib/robotparser.py](https://github.com/python/cpython/tree/3.15/Lib/urllib/robotparser.py)

* * *

This module provides a single class, [`RobotFileParser`](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser "urllib.robotparser.RobotFileParser")
, which answers questions about whether or not a particular user agent can fetch a URL on the website that published the `robots.txt` file. For more details on the structure of `robots.txt` files, see [**RFC 9309**](https://datatracker.ietf.org/doc/html/rfc9309.html)
.

class urllib.robotparser.RobotFileParser(_url\=''_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser "Link to this definition")

This class provides methods to read, parse and answer questions about the `robots.txt` file at _url_.

set\_url(_url_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.set_url "Link to this definition")

Sets the URL referring to a `robots.txt` file.

read()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.read "Link to this definition")

Reads the `robots.txt` URL and feeds it to the parser.

parse(_lines_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.parse "Link to this definition")

Parses the lines argument.

can\_fetch(_useragent_, _url_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.can_fetch "Link to this definition")

Returns `True` if the _useragent_ is allowed to fetch the _url_ according to the rules contained in the parsed `robots.txt` file.

mtime()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.mtime "Link to this definition")

Returns the time the `robots.txt` file was last fetched. This is useful for long-running web spiders that need to check for new `robots.txt` files periodically.

modified()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.modified "Link to this definition")

Sets the time the `robots.txt` file was last fetched to the current time.

crawl\_delay(_useragent_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.crawl_delay "Link to this definition")

Returns the value of the `Crawl-delay` parameter from `robots.txt` for the _useragent_ in question. If there is no such parameter or it doesn’t apply to the _useragent_ specified or the `robots.txt` entry for this parameter has invalid syntax, return `None`.

Added in version 3.6.

request\_rate(_useragent_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.request_rate "Link to this definition")

Returns the contents of the `Request-rate` parameter from `robots.txt` as a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 `RequestRate(requests, seconds)`. If there is no such parameter or it doesn’t apply to the _useragent_ specified or the `robots.txt` entry for this parameter has invalid syntax, return `None`.

Added in version 3.6.

site\_maps()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.site_maps "Link to this definition")

Returns the contents of the `Sitemap` parameter from `robots.txt` in the form of a [`list()`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
. If there is no such parameter or the `robots.txt` entry for this parameter has invalid syntax, return `None`.

Added in version 3.8.

The following example demonstrates basic use of the [`RobotFileParser`](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser "urllib.robotparser.RobotFileParser")
 class:

Copy

\>>> import urllib.robotparser
\>>> rp \= urllib.robotparser.RobotFileParser()
\>>> rp.set\_url("http://www.pythontest.net/robots.txt")
\>>> rp.read()
\>>> rrate \= rp.request\_rate("\*")
\>>> rrate.requests
1
\>>> rrate.seconds
1
\>>> rp.crawl\_delay("\*")
6
\>>> rp.can\_fetch("\*", "http://www.pythontest.net/")
True
\>>> rp.can\_fetch("\*", "http://www.pythontest.net/no-robots-here/")
False

#### Previous topic

[`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html "previous chapter")

#### Next topic

[`http` — HTTP modules](https://docs.python.org/3/library/http.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.robotparser+%E2%80%94++Parser+for+robots.txt&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.robotparser.html&pagesource=library%2Furllib.robotparser.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/urllib.robotparser.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/http.html "http — HTTP modules")
     |
*   [previous](https://docs.python.org/3/library/urllib.error.html "urllib.error — Exception classes raised by urllib.request")
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
*   [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html)
    
*    
    
    |
*   Theme Auto Light Dark |