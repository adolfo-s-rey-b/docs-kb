[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.replace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.replace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.replace.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.replace.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.replace.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.replace.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.replace.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.replace.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.replace.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.replace.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.replace.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.replace.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.replace.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.replace.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.replace.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.replace.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.replace.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.replace.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.replace.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.replace.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.replace.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.replace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.replace[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.replace.html#numpy-strings-replace "Link to this heading")

===================================================================================================================================================

strings.replace(_a_, _old_, _new_, _count\=\-1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1289-L1351)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.replace.html#numpy.strings.replace "Link to this definition")

For each element in `a`, return a copy of the string with occurrences of substring `old` replaced by `new`.

Parameters:

**a**array\_like, with `bytes_` or `str_` dtype

**old, new**array\_like, with `bytes_` or `str_` dtype

**count**array\_like, with `int_` dtype

If the optional argument `count` is given, only the first `count` occurrences are replaced.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

See also

[`str.replace`](https://docs.python.org/3/library/stdtypes.html#str.replace "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\["That is a mango", "Monkeys eat mangos"\])
\>>> np.strings.replace(a, 'mango', 'banana')
array(\['That is a banana', 'Monkeys eat bananas'\], dtype='<U19')

Copy to clipboard

\>>> a \= np.array(\["The dish is fresh", "This is it"\])
\>>> np.strings.replace(a, 'is', 'was')
array(\['The dwash was fresh', 'Thwas was it'\], dtype='<U19')

Copy to clipboard

Go BackOpen In Tab

On this page