[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.allequal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.allequal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.allequal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.allequal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.allequal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.allequal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.allequal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.allequal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.allequal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.allequal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.allequal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.allequal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.allequal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.allequal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.allequal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.allequal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.allequal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.allequal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.allequal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.allequal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.allequal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.allequal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.allequal[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.allequal.html#numpy-ma-allequal "Link to this heading")

=======================================================================================================================================

ma.allequal(_a_, _b_, _fill\_value\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8458-L8514)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.allequal.html#numpy.ma.allequal "Link to this definition")

Return True if all entries of a and b are equal, using fill\_value as a truth value where either or both are masked.

Parameters:

**a, b**array\_like

Input arrays to compare.

**fill\_value**bool, optional

Whether masked values in a or b are considered equal (True) or not (False).

Returns:

**y**bool

Returns True if the two arrays are equal within the given tolerance, False otherwise. If either array contains NaN, then False is returned.

See also

[`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
, [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")

[`numpy.ma.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.allclose.html#numpy.ma.allclose "numpy.ma.allclose")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[1e10, 1e-7, 42.0\], mask\=\[0, 0, 1\])
\>>> a
masked\_array(data=\[10000000000.0, 1e-07, --\],
             mask=\[False, False,  True\],
       fill\_value=1e+20)

Copy to clipboard

\>>> b \= np.array(\[1e10, 1e-7, \-42.0\])
\>>> b
array(\[  1.00000000e+10,   1.00000000e-07,  -4.20000000e+01\])
\>>> np.ma.allequal(a, b, fill\_value\=False)
False
\>>> np.ma.allequal(a, b)
True

Copy to clipboard

Go BackOpen In Tab

On this page