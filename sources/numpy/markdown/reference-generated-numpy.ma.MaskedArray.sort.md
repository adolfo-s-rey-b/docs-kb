[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.sort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.sort.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.sort.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.sort.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.sort.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.sort.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.sort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.sort[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#numpy-ma-maskedarray-sort "Link to this heading")

===============================================================================================================================================================

method

ma.MaskedArray.sort(_axis\=\-1_, _kind\=None_, _order\=None_, _endwith\=True_, _fill\_value\=None_, _\*_, _stable\=False_, _descending\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5782-L5873)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#numpy.ma.MaskedArray.sort "Link to this definition")

Sort the array, in-place

Parameters:

**a**array\_like

Array to be sorted.

**axis**int, optional

Axis along which to sort. If None, the array is flattened before sorting. The default is -1, which sorts along the last axis.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional

The sorting algorithm used.

**order**list, optional

When _a_ is a structured array, this argument specifies which fields to compare first, second, and so on. This list does not need to include all of the fields.

**endwith**{True, False}, optional

Whether missing values (if any) should be treated as the largest values (True) or the smallest values (False) When the array contains unmasked values sorting at the same extremes of the datatype, the ordering of these values and the masked values is undefined.

**fill\_value**scalar or None, optional

Value used internally for the masked values. If `fill_value` is not None, it supersedes `endwith`.

**stable**bool, optional

Only for compatibility with `np.sort`. Ignored.

**descending**bool, optional

Only for compatibility with `np.sort`. Ignored.

See also

[`numpy.ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")

Method to sort an array in-place.

[`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")

Indirect sort.

[`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")

Indirect stable sort on multiple keys.

[`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")

Find elements in a sorted array.

Notes

See `sort` for notes on the different sorting algorithms.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[1, 2, 5, 4, 3\],mask\=\[0, 1, 0, 1, 0\])
\>>> \# Default
\>>> a.sort()
\>>> a
masked\_array(data=\[1, 3, 5, --, --\],
             mask=\[False, False, False,  True,  True\],
       fill\_value=999999)

Copy to clipboard

\>>> a \= np.ma.array(\[1, 2, 5, 4, 3\],mask\=\[0, 1, 0, 1, 0\])
\>>> \# Put missing values in the front
\>>> a.sort(endwith\=False)
\>>> a
masked\_array(data=\[--, --, 1, 3, 5\],
             mask=\[ True,  True, False, False, False\],
       fill\_value=999999)

Copy to clipboard

\>>> a \= np.ma.array(\[1, 2, 5, 4, 3\],mask\=\[0, 1, 0, 1, 0\])
\>>> \# fill\_value takes over endwith
\>>> a.sort(endwith\=False, fill\_value\=3)
\>>> a
masked\_array(data=\[1, --, --, 3, 5\],
             mask=\[False,  True,  True, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page