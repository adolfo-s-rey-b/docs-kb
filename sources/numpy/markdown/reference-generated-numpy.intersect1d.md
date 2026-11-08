[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.intersect1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.intersect1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.intersect1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.intersect1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.intersect1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.intersect1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.intersect1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.intersect1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.intersect1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.intersect1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.intersect1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.intersect1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.intersect1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.intersect1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.intersect1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.intersect1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.intersect1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.intersect1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.intersect1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.intersect1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.intersect1d[#](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html#numpy-intersect1d "Link to this heading")

=======================================================================================================================================

numpy.intersect1d(_ar1_, _ar2_, _assume\_unique\=False_, _return\_indices\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L666-L755)
[#](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html#numpy.intersect1d "Link to this definition")

Find the intersection of two arrays.

Return the sorted, unique values that are in both of the input arrays.

Parameters:

**ar1, ar2**array\_like

Input arrays. Will be flattened if not already 1D.

**assume\_unique**bool

If True, the input arrays are both assumed to be unique, which can speed up the calculation. If True but `ar1` or `ar2` are not unique, incorrect results and out-of-bounds indices could result. Default is False.

**return\_indices**bool

If True, the indices which correspond to the intersection of the two arrays are returned. The first instance of a value is used if there are multiple. Default is False.

Returns:

**intersect1d**ndarray

Sorted 1D array of common and unique elements.

**comm1**ndarray

The indices of the first occurrences of the common values in _ar1_. Only provided if _return\_indices_ is True.

**comm2**ndarray

The indices of the first occurrences of the common values in _ar2_. Only provided if _return\_indices_ is True.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.intersect1d(\[1, 3, 4, 3\], \[3, 1, 2, 1\])
array(\[1, 3\])

Copy to clipboard

To intersect more than two arrays, use functools.reduce:

\>>> from functools import reduce
\>>> reduce(np.intersect1d, (\[1, 3, 4, 3\], \[3, 1, 2, 1\], \[6, 3, 4, 2\]))
array(\[3\])

Copy to clipboard

To return the indices of the values common to the input arrays along with the intersected values:

\>>> x \= np.array(\[1, 1, 2, 3, 4\])
\>>> y \= np.array(\[2, 1, 4, 6\])
\>>> xy, x\_ind, y\_ind \= np.intersect1d(x, y, return\_indices\=True)
\>>> x\_ind, y\_ind
(array(\[0, 2, 4\]), array(\[1, 0, 2\]))
\>>> xy, x\[x\_ind\], y\[y\_ind\]
(array(\[1, 2, 4\]), array(\[1, 2, 4\]), array(\[1, 2, 4\]))

Copy to clipboard

Go BackOpen In Tab

On this page