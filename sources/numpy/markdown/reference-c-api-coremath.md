[Skip to main content](https://numpy.org/doc/stable/reference/c-api/coremath.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/coremath.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/coremath.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/coremath.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/coremath.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/coremath.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/coremath.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/coremath.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/coremath.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/coremath.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/coremath.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/coremath.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/coremath.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/coremath.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/coremath.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/coremath.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/coremath.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/coremath.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/coremath.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/coremath.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/coremath.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/coremath.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

NumPy core math library[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#numpy-core-math-library "Link to this heading")

======================================================================================================================================

This library contains most math-related C99 functionality, which can be used on platforms where C99 is not well supported. The core math functions have the same API as the C99 ones, except for the `npy_*` prefix.

The available functions are defined in `<numpy/npy_math.h>` - please refer to this header when in doubt.

Note

An effort is underway to make `npymath` smaller (since C99 compatibility of compilers has improved over time) and more easily vendorable or usable as a header-only dependency. That will avoid problems with shipping a static library built with a compiler which may not match the compiler used by a downstream package or end user. See [gh-20880](https://github.com/numpy/numpy/issues/20880)
 for details.

Floating point classification[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#floating-point-classification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

NPY\_NAN[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_NAN "Link to this definition")
  

This macro is defined to a NaN (Not a Number), and is guaranteed to have the signbit unset (‘positive’ NaN). The corresponding single and extension precision macro are available with the suffix F and L.

NPY\_INFINITY[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_INFINITY "Link to this definition")
  

This macro is defined to a positive inf. The corresponding single and extension precision macro are available with the suffix F and L.

NPY\_PZERO[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_PZERO "Link to this definition")
  

This macro is defined to positive zero. The corresponding single and extension precision macro are available with the suffix F and L.

NPY\_NZERO[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_NZERO "Link to this definition")
  

This macro is defined to negative zero (that is with the sign bit set). The corresponding single and extension precision macro are available with the suffix F and L.

npy\_isnan(x)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_isnan "Link to this definition")
  

This is an alias for C99 isnan: works for single, double and extended precision, and return a non 0 value if x is a NaN.

npy\_isfinite(x)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_isfinite "Link to this definition")
  

This is an alias for C99 isfinite: works for single, double and extended precision, and return a non 0 value if x is neither a NaN nor an infinity.

npy\_isinf(x)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_isinf "Link to this definition")
  

This is an alias for C99 isinf: works for single, double and extended precision, and return a non 0 value if x is infinite (positive and negative).

npy\_signbit(x)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_signbit "Link to this definition")
  

This is an alias for C99 signbit: works for single, double and extended precision, and return a non 0 value if x has the signbit set (that is the number is negative).

npy\_copysign(x, y)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_copysign "Link to this definition")
  

This is an alias for C99 copysign: return x with the same sign as y. Works for any value, including inf and nan. Single and extended precisions are available with suffix f and l.

