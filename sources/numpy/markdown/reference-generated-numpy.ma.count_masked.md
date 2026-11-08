[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.count_masked.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.count_masked.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.count_masked.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.count_masked.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.count_masked.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.count_masked.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.count_masked.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.count_masked.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.count_masked.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.count_masked.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.count_masked.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.count_masked.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.count_masked.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.count_masked.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.count_masked.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.count_masked.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.count_masked.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.count_masked.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.count_masked.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.count_masked.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.count_masked.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.count_masked.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.count\_masked[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.count_masked.html#numpy-ma-count-masked "Link to this heading")

====================================================================================================================================================

ma.count\_masked(_arr_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L66-L117)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.count_masked.html#numpy.ma.count_masked "Link to this definition")

Count the number of masked elements along the given axis.

Parameters:

**arr**array\_like

An array with (possibly) masked elements.

**axis**int, optional

Axis along which to count. If None (default), a flattened version of the array is used.

Returns:

**count**int, ndarray

The total number of masked elements (axis=None) or the number of masked elements along each slice of the given axis.

See also

[`MaskedArray.count`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.count.html#numpy.ma.MaskedArray.count "numpy.ma.MaskedArray.count")

Count non-masked elements.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(9).reshape((3,3))
\>>> a \= np.ma.array(a)
\>>> a\[1, 0\] \= np.ma.masked
\>>> a\[1, 2\] \= np.ma.masked
\>>> a\[2, 1\] \= np.ma.masked
\>>> a
masked\_array(
  data=\[\[0, 1, 2\],\
        \[--, 4, --\],\
        \[6, --, 8\]\],
  mask=\[\[False, False, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)
\>>> np.ma.count\_masked(a)
3

Copy to clipboard

When the _axis_ keyword is used an array is returned.

\>>> np.ma.count\_masked(a, axis\=0)
array(\[1, 1, 1\])
\>>> np.ma.count\_masked(a, axis\=1)
array(\[0, 2, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page