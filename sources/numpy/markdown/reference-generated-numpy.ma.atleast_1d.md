[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.atleast_1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.atleast_1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.atleast_1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.atleast_1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.atleast_1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.atleast_1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.atleast_1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.atleast_1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.atleast_1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.atleast_1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.atleast_1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.atleast_1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.atleast_1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.atleast_1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.atleast_1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.atleast_1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.atleast_1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.atleast_1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.atleast_1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.atleast_1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.atleast\_1d[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_1d.html#numpy-ma-atleast-1d "Link to this heading")

==============================================================================================================================================

ma.atleast\_1d(_\*arys_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/shape_base.py#L19-L71)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_1d.html#numpy.ma.atleast_1d "Link to this definition")

Convert inputs to arrays with at least one dimension.

Scalar inputs are converted to 1-dimensional arrays, whilst higher-dimensional inputs are preserved.

Parameters:

**arys1, arys2, …**array\_like

One or more input arrays.

Returns:

**ret**ndarray

An array, or tuple of arrays, each with `a.ndim >= 1`. Copies are made only if necessary.

See also

[`atleast_2d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d")
, [`atleast_3d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d "numpy.atleast_3d")

Notes

The function is applied to both the `_data` and the `_mask`, if any.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.atleast\_1d(1.0)
array(\[1.\])

Copy to clipboard

\>>> x \= np.arange(9.0).reshape(3,3)
\>>> np.atleast\_1d(x)
array(\[\[0., 1., 2.\],\
       \[3., 4., 5.\],\
       \[6., 7., 8.\]\])
\>>> np.atleast\_1d(x) is x
True

Copy to clipboard

\>>> np.atleast\_1d(1, \[3, 4\])
(array(\[1\]), array(\[3, 4\]))

Copy to clipboard

Go BackOpen In Tab

On this page