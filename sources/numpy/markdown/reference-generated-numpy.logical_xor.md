[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.logical\_xor[#](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy-logical-xor "Link to this heading")

========================================================================================================================================

numpy.logical\_xor(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'logical\_xor'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "Link to this definition")

Compute the truth value of x1 XOR x2, element-wise.

Parameters:

**x1, x2**array\_like

Logical XOR is applied to the elements of _x1_ and _x2_. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**bool or ndarray of bool

Boolean result of the logical XOR operation applied to the elements of _x1_ and _x2_; the shape is determined by broadcasting. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`logical_and`](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "numpy.logical_and")
, [`logical_or`](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
, [`logical_not`](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
, [`bitwise_xor`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#numpy.bitwise_xor "numpy.bitwise_xor")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.logical\_xor(True, False)
True
\>>> np.logical\_xor(\[True, True, False, False\], \[True, False, True, False\])
array(\[False,  True,  True, False\])

Copy to clipboard

\>>> x \= np.arange(5)
\>>> np.logical\_xor(x < 1, x \> 3)
array(\[ True, False, False, False,  True\])

Copy to clipboard

Simple example showing support of broadcasting

\>>> np.logical\_xor(0, np.eye(2))
array(\[\[ True, False\],\
       \[False,  True\]\])

Copy to clipboard

Go BackOpen In Tab

On this page