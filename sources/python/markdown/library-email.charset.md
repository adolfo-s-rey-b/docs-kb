### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.encoders.html "email.encoders: Encoders")
     |
*   [previous](https://docs.python.org/3/library/email.header.html "email.header: Internationalized headers")
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
*   [`email.charset`: Representing character sets](https://docs.python.org/3/library/email.charset.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.charset`: Representing character sets[¶](https://docs.python.org/3/library/email.charset.html#module-email.charset "Link to this heading")

==================================================================================================================================================

**Source code:** [Lib/email/charset.py](https://github.com/python/cpython/tree/3.15/Lib/email/charset.py)

* * *

This module is part of the legacy (`Compat32`) email API. In the new API only the aliases table is used.

The remaining text in this section is the original documentation of the module.

This module provides a class [`Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset")
 for representing character sets and character set conversions in email messages, as well as a character set registry and several convenience methods for manipulating this registry. Instances of `Charset` are used in several other modules within the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package.

Import this class from the `email.charset` module.

class email.charset.Charset(_input\_charset\=DEFAULT\_CHARSET_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "Link to this definition")

Map character sets to their email properties.

This class provides information about the requirements imposed on email for a specific character set. It also provides convenience routines for converting between character sets, given the availability of the applicable codecs. Given a character set, it will do its best to provide information on how to use that character set in an email message in an RFC-compliant way.

Certain character sets must be encoded with quoted-printable or base64 when used in email headers or bodies. Certain character sets must be converted outright, and are not allowed in email.

Optional _input\_charset_ is as described below; it is always coerced to lower case. After being alias normalized it is also used as a lookup into the registry of character sets to find out the header encoding, body encoding, and output conversion codec to be used for the character set. For example, if _input\_charset_ is `iso-8859-1`, then headers and bodies will be encoded using quoted-printable and no output conversion codec is necessary. If _input\_charset_ is `euc-jp`, then headers will be encoded with base64, bodies will not be encoded, but output text will be converted from the `euc-jp` character set to the `iso-2022-jp` character set.

`Charset` instances have the following data attributes:

input\_charset[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.input_charset "Link to this definition")

The initial character set specified. Common aliases are converted to their _official_ email names (e.g. `latin_1` is converted to `iso-8859-1`). Defaults to 7-bit `us-ascii`.

header\_encoding[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.header_encoding "Link to this definition")

If the character set must be encoded before it can be used in an email header, this attribute will be set to `charset.QP` (for quoted-printable), `charset.BASE64` (for base64 encoding), or `charset.SHORTEST` for the shortest of QP or BASE64 encoding. Otherwise, it will be `None`.

body\_encoding[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.body_encoding "Link to this definition")

Same as _header\_encoding_, but describes the encoding for the mail message’s body, which indeed may be different than the header encoding. `charset.SHORTEST` is not allowed for _body\_encoding_.

output\_charset[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.output_charset "Link to this definition")

Some character sets must be converted before they can be used in email headers or bodies. If the _input\_charset_ is one of them, this attribute will contain the name of the character set output will be converted to. Otherwise, it will be `None`.

input\_codec[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.input_codec "Link to this definition")

The name of the Python codec used to convert the _input\_charset_ to Unicode. If no conversion codec is necessary, this attribute will be `None`.

output\_codec[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.output_codec "Link to this definition")

The name of the Python codec used to convert Unicode to the _output\_charset_. If no conversion codec is necessary, this attribute will have the same value as the _input\_codec_.

`Charset` instances also have the following methods:

get\_body\_encoding()[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.get_body_encoding "Link to this definition")

Return the content transfer encoding used for body encoding.

This is either the string `quoted-printable` or `base64` depending on the encoding used, or it is a function, in which case you should call the function with a single argument, the Message object being encoded. The function should then set the _Content-Transfer-Encoding_ header itself to whatever is appropriate.

Returns the string `quoted-printable` if _body\_encoding_ is `QP`, returns the string `base64` if _body\_encoding_ is `BASE64`, and returns the string `7bit` otherwise.

get\_output\_charset()[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.get_output_charset "Link to this definition")

Return the output character set.

This is the _output\_charset_ attribute if that is not `None`, otherwise it is _input\_charset_.

header\_encode(_string_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.header_encode "Link to this definition")

Header-encode the string _string_.

The type of encoding (base64 or quoted-printable) will be based on the _header\_encoding_ attribute.

header\_encode\_lines(_string_, _maxlengths_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.header_encode_lines "Link to this definition")

Header-encode a _string_ by converting it first to bytes.

This is similar to [`header_encode()`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.header_encode "email.charset.Charset.header_encode")
 except that the string is fit into maximum line lengths as given by the argument _maxlengths_, which must be an iterator: each element returned from this iterator will provide the next maximum line length.

body\_encode(_string_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.body_encode "Link to this definition")

Body-encode the string _string_.

The type of encoding (base64 or quoted-printable) will be based on the _body\_encoding_ attribute.

The `Charset` class also provides a number of methods to support standard operations and built-in functions.

\_\_str\_\_()[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.__str__ "Link to this definition")

Returns _input\_charset_ as a string coerced to lower case. `__repr__()` is an alias for `__str__()`.

\_\_eq\_\_(_other_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.__eq__ "Link to this definition")

This method allows you to compare two `Charset` instances for equality.

\_\_ne\_\_(_other_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.__ne__ "Link to this definition")

This method allows you to compare two `Charset` instances for inequality.

The `email.charset` module also provides the following functions for adding new entries to the global character set, alias, and codec registries:

email.charset.add\_charset(_charset_, _header\_enc\=None_, _body\_enc\=None_, _output\_charset\=None_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.add_charset "Link to this definition")

Add character properties to the global registry.

_charset_ is the input character set, and must be the canonical name of a character set.

Optional _header\_enc_ and _body\_enc_ is either `charset.QP` for quoted-printable, `charset.BASE64` for base64 encoding, `charset.SHORTEST` for the shortest of quoted-printable or base64 encoding, or `None` for no encoding. `SHORTEST` is only valid for _header\_enc_. The default is `None` for no encoding.

Optional _output\_charset_ is the character set that the output should be in. Conversions will proceed from input charset, to Unicode, to the output charset when the method [`Charset.body_encode()`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset.body_encode "email.charset.Charset.body_encode")
 is called. The default is to output in the same character set as the input.

Both _input\_charset_ and _output\_charset_ must have Unicode codec entries in the module’s character set-to-codec mapping; use [`add_codec()`](https://docs.python.org/3/library/email.charset.html#email.charset.add_codec "email.charset.add_codec")
 to add codecs the module does not know about. See the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
 module’s documentation for more information.

The global character set registry is kept in the module global dictionary `CHARSETS`.

email.charset.add\_alias(_alias_, _canonical_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.add_alias "Link to this definition")

Add a character set alias. _alias_ is the alias name, e.g. `latin-1`. _canonical_ is the character set’s canonical name, e.g. `iso-8859-1`.

The global charset alias registry is kept in the module global dictionary `ALIASES`.

email.charset.add\_codec(_charset_, _codecname_)[¶](https://docs.python.org/3/library/email.charset.html#email.charset.add_codec "Link to this definition")

Add a codec that map characters in the given character set to and from Unicode.

_charset_ is the canonical name of a character set. _codecname_ is the name of a Python codec, as appropriate for the second argument to the [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
’s [`encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
 method.

#### Previous topic

[`email.header`: Internationalized headers](https://docs.python.org/3/library/email.header.html "previous chapter")

#### Next topic

[`email.encoders`: Encoders](https://docs.python.org/3/library/email.encoders.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.charset%3A+Representing+character+sets&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.charset.html&pagesource=library%2Femail.charset.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.charset.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.encoders.html "email.encoders: Encoders")
     |
*   [previous](https://docs.python.org/3/library/email.header.html "email.header: Internationalized headers")
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
*   [`email.charset`: Representing character sets](https://docs.python.org/3/library/email.charset.html)
    
*    
    
    |
*   Theme Auto Light Dark |