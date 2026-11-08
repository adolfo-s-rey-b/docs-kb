[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.reshape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.reshape.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.reshape.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.reshape.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.reshape.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.reshape.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.reshape.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.reshape.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.reshape.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.reshape.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.reshape.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.reshape.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.reshape.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.reshape.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.reshape.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.reshape.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.reshape.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.reshape.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.reshape.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.reshape.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.reshape.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.reshape.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.reshape[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.reshape.html#numpy-ma-reshape "Link to this heading")

====================================================================================================================================

ma.reshape(_a_, _new\_shape_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7647-L7694)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.reshape.html#numpy.ma.reshape "Link to this definition")

Returns an array containing the same data with a new shape.

Refer to [`MaskedArray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.reshape.html#numpy.ma.MaskedArray.reshape "numpy.ma.MaskedArray.reshape")
 for full documentation.

See also

[`MaskedArray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.reshape.html#numpy.ma.MaskedArray.reshape "numpy.ma.MaskedArray.reshape")

equivalent function

Examples

Try it in your browser!

Reshaping a 1-D array:

\>>> a \= np.ma.array(\[1, 2, 3, 4\])
\>>> np.ma.reshape(a, (2, 2))
masked\_array(
  data=\[\[1, 2\],\
        \[3, 4\]\],
  mask=False,
  fill\_value=999999)

Copy to clipboard

Reshaping a 2-D array:

\>>> b \= np.ma.array(\[\[1, 2\], \[3, 4\]\])
\>>> np.ma.reshape(b, (1, 4))
masked\_array(data=\[\[1, 2, 3, 4\]\],
             mask=False,
       fill\_value=999999)

Copy to clipboard

Reshaping a 1-D array with a mask:

\>>> c \= np.ma.array(\[1, 2, 3, 4\], mask\=\[False, True, False, False\])
\>>> np.ma.reshape(c, (2, 2))
masked\_array(
  data=\[\[1, --\],\
        \[3, 4\]\],
  mask=\[\[False,  True\],\
        \[False, False\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page