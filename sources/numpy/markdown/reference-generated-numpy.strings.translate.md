[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.translate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.translate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.translate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.translate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.translate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.translate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.translate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.translate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.translate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.translate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.translate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.translate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.translate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.translate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.translate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.translate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.translate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.translate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.translate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.translate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.translate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.translate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.translate[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.translate.html#numpy-strings-translate "Link to this heading")

=========================================================================================================================================================

strings.translate(_a_, _table_, _deletechars\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1679-L1727)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.translate.html#numpy.strings.translate "Link to this definition")

For each element in _a_, return a copy of the string where all characters occurring in the optional argument _deletechars_ are removed, and the remaining characters have been mapped through the given translation table.

Calls [`str.translate`](https://docs.python.org/3/library/stdtypes.html#str.translate "(in Python v3.14)")
 element-wise.

Parameters:

**a**array-like, with `bytes_` or `str_` dtype

**table**str of length 256

**deletechars**str

Returns:

**out**ndarray

Output array of str or unicode, depending on input type

See also

[`str.translate`](https://docs.python.org/3/library/stdtypes.html#str.translate "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\['a1b c', '1bca', 'bca1'\])
\>>> table \= a\[0\].maketrans('abc', '123')
\>>> deletechars \= ' '
\>>> np.char.translate(a, table, deletechars)
array(\['112 3', '1231', '2311'\], dtype='<U5')

Copy to clipboard

Go BackOpen In Tab

On this page