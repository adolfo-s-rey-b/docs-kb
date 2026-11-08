[Skip to main content](https://numpy.org/doc/stable/reference/routines.ma.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.ma.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.ma.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.ma.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.ma.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.ma.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.ma.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.ma.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.ma.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.ma.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.ma.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.ma.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.ma.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.ma.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.ma.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.ma.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.ma.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.ma.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.ma.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.ma.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.ma.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.ma.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Masked array operations[#](https://numpy.org/doc/stable/reference/routines.ma.html#masked-array-operations "Link to this heading")

===================================================================================================================================

Constants[#](https://numpy.org/doc/stable/reference/routines.ma.html#constants "Link to this heading")

-------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ma.MaskType`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskType.html#numpy.ma.MaskType "numpy.ma.MaskType") | alias of [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool") |

Creation[#](https://numpy.org/doc/stable/reference/routines.ma.html#creation "Link to this heading")

-----------------------------------------------------------------------------------------------------

### From existing data[#](https://numpy.org/doc/stable/reference/routines.ma.html#from-existing-data "Link to this heading")

|     |     |
| --- | --- |
| [`ma.masked_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "numpy.ma.masked_array") | alias of [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray") |
| [`ma.array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html#numpy.ma.array "numpy.ma.array")<br>(data\[, dtype, copy, order, mask, ...\]) | An array class with possibly masked values. |
| [`ma.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ma.copy.html#numpy.ma.copy "numpy.ma.copy")<br>(a.copy) | Return a copy of the array. |
| [`ma.frombuffer`](https://numpy.org/doc/stable/reference/generated/numpy.ma.frombuffer.html#numpy.ma.frombuffer "numpy.ma.frombuffer")<br>(buffer\[, dtype, count, ...\]) | Interpret a buffer as a 1-dimensional array. |
| [`ma.fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromfunction.html#numpy.ma.fromfunction "numpy.ma.fromfunction")<br>(function, shape, \*\[, dtype, ...\]) | Construct an array by executing a function over each coordinate. |
| [`ma.MaskedArray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.copy.html#numpy.ma.MaskedArray.copy "numpy.ma.MaskedArray.copy")<br>(\[order\]) | Return a copy of the array. |
| [`ma.diagflat`](https://numpy.org/doc/stable/reference/generated/numpy.ma.diagflat.html#numpy.ma.diagflat "numpy.ma.diagflat")<br>(v\[, k\]) | Create a two-dimensional array with the flattened input as a diagonal. |

### Ones and zeros[#](https://numpy.org/doc/stable/reference/routines.ma.html#ones-and-zeros "Link to this heading")

|     |     |
| --- | --- |
| [`ma.empty`](https://numpy.org/doc/stable/reference/generated/numpy.ma.empty.html#numpy.ma.empty "numpy.ma.empty")<br>(shape\[, dtype, order, device, like\]) | Return a new array of given shape and type, without initializing entries. |
| [`ma.empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.empty_like.html#numpy.ma.empty_like "numpy.ma.empty_like")<br>(prototype, /\[, dtype, order, ...\]) | Return a new array with the same shape and type as a given array. |
| [`ma.masked_all`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html#numpy.ma.masked_all "numpy.ma.masked_all")<br>(shape\[, dtype\]) | Empty masked array with all elements masked. |
| [`ma.masked_all_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html#numpy.ma.masked_all_like "numpy.ma.masked_all_like")<br>(arr) | Empty masked array with the properties of an existing array. |
| [`ma.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ones.html#numpy.ma.ones "numpy.ma.ones")<br>(shape\[, dtype, order, device, like, ...\]) | Return a new array of given shape and type, filled with ones. |
| [`ma.ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ones_like.html#numpy.ma.ones_like "numpy.ma.ones_like")<br>(a\[, dtype, order, subok, ...\]) | Return an array of ones with the same shape and type as a given array. |
| [`ma.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros.html#numpy.ma.zeros "numpy.ma.zeros")<br>(shape\[, dtype, order, device, like\]) | Return a new array of given shape and type, filled with zeros. |
| [`ma.zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros_like.html#numpy.ma.zeros_like "numpy.ma.zeros_like")<br>(a\[, dtype, order, subok, ...\]) | Return an array of zeros with the same shape and type as a given array. |

* * *

Inspecting the array[#](https://numpy.org/doc/stable/reference/routines.ma.html#inspecting-the-array "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ma.all`](https://numpy.org/doc/stable/reference/generated/numpy.ma.all.html#numpy.ma.all "numpy.ma.all")<br>(self\[, axis, out, keepdims\]) | Returns True if all elements evaluate to True. |
| [`ma.any`](https://numpy.org/doc/stable/reference/generated/numpy.ma.any.html#numpy.ma.any "numpy.ma.any")<br>(self\[, axis, out, keepdims\]) | Returns True if any of the elements of _a_ evaluate to True. |
| [`ma.count`](https://numpy.org/doc/stable/reference/generated/numpy.ma.count.html#numpy.ma.count "numpy.ma.count")<br>(self\[, axis, keepdims\]) | Count the non-masked elements of the array along the given axis. |
| [`ma.count_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.count_masked.html#numpy.ma.count_masked "numpy.ma.count_masked")<br>(arr\[, axis\]) | Count the number of masked elements along the given axis. |
| [`ma.getmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmask.html#numpy.ma.getmask "numpy.ma.getmask")<br>(a) | Return the mask of a masked array, or nomask. |
| [`ma.getmaskarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#numpy.ma.getmaskarray "numpy.ma.getmaskarray")<br>(arr) | Return the mask of a masked array, or full boolean array of False. |
| [`ma.getdata`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html#numpy.ma.getdata "numpy.ma.getdata")<br>(a\[, subok\]) | Return the data of a masked array as an ndarray. |
| [`ma.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ma.nonzero.html#numpy.ma.nonzero "numpy.ma.nonzero")<br>(self) | Return the indices of unmasked elements that are not zero. |
| [`ma.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.shape.html#numpy.ma.shape "numpy.ma.shape")<br>(obj) | Return the shape of an array. |
| [`ma.size`](https://numpy.org/doc/stable/reference/generated/numpy.ma.size.html#numpy.ma.size "numpy.ma.size")<br>(obj\[, axis\]) | Return the number of elements along a given axis. |
| [`ma.is_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html#numpy.ma.is_masked "numpy.ma.is_masked")<br>(x) | Determine whether input has masked values. |
| [`ma.is_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_mask.html#numpy.ma.is_mask "numpy.ma.is_mask")<br>(m) | Return True if m is a valid, standard mask. |
| [`ma.isMaskedArray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMaskedArray.html#numpy.ma.isMaskedArray "numpy.ma.isMaskedArray")<br>(x) | Test whether input is an instance of MaskedArray. |
| [`ma.isMA`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMA.html#numpy.ma.isMA "numpy.ma.isMA")<br>(x) | Test whether input is an instance of MaskedArray. |
| [`ma.isarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isarray.html#numpy.ma.isarray "numpy.ma.isarray")<br>(x) | Test whether input is an instance of MaskedArray. |
| [`ma.isin`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isin.html#numpy.ma.isin "numpy.ma.isin")<br>(element, test\_elements\[, ...\]) | Calculates _element in test\_elements_, broadcasting over _element_ only. |
| [`ma.in1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.in1d.html#numpy.ma.in1d "numpy.ma.in1d")<br>(ar1, ar2\[, assume\_unique, invert\]) | Test whether each element of an array is also present in a second array. |
| [`ma.unique`](https://numpy.org/doc/stable/reference/generated/numpy.ma.unique.html#numpy.ma.unique "numpy.ma.unique")<br>(ar1\[, return\_index, return\_inverse\]) | Finds the unique elements of an array. |
| [`ma.MaskedArray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.all.html#numpy.ma.MaskedArray.all "numpy.ma.MaskedArray.all")<br>(\[axis, out, keepdims\]) | Returns True if all elements evaluate to True. |
| [`ma.MaskedArray.any`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.any.html#numpy.ma.MaskedArray.any "numpy.ma.MaskedArray.any")<br>(\[axis, out, keepdims\]) | Returns True if any of the elements of _a_ evaluate to True. |
| [`ma.MaskedArray.count`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.count.html#numpy.ma.MaskedArray.count "numpy.ma.MaskedArray.count")<br>(\[axis, keepdims\]) | Count the non-masked elements of the array along the given axis. |
| [`ma.MaskedArray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.nonzero.html#numpy.ma.MaskedArray.nonzero "numpy.ma.MaskedArray.nonzero")<br>() | Return the indices of unmasked elements that are not zero. |
| [`ma.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.shape.html#numpy.ma.shape "numpy.ma.shape")<br>(obj) | Return the shape of an array. |
| [`ma.size`](https://numpy.org/doc/stable/reference/generated/numpy.ma.size.html#numpy.ma.size "numpy.ma.size")<br>(obj\[, axis\]) | Return the number of elements along a given axis. |

|     |     |
| --- | --- |
| [`ma.MaskedArray.data`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "numpy.ma.MaskedArray.data") | Returns the underlying data, as a view of the masked array. |
| [`ma.MaskedArray.mask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.mask "numpy.ma.MaskedArray.mask") | Current mask. |
| [`ma.MaskedArray.recordmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.recordmask "numpy.ma.MaskedArray.recordmask") | Get or set the mask of the array if it has no named fields. |

* * *

Manipulating a MaskedArray[#](https://numpy.org/doc/stable/reference/routines.ma.html#manipulating-a-maskedarray "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

### Changing the shape[#](https://numpy.org/doc/stable/reference/routines.ma.html#changing-the-shape "Link to this heading")

|     |     |
| --- | --- |
| [`ma.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ravel.html#numpy.ma.ravel "numpy.ma.ravel")<br>(self\[, order\]) | Returns a 1D version of self, as a view. |
| [`ma.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.reshape.html#numpy.ma.reshape "numpy.ma.reshape")<br>(a, new\_shape\[, order\]) | Returns an array containing the same data with a new shape. |
| [`ma.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html#numpy.ma.resize "numpy.ma.resize")<br>(x, new\_shape) | Return a new masked array with the specified size and shape. |
| [`ma.MaskedArray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.flatten.html#numpy.ma.MaskedArray.flatten "numpy.ma.MaskedArray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |
| [`ma.MaskedArray.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ravel.html#numpy.ma.MaskedArray.ravel "numpy.ma.MaskedArray.ravel")<br>(\[order\]) | Returns a 1D version of self, as a view. |
| [`ma.MaskedArray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.reshape.html#numpy.ma.MaskedArray.reshape "numpy.ma.MaskedArray.reshape")<br>(\*s, \*\*kwargs) | Returns a reshaped masked array without changing its data. |
| [`ma.MaskedArray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.resize.html#numpy.ma.MaskedArray.resize "numpy.ma.MaskedArray.resize")<br>(newshape\[, refcheck, ...\]) |     |

### Modifying axes[#](https://numpy.org/doc/stable/reference/routines.ma.html#modifying-axes "Link to this heading")

|     |     |
| --- | --- |
| [`ma.swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.swapaxes.html#numpy.ma.swapaxes "numpy.ma.swapaxes")<br>(a.swapaxes) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`ma.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.transpose.html#numpy.ma.transpose "numpy.ma.transpose")<br>(a\[, axes\]) | Permute the dimensions of an array. |
| [`ma.MaskedArray.swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.swapaxes.html#numpy.ma.MaskedArray.swapaxes "numpy.ma.MaskedArray.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`ma.MaskedArray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html#numpy.ma.MaskedArray.transpose "numpy.ma.MaskedArray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |

### Changing the number of dimensions[#](https://numpy.org/doc/stable/reference/routines.ma.html#changing-the-number-of-dimensions "Link to this heading")

|     |     |
| --- | --- |
| [`ma.atleast_1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_1d.html#numpy.ma.atleast_1d "numpy.ma.atleast_1d")<br>(\*arys) | Convert inputs to arrays with at least one dimension. |
| [`ma.atleast_2d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_2d.html#numpy.ma.atleast_2d "numpy.ma.atleast_2d")<br>(\*arys) | View inputs as arrays with at least two dimensions. |
| [`ma.atleast_3d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.atleast_3d.html#numpy.ma.atleast_3d "numpy.ma.atleast_3d")<br>(\*arys) | View inputs as arrays with at least three dimensions. |
| [`ma.expand_dims`](https://numpy.org/doc/stable/reference/generated/numpy.ma.expand_dims.html#numpy.ma.expand_dims "numpy.ma.expand_dims")<br>(a, axis) | Expand the shape of an array. |
| [`ma.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ma.squeeze.html#numpy.ma.squeeze "numpy.ma.squeeze")<br>(a\[, axis, fill\_value, hardmask\]) | Remove axes of length one from _a_. |
| [`ma.MaskedArray.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.squeeze.html#numpy.ma.MaskedArray.squeeze "numpy.ma.MaskedArray.squeeze")<br>(\[axis\]) | Remove axes of length one from _a_. |
| [`ma.stack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.stack.html#numpy.ma.stack "numpy.ma.stack")<br>(arrays\[, axis, out, dtype, casting\]) | Join a sequence of arrays along a new axis. |
| [`ma.column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.column_stack.html#numpy.ma.column_stack "numpy.ma.column_stack")<br>(tup) | Stack 1-D arrays as columns into a 2-D array. |
| [`ma.concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html#numpy.ma.concatenate "numpy.ma.concatenate")<br>(arrays\[, axis\]) | Concatenate a sequence of arrays along the given axis. |
| [`ma.dstack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.dstack.html#numpy.ma.dstack "numpy.ma.dstack")<br>(tup) | Stack arrays in sequence depth wise (along third axis). |
| [`ma.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.hstack.html#numpy.ma.hstack "numpy.ma.hstack")<br>(tup, \*\[, dtype, casting\]) | Stack arrays in sequence horizontally (column wise). |
| [`ma.hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.ma.hsplit.html#numpy.ma.hsplit "numpy.ma.hsplit")<br>(ary, indices\_or\_sections) | Split an array into multiple sub-arrays horizontally (column-wise). |
| [`ma.mr_`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mr_.html#numpy.ma.mr_ "numpy.ma.mr_") | Translate slice objects to concatenation along the first axis. |
| [`ma.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.vstack.html#numpy.ma.vstack "numpy.ma.vstack")<br>(tup, \*\[, dtype, casting\]) | Stack arrays in sequence vertically (row wise). |

### Joining arrays[#](https://numpy.org/doc/stable/reference/routines.ma.html#joining-arrays "Link to this heading")

|     |     |
| --- | --- |
| [`ma.concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html#numpy.ma.concatenate "numpy.ma.concatenate")<br>(arrays\[, axis\]) | Concatenate a sequence of arrays along the given axis. |
| [`ma.stack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.stack.html#numpy.ma.stack "numpy.ma.stack")<br>(arrays\[, axis, out, dtype, casting\]) | Join a sequence of arrays along a new axis. |
| [`ma.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.vstack.html#numpy.ma.vstack "numpy.ma.vstack")<br>(tup, \*\[, dtype, casting\]) | Stack arrays in sequence vertically (row wise). |
| [`ma.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.hstack.html#numpy.ma.hstack "numpy.ma.hstack")<br>(tup, \*\[, dtype, casting\]) | Stack arrays in sequence horizontally (column wise). |
| [`ma.dstack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.dstack.html#numpy.ma.dstack "numpy.ma.dstack")<br>(tup) | Stack arrays in sequence depth wise (along third axis). |
| [`ma.column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.ma.column_stack.html#numpy.ma.column_stack "numpy.ma.column_stack")<br>(tup) | Stack 1-D arrays as columns into a 2-D array. |
| [`ma.append`](https://numpy.org/doc/stable/reference/generated/numpy.ma.append.html#numpy.ma.append "numpy.ma.append")<br>(a, b\[, axis\]) | Append values to the end of an array. |

* * *

Operations on masks[#](https://numpy.org/doc/stable/reference/routines.ma.html#operations-on-masks "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

### Creating a mask[#](https://numpy.org/doc/stable/reference/routines.ma.html#creating-a-mask "Link to this heading")

|     |     |
| --- | --- |
| [`ma.make_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask.html#numpy.ma.make_mask "numpy.ma.make_mask")<br>(m\[, copy, shrink, dtype\]) | Create a boolean mask from an array. |
| [`ma.make_mask_none`](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_none.html#numpy.ma.make_mask_none "numpy.ma.make_mask_none")<br>(newshape\[, dtype\]) | Return a boolean mask of the given shape, filled with False. |
| [`ma.mask_or`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_or.html#numpy.ma.mask_or "numpy.ma.mask_or")<br>(m1, m2\[, copy, shrink\]) | Combine two masks with the `logical_or` operator. |
| [`ma.make_mask_descr`](https://numpy.org/doc/stable/reference/generated/numpy.ma.make_mask_descr.html#numpy.ma.make_mask_descr "numpy.ma.make_mask_descr")<br>(ndtype) | Construct a dtype description list from a given dtype. |

### Accessing a mask[#](https://numpy.org/doc/stable/reference/routines.ma.html#accessing-a-mask "Link to this heading")

|     |     |
| --- | --- |
| [`ma.getmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmask.html#numpy.ma.getmask "numpy.ma.getmask")<br>(a) | Return the mask of a masked array, or nomask. |
| [`ma.getmaskarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#numpy.ma.getmaskarray "numpy.ma.getmaskarray")<br>(arr) | Return the mask of a masked array, or full boolean array of False. |
| [`ma.masked_array.mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mask.html#numpy.ma.masked_array.mask "numpy.ma.masked_array.mask") | Current mask. |

### Finding masked data[#](https://numpy.org/doc/stable/reference/routines.ma.html#finding-masked-data "Link to this heading")

|     |     |
| --- | --- |
| [`ma.ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ndenumerate.html#numpy.ma.ndenumerate "numpy.ma.ndenumerate")<br>(a\[, compressed\]) | Multidimensional index iterator. |
| [`ma.flatnotmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_contiguous.html#numpy.ma.flatnotmasked_contiguous "numpy.ma.flatnotmasked_contiguous")<br>(a) | Find contiguous unmasked data in a masked array. |
| [`ma.flatnotmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatnotmasked_edges.html#numpy.ma.flatnotmasked_edges "numpy.ma.flatnotmasked_edges")<br>(a) | Find the indices of the first and last unmasked values. |
| [`ma.notmasked_contiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_contiguous.html#numpy.ma.notmasked_contiguous "numpy.ma.notmasked_contiguous")<br>(a\[, axis\]) | Find contiguous unmasked data in a masked array along the given axis. |
| [`ma.notmasked_edges`](https://numpy.org/doc/stable/reference/generated/numpy.ma.notmasked_edges.html#numpy.ma.notmasked_edges "numpy.ma.notmasked_edges")<br>(a\[, axis\]) | Find the indices of the first and last unmasked values along an axis. |
| [`ma.clump_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_masked.html#numpy.ma.clump_masked "numpy.ma.clump_masked")<br>(a) | Returns a list of slices corresponding to the masked clumps of a 1-D array. |
| [`ma.clump_unmasked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clump_unmasked.html#numpy.ma.clump_unmasked "numpy.ma.clump_unmasked")<br>(a) | Return list of slices corresponding to the unmasked clumps of a 1-D array. |

### Modifying a mask[#](https://numpy.org/doc/stable/reference/routines.ma.html#modifying-a-mask "Link to this heading")

|     |     |
| --- | --- |
| [`ma.mask_cols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_cols.html#numpy.ma.mask_cols "numpy.ma.mask_cols")<br>(a\[, axis\]) | Mask columns of a 2D array that contain masked values. |
| [`ma.mask_or`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_or.html#numpy.ma.mask_or "numpy.ma.mask_or")<br>(m1, m2\[, copy, shrink\]) | Combine two masks with the `logical_or` operator. |
| [`ma.mask_rowcols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rowcols.html#numpy.ma.mask_rowcols "numpy.ma.mask_rowcols")<br>(a\[, axis\]) | Mask rows and/or columns of a 2D array that contain masked values. |
| [`ma.mask_rows`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rows.html#numpy.ma.mask_rows "numpy.ma.mask_rows")<br>(a\[, axis\]) | Mask rows of a 2D array that contain masked values. |
| [`ma.harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.harden_mask.html#numpy.ma.harden_mask "numpy.ma.harden_mask")<br>(self) | Force the mask to hard, preventing unmasking by assignment. |
| [`ma.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.soften_mask.html#numpy.ma.soften_mask "numpy.ma.soften_mask")<br>(self) | Force the mask to soft (default), allowing unmasking by assignment. |
| [`ma.MaskedArray.harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy.ma.MaskedArray.harden_mask "numpy.ma.MaskedArray.harden_mask")<br>() | Force the mask to hard, preventing unmasking by assignment. |
| [`ma.MaskedArray.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.soften_mask.html#numpy.ma.MaskedArray.soften_mask "numpy.ma.MaskedArray.soften_mask")<br>() | Force the mask to soft (default), allowing unmasking by assignment. |
| [`ma.MaskedArray.shrink_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.shrink_mask.html#numpy.ma.MaskedArray.shrink_mask "numpy.ma.MaskedArray.shrink_mask")<br>() | Reduce a mask to nomask when possible. |
| [`ma.MaskedArray.unshare_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.unshare_mask.html#numpy.ma.MaskedArray.unshare_mask "numpy.ma.MaskedArray.unshare_mask")<br>() | Copy the mask and set the _sharedmask_ flag to `False`. |

* * *

Conversion operations[#](https://numpy.org/doc/stable/reference/routines.ma.html#conversion-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### \> to a masked array[#](https://numpy.org/doc/stable/reference/routines.ma.html#to-a-masked-array "Link to this heading")

|     |     |
| --- | --- |
| [`ma.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.asarray.html#numpy.ma.asarray "numpy.ma.asarray")<br>(a\[, dtype, order\]) | Convert the input to a masked array of the given data-type. |
| [`ma.asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.asanyarray.html#numpy.ma.asanyarray "numpy.ma.asanyarray")<br>(a\[, dtype, order\]) | Convert the input to a masked array, conserving subclasses. |
| [`ma.fix_invalid`](https://numpy.org/doc/stable/reference/generated/numpy.ma.fix_invalid.html#numpy.ma.fix_invalid "numpy.ma.fix_invalid")<br>(a\[, mask, copy, fill\_value\]) | Return input with invalid data masked and replaced by a fill value. |
| [`ma.masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")<br>(x, value\[, copy\]) | Mask an array where equal to a given value. |
| [`ma.masked_greater`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater.html#numpy.ma.masked_greater "numpy.ma.masked_greater")<br>(x, value\[, copy\]) | Mask an array where greater than a given value. |
| [`ma.masked_greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater_equal.html#numpy.ma.masked_greater_equal "numpy.ma.masked_greater_equal")<br>(x, value\[, copy\]) | Mask an array where greater than or equal to a given value. |
| [`ma.masked_inside`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_inside.html#numpy.ma.masked_inside "numpy.ma.masked_inside")<br>(x, v1, v2\[, copy\]) | Mask an array inside a given interval. |
| [`ma.masked_invalid`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html#numpy.ma.masked_invalid "numpy.ma.masked_invalid")<br>(a\[, copy\]) | Mask an array where invalid values occur (NaNs or infs). |
| [`ma.masked_less`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#numpy.ma.masked_less "numpy.ma.masked_less")<br>(x, value\[, copy\]) | Mask an array where less than a given value. |
| [`ma.masked_less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less_equal.html#numpy.ma.masked_less_equal "numpy.ma.masked_less_equal")<br>(x, value\[, copy\]) | Mask an array where less than or equal to a given value. |
| [`ma.masked_not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_not_equal.html#numpy.ma.masked_not_equal "numpy.ma.masked_not_equal")<br>(x, value\[, copy\]) | Mask an array where _not_ equal to a given value. |
| [`ma.masked_object`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_object.html#numpy.ma.masked_object "numpy.ma.masked_object")<br>(x, value\[, copy, shrink\]) | Mask the array _x_ where the data are exactly equal to value. |
| [`ma.masked_outside`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html#numpy.ma.masked_outside "numpy.ma.masked_outside")<br>(x, v1, v2\[, copy\]) | Mask an array outside a given interval. |
| [`ma.masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")<br>(x, value\[, rtol, atol, ...\]) | Mask using floating point equality. |
| [`ma.masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")<br>(condition, a\[, copy\]) | Mask an array where a condition is met. |

### \> to an ndarray[#](https://numpy.org/doc/stable/reference/routines.ma.html#to-an-ndarray "Link to this heading")

|     |     |
| --- | --- |
| [`ma.compress_cols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_cols.html#numpy.ma.compress_cols "numpy.ma.compress_cols")<br>(a) | Suppress whole columns of a 2-D array that contain masked values. |
| [`ma.compress_rowcols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_rowcols.html#numpy.ma.compress_rowcols "numpy.ma.compress_rowcols")<br>(x\[, axis\]) | Suppress the rows and/or columns of a 2-D array that contain masked values. |
| [`ma.compress_rows`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_rows.html#numpy.ma.compress_rows "numpy.ma.compress_rows")<br>(a) | Suppress whole rows of a 2-D array that contain masked values. |
| [`ma.compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy.ma.compressed "numpy.ma.compressed")<br>(x) | Return all the non-masked data as a 1-D array. |
| [`ma.filled`](https://numpy.org/doc/stable/reference/generated/numpy.ma.filled.html#numpy.ma.filled "numpy.ma.filled")<br>(a\[, fill\_value\]) | Return input as an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")<br>, with masked values replaced by _fill\_value_. |
| [`ma.MaskedArray.compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "numpy.ma.MaskedArray.compressed")<br>() | Return all the non-masked data as a 1-D array. |
| [`ma.MaskedArray.filled`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html#numpy.ma.MaskedArray.filled "numpy.ma.MaskedArray.filled")<br>(\[fill\_value\]) | Return a copy of self, with masked values filled with a given value. |

### \> to another object[#](https://numpy.org/doc/stable/reference/routines.ma.html#to-another-object "Link to this heading")

|     |     |
| --- | --- |
| [`ma.MaskedArray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tofile.html#numpy.ma.MaskedArray.tofile "numpy.ma.MaskedArray.tofile")<br>(fid\[, sep, format\]) | Save a masked array to a file in binary format. |
| [`ma.MaskedArray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html#numpy.ma.MaskedArray.tolist "numpy.ma.MaskedArray.tolist")<br>(\[fill\_value\]) | Return the data portion of the masked array as a hierarchical Python list. |
| [`ma.MaskedArray.torecords`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.torecords.html#numpy.ma.MaskedArray.torecords "numpy.ma.MaskedArray.torecords")<br>() | Transforms a masked array into a flexible-type array. |
| [`ma.MaskedArray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tobytes.html#numpy.ma.MaskedArray.tobytes "numpy.ma.MaskedArray.tobytes")<br>(\[fill\_value, order\]) | Return the array data as a string containing the raw bytes in the array. |

### Filling a masked array[#](https://numpy.org/doc/stable/reference/routines.ma.html#filling-a-masked-array "Link to this heading")

|     |     |
| --- | --- |
| [`ma.common_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.common_fill_value.html#numpy.ma.common_fill_value "numpy.ma.common_fill_value")<br>(a, b) | Return the common filling value of two masked arrays, if any. |
| [`ma.default_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.default_fill_value.html#numpy.ma.default_fill_value "numpy.ma.default_fill_value")<br>(obj) | Return the default fill value for the argument object. |
| [`ma.maximum_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html#numpy.ma.maximum_fill_value "numpy.ma.maximum_fill_value")<br>(obj) | Return the minimum value that can be represented by the dtype of an object. |
| [`ma.minimum_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.minimum_fill_value.html#numpy.ma.minimum_fill_value "numpy.ma.minimum_fill_value")<br>(obj) | Return the maximum value that can be represented by the dtype of an object. |
| [`ma.set_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.set_fill_value.html#numpy.ma.set_fill_value "numpy.ma.set_fill_value")<br>(a, fill\_value) | Set the filling value of a, if a is a masked array. |
| [`ma.MaskedArray.get_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.get_fill_value.html#numpy.ma.MaskedArray.get_fill_value "numpy.ma.MaskedArray.get_fill_value")<br>() | The filling value of the masked array is a scalar. |
| [`ma.MaskedArray.set_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.set_fill_value.html#numpy.ma.MaskedArray.set_fill_value "numpy.ma.MaskedArray.set_fill_value")<br>(\[value\]) |     |

|     |     |
| --- | --- |
| [`ma.MaskedArray.fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value") | The filling value of the masked array is a scalar. |

* * *

Masked arrays arithmetic[#](https://numpy.org/doc/stable/reference/routines.ma.html#masked-arrays-arithmetic "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

### Arithmetic[#](https://numpy.org/doc/stable/reference/routines.ma.html#arithmetic "Link to this heading")

|     |     |
| --- | --- |
| [`ma.anom`](https://numpy.org/doc/stable/reference/generated/numpy.ma.anom.html#numpy.ma.anom "numpy.ma.anom")<br>(self\[, axis, dtype\]) | Compute the anomalies (deviations from the arithmetic mean) along the given axis. |
| [`ma.anomalies`](https://numpy.org/doc/stable/reference/generated/numpy.ma.anomalies.html#numpy.ma.anomalies "numpy.ma.anomalies")<br>(self\[, axis, dtype\]) | Compute the anomalies (deviations from the arithmetic mean) along the given axis. |
| [`ma.average`](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy.ma.average "numpy.ma.average")<br>(a\[, axis, weights, returned, ...\]) | Return the weighted average of array over the given axis. |
| [`ma.conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.conjugate.html#numpy.ma.conjugate "numpy.ma.conjugate")<br>(x, /\[, out, where, casting, ...\]) | Return the complex conjugate, element-wise. |
| [`ma.corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.ma.corrcoef.html#numpy.ma.corrcoef "numpy.ma.corrcoef")<br>(x\[, y, rowvar, allow\_masked\]) | Return Pearson product-moment correlation coefficients. |
| [`ma.cov`](https://numpy.org/doc/stable/reference/generated/numpy.ma.cov.html#numpy.ma.cov "numpy.ma.cov")<br>(x\[, y, rowvar, bias, allow\_masked, ddof\]) | Estimate the covariance matrix. |
| [`ma.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ma.cumsum.html#numpy.ma.cumsum "numpy.ma.cumsum")<br>(self\[, axis, dtype, out\]) | Return the cumulative sum of the array elements over the given axis. |
| [`ma.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ma.cumprod.html#numpy.ma.cumprod "numpy.ma.cumprod")<br>(self\[, axis, dtype, out\]) | Return the cumulative product of the array elements over the given axis. |
| [`ma.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mean.html#numpy.ma.mean "numpy.ma.mean")<br>(self\[, axis, dtype, out, keepdims\]) | Returns the average of the array elements along given axis. |
| [`ma.median`](https://numpy.org/doc/stable/reference/generated/numpy.ma.median.html#numpy.ma.median "numpy.ma.median")<br>(a\[, axis, out, overwrite\_input, ...\]) | Compute the median along the specified axis. |
| [`ma.power`](https://numpy.org/doc/stable/reference/generated/numpy.ma.power.html#numpy.ma.power "numpy.ma.power")<br>(a, b\[, third\]) | Returns element-wise base array raised to power from second array. |
| [`ma.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ma.prod.html#numpy.ma.prod "numpy.ma.prod")<br>(self\[, axis, dtype, out, keepdims\]) | Return the product of the array elements over the given axis. |
| [`ma.std`](https://numpy.org/doc/stable/reference/generated/numpy.ma.std.html#numpy.ma.std "numpy.ma.std")<br>(self\[, axis, dtype, out, ddof, ...\]) | Returns the standard deviation of the array elements along given axis. |
| [`ma.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ma.sum.html#numpy.ma.sum "numpy.ma.sum")<br>(self\[, axis, dtype, out, keepdims\]) | Return the sum of the array elements over the given axis. |
| [`ma.var`](https://numpy.org/doc/stable/reference/generated/numpy.ma.var.html#numpy.ma.var "numpy.ma.var")<br>(self\[, axis, dtype, out, ddof, ...\]) | Compute the variance along the specified axis. |
| [`ma.MaskedArray.anom`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.anom.html#numpy.ma.MaskedArray.anom "numpy.ma.MaskedArray.anom")<br>(\[axis, dtype\]) | Compute the anomalies (deviations from the arithmetic mean) along the given axis. |
| [`ma.MaskedArray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumprod.html#numpy.ma.MaskedArray.cumprod "numpy.ma.MaskedArray.cumprod")<br>(\[axis, dtype, out\]) | Return the cumulative product of the array elements over the given axis. |
| [`ma.MaskedArray.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumsum.html#numpy.ma.MaskedArray.cumsum "numpy.ma.MaskedArray.cumsum")<br>(\[axis, dtype, out\]) | Return the cumulative sum of the array elements over the given axis. |
| [`ma.MaskedArray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.mean.html#numpy.ma.MaskedArray.mean "numpy.ma.MaskedArray.mean")<br>(\[axis, dtype, out, keepdims\]) | Returns the average of the array elements along given axis. |
| [`ma.MaskedArray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.prod.html#numpy.ma.MaskedArray.prod "numpy.ma.MaskedArray.prod")<br>(\[axis, dtype, out, keepdims\]) | Return the product of the array elements over the given axis. |
| [`ma.MaskedArray.std`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.std.html#numpy.ma.MaskedArray.std "numpy.ma.MaskedArray.std")<br>(\[axis, dtype, out, ddof, ...\]) | Returns the standard deviation of the array elements along given axis. |
| [`ma.MaskedArray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sum.html#numpy.ma.MaskedArray.sum "numpy.ma.MaskedArray.sum")<br>(\[axis, dtype, out, keepdims\]) | Return the sum of the array elements over the given axis. |
| [`ma.MaskedArray.var`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.var.html#numpy.ma.MaskedArray.var "numpy.ma.MaskedArray.var")<br>(\[axis, dtype, out, ddof, ...\]) | Compute the variance along the specified axis. |

### Minimum/maximum[#](https://numpy.org/doc/stable/reference/routines.ma.html#minimum-maximum "Link to this heading")

|     |     |
| --- | --- |
| [`ma.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ma.argmax.html#numpy.ma.argmax "numpy.ma.argmax")<br>(self\[, axis, fill\_value, out, ...\]) | Returns array of indices of the maximum values along the given axis. |
| [`ma.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ma.argmin.html#numpy.ma.argmin "numpy.ma.argmin")<br>(self\[, axis, fill\_value, out, ...\]) | Return array of indices to the minimum values along the given axis. |
| [`ma.max`](https://numpy.org/doc/stable/reference/generated/numpy.ma.max.html#numpy.ma.max "numpy.ma.max")<br>(obj\[, axis, out, fill\_value, keepdims\]) | Return the maximum along a given axis. |
| [`ma.min`](https://numpy.org/doc/stable/reference/generated/numpy.ma.min.html#numpy.ma.min "numpy.ma.min")<br>(obj\[, axis, out, fill\_value, keepdims\]) | Return the minimum along a given axis. |
| [`ma.ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ptp.html#numpy.ma.ptp "numpy.ma.ptp")<br>(obj\[, axis, out, fill\_value, keepdims\]) | Return (maximum - minimum) along the given dimension (i.e. peak-to-peak value). |
| [`ma.diff`](https://numpy.org/doc/stable/reference/generated/numpy.ma.diff.html#numpy.ma.diff "numpy.ma.diff")<br>(a, /\[, n, axis, prepend, append\]) | Calculate the n-th discrete difference along the given axis. |
| [`ma.MaskedArray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmax.html#numpy.ma.MaskedArray.argmax "numpy.ma.MaskedArray.argmax")<br>(\[axis, fill\_value, ...\]) | Returns array of indices of the maximum values along the given axis. |
| [`ma.MaskedArray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmin.html#numpy.ma.MaskedArray.argmin "numpy.ma.MaskedArray.argmin")<br>(\[axis, fill\_value, ...\]) | Return array of indices to the minimum values along the given axis. |
| [`ma.MaskedArray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.max.html#numpy.ma.MaskedArray.max "numpy.ma.MaskedArray.max")<br>(\[axis, out, fill\_value, ...\]) | Return the maximum along a given axis. |
| [`ma.MaskedArray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.min.html#numpy.ma.MaskedArray.min "numpy.ma.MaskedArray.min")<br>(\[axis, out, fill\_value, ...\]) | Return the minimum along a given axis. |
| [`ma.MaskedArray.ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ptp.html#numpy.ma.MaskedArray.ptp "numpy.ma.MaskedArray.ptp")<br>(\[axis, out, fill\_value, ...\]) | Return (maximum - minimum) along the given dimension (i.e. peak-to-peak value). |

### Sorting[#](https://numpy.org/doc/stable/reference/routines.ma.html#sorting "Link to this heading")

|     |     |
| --- | --- |
| [`ma.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.argsort.html#numpy.ma.argsort "numpy.ma.argsort")<br>(a\[, axis, kind, order, endwith, ...\]) | Return an ndarray of indices that sort the array along the specified axis. |
| [`ma.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.sort.html#numpy.ma.sort "numpy.ma.sort")<br>(a\[, axis, kind, order, endwith, ...\]) | Return a sorted copy of the masked array. |
| [`ma.MaskedArray.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argsort.html#numpy.ma.MaskedArray.argsort "numpy.ma.MaskedArray.argsort")<br>(\[axis, kind, order, ...\]) | Return an ndarray of indices that sort the array along the specified axis. |
| [`ma.MaskedArray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#numpy.ma.MaskedArray.sort "numpy.ma.MaskedArray.sort")<br>(\[axis, kind, order, ...\]) | Sort the array, in-place |

### Algebra[#](https://numpy.org/doc/stable/reference/routines.ma.html#algebra "Link to this heading")

|     |     |
| --- | --- |
| [`ma.diag`](https://numpy.org/doc/stable/reference/generated/numpy.ma.diag.html#numpy.ma.diag "numpy.ma.diag")<br>(v\[, k\]) | Extract a diagonal or construct a diagonal array. |
| [`ma.dot`](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html#numpy.ma.dot "numpy.ma.dot")<br>(a, b\[, strict, out\]) | Return the dot product of two arrays. |
| [`ma.identity`](https://numpy.org/doc/stable/reference/generated/numpy.ma.identity.html#numpy.ma.identity "numpy.ma.identity")<br>(n\[, dtype, like, fill\_value, ...\]) | Return the identity array. |
| [`ma.inner`](https://numpy.org/doc/stable/reference/generated/numpy.ma.inner.html#numpy.ma.inner "numpy.ma.inner")<br>(a, b, /) | Inner product of two arrays. |
| [`ma.innerproduct`](https://numpy.org/doc/stable/reference/generated/numpy.ma.innerproduct.html#numpy.ma.innerproduct "numpy.ma.innerproduct")<br>(a, b, /) | Inner product of two arrays. |
| [`ma.outer`](https://numpy.org/doc/stable/reference/generated/numpy.ma.outer.html#numpy.ma.outer "numpy.ma.outer")<br>(a, b) | Compute the outer product of two vectors. |
| [`ma.outerproduct`](https://numpy.org/doc/stable/reference/generated/numpy.ma.outerproduct.html#numpy.ma.outerproduct "numpy.ma.outerproduct")<br>(a, b) | Compute the outer product of two vectors. |
| [`ma.trace`](https://numpy.org/doc/stable/reference/generated/numpy.ma.trace.html#numpy.ma.trace "numpy.ma.trace")<br>(a.trace) | Return the sum along diagonals of the array. |
| [`ma.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.transpose.html#numpy.ma.transpose "numpy.ma.transpose")<br>(a\[, axes\]) | Permute the dimensions of an array. |
| [`ma.MaskedArray.trace`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.trace.html#numpy.ma.MaskedArray.trace "numpy.ma.MaskedArray.trace")<br>(\[offset, axis1, axis2, ...\]) | Return the sum along diagonals of the array. |
| [`ma.MaskedArray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html#numpy.ma.MaskedArray.transpose "numpy.ma.MaskedArray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |

### Polynomial fit[#](https://numpy.org/doc/stable/reference/routines.ma.html#polynomial-fit "Link to this heading")

|     |     |
| --- | --- |
| [`ma.vander`](https://numpy.org/doc/stable/reference/generated/numpy.ma.vander.html#numpy.ma.vander "numpy.ma.vander")<br>(x\[, n\]) | Generate a Vandermonde matrix. |
| [`ma.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.ma.polyfit.html#numpy.ma.polyfit "numpy.ma.polyfit")<br>(x, y, deg\[, rcond, full, w, cov\]) | Least squares polynomial fit. |

### Clipping and rounding[#](https://numpy.org/doc/stable/reference/routines.ma.html#clipping-and-rounding "Link to this heading")

|     |     |
| --- | --- |
| [`ma.around`](https://numpy.org/doc/stable/reference/generated/numpy.ma.around.html#numpy.ma.around "numpy.ma.around") | Round an array to the given number of decimals. |
| [`ma.clip`](https://numpy.org/doc/stable/reference/generated/numpy.ma.clip.html#numpy.ma.clip "numpy.ma.clip")<br>(a\[, a\_min, a\_max, out, min, max, ...\]) | Clip (limit) the values in an array. |
| [`ma.round`](https://numpy.org/doc/stable/reference/generated/numpy.ma.round.html#numpy.ma.round "numpy.ma.round")<br>(a\[, decimals, out\]) | Return a copy of a, rounded to 'decimals' places. |
| [`ma.MaskedArray.clip`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.clip.html#numpy.ma.MaskedArray.clip "numpy.ma.MaskedArray.clip")<br>(\[min, max, out\]) | Return an array whose values are limited to `[min, max]`. |
| [`ma.MaskedArray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.round.html#numpy.ma.MaskedArray.round "numpy.ma.MaskedArray.round")<br>(\[decimals, out\]) | Return each element rounded to the given number of decimals. |

### Set operations[#](https://numpy.org/doc/stable/reference/routines.ma.html#set-operations "Link to this heading")

|     |     |
| --- | --- |
| [`ma.intersect1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.intersect1d.html#numpy.ma.intersect1d "numpy.ma.intersect1d")<br>(ar1, ar2\[, assume\_unique\]) | Returns the unique elements common to both arrays. |
| [`ma.setdiff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.setdiff1d.html#numpy.ma.setdiff1d "numpy.ma.setdiff1d")<br>(ar1, ar2\[, assume\_unique\]) | Set difference of 1D arrays with unique elements. |
| [`ma.setxor1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.setxor1d.html#numpy.ma.setxor1d "numpy.ma.setxor1d")<br>(ar1, ar2\[, assume\_unique\]) | Set exclusive-or of 1-D arrays with unique elements. |
| [`ma.union1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.union1d.html#numpy.ma.union1d "numpy.ma.union1d")<br>(ar1, ar2) | Union of two arrays. |

### Miscellanea[#](https://numpy.org/doc/stable/reference/routines.ma.html#miscellanea "Link to this heading")

|     |     |
| --- | --- |
| [`ma.allequal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.allequal.html#numpy.ma.allequal "numpy.ma.allequal")<br>(a, b\[, fill\_value\]) | Return True if all entries of a and b are equal, using fill\_value as a truth value where either or both are masked. |
| [`ma.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.allclose.html#numpy.ma.allclose "numpy.ma.allclose")<br>(a, b\[, masked\_equal, rtol, atol\]) | Returns True if two arrays are element-wise equal within a tolerance. |
| [`ma.amax`](https://numpy.org/doc/stable/reference/generated/numpy.ma.amax.html#numpy.ma.amax "numpy.ma.amax")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the maximum of an array or maximum along an axis. |
| [`ma.amin`](https://numpy.org/doc/stable/reference/generated/numpy.ma.amin.html#numpy.ma.amin "numpy.ma.amin")<br>(a\[, axis, out, keepdims, initial, where\]) | Return the minimum of an array or minimum along an axis. |
| [`ma.apply_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.ma.apply_along_axis.html#numpy.ma.apply_along_axis "numpy.ma.apply_along_axis")<br>(func1d, axis, arr, ...) | Apply a function to 1-D slices along the given axis. |
| [`ma.apply_over_axes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.apply_over_axes.html#numpy.ma.apply_over_axes "numpy.ma.apply_over_axes")<br>(func, a, axes) | Apply a function repeatedly over multiple axes. |
| [`ma.arange`](https://numpy.org/doc/stable/reference/generated/numpy.ma.arange.html#numpy.ma.arange "numpy.ma.arange")<br>(\[start,\] stop\[, step,\]\[, dtype, ...\]) | Return evenly spaced values within a given interval. |
| [`ma.choose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.choose.html#numpy.ma.choose "numpy.ma.choose")<br>(indices, choices\[, out, mode\]) | Use an index array to construct a new array from a list of choices. |
| [`ma.compress_nd`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compress_nd.html#numpy.ma.compress_nd "numpy.ma.compress_nd")<br>(x\[, axis\]) | Suppress slices from multiple dimensions which contain masked values. |
| [`ma.convolve`](https://numpy.org/doc/stable/reference/generated/numpy.ma.convolve.html#numpy.ma.convolve "numpy.ma.convolve")<br>(a, v\[, mode, propagate\_mask\]) | Returns the discrete, linear convolution of two one-dimensional sequences. |
| [`ma.correlate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.correlate.html#numpy.ma.correlate "numpy.ma.correlate")<br>(a, v\[, mode, propagate\_mask\]) | Cross-correlation of two 1-dimensional sequences. |
| [`ma.ediff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ediff1d.html#numpy.ma.ediff1d "numpy.ma.ediff1d")<br>(arr\[, to\_end, to\_begin\]) | Compute the differences between consecutive elements of an array. |
| [`ma.flatten_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatten_mask.html#numpy.ma.flatten_mask "numpy.ma.flatten_mask")<br>(mask) | Returns a completely flattened version of the mask, where nested fields are collapsed. |
| [`ma.flatten_structured_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatten_structured_array.html#numpy.ma.flatten_structured_array "numpy.ma.flatten_structured_array")<br>(a) | Flatten a structured array. |
| [`ma.fromflex`](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromflex.html#numpy.ma.fromflex "numpy.ma.fromflex")<br>(fxarray) | Build a masked array from a suitable flexible-type array. |
| [`ma.indices`](https://numpy.org/doc/stable/reference/generated/numpy.ma.indices.html#numpy.ma.indices "numpy.ma.indices")<br>(dimensions\[, dtype, sparse, ...\]) | Return an array representing the indices of a grid. |
| [`ma.left_shift`](https://numpy.org/doc/stable/reference/generated/numpy.ma.left_shift.html#numpy.ma.left_shift "numpy.ma.left_shift")<br>(a, n) | Shift the bits of an integer to the left. |
| [`ma.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ndim.html#numpy.ma.ndim "numpy.ma.ndim")<br>(obj) | Return the number of dimensions of an array. |
| [`ma.put`](https://numpy.org/doc/stable/reference/generated/numpy.ma.put.html#numpy.ma.put "numpy.ma.put")<br>(a, indices, values\[, mode\]) | Set storage-indexed locations to corresponding values. |
| [`ma.putmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.putmask.html#numpy.ma.putmask "numpy.ma.putmask")<br>(a, mask, values) | Changes elements of an array based on conditional and input values. |
| [`ma.right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.ma.right_shift.html#numpy.ma.right_shift "numpy.ma.right_shift")<br>(a, n) | Shift the bits of an integer to the right. |
| [`ma.round_`](https://numpy.org/doc/stable/reference/generated/numpy.ma.round_.html#numpy.ma.round_ "numpy.ma.round_")<br>(a\[, decimals, out\]) | Return a copy of a, rounded to 'decimals' places. |
| [`ma.take`](https://numpy.org/doc/stable/reference/generated/numpy.ma.take.html#numpy.ma.take "numpy.ma.take")<br>(a, indices\[, axis, out, mode\]) |     |
| [`ma.where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.where.html#numpy.ma.where "numpy.ma.where")<br>(condition\[, x, y\]) | Return a masked array with elements from _x_ or _y_, depending on condition. |

On this page