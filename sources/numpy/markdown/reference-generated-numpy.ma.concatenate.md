[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.concatenate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.concatenate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.concatenate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.concatenate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.concatenate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.concatenate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.concatenate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.concatenate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.concatenate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.concatenate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.concatenate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.concatenate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.concatenate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.concatenate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.concatenate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.concatenate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.concatenate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.concatenate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.concatenate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.concatenate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.concatenate[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html#numpy-ma-concatenate "Link to this heading")

================================================================================================================================================

ma.concatenate(_arrays_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7314-L7372)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html#numpy.ma.concatenate "Link to this definition")

Concatenate a sequence of arrays along the given axis.

Parameters:

**arrays**sequence of array\_like

The arrays must have the same shape, except in the dimension corresponding to _axis_ (the first, by default).

**axis**int, optional

The axis along which the arrays will be joined. Default is 0.

Returns:

**result**MaskedArray

The concatenated array with any masked entries preserved.

See also

[`numpy.concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Equivalent function in the top-level NumPy module.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= ma.arange(3)
\>>> a\[1\] \= ma.masked
\>>> b \= ma.arange(2, 5)
\>>> a
masked\_array(data=\[0, --, 2\],
             mask=\[False,  True, False\],
       fill\_value=999999)
\>>> b
masked\_array(data=\[2, 3, 4\],
             mask=False,
       fill\_value=999999)
\>>> ma.concatenate(\[a, b\])
masked\_array(data=\[0, --, 2, 2, 3, 4\],
             mask=\[False,  True, False, False, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page