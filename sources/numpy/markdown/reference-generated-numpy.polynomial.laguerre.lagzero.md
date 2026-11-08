[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagzero.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.laguerre.lagzero.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.laguerre.lagzero.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.laguerre.lagzero[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagzero.html#numpy-polynomial-laguerre-lagzero "Link to this heading")

=======================================================================================================================================================================================

polynomial.laguerre.lagzero _\= array(\[0\])_[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagzero.html#numpy.polynomial.laguerre.lagzero "Link to this definition")

ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) –

ndarray(shape, dtype=np.float64, buffer=None, offset=0, strides=None, order=None)

An array object represents a multidimensional, homogeneous array of fixed-size items. An associated data-type object describes the format of each element in the array (its byte-order, how many bytes it occupies in memory, whether it is an integer, a floating point number, or something else, etc.)

Arrays should be constructed using [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
, [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
 or [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
 (refer to the See Also section below). The parameters given here refer to a low-level method (_ndarray(…)_) for instantiating an array.

For more information, refer to the [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
 module and examine the methods and attributes of an array.

Parameters:

**(for the \_\_new\_\_ method; see Notes below)**

**shape**tuple of ints

Shape of created array.

**dtype**data-type, optional

Any object that can be interpreted as a numpy data type. Default is [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
.

**buffer**object exposing buffer interface, optional

Used to fill the array with data.

**offset**int, optional

Offset of array data in buffer.

**strides**tuple of ints, optional

Strides of data in memory.

**order**{‘C’, ‘F’}, optional

Row-major (C-style) or column-major (Fortran-style) order.

Attributes:

**T**ndarray

Transpose of the array.

**data**buffer

The array’s elements, in memory.

**dtype**dtype object

Describes the format of the elements in the array.

**flags**dict

Dictionary containing information related to memory use, e.g., ‘C\_CONTIGUOUS’, ‘OWNDATA’, ‘WRITEABLE’, etc.

**flat**numpy.flatiter object

Flattened version of the array as an iterator. The iterator allows assignments, e.g., `x.flat = 3` (See [`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat")
 for assignment examples; TODO).

**imag**ndarray

Imaginary part of the array.

**real**ndarray

Real part of the array.

**size**int

Number of elements in the array.

**itemsize**int

The memory use of each array element in bytes.

**nbytes**int

The total number of bytes required to store the array data, i.e., `itemsize * size`.

**ndim**int

The array’s number of dimensions.

**shape**tuple of ints

Shape of the array.

**strides**tuple of ints

The step-size required to move from one element to the next in memory. For example, a contiguous `(3, 4)` array of type `int16` in C-order has strides `(8, 2)`. This implies that to move from element to element in memory requires jumps of 2 bytes. To move from row-to-row, one needs to jump 8 bytes at a time (`2 * 4`).

**ctypes**ctypes object

Class containing properties of the array needed for interaction with ctypes.

**base**ndarray

If the array is a view into another array, that array is its _base_ (unless that array is also a view). The _base_ array is where the array data is actually stored.

See also

[`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")

Construct an array.

[`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")

Create an array, each element of which is zero.

[`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")

Create an array, but leave its allocated memory unchanged (i.e., it contains “garbage”).

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

Create a data-type.

[`numpy.typing.NDArray`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NDArray "numpy.typing.NDArray")

An ndarray alias [generic](https://docs.python.org/3/glossary.html#term-generic-type "(in Python v3.14)")
 w.r.t. its [`dtype.type`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.type.html#numpy.dtype.type "numpy.dtype.type")
.

Notes

There are two modes of creating an array using `__new__`:

1.  If _buffer_ is None, then only [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
    , [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
    , and _order_ are used.
    
2.  If _buffer_ is an object exposing the buffer interface, then all keywords are interpreted.
    

No `__init__` method is needed because the array is fully initialized after the `__new__` method.

Examples

Try it in your browser!

These examples illustrate the low-level [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 constructor. Refer to the _See Also_ section above for easier ways of constructing an ndarray.

First mode, _buffer_ is None:

\>>> import numpy as np
\>>> np.ndarray(shape\=(2,2), dtype\=np.float64, order\='F')
array(\[\[0.0e+000, 0.0e+000\], # random\
       \[     nan, 2.5e-323\]\])

Copy to clipboard

Second mode:

\>>> np.ndarray((2,), buffer\=np.array(\[1,2,3\]),
...            offset\=np.int\_().itemsize,
...            dtype\=np.int\_) \# offset = 1\*itemsize, i.e. skip first element
array(\[2, 3\])

Copy to clipboard

Go BackOpen In Tab

On this page