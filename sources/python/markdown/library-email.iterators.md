### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/json.html "json — JSON encoder and decoder")
     |
*   [previous](https://docs.python.org/3/library/email.utils.html "email.utils: Miscellaneous utilities")
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
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
     »
*   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
     »
*   [`email.iterators`: Iterators](https://docs.python.org/3/library/email.iterators.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.iterators`: Iterators[¶](https://docs.python.org/3/library/email.iterators.html#module-email.iterators "Link to this heading")

======================================================================================================================================

**Source code:** [Lib/email/iterators.py](https://github.com/python/cpython/tree/3.15/Lib/email/iterators.py)

* * *

Iterating over a message object tree is fairly easy with the [`Message.walk`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.walk "email.message.Message.walk")
 method. The `email.iterators` module provides some useful higher level iterations over message object trees.

email.iterators.body\_line\_iterator(_msg_, _decode\=False_)[¶](https://docs.python.org/3/library/email.iterators.html#email.iterators.body_line_iterator "Link to this definition")

This iterates over all the payloads in all the subparts of _msg_, returning the string payloads line-by-line. It skips over all the subpart headers, and it skips over any subpart with a payload that isn’t a Python string. This is somewhat equivalent to reading the flat text representation of the message from a file using [`readline()`](https://docs.python.org/3/library/io.html#io.TextIOBase.readline "io.TextIOBase.readline")
, skipping over all the intervening headers.

Optional _decode_ is passed through to [`Message.get_payload`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_payload "email.message.Message.get_payload")
.

email.iterators.typed\_subpart\_iterator(_msg_, _maintype\='text'_, _subtype\=None_)[¶](https://docs.python.org/3/library/email.iterators.html#email.iterators.typed_subpart_iterator "Link to this definition")

This iterates over all the subparts of _msg_, returning only those subparts that match the MIME type specified by _maintype_ and _subtype_.

Note that _subtype_ is optional; if omitted, then subpart MIME type matching is done only with the main type. _maintype_ is optional too; it defaults to _text_.

Thus, by default `typed_subpart_iterator()` returns each subpart that has a MIME type of _text/\*_.

The following function has been added as a useful debugging tool. It should _not_ be considered part of the supported public interface for the package.

email.iterators.\_structure(_msg_, _fp\=None_, _level\=0_, _include\_default\=False_)[¶](https://docs.python.org/3/library/email.iterators.html#email.iterators._structure "Link to this definition")

Prints an indented representation of the content types of the message object structure. For example:

Copy

\>>> msg \= email.message\_from\_file(somefile)
\>>> \_structure(msg)
multipart/mixed
    text/plain
    text/plain
    multipart/digest
        message/rfc822
            text/plain
        message/rfc822
            text/plain
        message/rfc822
            text/plain
        message/rfc822
            text/plain
        message/rfc822
            text/plain
    text/plain

Optional _fp_ is a file-like object to print the output to. It must be suitable for Python’s [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function. _level_ is used internally. _include\_default_, if true, prints the default type as well.

#### Previous topic

[`email.utils`: Miscellaneous utilities](https://docs.python.org/3/library/email.utils.html "previous chapter")

#### Next topic

[`json` — JSON encoder and decoder](https://docs.python.org/3/library/json.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.iterators%3A+Iterators&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.iterators.html&pagesource=library%2Femail.iterators.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.iterators.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/json.html "json — JSON encoder and decoder")
     |
*   [previous](https://docs.python.org/3/library/email.utils.html "email.utils: Miscellaneous utilities")
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
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
     »
*   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
     »
*   [`email.iterators`: Iterators](https://docs.python.org/3/library/email.iterators.html)
    
*    
    
    |
*   Theme Auto Light Dark |