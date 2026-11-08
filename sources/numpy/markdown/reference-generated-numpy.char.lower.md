[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.lower.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.lower.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.lower.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.lower.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.lower.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.lower.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.lower.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.lower.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.lower.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.lower.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.lower.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.lower.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.lower.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.lower.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.lower.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.lower.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.lower.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.lower.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.lower.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.lower.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.lower[#](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html#numpy-char-lower "Link to this heading")

====================================================================================================================================

char.lower(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1122-L1157)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html#numpy.char.lower "Link to this definition")

Return an array with the elements converted to lowercase.

Call [`str.lower`](https://docs.python.org/3/library/stdtypes.html#str.lower "(in Python v3.14)")
 element-wise.

For 8-bit strings, this method is locale-dependent.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Input array.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

See also

[`str.lower`](https://docs.python.org/3/library/stdtypes.html#str.lower "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> c \= np.array(\['A1B C', '1BCA', 'BCA1'\]); c
array(\['A1B C', '1BCA', 'BCA1'\], dtype='<U5')
\>>> np.strings.lower(c)
array(\['a1b c', '1bca', 'bca1'\], dtype='<U5')

Copy to clipboard

Go BackOpen In Tab

On this page