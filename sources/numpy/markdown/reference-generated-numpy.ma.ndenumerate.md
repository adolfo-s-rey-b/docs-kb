[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.ndenumerate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.ndenumerate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.ndenumerate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.ndenumerate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.ndenumerate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.ndenumerate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.ndenumerate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.ndenumerate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.ndenumerate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.ndenumerate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.ndenumerate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.ndenumerate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.ndenumerate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.ndenumerate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.ndenumerate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.ndenumerate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.ndenumerate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.ndenumerate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.ndenumerate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.ndenumerate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.ndenumerate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.ndenumerate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.ndenumerate[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ndenumerate.html#numpy-ma-ndenumerate "Link to this heading")

================================================================================================================================================

ma.ndenumerate(_a_, _compressed\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1800-L1866)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ndenumerate.html#numpy.ma.ndenumerate "Link to this definition")

Multidimensional index iterator.

Return an iterator yielding pairs of array coordinates and values, skipping elements that are masked. With _compressed=False_, [`ma.masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
 is yielded as the value of masked elements. This behavior differs from that of [`numpy.ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")
, which yields the value of the underlying data array.

Parameters:

**a**array\_like

An array with (possibly) masked elements.

**compressed**bool, optional

If True (default), masked elements are skipped.

See also

[`numpy.ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")

Equivalent function ignoring any mask.

Notes

New in version 1.23.0.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.arange(9).reshape((3, 3))
\>>> a\[1, 0\] \= np.ma.masked
\>>> a\[1, 2\] \= np.ma.masked
\>>> a\[2, 1\] \= np.ma.masked
\>>> a
masked\_array(
  data=\[\[0, 1, 2\],\
        \[--, 4, --\],\
        \[6, --, 8\]\],
  mask=\[\[False, False, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)
\>>> for index, x in np.ma.ndenumerate(a):
...     print(index, x)
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 1) 4
(2, 0) 6
(2, 2) 8

Copy to clipboard

\>>> for index, x in np.ma.ndenumerate(a, compressed\=False):
...     print(index, x)
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 0) --
(1, 1) 4
(1, 2) --
(2, 0) 6
(2, 1) --
(2, 2) 8

Copy to clipboard

Go BackOpen In Tab

On this page