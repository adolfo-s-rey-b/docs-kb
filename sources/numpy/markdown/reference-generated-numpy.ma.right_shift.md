[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.right_shift.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.right_shift.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.right_shift.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.right_shift.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.right_shift.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.right_shift.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.right_shift.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.right_shift.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.right_shift.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.right_shift.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.right_shift.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.right_shift.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.right_shift.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.right_shift.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.right_shift.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.right_shift.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.right_shift.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.right_shift.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.right_shift.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.right_shift.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.right_shift.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.right_shift.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.right\_shift[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.right_shift.html#numpy-ma-right-shift "Link to this heading")

=================================================================================================================================================

ma.right\_shift(_a_, _n_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7474-L7508)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.right_shift.html#numpy.ma.right_shift "Link to this definition")

Shift the bits of an integer to the right.

This is the masked array version of [`numpy.right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.right_shift.html#numpy.right_shift "numpy.right_shift")
, for details see that function.

See also

[`numpy.right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.right_shift.html#numpy.right_shift "numpy.right_shift")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= \[11, 3, 8, 1\]
\>>> mask \= \[0, 0, 0, 1\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> masked\_x
masked\_array(data=\[11, 3, 8, --\],
             mask=\[False, False, False,  True\],
       fill\_value=999999)
\>>> ma.right\_shift(masked\_x,1)
masked\_array(data=\[5, 1, 4, --\],
             mask=\[False, False, False,  True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page