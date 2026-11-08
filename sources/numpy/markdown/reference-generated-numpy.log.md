[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.log.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.log.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.log.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.log.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.log.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.log.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.log.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.log.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.log.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.log.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.log.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.log.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.log.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.log.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.log.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.log.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.log.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.log.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.log.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.log.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.log.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.log.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.log[#](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy-log "Link to this heading")

===============================================================================================================

numpy.log(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'log'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "Link to this definition")

Natural logarithm, element-wise.

The natural logarithm [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
 is the inverse of the exponential function, so that _log(exp(x)) = x_. The natural logarithm is logarithm in base [`e`](https://numpy.org/doc/stable/reference/constants.html#numpy.e "numpy.e")
.

Parameters:

**x**array\_like

Input value.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The natural logarithm of _x_, element-wise. This is a scalar if _x_ is a scalar.

See also

[`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
, [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")
, [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
, [`emath.log`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log.html#numpy.emath.log "numpy.emath.log")

Notes

Logarithm is a multivalued function: for each _x_ there is an infinite number of _z_ such that _exp(z) = x_. The convention is to return the _z_ whose imaginary part lies in _(-pi, pi\]_.

For real-valued input data types, [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
 is a complex analytical function that has a branch cut _\[-inf, 0\]_ and is continuous from above on it. [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
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
\>>> np.log(\[1, np.e, np.e\*\*2, 0\])
array(\[  0.,   1.,   2., -inf\])

Copy to clipboard

Go BackOpen In Tab

On this page