[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.partition[#](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy-partition "Link to this heading")

=================================================================================================================================

numpy.partition(_a_, _kth_, _axis\=\-1_, _kind\='introselect'_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L732-L841)
[#](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "Link to this definition")

Return a partitioned copy of an array.

Creates a copy of the array and partially sorts it in such a way that the value of the element in k-th position is in the position it would be in a sorted array. In the output array, all elements smaller than the k-th element are located to the left of this element and all equal or greater are located to its right. The ordering of the elements in the two partitions on the either side of the k-th element in the output array is undefined.

Parameters:

**a**array\_like

Array to be sorted.

**kth**int or sequence of ints

Element index to partition by. The k-th value of the element will be in its final sorted position and all smaller elements will be moved before it and all equal or greater elements behind it. The order of all elements in the partitions is undefined. If provided with a sequence of k-th it will partition all elements indexed by k-th of them into their sorted position at once.

**axis**int or None, optional

Axis along which to sort. If None, the array is flattened before sorting. The default is -1, which sorts along the last axis.

**kind**{‘introselect’}, optional

Selection algorithm. Default is ‘introselect’.

**order**str or list of str, optional

When _a_ is an array with fields defined, this argument specifies which fields to compare first, second, etc. A single field can be specified as a string. Not all fields need be specified, but unspecified fields will still be used, in the order in which they come up in the dtype, to break ties.

Returns:

**partitioned\_array**ndarray

Array of the same type and shape as _a_.

See also

[`ndarray.partition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.partition.html#numpy.ndarray.partition "numpy.ndarray.partition")

Method to sort an array in-place.

[`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")

Indirect partition.

[`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Full sorting

Notes

The various selection algorithms are characterized by their average speed, worst case performance, work space size, and whether they are stable. A stable sort keeps items with the same key in the same relative order. The available algorithms have the following properties:

| kind | speed | worst case | work space | stable |
| --- | --- | --- | --- | --- |
| ‘introselect’ | 1   | O(n) | 0   | no  |

All the partition algorithms make temporary copies of the data when partitioning along any but the last axis. Consequently, partitioning along the last axis is faster and uses less space than partitioning along any other axis.

The sort order for complex numbers is lexicographic. If both the real and imaginary parts are non-nan then the order is determined by the real parts except when they are equal, in which case the order is determined by the imaginary parts.

The sort order of `np.nan` is bigger than `np.inf`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[7, 1, 7, 7, 1, 5, 7, 2, 3, 2, 6, 2, 3, 0\])
\>>> p \= np.partition(a, 4)
\>>> p
array(\[0, 1, 2, 1, 2, 5, 2, 3, 3, 6, 7, 7, 7, 7\]) # may vary

Copy to clipboard

`p[4]` is 2; all elements in `p[:4]` are less than or equal to `p[4]`, and all elements in `p[5:]` are greater than or equal to `p[4]`. The partition is:

\[0, 1, 2, 1\], \[2\], \[5, 2, 3, 3, 6, 7, 7, 7, 7\]

Copy to clipboard

The next example shows the use of multiple values passed to _kth_.

\>>> p2 \= np.partition(a, (4, 8))
\>>> p2
array(\[0, 1, 2, 1, 2, 3, 3, 2, 5, 6, 7, 7, 7, 7\])

Copy to clipboard

`p2[4]` is 2 and `p2[8]` is 5. All elements in `p2[:4]` are less than or equal to `p2[4]`, all elements in `p2[5:8]` are greater than or equal to `p2[4]` and less than or equal to `p2[8]`, and all elements in `p2[9:]` are greater than or equal to `p2[8]`. The partition is:

\[0, 1, 2, 1\], \[2\], \[3, 3, 2\], \[5\], \[6, 7, 7, 7, 7\]

Copy to clipboard

Go BackOpen In Tab

On this page