[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.recarray.partition.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.recarray.partition[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.partition.html#numpy-recarray-partition "Link to this heading")

============================================================================================================================================================

method

recarray.partition(_kth_, _axis\=\-1_, _kind\='introselect'_, _order\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.partition.html#numpy.recarray.partition "Link to this definition")

Partially sorts the elements in the array in such a way that the value of the element in k-th position is in the position it would be in a sorted array. In the output array, all elements smaller than the k-th element are located to the left of this element and all equal or greater are located to its right. The ordering of the elements in the two partitions on the either side of the k-th element in the output array is undefined.

Parameters:

**kth**int or sequence of ints

Element index to partition by. The kth element value will be in its final sorted position and all smaller elements will be moved before it and all equal or greater elements behind it. The order of all elements in the partitions is undefined. If provided with a sequence of kth it will partition all elements indexed by kth of them into their sorted position at once.

Deprecated since version 1.22.0: Passing booleans as index is deprecated.

**axis**int, optional

Axis along which to sort. Default is -1, which means sort along the last axis.

**kind**{‘introselect’}, optional

Selection algorithm. Default is ‘introselect’.

**order**str or list of str, optional

When _a_ is an array with fields defined, this argument specifies which fields to compare first, second, etc. A single field can be specified as a string, and not all fields need to be specified, but unspecified fields will still be used, in the order in which they come up in the dtype, to break ties.

See also

[`numpy.partition`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "numpy.partition")

Return a partitioned copy of an array.

[`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")

Indirect partition.

[`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Full sort.

Notes

See `np.partition` for notes on the different algorithms.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[3, 4, 2, 1\])
\>>> a.partition(3)
\>>> a
array(\[2, 1, 3, 4\]) # may vary

Copy to clipboard

\>>> a.partition((1, 3))
\>>> a
array(\[1, 2, 3, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page