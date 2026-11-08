[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_less.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_less.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_less.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_less.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_less.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_less.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_less.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_less.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_less.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_less.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_less.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_less.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_less.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_less.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_less.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_less.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_less.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_less.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_less.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_less.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_less[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#numpy-ma-masked-less "Link to this heading")

=================================================================================================================================================

ma.masked\_less(_x_, _value_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2062-L2086)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#numpy.ma.masked_less "Link to this definition")

Mask an array where less than a given value.

This function is a shortcut to `masked_where`, with _condition_ = (x < value).

See also

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.arange(4)
\>>> a
array(\[0, 1, 2, 3\])
\>>> ma.masked\_less(a, 2)
masked\_array(data=\[--, --, 2, 3\],
             mask=\[ True,  True, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page