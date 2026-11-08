[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.compressed.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.compressed.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.compressed.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.compressed.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.compressed.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.compressed.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.compressed.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.compressed.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.compressed.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.compressed.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.compressed.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.compressed.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.compressed.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.compressed.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.compressed.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.compressed.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.compressed.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.compressed.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.compressed.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.compressed.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.compressed[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy-ma-compressed "Link to this heading")

=============================================================================================================================================

ma.compressed(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7275-L7311)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy.ma.compressed "Link to this definition")

Return all the non-masked data as a 1-D array.

This function is equivalent to calling the “compressed” method of a [`ma.MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, see [`ma.MaskedArray.compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "numpy.ma.MaskedArray.compressed")
 for details.

See also

[`ma.MaskedArray.compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "numpy.ma.MaskedArray.compressed")

Equivalent method.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Create an array with negative values masked:

\>>> import numpy as np
\>>> x \= np.array(\[\[1, \-1, 0\], \[2, \-1, 3\], \[7, 4, \-1\]\])
\>>> masked\_x \= np.ma.masked\_array(x, mask\=x < 0)
\>>> masked\_x
masked\_array(
  data=\[\[1, --, 0\],\
        \[2, --, 3\],\
        \[7, 4, --\]\],
  mask=\[\[False,  True, False\],\
        \[False,  True, False\],\
        \[False, False,  True\]\],
  fill\_value=999999)

Copy to clipboard

Compress the masked array into a 1-D array of non-masked values:

\>>> np.ma.compressed(masked\_x)
array(\[1, 0, 2, 3, 7, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page