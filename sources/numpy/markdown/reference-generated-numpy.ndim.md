[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndim.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndim.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndim.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndim.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndim.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndim.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndim.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndim.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndim.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndim.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndim.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndim.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndim.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndim.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndim.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndim.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndim.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndim.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndim.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndim.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndim[#](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy-ndim "Link to this heading")

==================================================================================================================

numpy.ndim(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3520-L3556)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "Link to this definition")

Return the number of dimensions of an array.

Parameters:

**a**array\_like

Input array. If it is not already an ndarray, a conversion is attempted.

Returns:

**number\_of\_dimensions**int

The number of dimensions in _a_. Scalars are zero-dimensional.

See also

[`ndarray.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html#numpy.ndarray.ndim "numpy.ndarray.ndim")

equivalent method

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

dimensions of array

[`ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")

dimensions of array

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.ndim(\[\[1,2,3\],\[4,5,6\]\])
2
\>>> np.ndim(np.array(\[\[1,2,3\],\[4,5,6\]\]))
2
\>>> np.ndim(1)
0

Copy to clipboard

Go BackOpen In Tab

On this page