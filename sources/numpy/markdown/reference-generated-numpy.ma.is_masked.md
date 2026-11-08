[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.is_masked.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.is_masked.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.is_masked.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.is_masked.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.is_masked.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.is_masked.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.is_masked.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.is_masked.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.is_masked.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.is_masked.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.is_masked.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.is_masked.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.is_masked.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.is_masked.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.is_masked.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.is_masked.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.is_masked.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.is_masked.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.is_masked.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.is_masked.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.is\_masked[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html#numpy-ma-is-masked "Link to this heading")

===========================================================================================================================================

ma.is\_masked(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6878-L6929)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html#numpy.ma.is_masked "Link to this definition")

Determine whether input has masked values.

Accepts any object as input, but always returns False unless the input is a MaskedArray containing masked values.

Parameters:

**x**array\_like

Array to check for masked values.

Returns:

**result**bool

True if _x_ is a MaskedArray with masked values, False otherwise.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= ma.masked\_equal(\[0, 1, 0, 2, 3\], 0)
\>>> x
masked\_array(data=\[--, 1, --, 2, 3\],
             mask=\[ True, False,  True, False, False\],
       fill\_value=0)
\>>> ma.is\_masked(x)
True
\>>> x \= ma.masked\_equal(\[0, 1, 0, 2, 3\], 42)
\>>> x
masked\_array(data=\[0, 1, 0, 2, 3\],
             mask=False,
       fill\_value=42)
\>>> ma.is\_masked(x)
False

Copy to clipboard

Always returns False if _x_ isn’t a MaskedArray.

\>>> x \= \[False, True, False\]
\>>> ma.is\_masked(x)
False
\>>> x \= 'a string'
\>>> ma.is\_masked(x)
False

Copy to clipboard

Go BackOpen In Tab

On this page