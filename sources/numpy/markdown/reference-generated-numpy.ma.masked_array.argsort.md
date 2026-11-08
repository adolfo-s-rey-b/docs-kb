[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argsort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.argsort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argsort.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.argsort.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.argsort.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.argsort.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.argsort.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.argsort.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.argsort.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.argsort.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.argsort.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.argsort.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.argsort.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.argsort.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.argsort.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.argsort.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.argsort.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.argsort.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.argsort.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.argsort.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.argsort.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.argsort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.argsort[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argsort.html#numpy-ma-masked-array-argsort "Link to this heading")

============================================================================================================================================================================

method

ma.masked\_array.argsort(_axis=<no value>_, _kind=None_, _order=None_, _endwith=True_, _fill\_value=None_, _\*_, _stable=False_, _descending=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5607-L5692)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argsort.html#numpy.ma.masked_array.argsort "Link to this definition")

Return an ndarray of indices that sort the array along the specified axis. Masked values are filled beforehand to [`fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill_value.html#numpy.ma.masked_array.fill_value "numpy.ma.masked_array.fill_value")
.

Parameters:

**axis**int, optional

Axis along which to sort. If None, the default, the flattened array is used.

**kind**{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional

The sorting algorithm used.

**order**str or list of str, optional

When _a_ is an array with fields defined, this argument specifies which fields to compare first, second, etc. Not all fields need be specified.

**endwith**{True, False}, optional

Whether missing values (if any) should be treated as the largest values (True) or the smallest values (False) When the array contains unmasked values at the same extremes of the datatype, the ordering of these values and the masked values is undefined.

**fill\_value**scalar or None, optional

Value used internally for the masked values. If `fill_value` is not None, it supersedes `endwith`.

**stable**bool, optional

Only for compatibility with `np.argsort`. Ignored.

**descending**bool, optional

Only for compatibility with `np.sort`. Ignored.

Returns:

**index\_array**ndarray, int

Array of indices that sort _a_ along the specified axis. In other words, `a[index_array]` yields a sorted _a_.

See also

[`ma.MaskedArray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#numpy.ma.MaskedArray.sort "numpy.ma.MaskedArray.sort")

Describes sorting algorithms used.

[`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")

Indirect stable sort with multiple keys.

[`numpy.ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")

Inplace sort.

Notes

See [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
 for notes on the different sorting algorithms.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[3,2,1\], mask\=\[False, False, True\])
\>>> a
masked\_array(data=\[3, 2, --\],
             mask=\[False, False,  True\],
       fill\_value=999999)
\>>> a.argsort()
array(\[1, 0, 2\])

Copy to clipboard

Go BackOpen In Tab

On this page