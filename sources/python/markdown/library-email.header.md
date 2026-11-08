### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.charset.html "email.charset: Representing character sets")
     |
*   [previous](https://docs.python.org/3/library/email.mime.html "email.mime: Creating email and MIME objects from scratch")
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
*   [`email.header`: Internationalized headers](https://docs.python.org/3/library/email.header.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.header`: Internationalized headers[¶](https://docs.python.org/3/library/email.header.html#module-email.header "Link to this heading")

=============================================================================================================================================

**Source code:** [Lib/email/header.py](https://github.com/python/cpython/tree/3.15/Lib/email/header.py)

* * *

This module is part of the legacy (`Compat32`) email API. In the current API encoding and decoding of headers is handled transparently by the dictionary-like API of the [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 class. In addition to uses in legacy code, this module can be useful in applications that need to completely control the character sets used when encoding headers.

The remaining text in this section is the original documentation of the module.

[**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
 is the base standard that describes the format of email messages. It derives from the older [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html)
 standard which came into widespread use at a time when most email was composed of ASCII characters only. [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
 is a specification written assuming email contains only 7-bit ASCII characters.

Of course, as email has been deployed worldwide, it has become internationalized, such that language specific character sets can now be used in email messages. The base standard still requires email messages to be transferred using only 7-bit ASCII characters, so a slew of RFCs have been written describing how to encode email containing non-ASCII characters into [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
\-compliant format. These RFCs include [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
, [**RFC 2046**](https://datatracker.ietf.org/doc/html/rfc2046.html)
, [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
, and [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html)
. The [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package supports these standards in its `email.header` and [`email.charset`](https://docs.python.org/3/library/email.charset.html#module-email.charset "email.charset: Character Sets")
 modules.

If you want to include non-ASCII characters in your email headers, say in the _Subject_ or _To_ fields, you should use the [`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header")
 class and assign the field in the [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 object to an instance of `Header` instead of using a string for the header value. Import the `Header` class from the `email.header` module. For example:

Copy

\>>> from email.message import Message
\>>> from email.header import Header
\>>> msg \= Message()
\>>> h \= Header('p\\xf6stal', 'iso-8859-1')
\>>> msg\['Subject'\] \= h
\>>> msg.as\_string()
'Subject: =?iso-8859-1?q?p=F6stal?=\\n\\n'

Notice here how we wanted the _Subject_ field to contain a non-ASCII character? We did this by creating a [`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header")
 instance and passing in the character set to use when encoding it. When the subsequent [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 instance was flattened, the _Subject_ field was properly [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 encoded. MIME-aware mail readers would show this header using the embedded ISO-8859-1 character.

Here is the [`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header")
 class description:

class email.header.Header(_s\=None_, _charset\=None_, _maxlinelen\=None_, _header\_name\=None_, _continuation\_ws\=' '_, _errors\='strict'_)[¶](https://docs.python.org/3/library/email.header.html#email.header.Header "Link to this definition")

Create a MIME-compliant header that can contain strings in different character sets.

Optional _s_ is the initial header value. If `None` (the default), the initial header value is not set. You can later append to the header with [`append()`](https://docs.python.org/3/library/email.header.html#email.header.Header.append "email.header.Header.append")
 method calls. _s_ may be an instance of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, but see the `append()` documentation for semantics.

Optional _charset_ serves two purposes: it has the same meaning as the _charset_ argument to the [`append()`](https://docs.python.org/3/library/email.header.html#email.header.Header.append "email.header.Header.append")
 method. It also sets the default character set for all subsequent `append()` calls that omit the _charset_ argument. If _charset_ is not provided in the constructor (the default), the `us-ascii` character set is used both as _s_’s initial charset and as the default for subsequent `append()` calls.

The maximum line length can be specified explicitly via _maxlinelen_. For splitting the first line to a shorter value (to account for the field header which isn’t included in _s_, e.g. _Subject_) pass in the name of the field in _header\_name_. The default _maxlinelen_ is 78, and the default value for _header\_name_ is `None`, meaning it is not taken into account for the first line of a long, split header.

Optional _continuation\_ws_ must be [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
\-compliant folding whitespace, and is usually either a space or a hard tab character. This character will be prepended to continuation lines. _continuation\_ws_ defaults to a single space character.

Optional _errors_ is passed straight through to the [`append()`](https://docs.python.org/3/library/email.header.html#email.header.Header.append "email.header.Header.append")
 method.

append(_s_, _charset\=None_, _errors\='strict'_)[¶](https://docs.python.org/3/library/email.header.html#email.header.Header.append "Link to this definition")

Append the string _s_ to the MIME header.

Optional _charset_, if given, should be a [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 instance (see [`email.charset`](https://docs.python.org/3/library/email.charset.html#module-email.charset "email.charset: Character Sets")
) or the name of a character set, which will be converted to a `Charset` instance. A value of `None` (the default) means that the _charset_ given in the constructor is used.

_s_ may be an instance of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
. If it is an instance of `bytes`, then _charset_ is the encoding of that byte string, and a [`UnicodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError "UnicodeError")
 will be raised if the string cannot be decoded with that character set.

If _s_ is an instance of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, then _charset_ is a hint specifying the character set of the characters in the string.

In either case, when producing an [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
\-compliant header using [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 rules, the string will be encoded using the output codec of the charset. If the string cannot be encoded using the output codec, a UnicodeError will be raised.

Optional _errors_ is passed as the errors argument to the decode call if _s_ is a byte string.

encode(_splitchars\=';, \\t'_, _maxlinelen\=None_, _linesep\='\\n'_)[¶](https://docs.python.org/3/library/email.header.html#email.header.Header.encode "Link to this definition")

Encode a message header into an RFC-compliant format, possibly wrapping long lines and encapsulating non-ASCII parts in base64 or quoted-printable encodings.

Optional _splitchars_ is a string containing characters which should be given extra weight by the splitting algorithm during normal header wrapping. This is in very rough support of [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html)
's ‘higher level syntactic breaks’: split points preceded by a splitchar are preferred during line splitting, with the characters preferred in the order in which they appear in the string. Space and tab may be included in the string to indicate whether preference should be given to one over the other as a split point when other split chars do not appear in the line being split. Splitchars does not affect [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 encoded lines.

_maxlinelen_, if given, overrides the instance’s value for the maximum line length.

_linesep_ specifies the characters used to separate the lines of the folded header. It defaults to the most useful value for Python application code (`\n`), but `\r\n` can be specified in order to produce headers with RFC-compliant line separators.

Changed in version 3.2: Added the _linesep_ argument.

The `Header` class also provides a number of methods to support standard operators and built-in functions.

\_\_str\_\_()[¶](https://docs.python.org/3/library/email.header.html#email.header.Header.__str__ "Link to this definition")

Returns an approximation of the `Header` as a string, using an unlimited line length. All pieces are decoded using the specified encoding and joined together appropriately. Any pieces with a charset of `'unknown-8bit'` are decoded as ASCII using the `'replace'` error handler.

Changed in version 3.2: Added handling for the `'unknown-8bit'` charset.

\_\_eq\_\_(_other_)[¶](https://docs.python.org/3/library/email.header.html#email.header.Header.__eq__ "Link to this definition")

This method allows you to compare two `Header` instances for equality.

\_\_ne\_\_(_other_)[¶](https://docs.python.org/3/library/email.header.html#email.header.Header.__ne__ "Link to this definition")

This method allows you to compare two `Header` instances for inequality.

The `email.header` module also provides the following convenient functions.

email.header.decode\_header(_header_)[¶](https://docs.python.org/3/library/email.header.html#email.header.decode_header "Link to this definition")

Decode a message header value without converting the character set. The header value is in _header_.

For historical reasons, this function may return either:

1.  A list of pairs containing each of the decoded parts of the header, `(decoded_bytes, charset)`, where _decoded\_bytes_ is always an instance of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , and _charset_ is either:
    
    > *   A lower case string containing the name of the character set specified.
    >     
    > *   `None` for non-encoded parts of the header.
    >     
    
2.  A list of length 1 containing a pair `(string, None)`, where _string_ is always an instance of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    .
    

An [`email.errors.HeaderParseError`](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderParseError "email.errors.HeaderParseError")
 may be raised when certain decoding errors occur (e.g. a base64 decoding exception).

Here are examples:

Copy

\>>> from email.header import decode\_header
\>>> decode\_header('=?iso-8859-1?q?p=F6stal?=')
\[(b'p\\xf6stal', 'iso-8859-1')\]
\>>> decode\_header('unencoded\_string')
\[('unencoded\_string', None)\]
\>>> decode\_header('bar =?utf-8?B?ZsOzbw==?=')
\[(b'bar ', None), (b'f\\xc3\\xb3o', 'utf-8')\]

Note

This function exists for backwards compatibility only. For new code, we recommend using [`email.headerregistry.HeaderRegistry`](https://docs.python.org/3/library/email.headerregistry.html#email.headerregistry.HeaderRegistry "email.headerregistry.HeaderRegistry")
.

email.header.make\_header(_decoded\_seq_, _maxlinelen\=None_, _header\_name\=None_, _continuation\_ws\=' '_)[¶](https://docs.python.org/3/library/email.header.html#email.header.make_header "Link to this definition")

Create a [`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header")
 instance from a sequence of pairs as returned by [`decode_header()`](https://docs.python.org/3/library/email.header.html#email.header.decode_header "email.header.decode_header")
.

[`decode_header()`](https://docs.python.org/3/library/email.header.html#email.header.decode_header "email.header.decode_header")
 takes a header value string and returns a sequence of pairs of the format `(decoded_string, charset)` where _charset_ is the name of the character set.

This function takes one of those sequence of pairs and returns a [`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header")
 instance. Optional _maxlinelen_, _header\_name_, and _continuation\_ws_ are as in the `Header` constructor.

Note

This function exists for backwards compatibility only, and is not recommended for use in new code.

#### Previous topic

[`email.mime`: Creating email and MIME objects from scratch](https://docs.python.org/3/library/email.mime.html "previous chapter")

#### Next topic

[`email.charset`: Representing character sets](https://docs.python.org/3/library/email.charset.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.header%3A+Internationalized+headers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.header.html&pagesource=library%2Femail.header.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.header.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.charset.html "email.charset: Representing character sets")
     |
*   [previous](https://docs.python.org/3/library/email.mime.html "email.mime: Creating email and MIME objects from scratch")
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
*   [`email.header`: Internationalized headers](https://docs.python.org/3/library/email.header.html)
    
*    
    
    |
*   Theme Auto Light Dark |