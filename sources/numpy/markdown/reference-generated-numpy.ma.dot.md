[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.dot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.dot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.dot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.dot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.dot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.dot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.dot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.dot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.dot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.dot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.dot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.dot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.dot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.dot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.dot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.dot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.dot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.dot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.dot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.dot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.dot[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html#numpy-ma-dot "Link to this heading")

========================================================================================================================

ma.dot(_a_, _b_, _strict\=False_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8229-L8307)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html#numpy.ma.dot "Link to this definition")

Return the dot product of two arrays.

This function is the equivalent of [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
 that takes masked values into account. Note that _strict_ and _out_ are in different position than in the method version. In order to maintain compatibility with the corresponding method, it is recommended that the optional arguments be treated as keyword only. At some point that may be mandatory.

Parameters:

**a, b**masked\_array\_like

Inputs arrays.

**strict**bool, optional

Whether masked data are propagated (True) or set to 0 (False) for the computation. Default is False. Propagating the mask means that if a masked value appears in a row or column, the whole row or column is considered masked.

**out**masked\_array, optional

Output argument. This must have the exact kind that would be returned if it was not used. In particular, it must have the right type, must be C-contiguous, and its dtype must be the dtype that would be returned for _dot(a,b)_. This is a performance feature. Therefore, if these conditions are not met, an exception is raised, instead of attempting to be flexible.

See also

[`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")

Equivalent function for ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[\[1, 2, 3\], \[4, 5, 6\]\], mask\=\[\[1, 0, 0\], \[0, 0, 0\]\])
\>>> b \= np.ma.array(\[\[1, 2\], \[3, 4\], \[5, 6\]\], mask\=\[\[1, 0\], \[0, 0\], \[0, 0\]\])
\>>> np.ma.dot(a, b)
masked\_array(
  data=\[\[21, 26\],\
        \[45, 64\]\],
  mask=\[\[False, False\],\
        \[False, False\]\],
  fill\_value=999999)
\>>> np.ma.dot(a, b, strict\=True)
masked\_array(
  data=\[\[--, --\],\
        \[--, 64\]\],
  mask=\[\[ True,  True\],\
        \[ True, False\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page