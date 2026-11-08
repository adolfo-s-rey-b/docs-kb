[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.ediff1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.ediff1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.ediff1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.ediff1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.ediff1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.ediff1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.ediff1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.ediff1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.ediff1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.ediff1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.ediff1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.ediff1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.ediff1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.ediff1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.ediff1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.ediff1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.ediff1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.ediff1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.ediff1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.ediff1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.ediff1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.ediff1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.ediff1d[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ediff1d.html#numpy-ma-ediff1d "Link to this heading")

====================================================================================================================================

ma.ediff1d(_arr_, _to\_end\=None_, _to\_begin\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1229-L1264)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ediff1d.html#numpy.ma.ediff1d "Link to this definition")

Compute the differences between consecutive elements of an array.

This function is the equivalent of [`numpy.ediff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d "numpy.ediff1d")
 that takes masked values into account, see [`numpy.ediff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d "numpy.ediff1d")
 for details.

See also

[`numpy.ediff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d "numpy.ediff1d")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.ma.array(\[1, 2, 4, 7, 0\])
\>>> np.ma.ediff1d(arr)
masked\_array(data=\[ 1,  2,  3, -7\],
             mask=False,
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page