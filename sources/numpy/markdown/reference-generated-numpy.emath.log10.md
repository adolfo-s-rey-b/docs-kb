[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.emath.log10.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.emath.log10.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.emath.log10.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.emath.log10.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.emath.log10.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.emath.log10.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.emath.log10.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.emath.log10.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.emath.log10.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.emath.log10.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.emath.log10.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.emath.log10.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.emath.log10.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.emath.log10.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.emath.log10.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.emath.log10.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.emath.log10.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.emath.log10.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.emath.log10.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.emath.log10.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.emath.log10.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.emath.log10.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.emath.log10[#](https://numpy.org/doc/stable/reference/generated/numpy.emath.log10.html#numpy-emath-log10 "Link to this heading")

=======================================================================================================================================

emath.log10(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_scimath_impl.py#L291-L340)
[#](https://numpy.org/doc/stable/reference/generated/numpy.emath.log10.html#numpy.emath.log10 "Link to this definition")

Compute the logarithm base 10 of _x_.

Return the “principal value” (for a description of this, see [`numpy.log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
) of \\(log\_{10}(x)\\). For real _x > 0_, this is a real number (`log10(0)` returns `-inf` and `log10(np.inf)` returns `inf`). Otherwise, the complex principle value is returned.

Parameters:

**x**array\_like or scalar

The value(s) whose log base 10 is (are) required.

Returns:

**out**ndarray or scalar

The log base 10 of the _x_ value(s). If _x_ was a scalar, so is _out_, otherwise an array object is returned.

See also

[`numpy.log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")

Notes

For a log10() that returns `NAN` when real _x < 0_, use [`numpy.log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
 (note, however, that otherwise [`numpy.log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
 and this [`log10`](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
 are identical, i.e., both return `-inf` for _x = 0_, `inf` for _x = inf_, and, notably, the complex principle value if `x.imag != 0`).

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

(We set the printing precision so the example can be auto-tested)

\>>> np.set\_printoptions(precision\=4)

Copy to clipboard

\>>> np.emath.log10(10\*\*1)
1.0

Copy to clipboard

\>>> np.emath.log10(\[\-10\*\*1, \-10\*\*2, 10\*\*2\])
array(\[1.+1.3644j, 2.+1.3644j, 2.+0.j    \])

Copy to clipboard

Go BackOpen In Tab

On this page