Useful math constants[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#useful-math-constants "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The following math constants are available in `npy_math.h`. Single and extended precision are also available by adding the `f` and `l` suffixes respectively.

NPY\_E[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_E "Link to this definition")
  

Base of natural logarithm (\\(e\\))

NPY\_LOG2E[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_LOG2E "Link to this definition")
  

Logarithm to base 2 of the Euler constant (\\(\\frac{\\ln(e)}{\\ln(2)}\\))

NPY\_LOG10E[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_LOG10E "Link to this definition")
  

Logarithm to base 10 of the Euler constant (\\(\\frac{\\ln(e)}{\\ln(10)}\\))

NPY\_LOGE2[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_LOGE2 "Link to this definition")
  

Natural logarithm of 2 (\\(\\ln(2)\\))

NPY\_LOGE10[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_LOGE10 "Link to this definition")
  

Natural logarithm of 10 (\\(\\ln(10)\\))

NPY\_PI[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_PI "Link to this definition")
  

Pi (\\(\\pi\\))

NPY\_PI\_2[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_PI_2 "Link to this definition")
  

Pi divided by 2 (\\(\\frac{\\pi}{2}\\))

NPY\_PI\_4[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_PI_4 "Link to this definition")
  

Pi divided by 4 (\\(\\frac{\\pi}{4}\\))

NPY\_1\_PI[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_1_PI "Link to this definition")
  

Reciprocal of pi (\\(\\frac{1}{\\pi}\\))

NPY\_2\_PI[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_2_PI "Link to this definition")
  

Two times the reciprocal of pi (\\(\\frac{2}{\\pi}\\))

NPY\_EULER[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_EULER "Link to this definition")
  

The Euler constant

\\(\\lim\_{n\\rightarrow\\infty}({\\sum\_{k=1}^n{\\frac{1}{k}}-\\ln n})\\)

Low-level floating point manipulation[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#low-level-floating-point-manipulation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those can be useful for precise floating point comparison.

double npy\_nextafter(double x, double y)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_nextafter "Link to this definition")
  

This is an alias to C99 nextafter: return next representable floating point value from x in the direction of y. Single and extended precisions are available with suffix f and l.

double npy\_spacing(double x)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_spacing "Link to this definition")
  

This is a function equivalent to Fortran intrinsic. Return distance between x and next representable floating point value from x, e.g. spacing(1) == eps. spacing of nan and +/- inf return nan. Single and extended precisions are available with suffix f and l.

void npy\_set\_floatstatus\_divbyzero()[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_set_floatstatus_divbyzero "Link to this definition")
  

Set the divide by zero floating point exception

void npy\_set\_floatstatus\_overflow()[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_set_floatstatus_overflow "Link to this definition")
  

Set the overflow floating point exception

void npy\_set\_floatstatus\_underflow()[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_set_floatstatus_underflow "Link to this definition")
  

Set the underflow floating point exception

void npy\_set\_floatstatus\_invalid()[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_set_floatstatus_invalid "Link to this definition")
  

Set the invalid floating point exception

int npy\_get\_floatstatus()[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_get_floatstatus "Link to this definition")
  

Get floating point status. Returns a bitmask with following possible flags:

*   NPY\_FPE\_DIVIDEBYZERO
    
*   NPY\_FPE\_OVERFLOW
    
*   NPY\_FPE\_UNDERFLOW
    
*   NPY\_FPE\_INVALID
    

Note that [`npy_get_floatstatus_barrier`](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_get_floatstatus_barrier "npy_get_floatstatus_barrier")
 is preferable as it prevents aggressive compiler optimizations reordering the call relative to the code setting the status, which could lead to incorrect results.

int npy\_get\_floatstatus\_barrier(char\*)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_get_floatstatus_barrier "Link to this definition")
  

Get floating point status. A pointer to a local variable is passed in to prevent aggressive compiler optimizations from reordering this function call relative to the code setting the status, which could lead to incorrect results.

Returns a bitmask with following possible flags:

*   NPY\_FPE\_DIVIDEBYZERO
    
*   NPY\_FPE\_OVERFLOW
    
*   NPY\_FPE\_UNDERFLOW
    
*   NPY\_FPE\_INVALID
    

int npy\_clear\_floatstatus()[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_clear_floatstatus "Link to this definition")
  

Clears the floating point status. Returns the previous status mask.

Note that [`npy_clear_floatstatus_barrier`](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_clear_floatstatus_barrier "npy_clear_floatstatus_barrier")
 is preferable as it prevents aggressive compiler optimizations reordering the call relative to the code setting the status, which could lead to incorrect results.

int npy\_clear\_floatstatus\_barrier(char\*)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_clear_floatstatus_barrier "Link to this definition")
  

Clears the floating point status. A pointer to a local variable is passed in to prevent aggressive compiler optimizations from reordering this function call. Returns the previous status mask.

