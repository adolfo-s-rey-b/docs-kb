### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/conversion.html "String conversion and formatting")
     |
*   [previous](https://docs.python.org/3/c-api/marshal.html "Data marshalling support")
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
*   [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Parsing arguments and building values[¶](https://docs.python.org/3/c-api/arg.html#parsing-arguments-and-building-values "Link to this heading")

================================================================================================================================================

These functions are useful when creating your own extension functions and methods. Additional information and examples are available in [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html#extending-index)
.

The first three of these functions described, [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
, [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
, and [`PyArg_Parse()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_Parse "PyArg_Parse")
, all use _format strings_ which are used to tell the function about the expected arguments. The format strings use the same syntax for each of these functions.

Parsing arguments[¶](https://docs.python.org/3/c-api/arg.html#parsing-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------

A format string consists of zero or more “format units.” A format unit describes one Python object; it is usually a single character or a parenthesized sequence of format units. With a few exceptions, a format unit that is not a parenthesized sequence normally corresponds to a single address argument to these functions. In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that matches the format unit; and the entry in \[square\] brackets is the type of the C variable(s) whose address should be passed.

### Strings and buffers[¶](https://docs.python.org/3/c-api/arg.html#strings-and-buffers "Link to this heading")

Note

On Python 3.12 and older, the macro `PY_SSIZE_T_CLEAN` must be defined before including `Python.h` to use all `#` variants of formats (`s#`, `y#`, etc.) explained below. This is not necessary on Python 3.13 and later.

These formats allow accessing an object as a contiguous chunk of memory. You don’t have to provide raw storage for the returned unicode or bytes area.

Unless otherwise stated, buffers are not NUL-terminated.

There are three ways strings and buffers can be converted to C:

*   Formats such as `y*` and `s*` fill a [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
     structure. This locks the underlying buffer so that the caller can subsequently use the buffer even inside a [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS "Py_BEGIN_ALLOW_THREADS")
     block without the risk of mutable data being resized or destroyed. As a result, **you have to call** [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
     after you have finished processing the data (or in any early abort case).
    
*   The `es`, `es#`, `et` and `et#` formats allocate the result buffer. **You have to call** [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
     after you have finished processing the data (or in any early abort case).
    
*   Other formats take a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     or a read-only [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
    , such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , and provide a `const char *` pointer to its buffer. In this case the buffer is “borrowed”: it is managed by the corresponding Python object, and shares the lifetime of this object. You won’t have to release any memory yourself.
    
    To ensure that the underlying buffer may be safely borrowed, the object’s [`PyBufferProcs.bf_releasebuffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer "PyBufferProcs.bf_releasebuffer")
     field must be `NULL`. This disallows common mutable objects such as [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    , but also some read-only objects such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
     of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
    Besides this `bf_releasebuffer` requirement, there is no check to verify whether the input object is immutable (e.g. whether it would honor a request for a writable buffer, or whether another thread can mutate the data).
    

`s` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) \[const char \*\]

Convert a Unicode object to a C pointer to a character string. A pointer to an existing string is stored in the character pointer variable whose address you pass. The C string is NUL-terminated. The Python string must not contain embedded null code points; if it does, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 exception is raised. Unicode objects are converted to C strings using `'utf-8'` encoding. If this conversion fails, a [`UnicodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError "UnicodeError")
 is raised.

Note

This format does not accept [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. If you want to accept filesystem paths and convert them to C character strings, it is preferable to use the `O&` format with [`PyUnicode_FSConverter()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSConverter "PyUnicode_FSConverter")
 as _converter_.

Changed in version 3.5: Previously, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 was raised when embedded null code points were encountered in the Python string.

`s*` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
) \[Py\_buffer\]

This format accepts Unicode objects as well as bytes-like objects. It fills a [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 structure provided by the caller. In this case the resulting C string may contain embedded NUL bytes. Unicode objects are converted to C strings using `'utf-8'` encoding.

`s#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, read-only [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Like `s*`, except that it provides a [borrowed buffer](https://docs.python.org/3/c-api/arg.html#c-arg-borrowed-buffer)
. The result is stored into two C variables, the first one a pointer to a C string, the second one its length. The string may contain embedded null bytes. Unicode objects are converted to C strings using `'utf-8'` encoding.

`z` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*\]

Like `s`, but the Python object may also be `None`, in which case the C pointer is set to `NULL`.

`z*` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or `None`) \[Py\_buffer\]

Like `s*`, but the Python object may also be `None`, in which case the `buf` member of the [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 structure is set to `NULL`.

`z#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, read-only [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 or `None`) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Like `s#`, but the Python object may also be `None`, in which case the C pointer is set to `NULL`.

`y` (read-only [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
) \[const char \*\]

This format converts a bytes-like object to a C pointer to a [borrowed](https://docs.python.org/3/c-api/arg.html#c-arg-borrowed-buffer)
 character string; it does not accept Unicode objects. The bytes buffer must not contain embedded null bytes; if it does, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 exception is raised.

Changed in version 3.5: Previously, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 was raised when embedded null bytes were encountered in the bytes buffer.

`y*` ([bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
) \[Py\_buffer\]

This variant on `s*` doesn’t accept Unicode objects, only bytes-like objects. **This is the recommended way to accept binary data.**

`y#` (read-only [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

This variant on `s#` doesn’t accept Unicode objects, only bytes-like objects.

`S` ([`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
) \[PyBytesObject \*\]

Requires that the Python object is a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object, without attempting any conversion. Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the object is not a bytes object. The C variable may also be declared as [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

`Y` ([`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
) \[PyByteArrayObject \*\]

Requires that the Python object is a [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 object, without attempting any conversion. Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the object is not a `bytearray` object. The C variable may also be declared as [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

`U` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) \[PyObject \*\]

Requires that the Python object is a Unicode object, without attempting any conversion. Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if the object is not a Unicode object. The C variable may also be declared as [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

`w*` (read-write [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
) \[Py\_buffer\]

This format accepts any object which implements the read-write buffer interface. It fills a [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 structure provided by the caller. The buffer may contain embedded null bytes. The caller has to call [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
 when it is done with the buffer.

`es` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) \[const char \*encoding, char \*\*buffer\]

This variant on `s` is used for encoding Unicode into a character buffer. It only works for encoded data without embedded NUL bytes.

This format requires two arguments. The first is only used as input, and must be a const char\* which points to the name of an encoding as a NUL-terminated string, or `NULL`, in which case `'utf-8'` encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char\*\*; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument.

[`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 will allocate a buffer of the needed size, copy the encoded data into this buffer and adjust _\*buffer_ to reference the newly allocated storage. The caller is responsible for calling [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
 to free the allocated buffer after use.

`et` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
) \[const char \*encoding, char \*\*buffer\]

Same as `es` except that byte string objects are passed through without recoding them. Instead, the implementation assumes that the byte string object uses the encoding passed in as parameter.

`es#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) \[const char \*encoding, char \*\*buffer, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
 \*buffer\_length\]

This variant on `s#` is used for encoding Unicode into a character buffer. Unlike the `es` format, this variant allows input data which contains NUL characters.

It requires three arguments. The first is only used as input, and must be a const char\* which points to the name of an encoding as a NUL-terminated string, or `NULL`, in which case `'utf-8'` encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char\*\*; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument. The third argument must be a pointer to an integer; the referenced integer will be set to the number of bytes in the output buffer.

There are two modes of operation:

If _\*buffer_ points a `NULL` pointer, the function will allocate a buffer of the needed size, copy the encoded data into this buffer and set _\*buffer_ to reference the newly allocated storage. The caller is responsible for calling [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
 to free the allocated buffer after usage.

If _\*buffer_ points to a non-`NULL` pointer (an already allocated buffer), [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 will use this location as the buffer and interpret the initial value of _\*buffer\_length_ as the buffer size. It will then copy the encoded data into the buffer and NUL-terminate it. If the buffer is not large enough, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be set.

In both cases, _\*buffer\_length_ is set to the length of the encoded data without the trailing NUL byte.

`et#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
) \[const char \*encoding, char \*\*buffer, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
 \*buffer\_length\]

Same as `es#` except that byte string objects are passed through without recoding them. Instead, the implementation assumes that the byte string object uses the encoding passed in as parameter.

Changed in version 3.12: `u`, `u#`, `Z`, and `Z#` are removed because they used a legacy `Py_UNICODE*` representation.

### Numbers[¶](https://docs.python.org/3/c-api/arg.html#numbers "Link to this heading")

These formats allow representing Python numbers or single characters as C numbers. Formats that require [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 or [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 can also use the corresponding special methods [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
, [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__")
 or [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
 to convert the Python object to the required type.

For signed integer formats, [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 is raised if the value is out of range for the C type. For unsigned integer formats, the most significant bits are silently truncated when the receiving field is too small to receive the value, and [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
 is emitted when the value is larger than the maximal value for the C type or less than the minimal value for the corresponding signed integer type of the same size.

`b` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned char\]

Convert a nonnegative Python integer to an unsigned tiny integer, stored in a C unsigned char.

`B` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned char\]

Convert a Python integer to a tiny integer without overflow checking, stored in a C unsigned char. Convert a Python integer to a C unsigned char.

`h` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[short int\]

Convert a Python integer to a C short int.

`H` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned short int\]

Convert a Python integer to a C unsigned short int.

`i` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[int\]

Convert a Python integer to a plain C int.

`I` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned int\]

Convert a Python integer to a C unsigned int.

`l` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[long int\]

Convert a Python integer to a C long int.

`k` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned long\]

Convert a Python integer to a C unsigned long.

Changed in version 3.14: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

`L` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[long long\]

Convert a Python integer to a C long long.

`K` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned long long\]

Convert a Python integer to a C unsigned long long.

Changed in version 3.14: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

`n` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[[`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Convert a Python integer to a C [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
.

`c` ([`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 of length 1) \[char\]

Convert a Python byte, represented as a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 object of length 1, to a C char.

Changed in version 3.3: Allow [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 objects.

`C` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 of length 1) \[int\]

Convert a Python character, represented as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object of length 1, to a C int.

`f` ([`float`](https://docs.python.org/3/builtins/functions.html#float "float")
) \[float\]

Convert a Python floating-point number to a C float.

`d` ([`float`](https://docs.python.org/3/builtins/functions.html#float "float")
) \[double\]

Convert a Python floating-point number to a C double.

`D` ([`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
) \[Py\_complex\]

Convert a Python complex number to a C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 structure.

Deprecated since version 3.15: For unsigned integer formats `B`, `H`, `I`, `k` and `K`, [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
 is emitted when the value is larger than the maximal value for the C type or less than the minimal value for the corresponding signed integer type of the same size.

### Other objects[¶](https://docs.python.org/3/c-api/arg.html#other-objects "Link to this heading")

`O` (object) \[PyObject \*\]

Store a Python object (without any conversion) in a C object pointer. The C program thus receives the actual object that was passed. A new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the object is not created (i.e. its reference count is not increased). The pointer stored is not `NULL`.

`O!` (object) \[_typeobject_, PyObject \*\]

Store a Python object in a C object pointer. This is similar to `O`, but takes two C arguments: the first is the address of a Python type object, the second is the address of the C variable (of type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*) into which the object pointer is stored. If the Python object does not have the required type, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

`O&` (object) \[_converter_, _address_\]

Convert a Python object to a C variable through a _converter_ function. This takes two arguments: the first is a function, the second is the address of a C variable (of arbitrary type), converted to void\*. The _converter_ function in turn is called as follows:

status \= converter(object, address);

where _object_ is the Python object to be converted and _address_ is the void\* argument that was passed to the `PyArg_Parse*` function. The returned _status_ should be `1` for a successful conversion and `0` if the conversion has failed. When the conversion fails, the _converter_ function should raise an exception and leave the content of _address_ unmodified.

If the _converter_ returns `Py_CLEANUP_SUPPORTED`, it may get called a second time if the argument parsing eventually fails, giving the converter a chance to release any memory that it had already allocated. In this second call, the _object_ parameter will be `NULL`; _address_ will have the same value as in the original call.

Examples of converters: [`PyUnicode_FSConverter()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSConverter "PyUnicode_FSConverter")
 and [`PyUnicode_FSDecoder()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSDecoder "PyUnicode_FSDecoder")
.

Changed in version 3.1: `Py_CLEANUP_SUPPORTED` was added.

`p` ([`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
) \[int\]

Tests the value passed in for truth (a boolean **p**redicate) and converts the result to its equivalent C true/false integer value. Sets the int to `1` if the expression was true and `0` if it was false. This accepts any valid Python value. See [Truth Value Testing](https://docs.python.org/3/builtins/stdtypes.html#truth)
 for more information about how Python tests values for truth.

Added in version 3.3.

`(items)` (sequence) \[_matching-items_\]

The object must be a Python sequence (except [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
) whose length is the number of format units in _items_. The C arguments must correspond to the individual format units in _items_. Format units for sequences may be nested.

If _items_ contains format units which store a [borrowed buffer](https://docs.python.org/3/c-api/arg.html#c-arg-borrowed-buffer)
 (`s`, `s#`, `z`, `z#`, `y`, or `y#`) or a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 (`S`, `Y`, `U`, `O`, or `O!`), the object must be a Python tuple. The _converter_ for the `O&` format unit in _items_ must not store a borrowed buffer or a borrowed reference.

Changed in version 3.14: [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 objects no longer accepted as a sequence.

Deprecated since version 3.14: Non-tuple sequences are deprecated if _items_ contains format units which store a borrowed buffer or a borrowed reference.

A few other characters have a meaning in a format string. These may not occur inside nested parentheses. They are:

`|`

Indicates that the remaining arguments in the Python argument list are optional. The C variables corresponding to optional arguments should be initialized to their default value — when an optional argument is not specified, [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 does not touch the contents of the corresponding C variable(s). For example, the format string `"OO|OO"` corresponds to the Python signature `f(a, b, c=None, d=None)`.

`$`

[`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
 only: Indicates that the remaining arguments in the Python argument list are keyword-only. They are optional if `|` was specified before `$`, and required otherwise. `|` cannot be specified after `$`. For example, the format string `"O|O$O"` corresponds to the Python signature `f(a, b=None, *, c=None)`, and the format string `"OO$OO"` corresponds to `f(a, b, *, c, d)`.

Added in version 3.3.

`:`

The list of format units ends here; the string after the colon is used as the function name in error messages (the “associated value” of the exception that [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 raises).

`;`

The list of format units ends here; the string after the semicolon is used as the error message _instead_ of the default error message. `:` and `;` mutually exclude each other.

Note that any Python object references which are provided to the caller are _borrowed_ references; do not release them (i.e. do not decrement their reference count)!

Additional arguments passed to these functions must be addresses of variables whose type is determined by the format string; these are used to store values from the input tuple. There are a few cases, as described in the list of format units above, where these parameters are used as input values; they should match what is specified for the corresponding format unit in that case.

For the conversion to succeed, the _arg_ object must match the format and the format must be exhausted. On success, the `PyArg_Parse*` functions return true, otherwise they return false and raise an appropriate exception. When the `PyArg_Parse*` functions fail due to conversion failure in one of the format units, the variables at the addresses corresponding to that and the following format units are left untouched.

### API Functions[¶](https://docs.python.org/3/c-api/arg.html#api-functions "Link to this heading")

int PyArg\_ParseTuple([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, const char \*format, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Parse the parameters of a function that takes only positional parameters into local variables. Returns true on success; on failure, it returns false and raises the appropriate exception.

int PyArg\_VaParse([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, const char \*format, va\_list vargs)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_VaParse "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Identical to [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
, except that it accepts a va\_list rather than a variable number of arguments.

int PyArg\_ParseTupleAndKeywords([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kw, const char \*format, char \*const \*keywords, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Parse the parameters of a function that takes both positional and keyword parameters into local variables. The _keywords_ argument is a `NULL`\-terminated array of keyword parameter names specified as null-terminated ASCII or UTF-8 encoded C strings. Empty names denote [positional-only parameters](https://docs.python.org/3/glossary.html#positional-only-parameter)
. Returns true on success; on failure, it returns false and raises the appropriate exception.

Note

The _keywords_ parameter declaration is char \*const\* in C and const char \*const\* in C++. This can be overridden with the [`PY_CXX_CONST`](https://docs.python.org/3/c-api/arg.html#c.PY_CXX_CONST "PY_CXX_CONST")
 macro.

Changed in version 3.6: Added support for [positional-only parameters](https://docs.python.org/3/glossary.html#positional-only-parameter)
.

Changed in version 3.13: The _keywords_ parameter has now type char \*const\* in C and const char \*const\* in C++, instead of char\*\*. Added support for non-ASCII keyword parameter names.

int PyArg\_VaParseTupleAndKeywords([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kw, const char \*format, char \*const \*keywords, va\_list vargs)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Identical to [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
, except that it accepts a va\_list rather than a variable number of arguments.

int PyArg\_ValidateKeywordArguments([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_ValidateKeywordArguments "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Ensure that the keys in the keywords argument dictionary are strings. This is only needed if [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
 is not used, since the latter already does this check.

Added in version 3.2.

int PyArg\_Parse([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, const char \*format, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_Parse "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Parse the parameter of a function that takes a single positional parameter into a local variable. Returns true on success; on failure, it returns false and raises the appropriate exception.

Example:

// Function using METH\_O calling convention
static PyObject\*
my\_function(PyObject \*module, PyObject \*arg)
{
    int value;
    if (!PyArg\_Parse(arg, "i:my\_function", &value)) {
        return NULL;
    }
    // ... use value ...
}

int PyArg\_ParseArray([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 nargs, const char \*format, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseArray "Link to this definition")
  

Parse the parameters of a function that takes only array parameters into local variables (that is, a function using the [`METH_FASTCALL`](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
 calling convention). Returns true on success; on failure, it returns false and raises the appropriate exception.

Added in version 3.15.

int PyArg\_ParseArrayAndKeywords([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 nargs, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwnames, const char \*format, const char \*const \*kwlist, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseArrayAndKeywords "Link to this definition")
  

Parse the parameters of a function that takes both array and keyword parameters into local variables (that is, a function using the [`METH_FASTCALL`](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
 `|` [`METH_KEYWORDS`](https://docs.python.org/3/c-api/structures.html#c.METH_KEYWORDS "METH_KEYWORDS")
 calling convention). Returns true on success; on failure, it returns false and raises the appropriate exception.

Added in version 3.15.

int PyArg\_UnpackTuple([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, const char \*name, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 min, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 max, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

A simpler form of parameter retrieval which does not use a format string to specify the types of the arguments. Functions which use this method to retrieve their parameters should be declared as [`METH_VARARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_VARARGS "METH_VARARGS")
 in function or method tables. The tuple containing the actual parameters should be passed as _args_; it must actually be a tuple. The length of the tuple must be at least _min_ and no more than _max_; _min_ and _max_ may be equal. Additional arguments must be passed to the function, each of which should be a pointer to a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* variable; these will be filled in with the values from _args_; they will contain [borrowed references](https://docs.python.org/3/glossary.html#term-borrowed-reference)
. The variables which correspond to optional parameters not given by _args_ will not be filled in; these should be initialized by the caller. This function returns true on success and false if _args_ is not a tuple or contains the wrong number of elements; an exception will be set if there was a failure.

This is an example of the use of this function, taken from the sources for the `_weakref` helper module for weak references:

static PyObject \*
weakref\_ref(PyObject \*self, PyObject \*args)
{
    PyObject \*object;
    PyObject \*callback \= NULL;
    PyObject \*result \= NULL;

    if (PyArg\_UnpackTuple(args, "ref", 1, 2, &object, &callback)) {
        result \= PyWeakref\_NewRef(object, callback);
    }
    return result;
}

The call to [`PyArg_UnpackTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple "PyArg_UnpackTuple")
 in this example is entirely equivalent to this call to [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
:

PyArg\_ParseTuple(args, "O|O:ref", &object, &callback)

PY\_CXX\_CONST[¶](https://docs.python.org/3/c-api/arg.html#c.PY_CXX_CONST "Link to this definition")
  

The value to be inserted, if any, before char \*const\* in the _keywords_ parameter declaration of [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
 and [`PyArg_VaParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords "PyArg_VaParseTupleAndKeywords")
. Default empty for C and `const` for C++ (const char \*const\*). To override, define it to the desired value before including `Python.h`.

Added in version 3.13.

Building values[¶](https://docs.python.org/3/c-api/arg.html#building-values "Link to this heading")

----------------------------------------------------------------------------------------------------

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_BuildValue(const char \*format, ...)[¶](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new value based on a format string similar to those accepted by the `PyArg_Parse*` family of functions and a sequence of values. Returns the value or `NULL` in the case of an error; an exception will be raised if `NULL` is returned.

[`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
 does not always build a tuple. It builds a tuple only if its format string contains two or more format units. If the format string is empty, it returns `None`; if it contains exactly one format unit, it returns whatever object is described by that format unit. To force it to return a tuple of size 0 or one, parenthesize the format string.

When memory buffers are passed as parameters to supply data to build objects, as for the `s` and `s#` formats, the required data is copied. Buffers provided by the caller are never referenced by the objects created by [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
. In other words, if your code invokes `malloc()` and passes the allocated memory to `Py_BuildValue()`, your code is responsible for calling `free()` for that memory once `Py_BuildValue()` returns.

In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that the format unit will return; and the entry in \[square\] brackets is the type of the C value(s) to be passed.

The characters space, tab, colon and comma are ignored in format strings (but not within format units such as `s#`). This can be used to make long format strings a tad more readable.

`s` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*\]

Convert a null-terminated C string to a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object using `'utf-8'` encoding. If the C string pointer is `NULL`, `None` is used.

`s#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Convert a C string and its length to a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object using `'utf-8'` encoding. If the C string pointer is `NULL`, the length is ignored and `None` is returned.

`y` ([`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
) \[const char \*\]

This converts a C string to a Python [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. If the C string pointer is `NULL`, `None` is returned.

`y#` ([`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

This converts a C string and its lengths to a Python object. If the C string pointer is `NULL`, `None` is returned.

`z` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*\]

Same as `s`.

`z#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Same as `s#`.

`u` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) \[const wchar\_t \*\]

Convert a null-terminated `wchar_t` buffer of Unicode (UTF-16 or UCS-4) data to a Python Unicode object. If the Unicode buffer pointer is `NULL`, `None` is returned.

`u#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
) \[const wchar\_t \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Convert a Unicode (UTF-16 or UCS-4) data buffer and its length to a Python Unicode object. If the Unicode buffer pointer is `NULL`, the length is ignored and `None` is returned.

`U` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*\]

Same as `s`.

`U#` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or `None`) \[const char \*, [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Same as `s#`.

`i` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[int\]

Convert a plain C int to a Python integer object.

`b` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[char\]

Convert a plain C char to a Python integer object.

`h` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[short int\]

Convert a plain C short int to a Python integer object.

`l` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[long int\]

Convert a C long int to a Python integer object.

`B` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned char\]

Convert a C unsigned char to a Python integer object.

`H` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned short int\]

Convert a C unsigned short int to a Python integer object.

`I` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned int\]

Convert a C unsigned int to a Python integer object.

`k` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned long\]

Convert a C unsigned long to a Python integer object.

`L` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[long long\]

Convert a C long long to a Python integer object.

`K` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[unsigned long long\]

Convert a C unsigned long long to a Python integer object.

`n` ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) \[[`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
\]

Convert a C [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 to a Python integer.

`p` ([`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
) \[int\]

Convert a C int to a Python [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 object.

Be aware that this format requires an `int` argument. Unlike most other contexts in C, variadic arguments are not coerced to a suitable type automatically. You can convert another type (for example, a pointer or a float) to a suitable `int` value using `(x) ? 1 : 0` or `!!x`.

Added in version 3.14.

`c` ([`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 of length 1) \[char\]

Convert a C int representing a byte to a Python [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object of length 1.

`C` ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 of length 1) \[int\]

Convert a C int representing a character to Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object of length 1.

`d` ([`float`](https://docs.python.org/3/builtins/functions.html#float "float")
) \[double\]

Convert a C double to a Python floating-point number.

`f` ([`float`](https://docs.python.org/3/builtins/functions.html#float "float")
) \[float\]

Convert a C float to a Python floating-point number.

`D` ([`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
) \[Py\_complex \*\]

Convert a C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
 structure to a Python complex number.

`O` (object) \[PyObject \*\]

Pass a Python object untouched but create a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to it (i.e. its reference count is incremented by one). If the object passed in is a `NULL` pointer, it is assumed that this was caused because the call producing the argument found an error and set an exception. Therefore, [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
 will return `NULL` but won’t raise an exception. If no exception has been raised yet, [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 is set.

`S` (object) \[PyObject \*\]

Same as `O`.

`N` (object) \[PyObject \*\]

Same as `O`, except it doesn’t create a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
. Useful when the object is created by a call to an object constructor in the argument list.

`O&` (object) \[_converter_, _anything_\]

Convert _anything_ to a Python object through a _converter_ function. The function is called with _anything_ (which should be compatible with void\*) as its argument and should return a “new” Python object, or `NULL` if an error occurred.

`(items)` ([`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
) \[_matching-items_\]

Convert a sequence of C values to a Python tuple with the same number of items.

`[items]` ([`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
) \[_matching-items_\]

Convert a sequence of C values to a Python list with the same number of items.

`{items}` ([`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
) \[_matching-items_\]

Convert a sequence of C values to a Python dictionary. Each pair of consecutive C values adds one item to the dictionary, serving as key and value, respectively.

If there is an error in the format string, the [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 exception is set and `NULL` returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_VaBuildValue(const char \*format, va\_list vargs)[¶](https://docs.python.org/3/c-api/arg.html#c.Py_VaBuildValue "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Identical to [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
, except that it accepts a va\_list rather than a variable number of arguments.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html#)
    *   [Parsing arguments](https://docs.python.org/3/c-api/arg.html#parsing-arguments)
        *   [Strings and buffers](https://docs.python.org/3/c-api/arg.html#strings-and-buffers)
            
        *   [Numbers](https://docs.python.org/3/c-api/arg.html#numbers)
            
        *   [Other objects](https://docs.python.org/3/c-api/arg.html#other-objects)
            
        *   [API Functions](https://docs.python.org/3/c-api/arg.html#api-functions)
            
    *   [Building values](https://docs.python.org/3/c-api/arg.html#building-values)
        

#### Previous topic

[Data marshalling support](https://docs.python.org/3/c-api/marshal.html "previous chapter")

#### Next topic

[String conversion and formatting](https://docs.python.org/3/c-api/conversion.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Parsing+arguments+and+building+values&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Farg.html&pagesource=c-api%2Farg.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/arg.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/conversion.html "String conversion and formatting")
     |
*   [previous](https://docs.python.org/3/c-api/marshal.html "Data marshalling support")
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
*   [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html)
    
*    
    
    |
*   Theme Auto Light Dark |