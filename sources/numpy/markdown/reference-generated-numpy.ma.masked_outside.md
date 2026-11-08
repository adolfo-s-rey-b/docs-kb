[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_outside.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_outside.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_outside.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_outside.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_outside.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_outside.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_outside.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_outside.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_outside.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_outside.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_outside.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_outside.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_outside.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_outside.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_outside.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_outside.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_outside.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_outside.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_outside.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_outside.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_outside[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html#numpy-ma-masked-outside "Link to this heading")

==========================================================================================================================================================

ma.masked\_outside(_x_, _v1_, _v2_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2217-L2255)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html#numpy.ma.masked_outside "Link to this definition")

Mask an array outside a given interval.

Shortcut to `masked_where`, where _condition_ is True for _x_ outside the interval \[v1,v2\] (x < v1)|(x > v2). The boundaries _v1_ and _v2_ can be given in either order.

See also

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

Notes

The array _x_ is prefilled with its filling value.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= \[0.31, 1.2, 0.01, 0.2, \-0.4, \-1.1\]
\>>> ma.masked\_outside(x, \-0.3, 0.3)
masked\_array(data=\[--, --, 0.01, 0.2, --, --\],
             mask=\[ True,  True, False, False,  True,  True\],
       fill\_value=1e+20)

Copy to clipboard

The order of _v1_ and _v2_ doesn’t matter.

\>>> ma.masked\_outside(x, 0.3, \-0.3)
masked\_array(data=\[--, --, 0.01, 0.2, --, --\],
             mask=\[ True,  True, False, False,  True,  True\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page