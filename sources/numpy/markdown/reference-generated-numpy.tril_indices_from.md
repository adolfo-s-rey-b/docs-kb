[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.tril_indices_from.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.tril_indices_from.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.tril_indices_from.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.tril_indices_from.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.tril_indices_from.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.tril_indices_from.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.tril_indices_from.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.tril_indices_from.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.tril_indices_from.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.tril_indices_from.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.tril_indices_from.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.tril_indices_from.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.tril_indices_from.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.tril_indices_from.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.tril_indices_from.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.tril_indices_from.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.tril_indices_from.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.tril_indices_from.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.tril_indices_from.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.tril_indices_from.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tril\_indices\_from[#](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html#numpy-tril-indices-from "Link to this heading")

===========================================================================================================================================================

numpy.tril\_indices\_from(_arr_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L1023-L1078)
[#](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices_from.html#numpy.tril_indices_from "Link to this definition")

Return the indices for the lower-triangle of arr.

See [`tril_indices`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices.html#numpy.tril_indices "numpy.tril_indices")
 for full details.

Parameters:

**arr**array\_like

The indices will be valid for square arrays whose dimensions are the same as arr.

**k**int, optional

Diagonal offset (see [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
 for details).

See also

[`tril_indices`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices.html#numpy.tril_indices "numpy.tril_indices")
, [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
, [`triu_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices_from.html#numpy.triu_indices_from "numpy.triu_indices_from")

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

Pass the array to get the indices of the lower triangular elements.

\>>> trili \= np.tril\_indices\_from(a)
\>>> trili
(array(\[0, 1, 1, 2, 2, 2, 3, 3, 3, 3\]), array(\[0, 0, 1, 0, 1, 2, 0, 1, 2, 3\]))

Copy to clipboard

\>>> a\[trili\]
array(\[ 0,  4,  5,  8,  9, 10, 12, 13, 14, 15\])

Copy to clipboard

This is syntactic sugar for tril\_indices().

\>>> np.tril\_indices(a.shape\[0\])
(array(\[0, 1, 1, 2, 2, 2, 3, 3, 3, 3\]), array(\[0, 0, 1, 0, 1, 2, 0, 1, 2, 3\]))

Copy to clipboard

Use the _k_ parameter to return the indices for the lower triangular array up to the k-th diagonal.

\>>> trili1 \= np.tril\_indices\_from(a, k\=1)
\>>> a\[trili1\]
array(\[ 0,  1,  4,  5,  6,  8,  9, 10, 11, 12, 13, 14, 15\])

Copy to clipboard

Go BackOpen In Tab

On this page