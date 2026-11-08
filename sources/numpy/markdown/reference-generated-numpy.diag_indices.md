[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.diag_indices.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.diag_indices.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.diag_indices.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.diag_indices.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.diag_indices.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.diag_indices.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.diag_indices.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.diag_indices.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.diag_indices.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.diag_indices.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.diag_indices.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.diag_indices.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.diag_indices.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.diag_indices.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.diag_indices.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.diag_indices.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.diag_indices.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.diag_indices.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.diag_indices.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.diag_indices.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.diag\_indices[#](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy-diag-indices "Link to this heading")

===========================================================================================================================================

numpy.diag\_indices(_n_, _ndim\=2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_index_tricks_impl.py#L926-L990)
[#](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy.diag_indices "Link to this definition")

Return the indices to access the main diagonal of an array.

This returns a tuple of indices that can be used to access the main diagonal of an array _a_ with `a.ndim >= 2` dimensions and shape (n, n, …, n). For `a.ndim = 2` this is the usual diagonal, for `a.ndim > 2` this is the set of indices to access `a[i, i, ..., i]` for `i = [0..n-1]`.

Parameters:

**n**int

The size, along each dimension, of the arrays for which the returned indices can be used.

**ndim**int, optional

The number of dimensions.

See also

[`diag_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html#numpy.diag_indices_from "numpy.diag_indices_from")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Create a set of indices to access the diagonal of a (4, 4) array:

\>>> di \= np.diag\_indices(4)
\>>> di
(array(\[0, 1, 2, 3\]), array(\[0, 1, 2, 3\]))
\>>> a \= np.arange(16).reshape(4, 4)
\>>> a
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\],\
       \[12, 13, 14, 15\]\])
\>>> a\[di\] \= 100
\>>> a
array(\[\[100,   1,   2,   3\],\
       \[  4, 100,   6,   7\],\
       \[  8,   9, 100,  11\],\
       \[ 12,  13,  14, 100\]\])

Copy to clipboard

Now, we create indices to manipulate a 3-D array:

\>>> d3 \= np.diag\_indices(2, 3)
\>>> d3
(array(\[0, 1\]), array(\[0, 1\]), array(\[0, 1\]))

Copy to clipboard

And use it to set the diagonal of an array of zeros to 1:

\>>> a \= np.zeros((2, 2, 2), dtype\=np.int\_)
\>>> a\[d3\] \= 1
\>>> a
array(\[\[\[1, 0\],\
        \[0, 0\]\],\
       \[\[0, 0\],\
        \[0, 1\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page