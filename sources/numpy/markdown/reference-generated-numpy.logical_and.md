[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.logical_and.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.logical_and.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.logical_and.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.logical_and.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.logical_and.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.logical_and.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.logical_and.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.logical_and.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.logical_and.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.logical_and.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.logical_and.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.logical_and.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.logical_and.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.logical_and.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.logical_and.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.logical_and.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.logical_and.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.logical_and.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.logical_and.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.logical_and.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.logical\_and[#](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy-logical-and "Link to this heading")

========================================================================================================================================

numpy.logical\_and(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'logical\_and'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "Link to this definition")

Compute the truth value of x1 AND x2 element-wise.

Parameters:

**x1, x2**array\_like

Input arrays. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray or bool

Boolean result of the logical AND operation applied to the elements of _x1_ and _x2_; the shape is determined by broadcasting. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`logical_or`](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
, [`logical_not`](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
, [`logical_xor`](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")

[`bitwise_and`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html#numpy.bitwise_and "numpy.bitwise_and")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.logical\_and(True, False)
False
\>>> np.logical\_and(\[True, False\], \[False, False\])
array(\[False, False\])

Copy to clipboard

\>>> x \= np.arange(5)
\>>> np.logical\_and(x\>1, x<4)
array(\[False, False,  True,  True, False\])

Copy to clipboard

The `&` operator can be used as a shorthand for `np.logical_and` on boolean ndarrays.

\>>> a \= np.array(\[True, False\])
\>>> b \= np.array(\[False, False\])
\>>> a & b
array(\[False, False\])

Copy to clipboard

Go BackOpen In Tab

On this page