[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.resize.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.resize.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.resize.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.resize.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.resize.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.resize.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.resize.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.resize.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.resize.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.resize.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.resize.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.resize.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.resize.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.resize.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.resize.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.resize.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.resize.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.resize.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.resize.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.resize.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.resize[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html#numpy-ma-resize "Link to this heading")

=================================================================================================================================

ma.resize(_x_, _new\_shape_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7697-L7759)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html#numpy.ma.resize "Link to this definition")

Return a new masked array with the specified size and shape.

This is the masked equivalent of the [`numpy.resize`](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "numpy.resize")
 function. The new array is filled with repeated copies of _x_ (in the order that the data are stored in memory). If _x_ is masked, the new array will be masked, and the new mask will be a repetition of the old one.

See also

[`numpy.resize`](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "numpy.resize")

Equivalent function in the top level NumPy module.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= ma.array(\[\[1, 2\] ,\[3, 4\]\])
\>>> a\[0, 1\] \= ma.masked
\>>> a
masked\_array(
  data=\[\[1, --\],\
        \[3, 4\]\],
  mask=\[\[False,  True\],\
        \[False, False\]\],
  fill\_value=999999)
\>>> np.resize(a, (3, 3))
masked\_array(
  data=\[\[1, 2, 3\],\
        \[4, 1, 2\],\
        \[3, 4, 1\]\],
  mask=False,
  fill\_value=999999)
\>>> ma.resize(a, (3, 3))
masked\_array(
  data=\[\[1, --, 3\],\
        \[4, 1, --\],\
        \[3, 4, 1\]\],
  mask=\[\[False,  True, False\],\
        \[False, False,  True\],\
        \[False, False, False\]\],
  fill\_value=999999)

Copy to clipboard

A MaskedArray is always returned, regardless of the input type.

\>>> a \= np.array(\[\[1, 2\] ,\[3, 4\]\])
\>>> ma.resize(a, (3, 3))
masked\_array(
  data=\[\[1, 2, 3\],\
        \[4, 1, 2\],\
        \[3, 4, 1\]\],
  mask=False,
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page