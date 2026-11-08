[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.empty.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.empty.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.empty.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.empty.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.empty.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.empty.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.empty.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.empty.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.empty.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.empty.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.empty.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.empty.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.empty.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.empty.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.empty.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.empty.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.empty.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.empty.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.empty.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.empty.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.empty.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.empty.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.empty[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.empty.html#numpy-ma-empty "Link to this heading")

==============================================================================================================================

ma.empty(_shape_, _dtype\=None_, _order\='C'_, _\*_, _device\=None_, _like\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8820-L8832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.empty.html#numpy.ma.empty "Link to this definition")

Return a new array of given shape and type, without initializing entries.

Parameters:

**shape**int or tuple of int

Shape of the empty array, e.g., `(2, 3)` or `2`.

**dtype**data-type, optional

Desired output data-type for the array, e.g, [`numpy.int8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int8 "numpy.int8")
. Default is [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
.

**order**{‘C’, ‘F’}, optional, default: ‘C’

Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

**device**str, optional

The device on which to place the created array. Default: `None`. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**MaskedArray

Array of uninitialized (arbitrary) data of the given shape, dtype, and order. Object arrays will be initialized to None.

See also

[`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like")

Return an empty array with shape and type of input.

[`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")

Return a new array setting values to one.

[`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")

Return a new array setting values to zero.

[`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")

Return a new array of given shape filled with value.

Notes

Unlike other array creation functions (e.g. [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
, [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
, [`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
), [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
 does not initialize the values of the array, and may therefore be marginally faster. However, the values stored in the newly allocated array are arbitrary. For reproducible behavior, be sure to set each element of the array before reading.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.empty(\[2, 2\])
array(\[\[ -9.74499359e+001,   6.69583040e-309\],\
       \[  2.13182611e-314,   3.06959433e-309\]\])         #uninitialized

Copy to clipboard

\>>> np.empty(\[2, 2\], dtype\=np.int\_)
array(\[\[-1073741821, -1067949133\],\
       \[  496041986,    19249760\]\])                     #uninitialized

Copy to clipboard

Go BackOpen In Tab

On this page