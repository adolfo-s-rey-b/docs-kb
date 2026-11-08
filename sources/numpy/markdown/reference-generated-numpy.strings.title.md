[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.title.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.title.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.title.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.title.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.title.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.title.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.title.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.title.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.title.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.title.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.title.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.title.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.title.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.title.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.title.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.title.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.title.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.title.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.title.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.title.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.title.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.title.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.title[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.title.html#numpy-strings-title "Link to this heading")

=============================================================================================================================================

strings.title(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1242-L1282)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.title.html#numpy.strings.title "Link to this definition")

Return element-wise title cased version of string or unicode.

Title case words start with uppercase characters, all remaining cased characters are lowercase.

Calls [`str.title`](https://docs.python.org/3/library/stdtypes.html#str.title "(in Python v3.14)")
 element-wise.

For 8-bit strings, this method is locale-dependent.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Input array.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

See also

[`str.title`](https://docs.python.org/3/library/stdtypes.html#str.title "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> c\=np.array(\['a1b c','1b ca','b ca1','ca1b'\],'S5'); c
array(\['a1b c', '1b ca', 'b ca1', 'ca1b'\],
    dtype='|S5')
\>>> np.strings.title(c)
array(\['A1B C', '1B Ca', 'B Ca1', 'Ca1B'\],
    dtype='|S5')

Copy to clipboard

Go BackOpen In Tab

On this page