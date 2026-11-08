[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arctanh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.scimath.arctanh.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arctanh.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.scimath.arctanh.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.scimath.arctanh.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.scimath.arctanh.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.scimath.arctanh.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.scimath.arctanh.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.scimath.arctanh.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.scimath.arctanh.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.scimath.arctanh.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.scimath.arctanh.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.scimath.arctanh.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.scimath.arctanh.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.scimath.arctanh.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.scimath.arctanh.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.scimath.arctanh.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.scimath.arctanh.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.scimath.arctanh.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.scimath.arctanh.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.scimath.arctanh.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.scimath.arctanh.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.scimath.arctanh[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arctanh.html#numpy-lib-scimath-arctanh "Link to this heading")

===============================================================================================================================================================

lib.scimath.arctanh(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_scimath_impl.py#L589-L642)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.scimath.arctanh.html#numpy.lib.scimath.arctanh "Link to this definition")

Compute the inverse hyperbolic tangent of _x_.

Return the “principal value” (for a description of this, see [`numpy.arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")
) of `arctanh(x)`. For real _x_ such that `abs(x) < 1`, this is a real number. If _abs(x) > 1_, or if _x_ is complex, the result is complex. Finally, _x = 1_ returns\`\`inf\`\` and `x=-1` returns `-inf`.

Parameters:

**x**array\_like

The value(s) whose arctanh is (are) required.

Returns:

**out**ndarray or scalar

The inverse hyperbolic tangent(s) of the _x_ value(s). If _x_ was a scalar so is _out_, otherwise an array is returned.

See also

[`numpy.arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")

Notes

For an arctanh() that returns `NAN` when real _x_ is not in the interval `(-1,1)`, use [`numpy.arctanh`](https://numpy.org/doc/stable/reference/generated/numpy.arctanh.html#numpy.arctanh "numpy.arctanh")
 (this latter, however, does return +/-inf for `x = +/-1`).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.set\_printoptions(precision\=4)

Copy to clipboard

\>>> np.emath.arctanh(0.5)
0.5493061443340549

Copy to clipboard

\>>> import warnings
\>>> with warnings.catch\_warnings():
...     warnings.simplefilter('ignore', RuntimeWarning)
...     np.emath.arctanh(np.eye(2))
array(\[\[inf,  0.\],\
       \[ 0., inf\]\])
\>>> np.emath.arctanh(\[1j\])
array(\[0.+0.7854j\])

Copy to clipboard

Go BackOpen In Tab

On this page