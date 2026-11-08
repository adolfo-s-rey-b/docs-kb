[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.atanh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.atanh.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.atanh.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.atanh.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.atanh.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.atanh.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.atanh.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.atanh.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.atanh.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.atanh.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.atanh.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.atanh.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.atanh.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.atanh.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.atanh.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.atanh.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.atanh.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.atanh.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.atanh.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.atanh.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.atanh.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.atanh.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.atanh[#](https://numpy.org/doc/stable/reference/generated/numpy.atanh.html#numpy-atanh "Link to this heading")

=====================================================================================================================

numpy.atanh(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'arctanh'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.atanh.html#numpy.atanh "Link to this definition")

Inverse hyperbolic tangent, element-wise.

Parameters:

**x**array\_like

Input array.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

Array of the same shape as _x_. This is a scalar if _x_ is a scalar.

See also

[`emath.arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.emath.arctanh.html#numpy.emath.arctanh "numpy.emath.arctanh")

Notes

[`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")
 is a multivalued function: for each _x_ there are infinitely many numbers _z_ such that `tanh(z) = x`. The convention is to return the _z_ whose imaginary part lies in _\[-pi/2, pi/2\]_.

For real-valued input data types, [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")
 is a complex analytical function that has branch cuts _\[-1, -inf\]_ and _\[1, inf\]_ and is continuous from above on the former and from below on the latter.

The inverse hyperbolic tangent is also known as [`atanh`](https://numpy.org/doc/stable/reference/generated/numpy.atanh.html#numpy.atanh "numpy.atanh")
 or `tanh^-1`.

References

\[1\]

M. Abramowitz and I.A. Stegun, “Handbook of Mathematical Functions”, 10th printing, 1964, pp. 86. [https://personal.math.ubc.ca/~cbm/aands/page\_86.htm](https://personal.math.ubc.ca/~cbm/aands/page_86.htm)

\[2\]

Wikipedia, “Inverse hyperbolic function”, [https://en.wikipedia.org/wiki/Arctanh](https://en.wikipedia.org/wiki/Arctanh)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.arctanh(\[0, \-0.5\])
array(\[ 0.        , -0.54930614\])

Copy to clipboard

Go BackOpen In Tab

On this page