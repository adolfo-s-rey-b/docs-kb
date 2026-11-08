[Skip to main content](https://numpy.org/doc/stable/user/basics.rec.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/basics.rec.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/basics.rec.html)
[2.4](https://numpy.org/doc/2.4/user/basics.rec.html)
[2.3](https://numpy.org/doc/2.3/user/basics.rec.html)
[2.2](https://numpy.org/doc/2.2/user/basics.rec.html)
[2.1](https://numpy.org/doc/2.1/user/basics.rec.html)
[2.0](https://numpy.org/doc/2.0/user/basics.rec.html)
[1.26](https://numpy.org/doc/1.26/user/basics.rec.html)
[1.25](https://numpy.org/doc/1.25/user/basics.rec.html)
[1.24](https://numpy.org/doc/1.24/user/basics.rec.html)
[1.23](https://numpy.org/doc/1.23/user/basics.rec.html)
[1.22](https://numpy.org/doc/1.22/user/basics.rec.html)
[1.21](https://numpy.org/doc/1.21/user/basics.rec.html)
[1.20](https://numpy.org/doc/1.20/user/basics.rec.html)
[1.19](https://numpy.org/doc/1.19/user/basics.rec.html)
[1.18](https://numpy.org/doc/1.18/user/basics.rec.html)
[1.17](https://numpy.org/doc/1.17/user/basics.rec.html)
[1.16](https://numpy.org/doc/1.16/user/basics.rec.html)
[1.15](https://numpy.org/doc/1.15/user/basics.rec.html)
[1.14](https://numpy.org/doc/1.14/user/basics.rec.html)
[1.13](https://numpy.org/doc/1.13/user/basics.rec.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Structured arrays[#](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays "Link to this heading")

=================================================================================================================

Introduction[#](https://numpy.org/doc/stable/user/basics.rec.html#introduction "Link to this heading")

-------------------------------------------------------------------------------------------------------

Structured arrays are ndarrays whose datatype is a composition of simpler datatypes organized as a sequence of named [fields](https://numpy.org/doc/stable/glossary.html#term-field)
. For example,

\>>> x \= np.array(\[('Rex', 9, 81.0), ('Fido', 3, 27.0)\],
...              dtype\=\[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')\])
\>>> x
array(\[('Rex', 9, 81.), ('Fido', 3, 27.)\],
      dtype=\[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')\])

Copy to clipboard

Here `x` is a one-dimensional array of length two whose datatype is a structure with three fields: 1. A string of length 10 or less named ‘name’, 2. a 32-bit integer named ‘age’, and 3. a 32-bit float named ‘weight’.

If you index `x` at position 1 you get a structure:

\>>> x\[1\]
np.void(('Fido', 3, 27.0), dtype=\[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')\])

Copy to clipboard

You can access and modify individual fields of a structured array by indexing with the field name:

\>>> x\['age'\]
array(\[9, 3\], dtype=int32)
\>>> x\['age'\] \= 5
\>>> x
array(\[('Rex', 5, 81.), ('Fido', 5, 27.)\],
      dtype=\[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')\])

Copy to clipboard

Structured datatypes are designed to be able to mimic ‘structs’ in the C language, and share a similar memory layout. They are meant for interfacing with C code and for low-level manipulation of structured buffers, for example for interpreting binary blobs. For these purposes they support specialized features such as subarrays, nested datatypes, and unions, and allow control over the memory layout of the structure.

Users looking to manipulate tabular data, such as stored in csv files, may find other pydata projects more suitable, such as xarray, pandas, or DataArray. These provide a high-level interface for tabular data analysis and are better optimized for that use. For instance, the C-struct-like memory layout of structured arrays in numpy can lead to poor cache behavior in comparison.

Structured datatypes[#](https://numpy.org/doc/stable/user/basics.rec.html#structured-datatypes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

A structured datatype can be thought of as a sequence of bytes of a certain length (the structure’s [itemsize](https://numpy.org/doc/stable/glossary.html#term-itemsize)
) which is interpreted as a collection of fields. Each field has a name, a datatype, and a byte offset within the structure. The datatype of a field may be any numpy datatype including other structured datatypes, and it may also be a [subarray data type](https://numpy.org/doc/stable/glossary.html#term-subarray-data-type)
 which behaves like an ndarray of a specified shape. The offsets of the fields are arbitrary, and fields may even overlap. These offsets are usually determined automatically by numpy, but can also be specified.

### Structured datatype creation[#](https://numpy.org/doc/stable/user/basics.rec.html#structured-datatype-creation "Link to this heading")

Structured datatypes may be created using the function [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
. There are 4 alternative forms of specification which vary in flexibility and conciseness. These are further documented in the [Data Type Objects](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing)
 reference page, and in summary they are:

1.  A list of tuples, one tuple per field
    
    Each tuple has the form `(fieldname, datatype, shape)` where shape is optional. `fieldname` is a string (or tuple if titles are used, see [Field Titles](https://numpy.org/doc/stable/user/basics.rec.html#titles)
     below), `datatype` may be any object convertible to a datatype, and `shape` is a tuple of integers specifying subarray shape.
    
    \>>> np.dtype(\[('x', 'f4'), ('y', np.float32), ('z', 'f4', (2, 2))\])
    dtype(\[('x', '<f4'), ('y', '<f4'), ('z', '<f4', (2, 2))\])
    
    Copy to clipboard
    
    If `fieldname` is the empty string `''`, the field will be given a default name of the form `f#`, where `#` is the integer index of the field, counting from 0 from the left:
    
    \>>> np.dtype(\[('x', 'f4'), ('', 'i4'), ('z', 'i8')\])
    dtype(\[('x', '<f4'), ('f1', '<i4'), ('z', '<i8')\])
    
    Copy to clipboard
    
    The byte offsets of the fields within the structure and the total structure itemsize are determined automatically.
    
2.  A string of comma-separated dtype specifications
    
    In this shorthand notation any of the [string dtype specifications](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing)
     may be used in a string and separated by commas. The itemsize and byte offsets of the fields are determined automatically, and the field names are given the default names `f0`, `f1`, etc.
    
    \>>> np.dtype('i8, f4, S3')
    dtype(\[('f0', '<i8'), ('f1', '<f4'), ('f2', 'S3')\])
    \>>> np.dtype('3int8, float32, (2, 3)float64')
    dtype(\[('f0', 'i1', (3,)), ('f1', '<f4'), ('f2', '<f8', (2, 3))\])
    
    Copy to clipboard
    
3.  A dictionary of field parameter arrays
    
    This is the most flexible form of specification since it allows control over the byte-offsets of the fields and the itemsize of the structure.
    
    The dictionary has two required keys, ‘names’ and ‘formats’, and four optional keys, ‘offsets’, ‘itemsize’, ‘aligned’ and ‘titles’. The values for ‘names’ and ‘formats’ should respectively be a list of field names and a list of dtype specifications, of the same length. The optional ‘offsets’ value should be a list of integer byte-offsets, one for each field within the structure. If ‘offsets’ is not given the offsets are determined automatically. The optional ‘itemsize’ value should be an integer describing the total size in bytes of the dtype, which must be large enough to contain all the fields.
    
    \>>> np.dtype({'names': \['col1', 'col2'\], 'formats': \['i4', 'f4'\]})
    dtype(\[('col1', '<i4'), ('col2', '<f4')\])
    \>>> np.dtype({'names': \['col1', 'col2'\],
    ...           'formats': \['i4', 'f4'\],
    ...           'offsets': \[0, 4\],
    ...           'itemsize': 12})
    dtype({'names': \['col1', 'col2'\], 'formats': \['<i4', '<f4'\], 'offsets': \[0, 4\], 'itemsize': 12})
    
    Copy to clipboard
    
    Offsets may be chosen such that the fields overlap, though this will mean that assigning to one field may clobber any overlapping field’s data. As an exception, fields of [`numpy.object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_")
     type cannot overlap with other fields, because of the risk of clobbering the internal object pointer and then dereferencing it.
    
    The optional ‘aligned’ value can be set to `True` to make the automatic offset computation use aligned offsets (see [Automatic byte offsets and alignment](https://numpy.org/doc/stable/user/basics.rec.html#offsets-and-alignment)
    ), as if the ‘align’ keyword argument of [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
     had been set to True.
    
    The optional ‘titles’ value should be a list of titles of the same length as ‘names’, see [Field Titles](https://numpy.org/doc/stable/user/basics.rec.html#titles)
     below.
    
4.  A dictionary of field names
    
    The keys of the dictionary are the field names and the values are tuples specifying type and offset:
    
    \>>> np.dtype({'col1': ('i1', 0), 'col2': ('f4', 1)})
    dtype(\[('col1', 'i1'), ('col2', '<f4')\])
    
    Copy to clipboard
    
    This form was discouraged because Python dictionaries did not preserve order in Python versions before Python 3.6. [Field Titles](https://numpy.org/doc/stable/user/basics.rec.html#titles)
     may be specified by using a 3-tuple, see below.
    

### Manipulating and displaying structured datatypes[#](https://numpy.org/doc/stable/user/basics.rec.html#manipulating-and-displaying-structured-datatypes "Link to this heading")

The list of field names of a structured datatype can be found in the `names` attribute of the dtype object:

\>>> d \= np.dtype(\[('x', 'i8'), ('y', 'f4')\])
\>>> d.names
('x', 'y')

Copy to clipboard

The dtype of each individual field can be looked up by name:

\>>> d\['x'\]
dtype('int64')

Copy to clipboard

The field names may be modified by assigning to the `names` attribute using a sequence of strings of the same length.

The dtype object also has a dictionary-like attribute, `fields`, whose keys are the field names (and [Field Titles](https://numpy.org/doc/stable/user/basics.rec.html#titles)
, see below) and whose values are tuples containing the dtype and byte offset of each field.

\>>> d.fields
mappingproxy({'x': (dtype('int64'), 0), 'y': (dtype('float32'), 8)})

Copy to clipboard

Both the `names` and `fields` attributes will equal `None` for unstructured arrays. The recommended way to test if a dtype is structured is with _if dt.names is not None_ rather than _if dt.names_, to account for dtypes with 0 fields.

The string representation of a structured datatype is shown in the “list of tuples” form if possible, otherwise numpy falls back to using the more general dictionary form.

### Automatic byte offsets and alignment[#](https://numpy.org/doc/stable/user/basics.rec.html#automatic-byte-offsets-and-alignment "Link to this heading")

Numpy uses one of two methods to automatically determine the field byte offsets and the overall itemsize of a structured datatype, depending on whether `align=True` was specified as a keyword argument to [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
.

By default (`align=False`), numpy will pack the fields together such that each field starts at the byte offset the previous field ended, and the fields are contiguous in memory.

\>>> def print\_offsets(d):
...     print("offsets:", \[d.fields\[name\]\[1\] for name in d.names\])
...     print("itemsize:", d.itemsize)
\>>> print\_offsets(np.dtype('u1, u1, i4, u1, i8, u2'))
offsets: \[0, 1, 2, 6, 7, 15\]
itemsize: 17

Copy to clipboard

If `align=True` is set, numpy will pad the structure in the same way many C compilers would pad a C-struct. Aligned structures can give a performance improvement in some cases, at the cost of increased datatype size. Padding bytes are inserted between fields such that each field’s byte offset will be a multiple of that field’s alignment, which is usually equal to the field’s size in bytes for simple datatypes, see [`PyArray_Descr.alignment`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.alignment "PyArray_Descr.alignment")
. The structure will also have trailing padding added so that its itemsize is a multiple of the largest field’s alignment.

\>>> print\_offsets(np.dtype('u1, u1, i4, u1, i8, u2', align\=True))
offsets: \[0, 1, 4, 8, 16, 24\]
itemsize: 32

Copy to clipboard

Note that although almost all modern C compilers pad in this way by default, padding in C structs is C-implementation-dependent so this memory layout is not guaranteed to exactly match that of a corresponding struct in a C program. Some work may be needed, either on the numpy side or the C side, to obtain exact correspondence.

If offsets were specified using the optional `offsets` key in the dictionary-based dtype specification, setting `align=True` will check that each field’s offset is a multiple of its size and that the itemsize is a multiple of the largest field size, and raise an exception if not.

If the offsets of the fields and itemsize of a structured array satisfy the alignment conditions, the array will have the `ALIGNED` [`flag`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags "numpy.ndarray.flags")
 set.

A convenience function [`numpy.lib.recfunctions.repack_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields")
 converts an aligned dtype or array to a packed one and vice versa. It takes either a dtype or structured ndarray as an argument, and returns a copy with fields re-packed, with or without padding bytes.

### Field titles[#](https://numpy.org/doc/stable/user/basics.rec.html#field-titles "Link to this heading")

In addition to field names, fields may also have an associated [title](https://numpy.org/doc/stable/glossary.html#term-title)
, an alternate name, which is sometimes used as an additional description or alias for the field. The title may be used to index an array, just like a field name.

To add titles when using the list-of-tuples form of dtype specification, the field name may be specified as a tuple of two strings instead of a single string, which will be the field’s title and field name respectively. For example:

\>>> np.dtype(\[(('my title', 'name'), 'f4')\])
dtype(\[(('my title', 'name'), '<f4')\])

Copy to clipboard

When using the first form of dictionary-based specification, the titles may be supplied as an extra `'titles'` key as described above. When using the second (discouraged) dictionary-based specification, the title can be supplied by providing a 3-element tuple `(datatype, offset, title)` instead of the usual 2-element tuple:

\>>> np.dtype({'name': ('i4', 0, 'my title')})
dtype(\[(('my title', 'name'), '<i4')\])

Copy to clipboard

The `dtype.fields` dictionary will contain titles as keys, if any titles are used. This means effectively that a field with a title will be represented twice in the fields dictionary. The tuple values for these fields will also have a third element, the field title. Because of this, and because the `names` attribute preserves the field order while the `fields` attribute may not, it is recommended to iterate through the fields of a dtype using the `names` attribute of the dtype, which will not list titles, as in:

\>>> for name in d.names:
...     print(d.fields\[name\]\[:2\])
(dtype('int64'), 0)
(dtype('float32'), 8)

Copy to clipboard

### Union types[#](https://numpy.org/doc/stable/user/basics.rec.html#union-types "Link to this heading")

Structured datatypes are implemented in numpy to have base type [`numpy.void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void")
 by default, but it is possible to interpret other numpy types as structured types using the `(base_dtype, dtype)` form of dtype specification described in [Data Type Objects](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing)
. Here, `base_dtype` is the desired underlying dtype, and fields and flags will be copied from `dtype`. This dtype is similar to a ‘union’ in C.

Indexing and assignment to structured arrays[#](https://numpy.org/doc/stable/user/basics.rec.html#indexing-and-assignment-to-structured-arrays "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Assigning data to a structured array[#](https://numpy.org/doc/stable/user/basics.rec.html#assigning-data-to-a-structured-array "Link to this heading")

There are a number of ways to assign values to a structured array: Using python tuples, using scalar values, or using other structured arrays.

#### Assignment from Python Native Types (Tuples)[#](https://numpy.org/doc/stable/user/basics.rec.html#assignment-from-python-native-types-tuples "Link to this heading")

The simplest way to assign values to a structured array is using python tuples. Each assigned value should be a tuple of length equal to the number of fields in the array, and not a list or array as these will trigger numpy’s broadcasting rules. The tuple’s elements are assigned to the successive fields of the array, from left to right:

\>>> x \= np.array(\[(1, 2, 3), (4, 5, 6)\], dtype\='i8, f4, f8')
\>>> x\[1\] \= (7, 8, 9)
\>>> x
array(\[(1, 2., 3.), (7, 8., 9.)\],
     dtype=\[('f0', '<i8'), ('f1', '<f4'), ('f2', '<f8')\])

Copy to clipboard

#### Assignment from Scalars[#](https://numpy.org/doc/stable/user/basics.rec.html#assignment-from-scalars "Link to this heading")

A scalar assigned to a structured element will be assigned to all fields. This happens when a scalar is assigned to a structured array, or when an unstructured array is assigned to a structured array:

\>>> x \= np.zeros(2, dtype\='i8, f4, ?, S1')
\>>> x\[:\] \= 3
\>>> x
array(\[(3, 3., True, b'3'), (3, 3., True, b'3')\],
      dtype=\[('f0', '<i8'), ('f1', '<f4'), ('f2', '?'), ('f3', 'S1')\])
\>>> x\[:\] \= np.arange(2)
\>>> x
array(\[(0, 0., False, b'0'), (1, 1., True, b'1')\],
      dtype=\[('f0', '<i8'), ('f1', '<f4'), ('f2', '?'), ('f3', 'S1')\])

Copy to clipboard

Structured arrays can also be assigned to unstructured arrays, but only if the structured datatype has just a single field:

\>>> twofield \= np.zeros(2, dtype\=\[('A', 'i4'), ('B', 'i4')\])
\>>> onefield \= np.zeros(2, dtype\=\[('A', 'i4')\])
\>>> nostruct \= np.zeros(2, dtype\='i4')
\>>> nostruct\[:\] \= twofield
Traceback (most recent call last):
...
TypeError: Cannot cast array data from dtype(\[('A', '<i4'), ('B', '<i4')\]) to dtype('int32') according to the rule 'unsafe'

Copy to clipboard

#### Assignment from other Structured Arrays[#](https://numpy.org/doc/stable/user/basics.rec.html#assignment-from-other-structured-arrays "Link to this heading")

Assignment between two structured arrays occurs as if the source elements had been converted to tuples and then assigned to the destination elements. That is, the first field of the source array is assigned to the first field of the destination array, and the second field likewise, and so on, regardless of field names. Structured arrays with a different number of fields cannot be assigned to each other. Bytes of the destination structure which are not included in any of the fields are unaffected.

\>>> a \= np.zeros(3, dtype\=\[('a', 'i8'), ('b', 'f4'), ('c', 'S3')\])
\>>> b \= np.ones(3, dtype\=\[('x', 'f4'), ('y', 'S3'), ('z', 'O')\])
\>>> b\[:\] \= a
\>>> b
array(\[(0., b'0.0', b''), (0., b'0.0', b''), (0., b'0.0', b'')\],
      dtype=\[('x', '<f4'), ('y', 'S3'), ('z', 'O')\])

Copy to clipboard

#### Assignment involving subarrays[#](https://numpy.org/doc/stable/user/basics.rec.html#assignment-involving-subarrays "Link to this heading")

When assigning to fields which are subarrays, the assigned value will first be broadcast to the shape of the subarray.

### Indexing structured arrays[#](https://numpy.org/doc/stable/user/basics.rec.html#indexing-structured-arrays "Link to this heading")

#### Accessing Individual Fields[#](https://numpy.org/doc/stable/user/basics.rec.html#accessing-individual-fields "Link to this heading")

Individual fields of a structured array may be accessed and modified by indexing the array with the field name.

\>>> x \= np.array(\[(1, 2), (3, 4)\], dtype\=\[('foo', 'i8'), ('bar', 'f4')\])
\>>> x\['foo'\]
array(\[1, 3\])
\>>> x\['foo'\] \= 10
\>>> x
array(\[(10, 2.), (10, 4.)\],
      dtype=\[('foo', '<i8'), ('bar', '<f4')\])

Copy to clipboard

The resulting array is a view into the original array. It shares the same memory locations and writing to the view will modify the original array.

\>>> y \= x\['bar'\]
\>>> y\[:\] \= 11
\>>> x
array(\[(10, 11.), (10, 11.)\],
      dtype=\[('foo', '<i8'), ('bar', '<f4')\])

Copy to clipboard

This view has the same dtype and itemsize as the indexed field, so it is typically a non-structured array, except in the case of nested structures.

\>>> y.dtype, y.shape, y.strides
(dtype('float32'), (2,), (12,))

Copy to clipboard

If the accessed field is a subarray, the dimensions of the subarray are appended to the shape of the result:

\>>> x \= np.zeros((2, 2), dtype\=\[('a', np.int32), ('b', np.float64, (3, 3))\])
\>>> x\['a'\].shape
(2, 2)
\>>> x\['b'\].shape
(2, 2, 3, 3)

Copy to clipboard

#### Accessing Multiple Fields[#](https://numpy.org/doc/stable/user/basics.rec.html#accessing-multiple-fields "Link to this heading")

One can index and assign to a structured array with a multi-field index, where the index is a list of field names.

Warning

The behavior of multi-field indexes changed from Numpy 1.15 to Numpy 1.16.

The result of indexing with a multi-field index is a view into the original array, as follows:

\>>> a \= np.zeros(3, dtype\=\[('a', 'i4'), ('b', 'i4'), ('c', 'f4')\])
\>>> a\[\['a', 'c'\]\]
array(\[(0, 0.), (0, 0.), (0, 0.)\],
     dtype={'names': \['a', 'c'\], 'formats': \['<i4', '<f4'\], 'offsets': \[0, 8\], 'itemsize': 12})

Copy to clipboard

Assignment to the view modifies the original array. The view’s fields will be in the order they were indexed. Note that unlike for single-field indexing, the dtype of the view has the same itemsize as the original array, and has fields at the same offsets as in the original array, and unindexed fields are merely missing.

Warning

In Numpy 1.15, indexing an array with a multi-field index returned a copy of the result above, but with fields packed together in memory as if passed through [`numpy.lib.recfunctions.repack_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields")
.

The new behavior as of Numpy 1.16 leads to extra “padding” bytes at the location of unindexed fields compared to 1.15. You will need to update any code which depends on the data having a “packed” layout. For instance code such as:

\>>> a\[\['a', 'c'\]\].view('i8')  \# Fails in Numpy 1.16
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: When changing to a smaller dtype, its size must be a divisor of the size of original dtype

Copy to clipboard

will need to be changed. This code has raised a `FutureWarning` since Numpy 1.12, and similar code has raised `FutureWarning` since 1.7.

In 1.16 a number of functions have been introduced in the [`numpy.lib.recfunctions`](https://numpy.org/doc/stable/user/basics.rec.html#module-numpy.lib.recfunctions "numpy.lib.recfunctions")
 module to help users account for this change. These are [`numpy.lib.recfunctions.repack_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields")
. [`numpy.lib.recfunctions.structured_to_unstructured`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.structured_to_unstructured "numpy.lib.recfunctions.structured_to_unstructured")
, [`numpy.lib.recfunctions.unstructured_to_structured`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.unstructured_to_structured "numpy.lib.recfunctions.unstructured_to_structured")
, [`numpy.lib.recfunctions.apply_along_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.apply_along_fields "numpy.lib.recfunctions.apply_along_fields")
, [`numpy.lib.recfunctions.assign_fields_by_name`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.assign_fields_by_name "numpy.lib.recfunctions.assign_fields_by_name")
, and [`numpy.lib.recfunctions.require_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.require_fields "numpy.lib.recfunctions.require_fields")
.

The function [`numpy.lib.recfunctions.repack_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields")
 can always be used to reproduce the old behavior, as it will return a packed copy of the structured array. The code above, for example, can be replaced with:

\>>> from numpy.lib.recfunctions import repack\_fields
\>>> repack\_fields(a\[\['a', 'c'\]\]).view('i8')  \# supported in 1.16
array(\[0, 0, 0\])

Copy to clipboard

Furthermore, numpy now provides a new function [`numpy.lib.recfunctions.structured_to_unstructured`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.structured_to_unstructured "numpy.lib.recfunctions.structured_to_unstructured")
 which is a safer and more efficient alternative for users who wish to convert structured arrays to unstructured arrays, as the view above is often intended to do. This function allows safe conversion to an unstructured type taking into account padding, often avoids a copy, and also casts the datatypes as needed, unlike the view. Code such as:

\>>> b \= np.zeros(3, dtype\=\[('x', 'f4'), ('y', 'f4'), ('z', 'f4')\])
\>>> b\[\['x', 'z'\]\].view('f4')
array(\[0., 0., 0., 0., 0., 0., 0., 0., 0.\], dtype=float32)

Copy to clipboard

can be made safer by replacing with:

\>>> from numpy.lib.recfunctions import structured\_to\_unstructured
\>>> structured\_to\_unstructured(b\[\['x', 'z'\]\])
array(\[\[0., 0.\],\
       \[0., 0.\],\
       \[0., 0.\]\], dtype=float32)

Copy to clipboard

Assignment to an array with a multi-field index modifies the original array:

\>>> a\[\['a', 'c'\]\] \= (2, 3)
\>>> a
array(\[(2, 0, 3.), (2, 0, 3.), (2, 0, 3.)\],
      dtype=\[('a', '<i4'), ('b', '<i4'), ('c', '<f4')\])

Copy to clipboard

This obeys the structured array assignment rules described above. For example, this means that one can swap the values of two fields using appropriate multi-field indexes:

\>>> a\[\['a', 'c'\]\] \= a\[\['c', 'a'\]\]

Copy to clipboard

#### Indexing with an Integer to get a Structured Scalar[#](https://numpy.org/doc/stable/user/basics.rec.html#indexing-with-an-integer-to-get-a-structured-scalar "Link to this heading")

Indexing a single element of a structured array (with an integer index) returns a structured scalar:

\>>> x \= np.array(\[(1, 2., 3.)\], dtype\='i, f, f')
\>>> scalar \= x\[0\]
\>>> scalar
np.void((1, 2.0, 3.0), dtype=\[('f0', '<i4'), ('f1', '<f4'), ('f2', '<f4')\])
\>>> type(scalar)
<class 'numpy.void'>

Copy to clipboard

Unlike other numpy scalars, structured scalars are mutable and act like views into the original array, such that modifying the scalar will modify the original array. Structured scalars also support access and assignment by field name:

\>>> x \= np.array(\[(1, 2), (3, 4)\], dtype\=\[('foo', 'i8'), ('bar', 'f4')\])
\>>> s \= x\[0\]
\>>> s\['bar'\] \= 100
\>>> x
array(\[(1, 100.), (3, 4.)\],
      dtype=\[('foo', '<i8'), ('bar', '<f4')\])

Copy to clipboard

Similarly to tuples, structured scalars can also be indexed with an integer:

\>>> scalar \= np.array(\[(1, 2., 3.)\], dtype\='i, f, f')\[0\]
\>>> scalar\[0\]
np.int32(1)
\>>> scalar\[1\] \= 4

Copy to clipboard

Thus, tuples might be thought of as the native Python equivalent to numpy’s structured types, much like native python integers are the equivalent to numpy’s integer types. Structured scalars may be converted to a tuple by calling [`numpy.ndarray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item")
:

\>>> scalar.item(), type(scalar.item())
((1, 4.0, 3.0), <class 'tuple'>)

Copy to clipboard

### Viewing structured arrays containing objects[#](https://numpy.org/doc/stable/user/basics.rec.html#viewing-structured-arrays-containing-objects "Link to this heading")

In order to prevent clobbering object pointers in fields of [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")
 type, numpy currently does not allow views of structured arrays containing objects.

### Structure comparison and promotion[#](https://numpy.org/doc/stable/user/basics.rec.html#structure-comparison-and-promotion "Link to this heading")

If the dtypes of two void structured arrays are equal, testing the equality of the arrays will result in a boolean array with the dimensions of the original arrays, with elements set to `True` where all fields of the corresponding structures are equal:

\>>> a \= np.array(\[(1, 1), (2, 2)\], dtype\=\[('a', 'i4'), ('b', 'i4')\])
\>>> b \= np.array(\[(1, 1), (2, 3)\], dtype\=\[('a', 'i4'), ('b', 'i4')\])
\>>> a \== b
array(\[True, False\])

Copy to clipboard

NumPy will promote individual field datatypes to perform the comparison. So the following is also valid (note the `'f4'` dtype for the `'a'` field):

\>>> b \= np.array(\[(1.0, 1), (2.5, 2)\], dtype\=\[("a", "f4"), ("b", "i4")\])
\>>> a \== b
array(\[True, False\])

Copy to clipboard

To compare two structured arrays, it must be possible to promote them to a common dtype as returned by [`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
 and [`numpy.promote_types`](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types")
. This enforces that the number of fields, the field names, and the field titles must match precisely. When promotion is not possible, for example due to mismatching field names, NumPy will raise an error. Promotion between two structured dtypes results in a canonical dtype that ensures native byte-order for all fields:

\>>> np.result\_type(np.dtype("i,>i"))
dtype(\[('f0', '<i4'), ('f1', '<i4')\])
\>>> np.result\_type(np.dtype("i,>i"), np.dtype("i,i"))
dtype(\[('f0', '<i4'), ('f1', '<i4')\])

Copy to clipboard

The resulting dtype from promotion is also guaranteed to be packed, meaning that all fields are ordered contiguously and any unnecessary padding is removed:

\>>> dt \= np.dtype("i1,V3,i4,V1")\[\["f0", "f2"\]\]
\>>> dt
dtype({'names': \['f0', 'f2'\], 'formats': \['i1', '<i4'\], 'offsets': \[0, 4\], 'itemsize': 9})
\>>> np.result\_type(dt)
dtype(\[('f0', 'i1'), ('f2', '<i4')\])

Copy to clipboard

Note that the result prints without `offsets` or `itemsize` indicating no additional padding. If a structured dtype is created with `align=True` ensuring that `dtype.isalignedstruct` is true, this property is preserved:

\>>> dt \= np.dtype("i1,V3,i4,V1", align\=True)\[\["f0", "f2"\]\]
\>>> dt
dtype({'names': \['f0', 'f2'\], 'formats': \['i1', '<i4'\], 'offsets': \[0, 4\], 'itemsize': 12}, align=True)

\>>> np.result\_type(dt)
dtype(\[('f0', 'i1'), ('f2', '<i4')\], align=True)
\>>> np.result\_type(dt).isalignedstruct
True

Copy to clipboard

When promoting multiple dtypes, the result is aligned if any of the inputs is:

\>>> np.result\_type(np.dtype("i,i"), np.dtype("i,i", align\=True))
dtype(\[('f0', '<i4'), ('f1', '<i4')\], align=True)

Copy to clipboard

The `<` and `>` operators always return `False` when comparing void structured arrays, and arithmetic and bitwise operations are not supported.

Changed in version 1.23: Before NumPy 1.23, a warning was given and `False` returned when promotion to a common dtype failed. Further, promotion was much more restrictive: It would reject the mixed float/integer comparison example above.

Record arrays[#](https://numpy.org/doc/stable/user/basics.rec.html#record-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------

As an optional convenience numpy provides an ndarray subclass, [`numpy.recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 that allows access to fields of structured arrays by attribute instead of only by index. Record arrays use a special datatype, [`numpy.record`](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "numpy.record")
, that allows field access by attribute on the structured scalars obtained from the array. The `numpy.rec` module provides functions for creating recarrays from various objects. Additional helper functions for creating and manipulating structured arrays can be found in [`numpy.lib.recfunctions`](https://numpy.org/doc/stable/user/basics.rec.html#module-numpy.lib.recfunctions "numpy.lib.recfunctions")
.

The simplest way to create a record array is with [`numpy.rec.array`](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#numpy.rec.array "numpy.rec.array")
:

\>>> recordarr \= np.rec.array(\[(1, 2., 'Hello'), (2, 3., "World")\],
...                    dtype\=\[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')\])
\>>> recordarr.bar
array(\[2., 3.\], dtype=float32)
\>>> recordarr\[1:2\]
rec.array(\[(2, 3., b'World')\],
      dtype=\[('foo', '<i4'), ('bar', '<f4'), ('baz', 'S10')\])
\>>> recordarr\[1:2\].foo
array(\[2\], dtype=int32)
\>>> recordarr.foo\[1:2\]
array(\[2\], dtype=int32)
\>>> recordarr\[1\].baz
b'World'

Copy to clipboard

[`numpy.rec.array`](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#numpy.rec.array "numpy.rec.array")
 can convert a wide variety of arguments into record arrays, including structured arrays:

\>>> arr \= np.array(\[(1, 2., 'Hello'), (2, 3., "World")\],
...             dtype\=\[('foo', 'i4'), ('bar', 'f4'), ('baz', 'S10')\])
\>>> recordarr \= np.rec.array(arr)

Copy to clipboard

The `numpy.rec` module provides a number of other convenience functions for creating record arrays, see [record array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation-rec)
.

A record array representation of a structured array can be obtained using the appropriate [`view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")
:

\>>> arr \= np.array(\[(1, 2., 'Hello'), (2, 3., "World")\],
...                dtype\=\[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')\])
\>>> recordarr \= arr.view(dtype\=np.dtype((np.record, arr.dtype)),
...                      type\=np.recarray)

Copy to clipboard

For convenience, viewing an ndarray as type [`numpy.recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 will automatically convert to [`numpy.record`](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "numpy.record")
 datatype, so the dtype can be left out of the view:

\>>> recordarr \= arr.view(np.recarray)
\>>> recordarr.dtype
dtype((numpy.record, \[('foo', '<i4'), ('bar', '<f4'), ('baz', 'S10')\]))

Copy to clipboard

To get back to a plain ndarray both the dtype and type must be reset. The following view does so, taking into account the unusual case that the recordarr was not a structured type:

\>>> arr2 \= recordarr.view(recordarr.dtype.fields or recordarr.dtype, np.ndarray)

Copy to clipboard

Record array fields accessed by index or by attribute are returned as a record array if the field has a structured type but as a plain ndarray otherwise.

\>>> recordarr \= np.rec.array(\[('Hello', (1, 2)), ("World", (3, 4))\],
...                 dtype\=\[('foo', 'S6'),('bar', \[('A', int), ('B', int)\])\])
\>>> type(recordarr.foo)
<class 'numpy.ndarray'>
\>>> type(recordarr.bar)
<class 'numpy.rec.recarray'>

Copy to clipboard

Note that if a field has the same name as an ndarray attribute, the ndarray attribute takes precedence. Such fields will be inaccessible by attribute but will still be accessible by index.

### Recarray helper functions[#](https://numpy.org/doc/stable/user/basics.rec.html#module-numpy.lib.recfunctions "Link to this heading")

Collection of utilities to manipulate structured arrays.

Most of these functions were initially implemented by John Hunter for matplotlib. They have been rewritten and extended for convenience.

numpy.lib.recfunctions.append\_fields(_base_, _names_, _data_, _dtypes\=None_, _fill\_value\=\-1_, _usemask\=True_, _asrecarray\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L654-L722)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.append_fields "Link to this definition")

Add new fields to an existing array.

The names of the fields are given with the _names_ arguments, the corresponding values with the _data_ arguments. If a single field is appended, _names_, _data_ and _dtypes_ do not have to be lists but just values.

Parameters:

**base**array

Input array to extend.

**names**string, sequence

String or sequence of strings corresponding to the names of the new fields.

**data**array or sequence of arrays

Array or sequence of arrays storing the fields to add to the base.

**dtypes**sequence of datatypes, optional

Datatype or sequence of datatypes. If None, the datatypes are estimated from the _data_.

**fill\_value**{float}, optional

Filling value used to pad missing data on the shorter arrays.

**usemask**{False, True}, optional

Whether to return a masked array or not.

**asrecarray**{False, True}, optional

Whether to return a recarray (MaskedRecords) or not.

numpy.lib.recfunctions.apply\_along\_fields(_func_, _arr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1185-L1227)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.apply_along_fields "Link to this definition")

Apply function ‘func’ as a reduction across fields of a structured array.

This is similar to [`numpy.apply_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis")
, but treats the fields of a structured array as an extra axis. The fields are all first cast to a common type following the type-promotion rules from [`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
 applied to the field’s dtypes.

Parameters:

**func**function

Function to apply on the “field” dimension. This function must support an _axis_ argument, like [`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
, [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
, etc.

**arr**ndarray

Structured array for which to apply func.

Returns:

**out**ndarray

Result of the reduction operation

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from numpy.lib import recfunctions as rfn
\>>> b \= np.array(\[(1, 2, 5), (4, 5, 7), (7, 8 ,11), (10, 11, 12)\],
...              dtype\=\[('x', 'i4'), ('y', 'f4'), ('z', 'f8')\])
\>>> rfn.apply\_along\_fields(np.mean, b)
array(\[ 2.66666667,  5.33333333,  8.66666667, 11.        \])
\>>> rfn.apply\_along\_fields(np.mean, b\[\['x', 'z'\]\])
array(\[ 3. ,  5.5,  9. , 11. \])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.assign\_fields\_by\_name(_dst_, _src_, _zero\_unassigned\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1232-L1268)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.assign_fields_by_name "Link to this definition")

Assigns values from one structured array to another by field name.

Normally in numpy >= 1.14, assignment of one structured array to another copies fields “by position”, meaning that the first field from the src is copied to the first field of the dst, and so on, regardless of field name.

This function instead copies “by field name”, such that fields in the dst are assigned from the identically named field in the src. This applies recursively for nested structures. This is how structure assignment worked in numpy >= 1.6 to <= 1.13.

Parameters:

**dst**ndarray

**src**ndarray

The source and destination arrays during assignment.

**zero\_unassigned**bool, optional

If True, fields in the dst for which there was no matching field in the src are filled with the value 0 (zero). This was the behavior of numpy <= 1.13. If False, those fields are not modified.

numpy.lib.recfunctions.drop\_fields(_base_, _drop\_names_, _usemask\=True_, _asrecarray\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L504-L563)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.drop_fields "Link to this definition")

Return a new array with fields in _drop\_names_ dropped.

Nested fields are supported.

Parameters:

**base**array

Input array

**drop\_names**string or sequence

String or sequence of strings corresponding to the names of the fields to drop.

**usemask**{False, True}, optional

Whether to return a masked array or not.

**asrecarray**string or sequence, optional

Whether to return a recarray or a mrecarray (_asrecarray=True_) or a plain ndarray or masked array with flexible dtype. The default is False.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> a \= np.array(\[(1, (2, 3.0)), (4, (5, 6.0))\],
...   dtype\=\[('a', np.int64), ('b', \[('ba', np.double), ('bb', np.int64)\])\])
\>>> rfn.drop\_fields(a, 'a')
array(\[((2., 3),), ((5., 6),)\],
      dtype=\[('b', \[('ba', '<f8'), ('bb', '<i8')\])\])
\>>> rfn.drop\_fields(a, 'ba')
array(\[(1, (3,)), (4, (6,))\], dtype=\[('a', '<i8'), ('b', \[('bb', '<i8')\])\])
\>>> rfn.drop\_fields(a, \['ba', 'bb'\])
array(\[(1,), (4,)\], dtype=\[('a', '<i8')\])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.find\_duplicates(_a_, _key\=None_, _ignoremask\=True_, _return\_index\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1416-L1472)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.find_duplicates "Link to this definition")

Find the duplicates in a structured array along a given key

Parameters:

**a**array-like

Input array

**key**{string, None}, optional

Name of the fields along which to check the duplicates. If None, the search is performed by records

**ignoremask**{True, False}, optional

Whether masked data should be discarded or considered as duplicates.

**return\_index**{False, True}, optional

Whether to return the indices of the duplicated values.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> ndtype \= \[('a', int)\]
\>>> a \= np.ma.array(\[1, 1, 1, 2, 2, 3, 3\],
...         mask\=\[0, 0, 1, 0, 0, 0, 1\]).view(ndtype)
\>>> rfn.find\_duplicates(a, ignoremask\=True, return\_index\=True)
(masked\_array(data=\[(1,), (1,), (2,), (2,)\],
             mask=\[(False,), (False,), (False,), (False,)\],
       fill\_value=(999999,),
            dtype=\[('a', '<i8')\]), array(\[0, 1, 3, 4\]))

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.flatten\_descr(_ndtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L169-L193)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.flatten_descr "Link to this definition")

Flatten a structured data-type description.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> ndtype \= np.dtype(\[('a', '<i4'), ('b', \[('ba', '<f8'), ('bb', '<i4')\])\])
\>>> rfn.flatten\_descr(ndtype)
(('a', dtype('int32')), ('ba', dtype('float64')), ('bb', dtype('int32')))

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.get\_fieldstructure(_adtype_, _lastname\=None_, _parents\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L226-L271)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.get_fieldstructure "Link to this definition")

Returns a dictionary with fields indexing lists of their parent fields.

This function is used to simplify access to fields nested in other fields.

Parameters:

**adtype**np.dtype

Input datatype

**lastname**optional

Last processed field name (used internally during recursion).

**parents**dictionary

Dictionary of parent fields (used internally during recursion).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> ndtype \=  np.dtype(\[('A', int),\
...                     ('B', \[('BA', int),\
...                            ('BB', \[('BBA', int), ('BBB', int)\])\])\])
\>>> rfn.get\_fieldstructure(ndtype)
... \# XXX: possible regression, order of BBA and BBB is swapped
{'A': \[\], 'B': \[\], 'BA': \['B'\], 'BB': \['B'\], 'BBA': \['B', 'BB'\], 'BBB': \['B', 'BB'\]}

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.get\_names(_adtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L103-L133)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.get_names "Link to this definition")

Returns the field names of the input datatype as a tuple. Input datatype must have fields otherwise error is raised.

Parameters:

**adtype**dtype

Input datatype

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> rfn.get\_names(np.empty((1,), dtype\=\[('A', int)\]).dtype)
('A',)
\>>> rfn.get\_names(np.empty((1,), dtype\=\[('A',int), ('B', float)\]).dtype)
('A', 'B')
\>>> adtype \= np.dtype(\[('a', int), ('b', \[('ba', int), ('bb', int)\])\])
\>>> rfn.get\_names(adtype)
('a', ('b', ('ba', 'bb')))

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.get\_names\_flat(_adtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L136-L166)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.get_names_flat "Link to this definition")

Returns the field names of the input datatype as a tuple. Input datatype must have fields otherwise error is raised. Nested structure are flattened beforehand.

Parameters:

**adtype**dtype

Input datatype

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> rfn.get\_names\_flat(np.empty((1,), dtype\=\[('A', int)\]).dtype) is None
False
\>>> rfn.get\_names\_flat(np.empty((1,), dtype\=\[('A',int), ('B', str)\]).dtype)
('A', 'B')
\>>> adtype \= np.dtype(\[('a', int), ('b', \[('ba', int), ('bb', int)\])\])
\>>> rfn.get\_names\_flat(adtype)
('a', 'b', 'ba', 'bb')

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.join\_by(_key_, _r1_, _r2_, _jointype\='inner'_, _r1postfix\='1'_, _r2postfix\='2'_, _defaults\=None_, _usemask\=True_, _asrecarray\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1481-L1656)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.join_by "Link to this definition")

Join arrays _r1_ and _r2_ on key _key_.

The key should be either a string or a sequence of string corresponding to the fields used to join the array. An exception is raised if the _key_ field cannot be found in the two input arrays. Neither _r1_ nor _r2_ should have any duplicates along _key_: the presence of duplicates will make the output quite unreliable. Note that duplicates are not looked for by the algorithm.

Parameters:

**key**{string, sequence}

A string or a sequence of strings corresponding to the fields used for comparison.

**r1, r2**arrays

Structured arrays.

**jointype**{‘inner’, ‘outer’, ‘leftouter’}, optional

If ‘inner’, returns the elements common to both r1 and r2. If ‘outer’, returns the common elements as well as the elements of r1 not in r2 and the elements of not in r2. If ‘leftouter’, returns the common elements and the elements of r1 not in r2.

**r1postfix**string, optional

String appended to the names of the fields of r1 that are present in r2 but absent of the key.

**r2postfix**string, optional

String appended to the names of the fields of r2 that are present in r1 but absent of the key.

**defaults**{dictionary}, optional

Dictionary mapping field names to the corresponding default values.

**usemask**{True, False}, optional

Whether to return a MaskedArray (or MaskedRecords is _asrecarray==True_) or an ndarray.

**asrecarray**{False, True}, optional

Whether to return a recarray (or MaskedRecords if _usemask==True_) or just a flexible-type ndarray.

Notes

*   The output is sorted along the key.
    
*   A temporary array is formed by dropping the fields not in the key for the two arrays and concatenating the result. This array is then sorted, and the common entries selected. The output is constructed by filling the fields with the selected entries. Matching is not preserved if there are some duplicates…
    

numpy.lib.recfunctions.merge\_arrays(_seqarrays_, _fill\_value\=\-1_, _flatten\=False_, _usemask\=False_, _asrecarray\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L363-L497)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.merge_arrays "Link to this definition")

Merge arrays field by field.

Parameters:

**seqarrays**sequence of ndarrays

Sequence of arrays

**fill\_value**{float}, optional

Filling value used to pad missing data on the shorter arrays.

**flatten**{False, True}, optional

Whether to collapse nested fields.

**usemask**{False, True}, optional

Whether to return a masked array or not.

**asrecarray**{False, True}, optional

Whether to return a recarray (MaskedRecords) or not.

Notes

*   Without a mask, the missing value will be filled with something, depending on what its corresponding type:
    
    *   `-1` for integers
        
    *   `-1.0` for floating point numbers
        
    *   `'-'` for characters
        
    *   `'-1'` for strings
        
    *   `True` for boolean values
        
*   XXX: I just obtained these values empirically
    

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> rfn.merge\_arrays((np.array(\[1, 2\]), np.array(\[10., 20., 30.\])))
array(\[( 1, 10.), ( 2, 20.), (-1, 30.)\],
      dtype=\[('f0', '<i8'), ('f1', '<f8')\])

Copy to clipboard

\>>> rfn.merge\_arrays((np.array(\[1, 2\], dtype\=np.int64),
...         np.array(\[10., 20., 30.\])), usemask\=False)
 array(\[(1, 10.0), (2, 20.0), (-1, 30.0)\],
         dtype=\[('f0', '<i8'), ('f1', '<f8')\])
\>>> rfn.merge\_arrays((np.array(\[1, 2\]).view(\[('a', np.int64)\]),
...               np.array(\[10., 20., 30.\])),
...              usemask\=False, asrecarray\=True)
rec.array(\[( 1, 10.), ( 2, 20.), (-1, 30.)\],
          dtype=\[('a', '<i8'), ('f1', '<f8')\])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.rec\_append\_fields(_base_, _names_, _data_, _dtypes\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L730-L762)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.rec_append_fields "Link to this definition")

Add new fields to an existing array.

The names of the fields are given with the _names_ arguments, the corresponding values with the _data_ arguments. If a single field is appended, _names_, _data_ and _dtypes_ do not have to be lists but just values.

Parameters:

**base**array

Input array to extend.

**names**string, sequence

String or sequence of strings corresponding to the names of the new fields.

**data**array or sequence of arrays

Array or sequence of arrays storing the fields to add to the base.

**dtypes**sequence of datatypes, optional

Datatype or sequence of datatypes. If None, the datatypes are estimated from the _data_.

Returns:

**appended\_array**np.recarray

See also

[`append_fields`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.append_fields "numpy.lib.recfunctions.append_fields")

numpy.lib.recfunctions.rec\_drop\_fields(_base_, _drop\_names_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L595-L600)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.rec_drop_fields "Link to this definition")

Returns a new numpy.recarray with fields in _drop\_names_ dropped.

numpy.lib.recfunctions.rec\_join(_key_, _r1_, _r2_, _jointype\='inner'_, _r1postfix\='1'_, _r2postfix\='2'_, _defaults\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1665-L1678)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.rec_join "Link to this definition")

Join arrays _r1_ and _r2_ on keys. Alternative to join\_by, that always returns a np.recarray.

See also

[`join_by`](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.join_by "numpy.lib.recfunctions.join_by")

equivalent function

numpy.lib.recfunctions.recursive\_fill\_fields(_input_, _output_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L31-L68)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.recursive_fill_fields "Link to this definition")

Fills fields from output with fields from input, with support for nested structures.

Parameters:

**input**ndarray

Input array.

**output**ndarray

Output array.

Notes

*   _output_ should be at least the same size as _input_
    

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> a \= np.array(\[(1, 10.), (2, 20.)\], dtype\=\[('A', np.int64), ('B', np.float64)\])
\>>> b \= np.zeros((3,), dtype\=a.dtype)
\>>> rfn.recursive\_fill\_fields(a, b)
array(\[(1, 10.), (2, 20.), (0,  0.)\], dtype=\[('A', '<i8'), ('B', '<f8')\])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.rename\_fields(_base_, _namemapper_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L607-L645)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.rename_fields "Link to this definition")

Rename the fields from a flexible-datatype ndarray or recarray.

Nested fields are supported.

Parameters:

**base**ndarray

Input array whose fields must be modified.

**namemapper**dictionary

Dictionary mapping old field names to their new version.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> a \= np.array(\[(1, (2, \[3.0, 30.\])), (4, (5, \[6.0, 60.\]))\],
...   dtype\=\[('a', int),('b', \[('ba', float), ('bb', (float, 2))\])\])
\>>> rfn.rename\_fields(a, {'a':'A', 'bb':'BB'})
array(\[(1, (2., \[ 3., 30.\])), (4, (5., \[ 6., 60.\]))\],
      dtype=\[('A', '<i8'), ('b', \[('ba', '<f8'), ('BB', '<f8', (2,))\])\])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.repack\_fields(_a_, _align\=False_, _recurse\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L769-L851)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.repack_fields "Link to this definition")

Re-pack the fields of a structured array or dtype in memory.

The memory layout of structured datatypes allows fields at arbitrary byte offsets. This means the fields can be separated by padding bytes, their offsets can be non-monotonically increasing, and they can overlap.

This method removes any overlaps and reorders the fields in memory so they have increasing byte offsets, and adds or removes padding bytes depending on the _align_ option, which behaves like the _align_ option to [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
.

If _align=False_, this method produces a “packed” memory layout in which each field starts at the byte the previous field ended, and any padding bytes are removed.

If _align=True_, this methods produces an “aligned” memory layout in which each field’s offset is a multiple of its alignment, and the total itemsize is a multiple of the largest alignment, by adding padding bytes as needed.

Parameters:

**a**ndarray or dtype

array or dtype for which to repack the fields.

**align**boolean

If true, use an “aligned” memory layout, otherwise use a “packed” layout.

**recurse**boolean

If True, also repack nested structures.

Returns:

**repacked**ndarray or dtype

Copy of _a_ with fields repacked, or _a_ itself if no repacking was needed.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from numpy.lib import recfunctions as rfn
\>>> def print\_offsets(d):
...     print("offsets:", \[d.fields\[name\]\[1\] for name in d.names\])
...     print("itemsize:", d.itemsize)
...
\>>> dt \= np.dtype('u1, <i8, <f8', align\=True)
\>>> dt
dtype({'names': \['f0', 'f1', 'f2'\], 'formats': \['u1', '<i8', '<f8'\], 'offsets': \[0, 8, 16\], 'itemsize': 24}, align=True)
\>>> print\_offsets(dt)
offsets: \[0, 8, 16\]
itemsize: 24
\>>> packed\_dt \= rfn.repack\_fields(dt)
\>>> packed\_dt
dtype(\[('f0', 'u1'), ('f1', '<i8'), ('f2', '<f8')\])
\>>> print\_offsets(packed\_dt)
offsets: \[0, 1, 9\]
itemsize: 17

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.require\_fields(_array_, _required\_dtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1273-L1315)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.require_fields "Link to this definition")

Casts a structured array to a new dtype using assignment by field-name.

This function assigns from the old to the new array by name, so the value of a field in the output array is the value of the field with the same name in the source array. This has the effect of creating a new ndarray containing only the fields “required” by the required\_dtype.

If a field name in the required\_dtype does not exist in the input array, that field is created and set to 0 in the output array.

Parameters:

**a**ndarray

array to cast

**required\_dtype**dtype

datatype for output array

Returns:

**out**ndarray

array with the new dtype, with field values copied from the fields in the input array with the same name

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from numpy.lib import recfunctions as rfn
\>>> a \= np.ones(4, dtype\=\[('a', 'i4'), ('b', 'f8'), ('c', 'u1')\])
\>>> rfn.require\_fields(a, \[('b', 'f4'), ('c', 'u1')\])
array(\[(1., 1), (1., 1), (1., 1), (1., 1)\],
  dtype=\[('b', '<f4'), ('c', 'u1')\])
\>>> rfn.require\_fields(a, \[('b', 'f4'), ('newf', 'u1')\])
array(\[(1., 0), (1., 0), (1., 0), (1., 0)\],
  dtype=\[('b', '<f4'), ('newf', 'u1')\])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.stack\_arrays(_arrays_, _defaults\=None_, _usemask\=True_, _asrecarray\=False_, _autoconvert\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1323-L1408)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.stack_arrays "Link to this definition")

Superposes arrays fields by fields

Parameters:

**arrays**array or sequence

Sequence of input arrays.

**defaults**dictionary, optional

Dictionary mapping field names to the corresponding default values.

**usemask**{True, False}, optional

Whether to return a MaskedArray (or MaskedRecords is _asrecarray==True_) or an ndarray.

**asrecarray**{False, True}, optional

Whether to return a recarray (or MaskedRecords if _usemask==True_) or just a flexible-type ndarray.

**autoconvert**{False, True}, optional

Whether automatically cast the type of the field to the maximum.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib import recfunctions as rfn
\>>> x \= np.array(\[1, 2,\])
\>>> rfn.stack\_arrays(x) is x
True
\>>> z \= np.array(\[('A', 1), ('B', 2)\], dtype\=\[('A', '|S3'), ('B', float)\])
\>>> zz \= np.array(\[('a', 10., 100.), ('b', 20., 200.), ('c', 30., 300.)\],
...   dtype\=\[('A', '|S3'), ('B', np.double), ('C', np.double)\])
\>>> test \= rfn.stack\_arrays((z,zz))
\>>> test
masked\_array(data=\[(b'A', 1.0, --), (b'B', 2.0, --), (b'a', 10.0, 100.0),\
                   (b'b', 20.0, 200.0), (b'c', 30.0, 300.0)\],
             mask=\[(False, False,  True), (False, False,  True),\
                   (False, False, False), (False, False, False),\
                   (False, False, False)\],
       fill\_value=(b'N/A', 1e+20, 1e+20),
            dtype=\[('A', 'S3'), ('B', '<f8'), ('C', '<f8')\])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.structured\_to\_unstructured(_arr_, _dtype\=None_, _copy\=False_, _casting\='unsafe'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L939-L1067)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.structured_to_unstructured "Link to this definition")

Converts an n-D structured array into an (n+1)-D unstructured array.

The new array will have a new last dimension equal in size to the number of field-elements of the input array. If not supplied, the output datatype is determined from the numpy type promotion rules applied to all the field datatypes.

Nested fields, as well as each element of any subarray fields, all count as a single field-elements.

Parameters:

**arr**ndarray

Structured array or dtype to convert. Cannot contain object datatype.

**dtype**dtype, optional

The dtype of the output unstructured array.

**copy**bool, optional

If true, always return a copy. If false, a view is returned if possible, such as when the _dtype_ and strides of the fields are suitable and the array subtype is one of [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [`numpy.recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 or [`numpy.memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")
.

Changed in version 1.25.0: A view can now be returned if the fields are separated by a uniform stride.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

See casting argument of [`numpy.ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")
. Controls what kind of data casting may occur.

Returns:

**unstructured**ndarray

Unstructured array with one more dimension.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from numpy.lib import recfunctions as rfn
\>>> a \= np.zeros(4, dtype\=\[('a', 'i4'), ('b', 'f4,u2'), ('c', 'f4', 2)\])
\>>> a
array(\[(0, (0., 0), \[0., 0.\]), (0, (0., 0), \[0., 0.\]),\
       (0, (0., 0), \[0., 0.\]), (0, (0., 0), \[0., 0.\])\],
      dtype=\[('a', '<i4'), ('b', \[('f0', '<f4'), ('f1', '<u2')\]), ('c', '<f4', (2,))\])
\>>> rfn.structured\_to\_unstructured(a)
array(\[\[0., 0., 0., 0., 0.\],\
       \[0., 0., 0., 0., 0.\],\
       \[0., 0., 0., 0., 0.\],\
       \[0., 0., 0., 0., 0.\]\])

Copy to clipboard

\>>> b \= np.array(\[(1, 2, 5), (4, 5, 7), (7, 8 ,11), (10, 11, 12)\],
...              dtype\=\[('x', 'i4'), ('y', 'f4'), ('z', 'f8')\])
\>>> np.mean(rfn.structured\_to\_unstructured(b\[\['x', 'z'\]\]), axis\=-1)
array(\[ 3. ,  5.5,  9. , 11. \])

Copy to clipboard

Go BackOpen In Tab

numpy.lib.recfunctions.unstructured\_to\_structured(_arr_, _dtype\=None_, _names\=None_, _align\=False_, _copy\=False_, _casting\='unsafe'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/recfunctions.py#L1074-L1180)
[#](https://numpy.org/doc/stable/user/basics.rec.html#numpy.lib.recfunctions.unstructured_to_structured "Link to this definition")

Converts an n-D unstructured array into an (n-1)-D structured array.

The last dimension of the input array is converted into a structure, with number of field-elements equal to the size of the last dimension of the input array. By default all output fields have the input array’s dtype, but an output structured dtype with an equal number of fields-elements can be supplied instead.

Nested fields, as well as each element of any subarray fields, all count towards the number of field-elements.

Parameters:

**arr**ndarray

Unstructured array or dtype to convert.

**dtype**dtype, optional

The structured dtype of the output array

**names**list of strings, optional

If dtype is not supplied, this specifies the field names for the output dtype, in order. The field dtypes will be the same as the input array.

**align**boolean, optional

Whether to create an aligned memory layout.

**copy**bool, optional

See copy argument to [`numpy.ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")
. If true, always return a copy. If false, and _dtype_ requirements are satisfied, a view is returned.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

See casting argument of [`numpy.ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")
. Controls what kind of data casting may occur.

Returns:

**structured**ndarray

Structured array with fewer dimensions.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from numpy.lib import recfunctions as rfn
\>>> dt \= np.dtype(\[('a', 'i4'), ('b', 'f4,u2'), ('c', 'f4', 2)\])
\>>> a \= np.arange(20).reshape((4,5))
\>>> a
array(\[\[ 0,  1,  2,  3,  4\],\
       \[ 5,  6,  7,  8,  9\],\
       \[10, 11, 12, 13, 14\],\
       \[15, 16, 17, 18, 19\]\])
\>>> rfn.unstructured\_to\_structured(a, dt)
array(\[( 0, ( 1.,  2), \[ 3.,  4.\]), ( 5, ( 6.,  7), \[ 8.,  9.\]),\
       (10, (11., 12), \[13., 14.\]), (15, (16., 17), \[18., 19.\])\],
      dtype=\[('a', '<i4'), ('b', \[('f0', '<f4'), ('f1', '<u2')\]), ('c', '<f4', (2,))\])

Copy to clipboard

Go BackOpen In Tab

On this page