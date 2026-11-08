[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.clump_unmasked.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.clump_unmasked.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.clump_unmasked.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.clump_unmasked.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.clump_unmasked.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.clump_unmasked.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.clump_unmasked.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.clump_unmasked.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.clump_unmasked.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.clump_unmasked.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.clump_unmasked.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.clump_unmasked.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.clump_unmasked.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.clump_unmasked.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.clump_unmasked.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.clump_unmasked.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.clump_unmasked.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.clump_unmasked.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.clump_unmasked.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.clump_unmasked.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.clump\_unmasked[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#numpy-ma-clump-unmasked "Link to this heading")

==========================================================================================================================================================

ma.clump\_unmasked(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L2139-L2172)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#numpy.ma.clump_unmasked "Link to this definition")

Return list of slices corresponding to the unmasked clumps of a 1-D array. (A “clump” is defined as a contiguous region of the array).

Parameters:

**a**ndarray

A one-dimensional masked array.

Returns:

**slices**list of slice

The list of slices, one for each continuous region of unmasked elements in _a_.

See also

[`flatnotmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#numpy.ma.flatnotmasked_edges "numpy.ma.flatnotmasked_edges")
, [`flatnotmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy.ma.flatnotmasked_contiguous "numpy.ma.flatnotmasked_contiguous")
, [`notmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_edges.html#numpy.ma.notmasked_edges "numpy.ma.notmasked_edges")

[`notmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#numpy.ma.notmasked_contiguous "numpy.ma.notmasked_contiguous")
, [`clump_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_masked.html#numpy.ma.clump_masked "numpy.ma.clump_masked")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.masked\_array(np.arange(10))
\>>> a\[\[0, 1, 2, 6, 8, 9\]\] \= np.ma.masked
\>>> np.ma.clump\_unmasked(a)
\[slice(3, 6, None), slice(7, 8, None)\]

Copy to clipboard

Go BackOpen In Tab

On this page