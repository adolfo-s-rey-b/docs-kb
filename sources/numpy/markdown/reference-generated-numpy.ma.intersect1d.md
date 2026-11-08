[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.intersect1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.intersect1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.intersect1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.intersect1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.intersect1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.intersect1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.intersect1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.intersect1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.intersect1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.intersect1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.intersect1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.intersect1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.intersect1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.intersect1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.intersect1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.intersect1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.intersect1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.intersect1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.intersect1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.intersect1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.intersect1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.intersect1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.intersect1d[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.intersect1d.html#numpy-ma-intersect1d "Link to this heading")

================================================================================================================================================

ma.intersect1d(_ar1_, _ar2_, _assume\_unique\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1317-L1347)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.intersect1d.html#numpy.ma.intersect1d "Link to this definition")

Returns the unique elements common to both arrays.

Masked values are considered equal one to the other. The output is always a masked array.

See [`numpy.intersect1d`](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html#numpy.intersect1d "numpy.intersect1d")
 for more details.

See also

[`numpy.intersect1d`](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html#numpy.intersect1d "numpy.intersect1d")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1, 3, 3, 3\], mask\=\[0, 0, 0, 1\])
\>>> y \= np.ma.array(\[3, 1, 1, 1\], mask\=\[0, 0, 0, 1\])
\>>> np.ma.intersect1d(x, y)
masked\_array(data=\[1, 3, --\],
             mask=\[False, False,  True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page