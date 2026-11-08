[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.flatnotmasked_contiguous.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.flatnotmasked_contiguous.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.flatnotmasked\_contiguous[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy-ma-flatnotmasked-contiguous "Link to this heading")

========================================================================================================================================================================================

ma.flatnotmasked\_contiguous(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1977-L2029)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy.ma.flatnotmasked_contiguous "Link to this definition")

Find contiguous unmasked data in a masked array.

Parameters:

**a**array\_like

The input array.

Returns:

**slice\_list**list

A sorted sequence of _slice_ objects (start index, end index).

See also

[`flatnotmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#numpy.ma.flatnotmasked_edges "numpy.ma.flatnotmasked_edges")
, [`notmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#numpy.ma.notmasked_contiguous "numpy.ma.notmasked_contiguous")
, [`notmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_edges.html#numpy.ma.notmasked_edges "numpy.ma.notmasked_edges")

[`clump_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_masked.html#numpy.ma.clump_masked "numpy.ma.clump_masked")
, [`clump_unmasked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#numpy.ma.clump_unmasked "numpy.ma.clump_unmasked")

Notes

Only accepts 2-D arrays at most.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.arange(10)
\>>> np.ma.flatnotmasked\_contiguous(a)
\[slice(0, 10, None)\]

Copy to clipboard

\>>> mask \= (a < 3) | (a \> 8) | (a \== 5)
\>>> a\[mask\] \= np.ma.masked
\>>> np.array(a\[~a.mask\])
array(\[3, 4, 6, 7, 8\])

Copy to clipboard

\>>> np.ma.flatnotmasked\_contiguous(a)
\[slice(3, 5, None), slice(6, 9, None)\]
\>>> a\[:\] \= np.ma.masked
\>>> np.ma.flatnotmasked\_contiguous(a)
\[\]

Copy to clipboard

Go BackOpen In Tab

On this page