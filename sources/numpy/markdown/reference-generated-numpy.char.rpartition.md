[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.rpartition.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.rpartition.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.rpartition.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.rpartition.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.rpartition.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.rpartition.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.rpartition.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.rpartition.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.rpartition.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.rpartition.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.rpartition.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.rpartition.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.rpartition.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.rpartition.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.rpartition.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.rpartition.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.rpartition.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.rpartition.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.rpartition.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.rpartition.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.rpartition.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.rpartition.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.rpartition[#](https://numpy.org/doc/stable/reference/generated/numpy.char.rpartition.html#numpy-char-rpartition "Link to this heading")

===================================================================================================================================================

char.rpartition(_a_, _sep_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/defchararray.py#L360-L401)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.rpartition.html#numpy.char.rpartition "Link to this definition")

Partition (split) each element around the right-most separator.

Calls [`str.rpartition`](https://docs.python.org/3/library/stdtypes.html#str.rpartition "(in Python v3.14)")
 element-wise.

For each element in _a_, split the element as the last occurrence of _sep_, and return 3 strings containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return 3 strings containing the string itself, followed by two empty strings.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

Input array

**sep**str or unicode

Right-most separator to split each element in array.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types. The output array will have an extra dimension with 3 elements per input element.

See also

[`str.rpartition`](https://docs.python.org/3/library/stdtypes.html#str.rpartition "(in Python v3.14)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\['aAaAaA', '  aA  ', 'abBABba'\])
\>>> np.char.rpartition(a, 'A')
array(\[\['aAaAa', 'A', ''\],\
   \['  a', 'A', '  '\],\
   \['abB', 'A', 'Bba'\]\], dtype='<U5')

Copy to clipboard

Go BackOpen In Tab

On this page