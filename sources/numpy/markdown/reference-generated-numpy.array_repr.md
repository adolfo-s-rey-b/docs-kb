[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array_repr.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array_repr.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array_repr.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array_repr.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array_repr.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array_repr.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array_repr.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array_repr.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array_repr.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array_repr.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array_repr.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array_repr.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array_repr.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array_repr.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array_repr.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array_repr.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array_repr.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array_repr.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array_repr.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array_repr.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array\_repr[#](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy-array-repr "Link to this heading")

=====================================================================================================================================

numpy.array\_repr(_arr_, _max\_line\_width\=None_, _precision\=None_, _suppress\_small\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L1660-L1707)
[#](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "Link to this definition")

Return the string representation of an array.

Parameters:

**arr**ndarray

Input array.

**max\_line\_width**int, optional

Inserts newlines if text is longer than _max\_line\_width_. Defaults to `numpy.get_printoptions()['linewidth']`.

**precision**int, optional

Floating point precision. Defaults to `numpy.get_printoptions()['precision']`.

**suppress\_small**bool, optional

Represent numbers “very close” to zero as zero; default is False. Very close is defined by precision: if the precision is 8, e.g., numbers smaller (in absolute value) than 5e-9 are represented as zero. Defaults to `numpy.get_printoptions()['suppress']`.

Returns:

**string**str

The string representation of an array.

See also

[`array_str`](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str "numpy.array_str")
, [`array2string`](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string "numpy.array2string")
, [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.array\_repr(np.array(\[1,2\]))
'array(\[1, 2\])'
\>>> np.array\_repr(np.ma.array(\[0.\]))
'MaskedArray(\[0.\])'
\>>> np.array\_repr(np.array(\[\], np.int32))
'array(\[\], dtype=int32)'

Copy to clipboard

\>>> x \= np.array(\[1e-6, 4e-7, 2, 3\])
\>>> np.array\_repr(x, precision\=6, suppress\_small\=True)
'array(\[0.000001,  0.      ,  2.      ,  3.      \])'

Copy to clipboard

Go BackOpen In Tab

On this page