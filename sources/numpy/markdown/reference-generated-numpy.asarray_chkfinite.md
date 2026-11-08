[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.asarray_chkfinite.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.asarray\_chkfinite[#](https://numpy.org/doc/stable/reference/generated/numpy.asarray_chkfinite.html#numpy-asarray-chkfinite "Link to this heading")

==========================================================================================================================================================

numpy.asarray\_chkfinite(_a_, _dtype\=None_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L614-L686)
[#](https://numpy.org/doc/stable/reference/generated/numpy.asarray_chkfinite.html#numpy.asarray_chkfinite "Link to this definition")

Convert the input to an array, checking for NaNs or Infs.

Parameters:

**a**array\_like

Input data, in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays. Success requires no NaNs or Infs.

**dtype**data-type, optional

By default, the data-type is inferred from the input data.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

The memory layout of the output. ‘C’ gives a row-major layout (C-style), ‘F’ gives a column-major layout (Fortran-style). ‘C’ and ‘F’ will copy if needed to ensure the output format. ‘A’ (any) is equivalent to ‘F’ if input a is non-contiguous or Fortran-contiguous, otherwise, it is equivalent to ‘C’. Unlike ‘C’ or ‘F’, ‘A’ does not ensure that the result is contiguous. ‘K’ (keep) preserves the input order for the output. ‘C’ is the default.

Returns:

**out**ndarray

Array interpretation of _a_. No copy is performed if the input is already an ndarray. If _a_ is a subclass of ndarray, a base class ndarray is returned.

Raises:

ValueError

Raises ValueError if _a_ contains NaN (Not a Number) or Inf (Infinity).

See also

[`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")

Create and array.

[`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")

Similar function which passes through subclasses.

[`ascontiguousarray`](https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray "numpy.ascontiguousarray")

Convert input to a contiguous array.

[`asfortranarray`](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#numpy.asfortranarray "numpy.asfortranarray")

Convert input to an ndarray with column-major memory order.

[`fromiter`](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy.fromiter "numpy.fromiter")

Create an array from an iterator.

[`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction")

Construct an array by executing a function on grid positions.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Convert a list into an array. If all elements are finite, then `asarray_chkfinite` is identical to `asarray`.

\>>> a \= \[1, 2\]
\>>> np.asarray\_chkfinite(a, dtype\=np.float64)
array(\[1., 2.\])

Copy to clipboard

Raises ValueError if array\_like contains Nans or Infs.

\>>> a \= \[1, 2, np.inf\]
\>>> try:
...     np.asarray\_chkfinite(a)
... except ValueError:
...     print('ValueError')
...
ValueError

Copy to clipboard

Go BackOpen In Tab

On this page