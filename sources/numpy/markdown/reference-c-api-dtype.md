[Skip to main content](https://numpy.org/doc/stable/reference/c-api/dtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/dtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/dtype.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/dtype.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/dtype.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/dtype.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/dtype.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/dtype.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/dtype.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/dtype.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/dtype.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/dtype.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/dtype.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/dtype.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/dtype.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/dtype.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/dtype.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/dtype.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/dtype.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/dtype.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/dtype.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/dtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Data type API[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#data-type-api "Link to this heading")

===============================================================================================================

The standard array can have 25 different data types (and has some support for adding your own types). These data types all have an enumerated type, an enumerated type-character, and a corresponding array scalar Python type object (placed in a hierarchy). There are also standard C typedefs to make it easier to manipulate elements of the given data type. For the numeric types, there are also bit-width equivalent C typedefs and named typenumbers that make it easier to select the precision desired.

Warning

The names for the types in c code follows c naming conventions more closely. The Python names for these types follow Python conventions. Thus, [`NPY_FLOAT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT "NPY_FLOAT")
 picks up a 32-bit float in C, but [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 in Python corresponds to a 64-bit double. The bit-width names can be used in both Python and C for clarity.

Enumerated types[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#enumerated-types "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

enum NPY\_TYPES[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES "Link to this definition")
  

There is a list of enumerated types defined providing the basic 25 data types plus some useful generic names. Whenever the code requires a type number, one of these enumerated types is requested. The types are all called `NPY_{NAME}`:

enumerator NPY\_BOOL[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_BOOL "Link to this definition")
  

The enumeration value for the boolean type, stored as one byte. It may only be set to the values 0 and 1.

enumerator NPY\_BYTE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_BYTE "Link to this definition")
  

enumerator NPY\_INT8[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT8 "Link to this definition")
  

The enumeration value for an 8-bit/1-byte signed integer.

enumerator NPY\_SHORT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_SHORT "Link to this definition")
  

enumerator NPY\_INT16[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT16 "Link to this definition")
  

The enumeration value for a 16-bit/2-byte signed integer.

enumerator NPY\_INT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT "Link to this definition")
  

enumerator NPY\_INT32[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT32 "Link to this definition")
  

The enumeration value for a 32-bit/4-byte signed integer.

enumerator NPY\_LONG[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONG "Link to this definition")
  

Equivalent to either NPY\_INT or NPY\_LONGLONG, depending on the platform.

enumerator NPY\_LONGLONG[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONGLONG "Link to this definition")
  

enumerator NPY\_INT64[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT64 "Link to this definition")
  

The enumeration value for a 64-bit/8-byte signed integer.

enumerator NPY\_UBYTE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UBYTE "Link to this definition")
  

enumerator NPY\_UINT8[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT8 "Link to this definition")
  

The enumeration value for an 8-bit/1-byte unsigned integer.

enumerator NPY\_USHORT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_USHORT "Link to this definition")
  

enumerator NPY\_UINT16[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT16 "Link to this definition")
  

The enumeration value for a 16-bit/2-byte unsigned integer.

enumerator NPY\_UINT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT "Link to this definition")
  

enumerator NPY\_UINT32[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT32 "Link to this definition")
  

The enumeration value for a 32-bit/4-byte unsigned integer.

enumerator NPY\_ULONG[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_ULONG "Link to this definition")
  

Equivalent to either NPY\_UINT or NPY\_ULONGLONG, depending on the platform.

enumerator NPY\_ULONGLONG[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_ULONGLONG "Link to this definition")
  

enumerator NPY\_UINT64[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT64 "Link to this definition")
  

The enumeration value for a 64-bit/8-byte unsigned integer.

enumerator NPY\_HALF[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_HALF "Link to this definition")
  

enumerator NPY\_FLOAT16[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT16 "Link to this definition")
  

The enumeration value for a 16-bit/2-byte IEEE 754-2008 compatible floating point type.

enumerator NPY\_FLOAT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT "Link to this definition")
  

enumerator NPY\_FLOAT32[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT32 "Link to this definition")
  

The enumeration value for a 32-bit/4-byte IEEE 754 compatible floating point type.

enumerator NPY\_DOUBLE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_DOUBLE "Link to this definition")
  

enumerator NPY\_FLOAT64[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT64 "Link to this definition")
  

The enumeration value for a 64-bit/8-byte IEEE 754 compatible floating point type.

enumerator NPY\_LONGDOUBLE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONGDOUBLE "Link to this definition")
  

The enumeration value for a platform-specific floating point type which is at least as large as NPY\_DOUBLE, but larger on many platforms.

enumerator NPY\_CFLOAT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_CFLOAT "Link to this definition")
  

enumerator NPY\_COMPLEX64[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_COMPLEX64 "Link to this definition")
  

The enumeration value for a 64-bit/8-byte complex type made up of two NPY\_FLOAT values.

enumerator NPY\_CDOUBLE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_CDOUBLE "Link to this definition")
  

enumerator NPY\_COMPLEX128[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_COMPLEX128 "Link to this definition")
  

The enumeration value for a 128-bit/16-byte complex type made up of two NPY\_DOUBLE values.

enumerator NPY\_CLONGDOUBLE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_CLONGDOUBLE "Link to this definition")
  

The enumeration value for a platform-specific complex floating point type which is made up of two NPY\_LONGDOUBLE values.

enumerator NPY\_DATETIME[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_DATETIME "Link to this definition")
  

The enumeration value for a data type which holds dates or datetimes with a precision based on selectable date or time units.

enumerator NPY\_TIMEDELTA[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_TIMEDELTA "Link to this definition")
  

The enumeration value for a data type which holds lengths of times in integers of selectable date or time units.

enumerator NPY\_STRING[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_STRING "Link to this definition")
  

The enumeration value for null-padded byte strings of a selectable size. The strings have a fixed maximum size within a given array.

enumerator NPY\_UNICODE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UNICODE "Link to this definition")
  

The enumeration value for UCS4 strings of a selectable size. The strings have a fixed maximum size within a given array.

enumerator NPY\_VSTRING[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_VSTRING "Link to this definition")
  

The enumeration value for UTF-8 variable-width strings. Note that this dtype holds an array of references, with string data stored outside of the array buffer. Use the C API for working with numpy variable-width static strings to access the string data in each array entry.

Note

This DType is new-style and is not included in `NPY_NTYPES_LEGACY`.

enumerator NPY\_OBJECT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "Link to this definition")
  

The enumeration value for references to arbitrary Python objects.

enumerator NPY\_VOID[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_VOID "Link to this definition")
  

Primarily used to hold struct dtypes, but can contain arbitrary binary data.

Some useful aliases of the above types are

enumerator NPY\_INTP[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INTP "Link to this definition")
  

The enumeration value for a signed integer of type `Py_ssize_t` (same as `ssize_t` if defined). This is the type used by all arrays of indices.

Changed in version 2.0: Previously, this was the same as `intptr_t` (same size as a pointer). In practice, this is identical except on very niche platforms. You can use the `'p'` character code for the pointer meaning.

enumerator NPY\_UINTP[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINTP "Link to this definition")
  

The enumeration value for an unsigned integer type that is identical to a `size_t`.

Changed in version 2.0: Previously, this was the same as `uintptr_t` (same size as a pointer). In practice, this is identical except on very niche platforms. You can use the `'P'` character code for the pointer meaning.

enumerator NPY\_MASK[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_MASK "Link to this definition")
  

The enumeration value of the type used for masks, such as with the [`NPY_ITER_ARRAYMASK`](https://numpy.org/doc/stable/reference/c-api/iterator.html#c.NPY_ITER_ARRAYMASK "NPY_ITER_ARRAYMASK")
 iterator flag. This is equivalent to [`NPY_UINT8`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT8 "NPY_UINT8")
.

enumerator NPY\_DEFAULT\_TYPE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_DEFAULT_TYPE "Link to this definition")
  

The default type to use when no dtype is explicitly specified, for example when calling np.zero(shape). This is equivalent to [`NPY_DOUBLE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_DOUBLE "NPY_DOUBLE")
.

Other useful related constants are

NPY\_NTYPES\_LEGACY[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_NTYPES_LEGACY "Link to this definition")
  

The number of built-in NumPy types written using the legacy DType system. New NumPy dtypes will be written using the new DType API and may not function in the same manner as legacy DTypes. Use this macro if you want to handle legacy DTypes using different code paths or if you do not want to update code that uses `NPY_NTYPES_LEGACY` and does not work correctly with new DTypes.

Note

Newly added DTypes such as `NPY_VSTRING` will not be counted in `NPY_NTYPES_LEGACY`.

NPY\_NOTYPE[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_NOTYPE "Link to this definition")
  

A signal value guaranteed not to be a valid type enumeration number.

NPY\_USERDEF[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_USERDEF "Link to this definition")
  

The start of type numbers used for legacy Custom Data types. New-style user DTypes currently are currently _not_ assigned a type-number.

Note

The total number of user dtypes is limited to below `NPY_VSTRING`. Higher numbers are reserved to future new-style DType use.

The various character codes indicating certain types are also part of an enumerated list. References to type characters (should they be needed at all) should always use these enumerations. The form of them is `NPY_{NAME}LTR` where `{NAME}` can be

> **BOOL**, **BYTE**, **UBYTE**, **SHORT**, **USHORT**, **INT**, **UINT**, **LONG**, **ULONG**, **LONGLONG**, **ULONGLONG**, **HALF**, **FLOAT**, **DOUBLE**, **LONGDOUBLE**, **CFLOAT**, **CDOUBLE**, **CLONGDOUBLE**, **DATETIME**, **TIMEDELTA**, **OBJECT**, **STRING**, **UNICODE**, **VSTRING**, **VOID**
> 
> **INTP**, **UINTP**
> 
> **GENBOOL**, **SIGNED**, **UNSIGNED**, **FLOATING**, **COMPLEX**

The latter group of `{NAME}s` corresponds to letters used in the array interface typestring specification.

Defines[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#defines "Link to this heading")

---------------------------------------------------------------------------------------------------

### Max and min values for integers[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#max-and-min-values-for-integers "Link to this heading")

`NPY_MAX_INT{bits}`, `NPY_MAX_UINT{bits}`, `NPY_MIN_INT{bits}`

These are defined for `{bits}` = 8, 16, 32, 64, 128, and 256 and provide the maximum (minimum) value of the corresponding (unsigned) integer type. Note: the actual integer type may not be available on all platforms (i.e. 128-bit and 256-bit integers are rare).

`NPY_MIN_{type}`

This is defined for `{type}` = **BYTE**, **SHORT**, **INT**, **LONG**, **LONGLONG**, **INTP**

`NPY_MAX_{type}`

This is defined for all defined for `{type}` = **BYTE**, **UBYTE**, **SHORT**, **USHORT**, **INT**, **UINT**, **LONG**, **ULONG**, **LONGLONG**, **ULONGLONG**, **INTP**, **UINTP**

### Number of bits in data types[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#number-of-bits-in-data-types "Link to this heading")

All `NPY_SIZEOF_{CTYPE}` constants have corresponding `NPY_BITSOF_{CTYPE}` constants defined. The `NPY_BITSOF_{CTYPE}` constants provide the number of bits in the data type. Specifically, the available `{CTYPE}s` are

> **BOOL**, **CHAR**, **SHORT**, **INT**, **LONG**, **LONGLONG**, **FLOAT**, **DOUBLE**, **LONGDOUBLE**

### Bit-width references to enumerated typenums[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#bit-width-references-to-enumerated-typenums "Link to this heading")

All of the numeric data types (integer, floating point, and complex) have constants that are defined to be a specific enumerated type number. Exactly which enumerated type a bit-width type refers to is platform dependent. In particular, the constants available are `PyArray_{NAME}{BITS}` where `{NAME}` is **INT**, **UINT**, **FLOAT**, **COMPLEX** and `{BITS}` can be 8, 16, 32, 64, 80, 96, 128, 160, 192, 256, and 512. Obviously not all bit-widths are available on all platforms for all the kinds of numeric types. Commonly 8-, 16-, 32-, 64-bit integers; 32-, 64-bit floats; and 64-, 128-bit complex types are available.

### Further integer aliases[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#further-integer-aliases "Link to this heading")

The constants **NPY\_INTP** and **NPY\_UINTP** refer to an `Py_ssize_t` and `size_t`. Although in practice normally true, these types are strictly speaking not pointer sized and the character codes `'p'` and `'P'` can be used for pointer sized integers. (Before NumPy 2, `intp` was pointer size, but this almost never matched the actual use, which is the reason for the name.)

Since NumPy 2, **NPY\_DEFAULT\_INT** is additionally defined. The value of the macro is runtime dependent: Since NumPy 2, it maps to `NPY_INTP` while on earlier versions it maps to `NPY_LONG`.

C-type names[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c-type-names "Link to this heading")

-------------------------------------------------------------------------------------------------------------

There are standard variable types for each of the numeric data types and the bool data type. Some of these are already available in the C-specification. You can create variables in extension code with these types.

### Boolean[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#boolean "Link to this heading")

type npy\_bool[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "Link to this definition")
  

unsigned char; The constants [`NPY_FALSE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FALSE "NPY_FALSE")
 and [`NPY_TRUE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "NPY_TRUE")
 are also defined.

### (Un)Signed Integer[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#un-signed-integer "Link to this heading")

Unsigned versions of the integers can be defined by prepending a ‘u’ to the front of the integer name.

type npy\_byte[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_byte "Link to this definition")
  

char

type npy\_ubyte[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_ubyte "Link to this definition")
  

unsigned char

type npy\_short[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_short "Link to this definition")
  

short

type npy\_ushort[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_ushort "Link to this definition")
  

unsigned short

type npy\_int[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int "Link to this definition")
  

int

type npy\_uint[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint "Link to this definition")
  

unsigned int

type npy\_int16[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int16 "Link to this definition")
  

16-bit integer

type npy\_uint16[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint16 "Link to this definition")
  

16-bit unsigned integer

type npy\_int32[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int32 "Link to this definition")
  

32-bit integer

type npy\_uint32[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint32 "Link to this definition")
  

32-bit unsigned integer

type npy\_int64[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "Link to this definition")
  

64-bit integer

type npy\_uint64[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "Link to this definition")
  

64-bit unsigned integer

type npy\_long[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_long "Link to this definition")
  

long int

type npy\_ulong[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_ulong "Link to this definition")
  

unsigned long int

type npy\_longlong[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_longlong "Link to this definition")
  

long long int

type npy\_ulonglong[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_ulonglong "Link to this definition")
  

unsigned long long int

type npy\_intp[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "Link to this definition")
  

`Py_ssize_t` (a signed integer with the same size as the C `size_t`). This is the correct integer for lengths or indexing. In practice this is normally the size of a pointer, but this is not guaranteed.

Note

Before NumPy 2.0, this was the same as `Py_intptr_t`. While a better match, this did not match actual usage in practice. On the Python side, we still support `np.dtype('p')` to fetch a dtype compatible with storing pointers, while `n` is the correct character for the `ssize_t`.

type npy\_uintp[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uintp "Link to this definition")
  

The C `size_t`/`Py_size_t`.

### (Complex) Floating point[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#complex-floating-point "Link to this heading")

type npy\_half[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "Link to this definition")
  

16-bit float

type npy\_float[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_float "Link to this definition")
  

32-bit float

type npy\_cfloat[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_cfloat "Link to this definition")
  

32-bit complex float

type npy\_double[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_double "Link to this definition")
  

64-bit double

type npy\_cdouble[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_cdouble "Link to this definition")
  

64-bit complex double

type npy\_longdouble[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_longdouble "Link to this definition")
  

long double

type npy\_clongdouble[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_clongdouble "Link to this definition")
  

long complex double

complex types are structures with **.real** and **.imag** members (in that order).

### Bit-width names[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#bit-width-names "Link to this heading")

There are also typedefs for signed integers, unsigned integers, floating point, and complex floating point types of specific bit- widths. The available type names are

> `npy_int{bits}`, `npy_uint{bits}`, `npy_float{bits}`, and `npy_complex{bits}`

where `{bits}` is the number of bits in the type and can be **8**, **16**, **32**, **64**, 128, and 256 for integer types; 16, **32** , **64**, 80, 96, 128, and 256 for floating-point types; and 32, **64**, **128**, 160, 192, and 512 for complex-valued types. Which bit-widths are available is platform dependent. The bolded bit-widths are usually available on all platforms.

### Time and timedelta[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#time-and-timedelta "Link to this heading")

type npy\_datetime[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_datetime "Link to this definition")
  

date or datetime (alias of [`npy_int64`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
)

type npy\_timedelta[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_timedelta "Link to this definition")
  

length of time (alias of [`npy_int64`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
)

Printf formatting[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#printf-formatting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

For help in printing, the following strings are defined as the correct format specifier in printf and related commands.

NPY\_LONGLONG\_FMT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_LONGLONG_FMT "Link to this definition")
  

NPY\_ULONGLONG\_FMT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_ULONGLONG_FMT "Link to this definition")
  

NPY\_INTP\_FMT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_INTP_FMT "Link to this definition")
  

NPY\_UINTP\_FMT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_UINTP_FMT "Link to this definition")
  

NPY\_LONGDOUBLE\_FMT[#](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_LONGDOUBLE_FMT "Link to this definition")
  

On this page