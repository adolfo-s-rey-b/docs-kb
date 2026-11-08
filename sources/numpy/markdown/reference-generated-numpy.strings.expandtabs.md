[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.expandtabs.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.expandtabs.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.expandtabs.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.expandtabs.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.expandtabs.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.expandtabs.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.expandtabs.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.expandtabs.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.expandtabs.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.expandtabs.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.expandtabs.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.expandtabs.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.expandtabs.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.expandtabs.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.expandtabs.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.expandtabs.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.expandtabs.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.expandtabs.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.expandtabs.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.expandtabs.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.expandtabs.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.expandtabs.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.expandtabs[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.expandtabs.html#numpy-strings-expandtabs "Link to this heading")

============================================================================================================================================================

strings.expandtabs(_a_, _tabsize\=8_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L634-L684)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.expandtabs.html#numpy.strings.expandtabs "Link to this definition")

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