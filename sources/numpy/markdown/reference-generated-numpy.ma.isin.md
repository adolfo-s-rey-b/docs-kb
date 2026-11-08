[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.isin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.isin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.isin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.isin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.isin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.isin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.isin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.isin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.isin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.isin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.isin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.isin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.isin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.isin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.isin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.isin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.isin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.isin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.isin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.isin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.isin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.isin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.isin[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.isin.html#numpy-ma-isin "Link to this heading")

===========================================================================================================================

ma.isin(_element_, _test\_elements_, _assume\_unique\=False_, _invert\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1434-L1460)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.isin.html#numpy.ma.isin "Link to this definition")

Calculates _element in test\_elements_, broadcasting over _element_ only.

The output is always a masked array of the same shape as _element_. See [`numpy.isin`](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "numpy.isin")
 for more details.

See also

[`in1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html#numpy.ma.in1d "numpy.ma.in1d")

Flattened version of this function.

[`numpy.isin`](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "numpy.isin")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> element \= np.ma.array(\[1, 2, 3, 4, 5, 6\])
\>>> test\_elements \= \[0, 2\]
\>>> np.ma.isin(element, test\_elements)
masked\_array(data=\[False,  True, False, False, False, False\],
             mask=False,
       fill\_value=True)

Copy to clipboard

Go BackOpen In Tab

On this page