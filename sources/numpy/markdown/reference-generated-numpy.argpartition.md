[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.argpartition.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.argpartition.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.argpartition.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.argpartition.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.argpartition.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.argpartition.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.argpartition.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.argpartition.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.argpartition.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.argpartition.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.argpartition.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.argpartition.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.argpartition.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.argpartition.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.argpartition.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.argpartition.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.argpartition.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.argpartition.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.argpartition.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.argpartition.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.argpartition[#](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy-argpartition "Link to this heading")

==========================================================================================================================================

numpy.argpartition(_a_, _kth_, _axis\=\-1_, _kind\='introselect'_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L848-L932)
[#](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "Link to this definition")

Perform an indirect partition along the given axis using the algorithm specified by the _kind_ keyword. It returns an array of indices of the same shape as _a_ that index data along the given axis in partitioned order.

Parameters:

**a**array\_like

Array to sort.

**kth**int or sequence of ints

Element index to partition by. The k-th element will be in its final sorted position and all smaller elements will be moved before it and all larger elements behind it. The order of all elements in the partitions is undefined. If provided with a sequence of k-th it will partition all of them into their sorted position at once.

**axis**int or None, optional

Axis along which to sort. The default is -1 (the last axis). If None, the flattened array is used.

**kind**{‘introselect’}, optional

Selection algorithm. Default is ‘introselect’

**order**str or list of str, optional

When _a_ is an array with fields defined, this argument specifies which fields to compare first, second, etc. A single field can be specified as a string, and not all fields need be specified, but unspecified fields will still be used, in the order in which they come up in the dtype, to break ties.

Returns:

**index\_array**ndarray, int

Array of indices that partition _a_ along the specified axis. If _a_ is one-dimensional, `a[index_array]` yields a partitioned _a_. More generally, `np.take_along_axis(a, index_array, axis=axis)` always yields the partitioned _a_, irrespective of dimensionality.

See also

[`partition`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "numpy.partition")

Describes partition algorithms used.

[`ndarray.partition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.partition.html#numpy.ndarray.partition "numpy.ndarray.partition")

Inplace partition.

[`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")

Full indirect sort.

[`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Apply `index_array` from argpartition to an array as if by calling partition.

Notes

The returned indices are not guaranteed to be sorted according to the values. Furthermore, the default selection algorithm `introselect` is unstable, and hence the returned indices are not guaranteed to be the earliest/latest occurrence of the element.

[`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")
 works for real/complex inputs with nan values, see [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "numpy.partition")
 for notes on the enhanced sort order and different selection algorithms.

Examples

Try it in your browser!

One dimensional array:

\>>> import numpy as np
\>>> x \= np.array(\[3, 4, 2, 1\])
\>>> x\[np.argpartition(x, 3)\]
array(\[2, 1, 3, 4\]) # may vary
\>>> x\[np.argpartition(x, (1, 3))\]
array(\[1, 2, 3, 4\]) # may vary

Copy to clipboard

\>>> x \= \[3, 4, 2, 1\]
\>>> np.array(x)\[np.argpartition(x, 3)\]
array(\[2, 1, 3, 4\]) # may vary

Copy to clipboard

Multi-dimensional array:

\>>> x \= np.array(\[\[3, 4, 2\], \[1, 3, 1\]\])
\>>> index\_array \= np.argpartition(x, kth\=1, axis\=-1)
\>>> \# below is the same as np.partition(x, kth=1)
\>>> np.take\_along\_axis(x, index\_array, axis\=-1)
array(\[\[2, 3, 4\],\
       \[1, 1, 3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page