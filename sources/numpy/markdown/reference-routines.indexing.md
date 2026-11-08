[Skip to main content](https://numpy.org/doc/stable/reference/routines.indexing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.indexing.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.indexing.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.indexing.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.indexing.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.indexing.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.indexing.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.indexing.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.indexing.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.indexing.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.indexing.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.indexing.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.indexing.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.indexing.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.indexing.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.indexing.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.indexing.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.indexing.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.indexing.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.indexing.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.indexing.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.indexing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Indexing routines[#](https://numpy.org/doc/stable/reference/routines.indexing.html#indexing-routines "Link to this heading")

=============================================================================================================================

See also

[Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing)

Generating index arrays[#](https://numpy.org/doc/stable/reference/routines.indexing.html#generating-index-arrays "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`c_`](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_") | Translates slice objects to concatenation along the second axis. |
| [`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_") | Translates slice objects to concatenation along the first axis. |
| [`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_") | A nicer way to build up index tuples for arrays. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")<br>(a) | Return the indices of the elements that are non-zero. |
| [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")<br>(condition, \[x, y\], /) | Return elements chosen from _x_ or _y_ depending on _condition_. |
| [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")<br>(dimensions\[, dtype, sparse\]) | Return an array representing the indices of a grid. |
| [`ix_`](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_")<br>(\*args) | Construct an open mesh from multiple sequences. |
| [`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid") | An instance which returns an open multi-dimensional "meshgrid". |
| [`ravel_multi_index`](https://numpy.org/doc/stable/reference/generated/numpy.ravel_multi_index.html#numpy.ravel_multi_index "numpy.ravel_multi_index")<br>(multi\_index, dims\[, mode, ...\]) | Converts a tuple of index arrays into an array of flat indices, applying boundary modes to the multi-index. |
| [`unravel_index`](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html#numpy.unravel_index "numpy.unravel_index")<br>(indices, shape\[, order\]) | Converts a flat index or array of flat indices into a tuple of coordinate arrays. |
| [`diag_indices`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy.diag_indices "numpy.diag_indices")<br>(n\[, ndim\]) | Return the indices to access the main diagonal of an array. |
| [`diag_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html#numpy.diag_indices_from "numpy.diag_indices_from")<br>(arr) | Return the indices to access the main diagonal of an n-dimensional array. |
| [`mask_indices`](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html#numpy.mask_indices "numpy.mask_indices")<br>(n, mask\_func\[, k\]) | Return the indices to access (n, n) arrays, given a masking function. |
| [`tril_indices`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices.html#numpy.tril_indices "numpy.tril_indices")<br>(n\[, k, m\]) | Return the indices for the lower-triangle of an (n, m) array. |
| [`tril_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html#numpy.tril_indices_from "numpy.tril_indices_from")<br>(arr\[, k\]) | Return the indices for the lower-triangle of arr. |
| [`triu_indices`](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#numpy.triu_indices "numpy.triu_indices")<br>(n\[, k, m\]) | Return the indices for the upper-triangle of an (n, m) array. |
| [`triu_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html#numpy.triu_indices_from "numpy.triu_indices_from")<br>(arr\[, k\]) | Return the indices for the upper-triangle of arr. |

Indexing-like operations[#](https://numpy.org/doc/stable/reference/routines.indexing.html#indexing-like-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")<br>(a, indices\[, axis, out, mode\]) | Take elements from an array along an axis. |
| [`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")<br>(arr, indices\[, axis\]) | Take values from the input array by matching 1d index and data slices. |
| [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")<br>(a, choices\[, out, mode\]) | Construct an array from an index array and a list of arrays to choose from. |
| [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")<br>(condition, a\[, axis, out\]) | Return selected slices of an array along given axis. |
| [`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")<br>(v\[, k\]) | Extract a diagonal or construct a diagonal array. |
| [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")<br>(a\[, offset, axis1, axis2\]) | Return specified diagonals. |
| [`select`](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy.select "numpy.select")<br>(condlist, choicelist\[, default\]) | Return an array drawn from elements in choicelist, depending on conditions. |

Inserting data into arrays[#](https://numpy.org/doc/stable/reference/routines.indexing.html#inserting-data-into-arrays "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")<br>(arr, mask, vals) | Change elements of an array based on conditional and input values. |
| [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put")<br>(a, ind, v\[, mode\]) | Replaces specified elements of an array with given values. |
| [`put_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html#numpy.put_along_axis "numpy.put_along_axis")<br>(arr, indices, values, axis) | Put values into the destination array by matching 1d index and data slices. |
| [`putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask")<br>(a, /, mask, values) | Changes elements of an array based on conditional and input values. |
| [`fill_diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#numpy.fill_diagonal "numpy.fill_diagonal")<br>(a, val\[, wrap\]) | Fill the main diagonal of the given array of any dimensionality. |

Iterating over arrays[#](https://numpy.org/doc/stable/reference/routines.indexing.html#iterating-over-arrays "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")<br>(op\[, flags, op\_flags, op\_dtypes, ...\]) | Efficient multi-dimensional iterator object to iterate over arrays. |
| [`ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")<br>(arr) | Multidimensional index iterator. |
| [`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")<br>(\*shape) | An N-dimensional iterator object to index arrays. |
| [`nested_iters`](https://numpy.org/doc/stable/reference/generated/numpy.nested_iters.html#numpy.nested_iters "numpy.nested_iters")<br>(op, axes\[, flags, op\_flags, ...\]) | Create nditers for use in nested loops |
| [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")<br>() | Flat iterator object to iterate over arrays. |
| [`iterable`](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "numpy.iterable")<br>(y) | Check whether or not an object can be iterated over. |

On this page