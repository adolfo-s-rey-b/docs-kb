[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.rpartition.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.rpartition.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.rpartition.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.rpartition.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.rpartition.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.rpartition.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.rpartition.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.rpartition.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.rpartition.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.rpartition.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.rpartition.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.rpartition.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.rpartition.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.rpartition.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.rpartition.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.rpartition.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.rpartition.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.rpartition.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.rpartition.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.rpartition.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.rpartition.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.rpartition.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.rpartition[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.rpartition.html#numpy-strings-rpartition "Link to this heading")

============================================================================================================================================================

strings.rpartition(_a_, _sep_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1605-L1672)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.rpartition.html#numpy.strings.rpartition "Link to this definition")

Partition (split) each element around the right-most separator.

For each element in `a`, split the element at the last occurrence of `sep`, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, the third item of the tuple will contain the whole string, and the first and second ones will be the empty string.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Input array

**sep**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Separator to split each string element in `a`.

Returns:

**out**3-tuple:

*   array with `StringDType`, `bytes_` or `str_` dtype with the part before the separator
    
*   array with `StringDType`, `bytes_` or `str_` dtype with the separator
    
*   array with `StringDType`, `bytes_` or `str_` dtype with the part after the separator
    

See also

[`str.rpartition`](https://docs.python.org/3/library/stdtypes.html#str.rpartition "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\['aAaAaA', '  aA  ', 'abBABba'\])
\>>> np.strings.rpartition(a, 'A')
(array(\['aAaAa', '  a', 'abB'\], dtype='<U5'),
 array(\['A', 'A', 'A'\], dtype='<U1'),
 array(\['', '  ', 'Bba'\], dtype='<U3'))

Copy to clipboard

Go BackOpen In Tab

On this page