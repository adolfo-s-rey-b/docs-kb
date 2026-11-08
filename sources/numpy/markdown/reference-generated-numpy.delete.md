[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.delete.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.delete.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.delete.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.delete.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.delete.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.delete.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.delete.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.delete.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.delete.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.delete.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.delete.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.delete.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.delete.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.delete.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.delete.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.delete.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.delete.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.delete.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.delete.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.delete.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.delete.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.delete[#](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy-delete "Link to this heading")

========================================================================================================================

numpy.delete(_arr_, _obj_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L5220-L5397)
[#](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "Link to this definition")

Return a new array with sub-arrays along an axis deleted. For a one dimensional array, this returns those entries not returned by _arr\[obj\]_.

Parameters:

**arr**array\_like

Input array.

**obj**slice, int, array-like of ints or bools

Indicate indices of sub-arrays to remove along the specified axis.

Changed in version 1.19.0: Boolean indices are now treated as a mask of elements to remove, rather than being cast to the integers 0 and 1.

**axis**int, optional

The axis along which to delete the subarray defined by _obj_. If _axis_ is None, _obj_ is applied to the flattened array.

Returns:

**out**ndarray

A copy of _arr_ with the elements specified by _obj_ removed. Note that [`delete`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")
 does not occur in-place. If _axis_ is None, _out_ is a flattened array.

See also

[`insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert "numpy.insert")

Insert elements into an array.

[`append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")

Append elements at the end of an array.

Notes

Often it is preferable to use a boolean mask. For example:

\>>> arr \= np.arange(12) + 1
\>>> mask \= np.ones(len(arr), dtype\=np.bool)
\>>> mask\[\[0,2,4\]\] \= False
\>>> result \= arr\[mask,...\]

Copy to clipboard

Is equivalent to `np.delete(arr, [0,2,4], axis=0)`, but allows further use of _mask_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.array(\[\[1,2,3,4\], \[5,6,7,8\], \[9,10,11,12\]\])
\>>> arr
array(\[\[ 1,  2,  3,  4\],\
       \[ 5,  6,  7,  8\],\
       \[ 9, 10, 11, 12\]\])
\>>> np.delete(arr, 1, 0)
array(\[\[ 1,  2,  3,  4\],\
       \[ 9, 10, 11, 12\]\])

Copy to clipboard

\>>> np.delete(arr, np.s\_\[::2\], 1)
array(\[\[ 2,  4\],\
       \[ 6,  8\],\
       \[10, 12\]\])
\>>> np.delete(arr, \[1,3,5\], None)
array(\[ 1,  3,  5,  7,  8,  9, 10, 11, 12\])

Copy to clipboard

Go BackOpen In Tab

On this page