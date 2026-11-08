[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.title.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.title[#](https://numpy.org/doc/stable/reference/generated/numpy.char.title.html#numpy-char-title "Link to this heading")

====================================================================================================================================

char.title(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1242-L1282)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.title.html#numpy.char.title "Link to this definition")

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