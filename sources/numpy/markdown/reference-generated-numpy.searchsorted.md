[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.searchsorted.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.searchsorted.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.searchsorted.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.searchsorted.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.searchsorted.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.searchsorted.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.searchsorted.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.searchsorted.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.searchsorted.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.searchsorted.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.searchsorted.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.searchsorted.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.searchsorted.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.searchsorted.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.searchsorted.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.searchsorted.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.searchsorted.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.searchsorted.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.searchsorted.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.searchsorted.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.searchsorted[#](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy-searchsorted "Link to this heading")

==========================================================================================================================================

numpy.searchsorted(_a_, _v_, _side\='left'_, _sorter\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1459-L1539)
[#](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "Link to this definition")

Find indices where elements should be inserted to maintain order.

Find the indices into a sorted array _a_ such that, if the corresponding elements in _v_ were inserted before the indices, the order of _a_ would be preserved.

Assuming that _a_ is sorted:

| _side_ | returned index _i_ satisfies |
| --- | --- |
| left | `a[i-1] < v <= a[i]` |
| right | `a[i-1] <= v < a[i]` |

Parameters:

**a**1-D array\_like

Input array. If _sorter_ is None, then it must be sorted in ascending order, otherwise _sorter_ must be an array of indices that sort it.

**v**array\_like

Values to insert into _a_.

**side**{‘left’, ‘right’}, optional

If ‘left’, the index of the first suitable location found is given. If ‘right’, return the last such index. If there is no suitable index, return either 0 or N (where N is the length of _a_).

**sorter**1-D array\_like, optional

Optional array of integer indices that sort array a into ascending order. They are typically the result of argsort.

Returns:

**indices**int or array of ints

Array of insertion points with the same shape as _v_, or an integer if _v_ is a scalar.

See also

[`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Return a sorted copy of an array.

[`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")

Produce histogram from 1-D data.

Notes

Binary search is used to find the required insertion points.

As of NumPy 1.4.0 [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
 works with real/complex arrays containing [`nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
 values. The enhanced sort order is documented in [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
.

This function uses the same algorithm as the builtin python [`bisect.bisect_left`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left "(in Python v3.14)")
 (`side='left'`) and [`bisect.bisect_right`](https://docs.python.org/3/library/bisect.html#bisect.bisect_right "(in Python v3.14)")
 (`side='right'`) functions, which is also vectorized in the _v_ argument.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.searchsorted(\[11,12,13,14,15\], 13)
2
\>>> np.searchsorted(\[11,12,13,14,15\], 13, side\='right')
3
\>>> np.searchsorted(\[11,12,13,14,15\], \[\-10, 20, 12, 13\])
array(\[0, 5, 1, 2\])

Copy to clipboard

When _sorter_ is used, the returned indices refer to the sorted array of _a_ and not _a_ itself:

\>>> a \= np.array(\[40, 10, 20, 30\])
\>>> sorter \= np.argsort(a)
\>>> sorter
array(\[1, 2, 3, 0\])  # Indices that would sort the array 'a'
\>>> result \= np.searchsorted(a, 25, sorter\=sorter)
\>>> result
2
\>>> a\[sorter\[result\]\]
30  # The element at index 2 of the sorted array is 30.

Copy to clipboard

Go BackOpen In Tab

On this page