Support for complex numbers[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#support-for-complex-numbers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

C99-like complex functions have been added. Those can be used if you wish to implement portable C extensions. Since NumPy 2.0 we use C99 complex types as the underlying type:

typedef double \_Complex npy\_cdouble;
typedef float \_Complex npy\_cfloat;
typedef long double \_Complex npy\_clongdouble;

Copy to clipboard

MSVC does not support the `_Complex` type itself, but has added support for the C99 `complex.h` header by providing its own implementation. Thus, under MSVC, the equivalent MSVC types will be used:

typedef \_Dcomplex npy\_cdouble;
typedef \_Fcomplex npy\_cfloat;
typedef \_Lcomplex npy\_clongdouble;

Copy to clipboard

Because MSVC still does not support C99 syntax for initializing a complex number, you need to restrict to C90-compatible syntax, e.g.:

/\* a = 1 + 2i \\\*/
npy\_complex a \= npy\_cpack(1, 2);
npy\_complex b;

b \= npy\_log(a);

Copy to clipboard

A few utilities have also been added in `numpy/npy_math.h`, in order to retrieve or set the real or the imaginary part of a complex number:

npy\_cdouble c;
npy\_csetreal(&c, 1.0);
npy\_csetimag(&c, 0.0);
printf("%d + %di\\n", npy\_creal(c), npy\_cimag(c));

Copy to clipboard

Changed in version 2.0.0: The underlying C types for all of numpy’s complex types have been changed to use C99 complex types. Up until now the following was being used to represent complex types:

typedef struct { double real, imag; } npy\_cdouble;
typedef struct { float real, imag; } npy\_cfloat;
typedef struct {npy\_longdouble real, imag;} npy\_clongdouble;

Copy to clipboard

Using the `struct` representation ensured that complex numbers could be used on all platforms, even the ones without support for built-in complex types. It also meant that a static library had to be shipped together with NumPy to provide a C99 compatibility layer for downstream packages to use. In recent years however, support for native complex types has been improved immensely, with MSVC adding built-in support for the `complex.h` header in 2019.

To ease cross-version compatibility, macros that use the new set APIs have been added.

#define NPY\_CSETREAL(z, r) npy\_csetreal(z, r)
#define NPY\_CSETIMAG(z, i) npy\_csetimag(z, i)

Copy to clipboard

A compatibility layer is also provided in `numpy/npy_2_complexcompat.h`. It checks whether the macros exist, and falls back to the 1.x syntax in case they don’t.

#include <numpy/npy\_math.h>

#ifndef NPY\_CSETREALF
#define NPY\_CSETREALF(c, r) (c)->real = (r)
#endif
#ifndef NPY\_CSETIMAGF
#define NPY\_CSETIMAGF(c, i) (c)->imag = (i)
#endif

Copy to clipboard

We suggest all downstream packages that need this functionality to copy-paste the compatibility layer code into their own sources and use that, so that they can continue to support both NumPy 1.x and 2.x without issues. Note also that the `complex.h` header is included in `numpy/npy_common.h`, which makes `complex` a reserved keyword.

Linking against the core math library in an extension[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#linking-against-the-core-math-library-in-an-extension "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To use the core math library that NumPy ships as a static library in your own Python extension, you need to add the `npymath` compile and link options to your extension. The exact steps to take will depend on the build system you are using. The generic steps to take are:

1.  Add the numpy include directory (= the value of `np.get_include()`) to your include directories,
    
2.  The `npymath` static library resides in the `lib` directory right next to numpy’s include directory (i.e., `pathlib.Path(np.get_include()) / '..' / 'lib'`). Add that to your library search directories,
    
3.  Link with `libnpymath` and `libm`.
    

Note

Keep in mind that when you are cross compiling, you must use the `numpy` for the platform you are building for, not the native one for the build machine. Otherwise you pick up a static library built for the wrong architecture.

When you are building with [Meson](https://mesonbuild.com/)
, use:

\# Note that this will get easier in the future, when Meson has
\# support for numpy built in; most of this can then be replaced
\# by \`dependency('numpy')\`.
incdir\_numpy \= run\_command(py3,
  \[\
    '-c',\
    'import os; os.chdir(".."); import numpy; print(numpy.get\_include())'\
  \],
  check: true
).stdout().strip()

inc\_np \= include\_directories(incdir\_numpy)

cc \= meson.get\_compiler('c')
npymath\_path \= incdir\_numpy / '..' / 'lib'
npymath\_lib \= cc.find\_library('npymath', dirs: npymath\_path)

py3.extension\_module('module\_name',
  ...
  include\_directories: inc\_np,
  dependencies: \[npymath\_lib\],

Copy to clipboard

Half-precision functions[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#half-precision-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

The header file `<numpy/halffloat.h>` provides functions to work with IEEE 754-2008 16-bit floating point values. While this format is not typically used for numerical computations, it is useful for storing values which require floating point but do not need much precision. It can also be used as an educational tool to understand the nature of floating point round-off error.

Like for other types, NumPy includes a typedef npy\_half for the 16 bit float. Unlike for most of the other types, you cannot use this as a normal type in C, since it is a typedef for npy\_uint16. For example, 1.0 looks like 0x3c00 to C, and if you do an equality comparison between the different signed zeros, you will get -0.0 != 0.0 (0x8000 != 0x0000), which is incorrect.

For these reasons, NumPy provides an API to work with npy\_half values accessible by including `<numpy/halffloat.h>` and linking to `npymath`. For functions that are not provided directly, such as the arithmetic operations, the preferred method is to convert to float or double and back again, as in the following example.

npy\_half sum(int n, npy\_half \*array) {
    float ret \= 0;
    while(n\--) {
        ret += npy\_half\_to\_float(\*array++);
    }
    return npy\_float\_to\_half(ret);
}

Copy to clipboard

External Links:

*   [754-2008 IEEE Standard for Floating-Point Arithmetic](https://ieeexplore.ieee.org/document/4610935/)
    
*   [Half-precision Float Wikipedia Article](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
    .
    
*   [OpenGL Half Float Pixel Support](https://www.khronos.org/registry/OpenGL/extensions/ARB/ARB_half_float_pixel.txt)
    
*   [The OpenEXR image format](https://www.openexr.com/about.html)
    .
    

NPY\_HALF\_ZERO[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_ZERO "Link to this definition")
  

This macro is defined to positive zero.

NPY\_HALF\_PZERO[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_PZERO "Link to this definition")
  

This macro is defined to positive zero.

NPY\_HALF\_NZERO[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_NZERO "Link to this definition")
  

This macro is defined to negative zero.

NPY\_HALF\_ONE[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_ONE "Link to this definition")
  

This macro is defined to 1.0.

NPY\_HALF\_NEGONE[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_NEGONE "Link to this definition")
  

This macro is defined to -1.0.

NPY\_HALF\_PINF[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_PINF "Link to this definition")
  

This macro is defined to +inf.

NPY\_HALF\_NINF[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_NINF "Link to this definition")
  

This macro is defined to -inf.

NPY\_HALF\_NAN[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.NPY_HALF_NAN "Link to this definition")
  

This macro is defined to a NaN value, guaranteed to have its sign bit unset.

float npy\_half\_to\_float([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_to_float "Link to this definition")
  

Converts a half-precision float to a single-precision float.

double npy\_half\_to\_double([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_to_double "Link to this definition")
  

Converts a half-precision float to a double-precision float.

[npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 npy\_float\_to\_half(float f)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_float_to_half "Link to this definition")
  

Converts a single-precision float to a half-precision float. The value is rounded to the nearest representable half, with ties going to the nearest even. If the value is too small or too big, the system’s floating point underflow or overflow bit will be set.

[npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 npy\_double\_to\_half(double d)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_double_to_half "Link to this definition")
  

Converts a double-precision float to a half-precision float. The value is rounded to the nearest representable half, with ties going to the nearest even. If the value is too small or too big, the system’s floating point underflow or overflow bit will be set.

int npy\_half\_eq([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_eq "Link to this definition")
  

Compares two half-precision floats (h1 == h2).

int npy\_half\_ne([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_ne "Link to this definition")
  

Compares two half-precision floats (h1 != h2).

int npy\_half\_le([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_le "Link to this definition")
  

Compares two half-precision floats (h1 <= h2).

int npy\_half\_lt([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_lt "Link to this definition")
  

Compares two half-precision floats (h1 < h2).

int npy\_half\_ge([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_ge "Link to this definition")
  

Compares two half-precision floats (h1 >= h2).

int npy\_half\_gt([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_gt "Link to this definition")
  

Compares two half-precision floats (h1 > h2).

int npy\_half\_eq\_nonan([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_eq_nonan "Link to this definition")
  

Compares two half-precision floats that are known to not be NaN (h1 == h2). If a value is NaN, the result is undefined.

int npy\_half\_lt\_nonan([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_lt_nonan "Link to this definition")
  

Compares two half-precision floats that are known to not be NaN (h1 < h2). If a value is NaN, the result is undefined.

int npy\_half\_le\_nonan([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h1, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h2)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_le_nonan "Link to this definition")
  

Compares two half-precision floats that are known to not be NaN (h1 <= h2). If a value is NaN, the result is undefined.

int npy\_half\_iszero([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_iszero "Link to this definition")
  

Tests whether the half-precision float has a value equal to zero. This may be slightly faster than calling npy\_half\_eq(h, NPY\_ZERO).

int npy\_half\_isnan([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_isnan "Link to this definition")
  

Tests whether the half-precision float is a NaN.

int npy\_half\_isinf([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_isinf "Link to this definition")
  

Tests whether the half-precision float is plus or minus Inf.

int npy\_half\_isfinite([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_isfinite "Link to this definition")
  

Tests whether the half-precision float is finite (not NaN or Inf).

int npy\_half\_signbit([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_signbit "Link to this definition")
  

Returns 1 is h is negative, 0 otherwise.

[npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 npy\_half\_copysign([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 x, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 y)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_copysign "Link to this definition")
  

Returns the value of x with the sign bit copied from y. Works for any value, including Inf and NaN.

[npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 npy\_half\_spacing([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_spacing "Link to this definition")
  

This is the same for half-precision float as npy\_spacing and npy\_spacingf described in the low-level floating point section.

[npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 npy\_half\_nextafter([npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 x, [npy\_half](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_half "npy_half")
 y)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_half_nextafter "Link to this definition")
  

This is the same for half-precision float as npy\_nextafter and npy\_nextafterf described in the low-level floating point section.

[npy\_uint16](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint16 "npy_uint16")
 npy\_floatbits\_to\_halfbits([npy\_uint32](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint32 "npy_uint32")
 f)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_floatbits_to_halfbits "Link to this definition")
  

Low-level function which converts a 32-bit single-precision float, stored as a uint32, into a 16-bit half-precision float.

[npy\_uint16](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint16 "npy_uint16")
 npy\_doublebits\_to\_halfbits([npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 d)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_doublebits_to_halfbits "Link to this definition")
  

Low-level function which converts a 64-bit double-precision float, stored as a uint64, into a 16-bit half-precision float.

[npy\_uint32](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint32 "npy_uint32")
 npy\_halfbits\_to\_floatbits([npy\_uint16](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint16 "npy_uint16")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_halfbits_to_floatbits "Link to this definition")
  

Low-level function which converts a 16-bit half-precision float into a 32-bit single-precision float, stored as a uint32.

[npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 npy\_halfbits\_to\_doublebits([npy\_uint16](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint16 "npy_uint16")
 h)[#](https://numpy.org/doc/stable/reference/c-api/coremath.html#c.npy_halfbits_to_doublebits "Link to this definition")
  

Low-level function which converts a 16-bit half-precision float into a 64-bit double-precision float, stored as a uint64.

On this page