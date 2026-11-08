### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/bytearray.html "Byte Array Objects")
     |
*   [previous](https://docs.python.org/3/c-api/complex.html "Complex Number Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Bytes Objects](https://docs.python.org/3/c-api/bytes.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Bytes Objects[¶](https://docs.python.org/3/c-api/bytes.html#bytes-objects "Link to this heading")

==================================================================================================

These functions raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 when expecting a bytes parameter and called with a non-bytes parameter.

**CPython implementation detail:** The internal buffer of [`PyBytesObject`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesObject "PyBytesObject")
 always includes an extra trailing null byte for compatibility with null terminated C strings. This extra byte is not counted in [`PyBytes_Size()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Size "PyBytes_Size")
 nor in the various _length_ and _size_ arguments of the functions below.

type PyBytesObject[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesObject "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python bytes object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyBytes\_Type[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python bytes type; it is the same object as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 in the Python layer.

int PyBytes\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Check "Link to this definition")
  

Return true if the object _o_ is a bytes object or an instance of a subtype of the bytes type. This function always succeeds.

int PyBytes\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_CheckExact "Link to this definition")
  

Return true if the object _o_ is a bytes object, but not an instance of a subtype of the bytes type. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_FromString(const char \*v)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new bytes object with a copy of the string _v_ as value on success, and `NULL` on failure. The parameter _v_ must not be `NULL`; it will not be checked.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_FromStringAndSize(const char \*v, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromStringAndSize "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new bytes object with a copy of the string _v_ as value and length _len_ on success, and `NULL` on failure. If _v_ is `NULL`, the contents of the bytes object are uninitialized.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Use the [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 API instead of `PyBytes_FromStringAndSize(NULL, len)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_FromFormat(const char \*format, ...)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromFormat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Take a C `printf()`\-style _format_ string and a variable number of arguments, calculate the size of the resulting Python bytes object and return a bytes object with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the _format_ string. The following format characters are allowed:

| Format Characters | Type | Comment |
| --- | --- | --- |
| `%%` | _n/a_ | The literal % character. |
| `%c` | int | A single byte, represented as a C int. |
| `%d` | int | Equivalent to `printf("%d")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%u` | unsigned int | Equivalent to `printf("%u")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%ld` | long | Equivalent to `printf("%ld")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%lu` | unsigned long | Equivalent to `printf("%lu")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%zd` | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | Equivalent to `printf("%zd")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%zu` | size\_t | Equivalent to `printf("%zu")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%i` | int | Equivalent to `printf("%i")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%x` | int | Equivalent to `printf("%x")`. [\[1\]](https://docs.python.org/3/c-api/bytes.html#id9) |
| `%s` | const char\* | A null-terminated C character array. |
| `%p` | const void\* | The hex representation of a C pointer. Mostly equivalent to `printf("%p")` except that it is guaranteed to start with the literal `0x` regardless of what the platform’s `printf` yields. |

An unrecognized format character causes all the rest of the format string to be copied as-is to the result object, and any extra arguments discarded.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_FromFormatV(const char \*format, va\_list vargs)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromFormatV "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Identical to [`PyBytes_FromFormat()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromFormat "PyBytes_FromFormat")
 except that it takes exactly two arguments.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_FromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Return the bytes representation of object _o_ that implements the buffer protocol.

Note

If the object implements the buffer protocol, then the buffer must not be mutated while the bytes object is being created.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyBytes\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return the length of the bytes in bytes object _o_.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyBytes\_GET\_SIZE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_GET_SIZE "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Similar to [`PyBytes_Size()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Size "PyBytes_Size")
, but without error checking.

char \*PyBytes\_AsString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Return a pointer to the contents of _o_. The pointer refers to the internal buffer of _o_, which consists of `len(o) + 1` bytes. The last byte in the buffer is always null, regardless of whether there are any other null bytes. The data must not be modified in any way, unless the object was just created using `PyBytes_FromStringAndSize(NULL, size)`. It must not be deallocated. If _o_ is not a bytes object at all, [`PyBytes_AsString()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsString "PyBytes_AsString")
 returns `NULL` and raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

char \*PyBytes\_AS\_STRING([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*string)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AS_STRING "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Similar to [`PyBytes_AsString()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsString "PyBytes_AsString")
, but without error checking.

int PyBytes\_AsStringAndSize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, char \*\*buffer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*length)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsStringAndSize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Return the null-terminated contents of the object _obj_ through the output variables _buffer_ and _length_. Returns `0` on success.

If _length_ is `NULL`, the bytes object may not contain embedded null bytes; if it does, the function returns `-1` and a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

The buffer refers to an internal buffer of _obj_, which includes an additional null byte at the end (not counted in _length_). The data must not be modified in any way, unless the object was just created using `PyBytes_FromStringAndSize(NULL, size)`. It must not be deallocated. If _obj_ is not a bytes object at all, [`PyBytes_AsStringAndSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsStringAndSize "PyBytes_AsStringAndSize")
 returns `-1` and raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

Changed in version 3.5: Previously, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 was raised when embedded null bytes were encountered in the bytes object.

void PyBytes\_Concat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*bytes, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*newpart)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Concat "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Create a new bytes object in _\*bytes_ containing the contents of _newpart_ appended to _bytes_; the caller will own the new reference. The reference to the old value of _bytes_ will be “[stolen](https://docs.python.org/3/glossary.html#term-steal)
”. If the new object cannot be created, the old reference to _bytes_ will still be “stolen”, the value of _\*bytes_ will be set to `NULL`, and the appropriate exception will be set.

Note

If _newpart_ implements the buffer protocol, then the buffer must not be mutated while the new bytes object is being created.

void PyBytes\_ConcatAndDel([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*bytes, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*newpart)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_ConcatAndDel "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Create a new bytes object in _\*bytes_ containing the contents of _newpart_ appended to _bytes_. This version releases the [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to _newpart_ (i.e. decrements its reference count).

Note

If _newpart_ implements the buffer protocol, then the buffer must not be mutated while the new bytes object is being created.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_Join([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*sep, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*iterable)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Join "Link to this definition")
  

_Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Similar to `sep.join(iterable)` in Python.

_sep_ must be Python [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. (Note that [`PyUnicode_Join()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Join "PyUnicode_Join")
 accepts `NULL` separator and treats it as a space, whereas [`PyBytes_Join()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Join "PyBytes_Join")
 doesn’t accept `NULL` separator.)

_iterable_ must be an iterable object yielding objects that implement the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
.

On success, return a new [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. On error, set an exception and return `NULL`.

Added in version 3.14.

Note

If _iterable_ objects implement the buffer protocol, then the buffers must not be mutated while the new bytes object is being created.

int \_PyBytes\_Resize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*bytes, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 newsize)[¶](https://docs.python.org/3/c-api/bytes.html#c._PyBytes_Resize "Link to this definition")
  

_Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Resize a bytes object. _newsize_ will be the new length of the bytes object. You can think of it as creating a new bytes object and destroying the old one, only more efficiently. Pass the address of an existing bytes object as an lvalue (it may be written into), and the new size desired. On success, _\*bytes_ holds the resized bytes object and `0` is returned; the address in _\*bytes_ may differ from its input value. If the reallocation fails, the original bytes object at _\*bytes_ is deallocated, _\*bytes_ is set to `NULL`, [`MemoryError`](https://docs.python.org/3/builtins/exceptions.html#MemoryError "MemoryError")
 is set, and `-1` is returned.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Use the [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 API instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_Repr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bytes, int smartquotes)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Repr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Get the string representation of _bytes_. This function is currently used to implement `bytes.__repr__()` in Python.

This function does not do type checking; it is undefined behavior to pass _bytes_ as a non-bytes object or `NULL`.

If _smartquotes_ is true, the representation will use a double-quoted string instead of single-quoted string when single-quotes are present in _bytes_. For example, the byte string `'Python'` would be represented as `b"'Python'"` when _smartquotes_ is true, or `b'\'Python\''` when it is false.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object containing the representation. On failure, this returns `NULL` with an exception set.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytes\_DecodeEscape(const char \*s, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len, const char \*errors, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 unicode, const char \*recode\_encoding)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_DecodeEscape "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Unescape a backslash-escaped string _s_. _s_ must not be `NULL`. _len_ must be the size of _s_.

_errors_ must be one of `"strict"`, `"replace"`, or `"ignore"`. If _errors_ is `NULL`, then `"strict"` is used by default.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a Python [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object containing the unescaped string. On failure, this function returns `NULL` with an exception set.

Changed in version 3.9: _unicode_ and _recode\_encoding_ are now unused.

PyBytesWriter[¶](https://docs.python.org/3/c-api/bytes.html#pybyteswriter "Link to this heading")

==================================================================================================

The [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 API can be used to create a Python [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

Added in version 3.15.

type PyBytesWriter[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "Link to this definition")
  

A bytes writer instance.

The API is **not thread safe**. To share a writer with multiple threads, a critical section or a lock is needed.

The instance must be destroyed by [`PyBytesWriter_Finish()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Finish "PyBytesWriter_Finish")
 on success, or [`PyBytesWriter_Discard()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Discard "PyBytesWriter_Discard")
 on error.

Create, Finish, Discard[¶](https://docs.python.org/3/c-api/bytes.html#create-finish-discard "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

[PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*PyBytesWriter\_Create([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Create "Link to this definition")
  

Create a [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 to write _size_ bytes.

If _size_ is greater than zero, allocate _size_ bytes, and set the writer size to _size_. The caller is responsible to write _size_ bytes using [`PyBytesWriter_GetData()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetData "PyBytesWriter_GetData")
. This function does not overallocate.

On error, set an exception and return `NULL`.

_size_ must be positive or zero.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytesWriter\_Finish([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Finish "Link to this definition")
  

Finish a [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 created by [`PyBytesWriter_Create()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Create "PyBytesWriter_Create")
.

On success, return a Python [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. On error, set an exception and return `NULL`.

The writer instance is invalid after the call in any case. No API can be called on the writer after [`PyBytesWriter_Finish()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Finish "PyBytesWriter_Finish")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytesWriter\_FinishWithSize([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_FinishWithSize "Link to this definition")
  

Similar to [`PyBytesWriter_Finish()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Finish "PyBytesWriter_Finish")
, but resize the writer to _size_ bytes before creating the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBytesWriter\_FinishWithPointer([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, void \*buf)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_FinishWithPointer "Link to this definition")
  

Similar to [`PyBytesWriter_Finish()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Finish "PyBytesWriter_Finish")
, but resize the writer using _buf_ pointer before creating the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

Set an exception and return `NULL` if _buf_ pointer is outside the internal buffer bounds.

Function pseudo-code:

Py\_ssize\_t size \= (char\*)buf \- (char\*)PyBytesWriter\_GetData(writer);
return PyBytesWriter\_FinishWithSize(writer, size);

void PyBytesWriter\_Discard([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Discard "Link to this definition")
  

Discard a [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 created by [`PyBytesWriter_Create()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Create "PyBytesWriter_Create")
.

Do nothing if _writer_ is `NULL`.

The writer instance is invalid after the call. No API can be called on the writer after [`PyBytesWriter_Discard()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Discard "PyBytesWriter_Discard")
.

High-level API[¶](https://docs.python.org/3/c-api/bytes.html#high-level-api "Link to this heading")

----------------------------------------------------------------------------------------------------

int PyBytesWriter\_WriteBytes([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, const void \*bytes, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_WriteBytes "Link to this definition")
  

Grow the _writer_ internal buffer by _size_ bytes, write _size_ bytes of _bytes_ at the _writer_ end, and add _size_ to the _writer_ size.

If _size_ is equal to `-1`, call `strlen(bytes)` to get the string length.

On success, return `0`. On error, set an exception and return `-1`.

int PyBytesWriter\_Format([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, const char \*format, ...)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Format "Link to this definition")
  

Similar to [`PyBytes_FromFormat()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromFormat "PyBytes_FromFormat")
, but write the output directly at the writer end. Grow the writer internal buffer on demand. Then add the written size to the writer size.

On success, return `0`. On error, set an exception and return `-1`.

Getters[¶](https://docs.python.org/3/c-api/bytes.html#getters "Link to this heading")

--------------------------------------------------------------------------------------

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyBytesWriter\_GetSize([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetSize "Link to this definition")
  

Get the writer size.

The function does not invalidate pointers returned by [`PyBytesWriter_GetData()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetData "PyBytesWriter_GetData")
.

The function cannot fail.

void \*PyBytesWriter\_GetData([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetData "Link to this definition")
  

Get the writer data: start of the internal buffer.

The pointer remains valid until a [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 function other than [`PyBytesWriter_GetData()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetData "PyBytesWriter_GetData")
 or [`PyBytesWriter_GetSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetSize "PyBytesWriter_GetSize")
 is called on _writer_.

The function cannot fail.

Low-level API[¶](https://docs.python.org/3/c-api/bytes.html#low-level-api "Link to this heading")

--------------------------------------------------------------------------------------------------

int PyBytesWriter\_Resize([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Resize "Link to this definition")
  

Resize the writer to _size_ bytes. It can be used to enlarge or to shrink the writer. This function typically overallocates to achieve amortized performance when resizing multiple times.

Newly allocated bytes are left uninitialized.

On success, return `0`. On error, set an exception and return `-1`.

_size_ must be positive or zero.

int PyBytesWriter\_Grow([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 grow)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Grow "Link to this definition")
  

Resize the writer by adding _grow_ bytes to the current writer size. This function typically overallocates to achieve amortized performance when resizing multiple times.

Newly allocated bytes are left uninitialized.

On success, return `0`. On error, set an exception and return `-1`.

_grow_ can be negative to shrink the writer.

void \*PyBytesWriter\_GrowAndUpdatePointer([PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")
 \*writer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, void \*buf)[¶](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GrowAndUpdatePointer "Link to this definition")
  

Similar to [`PyBytesWriter_Grow()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Grow "PyBytesWriter_Grow")
, but update also the _buf_ pointer.

The _buf_ pointer is moved if the internal buffer is moved in memory. The _buf_ relative position within the internal buffer is left unchanged.

On error, set an exception and return `NULL`.

_buf_ must not be `NULL`.

Function pseudo-code:

Py\_ssize\_t pos \= (char\*)buf \- (char\*)PyBytesWriter\_GetData(writer);
if (PyBytesWriter\_Grow(writer, size) < 0) {
    return NULL;
}
return (char\*)PyBytesWriter\_GetData(writer) + pos;

Example creating the string `b'abc'`[¶](https://docs.python.org/3/c-api/bytes.html#example-creating-the-string-b-abc "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Example creating the bytes string `b"abc"`, with a fixed size of 3 bytes:

PyObject\* create\_abc(void)
{
    PyBytesWriter \*writer \= PyBytesWriter\_Create(3);
    if (writer \== NULL) {
        return NULL;
    }

    char \*str \= PyBytesWriter\_GetData(writer);
    memcpy(str, "abc", 3);
    return PyBytesWriter\_Finish(writer);
}

Variant using a pointer to compute the final size:

PyObject\* create\_abc\_ptr(void)
{
    PyBytesWriter \*writer \= PyBytesWriter\_Create(3);
    if (writer \== NULL) {
        return NULL;
    }

    char \*str \= PyBytesWriter\_GetData(writer);
    memcpy(str, "abc", 3);
    str += 3;
    return PyBytesWriter\_FinishWithPointer(writer, str);
}

Update `PyBytes_FromStringAndSize()` code[¶](https://docs.python.org/3/c-api/bytes.html#update-pybytes-fromstringandsize-code "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

Example of code using the soft deprecated `PyBytes_FromStringAndSize(NULL, size)` API:

int copy\_bytes(char \*dest, const char \*src, Py\_ssize\_t num\_bytes)
{
    ...
}

PyObject\* create\_string(const char \*start, Py\_ssize\_t num\_bytes)
{
    PyObject \*result \= PyBytes\_FromStringAndSize(NULL, num\_bytes);
    if (result \== NULL) {
        return NULL;
    }
    if (copy\_bytes(PyBytes\_AS\_STRING(result), start, num\_bytes) < 0) {
        Py\_CLEAR(result);
    }
    return result;
}

It can now be updated to:

PyObject\* create\_string(const char \*start, Py\_ssize\_t num\_bytes)
{
    PyBytesWriter \*writer \= PyBytesWriter\_Create(num\_bytes);
    if (writer \== NULL) {
        return NULL;
    }
    if (copy\_bytes(PyBytesWriter\_GetData(writer), start, num\_bytes) < 0) {
        PyBytesWriter\_Discard(writer);
        return NULL;
    }
    return PyBytesWriter\_Finish(writer);
}

Update `_PyBytes_Resize()` code[¶](https://docs.python.org/3/c-api/bytes.html#update-pybytes-resize-code "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Example of code using the soft deprecated `_PyBytes_Resize()` API:

PyObject\* create\_string(Py\_ssize\_t size)
{
    PyObject \*bytes \= PyBytes\_FromStringAndSize(NULL, size);
    if (bytes \== NULL) {
        return NULL;
    }
    char \*str \= PyBytes\_AS\_STRING(bytes);

    // ... write data into str ...

    if (\_PyBytes\_Resize(&bytes, (str \- PyBytes\_AS\_STRING(bytes)))) {
        return NULL;
    }
    return bytes;
}

It can now be updated to:

PyObject\* create\_string(Py\_ssize\_t size)
{
    PyBytesWriter \*writer \= PyBytesWriter\_Create(size);
    if (writer \== NULL) {
        return NULL;
    }
    char \*str \= PyBytesWriter\_GetData(writer);

    // ... write data into str ...

    return PyBytesWriter\_FinishWithPointer(writer, str);
}

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Bytes Objects](https://docs.python.org/3/c-api/bytes.html#)
    
*   [PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#pybyteswriter)
    *   [Create, Finish, Discard](https://docs.python.org/3/c-api/bytes.html#create-finish-discard)
        
    *   [High-level API](https://docs.python.org/3/c-api/bytes.html#high-level-api)
        
    *   [Getters](https://docs.python.org/3/c-api/bytes.html#getters)
        
    *   [Low-level API](https://docs.python.org/3/c-api/bytes.html#low-level-api)
        
    *   [Example creating the string `b'abc'`](https://docs.python.org/3/c-api/bytes.html#example-creating-the-string-b-abc)
        
    *   [Update `PyBytes_FromStringAndSize()` code](https://docs.python.org/3/c-api/bytes.html#update-pybytes-fromstringandsize-code)
        
    *   [Update `_PyBytes_Resize()` code](https://docs.python.org/3/c-api/bytes.html#update-pybytes-resize-code)
        

#### Previous topic

[Complex Number Objects](https://docs.python.org/3/c-api/complex.html "previous chapter")

#### Next topic

[Byte Array Objects](https://docs.python.org/3/c-api/bytearray.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Bytes+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fbytes.html&pagesource=c-api%2Fbytes.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/bytes.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/bytearray.html "Byte Array Objects")
     |
*   [previous](https://docs.python.org/3/c-api/complex.html "Complex Number Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Bytes Objects](https://docs.python.org/3/c-api/bytes.html)
    
*    
    
    |
*   Theme Auto Light Dark |