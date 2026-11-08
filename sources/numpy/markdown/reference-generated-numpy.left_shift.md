[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.left_shift.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.left_shift.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.left_shift.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.left_shift.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.left_shift.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.left_shift.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.left_shift.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.left_shift.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.left_shift.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.left_shift.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.left_shift.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.left_shift.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.left_shift.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.left_shift.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.left_shift.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.left_shift.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.left_shift.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.left_shift.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.left_shift.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.left_shift.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.left\_shift[#](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#numpy-left-shift "Link to this heading")

=====================================================================================================================================

numpy.left\_shift(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'left\_shift'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#numpy.left_shift "Link to this definition")

Shift the bits of an integer to the left.

Bits are shifted to the left by appending _x2_ 0s at the right of _x1_. Since the internal representation of numbers is in binary format, this operation is equivalent to multiplying _x1_ by `2**x2`.

Parameters:

**x1**array\_like of integer type

Input values.

**x2**array\_like of integer type

Number of zeros to append to _x1_. Has to be non-negative. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**array of integer type

Return _x1_ with bits shifted _x2_ times to the left. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.right_shift.html#numpy.right_shift "numpy.right_shift")

Shift the bits of an integer to the right.

[`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")

Return the binary representation of the input number as a string.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.binary\_repr(5)
'101'
\>>> np.left\_shift(5, 2)
20
\>>> np.binary\_repr(20)
'10100'

Copy to clipboard

\>>> np.left\_shift(5, \[1,2,3\])
array(\[10, 20, 40\])

Copy to clipboard

Note that the dtype of the second argument may change the dtype of the result and can lead to unexpected results in some cases (see [Casting Rules](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-casting)
):

\>>> a \= np.left\_shift(np.uint8(255), np.int64(1))  \# Expect 254
\>>> print(a, type(a)) \# Unexpected result due to upcasting
510 <class 'numpy.int64'>
\>>> b \= np.left\_shift(np.uint8(255), np.uint8(1))
\>>> print(b, type(b))
254 <class 'numpy.uint8'>

Copy to clipboard

The `<<` operator can be used as a shorthand for `np.left_shift` on ndarrays.

\>>> x1 \= 5
\>>> x2 \= np.array(\[1, 2, 3\])
\>>> x1 << x2
array(\[10, 20, 40\])

Copy to clipboard

Go BackOpen In Tab

On this page