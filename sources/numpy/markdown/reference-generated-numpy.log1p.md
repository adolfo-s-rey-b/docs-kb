[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.log1p.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.log1p.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.log1p.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.log1p.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.log1p.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.log1p.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.log1p.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.log1p.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.log1p.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.log1p.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.log1p.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.log1p.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.log1p.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.log1p.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.log1p.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.log1p.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.log1p.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.log1p.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.log1p.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.log1p.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.log1p[#](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy-log1p "Link to this heading")

=====================================================================================================================

numpy.log1p(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'log1p'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "Link to this definition")

Return the natural logarithm of one plus the input array, element-wise.

Calculates `log(1 + x)`.

Parameters:

**x**array\_like

Input values.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

Natural logarithm of _1 + x_, element-wise. This is a scalar if _x_ is a scalar.

See also

[`expm1`](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html#numpy.expm1 "numpy.expm1")

`exp(x) - 1`, the inverse of [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
.

Notes

For real-valued input, [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
 is accurate also for _x_ so small that _1 + x == 1_ in floating-point accuracy.

Logarithm is a multivalued function: for each _x_ there is an infinite number of _z_ such that _exp(z) = 1 + x_. The convention is to return the _z_ whose imaginary part lies in _\[-pi, pi\]_.

For real-valued input data types, [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
 is a complex analytical function that has a branch cut _\[-inf, -1\]_ and is continuous from above on it. [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
 handles the floating-point negative zero as an infinitesimal negative number, conforming to the C99 standard.

References

\[1\]

M. Abramowitz and I.A. Stegun, “Handbook of Mathematical Functions”, 10th printing, 1964, pp. 67. [https://personal.math.ubc.ca/~cbm/aands/page\_67.htm](https://personal.math.ubc.ca/~cbm/aands/page_67.htm)

\[2\]

Wikipedia, “Logarithm”. [https://en.wikipedia.org/wiki/Logarithm](https://en.wikipedia.org/wiki/Logarithm)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.log1p(1e-99)
1e-99
\>>> np.log(1 + 1e-99)
0.0

Copy to clipboard

Go BackOpen In Tab

On this page