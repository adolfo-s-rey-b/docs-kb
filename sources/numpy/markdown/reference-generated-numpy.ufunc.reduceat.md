[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.reduceat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.reduceat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.reduceat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.reduceat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.reduceat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.reduceat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.reduceat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.reduceat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.reduceat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.reduceat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.reduceat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.reduceat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.reduceat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.reduceat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.reduceat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.reduceat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.reduceat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.reduceat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.reduceat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.reduceat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.reduceat[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#numpy-ufunc-reduceat "Link to this heading")

================================================================================================================================================

method

ufunc.reduceat(_array_, _indices_, _axis\=0_, _dtype\=None_, _out\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#numpy.ufunc.reduceat "Link to this definition")

Performs a (local) reduce with specified slices over a single axis.

For i in `range(len(indices))`, [`reduceat`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduceat.html#numpy.ufunc.reduceat "numpy.ufunc.reduceat")
 computes `ufunc.reduce(array[indices[i]:indices[i+1]])`, which becomes the i-th generalized “row” parallel to _axis_ in the final result (i.e., in a 2-D array, for example, if _axis = 0_, it becomes the i-th row, but if _axis = 1_, it becomes the i-th column). There are three exceptions to this:

*   when `i = len(indices) - 1` (so for the last index), `indices[i+1] = array.shape[axis]`.
    
*   if `indices[i] >= indices[i + 1]`, the i-th generalized “row” is simply `array[indices[i]]`.
    
*   if `indices[i] >= len(array)` or `indices[i] < 0`, an error is raised.
    

The shape of the output depends on the size of [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
, and may be larger than [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 (this happens if `len(indices) > array.shape[axis]`).

Parameters:

**array**array\_like

The array to act on.

**indices**array\_like

Paired indices, comma separated (not colon), specifying slices to reduce.

**axis**int, optional

The axis along which to apply the reduceat.

**dtype**data-type code, optional

The data type used to perform the operation. Defaults to that of `out` if given, and the data type of `array` otherwise (though upcast to conserve precision for some cases, such as `numpy.add.reduce` for integer or boolean input).

**out**ndarray, None, or tuple of ndarray and None, optional

Location into which the result is stored. If not provided or None, a freshly-allocated array is returned. For consistency with `ufunc.__call__`, if passed as a keyword argument, can be Ellipses (`out=...`, which has the same effect as None as an array is always returned), or a 1-element tuple.

Returns:

**r**ndarray

The reduced values. If _out_ was supplied, _r_ is a reference to _out_.

Notes

A descriptive example:

If [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 is 1-D, the function _ufunc.accumulate(array)_ is the same as `ufunc.reduceat(array, indices)[::2]` where [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
 is `range(len(array) - 1)` with a zero placed in every other element: `indices = zeros(2 * len(array) - 1)`, `indices[1::2] = range(1, len(array))`.

Don’t be fooled by this attribute’s name: _reduceat(array)_ is not necessarily smaller than [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
.

Examples

Try it in your browser!

To take the running sum of four successive values:

\>>> import numpy as np
\>>> np.add.reduceat(np.arange(8),\[0,4, 1,5, 2,6, 3,7\])\[::2\]
array(\[ 6, 10, 14, 18\])

Copy to clipboard

A 2-D example:

\>>> x \= np.linspace(0, 15, 16).reshape(4,4)
\>>> x
array(\[\[ 0.,   1.,   2.,   3.\],\
       \[ 4.,   5.,   6.,   7.\],\
       \[ 8.,   9.,  10.,  11.\],\
       \[12.,  13.,  14.,  15.\]\])

Copy to clipboard

\# reduce such that the result has the following five rows:
\# \[row1 + row2 + row3\]
\# \[row4\]
\# \[row2\]
\# \[row3\]
\# \[row1 + row2 + row3 + row4\]

Copy to clipboard

\>>> np.add.reduceat(x, \[0, 3, 1, 2, 0\])
array(\[\[12.,  15.,  18.,  21.\],\
       \[12.,  13.,  14.,  15.\],\
       \[ 4.,   5.,   6.,   7.\],\
       \[ 8.,   9.,  10.,  11.\],\
       \[24.,  28.,  32.,  36.\]\])

Copy to clipboard

\# reduce such that result has the following two columns:
\# \[col1 \* col2 \* col3, col4\]

Copy to clipboard

\>>> np.multiply.reduceat(x, \[0, 3\], 1)
array(\[\[   0.,     3.\],\
       \[ 120.,     7.\],\
       \[ 720.,    11.\],\
       \[2184.,    15.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page