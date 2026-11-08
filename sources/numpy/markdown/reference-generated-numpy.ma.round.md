[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.round.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.round.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.round.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.round.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.round.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.round.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.round.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.round.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.round.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.round.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.round.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.round.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.round.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.round.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.round.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.round.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.round.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.round.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.round.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.round.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.round.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.round.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.round[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.round.html#numpy-ma-round "Link to this heading")

==============================================================================================================================

ma.round(_a_, _decimals\=0_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8098-L8151)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.round.html#numpy.ma.round "Link to this definition")

Return a copy of a, rounded to ‘decimals’ places.

When ‘decimals’ is negative, it specifies the number of positions to the left of the decimal point. The real and imaginary parts of complex numbers are rounded separately. Nothing is done if the array is not of float type and ‘decimals’ is greater than or equal to 0.

Parameters:

**decimals**int

Number of decimals to round to. May be negative.

**out**array\_like

Existing array to use for output. If not given, returns a default copy of a.

Notes

If out is given and does not have a mask attribute, the mask of a is lost!

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= \[11.2, \-3.973, 0.801, \-1.41\]
\>>> mask \= \[0, 0, 0, 1\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> masked\_x
masked\_array(data=\[11.2, -3.973, 0.801, --\],
             mask=\[False, False, False, True\],
    fill\_value=1e+20)
\>>> ma.round(masked\_x)
masked\_array(data=\[11.0, -4.0, 1.0, --\],
             mask=\[False, False, False, True\],
    fill\_value=1e+20)
\>>> ma.round(masked\_x, decimals\=1)
masked\_array(data=\[11.2, -4.0, 0.8, --\],
             mask=\[False, False, False, True\],
    fill\_value=1e+20)
\>>> ma.round(masked\_x, decimals\=-1)
masked\_array(data=\[10.0, -0.0, 0.0, --\],
             mask=\[False, False, False, True\],
    fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page