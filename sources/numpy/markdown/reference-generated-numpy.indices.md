[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.indices.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.indices.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.indices.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.indices.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.indices.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.indices.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.indices.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.indices.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.indices.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.indices.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.indices.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.indices.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.indices.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.indices.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.indices.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.indices.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.indices.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.indices.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.indices.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.indices.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.indices.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.indices[#](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy-indices "Link to this heading")

===========================================================================================================================

numpy.indices(_dimensions_, _dtype=<class 'int'>_, _sparse=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1725-L1824)
[#](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "Link to this definition")

Return an array representing the indices of a grid.

Compute an array where the subarrays contain index values 0, 1, … varying only along the corresponding axis.

Parameters:

**dimensions**sequence of ints

The shape of the grid.

**dtype**dtype, optional

Data type of the result.

**sparse**boolean, optional

Return a sparse representation of the grid instead of a dense representation. Default is False.

Returns:

**grid**one ndarray or tuple of ndarrays

If sparse is False:

Returns one array of grid indices, `grid.shape = (len(dimensions),) + tuple(dimensions)`.

If sparse is True:

Returns a tuple of arrays, with `grid[i].shape = (1, ..., 1, dimensions[i], 1, ..., 1)` with dimensions\[i\] in the ith place

See also

[`mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
, [`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")
, [`meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")

Notes

The output shape in the dense case is obtained by prepending the number of dimensions in front of the tuple of dimensions, i.e. if _dimensions_ is a tuple `(r0, ..., rN-1)` of length `N`, the output shape is `(N, r0, ..., rN-1)`.

The subarrays `grid[k]` contains the N-D array of indices along the `k-th` axis. Explicitly:

grid\[k, i0, i1, ..., iN\-1\] \= ik

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> grid \= np.indices((2, 3))
\>>> grid.shape
(2, 2, 3)
\>>> grid\[0\]        \# row indices
array(\[\[0, 0, 0\],\
       \[1, 1, 1\]\])
\>>> grid\[1\]        \# column indices
array(\[\[0, 1, 2\],\
       \[0, 1, 2\]\])

Copy to clipboard

The indices can be used as an index into an array.

\>>> x \= np.arange(20).reshape(5, 4)
\>>> row, col \= np.indices((2, 3))
\>>> x\[row, col\]
array(\[\[0, 1, 2\],\
       \[4, 5, 6\]\])

Copy to clipboard

Note that it would be more straightforward in the above example to extract the required elements directly with `x[:2, :3]`.

If sparse is set to true, the grid will be returned in a sparse representation.

\>>> i, j \= np.indices((2, 3), sparse\=True)
\>>> i.shape
(2, 1)
\>>> j.shape
(1, 3)
\>>> i        \# row indices
array(\[\[0\],\
       \[1\]\])
\>>> j        \# column indices
array(\[\[0, 1, 2\]\])

Copy to clipboard

Go BackOpen In Tab

On this page