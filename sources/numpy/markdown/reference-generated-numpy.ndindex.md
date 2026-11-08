[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndindex.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndindex.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndindex.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndindex.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndindex.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndindex.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndindex.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndindex.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndindex.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndindex.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndindex.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndindex.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndindex.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndindex.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndindex.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndindex.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndindex.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndindex.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndindex.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndindex.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndindex[#](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy-ndindex "Link to this heading")

===========================================================================================================================

_class_ numpy.ndindex(_\*shape_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_index_tricks_impl.py#L640-L709)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "Link to this definition")

An N-dimensional iterator object to index arrays.

Given the shape of an array, an [`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")
 instance iterates over the N-dimensional index of the array. At each iteration a tuple of indices is returned, the last dimension is iterated over first.

Parameters:

**shape**ints, or a single tuple of ints

The size of each dimension of the array can be passed as individual parameters or as the elements of a tuple.

See also

[`ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")
, [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Dimensions as individual arguments

\>>> for index in np.ndindex(3, 2, 1):
...     print(index)
(0, 0, 0)
(0, 1, 0)
(1, 0, 0)
(1, 1, 0)
(2, 0, 0)
(2, 1, 0)

Copy to clipboard

Same dimensions - but in a tuple `(3, 2, 1)`

\>>> for index in np.ndindex((3, 2, 1)):
...     print(index)
(0, 0, 0)
(0, 1, 0)
(1, 0, 0)
(1, 1, 0)
(2, 0, 0)
(2, 1, 0)

Copy to clipboard

Go BackOpen In Tab

On this page