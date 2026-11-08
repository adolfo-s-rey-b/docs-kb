[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.asarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.asarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.asarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.asarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.asarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.asarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.asarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.asarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.asarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.asarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.asarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.asarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.asarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.asarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.asarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.asarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.asarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.asarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.asarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.asarray[#](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy-asarray "Link to this heading")

===========================================================================================================================

numpy.asarray(_a_, _dtype\=None_, _order\=None_, _\*_, _device\=None_, _copy\=None_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "Link to this definition")

Convert the input to an array.

Parameters:

**a**array\_like

Input data, in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.

**dtype**data-type, optional

By default, the data-type is inferred from the input data.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

The memory layout of the output. ‘C’ gives a row-major layout (C-style), ‘F’ gives a column-major layout (Fortran-style). ‘C’ and ‘F’ will copy if needed to ensure the output format. ‘A’ (any) is equivalent to ‘F’ if input a is non-contiguous or Fortran-contiguous, otherwise, it is equivalent to ‘C’. Unlike ‘C’ or ‘F’, ‘A’ does not ensure that the result is contiguous. ‘K’ (keep) is the default and preserves the input order for the output.

**device**str, optional

The device on which to place the created array. Default: `None`. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

**copy**bool, optional

If `True`, then the object is copied. If `None` then the object is copied only if needed, i.e. if `__array__` returns a copy, if obj is a nested sequence, or if a copy is needed to satisfy any of the other requirements (`dtype`, `order`, etc.). For `False` it raises a `ValueError` if a copy cannot be avoided. Default: `None`.

New in version 2.0.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

Array interpretation of `a`. No copy is performed if the input is already an ndarray with matching dtype and order. If `a` is a subclass of ndarray, a base class ndarray is returned.

See also

[`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")

Similar function which passes through subclasses.

[`ascontiguousarray`](https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray "numpy.ascontiguousarray")

Convert input to a contiguous array.

[`asfortranarray`](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#numpy.asfortranarray "numpy.asfortranarray")

Convert input to an ndarray with column-major memory order.

[`asarray_chkfinite`](https://numpy.org/doc/stable/reference/generated/numpy.asarray_chkfinite.html#numpy.asarray_chkfinite "numpy.asarray_chkfinite")

Similar function which checks input for NaNs and Infs.

[`fromiter`](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy.fromiter "numpy.fromiter")

Create an array from an iterator.

[`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction")

Construct an array by executing a function on grid positions.

Examples

Try it in your browser!

Convert a list into an array:

\>>> a \= \[1, 2\]
\>>> import numpy as np
\>>> np.asarray(a)
array(\[1, 2\])

Copy to clipboard

Existing arrays are not copied:

\>>> a \= np.array(\[1, 2\])
\>>> np.asarray(a) is a
True

Copy to clipboard

If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is set, array is copied only if dtype does not match:

\>>> a \= np.array(\[1, 2\], dtype\=np.float32)
\>>> np.shares\_memory(np.asarray(a, dtype\=np.float32), a)
True
\>>> np.shares\_memory(np.asarray(a, dtype\=np.float64), a)
False

Copy to clipboard

Contrary to [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")
, ndarray subclasses are not passed through:

\>>> issubclass(np.recarray, np.ndarray)
True
\>>> a \= np.array(\[(1., 2), (3., 4)\], dtype\='f4,i4').view(np.recarray)
\>>> np.asarray(a) is a
False
\>>> np.asanyarray(a) is a
True

Copy to clipboard

Go BackOpen In Tab

On this page