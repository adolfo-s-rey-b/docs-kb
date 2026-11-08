[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.strip.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.strip[#](https://numpy.org/doc/stable/reference/generated/numpy.char.strip.html#numpy-char-strip "Link to this heading")

====================================================================================================================================

char.strip(_a_, _chars\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1033-L1077)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.strip.html#numpy.char.strip "Link to this definition")

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