[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.frexp.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.frexp.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.frexp.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.frexp.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.frexp.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.frexp.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.frexp.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.frexp.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.frexp.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.frexp.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.frexp.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.frexp.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.frexp.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.frexp.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.frexp.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.frexp.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.frexp.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.frexp.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.frexp.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.frexp.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.frexp[#](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html#numpy-frexp "Link to this heading")

=====================================================================================================================

numpy.frexp(_x_, \[_out1_, _out2_, \]_/_, \[_out=(None_, _None)_, \]_\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'frexp'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html#numpy.frexp "Link to this definition")

Decompose the elements of x into mantissa and twos exponent.

Returns (_mantissa_, _exponent_), where `x = mantissa * 2**exponent`. The mantissa lies in the open interval(-1, 1), while the twos exponent is a signed integer.

Parameters:

**x**array\_like

Array of numbers to be decomposed.

**out1**ndarray, optional

Output array for the mantissa. Must have the same shape as _x_.

**out2**ndarray, optional

Output array for the exponent. Must have the same shape as _x_.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**mantissa**ndarray

Floating values between -1 and 1. This is a scalar if _x_ is a scalar.

**exponent**ndarray

Integer exponents of 2. This is a scalar if _x_ is a scalar.

See also

[`ldexp`](https://numpy.org/doc/stable/reference/generated/numpy.ldexp.html#numpy.ldexp "numpy.ldexp")

Compute `y = x1 * 2**x2`, the inverse of [`frexp`](https://numpy.org/doc/stable/reference/generated/numpy.frexp.html#numpy.frexp "numpy.frexp")
.

Notes

Complex dtypes are not supported, they will raise a TypeError.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(9)
\>>> y1, y2 \= np.frexp(x)
\>>> y1
array(\[ 0.   ,  0.5  ,  0.5  ,  0.75 ,  0.5  ,  0.625,  0.75 ,  0.875,\
        0.5  \])
\>>> y2
array(\[0, 1, 2, 2, 3, 3, 3, 3, 4\], dtype=int32)
\>>> y1 \* 2\*\*y2
array(\[ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.\])

Copy to clipboard

Go BackOpen In Tab

On this page