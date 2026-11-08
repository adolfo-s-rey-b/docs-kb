[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.endswith.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.endswith.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.endswith.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.endswith.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.endswith.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.endswith.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.endswith.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.endswith.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.endswith.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.endswith.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.endswith.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.endswith.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.endswith.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.endswith.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.endswith.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.endswith.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.endswith.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.endswith.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.endswith.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.endswith.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.endswith.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.endswith.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.endswith[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.endswith.html#numpy-strings-endswith "Link to this heading")

======================================================================================================================================================

strings.endswith(_a_, _suffix_, _start\=0_, _end\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L490-L528)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.endswith.html#numpy.strings.endswith "Link to this definition")

Returns a boolean array which is _True_ where the string element in `a` ends with `suffix`, otherwise _False_.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**suffix**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**start, end**array\_like, with any integer dtype

With `start`, test beginning at that position. With `end`, stop comparing at that position.

Returns:

**out**ndarray

Output array of bools

See also

[`str.endswith`](https://docs.python.org/3/library/stdtypes.html#str.endswith "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> s \= np.array(\['foo', 'bar'\])
\>>> s
array(\['foo', 'bar'\], dtype='<U3')
\>>> np.strings.endswith(s, 'ar')
array(\[False,  True\])
\>>> np.strings.endswith(s, 'a', start\=1, end\=2)
array(\[False,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page