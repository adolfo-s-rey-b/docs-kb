### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII")
     |
*   [previous](https://docs.python.org/3/library/mimetypes.html "mimetypes — Map filenames to MIME types")
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
*   [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`base64` — Base16, Base32, Base64, Base85 Data Encodings[¶](https://docs.python.org/3/library/base64.html#module-base64 "Link to this heading")

================================================================================================================================================

**Source code:** [Lib/base64.py](https://github.com/python/cpython/tree/3.15/Lib/base64.py)

* * *

This module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data. This includes the [encodings specified in](https://docs.python.org/3/library/base64.html#base64-rfc-4648)
 [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 (Base64, Base32 and Base16), the [Base85 encoding](https://docs.python.org/3/library/base64.html#base64-base-85)
 specified in [PDF 2.0](https://pdfa.org/resource/iso-32000-2/)
, and non-standard variants of Base85 used elsewhere.

There are two interfaces provided by this module. The modern interface supports encoding [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 to ASCII [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, and decoding bytes-like objects or strings containing ASCII to `bytes`. Both base-64 alphabets defined in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 (normal, and URL- and filesystem-safe) are supported.

The [legacy interface](https://docs.python.org/3/library/base64.html#base64-legacy)
 does not support decoding from strings, but it does provide functions for encoding and decoding to and from [file objects](https://docs.python.org/3/glossary.html#term-file-object)
. It only supports the Base64 standard alphabet, and it adds newlines every 76 characters as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
. Note that if you are looking for [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 support you probably want to be looking at the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package instead.

Changed in version 3.3: ASCII-only Unicode strings are now accepted by the decoding functions of the modern interface.

Changed in version 3.4: Any [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 are now accepted by all encoding and decoding functions in this module. Ascii85/Base85 support added.

RFC 4648 Encodings[¶](https://docs.python.org/3/library/base64.html#rfc-4648-encodings "Link to this heading")

---------------------------------------------------------------------------------------------------------------

The [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 encodings are suitable for encoding binary data so that it can be safely sent by email, used as parts of URLs, or included as part of an HTTP POST request.

base64.b64encode(_s_, _altchars\=None_, _\*_, _padded\=True_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/base64.html#base64.b64encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_ using Base64 and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Optional _altchars_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 of length 2 which specifies an alternative alphabet for the `+` and `/` characters. This allows an application to e.g. generate URL or filesystem safe Base64 strings. The default is `None`, for which the standard Base64 alphabet is used.

If _padded_ is true (default), pad the encoded data with the ‘=’ character to a size multiple of 4. If _padded_ is false, do not add the pad characters.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not insert any newlines.

Changed in version 3.15: Added the _padded_ and _wrapcol_ parameters.

base64.b64decode(_s_, _altchars\=None_, _validate\=False_, _\*_, _padded\=True_, _canonical\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.b64decode "Link to this definition")

base64.b64decode(_s_, _altchars\=None_, _validate\=True_, _\*_, _ignorechars_, _padded\=True_, _canonical\=False_)

Decode the Base64 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Optional _altchars_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string of length 2 which specifies the alternative alphabet used instead of the `+` and `/` characters.

If _padded_ is true, the last group of 4 base 64 alphabet characters must be padded with the ‘=’ character. If _padded_ is false, padding is neither required nor recognized: the ‘=’ character is not treated as padding but as a non-alphabet character, which means it is silently discarded when _validate_ is false, or causes an [`Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 when _validate_ is true unless b’=’ is included in _ignorechars_.

A [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 exception is raised if _s_ is incorrectly padded.

If _ignorechars_ is specified, it should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input when _validate_ is true. If _ignorechars_ contains the pad character `'='`, the pad characters presented before the end of the encoded data and the excess pad characters will be ignored. The default value of _validate_ is `True` if _ignorechars_ is specified, `False` otherwise.

If _validate_ is false, characters that are neither in the normal base-64 alphabet nor (if _ignorechars_ is not specified) the alternative alphabet are discarded prior to the padding check, but the `+` and `/` characters keep their meaning if they are not in _altchars_ (they will be discarded in future Python versions).

If _validate_ is true, these non-alphabet characters in the input result in a [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
.

If _canonical_ is true, non-zero padding bits are rejected. See [`binascii.a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")
 for details.

For more information about the strict base64 check, see [`binascii.a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")

Changed in version 3.15: Added the _canonical_, _ignorechars_, and _padded_ parameters.

Deprecated since version 3.15: Accepting the `+` and `/` characters with an alternative alphabet is now deprecated.

base64.standard\_b64encode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.standard_b64encode "Link to this definition")

Encode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_ using the standard Base64 alphabet and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

base64.standard\_b64decode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.standard_b64decode "Link to this definition")

Decode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _s_ using the standard Base64 alphabet and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

base64.urlsafe\_b64encode(_s_, _\*_, _padded\=True_)[¶](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64encode "Link to this definition")

Encode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_ using the URL- and filesystem-safe alphabet, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
. The result can still contain `=` if _padded_ is true (default).

Changed in version 3.15: Added the _padded_ parameter.

base64.urlsafe\_b64decode(_s_, _\*_, _padded\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64decode "Link to this definition")

Decode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _s_ using the URL- and filesystem-safe alphabet, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Changed in version 3.15: Added the _padded_ parameter. Padding of input is no longer required by default.

Deprecated since version 3.15: Accepting the `+` and `/` characters is now deprecated.

base64.b32encode(_s_, _\*_, _padded\=True_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/base64.html#base64.b32encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_ using Base32 and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

If _padded_ is true (default), pad the encoded data with the ‘=’ character to a size multiple of 8. If _padded_ is false, do not add the pad characters.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not add any newlines.

Changed in version 3.15: Added the _padded_ and _wrapcol_ parameters.

base64.b32decode(_s_, _casefold\=False_, _map01\=None_, _\*_, _padded\=True_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.b32decode "Link to this definition")

Decode the Base32 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Optional _casefold_ is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is `False`.

[**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 allows for optional mapping of the digit 0 (zero) to the letter O (oh), and for optional mapping of the digit 1 (one) to either the letter I (eye) or letter L (el). The optional argument _map01_ when not `None`, specifies which letter the digit 1 should be mapped to (when _map01_ is not `None`, the digit 0 is always mapped to the letter O). For security purposes the default is `None`, so that 0 and 1 are not allowed in the input.

If _padded_ is true, the last group of 8 base 32 alphabet characters must be padded with the ‘=’ character. If _padded_ is false, padding is neither required nor recognized: the ‘=’ character is not treated as padding but as a non-alphabet character, which means it raises an [`Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 unless b’=’ is included in _ignorechars_.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input.

If _canonical_ is true, non-zero padding bits are rejected. See [`binascii.a2b_base32()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base32 "binascii.a2b_base32")
 for details.

A [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 is raised if _s_ is incorrectly padded or if there are non-alphabet characters present in the input.

Changed in version 3.15: Added the _canonical_, _ignorechars_, and _padded_ parameters.

base64.b32hexencode(_s_, _\*_, _padded\=True_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/base64.html#base64.b32hexencode "Link to this definition")

Similar to [`b32encode()`](https://docs.python.org/3/library/base64.html#base64.b32encode "base64.b32encode")
 but uses the Extended Hex Alphabet, as defined in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
.

Added in version 3.10.

Changed in version 3.15: Added the _padded_ and _wrapcol_ parameters.

base64.b32hexdecode(_s_, _casefold\=False_, _\*_, _padded\=True_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.b32hexdecode "Link to this definition")

Similar to [`b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "base64.b32decode")
 but uses the Extended Hex Alphabet, as defined in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
.

This version does not allow the digit 0 (zero) to the letter O (oh) and digit 1 (one) to either the letter I (eye) or letter L (el) mappings, all these characters are included in the Extended Hex Alphabet and are not interchangeable.

Added in version 3.10.

Changed in version 3.15: Added the _canonical_, _ignorechars_, and _padded_ parameters.

base64.b16encode(_s_, _\*_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/base64.html#base64.b16encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_ using Base16 and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not add any newlines.

Changed in version 3.15: Added the _wrapcol_ parameter.

base64.b16decode(_s_, _casefold\=False_, _\*_, _ignorechars\=b''_)[¶](https://docs.python.org/3/library/base64.html#base64.b16decode "Link to this definition")

Decode the Base16 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Optional _casefold_ is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is `False`.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input.

A [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 is raised if _s_ is incorrectly padded or if there are non-alphabet characters present in the input.

Changed in version 3.15: Added the _ignorechars_ parameter.

Base85 Encodings[¶](https://docs.python.org/3/library/base64.html#base85-encodings "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Base85 encoding is a family of algorithms which represent four bytes using five ASCII characters. Originally implemented in the Unix `btoa(1)` utility, a version of it was later adopted by Adobe in the PostScript language and is standardized in PDF 2.0 (ISO 32000-2). This version, in both its `btoa` and PDF variants, is implemented by [`a85encode()`](https://docs.python.org/3/library/base64.html#base64.a85encode "base64.a85encode")
.

A separate version, using a different output character set, was defined as an April Fool’s joke in [**RFC 1924**](https://datatracker.ietf.org/doc/html/rfc1924.html)
 but is now used by Git and other software. This version is implemented by [`b85encode()`](https://docs.python.org/3/library/base64.html#base64.b85encode "base64.b85encode")
.

Finally, a third version, using yet another output character set designed for safe inclusion in programming language strings, is defined by ZeroMQ and implemented here by [`z85encode()`](https://docs.python.org/3/library/base64.html#base64.z85encode "base64.z85encode")
.

The functions present in this module differ in how they handle the following:

*   Whether to include and expect enclosing `<~` and `~>` markers.
    
*   Whether to fold the input into multiple lines.
    
*   The set of ASCII characters used for encoding.
    
*   Compact encodings of sequences of spaces and null bytes.
    
*   The encoding of zero-padding bytes applied to the input.
    

Refer to the documentation of the individual functions for more information.

base64.a85encode(_b_, _\*_, _foldspaces\=False_, _wrapcol\=0_, _pad\=False_, _adobe\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.a85encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _b_ using Ascii85 and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

_foldspaces_ is an optional flag that uses the special short sequence ‘y’ instead of 4 consecutive spaces (ASCII 0x20) as supported by ‘btoa’. This feature is not supported by the standard encoding used in PDF.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not insert any newlines.

_pad_ controls whether zero-padding applied to the end of the input is fully retained in the output encoding, as done by `btoa`, producing an exact multiple of 5 bytes of output. This is not part of the standard encoding used in PDF, as it does not preserve the length of the data.

_adobe_ controls whether the encoded byte sequence is framed with `<~` and `~>`, as in a PostScript base-85 string literal. Note that while ASCII85Decode streams in PDF documents _must_ be terminated with `~>`, they _must not_ use a leading `<~`.

Added in version 3.4.

base64.a85decode(_b_, _\*_, _foldspaces\=False_, _adobe\=False_, _ignorechars\=b' \\t\\n\\r\\x0b'_, _canonical\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.a85decode "Link to this definition")

Decode the Ascii85 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _b_ and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

_foldspaces_ is a flag that specifies whether the ‘y’ short sequence should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is not supported by the standard Ascii85 encoding used in PDF and PostScript.

_adobe_ controls whether the `<~` and `~>` markers are present. While the leading `<~` is not required, the input must end with `~>`, or a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input. This should only contain whitespace characters, and by default contains all whitespace characters in ASCII.

If _canonical_ is true, non-canonical encodings are rejected. See [`binascii.a2b_ascii85()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_ascii85 "binascii.a2b_ascii85")
 for details.

Added in version 3.4.

Changed in version 3.15: Added the _canonical_ parameter. Single-character final groups are now always rejected as encoding violations.

base64.b85encode(_b_, _pad\=False_, _\*_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/base64.html#base64.b85encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _b_ using base85 (as used in e.g. git-style binary diffs) and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

The input is padded with `b'\0'` so its length is a multiple of 4 bytes before encoding. If _pad_ is true, all the resulting characters are retained in the output, which will always be a multiple of 5 bytes, and thus the length of the data may not be preserved on decoding.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not add any newlines.

Added in version 3.4.

Changed in version 3.15: Added the _wrapcol_ parameter.

base64.b85decode(_b_, _\*_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.b85decode "Link to this definition")

Decode the base85-encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _b_ and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input.

If _canonical_ is true, non-canonical encodings are rejected. See [`binascii.a2b_base85()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base85 "binascii.a2b_base85")
 for details.

Added in version 3.4.

Changed in version 3.15: Added the _canonical_ and _ignorechars_ parameters. Single-character final groups are now always rejected as encoding violations.

base64.z85encode(_s_, _pad\=False_, _\*_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/base64.html#base64.z85encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_ using Z85 (as used in ZeroMQ) and return the encoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

The input is padded with `b'\0'` so its length is a multiple of 4 bytes before encoding. If _pad_ is true, all the resulting characters are retained in the output, which will always be a multiple of 5 bytes, as required by the ZeroMQ standard.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not add any newlines.

Added in version 3.13.

Changed in version 3.15: The _pad_ parameter was added.

Changed in version 3.15: Added the _wrapcol_ parameter.

base64.z85decode(_s_, _\*_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/base64.html#base64.z85decode "Link to this definition")

Decode the Z85-encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input.

If _canonical_ is true, non-canonical encodings are rejected. See [`binascii.a2b_base85()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base85 "binascii.a2b_base85")
 for details.

Added in version 3.13.

Changed in version 3.15: Added the _canonical_ and _ignorechars_ parameters. Single-character final groups are now always rejected as encoding violations.

Legacy Interface[¶](https://docs.python.org/3/library/base64.html#legacy-interface "Link to this heading")

-----------------------------------------------------------------------------------------------------------

base64.decode(_input_, _output_)[¶](https://docs.python.org/3/library/base64.html#base64.decode "Link to this definition")

Decode the contents of the binary _input_ file and write the resulting binary data to the _output_ file. _input_ and _output_ must be [file objects](https://docs.python.org/3/glossary.html#term-file-object)
. _input_ will be read until `input.readline()` returns an empty bytes object.

base64.decodebytes(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.decodebytes "Link to this definition")

Decode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_, which must contain one or more lines of base64 encoded data, and return the decoded [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Added in version 3.1.

base64.encode(_input_, _output_)[¶](https://docs.python.org/3/library/base64.html#base64.encode "Link to this definition")

Encode the contents of the binary _input_ file and write the resulting base64 encoded data to the _output_ file. _input_ and _output_ must be [file objects](https://docs.python.org/3/glossary.html#term-file-object)
. _input_ will be read until `input.read()` returns an empty bytes object. `encode()` inserts a newline character (`b'\n'`) after every 76 bytes of the output, as well as ensuring that the output always ends with a newline, as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 (MIME).

base64.encodebytes(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.encodebytes "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _s_, which can contain arbitrary binary data, and return [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 containing the base64-encoded data, with newlines (`b'\n'`) inserted after every 76 bytes of output, and ensuring that there is a trailing newline, as per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html)
 (MIME).

Added in version 3.1.

An example usage of the module:

Copy

\>>> import base64
\>>> encoded \= base64.b64encode(b'data to be encoded')
\>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
\>>> data \= base64.b64decode(encoded)
\>>> data
b'data to be encoded'

Security Considerations[¶](https://docs.python.org/3/library/base64.html#security-considerations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

A new security considerations section was added to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 (section 12); it’s recommended to review the security section for any code deployed to production.

See also

Module [`binascii`](https://docs.python.org/3/library/binascii.html#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.")

Support module containing ASCII-to-binary and binary-to-ASCII conversions.

[**RFC 1521**](https://datatracker.ietf.org/doc/html/rfc1521.html)
 - MIME (Multipurpose Internet Mail Extensions) Part One: Mechanisms for Specifying and Describing the Format of Internet Message Bodies

Section 5.2, “Base64 Content-Transfer-Encoding,” provides the definition of the base64 encoding.

[ISO 32000-2 Portable document format - Part 2: PDF 2.0](https://pdfa.org/resource/iso-32000-2/)

Section 7.4.3, “ASCII85Decode Filter,” provides the definition of the Ascii85 encoding used in PDF and PostScript, including the output character set and the details of data length preservation using zero-padding and partial output groups.

[ZeroMQ RFC 32/Z85](https://rfc.zeromq.org/spec/32/)

The “Formal Specification” section provides the character set used in Z85.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html#)
    *   [RFC 4648 Encodings](https://docs.python.org/3/library/base64.html#rfc-4648-encodings)
        
    *   [Base85 Encodings](https://docs.python.org/3/library/base64.html#base85-encodings)
        
    *   [Legacy Interface](https://docs.python.org/3/library/base64.html#legacy-interface)
        
    *   [Security Considerations](https://docs.python.org/3/library/base64.html#security-considerations)
        

#### Previous topic

[`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html "previous chapter")

#### Next topic

[`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=base64+%E2%80%94+Base16%2C+Base32%2C+Base64%2C+Base85+Data+Encodings&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbase64.html&pagesource=library%2Fbase64.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/base64.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII")
     |
*   [previous](https://docs.python.org/3/library/mimetypes.html "mimetypes — Map filenames to MIME types")
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
*   [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
    
*    
    
    |
*   Theme Auto Light Dark |