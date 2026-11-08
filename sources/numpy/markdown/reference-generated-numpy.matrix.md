[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy-matrix "Link to this heading")

========================================================================================================================

_class_ numpy.matrix(_data_, _dtype\=None_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L73-L1013)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "Link to this definition")

Returns a matrix from an array-like object, or from a string of data.

A matrix is a specialized 2-D array that retains its 2-D nature through operations. It has certain special operators, such as `*` (matrix multiplication) and `**` (matrix power).

Note

It is no longer recommended to use this class, even for linear algebra. Instead use regular arrays. The class may be removed in the future.

Parameters:

**data**array\_like or string

If [`data`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.data.html#numpy.matrix.data "numpy.matrix.data")
 is a string, it is interpreted as a matrix with commas or spaces separating columns, and semicolons separating rows.

**dtype**data-type

Data-type of the output matrix.

**copy**bool

If [`data`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.data.html#numpy.matrix.data "numpy.matrix.data")
 is already an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, then this flag determines whether the data is copied (the default), or whether a view is constructed.

Attributes:

[`A`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.A.html#numpy.matrix.A "numpy.matrix.A")

Return _self_ as an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 object.

[`A1`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.A1.html#numpy.matrix.A1 "numpy.matrix.A1")

Return _self_ as a flattened [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

[`H`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.H.html#numpy.matrix.H "numpy.matrix.H")

Returns the (complex) conjugate transpose of _self_.

[`I`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.I.html#numpy.matrix.I "numpy.matrix.I")

Returns the (multiplicative) inverse of invertible _self_.

[`T`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.T.html#numpy.matrix.T "numpy.matrix.T")

Returns the transpose of the matrix.

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.base.html#numpy.matrix.base "numpy.matrix.base")

Base object if memory is from some other object.

[`ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ctypes.html#numpy.matrix.ctypes "numpy.matrix.ctypes")

An object to simplify the interaction of the array with the ctypes module.

[`data`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.data.html#numpy.matrix.data "numpy.matrix.data")

Python buffer object pointing to the start of the array’s data.

**device**

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

Data-type of the array’s elements.

[`flags`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flags.html#numpy.matrix.flags "numpy.matrix.flags")

Information about the memory layout of the array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flat.html#numpy.matrix.flat "numpy.matrix.flat")

A 1-D iterator over the array.

[`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")

The imaginary part of the array.

[`itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.itemsize.html#numpy.matrix.itemsize "numpy.matrix.itemsize")

Length of one array element in bytes.

[`mT`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.mT.html#numpy.matrix.mT "numpy.matrix.mT")

View of the matrix transposed array.

[`nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.nbytes.html#numpy.matrix.nbytes "numpy.matrix.nbytes")

Total bytes consumed by the elements of the array.

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")

Number of array dimensions.

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")

The real part of the array.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

Tuple of array dimensions.

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")

Number of elements in the array.

[`strides`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.strides.html#numpy.matrix.strides "numpy.matrix.strides")

Tuple of bytes to step in each dimension when traversing an array.

Methods

|     |     |
| --- | --- |
| [`all`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.all.html#numpy.matrix.all "numpy.matrix.all")<br>(\[axis, out\]) | Test whether all matrix elements along a given axis evaluate to True. |
| [`any`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.any.html#numpy.matrix.any "numpy.matrix.any")<br>(\[axis, out\]) | Test whether any array element along a given axis evaluates to True. |
| [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmax.html#numpy.matrix.argmax "numpy.matrix.argmax")<br>(\[axis, out\]) | Indexes of the maximum values along an axis. |
| [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmin.html#numpy.matrix.argmin "numpy.matrix.argmin")<br>(\[axis, out\]) | Indexes of the minimum values along an axis. |
| [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argpartition.html#numpy.matrix.argpartition "numpy.matrix.argpartition")<br>(kth\[, axis, kind, order\]) | Returns the indices that would partition this array. |
| [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argsort.html#numpy.matrix.argsort "numpy.matrix.argsort")<br>(\[axis, kind, order, stable, descending\]) | Returns the indices that would sort this array. |
| [`astype`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.astype.html#numpy.matrix.astype "numpy.matrix.astype")<br>(dtype\[, order, casting, subok, copy\]) | Copy of the array, cast to a specified type. |
| [`byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.byteswap.html#numpy.matrix.byteswap "numpy.matrix.byteswap")<br>(\[inplace\]) | Swap the bytes of the array elements |
| [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.choose.html#numpy.matrix.choose "numpy.matrix.choose")<br>(choices\[, out, mode\]) | Use an index array to construct a new array from a set of choices. |
| [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.clip.html#numpy.matrix.clip "numpy.matrix.clip")<br>(\[min, max, out\]) | Return an array whose values are limited to `[min, max]`. |
| [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.compress.html#numpy.matrix.compress "numpy.matrix.compress")<br>(condition\[, axis, out\]) | Return selected slices of this array along given axis. |
| [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.conj.html#numpy.matrix.conj "numpy.matrix.conj")<br>() | Complex-conjugate all elements. |
| [`conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.conjugate.html#numpy.matrix.conjugate "numpy.matrix.conjugate")<br>() | Return the complex conjugate, element-wise. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.copy.html#numpy.matrix.copy "numpy.matrix.copy")<br>(\[order\]) | Return a copy of the array. |
| [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.cumprod.html#numpy.matrix.cumprod "numpy.matrix.cumprod")<br>(\[axis, dtype, out\]) | Return the cumulative product of the elements along the given axis. |
| [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.cumsum.html#numpy.matrix.cumsum "numpy.matrix.cumsum")<br>(\[axis, dtype, out\]) | Return the cumulative sum of the elements along the given axis. |
| [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.diagonal.html#numpy.matrix.diagonal "numpy.matrix.diagonal")<br>(\[offset, axis1, axis2\]) | Return specified diagonals. |
| [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.dot.html#numpy.matrix.dot "numpy.matrix.dot")<br>(other, /\[, out\]) | Refer to [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")<br> for full documentation. |
| [`dump`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.dump.html#numpy.matrix.dump "numpy.matrix.dump")<br>(file) | Dump a pickle of the array to the specified file. |
| [`dumps`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.dumps.html#numpy.matrix.dumps "numpy.matrix.dumps")<br>() | Returns the pickle of the array as a string. |
| [`fill`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.fill.html#numpy.matrix.fill "numpy.matrix.fill")<br>(value) | Fill the array with a scalar value. |
| [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flatten.html#numpy.matrix.flatten "numpy.matrix.flatten")<br>(\[order\]) | Return a flattened copy of the matrix. |
| [`getA`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getA.html#numpy.matrix.getA "numpy.matrix.getA")<br>() | Return _self_ as an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")<br> object. |
| [`getA1`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getA1.html#numpy.matrix.getA1 "numpy.matrix.getA1")<br>() | Return _self_ as a flattened [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")<br>. |
| [`getH`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getH.html#numpy.matrix.getH "numpy.matrix.getH")<br>() | Returns the (complex) conjugate transpose of _self_. |
| [`getI`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getI.html#numpy.matrix.getI "numpy.matrix.getI")<br>() | Returns the (multiplicative) inverse of invertible _self_. |
| [`getT`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getT.html#numpy.matrix.getT "numpy.matrix.getT")<br>() | Returns the transpose of the matrix. |
| [`getfield`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getfield.html#numpy.matrix.getfield "numpy.matrix.getfield")<br>(dtype\[, offset\]) | Returns a field of the given array as a certain type. |
| [`item`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.item.html#numpy.matrix.item "numpy.matrix.item")<br>(\*args) | Copy an element of an array to a standard Python scalar and return it. |
| [`max`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.max.html#numpy.matrix.max "numpy.matrix.max")<br>(\[axis, out\]) | Return the maximum value along an axis. |
| [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.mean.html#numpy.matrix.mean "numpy.matrix.mean")<br>(\[axis, dtype, out\]) | Returns the average of the matrix elements along the given axis. |
| [`min`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.min.html#numpy.matrix.min "numpy.matrix.min")<br>(\[axis, out\]) | Return the minimum value along an axis. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.nonzero.html#numpy.matrix.nonzero "numpy.matrix.nonzero")<br>() | Return the indices of the elements that are non-zero. |
| [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.partition.html#numpy.matrix.partition "numpy.matrix.partition")<br>(kth\[, axis, kind, order\]) | Partially sorts the elements in the array in such a way that the value of the element in k-th position is in the position it would be in a sorted array. |
| [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.prod.html#numpy.matrix.prod "numpy.matrix.prod")<br>(\[axis, dtype, out\]) | Return the product of the array elements over the given axis. |
| [`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ptp.html#numpy.matrix.ptp "numpy.matrix.ptp")<br>(\[axis, out\]) | Peak-to-peak (maximum - minimum) value along the given axis. |
| [`put`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.put.html#numpy.matrix.put "numpy.matrix.put")<br>(indices, values\[, mode\]) | Set `a.flat[n] = values[n]` for all `n` in indices. |
| [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ravel.html#numpy.matrix.ravel "numpy.matrix.ravel")<br>(\[order\]) | Return a flattened matrix. |
| [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.repeat.html#numpy.matrix.repeat "numpy.matrix.repeat")<br>(repeats\[, axis\]) | Repeat elements of an array. |
| [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.reshape.html#numpy.matrix.reshape "numpy.matrix.reshape")<br>(a.reshape) | Returns an array containing the same data with a new shape. |
| [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.resize.html#numpy.matrix.resize "numpy.matrix.resize")<br>(a.resize) | Change shape and size of array in-place. |
| [`round`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.round.html#numpy.matrix.round "numpy.matrix.round")<br>(\[decimals, out\]) | Return _a_ with each element rounded to the given number of decimals. |
| [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.searchsorted.html#numpy.matrix.searchsorted "numpy.matrix.searchsorted")<br>(v\[, side, sorter\]) | Find indices where elements of _v_ should be inserted in _a_ to maintain order. |
| [`setfield`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.setfield.html#numpy.matrix.setfield "numpy.matrix.setfield")<br>(val, dtype\[, offset\]) | Put a value into a specified place in a field defined by a data-type. |
| [`setflags`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.setflags.html#numpy.matrix.setflags "numpy.matrix.setflags")<br>(\[write, align, uic\]) | Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY, respectively. |
| [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sort.html#numpy.matrix.sort "numpy.matrix.sort")<br>(\[axis, kind, order, stable, descending\]) | Sort an array in-place. |
| [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.squeeze.html#numpy.matrix.squeeze "numpy.matrix.squeeze")<br>(\[axis\]) | Return a possibly reshaped matrix. |
| [`std`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.std.html#numpy.matrix.std "numpy.matrix.std")<br>(\[axis, dtype, out, ddof\]) | Return the standard deviation of the array elements along the given axis. |
| [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html#numpy.matrix.sum "numpy.matrix.sum")<br>(\[axis, dtype, out\]) | Returns the sum of the matrix elements, along the given axis. |
| [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.swapaxes.html#numpy.matrix.swapaxes "numpy.matrix.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`take`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.take.html#numpy.matrix.take "numpy.matrix.take")<br>(indices\[, axis, out, mode\]) | Return an array formed from the elements of _a_ at the given indices. |
| [`to_device`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.to_device.html#numpy.matrix.to_device "numpy.matrix.to_device")<br>(device, /, \*\[, stream\]) | For Array API compatibility. |
| [`tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.tobytes.html#numpy.matrix.tobytes "numpy.matrix.tobytes")<br>(\[order\]) | Construct Python bytes containing the raw data bytes in the array. |
| [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.tofile.html#numpy.matrix.tofile "numpy.matrix.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |
| [`tolist`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.tolist.html#numpy.matrix.tolist "numpy.matrix.tolist")<br>() | Return the matrix as a (possibly nested) list. |
| [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.trace.html#numpy.matrix.trace "numpy.matrix.trace")<br>(\[offset, axis1, axis2, dtype, out\]) | Return the sum along diagonals of the array. |
| [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.transpose.html#numpy.matrix.transpose "numpy.matrix.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |
| [`var`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.var.html#numpy.matrix.var "numpy.matrix.var")<br>(\[axis, dtype, out, ddof\]) | Returns the variance of the matrix elements, along the given axis. |
| [`view`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.view.html#numpy.matrix.view "numpy.matrix.view")<br>(\[dtype\]\[, type\]) | New view of array with the same data. |

See also

[`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.matrix('1 2; 3 4')
\>>> a
matrix(\[\[1, 2\],\
        \[3, 4\]\])

Copy to clipboard

\>>> np.matrix(\[\[1, 2\], \[3, 4\]\])
matrix(\[\[1, 2\],\
        \[3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page