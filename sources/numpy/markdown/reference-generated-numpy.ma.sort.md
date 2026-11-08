[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.sort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.sort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.sort.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.sort.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.sort.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.sort.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.sort.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.sort.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.sort.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.sort.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.sort.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.sort.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.sort.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.sort.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.sort.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.sort.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.sort.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.sort.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.sort.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.sort.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.sort.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.sort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.sort[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.sort.html#numpy-ma-sort "Link to this heading")

===========================================================================================================================

ma.sort(_a_, _axis\=\-1_, _kind\=None_, _order\=None_, _endwith\=True_, _fill\_value\=None_, _\*_, _stable\=None_, _descending\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7232-L7272)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.sort.html#numpy.ma.sort "Link to this definition")

Return a sorted copy of the masked array.

Equivalent to creating a copy of the array and applying the MaskedArray `sort()` method.

Refer to `MaskedArray.sort` for the full documentation

See also

[`MaskedArray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#numpy.ma.MaskedArray.sort "numpy.ma.MaskedArray.sort")

equivalent method

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= \[11.2, \-3.973, 0.801, \-1.41\]
\>>> mask \= \[0, 0, 0, 1\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> masked\_x
masked\_array(data=\[11.2, -3.973, 0.801, --\],
             mask=\[False, False, False,  True\],
       fill\_value=1e+20)
\>>> ma.sort(masked\_x)
masked\_array(data=\[-3.973, 0.801, 11.2, --\],
             mask=\[False, False, False,  True\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page