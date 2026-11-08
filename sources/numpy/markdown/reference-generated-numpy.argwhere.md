[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.argwhere[#](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html#numpy-argwhere "Link to this heading")

==============================================================================================================================

numpy.argwhere(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L619-L667)
[#](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html#numpy.argwhere "Link to this definition")

Find the indices of array elements that are non-zero, grouped by element.

Parameters:

**a**array\_like

Input data.

Returns:

**index\_array**(N, a.ndim) ndarray

Indices of elements that are non-zero. Indices are grouped by element. This array will have shape `(N, a.ndim)` where `N` is the number of non-zero items.

See also

[`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
, [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")

Notes

`np.argwhere(a)` is almost the same as `np.transpose(np.nonzero(a))`, but produces a result of the correct shape for a 0D array.

The output of `argwhere` is not suitable for indexing arrays. For this purpose use `nonzero(a)` instead.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(6).reshape(2,3)
\>>> x
array(\[\[0, 1, 2\],\
       \[3, 4, 5\]\])
\>>> np.argwhere(x\>1)
array(\[\[0, 2\],\
       \[1, 0\],\
       \[1, 1\],\
       \[1, 2\]\])

Copy to clipboard

Go BackOpen In Tab

On this page