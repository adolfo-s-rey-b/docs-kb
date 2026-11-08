[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.triu_indices.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.triu_indices.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.triu_indices.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.triu_indices.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.triu_indices.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.triu_indices.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.triu_indices.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.triu_indices.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.triu_indices.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.triu_indices.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.triu_indices.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.triu_indices.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.triu_indices.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.triu_indices.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.triu_indices.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.triu_indices.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.triu_indices.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.triu_indices.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.triu_indices.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.triu_indices.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.triu\_indices[#](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#numpy-triu-indices "Link to this heading")

===========================================================================================================================================

numpy.triu\_indices(_n_, _k\=0_, _m\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L1081-L1179)
[#](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#numpy.triu_indices "Link to this definition")

Return the indices for the upper-triangle of an (n, m) array.

Parameters:

**n**int

The size of the arrays for which the returned indices will be valid.

**k**int, optional

Diagonal offset (see [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
 for details).

**m**int, optional

The column dimension of the arrays for which the returned arrays will be valid. By default _m_ is taken equal to _n_.

Returns:

**inds**tuple, shape(2) of ndarrays, shape(_n_)

The row and column indices, respectively. The row indices are sorted in non-decreasing order, and the corresponding column indices are strictly increasing for each row.

See also

[`tril_indices`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices.html#numpy.tril_indices "numpy.tril_indices")

similar function, for lower-triangular.

[`mask_indices`](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html#numpy.mask_indices "numpy.mask_indices")

generic function accepting an arbitrary mask function.

[`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
, [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Compute two different sets of indices to access 4x4 arrays, one for the upper triangular part starting at the main diagonal, and one starting two diagonals further right:

\>>> iu1 \= np.triu\_indices(4)
\>>> iu1
(array(\[0, 0, 0, 0, 1, 1, 1, 2, 2, 3\]), array(\[0, 1, 2, 3, 1, 2, 3, 2, 3, 3\]))

Copy to clipboard

Note that row indices (first array) are non-decreasing, and the corresponding column indices (second array) are strictly increasing for each row.

Here is how they can be used with a sample array:

\>>> a \= np.arange(16).reshape(4, 4)
\>>> a
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\],\
       \[12, 13, 14, 15\]\])

Copy to clipboard

Both for indexing:

\>>> a\[iu1\]
array(\[ 0,  1,  2, ..., 10, 11, 15\])

Copy to clipboard

And for assigning values:

\>>> a\[iu1\] \= \-1
\>>> a
array(\[\[-1, -1, -1, -1\],\
       \[ 4, -1, -1, -1\],\
       \[ 8,  9, -1, -1\],\
       \[12, 13, 14, -1\]\])

Copy to clipboard

These cover only a small part of the whole array (two diagonals right of the main one):

\>>> iu2 \= np.triu\_indices(4, 2)
\>>> a\[iu2\] \= \-10
\>>> a
array(\[\[ -1,  -1, -10, -10\],\
       \[  4,  -1,  -1, -10\],\
       \[  8,   9,  -1,  -1\],\
       \[ 12,  13,  14,  -1\]\])

Copy to clipboard

Go BackOpen In Tab

On this page