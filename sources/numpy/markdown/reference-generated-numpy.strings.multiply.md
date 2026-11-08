[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.multiply.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.multiply.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.multiply.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.multiply.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.multiply.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.multiply.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.multiply.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.multiply.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.multiply.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.multiply.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.multiply.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.multiply.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.multiply.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.multiply.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.multiply.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.multiply.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.multiply.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.multiply.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.multiply.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.multiply.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.multiply.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.multiply.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.multiply[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.multiply.html#numpy-strings-multiply "Link to this heading")

======================================================================================================================================================

strings.multiply(_a_, _i_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L148-L210)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.multiply.html#numpy.strings.multiply "Link to this definition")

Return (a \* i), that is string multiple concatenation, element-wise.

Values in `i` of less than 0 are treated as 0 (which yields an empty string).

Parameters:

**a**array\_like, with `StringDType`, `bytes_` or `str_` dtype

**i**array\_like, with any integer dtype

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\["a", "b", "c"\])
\>>> np.strings.multiply(a, 3)
array(\['aaa', 'bbb', 'ccc'\], dtype='<U3')
\>>> i \= np.array(\[1, 2, 3\])
\>>> np.strings.multiply(a, i)
array(\['a', 'bb', 'ccc'\], dtype='<U3')
\>>> np.strings.multiply(np.array(\['a'\]), i)
array(\['a', 'aa', 'aaa'\], dtype='<U3')
\>>> a \= np.array(\['a', 'b', 'c', 'd', 'e', 'f'\]).reshape((2, 3))
\>>> np.strings.multiply(a, 3)
array(\[\['aaa', 'bbb', 'ccc'\],\
       \['ddd', 'eee', 'fff'\]\], dtype='<U3')
\>>> np.strings.multiply(a, i)
array(\[\['a', 'bb', 'ccc'\],\
       \['d', 'ee', 'fff'\]\], dtype='<U3')

Copy to clipboard

Go BackOpen In Tab

On this page