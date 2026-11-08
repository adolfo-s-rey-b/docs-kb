[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.minimum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.minimum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.minimum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.minimum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.minimum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.minimum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.minimum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.minimum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.minimum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.minimum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.minimum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.minimum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.minimum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.minimum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.minimum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.minimum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.minimum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.minimum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.minimum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.minimum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.minimum[#](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy-minimum "Link to this heading")

===========================================================================================================================

numpy.minimum(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'minimum'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "Link to this definition")

Element-wise minimum of array elements.

Compare two arrays and return a new array containing the element-wise minima. If one of the elements being compared is a NaN, then that element is returned. If both elements are NaNs then the first is returned. The latter distinction is important for complex NaNs, which are defined as at least one of the real or imaginary parts being a NaN. The net effect is that NaNs are propagated.

Parameters:

**x1, x2**array\_like

The arrays holding the elements to be compared. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray or scalar

The minimum of _x1_ and _x2_, element-wise. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum")

Element-wise maximum of two arrays, propagates NaNs.

[`fmin`](https://numpy.org/doc/stable/reference/generated/numpy.fmin.html#numpy.fmin "numpy.fmin")

Element-wise minimum of two arrays, ignores NaNs.

[`amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")

The minimum value of an array along a given axis, propagates NaNs.

[`nanmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html#numpy.nanmin "numpy.nanmin")

The minimum value of an array along a given axis, ignores NaNs.

[`fmax`](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")
, [`amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")
, [`nanmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "numpy.nanmax")

Notes

The minimum is equivalent to `np.where(x1 <= x2, x1, x2)` when neither x1 nor x2 are NaNs, but it is faster and does proper broadcasting.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.minimum(\[2, 3, 4\], \[1, 5, 2\])
array(\[1, 3, 2\])

Copy to clipboard

\>>> np.minimum(np.eye(2), \[0.5, 2\]) \# broadcasting
array(\[\[ 0.5,  0. \],\
       \[ 0. ,  1. \]\])

Copy to clipboard

\>>> np.minimum(\[np.nan, 0, np.nan\],\[0, np.nan, np.nan\])
array(\[nan, nan, nan\])
\>>> np.minimum(\-np.inf, 1)
\-inf

Copy to clipboard

Go BackOpen In Tab

On this page