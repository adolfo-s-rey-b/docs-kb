### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/time.html "PyTime C API")
     |
*   [previous](https://docs.python.org/3/c-api/reflection.html "Reflection")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Codec registry and support functions](https://docs.python.org/3/c-api/codec.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Codec registry and support functions[¶](https://docs.python.org/3/c-api/codec.html#codec-registry-and-support-functions "Link to this heading")

================================================================================================================================================

int PyCodec\_Register([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*search\_function)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Register "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Register a new codec search function.

As a side effect, this tries to load the `encodings` package, if not yet done, to make sure that it is always first in the list of search functions.

int PyCodec\_Unregister([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*search\_function)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Unregister "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Unregister a codec search function and clear the registry’s cache. If the search function is not registered, do nothing. Return 0 on success. Raise an exception and return -1 on error.

Added in version 3.10.

int PyCodec\_KnownEncoding(const char \*encoding)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_KnownEncoding "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` or `0` depending on whether there is a registered codec for the given _encoding_. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_Encode([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object, const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Generic codec based encoding API.

_object_ is passed through the encoder function found for the given _encoding_ using the error handling method defined by _errors_. _errors_ may be `NULL` to use the default method defined for the codec. Raises a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
 if no encoder can be found.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_Decode([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object, const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Generic codec based decoding API.

_object_ is passed through the decoder function found for the given _encoding_ using the error handling method defined by _errors_. _errors_ may be `NULL` to use the default method defined for the codec. Raises a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
 if no decoder can be found.

Codec lookup API[¶](https://docs.python.org/3/c-api/codec.html#codec-lookup-api "Link to this heading")

--------------------------------------------------------------------------------------------------------

In the following functions, the _encoding_ string is looked up converted to all lower-case characters, which makes encodings looked up through this mechanism effectively case-insensitive. If no codec is found, a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
 is set and `NULL` returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_Encoder(const char \*encoding)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encoder "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get an encoder function for the given _encoding_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_Decoder(const char \*encoding)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decoder "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get a decoder function for the given _encoding_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_IncrementalEncoder(const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_IncrementalEncoder "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get an [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "codecs.IncrementalEncoder")
 object for the given _encoding_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_IncrementalDecoder(const char \*encoding, const char \*errors)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_IncrementalDecoder "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get an [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder")
 object for the given _encoding_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_StreamReader(const char \*encoding, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*stream, const char \*errors)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_StreamReader "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get a [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader")
 factory function for the given _encoding_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_StreamWriter(const char \*encoding, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*stream, const char \*errors)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_StreamWriter "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get a [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter")
 factory function for the given _encoding_.

Registry API for Unicode encoding error handlers[¶](https://docs.python.org/3/c-api/codec.html#registry-api-for-unicode-encoding-error-handlers "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

int PyCodec\_RegisterError(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*error)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_RegisterError "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Register the error handling callback function _error_ under the given _name_. This callback function will be called by a codec when it encounters unencodable characters/undecodable bytes and _name_ is specified as the error parameter in the call to the encode/decode function.

The callback gets a single argument, an instance of [`UnicodeEncodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeEncodeError "UnicodeEncodeError")
, [`UnicodeDecodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")
 or [`UnicodeTranslateError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeTranslateError "UnicodeTranslateError")
 that holds information about the problematic sequence of characters or bytes and their offset in the original string (see [Unicode Exception Objects](https://docs.python.org/3/c-api/exceptions.html#unicodeexceptions)
 for functions to extract this information). The callback must either raise the given exception, or return a two-item tuple containing the replacement for the problematic sequence, and an integer giving the offset in the original string at which encoding/decoding should be resumed.

Return `0` on success, `-1` on error.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_LookupError(const char \*name)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_LookupError "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Lookup the error handling callback function registered under _name_. As a special case `NULL` can be passed, in which case the error handling callback for “strict” will be returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_StrictErrors([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_StrictErrors "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Raise _exc_ as an exception.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_IgnoreErrors([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_IgnoreErrors "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Ignore the unicode error, skipping the faulty input.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_ReplaceErrors([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_ReplaceErrors "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Replace the unicode encode error with `?` or `U+FFFD`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_XMLCharRefReplaceErrors([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_XMLCharRefReplaceErrors "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Replace the unicode encode error with XML character references.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_BackslashReplaceErrors([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_BackslashReplaceErrors "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Replace the unicode encode error with backslash escapes (`\x`, `\u` and `\U`).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCodec\_NameReplaceErrors([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/codec.html#c.PyCodec_NameReplaceErrors "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Replace the unicode encode error with `\N{...}` escapes.

Added in version 3.5.

Codec utility variables[¶](https://docs.python.org/3/c-api/codec.html#codec-utility-variables "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

const char \*Py\_hexdigits[¶](https://docs.python.org/3/c-api/codec.html#c.Py_hexdigits "Link to this definition")
  

A string constant containing the lowercase hexadecimal digits: `"0123456789abcdef"`.

Added in version 3.3.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Codec registry and support functions](https://docs.python.org/3/c-api/codec.html#)
    *   [Codec lookup API](https://docs.python.org/3/c-api/codec.html#codec-lookup-api)
        
    *   [Registry API for Unicode encoding error handlers](https://docs.python.org/3/c-api/codec.html#registry-api-for-unicode-encoding-error-handlers)
        
    *   [Codec utility variables](https://docs.python.org/3/c-api/codec.html#codec-utility-variables)
        

#### Previous topic

[Reflection](https://docs.python.org/3/c-api/reflection.html "previous chapter")

#### Next topic

[PyTime C API](https://docs.python.org/3/c-api/time.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Codec+registry+and+support+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcodec.html&pagesource=c-api%2Fcodec.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/codec.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/time.html "PyTime C API")
     |
*   [previous](https://docs.python.org/3/c-api/reflection.html "Reflection")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Codec registry and support functions](https://docs.python.org/3/c-api/codec.html)
    
*    
    
    |
*   Theme Auto Light Dark |