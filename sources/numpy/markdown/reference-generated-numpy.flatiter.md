[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.flatiter.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.flatiter.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.flatiter.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.flatiter.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.flatiter.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.flatiter.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.flatiter.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.flatiter.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.flatiter.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.flatiter.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.flatiter.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.flatiter.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.flatiter.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.flatiter.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.flatiter.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.flatiter.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.flatiter.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.flatiter.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.flatiter.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.flatiter.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.flatiter[#](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy-flatiter "Link to this heading")

==============================================================================================================================

_class_ numpy.flatiter[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "Link to this definition")

Flat iterator object to iterate over arrays.

A [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
 iterator is returned by `x.flat` for any array _x_. It allows iterating over the array as if it were a 1-D array, either in a for-loop or by calling its _next_ method.

Iteration is done in row-major, C-style order (the last index varying the fastest). The iterator can also be indexed using basic slicing or advanced indexing.

Attributes:

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.base.html#numpy.flatiter.base "numpy.flatiter.base")

A reference to the array that is iterated over.

[`coords`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.coords.html#numpy.flatiter.coords "numpy.flatiter.coords")

An N-dimensional tuple of current coordinates.

[`index`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.index.html#numpy.flatiter.index "numpy.flatiter.index")

Current flat index into the array.

Methods

|     |     |
| --- | --- |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.copy.html#numpy.flatiter.copy "numpy.flatiter.copy")<br>() | Get a copy of the iterator as a 1-D array. |

See also

[`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat")

Return a flat iterator over an array.

[`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")

Returns a flattened copy of an array.

Notes

A [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
 iterator can not be constructed directly from Python code by calling the [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
 constructor.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(6).reshape(2, 3)
\>>> fl \= x.flat
\>>> type(fl)
<class 'numpy.flatiter'>
\>>> for item in fl:
...     print(item)
...
0
1
2
3
4
5

Copy to clipboard

\>>> fl\[2:4\]
array(\[2, 3\])

Copy to clipboard

Go BackOpen In Tab

On this page