[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.unique.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.unique.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.unique.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.unique.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.unique.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.unique.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.unique.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.unique.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.unique.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.unique.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.unique.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.unique.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.unique.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.unique.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.unique.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.unique.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.unique.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.unique.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.unique.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.unique.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.unique.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.unique.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.unique[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.unique.html#numpy-ma-unique "Link to this heading")

=================================================================================================================================

ma.unique(_ar1_, _return\_index\=False_, _return\_inverse\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1267-L1314)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.unique.html#numpy.ma.unique "Link to this definition")

Finds the unique elements of an array.

Masked values are considered the same element (masked). The output array is always a masked array. See [`numpy.unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
 for more details.

See also

[`numpy.unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= \[1, 2, 1000, 2, 3\]
\>>> mask \= \[0, 0, 1, 0, 0\]
\>>> masked\_a \= np.ma.masked\_array(a, mask)
\>>> masked\_a
masked\_array(data=\[1, 2, --, 2, 3\],
            mask=\[False, False,  True, False, False\],
    fill\_value=999999)
\>>> np.ma.unique(masked\_a)
masked\_array(data=\[1, 2, 3, --\],
            mask=\[False, False, False,  True\],
    fill\_value=999999)
\>>> np.ma.unique(masked\_a, return\_index\=True)
(masked\_array(data=\[1, 2, 3, --\],
            mask=\[False, False, False,  True\],
    fill\_value=999999), array(\[0, 1, 4, 2\]))
\>>> np.ma.unique(masked\_a, return\_inverse\=True)
(masked\_array(data=\[1, 2, 3, --\],
            mask=\[False, False, False,  True\],
    fill\_value=999999), array(\[0, 1, 3, 1, 2\]))
\>>> np.ma.unique(masked\_a, return\_index\=True, return\_inverse\=True)
(masked\_array(data=\[1, 2, 3, --\],
            mask=\[False, False, False,  True\],
    fill\_value=999999), array(\[0, 1, 4, 2\]), array(\[0, 1, 3, 1, 2\]))

Copy to clipboard

Go BackOpen In Tab

On this page