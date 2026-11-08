[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.left_shift.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.left_shift.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.left_shift.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.left_shift.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.left_shift.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.left_shift.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.left_shift.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.left_shift.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.left_shift.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.left_shift.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.left_shift.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.left_shift.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.left_shift.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.left_shift.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.left_shift.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.left_shift.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.left_shift.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.left_shift.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.left_shift.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.left_shift.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.left_shift.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.left_shift.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.left\_shift[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.left_shift.html#numpy-ma-left-shift "Link to this heading")

==============================================================================================================================================

ma.left\_shift(_a_, _n_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7426-L7471)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.left_shift.html#numpy.ma.left_shift "Link to this definition")

Shift the bits of an integer to the left.

This is the masked array version of [`numpy.left_shift`](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#numpy.left_shift "numpy.left_shift")
, for details see that function.

See also

[`numpy.left_shift`](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#numpy.left_shift "numpy.left_shift")

Examples

Try it in your browser!

Shift with a masked array:

\>>> arr \= np.ma.array(\[10, 20, 30\], mask\=\[False, True, False\])
\>>> np.ma.left\_shift(arr, 1)
masked\_array(data=\[20, --, 60\],
             mask=\[False,  True, False\],
       fill\_value=999999)

Copy to clipboard

Large shift:

\>>> np.ma.left\_shift(10, 10)
masked\_array(data=10240,
             mask=False,
       fill\_value=999999)

Copy to clipboard

Shift with a scalar and an array:

\>>> scalar \= 10
\>>> arr \= np.ma.array(\[1, 2, 3\], mask\=\[False, True, False\])
\>>> np.ma.left\_shift(scalar, arr)
masked\_array(data=\[20, --, 80\],
             mask=\[False,  True, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page