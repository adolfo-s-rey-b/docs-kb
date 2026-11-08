[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.recarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.recarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.recarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.recarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.recarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.recarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.recarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.recarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.recarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.recarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.recarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.recarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.recarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.recarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.recarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.recarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.recarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.recarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.recarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.recarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.recarray[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy-recarray "Link to this heading")

==============================================================================================================================

_class_ numpy.recarray(_shape_, _dtype\=None_, _buf\=None_, _offset\=0_, _strides\=None_, _formats\=None_, _names\=None_, _titles\=None_, _byteorder\=None_, _aligned\=False_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L278-L554)
[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "Link to this definition")

Construct an ndarray that allows field access using attributes.

Arrays may have a data-types containing fields, analogous to columns in a spread sheet. An example is `[(x, int), (y, float)]`, where each entry in the array is a pair of `(int, float)`. Normally, these attributes are accessed using dictionary lookups such as `arr['x']` and `arr['y']`. Record arrays allow the fields to be accessed as members of the array, using `arr.x` and `arr.y`.

Parameters:

**shape**tuple

Shape of output array.

**dtype**data-type, optional

The desired data-type. By default, the data-type is determined from _formats_, _names_, _titles_, _aligned_ and _byteorder_.

**formats**list of data-types, optional

A list containing the data-types for the different columns, e.g. `['i4', 'f8', 'i4']`. _formats_ does _not_ support the new convention of using types directly, i.e. `(int, float, int)`. Note that _formats_ must be a list, not a tuple. Given that _formats_ is somewhat limited, we recommend specifying [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 instead.

**names**tuple of str, optional

The name of each column, e.g. `('x', 'y', 'z')`.

**buf**buffer, optional

By default, a new array is created of the given shape and data-type. If _buf_ is specified and is an object exposing the buffer interface, the array will use the memory from the existing buffer. In this case, the _offset_ and [`strides`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.strides.html#numpy.recarray.strides "numpy.recarray.strides")
 keywords are available.

Attributes:

[`T`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.T.html#numpy.recarray.T "numpy.recarray.T")

View of the transposed array.

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.base.html#numpy.recarray.base "numpy.recarray.base")

Base object if memory is from some other object.

[`ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.ctypes.html#numpy.recarray.ctypes "numpy.recarray.ctypes")

An object to simplify the interaction of the array with the ctypes module.

[`data`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.data.html#numpy.recarray.data "numpy.recarray.data")

Python buffer object pointing to the start of the array’s data.

**device**

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

Data-type of the array’s elements.

[`flags`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.flags.html#numpy.recarray.flags "numpy.recarray.flags")

Information about the memory layout of the array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.flat.html#numpy.recarray.flat "numpy.recarray.flat")

A 1-D iterator over the array.

[`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")

The imaginary part of the array.

[`itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.itemsize.html#numpy.recarray.itemsize "numpy.recarray.itemsize")

Length of one array element in bytes.

[`mT`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.mT.html#numpy.recarray.mT "numpy.recarray.mT")

View of the matrix transposed array.

[`nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.nbytes.html#numpy.recarray.nbytes "numpy.recarray.nbytes")

Total bytes consumed by the elements of the array.

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")

Number of array dimensions.

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")

The real part of the array.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

Tuple of array dimensions.

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")

Number of elements in the array.

[`strides`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.strides.html#numpy.recarray.strides "numpy.recarray.strides")

Tuple of bytes to step in each dimension when traversing an array.

Methods

|     |     |
| --- | --- |
| [`all`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.all.html#numpy.recarray.all "numpy.recarray.all")<br>(\[axis, out, keepdims, where\]) | Returns True if all elements evaluate to True. |
| [`any`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.any.html#numpy.recarray.any "numpy.recarray.any")<br>(\[axis, out, keepdims, where\]) | Returns True if any of the elements of _a_ evaluate to True. |
| [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.argmax.html#numpy.recarray.argmax "numpy.recarray.argmax")<br>(\[axis, out, keepdims\]) | Return indices of the maximum values along the given axis. |
| [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.argmin.html#numpy.recarray.argmin "numpy.recarray.argmin")<br>(\[axis, out, keepdims\]) | Return indices of the minimum values along the given axis. |
| [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.argpartition.html#numpy.recarray.argpartition "numpy.recarray.argpartition")<br>(kth\[, axis, kind, order\]) | Returns the indices that would partition this array. |
| [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.argsort.html#numpy.recarray.argsort "numpy.recarray.argsort")<br>(\[axis, kind, order, stable, descending\]) | Returns the indices that would sort this array. |
| [`astype`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.astype.html#numpy.recarray.astype "numpy.recarray.astype")<br>(dtype\[, order, casting, subok, copy\]) | Copy of the array, cast to a specified type. |
| [`byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.byteswap.html#numpy.recarray.byteswap "numpy.recarray.byteswap")<br>(\[inplace\]) | Swap the bytes of the array elements |
| [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.choose.html#numpy.recarray.choose "numpy.recarray.choose")<br>(choices\[, out, mode\]) | Use an index array to construct a new array from a set of choices. |
| [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.clip.html#numpy.recarray.clip "numpy.recarray.clip")<br>(\[min, max, out\]) | Return an array whose values are limited to `[min, max]`. |
| [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.compress.html#numpy.recarray.compress "numpy.recarray.compress")<br>(condition\[, axis, out\]) | Return selected slices of this array along given axis. |
| [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.conj.html#numpy.recarray.conj "numpy.recarray.conj")<br>() | Complex-conjugate all elements. |
| [`conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.conjugate.html#numpy.recarray.conjugate "numpy.recarray.conjugate")<br>() | Return the complex conjugate, element-wise. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.copy.html#numpy.recarray.copy "numpy.recarray.copy")<br>(\[order\]) | Return a copy of the array. |
| [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.cumprod.html#numpy.recarray.cumprod "numpy.recarray.cumprod")<br>(\[axis, dtype, out\]) | Return the cumulative product of the elements along the given axis. |
| [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.cumsum.html#numpy.recarray.cumsum "numpy.recarray.cumsum")<br>(\[axis, dtype, out\]) | Return the cumulative sum of the elements along the given axis. |
| [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.diagonal.html#numpy.recarray.diagonal "numpy.recarray.diagonal")<br>(\[offset, axis1, axis2\]) | Return specified diagonals. |
| [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.dot.html#numpy.recarray.dot "numpy.recarray.dot")<br>(other, /\[, out\]) | Refer to [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")<br> for full documentation. |
| [`dump`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.dump.html#numpy.recarray.dump "numpy.recarray.dump")<br>(file) | Dump a pickle of the array to the specified file. |
| [`dumps`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.dumps.html#numpy.recarray.dumps "numpy.recarray.dumps")<br>() | Returns the pickle of the array as a string. |
| [`fill`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.fill.html#numpy.recarray.fill "numpy.recarray.fill")<br>(value) | Fill the array with a scalar value. |
| [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.flatten.html#numpy.recarray.flatten "numpy.recarray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |
| [`getfield`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.getfield.html#numpy.recarray.getfield "numpy.recarray.getfield")<br>(dtype\[, offset\]) | Returns a field of the given array as a certain type. |
| [`item`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.item.html#numpy.recarray.item "numpy.recarray.item")<br>(\*args) | Copy an element of an array to a standard Python scalar and return it. |
| [`max`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.max.html#numpy.recarray.max "numpy.recarray.max")<br>(\[axis, out, keepdims, initial, where\]) | Return the maximum along a given axis. |
| [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.mean.html#numpy.recarray.mean "numpy.recarray.mean")<br>(\[axis, dtype, out, keepdims, where\]) | Returns the average of the array elements along given axis. |
| [`min`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.min.html#numpy.recarray.min "numpy.recarray.min")<br>(\[axis, out, keepdims, initial, where\]) | Return the minimum along a given axis. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.nonzero.html#numpy.recarray.nonzero "numpy.recarray.nonzero")<br>() | Return the indices of the elements that are non-zero. |
| [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.partition.html#numpy.recarray.partition "numpy.recarray.partition")<br>(kth\[, axis, kind, order\]) | Partially sorts the elements in the array in such a way that the value of the element in k-th position is in the position it would be in a sorted array. |
| [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.prod.html#numpy.recarray.prod "numpy.recarray.prod")<br>(\[axis, dtype, out, keepdims, initial, ...\]) | Return the product of the array elements over the given axis |
| [`put`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.put.html#numpy.recarray.put "numpy.recarray.put")<br>(indices, values\[, mode\]) | Set `a.flat[n] = values[n]` for all `n` in indices. |
| [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.ravel.html#numpy.recarray.ravel "numpy.recarray.ravel")<br>(\[order\]) | Return a flattened array. |
| [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.repeat.html#numpy.recarray.repeat "numpy.recarray.repeat")<br>(repeats\[, axis\]) | Repeat elements of an array. |
| [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.reshape.html#numpy.recarray.reshape "numpy.recarray.reshape")<br>(a.reshape) | Returns an array containing the same data with a new shape. |
| [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.resize.html#numpy.recarray.resize "numpy.recarray.resize")<br>(a.resize) | Change shape and size of array in-place. |
| [`round`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.round.html#numpy.recarray.round "numpy.recarray.round")<br>(\[decimals, out\]) | Return _a_ with each element rounded to the given number of decimals. |
| [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.searchsorted.html#numpy.recarray.searchsorted "numpy.recarray.searchsorted")<br>(v\[, side, sorter\]) | Find indices where elements of _v_ should be inserted in _a_ to maintain order. |
| [`setfield`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.setfield.html#numpy.recarray.setfield "numpy.recarray.setfield")<br>(val, dtype\[, offset\]) | Put a value into a specified place in a field defined by a data-type. |
| [`setflags`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.setflags.html#numpy.recarray.setflags "numpy.recarray.setflags")<br>(\[write, align, uic\]) | Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY, respectively. |
| [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.sort.html#numpy.recarray.sort "numpy.recarray.sort")<br>(\[axis, kind, order, stable, descending\]) | Sort an array in-place. |
| [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.squeeze.html#numpy.recarray.squeeze "numpy.recarray.squeeze")<br>(\[axis\]) | Remove axes of length one from _a_. |
| [`std`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.std.html#numpy.recarray.std "numpy.recarray.std")<br>(\[axis, dtype, out, ddof, keepdims, ...\]) | Returns the standard deviation of the array elements along given axis. |
| [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.sum.html#numpy.recarray.sum "numpy.recarray.sum")<br>(\[axis, dtype, out, keepdims, initial, where\]) | Return the sum of the array elements over the given axis. |
| [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.swapaxes.html#numpy.recarray.swapaxes "numpy.recarray.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`take`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.take.html#numpy.recarray.take "numpy.recarray.take")<br>(indices\[, axis, out, mode\]) | Return an array formed from the elements of _a_ at the given indices. |
| [`to_device`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.to_device.html#numpy.recarray.to_device "numpy.recarray.to_device")<br>(device, /, \*\[, stream\]) | For Array API compatibility. |
| [`tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tobytes.html#numpy.recarray.tobytes "numpy.recarray.tobytes")<br>(\[order\]) | Construct Python bytes containing the raw data bytes in the array. |
| [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tofile.html#numpy.recarray.tofile "numpy.recarray.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |
| [`tolist`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tolist.html#numpy.recarray.tolist "numpy.recarray.tolist")<br>() | Return the array as an `a.ndim`\-levels deep nested list of Python scalars. |
| [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.trace.html#numpy.recarray.trace "numpy.recarray.trace")<br>(\[offset, axis1, axis2, dtype, out\]) | Return the sum along diagonals of the array. |
| [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.transpose.html#numpy.recarray.transpose "numpy.recarray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |
| [`var`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.var.html#numpy.recarray.var "numpy.recarray.var")<br>(\[axis, dtype, out, ddof, keepdims, ...\]) | Returns the variance of the array elements, along given axis. |
| [`view`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.view.html#numpy.recarray.view "numpy.recarray.view")<br>(\[dtype\]\[, type\]) | New view of array with the same data. |

|     |     |
| --- | --- |
| **field** |     |

Returns:

**rec**recarray

Empty array of the given shape and type.

Other Parameters:

**titles**tuple of str, optional

Aliases for column names. For example, if _names_ were `('x', 'y', 'z')` and _titles_ is `('x_coordinate', 'y_coordinate', 'z_coordinate')`, then `arr['x']` is equivalent to both `arr.x` and `arr.x_coordinate`.

**byteorder**{‘<’, ‘>’, ‘=’}, optional

Byte-order for all fields.

**aligned**bool, optional

Align the fields in memory as the C-compiler would.

**strides**tuple of ints, optional

Buffer (_buf_) is interpreted according to these strides (strides define how many bytes each array element, row, column, etc. occupy in memory).

**offset**int, optional

Start reading buffer (_buf_) from this offset onwards.

**order**{‘C’, ‘F’}, optional

Row-major (C-style) or column-major (Fortran-style) order.

See also

[`numpy.rec.fromrecords`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#numpy.rec.fromrecords "numpy.rec.fromrecords")

Construct a record array from data.

[`numpy.record`](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "numpy.record")

fundamental data-type for [`recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
.

[`numpy.rec.format_parser`](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy.rec.format_parser "numpy.rec.format_parser")

determine data-type from formats, names, titles.

Notes

This constructor can be compared to `empty`: it creates a new record array but does not fill it with data. To create a record array from data, use one of the following methods:

1.  Create a standard ndarray and convert it to a record array, using `arr.view(np.recarray)`
    
2.  Use the _buf_ keyword.
    
3.  Use _np.rec.fromrecords_.
    

Examples

Try it in your browser!

Create an array with two fields, `x` and `y`:

\>>> import numpy as np
\>>> x \= np.array(\[(1.0, 2), (3.0, 4)\], dtype\=\[('x', '<f8'), ('y', '<i8')\])
\>>> x
array(\[(1., 2), (3., 4)\], dtype=\[('x', '<f8'), ('y', '<i8')\])

Copy to clipboard

\>>> x\['x'\]
array(\[1., 3.\])

Copy to clipboard

View the array as a record array:

\>>> x \= x.view(np.recarray)

Copy to clipboard

\>>> x.x
array(\[1., 3.\])

Copy to clipboard

\>>> x.y
array(\[2, 4\])

Copy to clipboard

Create a new, empty record array:

\>>> np.recarray((2,),
... dtype\=\[('x', int), ('y', float), ('z', int)\]) 
rec.array(\[(-1073741821, 1.2249118382103472e-301, 24547520),\
       (3471280, 1.2134086255804012e-316, 0)\],
      dtype=\[('x', '<i4'), ('y', '<f8'), ('z', '<i4')\])

Copy to clipboard

Go BackOpen In Tab

On this page