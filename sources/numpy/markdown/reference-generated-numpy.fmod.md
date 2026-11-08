[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fmod.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fmod.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fmod.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fmod.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fmod.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fmod.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fmod.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fmod.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fmod.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fmod.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fmod.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fmod.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fmod.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fmod.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fmod.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fmod.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fmod.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fmod.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fmod.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fmod.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fmod[#](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy-fmod "Link to this heading")

==================================================================================================================

numpy.fmod(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'fmod'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "Link to this definition")

Returns the element-wise remainder of division.

This is the NumPy implementation of the C library function fmod, the remainder has the same sign as the dividend _x1_. It is equivalent to the Matlab(TM) `rem` function and should not be confused with the Python modulus operator `x1 % x2`.

Parameters:

**x1**array\_like

Dividend.

**x2**array\_like

Divisor. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**array\_like

The remainder of the division of _x1_ by _x2_. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`remainder`](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#numpy.remainder "numpy.remainder")

Equivalent to the Python `%` operator.

[`divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html#numpy.divide "numpy.divide")

Notes

The result of the modulo operation for negative dividend and divisors is bound by conventions. For [`fmod`](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "numpy.fmod")
, the sign of result is the sign of the dividend, while for [`remainder`](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#numpy.remainder "numpy.remainder")
 the sign of the result is the sign of the divisor. The [`fmod`](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "numpy.fmod")
 function is equivalent to the Matlab(TM) `rem` function.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fmod(\[\-3, \-2, \-1, 1, 2, 3\], 2)
array(\[-1,  0, -1,  1,  0,  1\])
\>>> np.remainder(\[\-3, \-2, \-1, 1, 2, 3\], 2)
array(\[1, 0, 1, 1, 0, 1\])

Copy to clipboard

\>>> np.fmod(\[5, 3\], \[2, 2.\])
array(\[ 1.,  1.\])
\>>> a \= np.arange(\-3, 3).reshape(3, 2)
\>>> a
array(\[\[-3, -2\],\
       \[-1,  0\],\
       \[ 1,  2\]\])
\>>> np.fmod(a, \[2,2\])
array(\[\[-1,  0\],\
       \[-1,  0\],\
       \[ 1,  0\]\])

Copy to clipboard

Go BackOpen In Tab

On this page