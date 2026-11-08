[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rows.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.mask_rows.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rows.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.mask_rows.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.mask_rows.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.mask_rows.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.mask_rows.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.mask_rows.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.mask_rows.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.mask_rows.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.mask_rows.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.mask_rows.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.mask_rows.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.mask_rows.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.mask_rows.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.mask_rows.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.mask_rows.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.mask_rows.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.mask_rows.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.mask_rows.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.mask_rows.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.mask_rows.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.mask\_rows[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rows.html#numpy-ma-mask-rows "Link to this heading")

===========================================================================================================================================

ma.mask\_rows(_a_, _axis=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1124-L1172)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rows.html#numpy.ma.mask_rows "Link to this definition")

Mask rows of a 2D array that contain masked values.

This function is a shortcut to `mask_rowcols` with _axis_ equal to 0.

See also

[`mask_rowcols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rowcols.html#numpy.ma.mask_rowcols "numpy.ma.mask_rowcols")

Mask rows and/or columns of a 2D array.

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.zeros((3, 3), dtype\=np.int\_)
\>>> a\[1, 1\] \= 1
\>>> a
array(\[\[0, 0, 0\],\
       \[0, 1, 0\],\
       \[0, 0, 0\]\])
\>>> a \= np.ma.masked\_equal(a, 1)
\>>> a
masked\_array(
  data=\[\[0, 0, 0\],\
        \[0, --, 0\],\
        \[0, 0, 0\]\],
  mask=\[\[False, False, False\],\
        \[False,  True, False\],\
        \[False, False, False\]\],
  fill\_value=1)

Copy to clipboard

\>>> np.ma.mask\_rows(a)
masked\_array(
  data=\[\[0, 0, 0\],\
        \[--, --, --\],\
        \[0, 0, 0\]\],
  mask=\[\[False, False, False\],\
        \[ True,  True,  True\],\
        \[False, False, False\]\],
  fill\_value=1)

Copy to clipboard

Go BackOpen In Tab

On this page