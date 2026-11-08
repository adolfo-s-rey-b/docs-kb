[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.notmasked_contiguous.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.notmasked_contiguous.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.notmasked_contiguous.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.notmasked_contiguous.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.notmasked_contiguous.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.notmasked_contiguous.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.notmasked_contiguous.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.notmasked\_contiguous[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#numpy-ma-notmasked-contiguous "Link to this heading")

============================================================================================================================================================================

ma.notmasked\_contiguous(_a_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L2032-L2107)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#numpy.ma.notmasked_contiguous "Link to this definition")

Find contiguous unmasked data in a masked array along the given axis.

Parameters:

**a**array\_like

The input array.

**axis**int, optional

Axis along which to perform the operation. If None (default), applies to a flattened version of the array, and this is the same as [`flatnotmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy.ma.flatnotmasked_contiguous "numpy.ma.flatnotmasked_contiguous")
.

Returns:

**endpoints**list

A list of slices (start and end indexes) of unmasked indexes in the array.

If the input is 2d and axis is specified, the result is a list of lists.

See also

[`flatnotmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#numpy.ma.flatnotmasked_edges "numpy.ma.flatnotmasked_edges")
, [`flatnotmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy.ma.flatnotmasked_contiguous "numpy.ma.flatnotmasked_contiguous")
, [`notmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_edges.html#numpy.ma.notmasked_edges "numpy.ma.notmasked_edges")

[`clump_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_masked.html#numpy.ma.clump_masked "numpy.ma.clump_masked")
, [`clump_unmasked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#numpy.ma.clump_unmasked "numpy.ma.clump_unmasked")

Notes

Only accepts 2-D arrays at most.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(12).reshape((3, 4))
\>>> mask \= np.zeros\_like(a)
\>>> mask\[1:, :\-1\] \= 1; mask\[0, 1\] \= 1; mask\[\-1, 0\] \= 0
\>>> ma \= np.ma.array(a, mask\=mask)
\>>> ma
masked\_array(
  data=\[\[0, --, 2, 3\],\
        \[--, --, --, 7\],\
        \[8, --, --, 11\]\],
  mask=\[\[False,  True, False, False\],\
        \[ True,  True,  True, False\],\
        \[False,  True,  True, False\]\],
  fill\_value=999999)
\>>> np.array(ma\[~ma.mask\])
array(\[ 0,  2,  3,  7, 8, 11\])

Copy to clipboard

\>>> np.ma.notmasked\_contiguous(ma)
\[slice(0, 1, None), slice(2, 4, None), slice(7, 9, None), slice(11, 12, None)\]

Copy to clipboard

\>>> np.ma.notmasked\_contiguous(ma, axis\=0)
\[\[slice(0, 1, None), slice(2, 3, None)\], \[\], \[slice(0, 1, None)\], \[slice(0, 3, None)\]\]

Copy to clipboard

\>>> np.ma.notmasked\_contiguous(ma, axis\=1)
\[\[slice(0, 1, None), slice(2, 4, None)\], \[slice(3, 4, None)\], \[slice(0, 1, None), slice(3, 4, None)\]\]

Copy to clipboard

Go BackOpen In Tab

On this page