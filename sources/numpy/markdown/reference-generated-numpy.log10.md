[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.log10.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.log10.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.log10.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.log10.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.log10.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.log10.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.log10.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.log10.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.log10.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.log10.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.log10.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.log10.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.log10.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.log10.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.log10.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.log10.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.log10.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.log10.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.log10.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.log10.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.log10.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.log10[#](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy-log10 "Link to this heading")

=====================================================================================================================

numpy.log10(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'log10'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "Link to this definition")

Return the base 10 logarithm of the input array, element-wise.

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

The logarithm to the base 10 of _x_, element-wise. NaNs are returned where x is negative. This is a scalar if _x_ is a scalar.

See also

[`emath.log10`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log10.html#numpy.emath.log10 "numpy.emath.log10")

Notes

Logarithm is a multivalued function: for each _x_ there is an infinite number of _z_ such that _10\*\*z = x_. The convention is to return the _z_ whose imaginary part lies in _(-pi, pi\]_.

For real-valued input data types, [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
 is a complex analytical function that has a branch cut _\[-inf, 0\]_ and is continuous from above on it. [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
 handles the floating-point negative zero as an infinitesimal negative number, conforming to the C99 standard.

In the cases where the input has a negative real part and a very small negative complex part (approaching 0), the result is so close to _\-pi_ that it evaluates to exactly _\-pi_.

References

\[1\]

M. Abramowitz and I.A. Stegun, “Handbook of Mathematical Functions”, 10th printing, 1964, pp. 67. [https://personal.math.ubc.ca/~cbm/aands/page\_67.htm](https://personal.math.ubc.ca/~cbm/aands/page_67.htm)

\[2\]

Wikipedia, “Logarithm”. [https://en.wikipedia.org/wiki/Logarithm](https://en.wikipedia.org/wiki/Logarithm)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.log10(\[1e-15, \-3.\])
array(\[-15.,  nan\])

Copy to clipboard

Go BackOpen In Tab

On this page