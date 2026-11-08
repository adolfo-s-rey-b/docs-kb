[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unique.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unique.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unique.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unique.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unique.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unique.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unique.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unique.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unique.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unique.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unique.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unique.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unique.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unique.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unique.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unique.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unique.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unique.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unique.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unique.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unique[#](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy-unique "Link to this heading")

========================================================================================================================

numpy.unique(_ar_, _return\_index\=False_, _return\_inverse\=False_, _return\_counts\=False_, _axis\=None_, _\*_, _equal\_nan\=True_, _sorted\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L145-L347)
[#](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "Link to this definition")

Find the unique elements of an array.

Returns the sorted unique elements of an array. There are three optional outputs in addition to the unique elements:

*   the indices of the input array that give the unique values
    
*   the indices of the unique array that reconstruct the input array
    
*   the number of times each unique value comes up in the input array
    

Parameters:

**ar**array\_like

Input array. Unless _axis_ is specified, this will be flattened if it is not already 1-D.

**return\_index**bool, optional

If True, also return the indices of _ar_ (along the specified axis, if provided, or in the flattened array) that result in the unique array.

**return\_inverse**bool, optional

If True, also return the indices of the unique array (for the specified axis, if provided) that can be used to reconstruct _ar_.

**return\_counts**bool, optional

If True, also return the number of times each unique item appears in _ar_.

**axis**int or None, optional

The axis to operate on. If None, _ar_ will be flattened. If an integer, the subarrays indexed by the given axis will be flattened and treated as the elements of a 1-D array with the dimension of the given axis, see the notes for more details. Object arrays or structured arrays that contain objects are not supported if the _axis_ kwarg is used. The default is None.

**equal\_nan**bool, optional

If True, collapses multiple NaN values in the return array into one.

New in version 1.24.

**sorted**bool, optional

If True, the unique elements are sorted. Elements may be sorted in practice even if `sorted=False`, but this could change without notice.

New in version 2.3.

Returns:

**unique**ndarray

The sorted unique values.

**unique\_indices**ndarray, optional

The indices of the first occurrences of the unique values in the original array. Only provided if _return\_index_ is True.

**unique\_inverse**ndarray, optional

The indices to reconstruct the original array from the unique array. Only provided if _return\_inverse_ is True.

**unique\_counts**ndarray, optional

The number of times each of the unique values comes up in the original array. Only provided if _return\_counts_ is True.

See also

[`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")

Repeat elements of an array.

[`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Return a sorted copy of an array.

Notes

When an axis is specified the subarrays indexed by the axis are sorted. This is done by making the specified axis the first dimension of the array (move the axis to the first dimension to keep the order of the other axes) and then flattening the subarrays in C order. The flattened subarrays are then viewed as a structured type with each element given a label, with the effect that we end up with a 1-D array of structured types that can be treated in the same way as any other 1-D array. The result is that the flattened subarrays are sorted in lexicographic order starting with the first element.

Changed in version 1.21: Like np.sort, NaN will sort to the end of the values. For complex arrays all NaN values are considered equivalent (no matter whether the NaN is in the real or imaginary part). As the representant for the returned array the smallest one in the lexicographical order is chosen - see np.sort for how the lexicographical order is defined for complex arrays.

Changed in version 2.0: For multi-dimensional inputs, `unique_inverse` is reshaped such that the input can be reconstructed using `np.take(unique, unique_inverse, axis=axis)`. The result is now not 1-dimensional when `axis=None`.

Note that in NumPy 2.0.0 a higher dimensional array was returned also when `axis` was not `None`. This was reverted, but `inverse.reshape(-1)` can be used to ensure compatibility with both versions.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.unique(\[1, 1, 2, 2, 3, 3\])
array(\[1, 2, 3\])
\>>> a \= np.array(\[\[1, 1\], \[2, 3\]\])
\>>> np.unique(a)
array(\[1, 2, 3\])

Copy to clipboard

Return the unique rows of a 2D array

\>>> a \= np.array(\[\[1, 0, 0\], \[1, 0, 0\], \[2, 3, 4\]\])
\>>> np.unique(a, axis\=0)
array(\[\[1, 0, 0\], \[2, 3, 4\]\])

Copy to clipboard

Return the indices of the original array that give the unique values:

\>>> a \= np.array(\['a', 'b', 'b', 'c', 'a'\])
\>>> u, indices \= np.unique(a, return\_index\=True)
\>>> u
array(\['a', 'b', 'c'\], dtype='<U1')
\>>> indices
array(\[0, 1, 3\])
\>>> a\[indices\]
array(\['a', 'b', 'c'\], dtype='<U1')

Copy to clipboard

Reconstruct the input array from the unique values and inverse:

\>>> a \= np.array(\[1, 2, 6, 4, 2, 3, 2\])
\>>> u, indices \= np.unique(a, return\_inverse\=True)
\>>> u
array(\[1, 2, 3, 4, 6\])
\>>> indices
array(\[0, 1, 4, 3, 1, 2, 1\])
\>>> u\[indices\]
array(\[1, 2, 6, 4, 2, 3, 2\])

Copy to clipboard

Reconstruct the input values from the unique values and counts:

\>>> a \= np.array(\[1, 2, 6, 4, 2, 3, 2\])
\>>> values, counts \= np.unique(a, return\_counts\=True)
\>>> values
array(\[1, 2, 3, 4, 6\])
\>>> counts
array(\[1, 3, 1, 1, 1\])
\>>> np.repeat(values, counts)
array(\[1, 2, 2, 2, 3, 4, 6\])    # original order not preserved

Copy to clipboard

Go BackOpen In Tab

On this page