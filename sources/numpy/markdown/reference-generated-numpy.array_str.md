[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array_str.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array_str.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array_str.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array_str.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array_str.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array_str.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array_str.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array_str.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array_str.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array_str.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array_str.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array_str.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array_str.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array_str.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array_str.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array_str.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array_str.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array_str.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array_str.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array_str.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array\_str[#](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy-array-str "Link to this heading")

==================================================================================================================================

numpy.array\_str(_a_, _max\_line\_width\=None_, _precision\=None_, _suppress\_small\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L1742-L1780)
[#](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str "Link to this definition")

Return a string representation of the data in an array.

The data in the array is returned as a single string. This function is similar to [`array_repr`](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "numpy.array_repr")
, the difference being that [`array_repr`](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "numpy.array_repr")
 also returns information on the kind of array and its data type.

Parameters:

**a**ndarray

Input array.

**max\_line\_width**int, optional

Inserts newlines if text is longer than _max\_line\_width_. Defaults to `numpy.get_printoptions()['linewidth']`.

**precision**int, optional

Floating point precision. Defaults to `numpy.get_printoptions()['precision']`.

**suppress\_small**bool, optional

Represent numbers “very close” to zero as zero; default is False. Very close is defined by precision: if the precision is 8, e.g., numbers smaller (in absolute value) than 5e-9 are represented as zero. Defaults to `numpy.get_printoptions()['suppress']`.

See also

[`array2string`](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string "numpy.array2string")
, [`array_repr`](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "numpy.array_repr")
, [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.array\_str(np.arange(3))
'\[0 1 2\]'

Copy to clipboard

Go BackOpen In Tab

On this page