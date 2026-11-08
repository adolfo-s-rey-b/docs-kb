[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros_like.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.zeros_like.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros_like.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.zeros_like.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.zeros_like.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.zeros_like.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.zeros_like.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.zeros_like.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.zeros_like.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.zeros_like.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.zeros_like.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.zeros_like.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.zeros_like.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.zeros_like.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.zeros_like.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.zeros_like.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.zeros_like.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.zeros_like.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.zeros_like.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.zeros_like.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.zeros_like.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.zeros_like.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.zeros\_like[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros_like.html#numpy-ma-zeros-like "Link to this heading")

==============================================================================================================================================

ma.zeros\_like(_a_, _dtype\=None_, _order\='K'_, _subok\=True_, _shape\=None_, _\*_, _device\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8820-L8832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros_like.html#numpy.ma.zeros_like "Link to this definition")

Return an array of zeros with the same shape and type as a given array.

Parameters:

**a**array\_like

The shape and data-type of _a_ define these same attributes of the returned array.

**dtype**data-type, optional

Overrides the data type of the result.

**order**{‘C’, ‘F’, ‘A’, or ‘K’}, optional

Overrides the memory layout of the result. ‘C’ means C-order, ‘F’ means F-order, ‘A’ means ‘F’ if _a_ is Fortran contiguous, ‘C’ otherwise. ‘K’ means match the layout of _a_ as closely as possible.

**subok**bool, optional.

If True, then the newly created array will use the sub-class type of _a_, otherwise it will be a base-class array. Defaults to True.

**shape**int or sequence of ints, optional.

Overrides the shape of the result. If order=’K’ and the number of dimensions is unchanged, will try to keep order, otherwise, order=’C’ is implied.

**device**str, optional

The device on which to place the created array. Default: None. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

Returns:

**out**MaskedArray

Array of zeros with the same shape and type as _a_.

See also

[`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like")

Return an empty array with shape and type of input.

[`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")

Return an array of ones with shape and type of input.

[`full_like`](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")

Return a new array with shape of input filled with value.

[`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")

Return a new array setting values to zero.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(6)
\>>> x \= x.reshape((2, 3))
\>>> x
array(\[\[0, 1, 2\],\
       \[3, 4, 5\]\])
\>>> np.zeros\_like(x)
array(\[\[0, 0, 0\],\
       \[0, 0, 0\]\])

Copy to clipboard

\>>> y \= np.arange(3, dtype\=np.float64)
\>>> y
array(\[0., 1., 2.\])
\>>> np.zeros\_like(y)
array(\[0.,  0.,  0.\])

Copy to clipboard

Go BackOpen In Tab

On this page