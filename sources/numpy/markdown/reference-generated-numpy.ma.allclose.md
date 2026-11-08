[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.allclose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.allclose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.allclose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.allclose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.allclose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.allclose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.allclose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.allclose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.allclose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.allclose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.allclose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.allclose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.allclose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.allclose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.allclose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.allclose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.allclose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.allclose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.allclose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.allclose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.allclose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.allclose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.allclose[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.allclose.html#numpy-ma-allclose "Link to this heading")

=======================================================================================================================================

ma.allclose(_a_, _b_, _masked\_equal\=True_, _rtol\=1e-05_, _atol\=1e-08_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8517-L8623)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.allclose.html#numpy.ma.allclose "Link to this definition")

Returns True if two arrays are element-wise equal within a tolerance.

This function is equivalent to [`allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")
 except that masked values are treated as equal (default) or unequal, depending on the [`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")
 argument.

Parameters:

**a, b**array\_like

Input arrays to compare.

**masked\_equal**bool, optional

Whether masked values in _a_ and _b_ are considered equal (True) or not (False). They are considered equal by default.

**rtol**float, optional

Relative tolerance. The relative difference is equal to `rtol * b`. Default is 1e-5.

**atol**float, optional

Absolute tolerance. The absolute difference is equal to _atol_. Default is 1e-8.

Returns:

**y**bool

Returns True if the two arrays are equal within the given tolerance, False otherwise. If either array contains NaN, then False is returned.

See also

[`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
, [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")

[`numpy.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")

the non-masked [`allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")
.

Notes

If the following equation is element-wise True, then [`allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")
 returns True:

absolute(\`a\` - \`b\`) <= (\`atol\` + \`rtol\` \* absolute(\`b\`))

Copy to clipboard

Return True if all elements of _a_ and _b_ are equal subject to given tolerances.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[1e10, 1e-7, 42.0\], mask\=\[0, 0, 1\])
\>>> a
masked\_array(data=\[10000000000.0, 1e-07, --\],
             mask=\[False, False,  True\],
       fill\_value=1e+20)
\>>> b \= np.ma.array(\[1e10, 1e-8, \-42.0\], mask\=\[0, 0, 1\])
\>>> np.ma.allclose(a, b)
False

Copy to clipboard

\>>> a \= np.ma.array(\[1e10, 1e-8, 42.0\], mask\=\[0, 0, 1\])
\>>> b \= np.ma.array(\[1.00001e10, 1e-9, \-42.0\], mask\=\[0, 0, 1\])
\>>> np.ma.allclose(a, b)
True
\>>> np.ma.allclose(a, b, masked\_equal\=False)
False

Copy to clipboard

Masked values are not compared directly.

\>>> a \= np.ma.array(\[1e10, 1e-8, 42.0\], mask\=\[0, 0, 1\])
\>>> b \= np.ma.array(\[1.00001e10, 1e-9, 42.0\], mask\=\[0, 0, 1\])
\>>> np.ma.allclose(a, b)
True
\>>> np.ma.allclose(a, b, masked\_equal\=False)
False

Copy to clipboard

Go BackOpen In Tab

On this page