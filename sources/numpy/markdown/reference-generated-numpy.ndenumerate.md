[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndenumerate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndenumerate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndenumerate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndenumerate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndenumerate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndenumerate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndenumerate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndenumerate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndenumerate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndenumerate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndenumerate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndenumerate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndenumerate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndenumerate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndenumerate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndenumerate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndenumerate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndenumerate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndenumerate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndenumerate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndenumerate[#](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy-ndenumerate "Link to this heading")

=======================================================================================================================================

_class_ numpy.ndenumerate(_arr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_index_tricks_impl.py#L590-L637)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "Link to this definition")

Multidimensional index iterator.

Return an iterator yielding pairs of array coordinates and values.

Parameters:

**arr**ndarray

Input array.

See also

[`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")
, [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> for index, x in np.ndenumerate(a):
...     print(index, x)
(0, 0) 1
(0, 1) 2
(1, 0) 3
(1, 1) 4

Copy to clipboard

Go BackOpen In Tab

On this page