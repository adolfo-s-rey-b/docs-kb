[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arccos.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.scimath.arccos.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arccos.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.scimath.arccos.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.scimath.arccos.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.scimath.arccos.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.scimath.arccos.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.scimath.arccos.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.scimath.arccos.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.scimath.arccos.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.scimath.arccos.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.scimath.arccos.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.scimath.arccos.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.scimath.arccos.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.scimath.arccos.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.scimath.arccos.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.scimath.arccos.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.scimath.arccos.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.scimath.arccos.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.scimath.arccos.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.scimath.arccos.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.scimath.arccos.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.scimath.arccos[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arccos.html#numpy-lib-scimath-arccos "Link to this heading")

============================================================================================================================================================

lib.scimath.arccos(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_scimath_impl.py#L494-L538)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arccos.html#numpy.lib.scimath.arccos "Link to this definition")

Compute the inverse cosine of x.

Return the “principal value” (for a description of this, see [`numpy.arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")
) of the inverse cosine of _x_. For real _x_ such that _abs(x) <= 1_, this is a real number in the closed interval \\(\[0, \\pi\]\\). Otherwise, the complex principle value is returned.

Parameters:

**x**array\_like or scalar

The value(s) whose arccos is (are) required.

Returns:

**out**ndarray or scalar

The inverse cosine(s) of the _x_ value(s). If _x_ was a scalar, so is _out_, otherwise an array object is returned.

See also

[`numpy.arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")

Notes

For an arccos() that returns `NAN` when real _x_ is not in the interval `[-1,1]`, use [`numpy.arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.set\_printoptions(precision\=4)

Copy to clipboard

\>>> np.emath.arccos(1) \# a scalar is returned
0.0

Copy to clipboard

\>>> np.emath.arccos(\[1,2\])
array(\[0.-0.j   , 0.-1.317j\])

Copy to clipboard

Go BackOpen In Tab

On this page