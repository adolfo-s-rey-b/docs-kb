[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.append.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.append.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.append.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.append.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.append.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.append.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.append.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.append.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.append.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.append.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.append.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.append.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.append.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.append.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.append.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.append.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.append.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.append.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.append.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.append.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.append.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.append.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.append[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.append.html#numpy-ma-append "Link to this heading")

=================================================================================================================================

ma.append(_a_, _b_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8961-L9000)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.append.html#numpy.ma.append "Link to this definition")

Append values to the end of an array.

Parameters:

**a**array\_like

Values are appended to a copy of this array.

**b**array\_like

These values are appended to a copy of _a_. It must be of the correct shape (the same shape as _a_, excluding _axis_). If _axis_ is not specified, _b_ can be any shape and will be flattened before use.

**axis**int, optional

The axis along which _v_ are appended. If _axis_ is not given, both _a_ and _b_ are flattened before use.

Returns:

**append**MaskedArray

A copy of _a_ with _b_ appended to _axis_. Note that [`append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
 does not occur in-place: a new array is allocated and filled. If _axis_ is None, the result is a flattened array.

See also

[`numpy.append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")

Equivalent function in the top-level NumPy module.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= ma.masked\_values(\[1, 2, 3\], 2)
\>>> b \= ma.masked\_values(\[\[4, 5, 6\], \[7, 8, 9\]\], 7)
\>>> ma.append(a, b)
masked\_array(data=\[1, --, 3, 4, 5, 6, --, 8, 9\],
             mask=\[False,  True, False, False, False, False,  True, False,\
                   False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page