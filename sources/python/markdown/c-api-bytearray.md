### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/unicode.html "Unicode Objects and Codecs")
     |
*   [previous](https://docs.python.org/3/c-api/bytes.html "Bytes Objects")
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
*   [Byte Array Objects](https://docs.python.org/3/c-api/bytearray.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Byte Array Objects[¶](https://docs.python.org/3/c-api/bytearray.html#byte-array-objects "Link to this heading")

================================================================================================================

type PyByteArrayObject[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArrayObject "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python bytearray object.

**CPython implementation detail:** The internal buffer of [`PyByteArrayObject`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArrayObject "PyByteArrayObject")
 always includes an extra trailing null byte for compatibility with null terminated C strings. This extra byte is not counted in [`PyByteArray_Size()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Size "PyByteArray_Size")
 nor in the _len_ arguments of the functions below.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyByteArray\_Type[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python bytearray type; it is the same object as [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 in the Python layer.

Type check macros[¶](https://docs.python.org/3/c-api/bytearray.html#type-check-macros "Link to this heading")

--------------------------------------------------------------------------------------------------------------

int PyByteArray\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Check "Link to this definition")
  

Return true if the object _o_ is a bytearray object or an instance of a subtype of the bytearray type. This function always succeeds.

int PyByteArray\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_CheckExact "Link to this definition")
  

Return true if the object _o_ is a bytearray object, but not an instance of a subtype of the bytearray type. This function always succeeds.

Direct API functions[¶](https://docs.python.org/3/c-api/bytearray.html#direct-api-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyByteArray\_FromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_FromObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Return a new bytearray object from any object, _o_, that implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
.

On failure, return `NULL` with an exception set.

Note

If the object implements the buffer protocol, then the buffer must not be mutated while the bytearray object is being created.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyByteArray\_FromStringAndSize(const char \*string, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_FromStringAndSize "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Create a new bytearray object from _string_ and its length, _len_.

On failure, return `NULL` with an exception set.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyByteArray\_Concat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*a, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*b)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Concat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Concat bytearrays _a_ and _b_ and return a new bytearray with the result.

On failure, return `NULL` with an exception set.

Note

If the object implements the buffer protocol, then the buffer must not be mutated while the bytearray object is being created.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyByteArray\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bytearray)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return the size of _bytearray_ after checking for a `NULL` pointer.

char \*PyByteArray\_AsString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bytearray)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_AsString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Return the contents of _bytearray_ as a char array after checking for a `NULL` pointer. The returned array always has an extra null byte appended.

Note

It is not thread-safe to mutate the bytearray object while using the returned char array.

int PyByteArray\_Resize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bytearray, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Resize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Resize the internal buffer of _bytearray_ to _len_. Failure is a `-1` return with an exception set.

Changed in version 3.14: A negative _len_ will now result in an exception being set and -1 returned.

Macros[¶](https://docs.python.org/3/c-api/bytearray.html#macros "Link to this heading")

----------------------------------------------------------------------------------------

These macros trade safety for speed and they don’t check pointers.

char \*PyByteArray\_AS\_STRING([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bytearray)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_AS_STRING "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Similar to [`PyByteArray_AsString()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_AsString "PyByteArray_AsString")
, but without error checking.

Note

It is not thread-safe to mutate the bytearray object while using the returned char array.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyByteArray\_GET\_SIZE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bytearray)[¶](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_GET_SIZE "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Similar to [`PyByteArray_Size()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Size "PyByteArray_Size")
, but without error checking.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Byte Array Objects](https://docs.python.org/3/c-api/bytearray.html#)
    *   [Type check macros](https://docs.python.org/3/c-api/bytearray.html#type-check-macros)
        
    *   [Direct API functions](https://docs.python.org/3/c-api/bytearray.html#direct-api-functions)
        
    *   [Macros](https://docs.python.org/3/c-api/bytearray.html#macros)
        

#### Previous topic

[Bytes Objects](https://docs.python.org/3/c-api/bytes.html "previous chapter")

#### Next topic

[Unicode Objects and Codecs](https://docs.python.org/3/c-api/unicode.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Byte+Array+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fbytearray.html&pagesource=c-api%2Fbytearray.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/bytearray.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/unicode.html "Unicode Objects and Codecs")
     |
*   [previous](https://docs.python.org/3/c-api/bytes.html "Bytes Objects")
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
*   [Byte Array Objects](https://docs.python.org/3/c-api/bytearray.html)
    
*    
    
    |
*   Theme Auto Light Dark |