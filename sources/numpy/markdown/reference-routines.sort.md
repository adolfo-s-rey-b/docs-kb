[Skip to main content](https://numpy.org/doc/stable/reference/routines.sort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.sort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.sort.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.sort.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.sort.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.sort.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.sort.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.sort.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.sort.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.sort.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.sort.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.sort.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.sort.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.sort.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.sort.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.sort.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.sort.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.sort.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.sort.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.sort.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.sort.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.sort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Sorting, searching, and counting[#](https://numpy.org/doc/stable/reference/routines.sort.html#sorting-searching-and-counting "Link to this heading")

=====================================================================================================================================================

Sorting[#](https://numpy.org/doc/stable/reference/routines.sort.html#sorting "Link to this heading")

-----------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")<br>(a\[, axis, kind, order, stable, descending\]) | Return a sorted copy of an array. |
| [`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")<br>(keys\[, axis\]) | Perform an indirect stable sort using a sequence of keys. |
| [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")<br>(a\[, axis, kind, order, stable, ...\]) | Returns the indices that would sort an array. |
| [`ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")<br>(\[axis, kind, order, stable, ...\]) | Sort an array in-place. |
| [`sort_complex`](https://numpy.org/doc/stable/reference/generated/numpy.sort_complex.html#numpy.sort_complex "numpy.sort_complex")<br>(a) | Sort a complex array using the real part first, then the imaginary part. |
| [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "numpy.partition")<br>(a, kth\[, axis, kind, order\]) | Return a partitioned copy of an array. |
| [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")<br>(a, kth\[, axis, kind, order\]) | Perform an indirect partition along the given axis using the algorithm specified by the _kind_ keyword. |

Searching[#](https://numpy.org/doc/stable/reference/routines.sort.html#searching "Link to this heading")

---------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")<br>(a\[, axis, out, keepdims\]) | Returns the indices of the maximum values along an axis. |
| [`nanargmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanargmax.html#numpy.nanargmax "numpy.nanargmax")<br>(a\[, axis, out, keepdims\]) | Return the indices of the maximum values in the specified axis ignoring NaNs. |
| [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")<br>(a\[, axis, out, keepdims\]) | Returns the indices of the minimum values along an axis. |
| [`nanargmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html#numpy.nanargmin "numpy.nanargmin")<br>(a\[, axis, out, keepdims\]) | Return the indices of the minimum values in the specified axis ignoring NaNs. |
| [`argwhere`](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html#numpy.argwhere "numpy.argwhere")<br>(a) | Find the indices of array elements that are non-zero, grouped by element. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")<br>(a) | Return the indices of the elements that are non-zero. |
| [`flatnonzero`](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")<br>(a) | Return indices that are non-zero in the flattened version of a. |
| [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")<br>(condition, \[x, y\], /) | Return elements chosen from _x_ or _y_ depending on _condition_. |
| [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")<br>(a, v\[, side, sorter\]) | Find indices where elements should be inserted to maintain order. |
| [`extract`](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "numpy.extract")<br>(condition, arr) | Return the elements of an array that satisfy some condition. |

Counting[#](https://numpy.org/doc/stable/reference/routines.sort.html#counting "Link to this heading")

-------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`count_nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero "numpy.count_nonzero")<br>(a\[, axis, keepdims\]) | Counts the number of non-zero values in the array `a`. |

On this page