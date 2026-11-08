[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.asin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.asin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.asin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.asin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.asin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.asin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.asin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.asin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.asin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.asin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.asin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.asin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.asin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.asin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.asin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.asin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.asin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.asin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.asin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.asin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.asin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.asin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.asin[#](https://numpy.org/doc/stable/reference/generated/numpy.asin.html#numpy-asin "Link to this heading")

==================================================================================================================

numpy.asin(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'arcsin'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.asin.html#numpy.asin "Link to this definition")

Inverse sine, element-wise.

Parameters:

**x**array\_like

_y_\-coordinate on the unit circle.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**angle**ndarray

The inverse sine of each element in _x_, in radians and in the closed interval `[-pi/2, pi/2]`. This is a scalar if _x_ is a scalar.

See also

[`sin`](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
, [`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
, [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")
, [`tan`](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")
, [`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
, [`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
, [`emath.arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.emath.arcsin.html#numpy.emath.arcsin "numpy.emath.arcsin")

Notes

[`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html#numpy.arcsin "numpy.arcsin")
 is a multivalued function: for each _x_ there are infinitely many numbers _z_ such that . The convention is to return the angle _z_ whose real part lies in \[-pi/2, pi/2\].

For real-valued input data types, _arcsin_ always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html#numpy.arcsin "numpy.arcsin")
 is a complex analytic function that has, by convention, the branch cuts \[-inf, -1\] and \[1, inf\] and is continuous from above on the former and from below on the latter.

The inverse sine is also known as [`asin`](https://numpy.org/doc/stable/reference/generated/numpy.asin.html#numpy.asin "numpy.asin")
 or sin^{-1}.

References

Abramowitz, M. and Stegun, I. A., _Handbook of Mathematical Functions_, 10th printing, New York: Dover, 1964, pp. 79ff. [https://personal.math.ubc.ca/~cbm/aands/page\_79.htm](https://personal.math.ubc.ca/~cbm/aands/page_79.htm)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.arcsin(1)     \# pi/2
1.5707963267948966
\>>> np.arcsin(\-1)    \# -pi/2
\-1.5707963267948966
\>>> np.arcsin(0)
0.0

Copy to clipboard

Go BackOpen In Tab

On this page