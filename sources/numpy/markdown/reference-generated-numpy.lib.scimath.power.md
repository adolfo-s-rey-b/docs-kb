[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.power.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.scimath.power.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.power.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.scimath.power.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.scimath.power.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.scimath.power.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.scimath.power.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.scimath.power.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.scimath.power.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.scimath.power.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.scimath.power.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.scimath.power.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.scimath.power.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.scimath.power.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.scimath.power.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.scimath.power.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.scimath.power.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.scimath.power.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.scimath.power.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.scimath.power.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.scimath.power.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.scimath.power.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.scimath.power[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.power.html#numpy-lib-scimath-power "Link to this heading")

=========================================================================================================================================================

lib.scimath.power(_x_, _p_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_scimath_impl.py#L439-L491)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.power.html#numpy.lib.scimath.power "Link to this definition")

Return x to the power p, (x\*\*p).

If _x_ contains negative values, the output is converted to the complex domain.

Parameters:

**x**array\_like

The input value(s).

**p**array\_like of ints

The power(s) to which _x_ is raised. If _x_ contains multiple values, _p_ has to either be a scalar, or contain the same number of values as _x_. In the latter case, the result is `x[0]**p[0], x[1]**p[1], ...`.

Returns:

**out**ndarray or scalar

The result of `x**p`. If _x_ and _p_ are scalars, so is _out_, otherwise an array is returned.

See also

[`numpy.power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.set\_printoptions(precision\=4)

Copy to clipboard

\>>> np.emath.power(2, 2)
4

Copy to clipboard

\>>> np.emath.power(\[2, 4\], 2)
array(\[ 4, 16\])

Copy to clipboard

\>>> np.emath.power(\[2, 4\], \-2)
array(\[0.25  ,  0.0625\])

Copy to clipboard

\>>> np.emath.power(\[\-2, 4\], 2)
array(\[ 4.-0.j, 16.+0.j\])

Copy to clipboard

\>>> np.emath.power(\[2, 4\], \[2, 4\])
array(\[ 4, 256\])

Copy to clipboard

Go BackOpen In Tab

On this page