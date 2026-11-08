[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fix.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fix.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fix.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fix.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fix.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fix.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fix.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fix.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fix.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fix.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fix.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fix.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fix.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fix.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fix.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fix.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fix.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fix.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fix.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fix.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fix.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fix[#](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#numpy-fix "Link to this heading")

===============================================================================================================

numpy.fix(_x_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_ufunclike_impl.py#L18-L72)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#numpy.fix "Link to this definition")

Round to nearest integer towards zero.

Deprecated since version 2.5: [`numpy.fix`](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#numpy.fix "numpy.fix")
 is deprecated. Use [`numpy.trunc`](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html#numpy.trunc "numpy.trunc")
 instead, which is faster and follows the Array API standard.

Round an array of floats element-wise to nearest integer towards zero. The rounded values have the same data-type as the input.

Parameters:

**x**array\_like

An array to be rounded

**out**ndarray, optional

A location into which the result is stored. If provided, it must have a shape that the input broadcasts to. If not provided or None, a freshly-allocated array is returned.

Returns:

**out**ndarray of floats

An array with the same dimensions and data-type as the input. If second argument is not supplied then a new array is returned with the rounded values.

If a second argument is supplied the result is stored there. The return value `out` is then a reference to that array.

See also

[`rint`](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#numpy.rint "numpy.rint")
, [`trunc`](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html#numpy.trunc "numpy.trunc")
, [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")
, [`ceil`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil")

[`around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")

Round to given number of decimals

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fix(3.14)
3.0
\>>> np.fix(3)
3
\>>> np.fix(\[2.1, 2.9, \-2.1, \-2.9\])
array(\[ 2.,  2., -2., -2.\])

Copy to clipboard

Go BackOpen In Tab

On this page