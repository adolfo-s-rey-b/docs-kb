[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.split.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.split.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.split.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.split.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.split.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.split.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.split.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.split.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.split.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.split.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.split.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.split.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.split.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.split.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.split.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.split.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.split.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.split.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.split.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.split.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.split.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.split.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.split[#](https://numpy.org/doc/stable/reference/generated/numpy.char.split.html#numpy-char-split "Link to this heading")

====================================================================================================================================

char.split(_a_, _sep\=None_, _maxsplit\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L1399-L1441)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.split.html#numpy.char.split "Link to this definition")

For each element in _a_, return a list of the words in the string, using _sep_ as the delimiter string.

Calls [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split "(in Python v3.14)")
 element-wise.

Parameters:

**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype

**sep**str or unicode, optional

If _sep_ is not specified or None, any whitespace string is a separator.

**maxsplit**int, optional

If _maxsplit_ is given, at most _maxsplit_ splits are done.

Returns:

**out**ndarray

Array of list objects

See also

[`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split "(in Python v3.14)")
, [`rsplit`](https://numpy.org/doc/stable/reference/generated/numpy.char.rsplit.html#numpy.char.rsplit "numpy.char.rsplit")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array("Numpy is nice!")
\>>> np.strings.split(x, " ")  
array(list(\['Numpy', 'is', 'nice!'\]), dtype=object)  

Copy to clipboard

\>>> np.strings.split(x, " ", 1)  
array(list(\['Numpy', 'is nice!'\]), dtype=object)  

Copy to clipboard

Go BackOpen In Tab

On this page