### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/markup.html "Structured Markup Processing Tools")
     |
*   [previous](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII")
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
*   [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`quopri` — Encode and decode MIME quoted-printable data[¶](https://docs.python.org/3/library/quopri.html#module-quopri "Link to this heading")

===============================================================================================================================================

**Source code:** [Lib/quopri.py](https://github.com/python/cpython/tree/3.15/Lib/quopri.py)

* * *

This module performs quoted-printable transport encoding and decoding, as defined in [**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html)
: “MIME (Multipurpose Internet Mail Extensions) Part One: Mechanisms for Specifying and Describing the Format of Internet Message Bodies”. The quoted-printable encoding is designed for data where there are relatively few nonprintable characters; the base64 encoding scheme available via the [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
 module is more compact if there are many such characters, as when sending a graphics file.

quopri.decode(_input_, _output_, _header\=False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.decode "Link to this definition")

Decode the contents of the _input_ file and write the resulting decoded binary data to the _output_ file. _input_ and _output_ must be [binary file objects](https://docs.python.org/3/glossary.html#term-file-object)
. If the optional argument _header_ is present and true, underscore will be decoded as space. This is used to decode “Q”-encoded headers as described in [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html)
: “MIME (Multipurpose Internet Mail Extensions) Part Two: Message Header Extensions for Non-ASCII Text”.

quopri.encode(_input_, _output_, _quotetabs_, _header\=False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.encode "Link to this definition")

Encode the contents of the _input_ file and write the resulting quoted-printable data to the _output_ file. _input_ and _output_ must be [binary file objects](https://docs.python.org/3/glossary.html#term-file-object)
. _quotetabs_, a non-optional flag which controls whether to encode embedded spaces and tabs; when true it encodes such embedded whitespace, and when false it leaves them unencoded. Note that spaces and tabs appearing at the end of lines are always encoded, as per [**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html)
. _header_ is a flag which controls if spaces are encoded as underscores as per [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html)
.

quopri.decodestring(_s_, _header\=False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.decodestring "Link to this definition")

Like [`decode()`](https://docs.python.org/3/library/quopri.html#quopri.decode "quopri.decode")
, except that it accepts a source [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and returns the corresponding decoded `bytes`.

quopri.encodestring(_s_, _quotetabs\=False_, _header\=False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.encodestring "Link to this definition")

Like [`encode()`](https://docs.python.org/3/library/quopri.html#quopri.encode "quopri.encode")
, except that it accepts a source [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and returns the corresponding encoded `bytes`. By default, it sends a `False` value to _quotetabs_ parameter of the `encode()` function.

See also

Module [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")

Encode and decode MIME base64 data

#### Previous topic

[`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html "previous chapter")

#### Next topic

[Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=quopri+%E2%80%94+Encode+and+decode+MIME+quoted-printable+data&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fquopri.html&pagesource=library%2Fquopri.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/quopri.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/markup.html "Structured Markup Processing Tools")
     |
*   [previous](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII")
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
*   [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html)
    
*    
    
    |
*   Theme Auto Light Dark |