[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.getdata.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.getdata.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.getdata.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.getdata.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.getdata.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.getdata.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.getdata.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.getdata.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.getdata.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.getdata.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.getdata.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.getdata.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.getdata.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.getdata.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.getdata.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.getdata.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.getdata.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.getdata.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.getdata.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.getdata.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.getdata[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html#numpy-ma-getdata "Link to this heading")

====================================================================================================================================

ma.getdata(_a_, _subok\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L720-L769)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html#numpy.ma.getdata "Link to this definition")

Return the data of a masked array as an ndarray.

Return the data of _a_ (if any) as an ndarray if _a_ is a `MaskedArray`, else return _a_ as an ndarray or subclass (depending on _subok_) if not.

Parameters:

**a**array\_like

Input `MaskedArray`, alternatively an ndarray or a subclass thereof.

**subok**bool

Whether to force the output to be a _pure_ ndarray (False) or to return a subclass of ndarray if appropriate (True, default).

See also

[`getmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmask.html#numpy.ma.getmask "numpy.ma.getmask")

Return the mask of a masked array, or nomask.

[`getmaskarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#numpy.ma.getmaskarray "numpy.ma.getmaskarray")

Return the mask of a masked array, or full array of False.

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
\>>> ma.getdata(a)
array(\[\[1, 2\],\
       \[3, 4\]\])

Copy to clipboard

Equivalently use the `MaskedArray` _data_ attribute.

\>>> a.data
array(\[\[1, 2\],\
       \[3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page