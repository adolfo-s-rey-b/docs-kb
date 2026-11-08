[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.index[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.index.html#numpy-strings-index "Link to this heading")

=============================================================================================================================================

strings.index(_a_, _sub_, _start\=0_, _end\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L336-L367)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.index.html#numpy.strings.index "Link to this definition")

Like [`find`](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#numpy.strings.find "numpy.strings.find")
, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
 when the substring is not found.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**sub**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**start, end**array\_like, with any integer dtype, optional

Returns:

**out**ndarray

Output array of ints.

See also

[`find`](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#numpy.strings.find "numpy.strings.find")
, [`str.index`](https://docs.python.org/3/library/stdtypes.html#str.index "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\["Computer Science"\])
\>>> np.strings.index(a, "Science", start\=0, end\=None)
array(\[9\])

Copy to clipboard

Go BackOpen In Tab

On this page