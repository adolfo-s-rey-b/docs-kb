[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.add.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.add.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.add.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.add.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.add.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.add.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.add.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.add.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.add.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.add.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.add.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.add.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.add.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.add.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.add.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.add.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.add.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.add.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.add.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.add.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.add.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.add.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.add[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.add.html#numpy-strings-add "Link to this heading")

=======================================================================================================================================

strings.add(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'add'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.add.html#numpy.strings.add "Link to this definition")

Add arguments element-wise.

Parameters:

**x1, x2**array\_like

The arrays to be added. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**add**ndarray or scalar

The sum of _x1_ and _x2_, element-wise. This is a scalar if both _x1_ and _x2_ are scalars.

Notes

Equivalent to _x1_ + _x2_ in terms of array broadcasting.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.add(1.0, 4.0)
5.0
\>>> x1 \= np.arange(9.0).reshape((3, 3))
\>>> x2 \= np.arange(3.0)
\>>> np.add(x1, x2)
array(\[\[  0.,   2.,   4.\],\
       \[  3.,   5.,   7.\],\
       \[  6.,   8.,  10.\]\])

Copy to clipboard

The `+` operator can be used as a shorthand for `np.add` on ndarrays.

\>>> x1 \= np.arange(9.0).reshape((3, 3))
\>>> x2 \= np.arange(3.0)
\>>> x1 + x2
array(\[\[ 0.,  2.,  4.\],\
       \[ 3.,  5.,  7.\],\
       \[ 6.,  8., 10.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page