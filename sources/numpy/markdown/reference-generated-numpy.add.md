[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.add.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.add[#](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy-add "Link to this heading")

===============================================================================================================

numpy.add(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'add'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "Link to this definition")

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