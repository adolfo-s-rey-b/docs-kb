[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.atleast_2d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.atleast_2d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.atleast_2d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.atleast_2d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.atleast_2d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.atleast_2d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.atleast_2d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.atleast_2d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.atleast_2d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.atleast_2d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.atleast_2d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.atleast_2d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.atleast_2d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.atleast_2d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.atleast_2d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.atleast_2d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.atleast_2d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.atleast_2d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.atleast_2d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.atleast_2d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.atleast\_2d[#](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy-atleast-2d "Link to this heading")

=====================================================================================================================================

numpy.atleast\_2d(_\*arys_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/shape_base.py#L78-L130)
[#](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "Link to this definition")

View inputs as arrays with at least two dimensions.

Parameters:

**arys1, arys2, …**array\_like

One or more array-like sequences. Non-array inputs are converted to arrays. Arrays that already have two or more dimensions are preserved.

Returns:

**res, res2, …**ndarray

An array, or tuple of arrays, each with `a.ndim >= 2`. Copies are avoided where possible, and views with two or more dimensions are returned.

See also

[`atleast_1d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d "numpy.atleast_1d")
, [`atleast_3d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d "numpy.atleast_3d")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.atleast\_2d(3.0)
array(\[\[3.\]\])

Copy to clipboard

\>>> x \= np.arange(3.0)
\>>> np.atleast\_2d(x)
array(\[\[0., 1., 2.\]\])
\>>> np.atleast\_2d(x).base is x
True

Copy to clipboard

\>>> np.atleast\_2d(1, \[1, 2\], \[\[1, 2\]\])
(array(\[\[1\]\]), array(\[\[1, 2\]\]), array(\[\[1, 2\]\]))

Copy to clipboard

Go BackOpen In Tab

On this page