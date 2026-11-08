[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.triu_indices_from.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.triu_indices_from.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.triu_indices_from.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.triu_indices_from.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.triu_indices_from.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.triu_indices_from.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.triu_indices_from.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.triu_indices_from.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.triu_indices_from.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.triu_indices_from.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.triu_indices_from.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.triu_indices_from.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.triu_indices_from.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.triu_indices_from.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.triu_indices_from.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.triu_indices_from.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.triu_indices_from.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.triu_indices_from.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.triu_indices_from.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.triu_indices_from.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.triu\_indices\_from[#](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html#numpy-triu-indices-from "Link to this heading")

===========================================================================================================================================================

numpy.triu\_indices\_from(_arr_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L1182-L1242)
[#](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html#numpy.triu_indices_from "Link to this definition")

Return the indices for the upper-triangle of arr.

See [`triu_indices`](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#numpy.triu_indices "numpy.triu_indices")
 for full details.

Parameters:

**arr**ndarray, shape(N, N)

The indices will be valid for square arrays.

**k**int, optional

Diagonal offset (see [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
 for details).

Returns:

**triu\_indices\_from**tuple, shape(2) of ndarray, shape(N)

Indices for the upper-triangle of _arr_.

See also

[`triu_indices`](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#numpy.triu_indices "numpy.triu_indices")
, [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
, [`tril_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html#numpy.tril_indices_from "numpy.tril_indices_from")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Create a 4 by 4 array

\>>> a \= np.arange(16).reshape(4, 4)
\>>> a
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\],\
       \[12, 13, 14, 15\]\])

Copy to clipboard

Pass the array to get the indices of the upper triangular elements.

\>>> triui \= np.triu\_indices\_from(a)
\>>> triui
(array(\[0, 0, 0, 0, 1, 1, 1, 2, 2, 3\]), array(\[0, 1, 2, 3, 1, 2, 3, 2, 3, 3\]))

Copy to clipboard

\>>> a\[triui\]
array(\[ 0,  1,  2,  3,  5,  6,  7, 10, 11, 15\])

Copy to clipboard

This is syntactic sugar for triu\_indices().

\>>> np.triu\_indices(a.shape\[0\])
(array(\[0, 0, 0, 0, 1, 1, 1, 2, 2, 3\]), array(\[0, 1, 2, 3, 1, 2, 3, 2, 3, 3\]))

Copy to clipboard

Use the _k_ parameter to return the indices for the upper triangular array from the k-th diagonal.

\>>> triuim1 \= np.triu\_indices\_from(a, k\=1)
\>>> a\[triuim1\]
array(\[ 1,  2,  3,  6,  7, 11\])

Copy to clipboard

Go BackOpen In Tab

On this page