[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rint.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rint.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rint.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rint.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rint.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rint.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rint.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rint.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rint.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rint.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rint.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rint.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rint.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rint.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rint.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rint.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rint.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rint.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rint.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rint.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rint.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rint[#](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#numpy-rint "Link to this heading")

==================================================================================================================

numpy.rint(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'rint'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#numpy.rint "Link to this definition")

Round elements of the array to the nearest integer.

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

Output array is same shape and type as _x_. This is a scalar if _x_ is a scalar.

See also

[`fix`](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#numpy.fix "numpy.fix")
, [`ceil`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil")
, [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")
, [`trunc`](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html#numpy.trunc "numpy.trunc")

Notes

For values exactly halfway between rounded decimal values, NumPy rounds to the nearest even value. Thus 1.5 and 2.5 round to 2.0, -0.5 and 0.5 round to 0.0, etc.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\-1.7, \-1.5, \-0.2, 0.2, 1.5, 1.7, 2.0\])
\>>> np.rint(a)
array(\[-2., -2., -0.,  0.,  2.,  2.,  2.\])

Copy to clipboard

Go BackOpen In Tab

On this page