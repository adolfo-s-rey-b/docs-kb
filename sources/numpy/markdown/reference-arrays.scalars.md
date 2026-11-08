[Skip to main content](https://numpy.org/doc/stable/reference/arrays.scalars.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.scalars.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.scalars.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.scalars.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.scalars.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.scalars.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.scalars.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.scalars.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.scalars.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.scalars.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.scalars.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.scalars.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.scalars.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.scalars.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.scalars.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.scalars.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.scalars.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.scalars.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.scalars.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.scalars.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.scalars.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.scalars.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Scalars[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#scalars "Link to this heading")

======================================================================================================

Python defines only one type of a particular data class (there is only one integer type, one floating-point type, etc.). This can be convenient in applications that don’t need to be concerned with all the ways data can be represented in a computer. For scientific computing, however, more control is often needed.

In NumPy, there are 24 new fundamental Python types to describe different types of scalars. These type descriptors are mostly based on the types available in the C language that CPython is written in, with several additional types compatible with Python’s types.

Array scalars have the same attributes and methods as [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
. [\[1\]](https://numpy.org/doc/stable/reference/arrays.scalars.html#id2)
 This allows one to treat items of an array partly on the same footing as arrays, smoothing out rough edges that result when mixing scalar and array operations.

Array scalars live in a hierarchy (see the Figure below) of data types. They can be detected using the hierarchy: For example, `isinstance(val, np.generic)` will return [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 if _val_ is an array scalar object. Alternatively, what kind of array scalar is present can be determined using other members of the data type hierarchy. Thus, for example `isinstance(val, np.complexfloating)` will return [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 if _val_ is a complex valued type, while `isinstance(val, np.flexible)` will return true if _val_ is one of the flexible itemsize array types ([`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
, [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
, [`void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void")
).

![../_images/dtype-hierarchy.png](https://numpy.org/doc/stable/_images/dtype-hierarchy.png)

**Figure:** Hierarchy of type objects representing the array data types. Not shown are the two integer types [`intp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intp "numpy.intp")
 and [`uintp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintp "numpy.uintp")
 which are used for indexing (the same as the default integer since NumPy 2).[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#id4 "Link to this image")

Built-in scalar types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The built-in scalar types are shown below. The C-like names are associated with character codes, which are shown in their descriptions. Use of the character codes, however, is discouraged.

Some of the scalar types are essentially equivalent to fundamental Python types and therefore inherit from them as well as from the generic array scalar type:

| Array scalar type | Related Python type | Inherits? |
| --- | --- | --- |
| [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_") | [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | no  |
| [`double`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.double "numpy.double") | [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | yes |
| [`cdouble`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.cdouble "numpy.cdouble") | [`complex`](https://docs.python.org/3/library/functions.html#complex "(in Python v3.14)") | yes |
| [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_") | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | yes |
| [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_") | [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | yes |
| [`bool_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "numpy.bool_") | [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool") | no  |
| [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64") | [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | no  |
| [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64") | [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") | no  |

The [`bool_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "numpy.bool_")
 data type is very similar to the Python [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 but does not inherit from it because Python’s [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 does not allow itself to be inherited from, and on the C-level the size of the actual bool data is not the same as a Python Boolean scalar.

Warning

The [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 type does **not** inherit from the built-in [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
, because type [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 is not a fixed-width integer type.

Tip

The default data type in NumPy is [`double`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.double "numpy.double")
.

_class_ numpy.generic[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.generic "Link to this definition")

Base class for numpy scalar types.

Class from which most (all?) numpy scalar types are derived. For consistency, exposes the same API as [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, despite many consequent attributes being either “get-only,” or completely irrelevant. This is the class from which it is strongly suggested users should derive custom scalar types.

_class_ numpy.number[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "Link to this definition")

Abstract base class of all numeric scalar types.

### Integer types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#integer-types "Link to this heading")

_class_ numpy.integer[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.integer "Link to this definition")

Abstract base class of all integer scalar types.

Note

The numpy integer types mirror the behavior of C integers, and can therefore be subject to [Overflow errors](https://numpy.org/doc/stable/user/basics.types.html#overflow-errors)
.

#### Signed integer types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#signed-integer-types "Link to this heading")

_class_ numpy.signedinteger[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.signedinteger "Link to this definition")

Abstract base class of all signed integer scalar types.

_class_ numpy.byte[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.byte "Link to this definition")

int8(value=0, /) –

Signed integer type, compatible with C `char`.

Character code:

`'b'`

Canonical name:

[`numpy.byte`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.byte "numpy.byte")

Alias on this platform (Linux x86\_64):

[`numpy.int8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int8 "numpy.int8")
: 8-bit signed integer (`-128` to `127`).

_class_ numpy.short[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.short "Link to this definition")

int16(value=0, /) –

Signed integer type, compatible with C `short`.

Character code:

`'h'`

Canonical name:

[`numpy.short`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.short "numpy.short")

Alias on this platform (Linux x86\_64):

[`numpy.int16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int16 "numpy.int16")
: 16-bit signed integer (`-32_768` to `32_767`).

_class_ numpy.intc[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intc "Link to this definition")

int32(value=0, /) –

Signed integer type, compatible with C `int`.

Character code:

`'i'`

Canonical name:

[`numpy.intc`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intc "numpy.intc")

Alias on this platform (Linux x86\_64):

[`numpy.int32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
: 32-bit signed integer (`-2_147_483_648` to `2_147_483_647`).

_class_ numpy.int\_[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "Link to this definition")

int64(value=0, /) –

Signed integer type, compatible with C `long`.

Character code:

`'l'`

Canonical name:

[`numpy.long`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.long "numpy.long")

Alias on this platform (Linux x86\_64):

[`numpy.int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
: 64-bit signed integer (`-9_223_372_036_854_775_808` to `9_223_372_036_854_775_807`).

Alias on this platform (Linux x86\_64):

[`numpy.intp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intp "numpy.intp")
: Signed integer large enough to fit pointer, compatible with C `intptr_t`.

numpy.long[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.long "Link to this definition")

alias of [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")

_class_ numpy.longlong(_value\=0_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.longlong "Link to this definition")

Signed integer type, compatible with C `long long`.

Character code:

`'q'`

#### Unsigned integer types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#unsigned-integer-types "Link to this heading")

_class_ numpy.unsignedinteger[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.unsignedinteger "Link to this definition")

Abstract base class of all unsigned integer scalar types.

_class_ numpy.ubyte[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ubyte "Link to this definition")

uint8(value=0, /) –

Unsigned integer type, compatible with C `unsigned char`.

Character code:

`'B'`

Canonical name:

[`numpy.ubyte`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ubyte "numpy.ubyte")

Alias on this platform (Linux x86\_64):

[`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
: 8-bit unsigned integer (`0` to `255`).

_class_ numpy.ushort[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ushort "Link to this definition")

uint16(value=0, /) –

Unsigned integer type, compatible with C `unsigned short`.

Character code:

`'H'`

Canonical name:

[`numpy.ushort`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ushort "numpy.ushort")

Alias on this platform (Linux x86\_64):

[`numpy.uint16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint16 "numpy.uint16")
: 16-bit unsigned integer (`0` to `65_535`).

_class_ numpy.uintc[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintc "Link to this definition")

uint32(value=0, /) –

Unsigned integer type, compatible with C `unsigned int`.

Character code:

`'I'`

Canonical name:

[`numpy.uintc`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintc "numpy.uintc")

Alias on this platform (Linux x86\_64):

[`numpy.uint32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint32 "numpy.uint32")
: 32-bit unsigned integer (`0` to `4_294_967_295`).

_class_ numpy.uint[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "Link to this definition")

uint64(value=0, /) –

Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit systems.

Character code:

`'L'`

Canonical name:

[`numpy.uint`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "numpy.uint")

Alias on this platform (Linux x86\_64):

[`numpy.uint64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint64 "numpy.uint64")
: 64-bit unsigned integer (`0` to `18_446_744_073_709_551_615`).

Alias on this platform (Linux x86\_64):

[`numpy.uintp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintp "numpy.uintp")
: Unsigned integer large enough to fit pointer, compatible with C `uintptr_t`.

numpy.ulong[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ulong "Link to this definition")

alias of [`uint`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "numpy.uint")

_class_ numpy.ulonglong(_value\=0_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ulonglong "Link to this definition")

Unsigned integer type, compatible with C `unsigned long long`.

Character code:

`'Q'`

### Inexact types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#inexact-types "Link to this heading")

_class_ numpy.inexact[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.inexact "Link to this definition")

Abstract base class of all numeric scalar types with a (potentially) inexact representation of the values in its range, such as floating-point numbers.

Note

Inexact scalars are printed using the fewest decimal digits needed to distinguish their value from other values of the same datatype, by judicious rounding. See the `unique` parameter of [`format_float_positional`](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy.format_float_positional "numpy.format_float_positional")
 and [`format_float_scientific`](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy.format_float_scientific "numpy.format_float_scientific")
.

This means that variables with equal binary values but whose datatypes are of different precisions may display differently:

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> f16 \= np.float16("0.1")
\>>> f32 \= np.float32(f16)
\>>> f64 \= np.float64(f32)
\>>> f16 \== f32 \== f64
True
\>>> f16, f32, f64
(0.1, 0.099975586, 0.0999755859375)

Copy to clipboard

Note that none of these floats hold the exact value \\(\\frac{1}{10}\\); `f16` prints as `0.1` because it is as close to that value as possible, whereas the other types do not as they have more precision and therefore have closer values.

Conversely, floating-point scalars of different precisions which approximate the same decimal value may compare unequal despite printing identically:

\>>> f16 \= np.float16("0.1")
\>>> f32 \= np.float32("0.1")
\>>> f64 \= np.float64("0.1")
\>>> f16 \== f32 \== f64
False
\>>> f16, f32, f64
(0.1, 0.1, 0.1)

Copy to clipboard

Go BackOpen In Tab

#### Floating-point types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#floating-point-types "Link to this heading")

_class_ numpy.floating[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.floating "Link to this definition")

Abstract base class of all floating-point scalar types.

_class_ numpy.half[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.half "Link to this definition")

float16(value=0, /) –

Half-precision floating-point number type.

Character code:

`'e'`

Canonical name:

[`numpy.half`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.half "numpy.half")

Alias on this platform (Linux x86\_64):

[`numpy.float16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float16 "numpy.float16")
: 16-bit-precision floating-point number type: sign bit, 5 bits exponent, 10 bits mantissa.

_class_ numpy.single[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.single "Link to this definition")

float32(value=0, /) –

Single-precision floating-point number type, compatible with C `float`.

Character code:

`'f'`

Canonical name:

[`numpy.single`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.single "numpy.single")

Alias on this platform (Linux x86\_64):

[`numpy.float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
: 32-bit-precision floating-point number type: sign bit, 8 bits exponent, 23 bits mantissa.

_class_ numpy.double(_x\=0_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.double "Link to this definition")

float64(value=0, /) –

Double-precision floating-point number type, compatible with Python [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
 and C `double`.

Character code:

`'d'`

Canonical name:

[`numpy.double`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.double "numpy.double")

Alias on this platform (Linux x86\_64):

[`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.

_class_ numpy.longdouble(_value\=0_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.longdouble "Link to this definition")

Extended-precision floating-point number type, compatible with C `long double` but not necessarily with IEEE 754 quadruple-precision.

Character code:

`'g'`

Alias on this platform (Linux x86\_64):

[`numpy.float128`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float128 "numpy.float128")
: 128-bit extended-precision floating-point number type.

#### Complex floating-point types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#complex-floating-point-types "Link to this heading")

_class_ numpy.complexfloating[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complexfloating "Link to this definition")

Abstract base class of all complex number scalar types that are made up of floating-point numbers.

_class_ numpy.csingle[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.csingle "Link to this definition")

complex64(real=0, imag=0, /) –

Complex number type composed of two single-precision floating-point numbers.

Character code:

`'F'`

Canonical name:

[`numpy.csingle`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.csingle "numpy.csingle")

Alias on this platform (Linux x86\_64):

[`numpy.complex64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex64 "numpy.complex64")
: Complex number type composed of 2 32-bit-precision floating-point numbers.

_class_ numpy.cdouble(_real\=0_, _imag\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.cdouble "Link to this definition")

complex128(real=0, imag=0, /) –

Complex number type composed of two double-precision floating-point numbers, compatible with Python [`complex`](https://docs.python.org/3/library/functions.html#complex "(in Python v3.14)")
.

Character code:

`'D'`

Canonical name:

[`numpy.cdouble`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.cdouble "numpy.cdouble")

Alias on this platform (Linux x86\_64):

[`numpy.complex128`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex128 "numpy.complex128")
: Complex number type composed of 2 64-bit-precision floating-point numbers.

_class_ numpy.clongdouble(_real\=0_, _imag\=0_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.clongdouble "Link to this definition")

Complex number type composed of two extended-precision floating-point numbers.

Character code:

`'G'`

Alias on this platform (Linux x86\_64):

[`numpy.complex256`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex256 "numpy.complex256")
: Complex number type composed of 2 128-bit extended-precision floating-point numbers.

### Other types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#other-types "Link to this heading")

numpy.bool\_[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "Link to this definition")

alias of [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")

_class_ numpy.bool(_value\=False_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "Link to this definition")

Boolean type (True or False), stored as a byte.

Warning

The [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 type is not a subclass of the [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 type (the [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 is not even a number type). This is different than Python’s default implementation of [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 as a sub-class of [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
.

Character code:

`'?'`

_class_ numpy.datetime64(_value\=None_, _\*args_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "Link to this definition")

If created from a 64-bit integer, it represents an offset from `1970-01-01T00:00:00`. If created from string, the string can be in ISO 8601 date or datetime format.

When parsing a string to create a datetime object, if the string contains a trailing timezone (A ‘Z’ or a timezone offset), the timezone will be dropped and a User Warning is given.

Datetime64 objects should be considered to be UTC and therefore have an offset of +0000.

\>>> np.datetime64(10, 'Y')
np.datetime64('1980')
\>>> np.datetime64('1980', 'Y')
np.datetime64('1980')
\>>> np.datetime64(10, 'D')
np.datetime64('1970-01-11')

Copy to clipboard

See [Datetimes and timedeltas](https://numpy.org/doc/stable/reference/arrays.datetime.html#arrays-datetime)
 for more information.

Character code:

`'M'`

_class_ numpy.timedelta64(_value\=0_, _\*args_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "Link to this definition")

A timedelta stored as a 64-bit integer.

See [Datetimes and timedeltas](https://numpy.org/doc/stable/reference/arrays.datetime.html#arrays-datetime)
 for more information.

Character code:

`'m'`

_class_ numpy.object\_(_value\=None_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "Link to this definition")

Any Python object.

Character code:

`'O'`

Note

The data actually stored in object arrays (_i.e._, arrays having dtype [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_")
) are references to Python objects, not the objects themselves. Hence, object arrays behave more like usual Python [`lists`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")
, in the sense that their contents need not be of the same Python type.

The object type is also special because an array containing [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_")
 items does not return an [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_")
 object on item access, but instead returns the actual object that the array item refers to.

The following data types are **flexible**: they have no predefined size and the data they describe can be of different length in different arrays. (In the character codes `#` is an integer denoting how many elements the data type consists of.)

_class_ numpy.flexible[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.flexible "Link to this definition")

Abstract base class of all scalar types without predefined length. The actual size of these types depends on the specific [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 instantiation.

_class_ numpy.character[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.character "Link to this definition")

Abstract base class of all character string scalar types.

_class_ numpy.bytes\_(_value\=''_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "Link to this definition")

A byte string.

When used in arrays, this type strips trailing null bytes.

Character code:

`'S'`

_class_ numpy.str\_(_value\=''_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "Link to this definition")

A unicode string.

This type strips trailing null codepoints.

\>>> s \= np.str\_("abc\\x00")
\>>> s
'abc'

Copy to clipboard

Unlike the builtin [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
, this supports the [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects "(in Python v3.14)")
, exposing its contents as UCS4:

\>>> m \= memoryview(np.str\_("abc"))
\>>> m.format
'3w'
\>>> m.tobytes()
b'a\\x00\\x00\\x00b\\x00\\x00\\x00c\\x00\\x00\\x00'

Copy to clipboard

Character code:

`'U'`

_class_ numpy.void(_length\_or\_data_, _/_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "Link to this definition")

Create a new structured or unstructured void scalar.

Parameters:

**length\_or\_data**int, array-like, bytes-like, object

One of multiple meanings (see notes). The length or bytes data of an unstructured void. Or alternatively, the data to be stored in the new scalar when [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is provided. This can be an array-like, in which case an array may be returned.

**dtype**dtype, optional

If provided the dtype of the new scalar. This dtype must be “void” dtype (i.e. a structured or unstructured void, see also [Structured datatypes](https://numpy.org/doc/stable/user/basics.rec.html#defining-structured-types)
).

New in version 1.24.

Notes

For historical reasons and because void scalars can represent both arbitrary byte data and structured dtypes, the void constructor has three calling conventions:

1.  `np.void(5)` creates a `dtype="V5"` scalar filled with five
    
    `\0` bytes. The 5 can be a Python or NumPy integer.
    
2.  `np.void(b"bytes-like")` creates a void scalar from the byte string.
    
    The dtype itemsize will match the byte string length, here `"V10"`.
    
3.  When a `dtype=` is passed the call is roughly the same as an
    
    array creation. However, a void scalar rather than array is returned.
    

Please see the examples which show all three different conventions.

Examples

Try it in your browser!

\>>> np.void(5)
np.void(b'\\x00\\x00\\x00\\x00\\x00')
\>>> np.void(b'abcd')
np.void(b'\\x61\\x62\\x63\\x64')
\>>> np.void((3.2, b'eggs'), dtype\="d,S5")
np.void((3.2, b'eggs'), dtype=\[('f0', '<f8'), ('f1', 'S5')\])
\>>> np.void(3, dtype\=\[('x', np.int8), ('y', np.int8)\])
np.void((3, 3), dtype=\[('x', 'i1'), ('y', 'i1')\])

Copy to clipboard

Character code:

`'V'`

Go BackOpen In Tab

Warning

Numeric Compatibility: If you used old typecode characters in your Numeric code (which was never recommended), you will need to change some of them to the new characters. In particular, the needed changes are `c -> S1`, `b -> B`, `1 -> b`, `s -> h`, `w -> H`, and `u -> I`. These changes make the type character convention more consistent with other Python modules such as the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "(in Python v3.14)")
 module.

### Sized aliases[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases "Link to this heading")

Along with their (mostly) C-derived names, the integer, float, and complex data-types are also available using a bit-width convention so that an array of the right size can always be ensured. Two aliases ([`numpy.intp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intp "numpy.intp")
 and [`numpy.uintp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintp "numpy.uintp")
) pointing to the integer type that is sufficiently large to hold a C pointer are also provided.

numpy.int8[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int8 "Link to this definition")

numpy.int16[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int16 "Link to this definition")

numpy.int32[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "Link to this definition")

numpy.int64[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "Link to this definition")

Aliases for the signed integer types (one of [`numpy.byte`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.byte "numpy.byte")
, [`numpy.short`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.short "numpy.short")
, [`numpy.intc`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intc "numpy.intc")
, [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
, [`numpy.long`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.long "numpy.long")
 and [`numpy.longlong`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.longlong "numpy.longlong")
) with the specified number of bits.

Compatible with the C99 `int8_t`, `int16_t`, `int32_t`, and `int64_t`, respectively.

numpy.uint8[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "Link to this definition")

numpy.uint16[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint16 "Link to this definition")

numpy.uint32[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint32 "Link to this definition")

numpy.uint64[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint64 "Link to this definition")

Alias for the unsigned integer types (one of [`numpy.ubyte`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ubyte "numpy.ubyte")
, [`numpy.ushort`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ushort "numpy.ushort")
, [`numpy.uintc`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintc "numpy.uintc")
, [`numpy.uint`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "numpy.uint")
, [`numpy.ulong`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ulong "numpy.ulong")
 and [`numpy.ulonglong`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.ulonglong "numpy.ulonglong")
) with the specified number of bits.

Compatible with the C99 `uint8_t`, `uint16_t`, `uint32_t`, and `uint64_t`, respectively.

numpy.intp[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intp "Link to this definition")

Alias for the signed integer type (one of [`numpy.byte`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.byte "numpy.byte")
, [`numpy.short`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.short "numpy.short")
, [`numpy.intc`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intc "numpy.intc")
, [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
, [`numpy.long`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.long "numpy.long")
 and [`numpy.longlong`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.longlong "numpy.longlong")
) that is used as a default integer and for indexing.

Compatible with the C `Py_ssize_t`.

Character code:

`'n'`

Changed in version 2.0: Before NumPy 2, this had the same size as a pointer. In practice this is almost always identical, but the character code `'p'` maps to the C `intptr_t`. The character code `'n'` was added in NumPy 2.0.

numpy.uintp[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uintp "Link to this definition")

Alias for the unsigned integer type that is the same size as `intp`.

Compatible with the C `size_t`.

Character code:

`'N'`

Changed in version 2.0: Before NumPy 2, this had the same size as a pointer. In practice this is almost always identical, but the character code `'P'` maps to the C `uintptr_t`. The character code `'N'` was added in NumPy 2.0.

numpy.float16[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float16 "Link to this definition")

alias of [`half`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.half "numpy.half")

numpy.float32[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "Link to this definition")

alias of [`single`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.single "numpy.single")

numpy.float64[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "Link to this definition")

alias of [`double`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.double "numpy.double")

numpy.float96[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float96 "Link to this definition")

numpy.float128[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float128 "Link to this definition")

Alias for [`numpy.longdouble`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.longdouble "numpy.longdouble")
, named after its size in bits. The existence of these aliases depends on the platform.

numpy.complex64[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex64 "Link to this definition")

alias of [`csingle`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.csingle "numpy.csingle")

numpy.complex128[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex128 "Link to this definition")

alias of [`cdouble`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.cdouble "numpy.cdouble")

numpy.complex192[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex192 "Link to this definition")

numpy.complex256[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/scalartypes.c.src)
[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex256 "Link to this definition")

Alias for [`numpy.clongdouble`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.clongdouble "numpy.clongdouble")
, named after its size in bits. The existence of these aliases depends on the platform.

Attributes[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#attributes "Link to this heading")

------------------------------------------------------------------------------------------------------------

The array scalar objects have an [`array priority`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 of [`NPY_SCALAR_PRIORITY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALAR_PRIORITY "NPY_SCALAR_PRIORITY")
 (-1,000,000.0). They also do not (yet) have a [`ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ctypes.html#numpy.ndarray.ctypes "numpy.ndarray.ctypes")
 attribute. Otherwise, they share the same attributes as arrays:

|     |     |
| --- | --- |
| [`generic.flags`](https://numpy.org/doc/stable/reference/generated/numpy.generic.flags.html#numpy.generic.flags "numpy.generic.flags") | The integer value of flags. |
| [`generic.shape`](https://numpy.org/doc/stable/reference/generated/numpy.generic.shape.html#numpy.generic.shape "numpy.generic.shape") | Tuple of array dimensions. |
| [`generic.strides`](https://numpy.org/doc/stable/reference/generated/numpy.generic.strides.html#numpy.generic.strides "numpy.generic.strides") | Tuple of bytes steps in each dimension. |
| [`generic.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.generic.ndim.html#numpy.generic.ndim "numpy.generic.ndim") | The number of array dimensions. |
| [`generic.data`](https://numpy.org/doc/stable/reference/generated/numpy.generic.data.html#numpy.generic.data "numpy.generic.data") | Pointer to start of data. |
| [`generic.size`](https://numpy.org/doc/stable/reference/generated/numpy.generic.size.html#numpy.generic.size "numpy.generic.size") | The number of elements in the gentype. |
| [`generic.itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.generic.itemsize.html#numpy.generic.itemsize "numpy.generic.itemsize") | The length of one element in bytes. |
| [`generic.base`](https://numpy.org/doc/stable/reference/generated/numpy.generic.base.html#numpy.generic.base "numpy.generic.base") | Scalar attribute identical to [`ndarray.base`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base")<br>. |
| [`generic.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.generic.dtype.html#numpy.generic.dtype "numpy.generic.dtype") | Get array data-descriptor. |
| [`generic.real`](https://numpy.org/doc/stable/reference/generated/numpy.generic.real.html#numpy.generic.real "numpy.generic.real") | The real part of the scalar. |
| [`generic.imag`](https://numpy.org/doc/stable/reference/generated/numpy.generic.imag.html#numpy.generic.imag "numpy.generic.imag") | The imaginary part of the scalar. |
| [`generic.flat`](https://numpy.org/doc/stable/reference/generated/numpy.generic.flat.html#numpy.generic.flat "numpy.generic.flat") | A 1-D view of the scalar. |
| [`generic.T`](https://numpy.org/doc/stable/reference/generated/numpy.generic.T.html#numpy.generic.T "numpy.generic.T") | Scalar attribute identical to [`ndarray.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T "numpy.ndarray.T")<br>. |
| [`generic.__array_interface__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__array_interface__.html#numpy.generic.__array_interface__ "numpy.generic.__array_interface__") | Array protocol: Python side |
| [`generic.__array_struct__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__array_struct__.html#numpy.generic.__array_struct__ "numpy.generic.__array_struct__") | Array protocol: struct |
| [`generic.__array_priority__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__array_priority__.html#numpy.generic.__array_priority__ "numpy.generic.__array_priority__") | Array priority. |
| [`generic.__array_wrap__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__array_wrap__.html#numpy.generic.__array_wrap__ "numpy.generic.__array_wrap__") | \_\_array\_wrap\_\_ implementation for scalar types |

Indexing[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#indexing "Link to this heading")

--------------------------------------------------------------------------------------------------------

See also

[Indexing routines](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
, [Data type objects (dtype)](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)

Array scalars can be indexed like 0-dimensional arrays: if _x_ is an array scalar,

*   `x[()]` returns a copy of array scalar
    
*   `x[...]` returns a 0-dimensional [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    
*   `x['field-name']` returns the array scalar in the field _field-name_. (_x_ can have fields, for example, when it corresponds to a structured data type.)
    

Methods[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#methods "Link to this heading")

------------------------------------------------------------------------------------------------------

Array scalars have exactly the same methods as arrays. The default behavior of these methods is to internally convert the scalar to an equivalent 0-dimensional array and to call the corresponding array method. In addition, math operations on array scalars are defined so that the same hardware flags are set and used to interpret the results as for [ufunc](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs)
, so that the error state used for ufuncs also carries over to the math on array scalars.

The exceptions to the above rules are given below:

|     |     |
| --- | --- |
| [`generic.__array__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__array__.html#numpy.generic.__array__ "numpy.generic.__array__") | sc.\_\_array\_\_(dtype) return 0-dim array from scalar with specified dtype |
| [`generic.__array_wrap__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__array_wrap__.html#numpy.generic.__array_wrap__ "numpy.generic.__array_wrap__") | \_\_array\_wrap\_\_ implementation for scalar types |
| [`generic.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.generic.squeeze.html#numpy.generic.squeeze "numpy.generic.squeeze")<br>(/\[, axis\]) | Scalar method identical to [`ndarray.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.squeeze.html#numpy.ndarray.squeeze "numpy.ndarray.squeeze")<br>. |
| [`generic.byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.generic.byteswap.html#numpy.generic.byteswap "numpy.generic.byteswap")<br>(/\[, inplace\]) | Scalar method identical to [`ndarray.byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.byteswap.html#numpy.ndarray.byteswap "numpy.ndarray.byteswap")<br>. |
| [`generic.__reduce__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__reduce__.html#numpy.generic.__reduce__ "numpy.generic.__reduce__") | Helper for pickle. |
| [`generic.__setstate__`](https://numpy.org/doc/stable/reference/generated/numpy.generic.__setstate__.html#numpy.generic.__setstate__ "numpy.generic.__setstate__") |     |
| [`generic.setflags`](https://numpy.org/doc/stable/reference/generated/numpy.generic.setflags.html#numpy.generic.setflags "numpy.generic.setflags")<br>(\*\[, write, align, uic\]) | Scalar method identical to [`ndarray.setflags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setflags.html#numpy.ndarray.setflags "numpy.ndarray.setflags")<br>. |

Utility method for typing:

|     |     |
| --- | --- |
| [`number.__class_getitem__`](https://numpy.org/doc/stable/reference/generated/numpy.number.__class_getitem__.html#numpy.number.__class_getitem__ "numpy.number.__class_getitem__")<br>(item, /) | Return a parametrized wrapper around the [`number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")<br> type. |

Defining new types[#](https://numpy.org/doc/stable/reference/arrays.scalars.html#defining-new-types "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

There are two ways to effectively define a new array scalar type (apart from composing structured types [dtypes](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
 from the built-in scalar types): One way is to simply subclass the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 and overwrite the methods of interest. This will work to a degree, but internally certain behaviors are fixed by the data type of the array. To fully customize the data type of an array you need to define a new data-type, and register it with NumPy. Such new types can only be defined in C, using the [NumPy C-API](https://numpy.org/doc/stable/reference/c-api/index.html#c-api)
.

On this page