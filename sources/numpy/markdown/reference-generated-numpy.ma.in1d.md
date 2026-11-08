[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.in1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.in1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.in1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.in1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.in1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.in1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.in1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.in1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.in1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.in1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.in1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.in1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.in1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.in1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.in1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.in1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.in1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.in1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.in1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.in1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.in1d[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html#numpy-ma-in1d "Link to this heading")

===========================================================================================================================

ma.in1d(_ar1_, _ar2_, _assume\_unique\=False_, _invert\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1387-L1431)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html#numpy.ma.in1d "Link to this definition")

Test whether each element of an array is also present in a second array.

The output is always a masked array.

We recommend using [`isin`](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "numpy.isin")
 instead of [`in1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html#numpy.ma.in1d "numpy.ma.in1d")
 for new code.

See also

[`isin`](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "numpy.isin")

Version of this function that preserves the shape of ar1.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> ar1 \= np.ma.array(\[0, 1, 2, 5, 0\])
\>>> ar2 \= \[0, 2\]
\>>> np.ma.in1d(ar1, ar2)
masked\_array(data=\[ True, False,  True, False,  True\],
             mask=False,
       fill\_value=True)

Copy to clipboard

Go BackOpen In Tab

On this page