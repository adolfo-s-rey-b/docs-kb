[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.replace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.replace[#](https://numpy.org/doc/stable/reference/generated/numpy.char.replace.html#numpy-char-replace "Link to this heading")

==========================================================================================================================================

char.replace(_a_, _old_, _new_, _count\=\-1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1289-L1351)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.replace.html#numpy.char.replace "Link to this definition")

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