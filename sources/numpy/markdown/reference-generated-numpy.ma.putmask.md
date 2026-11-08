[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.putmask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.putmask.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.putmask.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.putmask.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.putmask.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.putmask.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.putmask.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.putmask.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.putmask.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.putmask.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.putmask.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.putmask.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.putmask.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.putmask.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.putmask.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.putmask.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.putmask.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.putmask.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.putmask.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.putmask.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.putmask.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.putmask.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.putmask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.putmask.html#numpy-ma-putmask "Link to this heading")

====================================================================================================================================

ma.putmask(_a_, _mask_, _values_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7552-L7605)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.putmask.html#numpy.ma.putmask "Link to this definition")

Changes elements of an array based on conditional and input values.

This is the masked array version of [`numpy.putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask")
, for details see [`numpy.putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask")
.

See also

[`numpy.putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask")

Notes

Using a masked array as _values_ will **not** transform a [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 into a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= \[\[1, 2\], \[3, 4\]\]
\>>> mask \= \[\[1, 0\], \[0, 0\]\]
\>>> x \= np.ma.array(arr, mask\=mask)
\>>> np.ma.putmask(x, x < 4, 10\*x)
\>>> x
masked\_array(
  data=\[\[--, 20\],\
        \[30, 4\]\],
  mask=\[\[ True, False\],\
        \[False, False\]\],
  fill\_value=999999)
\>>> x.data
array(\[\[10, 20\],\
       \[30,  4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page