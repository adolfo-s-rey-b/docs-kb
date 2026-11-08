[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.expandtabs.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.expandtabs[#](https://numpy.org/doc/stable/reference/generated/numpy.char.expandtabs.html#numpy-char-expandtabs "Link to this heading")

===================================================================================================================================================

char.expandtabs(_a_, _tabsize\=8_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L634-L684)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.expandtabs.html#numpy.char.expandtabs "Link to this definition")

Return a copy of each string element where all tab characters are replaced by one or more spaces.

Calls [`str.expandtabs`](https://docs.python.org/3/library/stdtypes.html#str.expandtabs "(in Python v3.14)")
 element-wise.

Return a copy of each string element where all tab characters are replaced by one or more spaces, depending on the current column and the given _tabsize_. The column number is reset to zero after each newline occurring in the string. This doesn’t understand other non-printing characters or escape sequences.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Input array

**tabsize**int, optional

Replace tabs with _tabsize_ number of spaces. If not given defaults to 8 spaces.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input type

See also

[`str.expandtabs`](https://docs.python.org/3/library/stdtypes.html#str.expandtabs "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\['         Hello   world'\])
\>>> np.strings.expandtabs(a, tabsize\=4)  
array(\['        Hello   world'\], dtype='<U21')  

Copy to clipboard

Go BackOpen In Tab

On this page