[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.log2.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.log2.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.log2.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.log2.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.log2.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.log2.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.log2.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.log2.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.log2.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.log2.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.log2.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.log2.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.log2.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.log2.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.log2.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.log2.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.log2.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.log2.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.log2.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.log2.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.log2.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.log2[#](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy-log2 "Link to this heading")

==================================================================================================================

numpy.log2(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'log2'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "Link to this definition")

Base-2 logarithm of _x_.

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

Base-2 logarithm of _x_. This is a scalar if _x_ is a scalar.

See also

[`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
, [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
, [`log1p`](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
, [`emath.log2`](https://numpy.org/doc/stable/reference/generated/numpy.emath.log2.html#numpy.emath.log2 "numpy.emath.log2")

Notes

Logarithm is a multivalued function: for each _x_ there is an infinite number of _z_ such that _2\*\*z = x_. The convention is to return the _z_ whose imaginary part lies in _(-pi, pi\]_.

For real-valued input data types, [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")
 is a complex analytical function that has a branch cut _\[-inf, 0\]_ and is continuous from above on it. [`log2`](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")
 handles the floating-point negative zero as an infinitesimal negative number, conforming to the C99 standard.

In the cases where the input has a negative real part and a very small negative complex part (approaching 0), the result is so close to _\-pi_ that it evaluates to exactly _\-pi_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[0, 1, 2, 2\*\*4\])
\>>> np.log2(x)
array(\[-inf,   0.,   1.,   4.\])

Copy to clipboard

\>>> xi \= np.array(\[0+1.j, 1, 2+0.j, 4.j\])
\>>> np.log2(xi)
array(\[ 0.+2.26618007j,  0.+0.j        ,  1.+0.j        ,  2.+2.26618007j\])

Copy to clipboard

Go BackOpen In Tab

On this page