[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.center.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.center.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.center.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.center.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.center.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.center.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.center.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.center.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.center.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.center.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.center.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.center.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.center.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.center.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.center.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.center.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.center.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.center.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.center.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.center.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.center.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.center.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.center[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.center.html#numpy-strings-center "Link to this heading")

================================================================================================================================================

strings.center(_a_, _width_, _fillchar\=' '_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L691-L757)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.center.html#numpy.strings.center "Link to this definition")

Return a copy of _a_ with its elements centered in a string of length _width_.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**width**array\_like, with any integer dtype

The length of the resulting strings, unless `width < str_len(a)`.

**fillchar**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Optional padding character to use (default is space).

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

See also

[`str.center`](https://docs.python.org/3/library/stdtypes.html#str.center "(in Python v3.14)")

Notes

While it is possible for `a` and `fillchar` to have different dtypes, passing a non-ASCII character in `fillchar` when `a` is of dtype “S” is not allowed, and a `ValueError` is raised.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> c \= np.array(\['a1b2','1b2a','b2a1','2a1b'\]); c
array(\['a1b2', '1b2a', 'b2a1', '2a1b'\], dtype='<U4')
\>>> np.strings.center(c, width\=9)
array(\['   a1b2  ', '   1b2a  ', '   b2a1  ', '   2a1b  '\], dtype='<U9')
\>>> np.strings.center(c, width\=9, fillchar\='\*')
array(\['\*\*\*a1b2\*\*', '\*\*\*1b2a\*\*', '\*\*\*b2a1\*\*', '\*\*\*2a1b\*\*'\], dtype='<U9')
\>>> np.strings.center(c, width\=1)
array(\['a1b2', '1b2a', 'b2a1', '2a1b'\], dtype='<U4')

Copy to clipboard

Go BackOpen In Tab

On this page