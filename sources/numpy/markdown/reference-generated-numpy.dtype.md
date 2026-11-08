[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy-dtype "Link to this heading")

=====================================================================================================================

_class_ numpy.dtype(_dtype_, _align\=False_, _copy\=False_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "Link to this definition")

–

dtype(dtype, align=False, copy=False, \[metadata\])

Create a data type object.

A numpy array is homogeneous, and contains elements described by a dtype object. A dtype object can be constructed from different combinations of fundamental numeric types.

Parameters:

**dtype**

Object to be converted to a data type object.

**align**bool, optional

Add padding to the fields to match what a C compiler would output for a similar C-struct. Can be `True` only if _obj_ is a dictionary or a comma-separated string. If a struct dtype is being created, this also sets a sticky alignment flag `isalignedstruct`.

**copy**bool, optional

Make a new copy of the data-type object. If `False`, the result may just be a reference to a built-in data-type object.

**metadata**dict, optional

An optional dictionary with dtype metadata.

Attributes:

[`alignment`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.alignment.html#numpy.dtype.alignment "numpy.dtype.alignment")

The required alignment (bytes) of this data-type according to the compiler.

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.base.html#numpy.dtype.base "numpy.dtype.base")

Returns dtype for the base element of the subarrays, regardless of their dimension or shape.

[`byteorder`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html#numpy.dtype.byteorder "numpy.dtype.byteorder")

A character indicating the byte-order of this data-type object.

[`char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")

A unique character code for each of the 21 different built-in types.

[`descr`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.descr.html#numpy.dtype.descr "numpy.dtype.descr")

_\_\_array\_interface\_\__ description of the data-type.

[`fields`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html#numpy.dtype.fields "numpy.dtype.fields")

Dictionary of named fields defined for this data type, or `None`.

[`flags`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.flags.html#numpy.dtype.flags "numpy.dtype.flags")

Bit-flags describing how this data type is to be interpreted.

[`hasobject`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.hasobject.html#numpy.dtype.hasobject "numpy.dtype.hasobject")

Boolean indicating whether this dtype contains any reference-counted objects in any fields or sub-dtypes.

[`isalignedstruct`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.isalignedstruct.html#numpy.dtype.isalignedstruct "numpy.dtype.isalignedstruct")

Boolean indicating whether the dtype is a struct which maintains field alignment.

[`isbuiltin`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.isbuiltin.html#numpy.dtype.isbuiltin "numpy.dtype.isbuiltin")

Integer indicating how this dtype relates to the built-in dtypes.

[`isnative`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.isnative.html#numpy.dtype.isnative "numpy.dtype.isnative")

Boolean indicating whether the byte order of this dtype is native to the platform.

[`itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.itemsize.html#numpy.dtype.itemsize "numpy.dtype.itemsize")

The element size of this data-type object.

[`kind`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy.dtype.kind "numpy.dtype.kind")

A character code (one of ‘biufcmMOSTUV’) identifying the general kind of data.

[`metadata`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.metadata.html#numpy.dtype.metadata "numpy.dtype.metadata")

Either `None` or a readonly dictionary of metadata (mappingproxy).

[`name`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.name.html#numpy.dtype.name "numpy.dtype.name")

A bit-width name for this data-type.

[`names`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.names.html#numpy.dtype.names "numpy.dtype.names")

Ordered list of field names, or `None` if there are no fields.

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")

Number of dimensions of the sub-array if this data type describes a sub-array, and `0` otherwise.

[`num`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.num.html#numpy.dtype.num "numpy.dtype.num")

A unique number for each of the 21 different built-in types.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

Shape tuple of the sub-array if this data type describes a sub-array, and `()` otherwise.

[`str`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.str.html#numpy.dtype.str "numpy.dtype.str")

The array-protocol typestring of this data-type object.

[`subdtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.subdtype.html#numpy.dtype.subdtype "numpy.dtype.subdtype")

Tuple `(item_dtype, shape)` if this [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 describes a sub-array, and None otherwise.

**type**

Methods

|     |     |
| --- | --- |
| [`newbyteorder`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.newbyteorder.html#numpy.dtype.newbyteorder "numpy.dtype.newbyteorder")<br>(\[new\_order\]) | Return a new dtype with a different byte order. |

See also

[`result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")

Examples

Try it in your browser!

Using array-scalar type:

\>>> import numpy as np
\>>> np.dtype(np.int16)
dtype('int16')

Copy to clipboard

Structured type, one field name ‘f1’, containing int16:

\>>> np.dtype(\[('f1', np.int16)\])
dtype(\[('f1', '<i2')\])

Copy to clipboard

Structured type, one field named ‘f1’, in itself containing a structured type with one field:

\>>> np.dtype(\[('f1', \[('f1', np.int16)\])\])
dtype(\[('f1', \[('f1', '<i2')\])\])

Copy to clipboard

Structured type, two fields: the first field contains an unsigned int, the second an int32:

\>>> np.dtype(\[('f1', np.uint64), ('f2', np.int32)\])
dtype(\[('f1', '<u8'), ('f2', '<i4')\])

Copy to clipboard

Using array-protocol type strings:

\>>> np.dtype(\[('a','f8'),('b','S10')\])
dtype(\[('a', '<f8'), ('b', 'S10')\])

Copy to clipboard

Using comma-separated field formats. The shape is (2,3):

\>>> np.dtype("i4, (2,3)f8")
dtype(\[('f0', '<i4'), ('f1', '<f8', (2, 3))\])

Copy to clipboard

Using tuples. `int` is a fixed type, 3 the field’s shape. `void` is a flexible type, here of size 10:

\>>> np.dtype(\[('hello',(np.int64,3)),('world',np.void,10)\])
dtype(\[('hello', '<i8', (3,)), ('world', 'V10')\])

Copy to clipboard

Subdivide `int16` into 2 `int8`’s, called x and y. 0 and 1 are the offsets in bytes:

\>>> np.dtype((np.int16, {'x':(np.int8,0), 'y':(np.int8,1)}))
dtype((numpy.int16, \[('x', 'i1'), ('y', 'i1')\]))

Copy to clipboard

Using dictionaries. Two fields named ‘gender’ and ‘age’:

\>>> np.dtype({'names':\['gender','age'\], 'formats':\['S1',np.uint8\]})
dtype(\[('gender', 'S1'), ('age', 'u1')\])

Copy to clipboard

Offsets in bytes, here 0 and 25:

\>>> np.dtype({'surname':('S25',0),'age':(np.uint8,25)})
dtype(\[('surname', 'S25'), ('age', 'u1')\])

Copy to clipboard

Go BackOpen In Tab

On this page