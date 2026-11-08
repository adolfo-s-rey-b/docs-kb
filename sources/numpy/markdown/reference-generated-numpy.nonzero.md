[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nonzero.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nonzero.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nonzero.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nonzero.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nonzero.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nonzero.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nonzero.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nonzero.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nonzero.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nonzero.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nonzero.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nonzero.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nonzero.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nonzero.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nonzero.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nonzero.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nonzero.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nonzero.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nonzero.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nonzero.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nonzero[#](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy-nonzero "Link to this heading")

===========================================================================================================================

numpy.nonzero(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2031-L2115)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "Link to this definition")

Return the indices of the elements that are non-zero.

Returns a tuple of arrays, one for each dimension of _a_, containing the indices of the non-zero elements in that dimension. The values in _a_ are always tested and returned in row-major, C-style order.

To group the indices by element, rather than dimension, use [`argwhere`](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html#numpy.argwhere "numpy.argwhere")
, which returns a row for each non-zero element.

Parameters:

**a**array\_like

Input array.

Returns:

**tuple\_of\_arrays**tuple

Indices of elements that are non-zero.

See also

[`flatnonzero`](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")

Return indices that are non-zero in the flattened version of the input array.

[`ndarray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero")

Equivalent ndarray method.

[`count_nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero "numpy.count_nonzero")

Counts the number of non-zero elements in the input array.

Notes

While the nonzero values can be obtained with `a[nonzero(a)]`, it is recommended to use `x[x.astype(np.bool)]` or `x[x != 0]` instead, which will correctly handle 0-d arrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[3, 0, 0\], \[0, 4, 0\], \[5, 6, 0\]\])
\>>> x
array(\[\[3, 0, 0\],\
       \[0, 4, 0\],\
       \[5, 6, 0\]\])
\>>> np.nonzero(x)
(array(\[0, 1, 2, 2\]), array(\[0, 1, 0, 1\]))

Copy to clipboard

\>>> x\[np.nonzero(x)\]
array(\[3, 4, 5, 6\])
\>>> np.transpose(np.nonzero(x))
array(\[\[0, 0\],\
       \[1, 1\],\
       \[2, 0\],\
       \[2, 1\]\])

Copy to clipboard

A common use for `nonzero` is to find the indices of an array, where a condition is True. Given an array _a_, the condition _a_ > 3 is a boolean array and since False is interpreted as 0, np.nonzero(a > 3) yields the indices of the _a_ where the condition is true.

\>>> a \= np.array(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\])
\>>> a \> 3
array(\[\[False, False, False\],\
       \[ True,  True,  True\],\
       \[ True,  True,  True\]\])
\>>> np.nonzero(a \> 3)
(array(\[1, 1, 1, 2, 2, 2\]), array(\[0, 1, 2, 0, 1, 2\]))

Copy to clipboard

Using this result to index _a_ is equivalent to using the mask directly:

\>>> a\[np.nonzero(a \> 3)\]
array(\[4, 5, 6, 7, 8, 9\])
\>>> a\[a \> 3\]  \# prefer this spelling
array(\[4, 5, 6, 7, 8, 9\])

Copy to clipboard

`nonzero` can also be called as a method of the array.

\>>> (a \> 3).nonzero()
(array(\[1, 1, 1, 2, 2, 2\]), array(\[0, 1, 2, 0, 1, 2\]))

Copy to clipboard

Go BackOpen In Tab

On this page