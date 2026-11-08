[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.sort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.sort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.sort.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.sort.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.sort.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.sort.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.sort.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.sort.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.sort.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.sort.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.sort.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.sort.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.sort.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.sort.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.sort.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.sort.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.sort.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.sort.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.sort.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.sort.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.sort.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.sort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.sort[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.sort.html#numpy-memmap-sort "Link to this heading")

=======================================================================================================================================

method

memmap.sort(_axis\=\-1_, _kind\=None_, _order\=None_, _\*_, _stable\=None_, _descending\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.sort.html#numpy.memmap.sort "Link to this definition")

Sort an array in-place. Refer to [`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
 for full documentation.

Parameters:

**axis**int, optional

Axis along which to sort. Default is -1, which means sort along the last axis.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional

Sorting algorithm. The default is ‘quicksort’. Note that both ‘stable’ and ‘mergesort’ use timsort under the covers and, in general, the actual implementation will vary with datatype. The ‘mergesort’ option is retained for backwards compatibility.

**order**str or list of str, optional

When _a_ is an array with fields defined, this argument specifies which fields to compare first, second, etc. A single field can be specified as a string, and not all fields need be specified, but unspecified fields will still be used, in the order in which they come up in the dtype, to break ties.

**stable**bool, optional

Sort stability. If `True`, the returned array will maintain the relative order of `a` values which compare as equal. If `False` or `None`, this is not guaranteed. Internally, this option selects `kind='stable'`. Default: `None`.

New in version 2.0.0.

See also

[`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Return a sorted copy of an array.

[`numpy.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")

Indirect sort.

[`numpy.lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")

Indirect stable sort on multiple keys.

[`numpy.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")

Find elements in sorted array.

[`numpy.partition`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "numpy.partition")

Partial sort.

Notes

See [`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
 for notes on the different sorting algorithms.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1,4\], \[3,1\]\])
\>>> a.sort(axis\=1)
\>>> a
array(\[\[1, 4\],\
       \[1, 3\]\])
\>>> a.sort(axis\=0)
\>>> a
array(\[\[1, 3\],\
       \[1, 4\]\])

Copy to clipboard

Use the _order_ keyword to specify a field to use when sorting a structured array:

\>>> a \= np.array(\[('a', 2), ('c', 1)\], dtype\=\[('x', 'S1'), ('y', int)\])
\>>> a.sort(order\='y')
\>>> a
array(\[(b'c', 1), (b'a', 2)\],
      dtype=\[('x', 'S1'), ('y', '<i8')\])

Copy to clipboard

Go BackOpen In Tab

On this page