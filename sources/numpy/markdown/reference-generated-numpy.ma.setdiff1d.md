[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.setdiff1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.setdiff1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.setdiff1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.setdiff1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.setdiff1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.setdiff1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.setdiff1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.setdiff1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.setdiff1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.setdiff1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.setdiff1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.setdiff1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.setdiff1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.setdiff1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.setdiff1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.setdiff1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.setdiff1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.setdiff1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.setdiff1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.setdiff1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.setdiff1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.setdiff1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.setdiff1d[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.setdiff1d.html#numpy-ma-setdiff1d "Link to this heading")

==========================================================================================================================================

ma.setdiff1d(_ar1_, _ar2_, _assume\_unique\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1487-L1513)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.setdiff1d.html#numpy.ma.setdiff1d "Link to this definition")

Set difference of 1D arrays with unique elements.

The output is always a masked array. See [`numpy.setdiff1d`](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html#numpy.setdiff1d "numpy.setdiff1d")
 for more details.

See also

[`numpy.setdiff1d`](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html#numpy.setdiff1d "numpy.setdiff1d")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1, 2, 3, 4\], mask\=\[0, 1, 0, 1\])
\>>> np.ma.setdiff1d(x, \[1, 2\])
masked\_array(data=\[3, --\],
             mask=\[False,  True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page