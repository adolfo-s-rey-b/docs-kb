[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.trim_zeros.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.trim_zeros.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.trim_zeros.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.trim_zeros.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.trim_zeros.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.trim_zeros.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.trim_zeros.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.trim_zeros.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.trim_zeros.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.trim_zeros.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.trim_zeros.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.trim_zeros.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.trim_zeros.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.trim_zeros.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.trim_zeros.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.trim_zeros.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.trim_zeros.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.trim_zeros.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.trim_zeros.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.trim_zeros.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.trim\_zeros[#](https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html#numpy-trim-zeros "Link to this heading")

=====================================================================================================================================

numpy.trim\_zeros(_filt_, _trim\='fb'_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1951-L2047)
[#](https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html#numpy.trim_zeros "Link to this definition")

Remove values along a dimension which are zero along all other.

Parameters:

**filt**array\_like

Input array.

**trim**{“fb”, “f”, “b”}, optional

A string with ‘f’ representing trim from front and ‘b’ to trim from back. By default, zeros are trimmed on both sides. Front and back refer to the edges of a dimension, with “front” referring to the side with the lowest index 0, and “back” referring to the highest index (or index -1).

**axis**int or sequence, optional

If None, _filt_ is cropped such that the smallest bounding box is returned that still contains all values which are not zero. If an axis is specified, _filt_ will be sliced in that dimension only on the sides specified by _trim_. The remaining area will be the smallest that still contains all values which are not zero.

New in version 2.2.0.

Returns:

**trimmed**ndarray or sequence

The result of trimming the input. The number of dimensions and the input data type are preserved.

Notes

For all-zero arrays, the first axis is trimmed first.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array((0, 0, 0, 1, 2, 3, 0, 2, 1, 0))
\>>> np.trim\_zeros(a)
array(\[1, 2, 3, 0, 2, 1\])

Copy to clipboard

\>>> np.trim\_zeros(a, trim\='b')
array(\[0, 0, 0, ..., 0, 2, 1\])

Copy to clipboard

Multiple dimensions are supported.

\>>> b \= np.array(\[\[0, 0, 2, 3, 0, 0\],\
...               \[0, 1, 0, 3, 0, 0\],\
...               \[0, 0, 0, 0, 0, 0\]\])
\>>> np.trim\_zeros(b)
array(\[\[0, 2, 3\],\
       \[1, 0, 3\]\])

Copy to clipboard

\>>> np.trim\_zeros(b, axis\=-1)
array(\[\[0, 2, 3\],\
       \[1, 0, 3\],\
       \[0, 0, 0\]\])

Copy to clipboard

The input data type is preserved, list/tuple in means list/tuple out.

\>>> np.trim\_zeros(\[0, 1, 2, 0\])
\[1, 2\]

Copy to clipboard

Go BackOpen In Tab

On this page