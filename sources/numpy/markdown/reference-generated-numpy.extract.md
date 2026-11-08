[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.extract.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.extract.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.extract.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.extract.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.extract.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.extract.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.extract.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.extract.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.extract.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.extract.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.extract.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.extract.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.extract.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.extract.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.extract.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.extract.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.extract.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.extract.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.extract.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.extract.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.extract.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.extract[#](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy-extract "Link to this heading")

===========================================================================================================================

numpy.extract(_condition_, _arr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L2054-L2104)
[#](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "Link to this definition")

Return the elements of an array that satisfy some condition.

This is equivalent to `np.compress(ravel(condition), ravel(arr))`. If _condition_ is boolean `np.extract` is equivalent to `arr[condition]`.

Note that [`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")
 does the exact opposite of [`extract`](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "numpy.extract")
.

Parameters:

**condition**array\_like

An array whose nonzero or True entries indicate the elements of _arr_ to extract.

**arr**array\_like

Input array of the same size as _condition_.

Returns:

**extract**ndarray

Rank 1 array of values from _arr_ where _condition_ is True.

See also

[`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put")
, [`copyto`](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "numpy.copyto")
, [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")
, [`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.arange(12).reshape((3, 4))
\>>> arr
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\]\])
\>>> condition \= np.mod(arr, 3)\==0
\>>> condition
array(\[\[ True, False, False,  True\],\
       \[False, False,  True, False\],\
       \[False,  True, False, False\]\])
\>>> np.extract(condition, arr)
array(\[0, 3, 6, 9\])

Copy to clipboard

If _condition_ is boolean:

\>>> arr\[condition\]
array(\[0, 3, 6, 9\])

Copy to clipboard

Go BackOpen In Tab

On this page