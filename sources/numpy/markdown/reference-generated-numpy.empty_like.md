[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.empty_like.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.empty_like.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.empty_like.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.empty_like.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.empty_like.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.empty_like.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.empty_like.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.empty_like.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.empty_like.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.empty_like.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.empty_like.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.empty_like.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.empty_like.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.empty_like.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.empty_like.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.empty_like.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.empty_like.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.empty_like.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.empty_like.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.empty_like.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.empty\_like[#](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy-empty-like "Link to this heading")

=====================================================================================================================================

numpy.empty\_like(_prototype_, _/_, _dtype\=None_, _order\='K'_, _subok\=True_, _shape\=None_, _\*_, _device\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "Link to this definition")

Return a new array with the same shape and type as a given array.

Parameters:

**prototype**array\_like

The shape and data-type of _prototype_ define these same attributes of the returned array.

**dtype**data-type, optional

Overrides the data type of the result.

**order**{‘C’, ‘F’, ‘A’, or ‘K’}, optional

Overrides the memory layout of the result. ‘C’ means C-order, ‘F’ means F-order, ‘A’ means ‘F’ if _prototype_ is Fortran contiguous, ‘C’ otherwise. ‘K’ means match the layout of _prototype_ as closely as possible.

**subok**bool, optional.

If True, then the newly created array will use the sub-class type of _prototype_, otherwise it will be a base-class array. Defaults to True.

**shape**int or sequence of ints, optional.

Overrides the shape of the result. If order=’K’ and the number of dimensions is unchanged, will try to keep order, otherwise, order=’C’ is implied.

**device**str, optional

The device on which to place the created array. Default: None. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

Returns:

**out**ndarray

Array of uninitialized (arbitrary) data with the same shape and type as _prototype_.

See also

[`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")

Return an array of ones with shape and type of input.

[`zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")

Return an array of zeros with shape and type of input.

[`full_like`](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")

Return a new array with shape of input filled with value.

[`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")

Return a new uninitialized array.

Notes

Unlike other array creation functions (e.g. [`zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
, [`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")
, [`full_like`](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
), [`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like")
 does not initialize the values of the array, and may therefore be marginally faster. However, the values stored in the newly allocated array are arbitrary. For reproducible behavior, be sure to set each element of the array before reading.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= (\[1,2,3\], \[4,5,6\])                         \# a is array-like
\>>> np.empty\_like(a)
array(\[\[-1073741821, -1073741821,           3\],    # uninitialized\
       \[          0,           0, -1073741821\]\])
\>>> a \= np.array(\[\[1., 2., 3.\],\[4.,5.,6.\]\])
\>>> np.empty\_like(a)
array(\[\[ -2.00000715e+000,   1.48219694e-323,  -2.00000572e+000\], # uninitialized\
       \[  4.38791518e-305,  -2.00000715e+000,   4.17269252e-309\]\])

Copy to clipboard

Go BackOpen In Tab

On this page