[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy-ndarray "Link to this heading")

===========================================================================================================================

_class_ numpy.ndarray(_shape_, _dtype\=np.float64_, _buffer\=None_, _offset\=0_, _strides\=None_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/src/multiarray/arrayobject.c)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "Link to this definition")

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

[`T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T "numpy.ndarray.T")
ndarray

View of the transposed array.

[`data`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.data.html#numpy.ndarray.data "numpy.ndarray.data")
buffer

Python buffer object pointing to the start of the array’s data.

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
dtype object

Data-type of the array’s elements.

[`flags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags "numpy.ndarray.flags")
dict

Information about the memory layout of the array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat")
numpy.flatiter object

A 1-D iterator over the array.

[`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")
ndarray

The imaginary part of the array.

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")
ndarray

The real part of the array.

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")
int

Number of elements in the array.

[`itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.itemsize.html#numpy.ndarray.itemsize "numpy.ndarray.itemsize")
int

Length of one array element in bytes.

[`nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nbytes.html#numpy.ndarray.nbytes "numpy.ndarray.nbytes")
int

Total bytes consumed by the elements of the array.

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")
int

Number of array dimensions.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
tuple of ints

Tuple of array dimensions.

[`strides`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides "numpy.ndarray.strides")
tuple of ints

Tuple of bytes to step in each dimension when traversing an array.

[`ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ctypes.html#numpy.ndarray.ctypes "numpy.ndarray.ctypes")
ctypes object

An object to simplify the interaction of the array with the ctypes module.

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base")
ndarray

Base object if memory is from some other object.

Methods

|     |     |
| --- | --- |
| [`all`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")<br>(\[axis, out, keepdims, where\]) | Returns True if all elements evaluate to True. |
| [`any`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html#numpy.ndarray.any "numpy.ndarray.any")<br>(\[axis, out, keepdims, where\]) | Returns True if any of the elements of _a_ evaluate to True. |
| [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")<br>(\[axis, out, keepdims\]) | Return indices of the maximum values along the given axis. |
| [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "numpy.ndarray.argmin")<br>(\[axis, out, keepdims\]) | Return indices of the minimum values along the given axis. |
| [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argpartition.html#numpy.ndarray.argpartition "numpy.ndarray.argpartition")<br>(kth\[, axis, kind, order\]) | Returns the indices that would partition this array. |
| [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argsort.html#numpy.ndarray.argsort "numpy.ndarray.argsort")<br>(\[axis, kind, order, stable, descending\]) | Returns the indices that would sort this array. |
| [`astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")<br>(dtype\[, order, casting, subok, copy\]) | Copy of the array, cast to a specified type. |
| [`byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.byteswap.html#numpy.ndarray.byteswap "numpy.ndarray.byteswap")<br>(\[inplace\]) | Swap the bytes of the array elements |
| [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.choose.html#numpy.ndarray.choose "numpy.ndarray.choose")<br>(choices\[, out, mode\]) | Use an index array to construct a new array from a set of choices. |
| [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.clip.html#numpy.ndarray.clip "numpy.ndarray.clip")<br>(\[min, max, out\]) | Return an array whose values are limited to `[min, max]`. |
| [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.compress.html#numpy.ndarray.compress "numpy.ndarray.compress")<br>(condition\[, axis, out\]) | Return selected slices of this array along given axis. |
| [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conj.html#numpy.ndarray.conj "numpy.ndarray.conj")<br>() | Complex-conjugate all elements. |
| [`conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conjugate.html#numpy.ndarray.conjugate "numpy.ndarray.conjugate")<br>() | Return the complex conjugate, element-wise. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")<br>(\[order\]) | Return a copy of the array. |
| [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html#numpy.ndarray.cumprod "numpy.ndarray.cumprod")<br>(\[axis, dtype, out\]) | Return the cumulative product of the elements along the given axis. |
| [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumsum.html#numpy.ndarray.cumsum "numpy.ndarray.cumsum")<br>(\[axis, dtype, out\]) | Return the cumulative sum of the elements along the given axis. |
| [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.diagonal.html#numpy.ndarray.diagonal "numpy.ndarray.diagonal")<br>(\[offset, axis1, axis2\]) | Return specified diagonals. |
| [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dot.html#numpy.ndarray.dot "numpy.ndarray.dot")<br>(other, /\[, out\]) | Refer to [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")<br> for full documentation. |
| [`dump`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dump.html#numpy.ndarray.dump "numpy.ndarray.dump")<br>(file) | Dump a pickle of the array to the specified file. |
| [`dumps`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dumps.html#numpy.ndarray.dumps "numpy.ndarray.dumps")<br>() | Returns the pickle of the array as a string. |
| [`fill`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill")<br>(value) | Fill the array with a scalar value. |
| [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |
| [`getfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.getfield.html#numpy.ndarray.getfield "numpy.ndarray.getfield")<br>(dtype\[, offset\]) | Returns a field of the given array as a certain type. |
| [`item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item")<br>(\*args) | Copy an element of an array to a standard Python scalar and return it. |
| [`max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")<br>(\[axis, out, keepdims, initial, where\]) | Return the maximum along a given axis. |
| [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#numpy.ndarray.mean "numpy.ndarray.mean")<br>(\[axis, dtype, out, keepdims, where\]) | Returns the average of the array elements along given axis. |
| [`min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")<br>(\[axis, out, keepdims, initial, where\]) | Return the minimum along a given axis. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero")<br>() | Return the indices of the elements that are non-zero. |
| [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.partition.html#numpy.ndarray.partition "numpy.ndarray.partition")<br>(kth\[, axis, kind, order\]) | Partially sorts the elements in the array in such a way that the value of the element in k-th position is in the position it would be in a sorted array. |
| [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")<br>(\[axis, dtype, out, keepdims, initial, ...\]) | Return the product of the array elements over the given axis |
| [`put`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.put.html#numpy.ndarray.put "numpy.ndarray.put")<br>(indices, values\[, mode\]) | Set `a.flat[n] = values[n]` for all `n` in indices. |
| [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html#numpy.ndarray.ravel "numpy.ndarray.ravel")<br>(\[order\]) | Return a flattened array. |
| [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.repeat.html#numpy.ndarray.repeat "numpy.ndarray.repeat")<br>(repeats\[, axis\]) | Repeat elements of an array. |
| [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")<br>(a.reshape) | Returns an array containing the same data with a new shape. |
| [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize")<br>(a.resize) | Change shape and size of array in-place. |
| [`round`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round "numpy.ndarray.round")<br>(\[decimals, out\]) | Return _a_ with each element rounded to the given number of decimals. |
| [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.searchsorted.html#numpy.ndarray.searchsorted "numpy.ndarray.searchsorted")<br>(v\[, side, sorter\]) | Find indices where elements of _v_ should be inserted in _a_ to maintain order. |
| [`setfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setfield.html#numpy.ndarray.setfield "numpy.ndarray.setfield")<br>(val, dtype\[, offset\]) | Put a value into a specified place in a field defined by a data-type. |
| [`setflags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setflags.html#numpy.ndarray.setflags "numpy.ndarray.setflags")<br>(\[write, align, uic\]) | Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY, respectively. |
| [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")<br>(\[axis, kind, order, stable, descending\]) | Sort an array in-place. |
| [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.squeeze.html#numpy.ndarray.squeeze "numpy.ndarray.squeeze")<br>(\[axis\]) | Remove axes of length one from _a_. |
| [`std`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html#numpy.ndarray.std "numpy.ndarray.std")<br>(\[axis, dtype, out, ddof, keepdims, ...\]) | Returns the standard deviation of the array elements along given axis. |
| [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")<br>(\[axis, dtype, out, keepdims, initial, where\]) | Return the sum of the array elements over the given axis. |
| [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.swapaxes.html#numpy.ndarray.swapaxes "numpy.ndarray.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`take`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "numpy.ndarray.take")<br>(indices\[, axis, out, mode\]) | Return an array formed from the elements of _a_ at the given indices. |
| [`to_device`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.to_device.html#numpy.ndarray.to_device "numpy.ndarray.to_device")<br>(device, /, \*\[, stream\]) | For Array API compatibility. |
| [`tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")<br>(\[order\]) | Construct Python bytes containing the raw data bytes in the array. |
| [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |
| [`tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist "numpy.ndarray.tolist")<br>() | Return the array as an `a.ndim`\-levels deep nested list of Python scalars. |
| [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.trace.html#numpy.ndarray.trace "numpy.ndarray.trace")<br>(\[offset, axis1, axis2, dtype, out\]) | Return the sum along diagonals of the array. |
| [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |
| [`var`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.var.html#numpy.ndarray.var "numpy.ndarray.var")<br>(\[axis, dtype, out, ddof, keepdims, ...\]) | Returns the variance of the array elements, along given axis. |
| [`view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")<br>(\[dtype\]\[, type\]) | New view of array with the same data. |

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