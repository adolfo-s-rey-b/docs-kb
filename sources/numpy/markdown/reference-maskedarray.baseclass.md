[Skip to main content](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/maskedarray.baseclass.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html)
[2.4](https://numpy.org/doc/2.4/reference/maskedarray.baseclass.html)
[2.3](https://numpy.org/doc/2.3/reference/maskedarray.baseclass.html)
[2.2](https://numpy.org/doc/2.2/reference/maskedarray.baseclass.html)
[2.1](https://numpy.org/doc/2.1/reference/maskedarray.baseclass.html)
[2.0](https://numpy.org/doc/2.0/reference/maskedarray.baseclass.html)
[1.26](https://numpy.org/doc/1.26/reference/maskedarray.baseclass.html)
[1.25](https://numpy.org/doc/1.25/reference/maskedarray.baseclass.html)
[1.24](https://numpy.org/doc/1.24/reference/maskedarray.baseclass.html)
[1.23](https://numpy.org/doc/1.23/reference/maskedarray.baseclass.html)
[1.22](https://numpy.org/doc/1.22/reference/maskedarray.baseclass.html)
[1.21](https://numpy.org/doc/1.21/reference/maskedarray.baseclass.html)
[1.20](https://numpy.org/doc/1.20/reference/maskedarray.baseclass.html)
[1.19](https://numpy.org/doc/1.19/reference/maskedarray.baseclass.html)
[1.18](https://numpy.org/doc/1.18/reference/maskedarray.baseclass.html)
[1.17](https://numpy.org/doc/1.17/reference/maskedarray.baseclass.html)
[1.16](https://numpy.org/doc/1.16/reference/maskedarray.baseclass.html)
[1.15](https://numpy.org/doc/1.15/reference/maskedarray.baseclass.html)
[1.14](https://numpy.org/doc/1.14/reference/maskedarray.baseclass.html)
[1.13](https://numpy.org/doc/1.13/reference/maskedarray.baseclass.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Constants of the [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#constants-of-the-numpy-ma-module "Link to this heading")

================================================================================================================================================================================================================================================================

In addition to the [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 class, the [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module defines several constants.

numpy.ma.masked[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "Link to this definition")

The [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
 constant is a special case of [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, with a float datatype and a null shape. It is used to test whether a specific entry of a masked array is masked, or to mask one or several entries of a masked array:

.. try\_examples::

Copy to clipboard

\>>> import numpy as np

Copy to clipboard

\>>> x \= np.ma.array(\[1, 2, 3\], mask\=\[0, 1, 0\])
\>>> x\[1\] is np.ma.masked
True
\>>> x\[\-1\] \= np.ma.masked
\>>> x
masked\_array(data=\[1, --, --\],
             mask=\[False,  True,  True\],
       fill\_value=999999)

Copy to clipboard

numpy.ma.nomask[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "Link to this definition")

Value indicating that a masked array has no invalid entry. [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 is used internally to speed up computations when the mask is not needed. It is represented internally as `np.False_`.

numpy.ma.masked\_print\_option[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked_print_option "Link to this definition")

String used in lieu of missing data when a masked array is printed. By default, this string is `'--'`.

Use `set_display()` to change the default string. Example usage: `numpy.ma.masked_print_option.set_display('X')` replaces missing data with `'X'`.

The [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 class[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#the-maskedarray-class "Link to this heading")

=============================================================================================================================================================================================================================================================

_class_ numpy.ma.MaskedArray[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2769-L6531)
[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "Link to this definition")

A subclass of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 designed to manipulate numerical arrays with missing data.

An instance of [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 can be thought as the combination of several elements:

*   The [`data`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "numpy.ma.MaskedArray.data")
    , as a regular [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
     of any shape or datatype (the data).
    
*   A boolean [`mask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.mask "numpy.ma.MaskedArray.mask")
     with the same shape as the data, where a `True` value indicates that the corresponding element of the data is invalid. The special value [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
     is also acceptable for arrays without named fields, and indicates that no data is invalid.
    
*   A [`fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")
    , a value that may be used to replace the invalid entries in order to return a standard [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    .
    

Attributes and properties of masked arrays[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#attributes-and-properties-of-masked-arrays "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See also

[Array Attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray-attributes)

ma.MaskedArray.data[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "Link to this definition")

Returns the underlying data, as a view of the masked array.

If the underlying data is a subclass of [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, it is returned as such.

\>>> x \= np.ma.array(np.matrix(\[\[1, 2\], \[3, 4\]\]), mask\=\[\[0, 1\], \[1, 0\]\])
\>>> x.data
matrix(\[\[1, 2\],\
        \[3, 4\]\])

Copy to clipboard

The type of the data can be accessed through the [`baseclass`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.baseclass "numpy.ma.MaskedArray.baseclass")
 attribute.

ma.MaskedArray.mask[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.mask "Link to this definition")

Current mask.

ma.MaskedArray.recordmask[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.recordmask "Link to this definition")

Get or set the mask of the array if it has no named fields. For structured arrays, returns an ndarray of booleans where entries are `True` if **all** the fields are masked, `False` otherwise:

\>>> x \= np.ma.array(\[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)\],
...         mask\=\[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)\],
...        dtype\=\[('a', int), ('b', int)\])
\>>> x.recordmask
array(\[False, False,  True, False, False\])

Copy to clipboard

ma.MaskedArray.fill\_value[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "Link to this definition")

The filling value of the masked array is a scalar. When setting, None will set to a default based on the data type.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> for dt in \[np.int32, np.int64, np.float64, np.complex128\]:
...     np.ma.array(\[0, 1\], dtype\=dt).get\_fill\_value()
...
np.int64(999999)
np.int64(999999)
np.float64(1e+20)
np.complex128(1e+20+0j)

Copy to clipboard

\>>> x \= np.ma.array(\[0, 1.\], fill\_value\=-np.inf)
\>>> x.fill\_value
np.float64(-inf)
\>>> x.fill\_value \= np.pi
\>>> x.fill\_value
np.float64(3.1415926535897931)

Copy to clipboard

Reset to default:

\>>> x.fill\_value \= None
\>>> x.fill\_value
np.float64(1e+20)

Copy to clipboard

Go BackOpen In Tab

ma.MaskedArray.baseclass[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.baseclass "Link to this definition")

Class of the underlying data (read-only).

ma.MaskedArray.sharedmask[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.sharedmask "Link to this definition")

Share status of the mask (read-only).

ma.MaskedArray.hardmask[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "Link to this definition")

Specifies whether values can be unmasked through assignments.

By default, assigning definite values to masked array entries will unmask them. When [`hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")
 is `True`, the mask will not change through assignments.

See also

[`ma.MaskedArray.harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy.ma.MaskedArray.harden_mask "numpy.ma.MaskedArray.harden_mask")

[`ma.MaskedArray.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.soften_mask.html#numpy.ma.MaskedArray.soften_mask "numpy.ma.MaskedArray.soften_mask")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(10)
\>>> m \= np.ma.masked\_array(x, x\>5)
\>>> assert not m.hardmask

Copy to clipboard

Since _m_ has a soft mask, assigning an element value unmasks that element:

\>>> m\[8\] \= 42
\>>> m
masked\_array(data=\[0, 1, 2, 3, 4, 5, --, --, 42, --\],
             mask=\[False, False, False, False, False, False,\
                   True, True, False, True\],
       fill\_value=999999)

Copy to clipboard

After hardening, the mask is not affected by assignments:

\>>> hardened \= np.ma.harden\_mask(m)
\>>> assert m.hardmask and hardened is m
\>>> m\[:\] \= 23
\>>> m
masked\_array(data=\[23, 23, 23, 23, 23, 23, --, --, 23, --\],
             mask=\[False, False, False, False, False, False,\
                   True, True, False, True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

As [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 is a subclass of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, a masked array also inherits all the attributes and properties of a [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 instance.

|     |     |
| --- | --- |
| [`MaskedArray.base`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.base.html#numpy.ma.MaskedArray.base "numpy.ma.MaskedArray.base") | Base object if memory is from some other object. |
| [`MaskedArray.ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ctypes.html#numpy.ma.MaskedArray.ctypes "numpy.ma.MaskedArray.ctypes") | An object to simplify the interaction of the array with the ctypes module. |
| [`MaskedArray.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.dtype.html#numpy.ma.MaskedArray.dtype "numpy.ma.MaskedArray.dtype") | Data-type of the array's elements. |
| [`MaskedArray.flags`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.flags.html#numpy.ma.MaskedArray.flags "numpy.ma.MaskedArray.flags") | Information about the memory layout of the array. |
| [`MaskedArray.itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.itemsize.html#numpy.ma.MaskedArray.itemsize "numpy.ma.MaskedArray.itemsize") | Length of one array element in bytes. |
| [`MaskedArray.nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.nbytes.html#numpy.ma.MaskedArray.nbytes "numpy.ma.MaskedArray.nbytes") | Total bytes consumed by the elements of the array. |
| [`MaskedArray.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ndim.html#numpy.ma.MaskedArray.ndim "numpy.ma.MaskedArray.ndim") | Number of array dimensions. |
| [`MaskedArray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.shape.html#numpy.ma.MaskedArray.shape "numpy.ma.MaskedArray.shape") | Tuple of array dimensions. |
| [`MaskedArray.size`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.size.html#numpy.ma.MaskedArray.size "numpy.ma.MaskedArray.size") | Number of elements in the array. |
| [`MaskedArray.strides`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.strides.html#numpy.ma.MaskedArray.strides "numpy.ma.MaskedArray.strides") | Tuple of bytes to step in each dimension when traversing an array. |
| [`MaskedArray.imag`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.imag.html#numpy.ma.MaskedArray.imag "numpy.ma.MaskedArray.imag") | The imaginary part of the masked array. |
| [`MaskedArray.real`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.real.html#numpy.ma.MaskedArray.real "numpy.ma.MaskedArray.real") | The real part of the masked array. |
| [`MaskedArray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.flat.html#numpy.ma.MaskedArray.flat "numpy.ma.MaskedArray.flat") | Return a flat iterator, or set a flattened version of self to value. |
| [`MaskedArray.__array_priority__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array_priority__.html#numpy.ma.MaskedArray.__array_priority__ "numpy.ma.MaskedArray.__array_priority__") |     |

[`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 methods[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#maskedarray-methods "Link to this heading")

=========================================================================================================================================================================================================================================================

See also

[Array methods](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-ndarray-methods)

Conversion[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#conversion "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MaskedArray.__float__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__float__.html#numpy.ma.MaskedArray.__float__ "numpy.ma.MaskedArray.__float__")<br>() | Convert to float. |
| [`MaskedArray.__int__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__int__.html#numpy.ma.MaskedArray.__int__ "numpy.ma.MaskedArray.__int__")<br>() | Convert to int. |
| [`MaskedArray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.view.html#numpy.ma.MaskedArray.view "numpy.ma.MaskedArray.view")<br>(\[dtype, type, fill\_value\]) | Return a view of the MaskedArray data. |
| [`MaskedArray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.astype.html#numpy.ma.MaskedArray.astype "numpy.ma.MaskedArray.astype")<br>(dtype\[, order, casting, ...\]) | Copy of the array, cast to a specified type. |
| [`MaskedArray.byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.byteswap.html#numpy.ma.MaskedArray.byteswap "numpy.ma.MaskedArray.byteswap")<br>(\[inplace\]) | Swap the bytes of the array elements |
| [`MaskedArray.compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "numpy.ma.MaskedArray.compressed")<br>() | Return all the non-masked data as a 1-D array. |
| [`MaskedArray.filled`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html#numpy.ma.MaskedArray.filled "numpy.ma.MaskedArray.filled")<br>(\[fill\_value\]) | Return a copy of self, with masked values filled with a given value. |
| [`MaskedArray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tofile.html#numpy.ma.MaskedArray.tofile "numpy.ma.MaskedArray.tofile")<br>(fid\[, sep, format\]) | Save a masked array to a file in binary format. |
| [`MaskedArray.toflex`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.toflex.html#numpy.ma.MaskedArray.toflex "numpy.ma.MaskedArray.toflex")<br>() | Transforms a masked array into a flexible-type array. |
| [`MaskedArray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tolist.html#numpy.ma.MaskedArray.tolist "numpy.ma.MaskedArray.tolist")<br>(\[fill\_value\]) | Return the data portion of the masked array as a hierarchical Python list. |
| [`MaskedArray.torecords`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.torecords.html#numpy.ma.MaskedArray.torecords "numpy.ma.MaskedArray.torecords")<br>() | Transforms a masked array into a flexible-type array. |
| [`MaskedArray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tobytes.html#numpy.ma.MaskedArray.tobytes "numpy.ma.MaskedArray.tobytes")<br>(\[fill\_value, order\]) | Return the array data as a string containing the raw bytes in the array. |

Shape manipulation[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#shape-manipulation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

For reshape, resize, and transpose, the single tuple argument may be replaced with `n` integers which will be interpreted as an n-tuple.

|     |     |
| --- | --- |
| [`MaskedArray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.flatten.html#numpy.ma.MaskedArray.flatten "numpy.ma.MaskedArray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |
| [`MaskedArray.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ravel.html#numpy.ma.MaskedArray.ravel "numpy.ma.MaskedArray.ravel")<br>(\[order\]) | Returns a 1D version of self, as a view. |
| [`MaskedArray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.reshape.html#numpy.ma.MaskedArray.reshape "numpy.ma.MaskedArray.reshape")<br>(\*s, \*\*kwargs) | Returns a reshaped masked array without changing its data. |
| [`MaskedArray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.resize.html#numpy.ma.MaskedArray.resize "numpy.ma.MaskedArray.resize")<br>(newshape\[, refcheck, order\]) |     |
| [`MaskedArray.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.squeeze.html#numpy.ma.MaskedArray.squeeze "numpy.ma.MaskedArray.squeeze")<br>(\[axis\]) | Remove axes of length one from _a_. |
| [`MaskedArray.swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.swapaxes.html#numpy.ma.MaskedArray.swapaxes "numpy.ma.MaskedArray.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`MaskedArray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html#numpy.ma.MaskedArray.transpose "numpy.ma.MaskedArray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |
| [`MaskedArray.T`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.T.html#numpy.ma.MaskedArray.T "numpy.ma.MaskedArray.T") | View of the transposed array. |

Item selection and manipulation[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#item-selection-and-manipulation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

For array methods that take an `axis` keyword, it defaults to None. If axis is None, then the array is treated as a 1-D array. Any other value for `axis` represents the dimension along which the operation should proceed.

|     |     |
| --- | --- |
| [`MaskedArray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmax.html#numpy.ma.MaskedArray.argmax "numpy.ma.MaskedArray.argmax")<br>(\[axis, fill\_value, out, ...\]) | Returns array of indices of the maximum values along the given axis. |
| [`MaskedArray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmin.html#numpy.ma.MaskedArray.argmin "numpy.ma.MaskedArray.argmin")<br>(\[axis, fill\_value, out, ...\]) | Return array of indices to the minimum values along the given axis. |
| [`MaskedArray.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argsort.html#numpy.ma.MaskedArray.argsort "numpy.ma.MaskedArray.argsort")<br>(\[axis, kind, order, ...\]) | Return an ndarray of indices that sort the array along the specified axis. |
| [`MaskedArray.choose`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.choose.html#numpy.ma.MaskedArray.choose "numpy.ma.MaskedArray.choose")<br>(choices\[, out, mode\]) | Use an index array to construct a new array from a set of choices. |
| [`MaskedArray.compress`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compress.html#numpy.ma.MaskedArray.compress "numpy.ma.MaskedArray.compress")<br>(condition\[, axis, out\]) | Return _a_ where condition is `True`. |
| [`MaskedArray.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.diagonal.html#numpy.ma.MaskedArray.diagonal "numpy.ma.MaskedArray.diagonal")<br>(\[offset, axis1, axis2\]) | Return specified diagonals. |
| [`MaskedArray.fill`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.fill.html#numpy.ma.MaskedArray.fill "numpy.ma.MaskedArray.fill")<br>(value) | Fill the array with a scalar value. |
| [`MaskedArray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.item.html#numpy.ma.MaskedArray.item "numpy.ma.MaskedArray.item")<br>(\*args) | Copy an element of an array to a standard Python scalar and return it. |
| [`MaskedArray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.nonzero.html#numpy.ma.MaskedArray.nonzero "numpy.ma.MaskedArray.nonzero")<br>() | Return the indices of unmasked elements that are not zero. |
| [`MaskedArray.put`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html#numpy.ma.MaskedArray.put "numpy.ma.MaskedArray.put")<br>(indices, values\[, mode\]) | Set storage-indexed locations to corresponding values. |
| [`MaskedArray.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.repeat.html#numpy.ma.MaskedArray.repeat "numpy.ma.MaskedArray.repeat")<br>(repeats\[, axis\]) | Repeat elements of an array. |
| [`MaskedArray.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.searchsorted.html#numpy.ma.MaskedArray.searchsorted "numpy.ma.MaskedArray.searchsorted")<br>(v\[, side, sorter\]) | Find indices where elements of _v_ should be inserted in _a_ to maintain order. |
| [`MaskedArray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sort.html#numpy.ma.MaskedArray.sort "numpy.ma.MaskedArray.sort")<br>(\[axis, kind, order, ...\]) | Sort the array, in-place |
| [`MaskedArray.take`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.take.html#numpy.ma.MaskedArray.take "numpy.ma.MaskedArray.take")<br>(indices\[, axis, out, mode\]) | Take elements from a masked array along an axis. |

Pickling and copy[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#pickling-and-copy "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MaskedArray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.copy.html#numpy.ma.MaskedArray.copy "numpy.ma.MaskedArray.copy")<br>(\[order\]) | Return a copy of the array. |
| [`MaskedArray.dump`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.dump.html#numpy.ma.MaskedArray.dump "numpy.ma.MaskedArray.dump")<br>(file) | Dump a pickle of the array to the specified file. |
| [`MaskedArray.dumps`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.dumps.html#numpy.ma.MaskedArray.dumps "numpy.ma.MaskedArray.dumps")<br>() | Returns the pickle of the array as a string. |

Calculations[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#calculations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MaskedArray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.all.html#numpy.ma.MaskedArray.all "numpy.ma.MaskedArray.all")<br>(\[axis, out, keepdims\]) | Returns True if all elements evaluate to True. |
| [`MaskedArray.anom`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.anom.html#numpy.ma.MaskedArray.anom "numpy.ma.MaskedArray.anom")<br>(\[axis, dtype\]) | Compute the anomalies (deviations from the arithmetic mean) along the given axis. |
| [`MaskedArray.any`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.any.html#numpy.ma.MaskedArray.any "numpy.ma.MaskedArray.any")<br>(\[axis, out, keepdims\]) | Returns True if any of the elements of _a_ evaluate to True. |
| [`MaskedArray.clip`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.clip.html#numpy.ma.MaskedArray.clip "numpy.ma.MaskedArray.clip")<br>(\[min, max, out\]) | Return an array whose values are limited to `[min, max]`. |
| [`MaskedArray.conj`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.conj.html#numpy.ma.MaskedArray.conj "numpy.ma.MaskedArray.conj")<br>() | Complex-conjugate all elements. |
| [`MaskedArray.conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.conjugate.html#numpy.ma.MaskedArray.conjugate "numpy.ma.MaskedArray.conjugate")<br>() | Return the complex conjugate, element-wise. |
| [`MaskedArray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumprod.html#numpy.ma.MaskedArray.cumprod "numpy.ma.MaskedArray.cumprod")<br>(\[axis, dtype, out\]) | Return the cumulative product of the array elements over the given axis. |
| [`MaskedArray.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumsum.html#numpy.ma.MaskedArray.cumsum "numpy.ma.MaskedArray.cumsum")<br>(\[axis, dtype, out\]) | Return the cumulative sum of the array elements over the given axis. |
| [`MaskedArray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.max.html#numpy.ma.MaskedArray.max "numpy.ma.MaskedArray.max")<br>(\[axis, out, fill\_value, ...\]) | Return the maximum along a given axis. |
| [`MaskedArray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.mean.html#numpy.ma.MaskedArray.mean "numpy.ma.MaskedArray.mean")<br>(\[axis, dtype, out, keepdims\]) | Returns the average of the array elements along given axis. |
| [`MaskedArray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.min.html#numpy.ma.MaskedArray.min "numpy.ma.MaskedArray.min")<br>(\[axis, out, fill\_value, ...\]) | Return the minimum along a given axis. |
| [`MaskedArray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.prod.html#numpy.ma.MaskedArray.prod "numpy.ma.MaskedArray.prod")<br>(\[axis, dtype, out, keepdims\]) | Return the product of the array elements over the given axis. |
| [`MaskedArray.product`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.product.html#numpy.ma.MaskedArray.product "numpy.ma.MaskedArray.product")<br>(\[axis, dtype, out, keepdims\]) | Return the product of the array elements over the given axis. |
| [`MaskedArray.ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ptp.html#numpy.ma.MaskedArray.ptp "numpy.ma.MaskedArray.ptp")<br>(\[axis, out, fill\_value, ...\]) | Return (maximum - minimum) along the given dimension (i.e. peak-to-peak value). |
| [`MaskedArray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.round.html#numpy.ma.MaskedArray.round "numpy.ma.MaskedArray.round")<br>(\[decimals, out\]) | Return each element rounded to the given number of decimals. |
| [`MaskedArray.std`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.std.html#numpy.ma.MaskedArray.std "numpy.ma.MaskedArray.std")<br>(\[axis, dtype, out, ddof, ...\]) | Returns the standard deviation of the array elements along given axis. |
| [`MaskedArray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sum.html#numpy.ma.MaskedArray.sum "numpy.ma.MaskedArray.sum")<br>(\[axis, dtype, out, keepdims\]) | Return the sum of the array elements over the given axis. |
| [`MaskedArray.trace`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.trace.html#numpy.ma.MaskedArray.trace "numpy.ma.MaskedArray.trace")<br>(\[offset, axis1, axis2, ...\]) | Return the sum along diagonals of the array. |
| [`MaskedArray.var`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.var.html#numpy.ma.MaskedArray.var "numpy.ma.MaskedArray.var")<br>(\[axis, dtype, out, ddof, ...\]) | Compute the variance along the specified axis. |

Arithmetic and comparison operations[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#arithmetic-and-comparison-operations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Comparison operators:[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#comparison-operators "Link to this heading")

|     |     |
| --- | --- |
| [`MaskedArray.__lt__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__lt__.html#numpy.ma.MaskedArray.__lt__ "numpy.ma.MaskedArray.__lt__")<br>(other) | Return self<value. |
| [`MaskedArray.__le__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__le__.html#numpy.ma.MaskedArray.__le__ "numpy.ma.MaskedArray.__le__")<br>(other) | Return self<=value. |
| [`MaskedArray.__gt__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__gt__.html#numpy.ma.MaskedArray.__gt__ "numpy.ma.MaskedArray.__gt__")<br>(other) | Return self>value. |
| [`MaskedArray.__ge__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ge__.html#numpy.ma.MaskedArray.__ge__ "numpy.ma.MaskedArray.__ge__")<br>(other) | Return self>=value. |
| [`MaskedArray.__eq__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__eq__.html#numpy.ma.MaskedArray.__eq__ "numpy.ma.MaskedArray.__eq__")<br>(other) | Check whether other equals self elementwise. |
| [`MaskedArray.__ne__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ne__.html#numpy.ma.MaskedArray.__ne__ "numpy.ma.MaskedArray.__ne__")<br>(other) | Check whether other does not equal self elementwise. |

### Truth value of an array ([`bool()`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
):[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#truth-value-of-an-array-bool "Link to this heading")

|     |     |
| --- | --- |
| [`MaskedArray.__bool__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__bool__.html#numpy.ma.MaskedArray.__bool__ "numpy.ma.MaskedArray.__bool__")<br>(/) | True if self else False |

### Arithmetic:[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#arithmetic "Link to this heading")

|     |     |
| --- | --- |
| [`MaskedArray.__abs__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__abs__.html#numpy.ma.MaskedArray.__abs__ "numpy.ma.MaskedArray.__abs__")<br>(self) |     |
| [`MaskedArray.__add__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__add__.html#numpy.ma.MaskedArray.__add__ "numpy.ma.MaskedArray.__add__")<br>(other) | Add self to other, and return a new masked array. |
| [`MaskedArray.__radd__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__radd__.html#numpy.ma.MaskedArray.__radd__ "numpy.ma.MaskedArray.__radd__")<br>(other) | Add other to self, and return a new masked array. |
| [`MaskedArray.__sub__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__sub__.html#numpy.ma.MaskedArray.__sub__ "numpy.ma.MaskedArray.__sub__")<br>(other) | Subtract other from self, and return a new masked array. |
| [`MaskedArray.__rsub__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rsub__.html#numpy.ma.MaskedArray.__rsub__ "numpy.ma.MaskedArray.__rsub__")<br>(other) | Subtract self from other, and return a new masked array. |
| [`MaskedArray.__mul__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__mul__.html#numpy.ma.MaskedArray.__mul__ "numpy.ma.MaskedArray.__mul__")<br>(other) | Multiply self by other, and return a new masked array. |
| [`MaskedArray.__rmul__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rmul__.html#numpy.ma.MaskedArray.__rmul__ "numpy.ma.MaskedArray.__rmul__")<br>(other) | Multiply other by self, and return a new masked array. |
| [`MaskedArray.__truediv__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__truediv__.html#numpy.ma.MaskedArray.__truediv__ "numpy.ma.MaskedArray.__truediv__")<br>(other) | Divide other into self, and return a new masked array. |
| [`MaskedArray.__rtruediv__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rtruediv__.html#numpy.ma.MaskedArray.__rtruediv__ "numpy.ma.MaskedArray.__rtruediv__")<br>(other) | Divide self into other, and return a new masked array. |
| [`MaskedArray.__floordiv__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__floordiv__.html#numpy.ma.MaskedArray.__floordiv__ "numpy.ma.MaskedArray.__floordiv__")<br>(other) | Divide other into self, and return a new masked array. |
| [`MaskedArray.__rfloordiv__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rfloordiv__.html#numpy.ma.MaskedArray.__rfloordiv__ "numpy.ma.MaskedArray.__rfloordiv__")<br>(other) | Divide self into other, and return a new masked array. |
| [`MaskedArray.__mod__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__mod__.html#numpy.ma.MaskedArray.__mod__ "numpy.ma.MaskedArray.__mod__")<br>(value, /) | Return self%value. |
| [`MaskedArray.__rmod__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rmod__.html#numpy.ma.MaskedArray.__rmod__ "numpy.ma.MaskedArray.__rmod__")<br>(value, /) | Return value%self. |
| [`MaskedArray.__divmod__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__divmod__.html#numpy.ma.MaskedArray.__divmod__ "numpy.ma.MaskedArray.__divmod__")<br>(value, /) | Return divmod(self, value). |
| [`MaskedArray.__rdivmod__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rdivmod__.html#numpy.ma.MaskedArray.__rdivmod__ "numpy.ma.MaskedArray.__rdivmod__")<br>(value, /) | Return divmod(value, self). |
| [`MaskedArray.__pow__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__pow__.html#numpy.ma.MaskedArray.__pow__ "numpy.ma.MaskedArray.__pow__")<br>(other) | Raise self to the power other, masking the potential NaNs/Infs |
| [`MaskedArray.__rpow__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rpow__.html#numpy.ma.MaskedArray.__rpow__ "numpy.ma.MaskedArray.__rpow__")<br>(other) | Raise other to the power self, masking the potential NaNs/Infs |
| [`MaskedArray.__lshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__lshift__.html#numpy.ma.MaskedArray.__lshift__ "numpy.ma.MaskedArray.__lshift__")<br>(value, /) | Return self<<value. |
| [`MaskedArray.__rlshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rlshift__.html#numpy.ma.MaskedArray.__rlshift__ "numpy.ma.MaskedArray.__rlshift__")<br>(value, /) | Return value<<self. |
| [`MaskedArray.__rshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rshift__.html#numpy.ma.MaskedArray.__rshift__ "numpy.ma.MaskedArray.__rshift__")<br>(value, /) | Return self>>value. |
| [`MaskedArray.__rrshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rrshift__.html#numpy.ma.MaskedArray.__rrshift__ "numpy.ma.MaskedArray.__rrshift__")<br>(value, /) | Return value>>self. |
| [`MaskedArray.__and__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__and__.html#numpy.ma.MaskedArray.__and__ "numpy.ma.MaskedArray.__and__")<br>(value, /) | Return self&value. |
| [`MaskedArray.__rand__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rand__.html#numpy.ma.MaskedArray.__rand__ "numpy.ma.MaskedArray.__rand__")<br>(value, /) | Return value&self. |
| [`MaskedArray.__or__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__or__.html#numpy.ma.MaskedArray.__or__ "numpy.ma.MaskedArray.__or__")<br>(value, /) | Return self\|value. |
| [`MaskedArray.__ror__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ror__.html#numpy.ma.MaskedArray.__ror__ "numpy.ma.MaskedArray.__ror__")<br>(value, /) | Return value\|self. |
| [`MaskedArray.__xor__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__xor__.html#numpy.ma.MaskedArray.__xor__ "numpy.ma.MaskedArray.__xor__")<br>(value, /) | Return self^value. |
| [`MaskedArray.__rxor__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__rxor__.html#numpy.ma.MaskedArray.__rxor__ "numpy.ma.MaskedArray.__rxor__")<br>(value, /) | Return value^self. |

### Arithmetic, in-place:[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#arithmetic-in-place "Link to this heading")

|     |     |
| --- | --- |
| [`MaskedArray.__iadd__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__iadd__.html#numpy.ma.MaskedArray.__iadd__ "numpy.ma.MaskedArray.__iadd__")<br>(other) | Add other to self in-place. |
| [`MaskedArray.__isub__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__isub__.html#numpy.ma.MaskedArray.__isub__ "numpy.ma.MaskedArray.__isub__")<br>(other) | Subtract other from self in-place. |
| [`MaskedArray.__imul__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__imul__.html#numpy.ma.MaskedArray.__imul__ "numpy.ma.MaskedArray.__imul__")<br>(other) | Multiply self by other in-place. |
| [`MaskedArray.__itruediv__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__itruediv__.html#numpy.ma.MaskedArray.__itruediv__ "numpy.ma.MaskedArray.__itruediv__")<br>(other) | True divide self by other in-place. |
| [`MaskedArray.__ifloordiv__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ifloordiv__.html#numpy.ma.MaskedArray.__ifloordiv__ "numpy.ma.MaskedArray.__ifloordiv__")<br>(other) | Floor divide self by other in-place. |
| [`MaskedArray.__imod__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__imod__.html#numpy.ma.MaskedArray.__imod__ "numpy.ma.MaskedArray.__imod__")<br>(value, /) | Return self%=value. |
| [`MaskedArray.__ipow__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ipow__.html#numpy.ma.MaskedArray.__ipow__ "numpy.ma.MaskedArray.__ipow__")<br>(other) | Raise self to the power other, in place. |
| [`MaskedArray.__ilshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ilshift__.html#numpy.ma.MaskedArray.__ilshift__ "numpy.ma.MaskedArray.__ilshift__")<br>(value, /) | Return self<<=value. |
| [`MaskedArray.__irshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__irshift__.html#numpy.ma.MaskedArray.__irshift__ "numpy.ma.MaskedArray.__irshift__")<br>(value, /) | Return self>>=value. |
| [`MaskedArray.__iand__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__iand__.html#numpy.ma.MaskedArray.__iand__ "numpy.ma.MaskedArray.__iand__")<br>(value, /) | Return self&=value. |
| [`MaskedArray.__ior__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ior__.html#numpy.ma.MaskedArray.__ior__ "numpy.ma.MaskedArray.__ior__")<br>(value, /) | Return self\|=value. |
| [`MaskedArray.__ixor__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__ixor__.html#numpy.ma.MaskedArray.__ixor__ "numpy.ma.MaskedArray.__ixor__")<br>(value, /) | Return self^=value. |

Representation[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#representation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MaskedArray.__repr__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__repr__.html#numpy.ma.MaskedArray.__repr__ "numpy.ma.MaskedArray.__repr__")<br>() | Literal string representation. |
| [`MaskedArray.__str__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__str__.html#numpy.ma.MaskedArray.__str__ "numpy.ma.MaskedArray.__str__")<br>() | Return str(self). |
| [`MaskedArray.ids`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.ids.html#numpy.ma.MaskedArray.ids "numpy.ma.MaskedArray.ids")<br>() | Return the addresses of the data and mask areas. |
| [`MaskedArray.iscontiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.iscontiguous.html#numpy.ma.MaskedArray.iscontiguous "numpy.ma.MaskedArray.iscontiguous")<br>() | Return a boolean indicating whether the data is contiguous. |

Special methods[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#special-methods "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

For standard library functions:

|     |     |
| --- | --- |
| [`MaskedArray.__copy__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__copy__.html#numpy.ma.MaskedArray.__copy__ "numpy.ma.MaskedArray.__copy__")<br>() | Used if [`copy.copy`](https://docs.python.org/3/library/copy.html#copy.copy "(in Python v3.14)")<br> is called on an array. |
| [`MaskedArray.__deepcopy__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__deepcopy__.html#numpy.ma.MaskedArray.__deepcopy__ "numpy.ma.MaskedArray.__deepcopy__")<br>(memo, /) | Used if [`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.14)")<br> is called on an array. |
| [`MaskedArray.__getstate__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__getstate__.html#numpy.ma.MaskedArray.__getstate__ "numpy.ma.MaskedArray.__getstate__")<br>() | Return the internal state of the masked array, for pickling purposes. |
| [`MaskedArray.__reduce__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__reduce__.html#numpy.ma.MaskedArray.__reduce__ "numpy.ma.MaskedArray.__reduce__")<br>() | Return a 3-tuple for pickling a MaskedArray. |
| [`MaskedArray.__setstate__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__setstate__.html#numpy.ma.MaskedArray.__setstate__ "numpy.ma.MaskedArray.__setstate__")<br>(state) | Restore the internal state of the masked array, for pickling purposes. |

Basic customization:

|     |     |
| --- | --- |
| [`MaskedArray.__new__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__new__.html#numpy.ma.MaskedArray.__new__ "numpy.ma.MaskedArray.__new__")<br>(cls\[, data, mask, ...\]) | Create a new masked array from scratch. |
| [`MaskedArray.__array__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array__.html#numpy.ma.MaskedArray.__array__ "numpy.ma.MaskedArray.__array__")<br>(\[dtype\], \*\[, copy\]) | For `dtype` parameter it returns a new reference to self if `dtype` is not given or it matches array's data type. |
| [`MaskedArray.__array_wrap__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array_wrap__.html#numpy.ma.MaskedArray.__array_wrap__ "numpy.ma.MaskedArray.__array_wrap__")<br>(obj\[, context, ...\]) | Special hook for ufuncs. |

Container customization: (see [Indexing](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
)

|     |     |
| --- | --- |
| [`MaskedArray.__len__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__len__.html#numpy.ma.MaskedArray.__len__ "numpy.ma.MaskedArray.__len__")<br>(/) | Return len(self). |
| [`MaskedArray.__getitem__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__getitem__.html#numpy.ma.MaskedArray.__getitem__ "numpy.ma.MaskedArray.__getitem__")<br>(indx) | x.\_\_getitem\_\_(y) <==> x\[y\] |
| [`MaskedArray.__setitem__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__setitem__.html#numpy.ma.MaskedArray.__setitem__ "numpy.ma.MaskedArray.__setitem__")<br>(indx, value) | x.\_\_setitem\_\_(i, y) <==> x\[i\]=y |
| [`MaskedArray.__delitem__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__delitem__.html#numpy.ma.MaskedArray.__delitem__ "numpy.ma.MaskedArray.__delitem__")<br>(key, /) | Delete self\[key\]. |
| [`MaskedArray.__contains__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__contains__.html#numpy.ma.MaskedArray.__contains__ "numpy.ma.MaskedArray.__contains__")<br>(key, /) | Return bool(key in self). |

Specific methods[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#specific-methods "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Handling the mask[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#handling-the-mask "Link to this heading")

The following methods can be used to access information about the mask or to manipulate the mask.

|     |     |
| --- | --- |
| [`MaskedArray.__setmask__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__setmask__.html#numpy.ma.MaskedArray.__setmask__ "numpy.ma.MaskedArray.__setmask__")<br>(mask\[, copy\]) | Set the mask. |
| [`MaskedArray.harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy.ma.MaskedArray.harden_mask "numpy.ma.MaskedArray.harden_mask")<br>() | Force the mask to hard, preventing unmasking by assignment. |
| [`MaskedArray.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.soften_mask.html#numpy.ma.MaskedArray.soften_mask "numpy.ma.MaskedArray.soften_mask")<br>() | Force the mask to soft (default), allowing unmasking by assignment. |
| [`MaskedArray.unshare_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.unshare_mask.html#numpy.ma.MaskedArray.unshare_mask "numpy.ma.MaskedArray.unshare_mask")<br>() | Copy the mask and set the _sharedmask_ flag to `False`. |
| [`MaskedArray.shrink_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.shrink_mask.html#numpy.ma.MaskedArray.shrink_mask "numpy.ma.MaskedArray.shrink_mask")<br>() | Reduce a mask to nomask when possible. |

### Handling the _fill\_value_[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#handling-the-fill-value "Link to this heading")

|     |     |
| --- | --- |
| [`MaskedArray.get_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.get_fill_value.html#numpy.ma.MaskedArray.get_fill_value "numpy.ma.MaskedArray.get_fill_value")<br>() | The filling value of the masked array is a scalar. |
| [`MaskedArray.set_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.set_fill_value.html#numpy.ma.MaskedArray.set_fill_value "numpy.ma.MaskedArray.set_fill_value")<br>(\[value\]) |     |

### Counting the missing elements[#](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#counting-the-missing-elements "Link to this heading")

|     |     |
| --- | --- |
| [`MaskedArray.count`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.count.html#numpy.ma.MaskedArray.count "numpy.ma.MaskedArray.count")<br>(\[axis, keepdims\]) | Count the non-masked elements of the array along the given axis. |

On this page