[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.tolist.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.tolist.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.tolist.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.tolist.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.tolist.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.tolist.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.tolist.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.tolist[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html#numpy-ma-maskedarray-tolist "Link to this heading")

=====================================================================================================================================================================

method

ma.MaskedArray.tolist(_fill\_value\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6315-L6365)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html#numpy.ma.MaskedArray.tolist "Link to this definition")

Return the data portion of the masked array as a hierarchical Python list.

Data items are converted to the nearest compatible Python type. Masked values are converted to [`fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")
. If [`fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")
 is None, the corresponding entries in the output list will be `None`.

Parameters:

**fill\_value**scalar, optional

The value to use for invalid entries. Default is None.

Returns:

**result**list

The Python list representation of the masked array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[\[1,2,3\], \[4,5,6\], \[7,8,9\]\], mask\=\[0\] + \[1,0\]\*4)
\>>> x.tolist()
\[\[1, None, 3\], \[None, 5, None\], \[7, None, 9\]\]
\>>> x.tolist(\-999)
\[\[1, -999, 3\], \[-999, 5, -999\], \[7, -999, 9\]\]

Copy to clipboard

Go BackOpen In Tab

On this page