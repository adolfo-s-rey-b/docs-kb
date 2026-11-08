[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.diag\_indices\_from[#](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html#numpy-diag-indices-from "Link to this heading")

===========================================================================================================================================================

numpy.diag\_indices\_from(_arr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_index_tricks_impl.py#L997-L1048)
[#](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html#numpy.diag_indices_from "Link to this definition")

Return the indices to access the main diagonal of an n-dimensional array.

See [`diag_indices`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy.diag_indices "numpy.diag_indices")
 for full details.

Parameters:

**arr**array, at least 2-D

See also

[`diag_indices`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy.diag_indices "numpy.diag_indices")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Create a 4 by 4 array.

\>>> a \= np.arange(16).reshape(4, 4)
\>>> a
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\],\
       \[12, 13, 14, 15\]\])

Copy to clipboard

Get the indices of the diagonal elements.

\>>> di \= np.diag\_indices\_from(a)
\>>> di
(array(\[0, 1, 2, 3\]), array(\[0, 1, 2, 3\]))

Copy to clipboard

\>>> a\[di\]
array(\[ 0,  5, 10, 15\])

Copy to clipboard

This is simply syntactic sugar for diag\_indices.

\>>> np.diag\_indices(a.shape\[0\])
(array(\[0, 1, 2, 3\]), array(\[0, 1, 2, 3\]))

Copy to clipboard

Go BackOpen In Tab

On this page