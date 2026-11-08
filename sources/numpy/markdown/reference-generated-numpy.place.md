[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.place.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.place.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.place.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.place.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.place.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.place.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.place.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.place.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.place.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.place.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.place.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.place.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.place.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.place.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.place.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.place.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.place.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.place.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.place.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.place.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.place.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.place.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.place[#](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy-place "Link to this heading")

=====================================================================================================================

numpy.place(_arr_, _mask_, _vals_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L2111-L2149)
[#](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "Link to this definition")

Change elements of an array based on conditional and input values.

Similar to `np.copyto(arr, vals, where=mask)`, the difference is that [`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")
 uses the first N elements of _vals_, where N is the number of True values in _mask_, while [`copyto`](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "numpy.copyto")
 uses the elements where _mask_ is True.

Note that [`extract`](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "numpy.extract")
 does the exact opposite of [`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")
.

Parameters:

**arr**ndarray

Array to put data into.

**mask**array\_like

Boolean mask array. Must have the same size as _arr_.

**vals**1-D sequence

Values to put into _arr_. Only the first N elements are used, where N is the number of True values in _mask_. If _vals_ is smaller than N, it will be repeated, and if elements of _arr_ are to be masked, this sequence must be non-empty.

See also

[`copyto`](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "numpy.copyto")
, [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put")
, [`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, [`extract`](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "numpy.extract")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.arange(6).reshape(2, 3)
\>>> np.place(arr, arr\>2, \[44, 55\])
\>>> arr
array(\[\[ 0,  1,  2\],\
       \[44, 55, 44\]\])

Copy to clipboard

Go BackOpen In Tab

On this page