[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.flatnotmasked_edges.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.flatnotmasked_edges.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.flatnotmasked_edges.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.flatnotmasked_edges.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.flatnotmasked_edges.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.flatnotmasked_edges.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.flatnotmasked_edges.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.flatnotmasked\_edges[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#numpy-ma-flatnotmasked-edges "Link to this heading")

=========================================================================================================================================================================

ma.flatnotmasked\_edges(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1869-L1922)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#numpy.ma.flatnotmasked_edges "Link to this definition")

Find the indices of the first and last unmasked values.

Expects a 1-D [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, returns None if all values are masked.

Parameters:

**a**array\_like

Input 1-D [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")

Returns:

**edges**ndarray or None

The indices of first and last non-masked value in the array. Returns None if all values are masked.

See also

[`flatnotmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy.ma.flatnotmasked_contiguous "numpy.ma.flatnotmasked_contiguous")
, [`notmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#numpy.ma.notmasked_contiguous "numpy.ma.notmasked_contiguous")
, [`notmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_edges.html#numpy.ma.notmasked_edges "numpy.ma.notmasked_edges")

[`clump_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_masked.html#numpy.ma.clump_masked "numpy.ma.clump_masked")
, [`clump_unmasked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#numpy.ma.clump_unmasked "numpy.ma.clump_unmasked")

Notes

Only accepts 1-D arrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.arange(10)
\>>> np.ma.flatnotmasked\_edges(a)
array(\[0, 9\])

Copy to clipboard

\>>> mask \= (a < 3) | (a \> 8) | (a \== 5)
\>>> a\[mask\] \= np.ma.masked
\>>> np.array(a\[~a.mask\])
array(\[3, 4, 6, 7, 8\])

Copy to clipboard

\>>> np.ma.flatnotmasked\_edges(a)
array(\[3, 8\])

Copy to clipboard

\>>> a\[:\] \= np.ma.masked
\>>> print(np.ma.flatnotmasked\_edges(a))
None

Copy to clipboard

Go BackOpen In Tab

On this page