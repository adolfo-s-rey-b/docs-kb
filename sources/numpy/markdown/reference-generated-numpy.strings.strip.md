[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.strip.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.strip.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.strip.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.strip.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.strip.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.strip.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.strip.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.strip.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.strip.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.strip.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.strip.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.strip.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.strip.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.strip.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.strip.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.strip.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.strip.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.strip.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.strip.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.strip.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.strip.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.strip.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.strip[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.strip.html#numpy-strings-strip "Link to this heading")

=============================================================================================================================================

strings.strip(_a_, _chars\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1033-L1077)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.strip.html#numpy.strings.strip "Link to this definition")

For each element in _a_, return a copy with the leading and trailing characters removed.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**chars**scalar with the same dtype as `a`, optional

The `chars` argument is a string specifying the set of characters to be removed. If `None`, the `chars` argument defaults to removing whitespace. The `chars` argument is not a prefix or suffix; rather, all combinations of its values are stripped.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

See also

[`str.strip`](https://docs.python.org/3/library/stdtypes.html#str.strip "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> c \= np.array(\['aAaAaA', '  aA  ', 'abBABba'\])
\>>> c
array(\['aAaAaA', '  aA  ', 'abBABba'\], dtype='<U7')
\>>> np.strings.strip(c)
array(\['aAaAaA', 'aA', 'abBABba'\], dtype='<U7')
\# 'a' unstripped from c\[1\] because of leading whitespace.
\>>> np.strings.strip(c, 'a')
array(\['AaAaA', '  aA  ', 'bBABb'\], dtype='<U7')
\# 'A' unstripped from c\[1\] because of trailing whitespace.
\>>> np.strings.strip(c, 'A')
array(\['aAaAa', '  aA  ', 'abBABba'\], dtype='<U7')

Copy to clipboard

Go BackOpen In Tab

On this page