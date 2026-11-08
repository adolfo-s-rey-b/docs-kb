[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.acosh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.acosh[#](https://numpy.org/doc/stable/reference/generated/numpy.acosh.html#numpy-acosh "Link to this heading")

=====================================================================================================================

numpy.acosh(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'arccosh'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.acosh.html#numpy.acosh "Link to this definition")

Inverse hyperbolic cosine, element-wise.

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

**arccosh**ndarray

Array of the same shape as _x_. This is a scalar if _x_ is a scalar.

See also

[`cosh`](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html#numpy.cosh "numpy.cosh")
, [`arcsinh`](https://numpy.org/doc/stable/reference/generated/numpy.arcsinh.html#numpy.arcsinh "numpy.arcsinh")
, [`sinh`](https://numpy.org/doc/stable/reference/generated/numpy.sinh.html#numpy.sinh "numpy.sinh")
, [`arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")
, [`tanh`](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html#numpy.tanh "numpy.tanh")

Notes

[`arccosh`](https://numpy.org/doc/stable/reference/generated/numpy.arccosh.html#numpy.arccosh "numpy.arccosh")
 is a multivalued function: for each _x_ there are infinitely many numbers _z_ such that _cosh(z) = x_. The convention is to return the _z_ whose imaginary part lies in `[-pi, pi]` and the real part in `[0, inf]`.

For real-valued input data types, [`arccosh`](https://numpy.org/doc/stable/reference/generated/numpy.arccosh.html#numpy.arccosh "numpy.arccosh")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`arccosh`](https://numpy.org/doc/stable/reference/generated/numpy.arccosh.html#numpy.arccosh "numpy.arccosh")
 is a complex analytical function that has a branch cut _\[-inf, 1\]_ and is continuous from above on it.

References

\[1\]

M. Abramowitz and I.A. Stegun, “Handbook of Mathematical Functions”, 10th printing, 1964, pp. 86. [https://personal.math.ubc.ca/~cbm/aands/page\_86.htm](https://personal.math.ubc.ca/~cbm/aands/page_86.htm)

\[2\]

Wikipedia, “Inverse hyperbolic function”, [https://en.wikipedia.org/wiki/Arccosh](https://en.wikipedia.org/wiki/Arccosh)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.arccosh(\[np.e, 10.0\])
array(\[ 1.65745445,  2.99322285\])
\>>> np.arccosh(1)
0.0

Copy to clipboard

Go BackOpen In Tab

On this page