[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tobytes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.tobytes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.tobytes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.tobytes[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tobytes.html#numpy-ma-maskedarray-tobytes "Link to this heading")

========================================================================================================================================================================

method

ma.MaskedArray.tobytes(_fill\_value\=None_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6367-L6404)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tobytes.html#numpy.ma.MaskedArray.tobytes "Link to this definition")

Return the array data as a string containing the raw bytes in the array.

The array is filled with a fill value before the string conversion.

Parameters:

**fill\_value**scalar, optional

Value used to fill in the masked values. Default is None, in which case _MaskedArray.fill\_value_ is used.

**order**{‘C’,’F’,’A’}, optional

Order of the data item in the copy. Default is ‘C’.

*   ‘C’ – C order (row major).
    
*   ‘F’ – Fortran order (column major).
    
*   ‘A’ – Any, current order of array.
    
*   None – Same as ‘A’.
    

See also

[`numpy.ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")

[`tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html#numpy.ma.MaskedArray.tolist "numpy.ma.MaskedArray.tolist")
, [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tofile.html#numpy.ma.MaskedArray.tofile "numpy.ma.MaskedArray.tofile")

Notes

As for [`ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")
, information about the shape, dtype, etc., but also about [`fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")
, will be lost.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(np.array(\[\[1, 2\], \[3, 4\]\]), mask\=\[\[0, 1\], \[1, 0\]\])
\>>> x.tobytes()
b'\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00?B\\x0f\\x00\\x00\\x00\\x00\\x00?B\\x0f\\x00\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x00\\x00\\x00\\x00'

Copy to clipboard

Go BackOpen In Tab

On this page