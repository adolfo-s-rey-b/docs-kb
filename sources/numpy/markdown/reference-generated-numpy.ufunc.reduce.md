[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.reduce.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.reduce.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.reduce.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.reduce.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.reduce.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.reduce.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.reduce.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.reduce.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.reduce.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.reduce.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.reduce.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.reduce.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.reduce.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.reduce.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.reduce.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.reduce.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.reduce.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.reduce.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.reduce.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.reduce.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.reduce[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy-ufunc-reduce "Link to this heading")

==========================================================================================================================================

method

ufunc.reduce(_array_, _axis=0_, _dtype=None_, _out=None_, _keepdims=False_, _initial=<no value>_, _where=True_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "Link to this definition")

Reduces [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
’s dimension by one, by applying ufunc along one axis.

Let \\(array.shape = (N\_0, ..., N\_i, ..., N\_{M-1})\\). Then \\(ufunc.reduce(array, axis=i)\[k\_0, ..,k\_{i-1}, k\_{i+1}, .., k\_{M-1}\]\\) = the result of iterating _j_ over \\(range(N\_i)\\), cumulatively applying ufunc to each \\(array\[k\_0, ..,k\_{i-1}, j, k\_{i+1}, .., k\_{M-1}\]\\). For a one-dimensional array, reduce produces results equivalent to:

r \= op.identity \# op = ufunc
for i in range(len(A)):
  r \= op(r, A\[i\])
return r

Copy to clipboard

For example, add.reduce() is equivalent to sum().

Parameters:

**array**array\_like

The array to act on.

**axis**None or int or tuple of ints, optional

Axis or axes along which a reduction is performed. The default (_axis_ = 0) is perform a reduction over the first dimension of the input array. _axis_ may be negative, in which case it counts from the last to the first axis.

If this is None, a reduction is performed over all the axes. If this is a tuple of ints, a reduction is performed on multiple axes, instead of a single axis or all the axes as before.

For operations which are either not commutative or not associative, doing a reduction over multiple axes is not well-defined. The ufuncs do not currently raise an exception in this case, but will likely do so in the future.

**dtype**data-type code, optional

The data type used to perform the operation. Defaults to that of `out` if given, and the data type of `array` otherwise (though upcast to conserve precision for some cases, such as `numpy.add.reduce` for integer or boolean input).

**out**ndarray, None, …, or tuple of ndarray and None, optional

Location into which the result is stored. If not provided or None, a freshly-allocated array is returned. If passed as a keyword argument, can be Ellipses (`out=...`) to ensure an array is returned even if the result is 0-dimensional (which is useful especially for object dtype), or a 1-element tuple (latter for consistency with `ufunc.__call__`).

New in version 2.3: Support for `out=...` was added.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
.

**initial**scalar, optional

The value with which to start the reduction. If the ufunc has no identity or the dtype is object, this defaults to None - otherwise it defaults to ufunc.identity. If `None` is given, the first element of the reduction is used, and an error is thrown if the reduction is empty.

**where**array\_like of bool, optional

A boolean array which is broadcasted to match the dimensions of [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
, and selects elements to include in the reduction. Note that for ufuncs like `minimum` that do not have an identity defined, one has to pass in also `initial`.

Returns:

**r**ndarray

The reduced array. If _out_ was supplied, _r_ is a reference to it.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.multiply.reduce(\[2,3,5\])
30

Copy to clipboard

A multi-dimensional array example:

\>>> X \= np.arange(8).reshape((2,2,2))
\>>> X
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> np.add.reduce(X, 0)
array(\[\[ 4,  6\],\
       \[ 8, 10\]\])
\>>> np.add.reduce(X) \# confirm: default axis value is 0
array(\[\[ 4,  6\],\
       \[ 8, 10\]\])
\>>> np.add.reduce(X, 1)
array(\[\[ 2,  4\],\
       \[10, 12\]\])
\>>> np.add.reduce(X, 2)
array(\[\[ 1,  5\],\
       \[ 9, 13\]\])

Copy to clipboard

You can use the `initial` keyword argument to initialize the reduction with a different value, and `where` to select specific elements to include:

\>>> np.add.reduce(\[10\], initial\=5)
15
\>>> np.add.reduce(np.ones((2, 2, 2)), axis\=(0, 2), initial\=10)
array(\[14., 14.\])
\>>> a \= np.array(\[10., np.nan, 10\])
\>>> np.add.reduce(a, where\=~np.isnan(a))
20.0

Copy to clipboard

Allows reductions of empty arrays where they would normally fail, i.e. for ufuncs without an identity.

\>>> np.minimum.reduce(\[\], initial\=np.inf)
inf
\>>> np.minimum.reduce(\[\[1., 2.\], \[3., 4.\]\], initial\=10., where\=\[True, False\])
array(\[ 1., 10.\])
\>>> np.minimum.reduce(\[\])
Traceback (most recent call last):
    ...
ValueError: zero-size array to reduction operation minimum which has no identity

Copy to clipboard

Go BackOpen In Tab

On this page