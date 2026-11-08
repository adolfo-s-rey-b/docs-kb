[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.insert.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.insert.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.insert.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.insert.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.insert.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.insert.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.insert.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.insert.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.insert.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.insert.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.insert.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.insert.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.insert.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.insert.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.insert.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.insert.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.insert.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.insert.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.insert.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.insert.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.insert.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.insert[#](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy-insert "Link to this heading")

========================================================================================================================

numpy.insert(_arr_, _obj_, _values_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L5404-L5585)
[#](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert "Link to this definition")

Insert values along the given axis before the given indices.

Parameters:

**arr**array\_like

Input array.

**obj**slice, int, array-like of ints or bools

Object that defines the index or indices before which _values_ is inserted.

Changed in version 2.1.2: Boolean indices are now treated as a mask of elements to insert, rather than being cast to the integers 0 and 1.

Support for multiple insertions when _obj_ is a single scalar or a sequence with one element (similar to calling insert multiple times).

**values**array\_like

Values to insert into _arr_. If the type of _values_ is different from that of _arr_, _values_ is converted to the type of _arr_. _values_ should be shaped so that `arr[...,obj,...] = values` is legal.

**axis**int, optional

Axis along which to insert _values_. If _axis_ is None then _arr_ is flattened first.

Returns:

**out**ndarray

A copy of _arr_ with _values_ inserted. Note that [`insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert "numpy.insert")
 does not occur in-place: a new array is returned. If _axis_ is None, _out_ is a flattened array.

See also

[`append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")

Append elements at the end of an array.

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`delete`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")

Delete elements from an array.

Notes

Note that for higher dimensional inserts `obj=0` behaves very different from `obj=[0]` just like `arr[:,0,:] = values` is different from `arr[:,[0],:] = values`. This is because of the difference between basic and advanced [indexing](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing)
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(6).reshape(3, 2)
\>>> a
array(\[\[0, 1\],\
       \[2, 3\],\
       \[4, 5\]\])
\>>> np.insert(a, 1, 6)
array(\[0, 6, 1, 2, 3, 4, 5\])
\>>> np.insert(a, 1, 6, axis\=1)
array(\[\[0, 6, 1\],\
       \[2, 6, 3\],\
       \[4, 6, 5\]\])

Copy to clipboard

Difference between sequence and scalars, showing how `obj=[1]` behaves different from `obj=1`:

\>>> np.insert(a, \[1\], \[\[7\],\[8\],\[9\]\], axis\=1)
array(\[\[0, 7, 1\],\
       \[2, 8, 3\],\
       \[4, 9, 5\]\])
\>>> np.insert(a, 1, \[\[7\],\[8\],\[9\]\], axis\=1)
array(\[\[0, 7, 8, 9, 1\],\
       \[2, 7, 8, 9, 3\],\
       \[4, 7, 8, 9, 5\]\])
\>>> np.array\_equal(np.insert(a, 1, \[7, 8, 9\], axis\=1),
...                np.insert(a, \[1\], \[\[7\],\[8\],\[9\]\], axis\=1))
True

Copy to clipboard

\>>> b \= a.flatten()
\>>> b
array(\[0, 1, 2, 3, 4, 5\])
\>>> np.insert(b, \[2, 2\], \[6, 7\])
array(\[0, 1, 6, 7, 2, 3, 4, 5\])

Copy to clipboard

\>>> np.insert(b, slice(2, 4), \[7, 8\])
array(\[0, 1, 7, 2, 8, 3, 4, 5\])

Copy to clipboard

\>>> np.insert(b, \[2, 2\], \[7.13, False\]) \# type casting
array(\[0, 1, 7, 0, 2, 3, 4, 5\])

Copy to clipboard

\>>> x \= np.arange(8).reshape(2, 4)
\>>> idx \= (1, 3)
\>>> np.insert(x, idx, 999, axis\=1)
array(\[\[  0, 999,   1,   2, 999,   3\],\
       \[  4, 999,   5,   6, 999,   7\]\])

Copy to clipboard

Go BackOpen In Tab

On this page