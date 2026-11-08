### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/bool.html "Boolean Objects")
     |
*   [previous](https://docs.python.org/3/c-api/none.html "The None Object")
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
*   [Integer Objects](https://docs.python.org/3/c-api/long.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Integer Objects[¶](https://docs.python.org/3/c-api/long.html#integer-objects "Link to this heading")

=====================================================================================================

All integers are implemented as “long” integer objects of arbitrary size.

On error, most `PyLong_As*` APIs return `(return type)-1` which cannot be distinguished from a number. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

type PyLongObject[¶](https://docs.python.org/3/c-api/long.html#c.PyLongObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (as an opaque struct)._

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python integer object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyLong\_Type[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python integer type. This is the same object as [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 in the Python layer.

int PyLong\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_Check "Link to this definition")
  

Return true if its argument is a [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 or a subtype of `PyLongObject`. This function always succeeds.

int PyLong\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_CheckExact "Link to this definition")
  

Return true if its argument is a [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, but not a subtype of `PyLongObject`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromLong(long v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from _v_, or `NULL` on failure.

**CPython implementation detail:** CPython keeps an array of integer objects for all integers between `-5` and `1024`. When you create an int in that range you actually just get back a reference to the existing object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromUnsignedLong(unsigned long v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedLong "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from a C unsigned long, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromSsize\_t([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromSsize_t "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from a C [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromSize\_t(size\_t v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromSize_t "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from a C `size_t`, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromLongLong(long long v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLongLong "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from a C long long, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromUnsignedLongLong(unsigned long long v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedLongLong "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from a C unsigned long long, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromInt32(int32\_t value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromInt32 "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromInt64(int64\_t value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromInt64 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from a signed C int32\_t or int64\_t, or `NULL` with an exception set on failure.

Added in version 3.14.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromUInt32(uint32\_t value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUInt32 "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromUInt64(uint64\_t value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUInt64 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from an unsigned C uint32\_t or uint64\_t, or `NULL` with an exception set on failure.

Added in version 3.14.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromDouble(double v)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromDouble "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 object from the integer part of _v_, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromString(const char \*str, char \*\*pend, int base)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 based on the string value in _str_, which is interpreted according to the radix in _base_, or `NULL` on failure. If _pend_ is non-`NULL`, _\*pend_ will point to the end of _str_ on success or to the first character that could not be processed on error. If _base_ is `0`, _str_ is interpreted using the [Integer literals](https://docs.python.org/3/reference/lexical_analysis.html#integers)
 definition; in this case, leading zeros in a non-zero decimal number raises a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. If _base_ is not `0`, it must be between `2` and `36`, inclusive. Leading and trailing whitespace and single underscores after a base specifier and between digits are ignored. If there are no digits or _str_ is not NULL-terminated following the digits and trailing whitespace, `ValueError` will be raised.

See also

[`PyLong_AsNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes")
 and [`PyLong_FromNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromNativeBytes "PyLong_FromNativeBytes")
 functions can be used to convert a [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 to/from an array of bytes in base `256`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromUnicodeObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*u, int base)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnicodeObject "Link to this definition")
  

_Return value: New reference._

Convert a sequence of Unicode digits in the string _u_ to a Python integer value.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromVoidPtr(void \*p)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromVoidPtr "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Python integer from the pointer _p_. The pointer value can be retrieved from the resulting value using [`PyLong_AsVoidPtr()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsVoidPtr "PyLong_AsVoidPtr")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromNativeBytes(const void \*buffer, size\_t n\_bytes, int flags)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromNativeBytes "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Create a Python integer from the value contained in the first _n\_bytes_ of _buffer_, interpreted as a two’s-complement signed number.

_flags_ are as for [`PyLong_AsNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes")
. Passing `-1` will select the native endian that CPython was compiled with and assume that the most-significant bit is a sign bit. Passing `Py_ASNATIVEBYTES_UNSIGNED_BUFFER` will produce the same result as calling [`PyLong_FromUnsignedNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedNativeBytes "PyLong_FromUnsignedNativeBytes")
. Other flags are ignored.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_FromUnsignedNativeBytes(const void \*buffer, size\_t n\_bytes, int flags)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedNativeBytes "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Create a Python integer from the value contained in the first _n\_bytes_ of _buffer_, interpreted as an unsigned number.

_flags_ are as for [`PyLong_AsNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes")
. Passing `-1` will select the native endian that CPython was compiled with and assume that the most-significant bit is not a sign bit. Flags other than endian are ignored.

Added in version 3.13.

PyLong\_FromPid(pid)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FromPid "Link to this definition")
  

Macro for creating a Python integer from a process identifier.

This can be defined as an alias to [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")
 or [`PyLong_FromLongLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLongLong "PyLong_FromLongLong")
, depending on the size of the system’s PID type.

Added in version 3.2.

long PyLong\_AsLong([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLong "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C long representation of _obj_. If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _obj_ is out of range for a long.

Returns `-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
.

long PyLong\_AS\_LONG([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AS_LONG "Link to this definition")
  

Exactly equivalent to the preferred `PyLong_AsLong`. In particular, it can fail with [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 or another exception.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14.

int PyLong\_AsInt([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Similar to [`PyLong_AsLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLong "PyLong_AsLong")
, but store the result in a C int instead of a C long.

Added in version 3.13.

long PyLong\_AsLongAndOverflow([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, int \*overflow)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongAndOverflow "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C long representation of _obj_. If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

If the value of _obj_ is greater than `LONG_MAX` or less than `LONG_MIN`, set _\*overflow_ to `1` or `-1`, respectively, and return `-1`; otherwise, set _\*overflow_ to `0`. If any other exception occurs set _\*overflow_ to `0` and return `-1` as usual.

Returns `-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
.

long long PyLong\_AsLongLong([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongLong "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C long long representation of _obj_. If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _obj_ is out of range for a long long.

Returns `-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
.

long long PyLong\_AsLongLongAndOverflow([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, int \*overflow)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongLongAndOverflow "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C long long representation of _obj_. If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

If the value of _obj_ is greater than `LLONG_MAX` or less than `LLONG_MIN`, set _\*overflow_ to `1` or `-1`, respectively, and return `-1`; otherwise, set _\*overflow_ to `0`. If any other exception occurs set _\*overflow_ to `0` and return `-1` as usual.

Returns `-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Added in version 3.2.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyLong\_AsSsize\_t([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsSsize_t "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 representation of _pylong_. _pylong_ must be an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _pylong_ is out of range for a [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
.

Returns `-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

unsigned long PyLong\_AsUnsignedLong([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLong "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C unsigned long representation of _pylong_. _pylong_ must be an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _pylong_ is out of range for a unsigned long.

Returns `(unsigned long)-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

size\_t PyLong\_AsSize\_t([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsSize_t "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C `size_t` representation of _pylong_. _pylong_ must be an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _pylong_ is out of range for a `size_t`.

Returns `(size_t)-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

unsigned long long PyLong\_AsUnsignedLongLong([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLongLong "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C unsigned long long representation of _pylong_. _pylong_ must be an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _pylong_ is out of range for an unsigned long long.

Returns `(unsigned long long)-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Changed in version 3.1: A negative _pylong_ now raises [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
, not [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

unsigned long PyLong\_AsUnsignedLongMask([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLongMask "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C unsigned long representation of _obj_. If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

If the value of _obj_ is out of range for an unsigned long, return the reduction of that value modulo `ULONG_MAX + 1`.

Returns `(unsigned long)-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
.

unsigned long long PyLong\_AsUnsignedLongLongMask([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLongLongMask "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C unsigned long long representation of _obj_. If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

If the value of _obj_ is out of range for an unsigned long long, return the reduction of that value modulo `ULLONG_MAX + 1`.

Returns `(unsigned long long)-1` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__")
.

int PyLong\_AsInt32([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, int32\_t \*value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt32 "Link to this definition")
  

int PyLong\_AsInt64([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, int64\_t \*value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt64 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Set _\*value_ to a signed C int32\_t or int64\_t representation of _obj_.

If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

If the _obj_ value is out of range, raise an [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
.

Set _\*value_ and return `0` on success. Set an exception and return `-1` on error.

_value_ must not be `NULL`.

Added in version 3.14.

int PyLong\_AsUInt32([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, uint32\_t \*value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUInt32 "Link to this definition")
  

int PyLong\_AsUInt64([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, uint64\_t \*value)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUInt64 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Set _\*value_ to an unsigned C uint32\_t or uint64\_t representation of _obj_.

If _obj_ is not an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
, first call its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method (if present) to convert it to a `PyLongObject`.

*   If _obj_ is negative, raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
    .
    
*   If the _obj_ value is out of range, raise an [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
    .
    

Set _\*value_ and return `0` on success. Set an exception and return `-1` on error.

_value_ must not be `NULL`.

Added in version 3.14.

double PyLong\_AsDouble([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsDouble "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a C double representation of _pylong_. _pylong_ must be an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
.

Raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if the value of _pylong_ is out of range for a double.

Returns `-1.0` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

void \*PyLong\_AsVoidPtr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsVoidPtr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Convert a Python integer _pylong_ to a C void pointer. If _pylong_ cannot be converted, an [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 will be raised. This is only assured to produce a usable void pointer for values created with [`PyLong_FromVoidPtr()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromVoidPtr "PyLong_FromVoidPtr")
.

Returns `NULL` on error. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to disambiguate.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyLong\_AsNativeBytes([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pylong, void \*buffer, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 n\_bytes, int flags)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Copy the Python integer value _pylong_ to a native _buffer_ of size _n\_bytes_. The _flags_ can be set to `-1` to behave similarly to a C cast, or to values documented below to control the behavior.

Returns `-1` with an exception raised on error. This may happen if _pylong_ cannot be interpreted as an integer, or if _pylong_ was negative and the `Py_ASNATIVEBYTES_REJECT_NEGATIVE` flag was set.

Otherwise, returns the number of bytes required to store the value. If this is equal to or less than _n\_bytes_, the entire value was copied. All _n\_bytes_ of the buffer are written: remaining bytes filled by copies of the sign bit.

If the returned value is greater than _n\_bytes_, the value was truncated: as many of the lowest bits of the value as could fit are written, and the higher bits are ignored. This matches the typical behavior of a C-style downcast.

Note

Overflow is not considered an error. If the returned value is larger than _n\_bytes_, most significant bits were discarded.

`0` will never be returned.

Values are always copied as two’s-complement.

Usage example:

int32\_t value;
Py\_ssize\_t bytes \= PyLong\_AsNativeBytes(pylong, &value, sizeof(value), \-1);
if (bytes < 0) {
    // Failed. A Python exception was set with the reason.
    return NULL;
}
else if (bytes <= (Py\_ssize\_t)sizeof(value)) {
    // Success!
}
else {
    // Overflow occurred, but 'value' contains the truncated
    // lowest bits of pylong.
}

Passing zero to _n\_bytes_ will return the size of a buffer that would be large enough to hold the value. This may be larger than technically necessary, but not unreasonably so. If _n\_bytes=0_, _buffer_ may be `NULL`.

Note

Passing _n\_bytes=0_ to this function is not an accurate way to determine the bit length of the value.

To get at the entire Python value of an unknown size, the function can be called twice: first to determine the buffer size, then to fill it:

// Ask how much space we need.
Py\_ssize\_t expected \= PyLong\_AsNativeBytes(pylong, NULL, 0, \-1);
if (expected < 0) {
    // Failed. A Python exception was set with the reason.
    return NULL;
}
assert(expected != 0);  // Impossible per the API definition.
uint8\_t \*bignum \= malloc(expected);
if (!bignum) {
    PyErr\_SetString(PyExc\_MemoryError, "bignum malloc failed.");
    return NULL;
}
// Safely get the entire value.
Py\_ssize\_t bytes \= PyLong\_AsNativeBytes(pylong, bignum, expected, \-1);
if (bytes < 0) {  // Exception has been set.
    free(bignum);
    return NULL;
}
else if (bytes \> expected) {  // This should not be possible.
    PyErr\_SetString(PyExc\_RuntimeError,
        "Unexpected bignum truncation after a size check.");
    free(bignum);
    return NULL;
}
// The expected success given the above pre-check.
// ... use bignum ...
free(bignum);

_flags_ is either `-1` (`Py_ASNATIVEBYTES_DEFAULTS`) to select defaults that behave most like a C cast, or a combination of the other flags in the table below. Note that `-1` cannot be combined with other flags.

Currently, `-1` corresponds to `Py_ASNATIVEBYTES_NATIVE_ENDIAN | Py_ASNATIVEBYTES_UNSIGNED_BUFFER`.

These values are available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14.

| Flag | Value |
| --- | --- |
| Py\_ASNATIVEBYTES\_DEFAULTS[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_DEFAULTS "Link to this definition") | `-1` |
| Py\_ASNATIVEBYTES\_BIG\_ENDIAN[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_BIG_ENDIAN "Link to this definition") | `0` |
| Py\_ASNATIVEBYTES\_LITTLE\_ENDIAN[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_LITTLE_ENDIAN "Link to this definition") | `1` |
| Py\_ASNATIVEBYTES\_NATIVE\_ENDIAN[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_NATIVE_ENDIAN "Link to this definition") | `3` |
| Py\_ASNATIVEBYTES\_UNSIGNED\_BUFFER[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_UNSIGNED_BUFFER "Link to this definition") | `4` |
| Py\_ASNATIVEBYTES\_REJECT\_NEGATIVE[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_REJECT_NEGATIVE "Link to this definition") | `8` |
| Py\_ASNATIVEBYTES\_ALLOW\_INDEX[¶](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_ALLOW_INDEX "Link to this definition") | `16` |

Specifying `Py_ASNATIVEBYTES_NATIVE_ENDIAN` will override any other endian flags. Passing `2` is reserved.

By default, sufficient buffer will be requested to include a sign bit. For example, when converting 128 with _n\_bytes=1_, the function will return 2 (or more) in order to store a zero sign bit.

If `Py_ASNATIVEBYTES_UNSIGNED_BUFFER` is specified, a zero sign bit will be omitted from size calculations. This allows, for example, 128 to fit in a single-byte buffer. If the destination buffer is later treated as signed, a positive input value may become negative. Note that the flag does not affect handling of negative values: for those, space for a sign bit is always requested.

Specifying `Py_ASNATIVEBYTES_REJECT_NEGATIVE` causes an exception to be set if _pylong_ is negative. Without this flag, negative values will be copied provided there is enough space for at least one sign bit, regardless of whether `Py_ASNATIVEBYTES_UNSIGNED_BUFFER` was specified.

If `Py_ASNATIVEBYTES_ALLOW_INDEX` is specified and a non-integer value is passed, its [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 method will be called first. This may result in Python code executing and other threads being allowed to run, which could cause changes to other objects or values in use. When _flags_ is `-1`, this option is not set, and non-integer values will raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

Note

With the default _flags_ (`-1`, or _UNSIGNED\_BUFFER_ without _REJECT\_NEGATIVE_), multiple Python integers can map to a single value without overflow. For example, both `255` and `-1` fit a single-byte buffer and set all its bits. This matches typical C cast behavior.

Added in version 3.13.

PyLong\_AsPid(pid)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_AsPid "Link to this definition")
  

Macro for converting a Python integer into a process identifier.

This can be defined as an alias to [`PyLong_AsLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLong "PyLong_AsLong")
, [`PyLong_AsLongLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongLong "PyLong_AsLongLong")
, or [`PyLong_AsInt()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt "PyLong_AsInt")
, depending on the size of the system’s PID type.

Added in version 3.2.

int PyLong\_GetSign([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, int \*sign)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_GetSign "Link to this definition")
  

Get the sign of the integer object _obj_.

On success, set _\*sign_ to the integer sign (0, -1 or +1 for zero, negative or positive integer, respectively) and return 0.

On failure, return -1 with an exception set. This function always succeeds if _obj_ is a [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 or its subtype.

Added in version 3.14.

int PyLong\_IsPositive([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_IsPositive "Link to this definition")
  

Check if the integer object _obj_ is positive (`obj > 0`).

If _obj_ is an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 or its subtype, return `1` when it’s positive and `0` otherwise. Else set an exception and return `-1`.

Added in version 3.14.

int PyLong\_IsNegative([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_IsNegative "Link to this definition")
  

Check if the integer object _obj_ is negative (`obj < 0`).

If _obj_ is an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 or its subtype, return `1` when it’s negative and `0` otherwise. Else set an exception and return `-1`.

Added in version 3.14.

int PyLong\_IsZero([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_IsZero "Link to this definition")
  

Check if the integer object _obj_ is zero.

If _obj_ is an instance of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 or its subtype, return `1` when it’s zero and `0` otherwise. Else set an exception and return `-1`.

Added in version 3.14.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLong\_GetInfo(void)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_GetInfo "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

On success, return a read only [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
, that holds information about Python’s internal representation of integers. See [`sys.int_info`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info")
 for description of individual fields.

On failure, return `NULL` with an exception set.

Added in version 3.1.

int PyUnstable\_Long\_IsCompact(const [PyLongObject](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 \*op)[¶](https://docs.python.org/3/c-api/long.html#c.PyUnstable_Long_IsCompact "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Return 1 if _op_ is compact, 0 otherwise.

This function makes it possible for performance-critical code to implement a “fast path” for small integers. For compact values use [`PyUnstable_Long_CompactValue()`](https://docs.python.org/3/c-api/long.html#c.PyUnstable_Long_CompactValue "PyUnstable_Long_CompactValue")
; for others fall back to a [`PyLong_As*`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsSize_t "PyLong_AsSize_t")
 function or [`PyLong_AsNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes")
.

The speedup is expected to be negligible for most users.

Exactly what values are considered compact is an implementation detail and is subject to change.

Added in version 3.12.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnstable\_Long\_CompactValue(const [PyLongObject](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 \*op)[¶](https://docs.python.org/3/c-api/long.html#c.PyUnstable_Long_CompactValue "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

If _op_ is compact, as determined by [`PyUnstable_Long_IsCompact()`](https://docs.python.org/3/c-api/long.html#c.PyUnstable_Long_IsCompact "PyUnstable_Long_IsCompact")
, return its value.

Otherwise, the return value is undefined.

Added in version 3.12.

Build configuration[¶](https://docs.python.org/3/c-api/long.html#build-configuration "Link to this heading")

-------------------------------------------------------------------------------------------------------------

PYLONG\_BITS\_IN\_DIGIT[¶](https://docs.python.org/3/c-api/long.html#c.PYLONG_BITS_IN_DIGIT "Link to this definition")
  

The number of bits in each digit of CPython’s native representation of integers. The value can currently be either `30` (the default) or `15`, selected with [`--enable-big-digits`](https://docs.python.org/3/using/configure.html#cmdoption-enable-big-digits)
 when building Python.

To access the native representation of integers, use [`PyLong_GetNativeLayout()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "PyLong_GetNativeLayout")
 and its [`bits_per_digit`](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.bits_per_digit "PyLongLayout.bits_per_digit")
 member instead.

Export API[¶](https://docs.python.org/3/c-api/long.html#export-api "Link to this heading")

-------------------------------------------------------------------------------------------

Added in version 3.14.

type PyLongLayout[¶](https://docs.python.org/3/c-api/long.html#c.PyLongLayout "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.15._

Layout of an array of “digits” (“limbs” in the GMP terminology), used to represent absolute value for arbitrary precision integers.

Use [`PyLong_GetNativeLayout()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "PyLong_GetNativeLayout")
 to get the native layout of Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 objects, used internally for integers with “big enough” absolute value.

See also [`sys.int_info`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info")
 which exposes similar information in Python.

uint8\_t bits\_per\_digit[¶](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.bits_per_digit "Link to this definition")
  

Bits per digit. For example, a 15 bit digit means that bits 0-14 contain meaningful information.

uint8\_t digit\_size[¶](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.digit_size "Link to this definition")
  

Digit size in bytes. For example, a 15 bit digit will require at least 2 bytes.

int8\_t digits\_order[¶](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.digits_order "Link to this definition")
  

Digits order:

*   `1` for most significant digit first
    
*   `-1` for least significant digit first
    

int8\_t digit\_endianness[¶](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.digit_endianness "Link to this definition")
  

Digit endianness:

*   `1` for most significant byte first (big endian)
    
*   `-1` for least significant byte first (little endian)
    

const [PyLongLayout](https://docs.python.org/3/c-api/long.html#c.PyLongLayout "PyLongLayout")
 \*PyLong\_GetNativeLayout(void)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Get the native layout of Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 objects.

See the [`PyLongLayout`](https://docs.python.org/3/c-api/long.html#c.PyLongLayout "PyLongLayout")
 structure.

The function must not be called before Python initialization nor after Python finalization. The returned layout is valid until Python is finalized. The layout is the same for all Python sub-interpreters in a process, and so it can be cached.

type PyLongExport[¶](https://docs.python.org/3/c-api/long.html#c.PyLongExport "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.15._

Export of a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object.

There are two cases:

*   If [`digits`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.digits "digits")
     is `NULL`, only use the [`value`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.value "value")
     member.
    
*   If [`digits`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.digits "digits")
     is not `NULL`, use [`negative`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.negative "negative")
    , [`ndigits`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.ndigits "ndigits")
     and `digits` members.
    

int64\_t value[¶](https://docs.python.org/3/c-api/long.html#c.PyLongExport.value "Link to this definition")
  

The native integer value of the exported [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object. Only valid if [`digits`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.digits "digits")
 is `NULL`.

uint8\_t negative[¶](https://docs.python.org/3/c-api/long.html#c.PyLongExport.negative "Link to this definition")
  

`1` if the number is negative, `0` otherwise. Only valid if [`digits`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.digits "digits")
 is not `NULL`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 ndigits[¶](https://docs.python.org/3/c-api/long.html#c.PyLongExport.ndigits "Link to this definition")
  

Number of digits in [`digits`](https://docs.python.org/3/c-api/long.html#c.PyLongExport.digits "digits")
 array. Only valid if `digits` is not `NULL`.

const void \*digits[¶](https://docs.python.org/3/c-api/long.html#c.PyLongExport.digits "Link to this definition")
  

Read-only array of unsigned digits. Can be `NULL`.

int PyLong\_Export([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyLongExport](https://docs.python.org/3/c-api/long.html#c.PyLongExport "PyLongExport")
 \*export\_long)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_Export "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Export a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object.

_export\_long_ must point to a [`PyLongExport`](https://docs.python.org/3/c-api/long.html#c.PyLongExport "PyLongExport")
 structure allocated by the caller. It must not be `NULL`.

On success, fill in _\*export\_long_ and return `0`. On error, set an exception and return `-1`.

[`PyLong_FreeExport()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FreeExport "PyLong_FreeExport")
 must be called when the export is no longer needed.

> **CPython implementation detail:** This function always succeeds if _obj_ is a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
>  object or a subclass.

void PyLong\_FreeExport([PyLongExport](https://docs.python.org/3/c-api/long.html#c.PyLongExport "PyLongExport")
 \*export\_long)[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_FreeExport "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Release the export _export\_long_ created by [`PyLong_Export()`](https://docs.python.org/3/c-api/long.html#c.PyLong_Export "PyLong_Export")
.

**CPython implementation detail:** Calling [`PyLong_FreeExport()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FreeExport "PyLong_FreeExport")
 is optional if _export\_long->digits_ is `NULL`.

PyLongWriter API[¶](https://docs.python.org/3/c-api/long.html#pylongwriter-api "Link to this heading")

-------------------------------------------------------------------------------------------------------

The [`PyLongWriter`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 API can be used to import an integer.

Added in version 3.14.

type PyLongWriter[¶](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (as an opaque struct) since version 3.15._

A Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 writer instance.

The instance must be destroyed by [`PyLongWriter_Finish()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Finish "PyLongWriter_Finish")
 or [`PyLongWriter_Discard()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Discard "PyLongWriter_Discard")
.

[PyLongWriter](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 \*PyLongWriter\_Create(int negative, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 ndigits, void \*\*digits)[¶](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Create a [`PyLongWriter`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
.

On success, allocate _\*digits_ and return a writer. On error, set an exception and return `NULL`.

_negative_ is `1` if the number is negative, or `0` otherwise.

_ndigits_ is the number of digits in the _digits_ array. It must be greater than 0.

_digits_ must not be NULL.

After a successful call to this function, the caller should fill in the array of digits _digits_ and then call [`PyLongWriter_Finish()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Finish "PyLongWriter_Finish")
 to get a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. The layout of _digits_ is described by [`PyLong_GetNativeLayout()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "PyLong_GetNativeLayout")
.

Digits must be in the range \[`0`; `(1 << bits_per_digit) - 1`\] (where the [`bits_per_digit`](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.bits_per_digit "PyLongLayout.bits_per_digit")
 is the number of bits per digit). Any unused most significant digits must be set to `0`.

Alternately, call [`PyLongWriter_Discard()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Discard "PyLongWriter_Discard")
 to destroy the writer instance without creating an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyLongWriter\_Finish([PyLongWriter](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Finish "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Finish a [`PyLongWriter`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 created by [`PyLongWriter_Create()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "PyLongWriter_Create")
.

On success, return a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object. On error, set an exception and return `NULL`.

The function takes care of normalizing the digits and converts the object to a compact integer if needed.

The writer instance and the _digits_ array are invalid after the call.

void PyLongWriter\_Discard([PyLongWriter](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 \*writer)[¶](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Discard "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Discard a [`PyLongWriter`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 created by [`PyLongWriter_Create()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "PyLongWriter_Create")
.

If _writer_ is `NULL`, no operation is performed.

The writer instance and the _digits_ array are invalid after the call.

Deprecated API[¶](https://docs.python.org/3/c-api/long.html#deprecated-api "Link to this heading")

---------------------------------------------------------------------------------------------------

These macros are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
. They describe parameters of the internal representation of [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
 instances.

Use [`PyLong_GetNativeLayout()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "PyLong_GetNativeLayout")
 instead, along with [`PyLong_Export()`](https://docs.python.org/3/c-api/long.html#c.PyLong_Export "PyLong_Export")
 to read integer data or [`PyLongWriter`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
 to write it. These currently use the same layout, but are designed to continue working correctly even if CPython’s internal integer representation changes.

PyLong\_SHIFT[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_SHIFT "Link to this definition")
  

This is equivalent to [`bits_per_digit`](https://docs.python.org/3/c-api/long.html#c.PyLongLayout.bits_per_digit "PyLongLayout.bits_per_digit")
 in the output of [`PyLong_GetNativeLayout()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "PyLong_GetNativeLayout")
.

PyLong\_BASE[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_BASE "Link to this definition")
  

This is currently equivalent to 1 << [PyLong\_SHIFT](https://docs.python.org/3/c-api/long.html#c.PyLong_SHIFT "PyLong_SHIFT")
.

PyLong\_MASK[¶](https://docs.python.org/3/c-api/long.html#c.PyLong_MASK "Link to this definition")
  

This is currently equivalent to (1 << [PyLong\_SHIFT](https://docs.python.org/3/c-api/long.html#c.PyLong_SHIFT "PyLong_SHIFT")
) \- 1

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Integer Objects](https://docs.python.org/3/c-api/long.html#)
    *   [Build configuration](https://docs.python.org/3/c-api/long.html#build-configuration)
        
    *   [Export API](https://docs.python.org/3/c-api/long.html#export-api)
        
    *   [PyLongWriter API](https://docs.python.org/3/c-api/long.html#pylongwriter-api)
        
    *   [Deprecated API](https://docs.python.org/3/c-api/long.html#deprecated-api)
        

#### Previous topic

[The `None` Object](https://docs.python.org/3/c-api/none.html "previous chapter")

#### Next topic

[Boolean Objects](https://docs.python.org/3/c-api/bool.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Integer+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Flong.html&pagesource=c-api%2Flong.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/long.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/bool.html "Boolean Objects")
     |
*   [previous](https://docs.python.org/3/c-api/none.html "The None Object")
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
*   [Integer Objects](https://docs.python.org/3/c-api/long.html)
    
*    
    
    |
*   Theme Auto Light Dark |