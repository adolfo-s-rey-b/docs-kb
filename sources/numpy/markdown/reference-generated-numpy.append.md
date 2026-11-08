[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.append.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.append.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.append.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.append.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.append.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.append.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.append.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.append.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.append.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.append.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.append.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.append.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.append.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.append.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.append.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.append.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.append.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.append.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.append.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.append.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.append.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.append.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.append[#](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy-append "Link to this heading")

========================================================================================================================

numpy.append(_arr_, _values_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L5592-L5659)
[#](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "Link to this definition")

Append values to the end of an array.

Parameters:

**arr**array\_like

Values are appended to a copy of this array.

**values**array\_like

These values are appended to a copy of _arr_. It must be of the correct shape (the same shape as _arr_, excluding _axis_). If _axis_ is not specified, _values_ can be any shape and will be flattened before use.

**axis**int, optional

The axis along which _values_ are appended. If _axis_ is not given, both _arr_ and _values_ are flattened before use.

Returns:

**append**ndarray

A copy of _arr_ with _values_ appended to _axis_. Note that [`append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
 does not occur in-place: a new array is allocated and filled. If _axis_ is None, _out_ is a flattened array.

See also

[`insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert "numpy.insert")

Insert elements into an array.

[`delete`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")

Delete elements from an array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.append(\[1, 2, 3\], \[\[4, 5, 6\], \[7, 8, 9\]\])
array(\[1, 2, 3, ..., 7, 8, 9\])

Copy to clipboard

When _axis_ is specified, _values_ must have the correct shape.

\>>> np.append(\[\[1, 2, 3\], \[4, 5, 6\]\], \[\[7, 8, 9\]\], axis\=0)
array(\[\[1, 2, 3\],\
       \[4, 5, 6\],\
       \[7, 8, 9\]\])

Copy to clipboard

\>>> np.append(\[\[1, 2, 3\], \[4, 5, 6\]\], \[7, 8, 9\], axis\=0)
Traceback (most recent call last):
    ...
ValueError: all the input arrays must have same number of dimensions, but
the array at index 0 has 2 dimension(s) and the array at index 1 has 1
dimension(s)

Copy to clipboard

\>>> a \= np.array(\[1, 2\], dtype\=np.int\_)
\>>> c \= np.append(a, \[\])
\>>> c
array(\[1., 2.\])
\>>> c.dtype
float64

Copy to clipboard

Default dtype for empty ndarrays is [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 thus making the output of dtype [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 when appended with dtype [`int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")

Go BackOpen In Tab

On this page