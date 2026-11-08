[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.transpose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.transpose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.transpose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.transpose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.transpose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.transpose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.transpose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.transpose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.transpose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.transpose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.transpose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.transpose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.transpose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.transpose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.transpose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.transpose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.transpose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.transpose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.transpose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.transpose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.transpose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.transpose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.transpose[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.transpose.html#numpy-ma-transpose "Link to this heading")

==========================================================================================================================================

ma.transpose(_a_, _axes\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7608-L7644)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.transpose.html#numpy.ma.transpose "Link to this definition")

Permute the dimensions of an array.

This function is exactly equivalent to [`numpy.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")
.

See also

[`numpy.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")

Equivalent function in top-level NumPy module.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= ma.arange(4).reshape((2,2))
\>>> x\[1, 1\] \= ma.masked
\>>> x
masked\_array(
  data=\[\[0, 1\],\
        \[2, --\]\],
  mask=\[\[False, False\],\
        \[False,  True\]\],
  fill\_value=999999)

Copy to clipboard

\>>> ma.transpose(x)
masked\_array(
  data=\[\[0, 2\],\
        \[1, --\]\],
  mask=\[\[False, False\],\
        \[False,  True\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page