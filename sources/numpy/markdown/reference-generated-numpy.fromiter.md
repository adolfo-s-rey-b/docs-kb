[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fromiter.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fromiter.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fromiter.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fromiter.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fromiter.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fromiter.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fromiter.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fromiter.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fromiter.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fromiter.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fromiter.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fromiter.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fromiter.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fromiter.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fromiter.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fromiter.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fromiter.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fromiter.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fromiter.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fromiter[#](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy-fromiter "Link to this heading")

==============================================================================================================================

numpy.fromiter(_iter_, _dtype_, _count\=\-1_, _\*_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy.fromiter "Link to this definition")

Create a new 1-dimensional array from an iterable object.

Parameters:

**iter**iterable object

An iterable object providing data for the array.

**dtype**data-type

The data-type of the returned array.

Changed in version 1.23: Object and subarray dtypes are now supported (note that the final result is not 1-D for a subarray dtype).

**count**int, optional

The number of items to read from _iterable_. The default is -1, which means all data is read.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

The output array.

Notes

Specify _count_ to improve performance. It allows `fromiter` to pre-allocate the output array, instead of resizing it on demand.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> iterable \= (x\*x for x in range(5))
\>>> np.fromiter(iterable, float)
array(\[  0.,   1.,   4.,   9.,  16.\])

Copy to clipboard

A carefully constructed subarray dtype will lead to higher dimensional results:

\>>> iterable \= ((x+1, x+2) for x in range(5))
\>>> np.fromiter(iterable, dtype\=np.dtype((int, 2)))
array(\[\[1, 2\],\
       \[2, 3\],\
       \[3, 4\],\
       \[4, 5\],\
       \[5, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page