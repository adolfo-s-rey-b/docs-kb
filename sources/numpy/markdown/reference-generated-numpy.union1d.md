[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.union1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.union1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.union1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.union1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.union1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.union1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.union1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.union1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.union1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.union1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.union1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.union1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.union1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.union1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.union1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.union1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.union1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.union1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.union1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.union1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.union1d[#](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html#numpy-union1d "Link to this heading")

===========================================================================================================================

numpy.union1d(_ar1_, _ar2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L1083-L1113)
[#](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html#numpy.union1d "Link to this definition")

Find the union of two arrays.

Return the unique, sorted array of values that are in either of the two input arrays.

Parameters:

**ar1, ar2**array\_like

Input arrays. They are flattened if they are not already 1D.

Returns:

**union1d**ndarray

Unique, sorted union of the input arrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.union1d(\[\-1, 0, 1\], \[\-2, 0, 2\])
array(\[-2, -1,  0,  1,  2\])

Copy to clipboard

To find the union of more than two arrays, use functools.reduce:

\>>> from functools import reduce
\>>> reduce(np.union1d, (\[1, 3, 4, 3\], \[3, 1, 2, 1\], \[6, 3, 4, 2\]))
array(\[1, 2, 3, 4, 6\])

Copy to clipboard

Go BackOpen In Tab

On this page