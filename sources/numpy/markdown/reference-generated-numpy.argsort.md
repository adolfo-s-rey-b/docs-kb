[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.argsort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.argsort.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.argsort.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.argsort.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.argsort.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.argsort.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.argsort.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.argsort.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.argsort.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.argsort.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.argsort.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.argsort.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.argsort.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.argsort.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.argsort.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.argsort.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.argsort.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.argsort.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.argsort.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.argsort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.argsort[#](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy-argsort "Link to this heading")

===========================================================================================================================

numpy.argsort(_a_, _axis=-1_, _kind=None_, _order=None_, _\*_, _stable=None_, _descending=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1115-L1253)
[#](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "Link to this definition")

Returns the indices that would sort an array.

Perform an indirect sort along the given axis using the algorithm specified by the _kind_ keyword. It returns an array of indices of the same shape as _a_ that index data along the given axis in sorted order.

Parameters:

**a**array\_like

Array to sort.

**axis**int or None, optional

Axis along which to sort. The default is -1 (the last axis). If None, the flattened array is used.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional

Sorting algorithm. The default is ‘quicksort’. Note that both ‘stable’ and ‘mergesort’ use timsort under the covers and, in general, the actual implementation will vary with data type. The ‘mergesort’ option is retained for backwards compatibility.

**order**str or list of str, optional

When _a_ is an array with fields defined, this argument specifies which fields to compare first, second, etc. A single field can be specified as a string, and not all fields need be specified, but unspecified fields will still be used, in the order in which they come up in the dtype, to break ties.

**stable**bool, optional

Sort stability. If `True`, the returned array will maintain the relative order of `a` values which compare as equal. If `False` or `None`, this is not guaranteed. Internally, this option selects `kind='stable'`. Default: `None`.

New in version 2.0.0.

**descending**bool, optional

Sort order. If `True`, the returned array will be sorted in descending order. If `False` or `None`, the returned array will be sorted in ascending order. Values that are NaN are sorted to the end for both orders. Default: `None`.

New in version 2.5.0.

Returns:

**index\_array**ndarray, int

Array of indices that sort _a_ along the specified _axis_. If _a_ is one-dimensional, `a[index_array]` yields a sorted _a_. More generally, `np.take_along_axis(a, index_array, axis=axis)` always yields the sorted _a_, irrespective of dimensionality.

See also

[`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Describes sorting algorithms used.

[`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")

Indirect stable sort with multiple keys.

[`ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")

Inplace sort.

[`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")

Indirect partial sort.

[`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Apply `index_array` from argsort to an array as if by calling sort.

Notes

See [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
 for notes on the different sorting algorithms.

As of NumPy 1.4.0 [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
 works with real/complex arrays containing nan values. The enhanced sort order is documented in [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
.

Examples

Try it in your browser!

One dimensional array:

\>>> import numpy as np
\>>> x \= np.array(\[3, 1, 2\])
\>>> np.argsort(x)
array(\[1, 2, 0\])

Copy to clipboard

Two-dimensional array:

\>>> x \= np.array(\[\[0, 3\], \[2, 2\]\])
\>>> x
array(\[\[0, 3\],\
       \[2, 2\]\])

Copy to clipboard

\>>> ind \= np.argsort(x, axis\=0)  \# sorts along first axis (down)
\>>> ind
array(\[\[0, 1\],\
       \[1, 0\]\])
\>>> np.take\_along\_axis(x, ind, axis\=0)  \# same as np.sort(x, axis=0)
array(\[\[0, 2\],\
       \[2, 3\]\])

Copy to clipboard

\>>> ind \= np.argsort(x, axis\=1)  \# sorts along last axis (across)
\>>> ind
array(\[\[0, 1\],\
       \[0, 1\]\])
\>>> np.take\_along\_axis(x, ind, axis\=1)  \# same as np.sort(x, axis=1)
array(\[\[0, 3\],\
       \[2, 2\]\])

Copy to clipboard

Indices of the sorted elements of an N-dimensional array:

\>>> ind \= np.unravel\_index(np.argsort(x, axis\=None), x.shape)
\>>> ind
(array(\[0, 1, 1, 0\]), array(\[0, 0, 1, 1\]))
\>>> x\[ind\]  \# same as np.sort(x, axis=None)
array(\[0, 2, 2, 3\])

Copy to clipboard

Sorting with keys:

\>>> x \= np.array(\[(1, 0), (0, 1)\], dtype\=\[('x', '<i4'), ('y', '<i4')\])
\>>> x
array(\[(1, 0), (0, 1)\],
      dtype=\[('x', '<i4'), ('y', '<i4')\])

Copy to clipboard

\>>> np.argsort(x, order\=('x','y'))
array(\[1, 0\])

Copy to clipboard

\>>> np.argsort(x, order\=('y','x'))
array(\[0, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page