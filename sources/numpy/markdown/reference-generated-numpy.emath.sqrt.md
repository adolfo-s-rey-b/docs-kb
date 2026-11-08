[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.emath.sqrt.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.emath.sqrt.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.emath.sqrt.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.emath.sqrt.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.emath.sqrt.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.emath.sqrt.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.emath.sqrt.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.emath.sqrt.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.emath.sqrt.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.emath.sqrt.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.emath.sqrt.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.emath.sqrt.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.emath.sqrt.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.emath.sqrt.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.emath.sqrt.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.emath.sqrt.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.emath.sqrt.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.emath.sqrt.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.emath.sqrt.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.emath.sqrt.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.emath.sqrt[#](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html#numpy-emath-sqrt "Link to this heading")

====================================================================================================================================

emath.sqrt(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_scimath_impl.py#L185-L238)
[#](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html#numpy.emath.sqrt "Link to this definition")

Compute the square root of x.

For negative input elements, a complex value is returned (unlike [`numpy.sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
 which returns NaN).

Parameters:

**x**array\_like

The input value(s).

Returns:

**out**ndarray or scalar

The square root of _x_. If _x_ was a scalar, so is _out_, otherwise an array is returned.

See also

[`numpy.sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")

Examples

Try it in your browser!

For real, non-negative inputs this works just like [`numpy.sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
:

\>>> import numpy as np

Copy to clipboard

\>>> np.emath.sqrt(1)
1.0
\>>> np.emath.sqrt(\[1, 4\])
array(\[1.,  2.\])

Copy to clipboard

But it automatically handles negative inputs:

\>>> np.emath.sqrt(\-1)
1j
\>>> np.emath.sqrt(\[\-1,4\])
array(\[0.+1.j, 2.+0.j\])

Copy to clipboard

Different results are expected because: floating point 0.0 and -0.0 are distinct.

For more control, explicitly use complex() as follows:

\>>> np.emath.sqrt(complex(\-4.0, 0.0))
2j
\>>> np.emath.sqrt(complex(\-4.0, \-0.0))
\-2j

Copy to clipboard

Go BackOpen In Tab

On this page