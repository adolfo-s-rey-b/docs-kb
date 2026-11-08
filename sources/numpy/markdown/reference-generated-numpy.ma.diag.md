[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.diag.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.diag.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.diag.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.diag.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.diag.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.diag.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.diag.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.diag.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.diag.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.diag.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.diag.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.diag.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.diag.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.diag.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.diag.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.diag.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.diag.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.diag.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.diag.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.diag.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.diag.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.diag.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.diag[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.diag.html#numpy-ma-diag "Link to this heading")

===========================================================================================================================

ma.diag(_v_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7375-L7423)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.diag.html#numpy.ma.diag "Link to this definition")

Extract a diagonal or construct a diagonal array.

This function is the equivalent of [`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
 that takes masked values into account, see [`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
 for details.

See also

[`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Create an array with negative values masked:

\>>> import numpy as np
\>>> x \= np.array(\[\[11.2, \-3.973, 18\], \[0.801, \-1.41, 12\], \[7, 33, \-12\]\])
\>>> masked\_x \= np.ma.masked\_array(x, mask\=x < 0)
\>>> masked\_x
masked\_array(
  data=\[\[11.2, --, 18.0\],\
        \[0.801, --, 12.0\],\
        \[7.0, 33.0, --\]\],
  mask=\[\[False,  True, False\],\
        \[False,  True, False\],\
        \[False, False,  True\]\],
  fill\_value=1e+20)

Copy to clipboard

Isolate the main diagonal from the masked array:

\>>> np.ma.diag(masked\_x)
masked\_array(data=\[11.2, --, --\],
             mask=\[False,  True,  True\],
       fill\_value=1e+20)

Copy to clipboard

Isolate the first diagonal below the main diagonal:

\>>> np.ma.diag(masked\_x, \-1)
masked\_array(data=\[0.801, 33.0\],
             mask=\[False, False\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page