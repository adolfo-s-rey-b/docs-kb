### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/quopri.html "quopri — Encode and decode MIME quoted-printable data")
     |
*   [previous](https://docs.python.org/3/library/base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings")
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
*   [`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`binascii` — Convert between binary and ASCII[¶](https://docs.python.org/3/library/binascii.html#module-binascii "Link to this heading")

=========================================================================================================================================

* * *

The `binascii` module contains a number of methods to convert between binary and various ASCII-encoded binary representations. Normally, you will not use these functions directly but use wrapper modules like [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
 instead. The `binascii` module contains low-level functions written in C for greater speed that are used by the higher-level modules.

Note

`a2b_*` functions accept Unicode strings containing only ASCII characters. Other functions only accept [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 (such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 and other objects that support the buffer protocol).

Changed in version 3.3: ASCII-only unicode strings are now accepted by the `a2b_*` functions.

The `binascii` module defines the following functions:

binascii.a2b\_uu(_string_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_uu "Link to this definition")

Convert a single line of uuencoded data back to binary and return the binary data. Lines normally contain 45 (binary) bytes, except for the last line. Line data may be followed by whitespace.

binascii.b2a\_uu(_data_, _\*_, _backtick\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_uu "Link to this definition")

Convert binary data to a line of ASCII characters, the return value is the converted line, including a newline char. The length of _data_ should be at most 45. If _backtick_ is true, zeros are represented by ``'`'`` instead of spaces.

Changed in version 3.7: Added the _backtick_ parameter.

binascii.a2b\_base64(_string_, _/_, _\*_, _padded\=True_, _alphabet\=BASE64\_ALPHABET_, _strict\_mode\=False_, _canonical\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "Link to this definition")

binascii.a2b\_base64(_string_, _/_, _\*_, _ignorechars_, _padded\=True_, _alphabet\=BASE64\_ALPHABET_, _strict\_mode\=True_, _canonical\=False_)

Convert a block of base64 data back to binary and return the binary data. More than one line may be passed at a time.

Optional _alphabet_ must be a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object of length 64 which specifies an alternative alphabet.

If _padded_ is true, the last group of 4 base 64 alphabet characters must be padded with the ‘=’ character. If _padded_ is false, padding is neither required nor recognized: the ‘=’ character is not treated as padding but as a non-alphabet character, which means it is silently discarded when _strict\_mode_ is false, or causes an [`Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 when _strict\_mode_ is true unless b’=’ is included in _ignorechars_.

If _ignorechars_ is specified, it should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input when _strict\_mode_ is true. If _ignorechars_ contains the pad character `'='`, the pad characters presented before the end of the encoded data and the excess pad characters will be ignored. The default value of _strict\_mode_ is `True` if _ignorechars_ is specified, `False` otherwise.

If _strict\_mode_ is true, only valid base64 data will be converted. Invalid base64 data will raise [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
.

Valid base64:

*   Conforms to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
    .
    
*   Contains only characters from the base64 alphabet.
    
*   Contains no excess data after padding (including excess padding, newlines, etc.).
    
*   Does not start with a padding.
    

If _canonical_ is true, non-zero padding bits in the last group are rejected with [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
, enforcing canonical encoding as defined in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 section 3.5. This check is independent of _strict\_mode_.

Changed in version 3.11: Added the _strict\_mode_ parameter.

Changed in version 3.15: Added the _alphabet_, _canonical_, _ignorechars_, and _padded_ parameters.

binascii.b2a\_base64(_data_, _\*_, _padded\=True_, _alphabet\=BASE64\_ALPHABET_, _wrapcol\=0_, _newline\=True_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_base64 "Link to this definition")

Convert binary data to a line(s) of ASCII characters in base64 coding, as specified in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
.

If _padded_ is true (default), pad the encoded data with the ‘=’ character to a size multiple of 4. If _padded_ is false, do not add the pad characters.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not insert any newlines.

If _newline_ is true (default), a newline character will be added at the end of the output.

Changed in version 3.6: Added the _newline_ parameter.

Changed in version 3.15: Added the _alphabet_, _padded_ and _wrapcol_ parameters.

binascii.a2b\_ascii85(_string_, _/_, _\*_, _foldspaces\=False_, _adobe\=False_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_ascii85 "Link to this definition")

Convert Ascii85 data back to binary and return the binary data.

Valid Ascii85 data contains characters from the Ascii85 alphabet in groups of five (except for the final group, which may have from two to five characters). Each group encodes 32 bits of binary data in the range from `0` to `2 ** 32 - 1`, inclusive. The special character `z` is accepted as a short form of the group `!!!!!`, which encodes four consecutive null bytes. A single-character final group is always rejected as an encoding violation.

_foldspaces_ is a flag that specifies whether the ‘y’ short sequence should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is not supported by the “standard” Ascii85 encoding.

_adobe_ controls whether the encoded byte sequence is framed with `<~` and `~>`, as in a PostScript base-85 string literal. If _adobe_ is true, a leading `<~` is optionally accepted, while a trailing `~>` is _required_, and [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 is raised if it is not found.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input. This should only contain whitespace characters.

If _canonical_ is true, non-canonical encodings are rejected with [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
. Here “canonical” means the encoding that [`b2a_ascii85()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_ascii85 "binascii.b2a_ascii85")
 would produce: the `z` abbreviation must be used for all-zero groups (rather than `!!!!!`), and partial final groups must use the same padding digits as the encoder.

Invalid Ascii85 data will raise [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
.

Added in version 3.15.

binascii.b2a\_ascii85(_data_, _/_, _\*_, _foldspaces\=False_, _wrapcol\=0_, _pad\=False_, _adobe\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_ascii85 "Link to this definition")

Convert binary data to a formatted sequence of ASCII characters in Ascii85 coding. The return value is the converted data.

_foldspaces_ is an optional flag that uses the special short sequence ‘y’ instead of 4 consecutive spaces (ASCII 0x20) as supported by ‘btoa’. This feature is not supported by the “standard” Ascii85 encoding.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not insert any newlines.

If _pad_ is true, the zero-padding applied to the end of the input is fully retained in the output encoding, as done by `btoa`, producing an exact multiple of 5 bytes of output. This is not part of the standard encoding used in PDF, as it does not preserve the length of the data.

_adobe_ controls whether the encoded byte sequence is framed with `<~` and `~>`, as in a PostScript base-85 string literal. Note that while ASCII85Decode streams in PDF documents _must_ be terminated with `~>`, they _must not_ use a leading `<~`.

Added in version 3.15.

binascii.a2b\_base85(_string_, _/_, _\*_, _alphabet\=BASE85\_ALPHABET_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_base85 "Link to this definition")

Convert Base85 data back to binary and return the binary data. More than one line may be passed at a time.

Valid Base85 data contains characters from the Base85 alphabet in groups of five (except for the final group, which may have from two to five characters). Each group encodes 32 bits of binary data in the range from `0` to `2 ** 32 - 1`, inclusive. A single-character final group is always rejected as an encoding violation.

Optional _alphabet_ must be a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object of length 85 which specifies an alternative alphabet.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input.

If _canonical_ is true, non-canonical encodings are rejected with [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
. Here “canonical” means the encoding that [`b2a_base85()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base85 "binascii.b2a_base85")
 would produce: partial final groups must use the same padding digits as the encoder.

Invalid Base85 data will raise [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
.

Added in version 3.15.

binascii.b2a\_base85(_data_, _/_, _\*_, _alphabet\=BASE85\_ALPHABET_, _wrapcol\=0_, _pad\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_base85 "Link to this definition")

Convert binary data to a line of ASCII characters in Base85 coding. The return value is the converted line.

Optional _alphabet_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 of length 85 which specifies an alternative alphabet.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not insert any newlines.

If _pad_ is true, the zero-padding applied to the end of the input is retained in the output, which will always be a multiple of 5 bytes, and thus the length of the data may not be preserved on decoding.

Added in version 3.15.

binascii.a2b\_base32(_string_, _/_, _\*_, _padded\=True_, _alphabet\=BASE32\_ALPHABET_, _ignorechars\=b''_, _canonical\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_base32 "Link to this definition")

Convert base32 data back to binary and return the binary data.

Valid base32 data contains characters from the base32 alphabet specified in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 in groups of eight (if necessary, the final group is padded to eight characters with `=`). Each group encodes 40 bits of binary data in the range from `0` to `2 ** 40 - 1`, inclusive.

Note

This function does not map lowercase characters (which are invalid in standard base32) to their uppercase counterparts, nor does it contextually map `0` to `O` and `1` to `I`/`L` as [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 allows.

Optional _alphabet_ must be a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object of length 32 which specifies an alternative alphabet.

If _padded_ is true, the last group of 8 base 32 alphabet characters must be padded with the ‘=’ character. If _padded_ is false, the ‘=’ character is treated as other non-alphabet characters (depending on the value of _ignorechars_).

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input. If _ignorechars_ contains the pad character `'='`, the pad characters presented before the end of the encoded data and the excess pad characters will be ignored.

If _canonical_ is true, non-zero padding bits in the last group are rejected with [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
, enforcing canonical encoding as defined in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
 section 3.5.

Invalid base32 data will raise [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
.

Added in version 3.15.

binascii.b2a\_base32(_data_, _/_, _\*_, _padded\=True_, _alphabet\=BASE32\_ALPHABET_, _wrapcol\=0_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_base32 "Link to this definition")

Convert binary data to a line of ASCII characters in base32 coding, as specified in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
. The return value is the converted line.

Optional _alphabet_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 of length 32 which specifies an alternative alphabet.

If _padded_ is true (default), pad the encoded data with the ‘=’ character to a size multiple of 8. If _padded_ is false, do not add the pad characters.

If _wrapcol_ is non-zero, insert a newline (`b'\n'`) character after at most every _wrapcol_ characters. If _wrapcol_ is zero (default), do not insert any newlines.

Added in version 3.15.

binascii.a2b\_qp(_data_, _header\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_qp "Link to this definition")

Convert a block of quoted-printable data back to binary and return the binary data. More than one line may be passed at a time. If the optional argument _header_ is present and true, underscores will be decoded as spaces.

binascii.b2a\_qp(_data_, _quotetabs\=False_, _istext\=True_, _header\=False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_qp "Link to this definition")

Convert binary data to a line(s) of ASCII characters in quoted-printable encoding. The return value is the converted line(s). If the optional argument _quotetabs_ is present and true, all tabs and spaces will be encoded. If the optional argument _istext_ is present and true, newlines are not encoded but trailing whitespace will be encoded. If the optional argument _istext_ is present and false, newline characters will be encoded as well; otherwise linefeed conversion might corrupt the binary data stream. If the optional argument _header_ is present and true, spaces will be encoded as underscores per [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html)
.

binascii.crc\_hqx(_data_, _value_)[¶](https://docs.python.org/3/library/binascii.html#binascii.crc_hqx "Link to this definition")

Compute a 16-bit CRC value of _data_, starting with _value_ as the initial CRC, and return the result. This uses the CRC-CCITT polynomial _x_16 + _x_12 + _x_5 + 1, often represented as 0x1021. This CRC is used in the binhex4 format.

binascii.crc32(_data_\[, _value_\])[¶](https://docs.python.org/3/library/binascii.html#binascii.crc32 "Link to this definition")

Compute CRC-32, the unsigned 32-bit checksum of _data_, starting with an initial CRC of _value_. The default initial CRC is zero. The algorithm is consistent with the ZIP file checksum. Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use as a general hash algorithm. Use as follows:

Copy

print(binascii.crc32(b"hello world"))
\# Or, in two pieces:
crc \= binascii.crc32(b"hello")
crc \= binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))

Changed in version 3.0: The result is always unsigned.

binascii.b2a\_hex(_data_\[, _sep_\[, _bytes\_per\_sep\=1_\]\])[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_hex "Link to this definition")

binascii.hexlify(_data_\[, _sep_\[, _bytes\_per\_sep\=1_\]\])[¶](https://docs.python.org/3/library/binascii.html#binascii.hexlify "Link to this definition")

Return the hexadecimal representation of the binary _data_. Every byte of _data_ is converted into the corresponding 2-digit hex representation. The returned bytes object is therefore twice as long as the length of _data_.

Similar functionality (but returning a text string) is also conveniently accessible using the [`bytes.hex()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.hex "bytes.hex")
 method.

If _sep_ is specified, it must be a single character str or bytes object. It will be inserted in the output after every _bytes\_per\_sep_ input bytes. Separator placement is counted from the right end of the output by default, if you wish to count from the left, supply a negative _bytes\_per\_sep_ value.

Copy

\>>> import binascii
\>>> binascii.b2a\_hex(b'\\xb9\\x01\\xef')
b'b901ef'
\>>> binascii.hexlify(b'\\xb9\\x01\\xef', '-')
b'b9-01-ef'
\>>> binascii.b2a\_hex(b'\\xb9\\x01\\xef', b'\_', 2)
b'b9\_01ef'
\>>> binascii.b2a\_hex(b'\\xb9\\x01\\xef', b' ', \-2)
b'b901 ef'

Changed in version 3.8: The _sep_ and _bytes\_per\_sep_ parameters were added.

binascii.a2b\_hex(_hexstr_, _\*_, _ignorechars\=b''_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_hex "Link to this definition")

binascii.unhexlify(_hexstr_, _\*_, _ignorechars\=b''_)[¶](https://docs.python.org/3/library/binascii.html#binascii.unhexlify "Link to this definition")

Return the binary data represented by the hexadecimal string _hexstr_. This function is the inverse of [`b2a_hex()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_hex "binascii.b2a_hex")
. _hexstr_ must contain an even number of hexadecimal digits (which can be upper or lower case), otherwise an [`Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
 exception is raised.

_ignorechars_ should be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 containing characters to ignore from the input.

Similar functionality (but more liberal towards whitespace) is also accessible using the [`bytes.fromhex()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.fromhex "bytes.fromhex")
 class method.

Changed in version 3.15: Added the _ignorechars_ parameter.

exception binascii.Error[¶](https://docs.python.org/3/library/binascii.html#binascii.Error "Link to this definition")

Exception raised on errors. These are usually programming errors.

exception binascii.Incomplete[¶](https://docs.python.org/3/library/binascii.html#binascii.Incomplete "Link to this definition")

Exception raised on incomplete data. These are usually not programming errors, but may be handled by reading a little more data and trying again.

binascii.BASE64\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.BASE64_ALPHABET "Link to this definition")

The Base 64 alphabet according to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
.

Added in version 3.15.

binascii.URLSAFE\_BASE64\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.URLSAFE_BASE64_ALPHABET "Link to this definition")

The “URL and filename safe” Base 64 alphabet according to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
.

Added in version 3.15.

binascii.UU\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.UU_ALPHABET "Link to this definition")

The uuencoding alphabet.

Added in version 3.15.

binascii.CRYPT\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.CRYPT_ALPHABET "Link to this definition")

The Base 64 alphabet used in the _[crypt(3)](https://manpages.debian.org/crypt(3))
_ routine and in the GEDCOM format.

Added in version 3.15.

binascii.BINHEX\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.BINHEX_ALPHABET "Link to this definition")

The Base 64 alphabet used in BinHex 4 (HQX) within the classic Mac OS.

Added in version 3.15.

binascii.BASE85\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.BASE85_ALPHABET "Link to this definition")

The Base85 alphabet.

Added in version 3.15.

binascii.ASCII85\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.ASCII85_ALPHABET "Link to this definition")

The Ascii85 alphabet.

Added in version 3.15.

binascii.Z85\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.Z85_ALPHABET "Link to this definition")

The [Z85](https://rfc.zeromq.org/spec/32/)
 alphabet.

Added in version 3.15.

binascii.BASE32\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.BASE32_ALPHABET "Link to this definition")

The Base 32 alphabet according to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
.

Added in version 3.15.

binascii.BASE32HEX\_ALPHABET[¶](https://docs.python.org/3/library/binascii.html#binascii.BASE32HEX_ALPHABET "Link to this definition")

The “Extended Hex” Base 32 alphabet according to [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
. Data encoded with this alphabet maintains its sort order during bitwise comparisons.

Added in version 3.15.

See also

Module [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")

Support for RFC compliant base64-style encoding in base 16, 32, 64, and 85.

Module [`quopri`](https://docs.python.org/3/library/quopri.html#module-quopri "quopri: Encode and decode files using the MIME quoted-printable encoding.")

Support for quoted-printable encoding used in MIME email messages.

#### Previous topic

[`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html "previous chapter")

#### Next topic

[`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=binascii+%E2%80%94+Convert+between+binary+and+ASCII&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbinascii.html&pagesource=library%2Fbinascii.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/binascii.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/quopri.html "quopri — Encode and decode MIME quoted-printable data")
     |
*   [previous](https://docs.python.org/3/library/base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings")
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
*   [`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html)
    
*    
    
    |
*   Theme Auto Light Dark |