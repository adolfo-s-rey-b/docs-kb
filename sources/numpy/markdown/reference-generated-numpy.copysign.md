[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.copysign.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.copysign[#](https://numpy.org/doc/stable/reference/generated/numpy.copysign.html#numpy-copysign "Link to this heading")

==============================================================================================================================

numpy.copysign(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'copysign'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.copysign.html#numpy.copysign "Link to this definition")

Change the sign of x1 to that of x2, element-wise.

If _x2_ is a scalar, its sign will be copied to all elements of _x1_.

Parameters:

**x1**array\_like

Values to change the sign of.

**x2**array\_like

The sign of _x2_ is copied to _x1_. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

The values of _x1_ with the sign of _x2_. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`sign`](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")

[`signbit`](https://numpy.org/doc/stable/reference/generated/numpy.signbit.html#numpy.signbit "numpy.signbit")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.copysign(1.3, \-1)
\-1.3
\>>> 1/np.copysign(0, 1)
inf
\>>> 1/np.copysign(0, \-1)
\-inf

Copy to clipboard

\>>> np.copysign(\[\-1, 0, 1\], \-1.1)
array(\[-1., -0., -1.\])
\>>> np.copysign(\[\-1, 0, 1\], np.arange(3)\-1)
array(\[-1.,  0.,  1.\])

Copy to clipboard

Go BackOpen In Tab

On this page