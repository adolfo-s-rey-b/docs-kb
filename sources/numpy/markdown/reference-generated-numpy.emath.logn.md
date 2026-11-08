[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.emath.logn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.emath.logn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.emath.logn.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.emath.logn.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.emath.logn.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.emath.logn.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.emath.logn.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.emath.logn.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.emath.logn.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.emath.logn.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.emath.logn.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.emath.logn.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.emath.logn.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.emath.logn.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.emath.logn.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.emath.logn.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.emath.logn.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.emath.logn.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.emath.logn.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.emath.logn.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.emath.logn.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.emath.logn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.emath.logn[#](https://numpy.org/doc/stable/reference/generated/numpy.emath.logn.html#numpy-emath-logn "Link to this heading")

====================================================================================================================================

emath.logn(_n_, _x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_scimath_impl.py#L347-L382)
[#](https://numpy.org/doc/stable/reference/generated/numpy.emath.logn.html#numpy.emath.logn "Link to this definition")

Take log base n of x.

If _x_ contains negative inputs, the answer is computed and returned in the complex domain.

Parameters:

**n**array\_like

The integer base(s) in which the log is taken.

**x**array\_like

The value(s) whose log base _n_ is (are) required.

Returns:

**out**ndarray or scalar

The log base _n_ of the _x_ value(s). If _x_ was a scalar, so is _out_, otherwise an array is returned.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.set\_printoptions(precision\=4)

Copy to clipboard

\>>> np.emath.logn(2, \[4, 8\])
array(\[2., 3.\])
\>>> np.emath.logn(2, \[\-4, \-8, 8\])
array(\[2.+4.5324j, 3.+4.5324j, 3.+0.j    \])

Copy to clipboard

Go BackOpen In Tab

On this page