[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.mask_indices.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.mask_indices.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.mask_indices.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.mask_indices.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.mask_indices.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.mask_indices.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.mask_indices.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.mask_indices.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.mask_indices.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.mask_indices.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.mask_indices.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.mask_indices.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.mask_indices.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.mask_indices.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.mask_indices.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.mask_indices.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.mask_indices.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.mask_indices.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.mask_indices.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.mask_indices.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.mask\_indices[#](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html#numpy-mask-indices "Link to this heading")

===========================================================================================================================================

numpy.mask\_indices(_n_, _mask\_func_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L865-L931)
[#](https://numpy.org/doc/stable/reference/generated/numpy.mask_indices.html#numpy.mask_indices "Link to this definition")

Return the indices to access (n, n) arrays, given a masking function.

Assume _mask\_func_ is a function that, for a square array a of size `(n, n)` with a possible offset argument _k_, when called as `mask_func(a, k)` returns a new array with zeros in certain locations (functions like [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
 or [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
 do precisely this). Then this function returns the indices where the non-zero values would be located.

Parameters:

**n**int

The returned indices will be valid to access arrays of shape (n, n).

**mask\_func**callable

A function whose call signature is similar to that of [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
, [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
. That is, `mask_func(x, k)` returns a boolean array, shaped like _x_. _k_ is an optional argument to the function.

**k**scalar

An optional argument which is passed through to _mask\_func_. Functions like [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
, [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
 take a second argument that is interpreted as an offset.

Returns:

**indices**tuple of arrays.

The _n_ arrays of indices corresponding to the locations where `mask_func(np.ones((n, n)), k)` is True.

See also

[`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
, [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
, [`triu_indices`](https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html#numpy.triu_indices "numpy.triu_indices")
, [`tril_indices`](https://numpy.org/doc/stable/reference/generated/numpy.tril_indices.html#numpy.tril_indices "numpy.tril_indices")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

These are the indices that would allow you to access the upper triangular part of any 3x3 array:

\>>> iu \= np.mask\_indices(3, np.triu)

Copy to clipboard

For example, if _a_ is a 3x3 array:

\>>> a \= np.arange(9).reshape(3, 3)
\>>> a
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> a\[iu\]
array(\[0, 1, 2, 4, 5, 8\])

Copy to clipboard

An offset can be passed also to the masking function. This gets us the indices starting on the first diagonal right of the main one:

\>>> iu1 \= np.mask\_indices(3, np.triu, 1)

Copy to clipboard

with which we now extract only three elements:

\>>> a\[iu1\]
array(\[1, 2, 5\])

Copy to clipboard

Go BackOpen In Tab

On this page