[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.remainder.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.remainder.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.remainder.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.remainder.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.remainder.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.remainder.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.remainder.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.remainder.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.remainder.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.remainder.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.remainder.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.remainder.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.remainder.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.remainder.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.remainder.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.remainder.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.remainder.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.remainder.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.remainder.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.remainder.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.remainder[#](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#numpy-remainder "Link to this heading")

=================================================================================================================================

numpy.remainder(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'remainder'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.remainder.html#numpy.remainder "Link to this definition")

Returns the element-wise remainder of division.

Computes the remainder complementary to the [`floor_divide`](https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html#numpy.floor_divide "numpy.floor_divide")
 function. It is equivalent to the Python modulus operator `x1 % x2` and has the same sign as the divisor _x2_. The MATLAB function equivalent to `np.remainder` is `mod`.

Warning

This should not be confused with:

*   Python’s [`math.remainder`](https://docs.python.org/3/library/math.html#math.remainder "(in Python v3.14)")
     and C’s `remainder`, which compute the IEEE remainder, which are the complement to `round(x1 / x2)`.
    
*   The MATLAB `rem` function and or the C `%` operator which is the complement to `int(x1 / x2)`.
    

Parameters:

**x1**array\_like

Dividend array.

**x2**array\_like

Divisor array. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The element-wise remainder of the quotient `floor_divide(x1, x2)`. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`floor_divide`](https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html#numpy.floor_divide "numpy.floor_divide")

Equivalent of Python `//` operator.

[`divmod`](https://numpy.org/doc/stable/reference/generated/numpy.divmod.html#numpy.divmod "numpy.divmod")

Simultaneous floor division and remainder.

[`fmod`](https://numpy.org/doc/stable/reference/generated/numpy.fmod.html#numpy.fmod "numpy.fmod")

Equivalent of the MATLAB `rem` function.

[`divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html#numpy.divide "numpy.divide")
, [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")

Notes

Returns 0 when _x2_ is 0 and both _x1_ and _x2_ are (arrays of) integers. `mod` is an alias of `remainder`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.remainder(\[4, 7\], \[2, 3\])
array(\[0, 1\])
\>>> np.remainder(np.arange(7), 5)
array(\[0, 1, 2, 3, 4, 0, 1\])

Copy to clipboard

The `%` operator can be used as a shorthand for `np.remainder` on ndarrays.

\>>> x1 \= np.arange(7)
\>>> x1 % 5
array(\[0, 1, 2, 3, 4, 0, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page