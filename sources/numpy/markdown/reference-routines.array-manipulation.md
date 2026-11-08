[Skip to main content](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.array-manipulation.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.array-manipulation.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.array-manipulation.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.array-manipulation.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.array-manipulation.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.array-manipulation.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.array-manipulation.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.array-manipulation.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.array-manipulation.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.array-manipulation.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.array-manipulation.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.array-manipulation.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.array-manipulation.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.array-manipulation.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.array-manipulation.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.array-manipulation.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.array-manipulation.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.array-manipulation.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.array-manipulation.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.array-manipulation.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Array manipulation routines[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#array-manipulation-routines "Link to this heading")

===========================================================================================================================================================

Basic operations[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#basic-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`copyto`](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "numpy.copyto")<br>(dst, src\[, casting, where\]) | Copies values from one array to another, broadcasting as necessary. |
| [`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")<br>(a) | Return the number of dimensions of an array. |
| [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")<br>(a) | Return the shape of an array. |
| [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")<br>(a\[, axis\]) | Return the number of elements along a given axis. |

Changing array shape[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#changing-array-shape "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")<br>(a, /, shape\[, order, copy\]) | Returns a reshaped ndarray without changing data. |
| [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")<br>(a\[, order\]) | Return a contiguous flattened array. |
| [`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat") | A 1-D iterator over the array. |
| [`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |

Transpose-like operations[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#transpose-like-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`moveaxis`](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis "numpy.moveaxis")<br>(a, source, destination) | Move axes of an array to new positions. |
| [`rollaxis`](https://numpy.org/doc/stable/reference/generated/numpy.rollaxis.html#numpy.rollaxis "numpy.rollaxis")<br>(a, axis\[, start\]) | Roll the specified axis backwards, until it lies in a given position. |
| [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes "numpy.swapaxes")<br>(a, axis1, axis2) | Interchange two axes of an array. |
| [`ndarray.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T "numpy.ndarray.T") | View of the transposed array. |
| [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")<br>(a\[, axes\]) | Returns an array with axes transposed. |
| [`permute_dims`](https://numpy.org/doc/stable/reference/generated/numpy.permute_dims.html#numpy.permute_dims "numpy.permute_dims")<br>(a\[, axes\]) | Returns an array with axes transposed. |
| [`matrix_transpose`](https://numpy.org/doc/stable/reference/generated/numpy.matrix_transpose.html#numpy.matrix_transpose "numpy.matrix_transpose")<br>(x, /) | Transposes a matrix (or a stack of matrices) `x`. |

Changing number of dimensions[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#changing-number-of-dimensions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`atleast_1d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d "numpy.atleast_1d")<br>(\*arys) | Convert inputs to arrays with at least one dimension. |
| [`atleast_2d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d")<br>(\*arys) | View inputs as arrays with at least two dimensions. |
| [`atleast_3d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d "numpy.atleast_3d")<br>(\*arys) | View inputs as arrays with at least three dimensions. |
| [`broadcast`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")<br>(\*arrays) | Produce an object that mimics broadcasting. |
| [`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")<br>(array, shape\[, subok\]) | Broadcast an array to a new shape. |
| [`broadcast_arrays`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy.broadcast_arrays "numpy.broadcast_arrays")<br>(\*args\[, subok\]) | Broadcast any number of arrays against each other. |
| [`expand_dims`](https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html#numpy.expand_dims "numpy.expand_dims")<br>(a, axis) | Expand the shape of an array. |
| [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")<br>(a\[, axis\]) | Remove axes of length one from _a_. |

Changing kind of array[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#changing-kind-of-array "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")<br>(a\[, dtype, order, device, copy, like\]) | Convert the input to an array. |
| [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")<br>(a\[, dtype, order, device, copy, like\]) | Convert the input to an ndarray, but pass ndarray subclasses through. |
| [`asmatrix`](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy.asmatrix "numpy.asmatrix")<br>(data\[, dtype\]) | Interpret the input as a matrix. |
| [`asfortranarray`](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#numpy.asfortranarray "numpy.asfortranarray")<br>(a\[, dtype, like\]) | Return an array (ndim >= 1) laid out in Fortran order in memory. |
| [`ascontiguousarray`](https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray "numpy.ascontiguousarray")<br>(a\[, dtype, like\]) | Return a contiguous array (ndim >= 1) in memory (C order). |
| [`asarray_chkfinite`](https://numpy.org/doc/stable/reference/generated/numpy.asarray_chkfinite.html#numpy.asarray_chkfinite "numpy.asarray_chkfinite")<br>(a\[, dtype, order\]) | Convert the input to an array, checking for NaNs or Infs. |
| [`require`](https://numpy.org/doc/stable/reference/generated/numpy.require.html#numpy.require "numpy.require")<br>(a\[, dtype, requirements, like\]) | Return an ndarray of the provided type that satisfies requirements. |

Joining arrays[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#joining-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")<br>(arrays, /\[, axis, out, dtype, ...\]) | Join a sequence of arrays along an existing axis. |
| [`concat`](https://numpy.org/doc/stable/reference/generated/numpy.concat.html#numpy.concat "numpy.concat")<br>(arrays, /\[, axis, out, dtype, casting\]) | Join a sequence of arrays along an existing axis. |
| [`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")<br>(arrays\[, axis, out, dtype, casting\]) | Join a sequence of arrays along a new axis. |
| [`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")<br>(arrays) | Assemble an nd-array from nested lists of blocks. |
| [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")<br>(tup, \*\[, dtype, casting\]) | Stack arrays in sequence vertically (row wise). |
| [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")<br>(tup, \*\[, dtype, casting\]) | Stack arrays in sequence horizontally (column wise). |
| [`dstack`](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")<br>(tup) | Stack arrays in sequence depth wise (along third axis). |
| [`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")<br>(tup) | Stack 1-D arrays as columns into a 2-D array. |

Splitting arrays[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#splitting-arrays "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")<br>(ary, indices\_or\_sections\[, axis\]) | Split an array into multiple sub-arrays as views into _ary_. |
| [`array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split")<br>(ary, indices\_or\_sections\[, axis\]) | Split an array into multiple sub-arrays. |
| [`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit")<br>(ary, indices\_or\_sections) | Split array into multiple sub-arrays along the 3rd axis (depth). |
| [`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit")<br>(ary, indices\_or\_sections) | Split an array into multiple sub-arrays horizontally (column-wise). |
| [`vsplit`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit")<br>(ary, indices\_or\_sections) | Split an array into multiple sub-arrays vertically (row-wise). |
| [`unstack`](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#numpy.unstack "numpy.unstack")<br>(x, /, \*\[, axis\]) | Split an array into a sequence of arrays along the given axis. |

Tiling arrays[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#tiling-arrays "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`tile`](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy.tile "numpy.tile")<br>(A, reps) | Construct an array by repeating A the number of times given by reps. |
| [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")<br>(a, repeats\[, axis\]) | Repeat each element of an array after themselves |

Adding and removing elements[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#adding-and-removing-elements "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`delete`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")<br>(arr, obj\[, axis\]) | Return a new array with sub-arrays along an axis deleted. |
| [`insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert "numpy.insert")<br>(arr, obj, values\[, axis\]) | Insert values along the given axis before the given indices. |
| [`append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")<br>(arr, values\[, axis\]) | Append values to the end of an array. |
| [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "numpy.resize")<br>(a, new\_shape) | Return a new array with the specified shape. |
| [`trim_zeros`](https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html#numpy.trim_zeros "numpy.trim_zeros")<br>(filt\[, trim, axis\]) | Remove values along a dimension which are zero along all other. |
| [`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")<br>(ar\[, return\_index, return\_inverse, ...\]) | Find the unique elements of an array. |
| [`pad`](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#numpy.pad "numpy.pad")<br>(array, pad\_width\[, mode\]) | Pad an array. |

Rearranging elements[#](https://numpy.org/doc/stable/reference/routines.array-manipulation.html#rearranging-elements "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`flip`](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip "numpy.flip")<br>(m\[, axis\]) | Reverse the order of elements in an array along the given axis. |
| [`fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")<br>(m) | Reverse the order of elements along axis 1 (left/right). |
| [`flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")<br>(m) | Reverse the order of elements along axis 0 (up/down). |
| [`roll`](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll "numpy.roll")<br>(a, shift\[, axis\]) | Roll array elements along a given axis. |
| [`rot90`](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#numpy.rot90 "numpy.rot90")<br>(m\[, k, axes\]) | Rotate an array by 90 degrees in the plane specified by axes. |

On this page