[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.getmaskarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.getmaskarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.getmaskarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.getmaskarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.getmaskarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.getmaskarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.getmaskarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.getmaskarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.getmaskarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.getmaskarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.getmaskarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.getmaskarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.getmaskarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.getmaskarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.getmaskarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.getmaskarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.getmaskarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.getmaskarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.getmaskarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.getmaskarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.getmaskarray[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#numpy-ma-getmaskarray "Link to this heading")

===================================================================================================================================================

ma.getmaskarray(_arr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1474-L1525)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#numpy.ma.getmaskarray "Link to this definition")

Return the mask of a masked array, or full boolean array of False.

Return the mask of _arr_ as an ndarray if _arr_ is a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 and the mask is not [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
, else return a full boolean array of False of the same shape as _arr_.

Parameters:

**arr**array\_like

Input [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 for which the mask is required.

See also

[`getmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmask.html#numpy.ma.getmask "numpy.ma.getmask")

Return the mask of a masked array, or nomask.

[`getdata`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html#numpy.ma.getdata "numpy.ma.getdata")

Return the data of a masked array as an ndarray.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= ma.masked\_equal(\[\[1,2\],\[3,4\]\], 2)
\>>> a
masked\_array(
  data=\[\[1, --\],\
        \[3, 4\]\],
  mask=\[\[False,  True\],\
        \[False, False\]\],
  fill\_value=2)
\>>> ma.getmaskarray(a)
array(\[\[False,  True\],\
       \[False, False\]\])

Copy to clipboard

Result when mask == `nomask`

\>>> b \= ma.masked\_array(\[\[1,2\],\[3,4\]\])
\>>> b
masked\_array(
  data=\[\[1, 2\],\
        \[3, 4\]\],
  mask=False,
  fill\_value=999999)
\>>> ma.getmaskarray(b)
array(\[\[False, False\],\
       \[False, False\]\])

Copy to clipboard

Go BackOpen In Tab

On this page