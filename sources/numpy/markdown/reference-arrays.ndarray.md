[Skip to main content](https://numpy.org/doc/stable/reference/arrays.ndarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.ndarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.ndarray.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.ndarray.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.ndarray.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.ndarray.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.ndarray.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.ndarray.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.ndarray.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.ndarray.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.ndarray.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.ndarray.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.ndarray.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.ndarray.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.ndarray.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.ndarray.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.ndarray.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.ndarray.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.ndarray.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.ndarray.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.ndarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

The N-dimensional array ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#the-n-dimensional-array-ndarray "Link to this heading")

================================================================================================================================================================================================================================================================

An [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 is a (usually fixed-size) multidimensional container of items of the same type and size. The number of dimensions and items in an array is defined by its [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")
, which is a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
 of _N_ non-negative integers that specify the sizes of each dimension. The type of items in the array is specified by a separate [data-type object (dtype)](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
, one of which is associated with each ndarray.

As with other container objects in Python, the contents of an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 can be accessed and modified by [indexing or slicing](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
 the array (using, for example, _N_ integers), and via the methods and attributes of the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

Different [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 can share the same data, so that changes made in one [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 may be visible in another. That is, an ndarray can be a _“view”_ to another ndarray, and the data it is referring to is taken care of by the _“base”_ ndarray. ndarrays can also be views to memory owned by Python [`strings`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or objects implementing the [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)")
 or [array](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)
 interfaces.

Example

Try it in your browser!

A 2-dimensional array of size 2 x 3, composed of 4-byte integer elements:

\>>> import numpy as np

Copy to clipboard

\>>> x \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\], np.int32)
\>>> type(x)
<class 'numpy.ndarray'>
\>>> x.shape
(2, 3)
\>>> x.dtype
dtype('int32')

Copy to clipboard

The array can be indexed using Python container-like syntax:

\>>> \# The element of x in the \*second\* row, \*third\* column, namely, 6.
\>>> x\[1, 2\]
   6

Copy to clipboard

For example [slicing](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
 can produce views of the array:

\>>> y \= x\[:,1\]
\>>> y
array(\[2, 5\], dtype=int32)
\>>> y\[0\] \= 9 \# this also changes the corresponding element in x
\>>> y
array(\[9, 5\], dtype=int32)
\>>> x
array(\[\[1, 9, 3\],\
       \[4, 5, 6\]\], dtype=int32)

Copy to clipboard

Go BackOpen In Tab

Constructing arrays[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#constructing-arrays "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

New arrays can be constructed using the routines detailed in [Array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation)
, and also by using the low-level [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 constructor:

|     |     |
| --- | --- |
| [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")<br>(shape\[, dtype, buffer, offset, ...\]) | An array object represents a multidimensional, homogeneous array of fixed-size items. |

Indexing arrays[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#indexing-arrays "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Arrays can be indexed using an extended Python slicing syntax, `array[selection]`. Similar syntax is also used for accessing fields in a [structured data type](https://numpy.org/doc/stable/glossary.html#term-structured-data-type)
.

See also

[Array Indexing](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
.

Internal memory layout of an ndarray[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#internal-memory-layout-of-an-ndarray "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

An instance of class [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 consists of a contiguous one-dimensional segment of computer memory (owned by the array, or by some other object), combined with an indexing scheme that maps _N_ integers into the location of an item in the block. The ranges in which the indices can vary is specified by the [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")
 of the array. How many bytes each item takes and how the bytes are interpreted is defined by the [data-type object](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
 associated with the array.

A segment of memory is inherently 1-dimensional, and there are many different schemes for arranging the items of an _N_\-dimensional array in a 1-dimensional block. NumPy is flexible, and [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 objects can accommodate any _strided indexing scheme_. In a strided scheme, the N-dimensional index \\((n\_0, n\_1, ..., n\_{N-1})\\) corresponds to the offset (in bytes):

\\\[n\_{\\mathrm{offset}} = \\sum\_{k=0}^{N-1} s\_k n\_k\\\]

from the beginning of the memory block associated with the array. Here, \\(s\_k\\) are integers which specify the [`strides`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides "numpy.ndarray.strides")
 of the array. The [column-major](https://numpy.org/doc/stable/glossary.html#term-column-major)
 order (used, for example, in the Fortran language and in _Matlab_) and [row-major](https://numpy.org/doc/stable/glossary.html#term-row-major)
 order (used in C) schemes are just specific kinds of strided scheme, and correspond to memory that can be _addressed_ by the strides:

\\\[s\_k^{\\mathrm{column}} = \\mathrm{itemsize} \\prod\_{j=0}^{k-1} d\_j , \\quad s\_k^{\\mathrm{row}} = \\mathrm{itemsize} \\prod\_{j=k+1}^{N-1} d\_j .\\\]

where \\(d\_j\\) _\= self.shape\[j\]_.

Both the C and Fortran orders are [contiguous](https://numpy.org/doc/stable/glossary.html#term-contiguous)
, _i.e.,_ single-segment, memory layouts, in which every part of the memory block can be accessed by some combination of the indices.

Note

_Contiguous arrays_ and _single-segment arrays_ are synonymous and are used interchangeably throughout the documentation.

While a C-style and Fortran-style contiguous array, which has the corresponding flags set, can be addressed with the above strides, the actual strides may be different. This can happen in two cases:

1.  If `self.shape[k] == 1` then for any legal index `index[k] == 0`. This means that in the formula for the offset \\(n\_k = 0\\) and thus \\(s\_k n\_k = 0\\) and the value of \\(s\_k\\) _\= self.strides\[k\]_ is arbitrary.
    
2.  If an array has no elements (`self.size == 0`) there is no legal index and the strides are never used. Any array with no elements may be considered C-style and Fortran-style contiguous.
    

Point 1. means that `self` and `self.squeeze()` always have the same contiguity and `aligned` flags value. This also means that even a high dimensional array could be C-style and Fortran-style contiguous at the same time.

An array is considered aligned if the memory offsets for all elements and the base offset itself is a multiple of [`self.itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.itemsize.html#numpy.ndarray.itemsize "numpy.ndarray.itemsize")
. Understanding _memory-alignment_ leads to better performance on most hardware.

Warning

It does _not_ generally hold that `self.strides[-1] == self.itemsize` for C-style contiguous arrays or `self.strides[0] == self.itemsize` for Fortran-style contiguous arrays is true.

Data in new [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 is in the [row-major](https://numpy.org/doc/stable/glossary.html#term-row-major)
 (C) order, unless otherwise specified, but, for example, [basic array slicing](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
 often produces [views](https://numpy.org/doc/stable/glossary.html#term-view)
 in a different scheme.

Note

Several algorithms in NumPy work on arbitrarily strided arrays. However, some algorithms require single-segment arrays. When an irregularly strided array is passed in to such algorithms, a copy is automatically made.

Array attributes[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Array attributes reflect information that is intrinsic to the array itself. Generally, accessing an array through its attributes allows you to get and sometimes set intrinsic properties of the array without creating a new array. The exposed attributes are the core parts of an array and only some of them can be reset meaningfully without creating a new array. Information on each attribute is given below.

### Memory layout[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#id1 "Link to this heading")

The following attributes contain information about the memory layout of the array:

|     |     |
| --- | --- |
| [`ndarray.flags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags "numpy.ndarray.flags") | Information about the memory layout of the array. |
| [`ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape") | Tuple of array dimensions. |
| [`ndarray.strides`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides "numpy.ndarray.strides") | Tuple of bytes to step in each dimension when traversing an array. |
| [`ndarray.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html#numpy.ndarray.ndim "numpy.ndarray.ndim") | Number of array dimensions. |
| [`ndarray.data`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.data.html#numpy.ndarray.data "numpy.ndarray.data") | Python buffer object pointing to the start of the array's data. |
| [`ndarray.size`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html#numpy.ndarray.size "numpy.ndarray.size") | Number of elements in the array. |
| [`ndarray.itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.itemsize.html#numpy.ndarray.itemsize "numpy.ndarray.itemsize") | Length of one array element in bytes. |
| [`ndarray.nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nbytes.html#numpy.ndarray.nbytes "numpy.ndarray.nbytes") | Total bytes consumed by the elements of the array. |
| [`ndarray.base`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base") | Base object if memory is from some other object. |

### Data type[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#data-type "Link to this heading")

See also

[Data type objects](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)

The data type object associated with the array can be found in the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html#numpy.ndarray.dtype "numpy.ndarray.dtype")
 attribute:

|     |     |
| --- | --- |
| [`ndarray.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html#numpy.ndarray.dtype "numpy.ndarray.dtype") | Data-type of the array's elements. |

### Other attributes[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#other-attributes "Link to this heading")

|     |     |
| --- | --- |
| [`ndarray.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T "numpy.ndarray.T") | View of the transposed array. |
| [`ndarray.real`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.real.html#numpy.ndarray.real "numpy.ndarray.real") | The real part of the array. |
| [`ndarray.imag`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.imag.html#numpy.ndarray.imag "numpy.ndarray.imag") | The imaginary part of the array. |
| [`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat") | A 1-D iterator over the array. |

### Array interface[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-interface "Link to this heading")

See also

[The array interface protocol](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)
.

|     |     |
| --- | --- |
| [`__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "object.__array_interface__") | Python-side of the array interface |
| [`__array_struct__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "object.__array_struct__") | C-side of the array interface |

### [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.14)")
 foreign function interface[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#ctypes-foreign-function-interface "Link to this heading")

|     |     |
| --- | --- |
| [`ndarray.ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ctypes.html#numpy.ndarray.ctypes "numpy.ndarray.ctypes") | An object to simplify the interaction of the array with the ctypes module. |

Array methods[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-methods "Link to this heading")

------------------------------------------------------------------------------------------------------------------

An [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 object has many methods which operate on or with the array in some fashion, typically returning an array result. These methods are briefly explained below. (Each method’s docstring has a more complete description.)

For the following methods there are also corresponding functions in [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
: [`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
, [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
, [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")
, [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")
, [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")
, [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
, [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")
, [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
, [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")
, [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
, [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod")
, [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
, [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")
, [`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")
, [`max`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")
, [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
, [`min`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")
, [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
, [`partition`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition "numpy.partition")
, [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
, [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put")
, [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
, [`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")
, [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
, [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
, [`round`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")
, [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
, [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
, [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")
, [`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
, [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
, [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes "numpy.swapaxes")
, [`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")
, [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")
, [`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
.

### Array conversion[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-conversion "Link to this heading")

|     |     |
| --- | --- |
| [`ndarray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item")<br>(\*args) | Copy an element of an array to a standard Python scalar and return it. |
| [`ndarray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist "numpy.ndarray.tolist")<br>() | Return the array as an `a.ndim`\-levels deep nested list of Python scalars. |
| [`ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")<br>(\[order\]) | Construct Python bytes containing the raw data bytes in the array. |
| [`ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |
| [`ndarray.dump`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dump.html#numpy.ndarray.dump "numpy.ndarray.dump")<br>(file) | Dump a pickle of the array to the specified file. |
| [`ndarray.dumps`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dumps.html#numpy.ndarray.dumps "numpy.ndarray.dumps")<br>() | Returns the pickle of the array as a string. |
| [`ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")<br>(dtype\[, order, casting, ...\]) | Copy of the array, cast to a specified type. |
| [`ndarray.byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.byteswap.html#numpy.ndarray.byteswap "numpy.ndarray.byteswap")<br>(\[inplace\]) | Swap the bytes of the array elements |
| [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")<br>(\[order\]) | Return a copy of the array. |
| [`ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")<br>(\[dtype\]\[, type\]) | New view of array with the same data. |
| [`ndarray.getfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.getfield.html#numpy.ndarray.getfield "numpy.ndarray.getfield")<br>(dtype\[, offset\]) | Returns a field of the given array as a certain type. |
| [`ndarray.setflags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setflags.html#numpy.ndarray.setflags "numpy.ndarray.setflags")<br>(\[write, align, uic\]) | Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY, respectively. |
| [`ndarray.fill`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill")<br>(value) | Fill the array with a scalar value. |

### Shape manipulation[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#shape-manipulation "Link to this heading")

For reshape, resize, and transpose, the single tuple argument may be replaced with `n` integers which will be interpreted as an n-tuple.

|     |     |
| --- | --- |
| [`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")<br>(a.reshape) | Returns an array containing the same data with a new shape. |
| [`ndarray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize")<br>(a.resize) | Change shape and size of array in-place. |
| [`ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |
| [`ndarray.swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.swapaxes.html#numpy.ndarray.swapaxes "numpy.ndarray.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |
| [`ndarray.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html#numpy.ndarray.ravel "numpy.ndarray.ravel")<br>(\[order\]) | Return a flattened array. |
| [`ndarray.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.squeeze.html#numpy.ndarray.squeeze "numpy.ndarray.squeeze")<br>(\[axis\]) | Remove axes of length one from _a_. |

### Item selection and manipulation[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#item-selection-and-manipulation "Link to this heading")

For array methods that take an _axis_ keyword, it defaults to _None_. If axis is _None_, then the array is treated as a 1-D array. Any other value for _axis_ represents the dimension along which the operation should proceed.

|     |     |
| --- | --- |
| [`ndarray.take`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "numpy.ndarray.take")<br>(indices\[, axis, out, mode\]) | Return an array formed from the elements of _a_ at the given indices. |
| [`ndarray.put`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.put.html#numpy.ndarray.put "numpy.ndarray.put")<br>(indices, values\[, mode\]) | Set `a.flat[n] = values[n]` for all `n` in indices. |
| [`ndarray.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.repeat.html#numpy.ndarray.repeat "numpy.ndarray.repeat")<br>(repeats\[, axis\]) | Repeat elements of an array. |
| [`ndarray.choose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.choose.html#numpy.ndarray.choose "numpy.ndarray.choose")<br>(choices\[, out, mode\]) | Use an index array to construct a new array from a set of choices. |
| [`ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")<br>(\[axis, kind, order, stable, ...\]) | Sort an array in-place. |
| [`ndarray.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argsort.html#numpy.ndarray.argsort "numpy.ndarray.argsort")<br>(\[axis, kind, order, stable, ...\]) | Returns the indices that would sort this array. |
| [`ndarray.partition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.partition.html#numpy.ndarray.partition "numpy.ndarray.partition")<br>(kth\[, axis, kind, order\]) | Partially sorts the elements in the array in such a way that the value of the element in k-th position is in the position it would be in a sorted array. |
| [`ndarray.argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argpartition.html#numpy.ndarray.argpartition "numpy.ndarray.argpartition")<br>(kth\[, axis, kind, order\]) | Returns the indices that would partition this array. |
| [`ndarray.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.searchsorted.html#numpy.ndarray.searchsorted "numpy.ndarray.searchsorted")<br>(v\[, side, sorter\]) | Find indices where elements of _v_ should be inserted in _a_ to maintain order. |
| [`ndarray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero")<br>() | Return the indices of the elements that are non-zero. |
| [`ndarray.compress`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.compress.html#numpy.ndarray.compress "numpy.ndarray.compress")<br>(condition\[, axis, out\]) | Return selected slices of this array along given axis. |
| [`ndarray.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.diagonal.html#numpy.ndarray.diagonal "numpy.ndarray.diagonal")<br>(\[offset, axis1, axis2\]) | Return specified diagonals. |

### Calculation[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#calculation "Link to this heading")

Many of these methods take an argument named _axis_. In such cases,

*   If _axis_ is _None_ (the default), the array is treated as a 1-D array and the operation is performed over the entire array. This behavior is also the default if self is a 0-dimensional array or array scalar. (An array scalar is an instance of the types/classes float32, float64, etc., whereas a 0-dimensional array is an ndarray instance containing precisely one array scalar.)
    
*   If _axis_ is an integer, then the operation is done over the given axis (for each 1-D subarray that can be created along the given axis).
    

Example of the _axis_ argument

Try it in your browser!

A 3-dimensional array of size 3 x 3 x 3, summed over each of its three axes:

\>>> import numpy as np

Copy to clipboard

\>>> x \= np.arange(27).reshape((3,3,3))
\>>> x
array(\[\[\[ 0,  1,  2\],\
      \[ 3,  4,  5\],\
      \[ 6,  7,  8\]\],\
      \[\[ 9, 10, 11\],\
      \[12, 13, 14\],\
      \[15, 16, 17\]\],\
      \[\[18, 19, 20\],\
      \[21, 22, 23\],\
      \[24, 25, 26\]\]\])
\>>> x.sum(axis\=0)
array(\[\[27, 30, 33\],\
      \[36, 39, 42\],\
      \[45, 48, 51\]\])
\>>> \# for sum, axis is the first keyword, so we may omit it,
\>>> \# specifying only its value
\>>> x.sum(0), x.sum(1), x.sum(2)
(array(\[\[27, 30, 33\],\
      \[36, 39, 42\],\
      \[45, 48, 51\]\]),
array(\[\[ 9, 12, 15\],\
      \[36, 39, 42\],\
      \[63, 66, 69\]\]),
array(\[\[ 3, 12, 21\],\
      \[30, 39, 48\],\
      \[57, 66, 75\]\]))

Copy to clipboard

Go BackOpen In Tab

The parameter _dtype_ specifies the data type over which a reduction operation (like summing) should take place. The default reduce data type is the same as the data type of _self_. To avoid overflow, it can be useful to perform the reduction using a larger data type.

For several methods, an optional _out_ argument can also be provided and the result will be placed into the output array given. The _out_ argument must be an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 and have the same number of elements. It can have a different data type in which case casting will be performed.

|     |     |
| --- | --- |
| [`ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")<br>(\[axis, out, keepdims, initial, ...\]) | Return the maximum along a given axis. |
| [`ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")<br>(\[axis, out, keepdims\]) | Return indices of the maximum values along the given axis. |
| [`ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")<br>(\[axis, out, keepdims, initial, ...\]) | Return the minimum along a given axis. |
| [`ndarray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "numpy.ndarray.argmin")<br>(\[axis, out, keepdims\]) | Return indices of the minimum values along the given axis. |
| [`ndarray.clip`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.clip.html#numpy.ndarray.clip "numpy.ndarray.clip")<br>(\[min, max, out\]) | Return an array whose values are limited to `[min, max]`. |
| [`ndarray.conj`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conj.html#numpy.ndarray.conj "numpy.ndarray.conj")<br>() | Complex-conjugate all elements. |
| [`ndarray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round "numpy.ndarray.round")<br>(\[decimals, out\]) | Return _a_ with each element rounded to the given number of decimals. |
| [`ndarray.trace`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.trace.html#numpy.ndarray.trace "numpy.ndarray.trace")<br>(\[offset, axis1, axis2, dtype, out\]) | Return the sum along diagonals of the array. |
| [`ndarray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")<br>(\[axis, dtype, out, keepdims, ...\]) | Return the sum of the array elements over the given axis. |
| [`ndarray.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumsum.html#numpy.ndarray.cumsum "numpy.ndarray.cumsum")<br>(\[axis, dtype, out\]) | Return the cumulative sum of the elements along the given axis. |
| [`ndarray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#numpy.ndarray.mean "numpy.ndarray.mean")<br>(\[axis, dtype, out, keepdims, where\]) | Returns the average of the array elements along given axis. |
| [`ndarray.var`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.var.html#numpy.ndarray.var "numpy.ndarray.var")<br>(\[axis, dtype, out, ddof, ...\]) | Returns the variance of the array elements, along given axis. |
| [`ndarray.std`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html#numpy.ndarray.std "numpy.ndarray.std")<br>(\[axis, dtype, out, ddof, ...\]) | Returns the standard deviation of the array elements along given axis. |
| [`ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")<br>(\[axis, dtype, out, keepdims, ...\]) | Return the product of the array elements over the given axis |
| [`ndarray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html#numpy.ndarray.cumprod "numpy.ndarray.cumprod")<br>(\[axis, dtype, out\]) | Return the cumulative product of the elements along the given axis. |
| [`ndarray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")<br>(\[axis, out, keepdims, where\]) | Returns True if all elements evaluate to True. |
| [`ndarray.any`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html#numpy.ndarray.any "numpy.ndarray.any")<br>(\[axis, out, keepdims, where\]) | Returns True if any of the elements of _a_ evaluate to True. |

Arithmetic, matrix multiplication, and comparison operations[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arithmetic-matrix-multiplication-and-comparison-operations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Arithmetic and comparison operations on [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 are defined as element-wise operations, and generally yield [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 objects as results.

Each of the arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `divmod()`, `**` or `pow()`, `<<`, `>>`, `&`, `^`, `|`, `~`) and the comparisons (`==`, `<`, `>`, `<=`, `>=`, `!=`) is equivalent to the corresponding universal function (or [ufunc](https://numpy.org/doc/stable/glossary.html#term-ufunc)
 for short) in NumPy. For more information, see the section on [Universal Functions](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs)
.

Comparison operators:

|     |     |
| --- | --- |
| [`ndarray.__lt__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__lt__.html#numpy.ndarray.__lt__ "numpy.ndarray.__lt__")<br>(value, /) | Return self<value. |
| [`ndarray.__le__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__le__.html#numpy.ndarray.__le__ "numpy.ndarray.__le__")<br>(value, /) | Return self<=value. |
| [`ndarray.__gt__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__gt__.html#numpy.ndarray.__gt__ "numpy.ndarray.__gt__")<br>(value, /) | Return self>value. |
| [`ndarray.__ge__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ge__.html#numpy.ndarray.__ge__ "numpy.ndarray.__ge__")<br>(value, /) | Return self>=value. |
| [`ndarray.__eq__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__eq__.html#numpy.ndarray.__eq__ "numpy.ndarray.__eq__")<br>(value, /) | Return self==value. |
| [`ndarray.__ne__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ne__.html#numpy.ndarray.__ne__ "numpy.ndarray.__ne__")<br>(value, /) | Return self!=value. |

Truth value of an array ([`bool()`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
):

|     |     |
| --- | --- |
| [`ndarray.__bool__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__bool__.html#numpy.ndarray.__bool__ "numpy.ndarray.__bool__")<br>(/) | True if self else False |

Note

Truth-value testing of an array invokes [`ndarray.__bool__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__bool__.html#numpy.ndarray.__bool__ "numpy.ndarray.__bool__")
, which raises an error if the number of elements in the array is not 1, because the truth value of such arrays is ambiguous. Use [`.any()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html#numpy.ndarray.any "numpy.ndarray.any")
 and [`.all()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")
 instead to be clear about what is meant in such cases. (If you wish to check for whether an array is empty, use for example `.size > 0`.)

Unary operations:

|     |     |
| --- | --- |
| [`ndarray.__neg__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__neg__.html#numpy.ndarray.__neg__ "numpy.ndarray.__neg__")<br>(/) | \-self |
| [`ndarray.__pos__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__pos__.html#numpy.ndarray.__pos__ "numpy.ndarray.__pos__")<br>(/) | +self |
| [`ndarray.__abs__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__abs__.html#numpy.ndarray.__abs__ "numpy.ndarray.__abs__")<br>(self) |     |
| [`ndarray.__invert__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__invert__.html#numpy.ndarray.__invert__ "numpy.ndarray.__invert__")<br>(/) | ~self |

Arithmetic:

|     |     |
| --- | --- |
| [`ndarray.__add__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__add__.html#numpy.ndarray.__add__ "numpy.ndarray.__add__")<br>(value, /) | Return self+value. |
| [`ndarray.__sub__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__sub__.html#numpy.ndarray.__sub__ "numpy.ndarray.__sub__")<br>(value, /) | Return self-value. |
| [`ndarray.__mul__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__mul__.html#numpy.ndarray.__mul__ "numpy.ndarray.__mul__")<br>(value, /) | Return self\*value. |
| [`ndarray.__truediv__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__truediv__.html#numpy.ndarray.__truediv__ "numpy.ndarray.__truediv__")<br>(value, /) | Return self/value. |
| [`ndarray.__floordiv__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__floordiv__.html#numpy.ndarray.__floordiv__ "numpy.ndarray.__floordiv__")<br>(value, /) | Return self//value. |
| [`ndarray.__mod__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__mod__.html#numpy.ndarray.__mod__ "numpy.ndarray.__mod__")<br>(value, /) | Return self%value. |
| [`ndarray.__divmod__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__divmod__.html#numpy.ndarray.__divmod__ "numpy.ndarray.__divmod__")<br>(value, /) | Return divmod(self, value). |
| [`ndarray.__pow__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__pow__.html#numpy.ndarray.__pow__ "numpy.ndarray.__pow__")<br>(value\[, mod\]) | Return pow(self, value, mod). |
| [`ndarray.__lshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__lshift__.html#numpy.ndarray.__lshift__ "numpy.ndarray.__lshift__")<br>(value, /) | Return self<<value. |
| [`ndarray.__rshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__rshift__.html#numpy.ndarray.__rshift__ "numpy.ndarray.__rshift__")<br>(value, /) | Return self>>value. |
| [`ndarray.__and__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__and__.html#numpy.ndarray.__and__ "numpy.ndarray.__and__")<br>(value, /) | Return self&value. |
| [`ndarray.__or__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__or__.html#numpy.ndarray.__or__ "numpy.ndarray.__or__")<br>(value, /) | Return self\|value. |
| [`ndarray.__xor__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__xor__.html#numpy.ndarray.__xor__ "numpy.ndarray.__xor__")<br>(value, /) | Return self^value. |

Note

*   Any third argument to [`pow`](https://numpy.org/doc/stable/reference/generated/numpy.pow.html#numpy.pow "numpy.pow")
     is silently ignored, as the underlying [`ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")
     takes only two arguments.
    
*   Because [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
     is a built-in type (written in C), the `__r{op}__` special methods are not directly defined.
    
*   The functions called to implement many arithmetic special methods for arrays can be modified using [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
    .
    

Arithmetic, in-place:

|     |     |
| --- | --- |
| [`ndarray.__iadd__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__iadd__.html#numpy.ndarray.__iadd__ "numpy.ndarray.__iadd__")<br>(value, /) | Return self+=value. |
| [`ndarray.__isub__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__isub__.html#numpy.ndarray.__isub__ "numpy.ndarray.__isub__")<br>(value, /) | Return self-=value. |
| [`ndarray.__imul__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__imul__.html#numpy.ndarray.__imul__ "numpy.ndarray.__imul__")<br>(value, /) | Return self\*=value. |
| [`ndarray.__itruediv__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__itruediv__.html#numpy.ndarray.__itruediv__ "numpy.ndarray.__itruediv__")<br>(value, /) | Return self/=value. |
| [`ndarray.__ifloordiv__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ifloordiv__.html#numpy.ndarray.__ifloordiv__ "numpy.ndarray.__ifloordiv__")<br>(value, /) | Return self//=value. |
| [`ndarray.__imod__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__imod__.html#numpy.ndarray.__imod__ "numpy.ndarray.__imod__")<br>(value, /) | Return self%=value. |
| [`ndarray.__ipow__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ipow__.html#numpy.ndarray.__ipow__ "numpy.ndarray.__ipow__")<br>(value, /) | Return self\*\*=value. |
| [`ndarray.__ilshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ilshift__.html#numpy.ndarray.__ilshift__ "numpy.ndarray.__ilshift__")<br>(value, /) | Return self<<=value. |
| [`ndarray.__irshift__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__irshift__.html#numpy.ndarray.__irshift__ "numpy.ndarray.__irshift__")<br>(value, /) | Return self>>=value. |
| [`ndarray.__iand__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__iand__.html#numpy.ndarray.__iand__ "numpy.ndarray.__iand__")<br>(value, /) | Return self&=value. |
| [`ndarray.__ior__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ior__.html#numpy.ndarray.__ior__ "numpy.ndarray.__ior__")<br>(value, /) | Return self\|=value. |
| [`ndarray.__ixor__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__ixor__.html#numpy.ndarray.__ixor__ "numpy.ndarray.__ixor__")<br>(value, /) | Return self^=value. |

Warning

In place operations will perform the calculation using the precision decided by the data type of the two operands, but will silently downcast the result (if necessary) so it can fit back into the array. Therefore, for mixed precision calculations, `A {op}= B` can be different than `A = A {op} B`. For example, suppose `a = ones((3,3))`. Then, `a += 3j` is different than `a = a + 3j`: while they both perform the same computation, `a += 3` casts the result to fit back in `a`, whereas `a = a + 3j` re-binds the name `a` to the result.

Matrix Multiplication:

|     |     |
| --- | --- |
| [`ndarray.__matmul__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__matmul__.html#numpy.ndarray.__matmul__ "numpy.ndarray.__matmul__")<br>(value, /) | Return [self@value](mailto:self%40value)<br>. |

Note

Matrix operators `@` and `@=` were introduced in Python 3.5 following [**PEP 465**](https://peps.python.org/pep-0465/)
, and the `@` operator has been introduced in NumPy 1.10.0. Further information can be found in the [`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
 documentation.

Special methods[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#special-methods "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

For standard library functions:

|     |     |
| --- | --- |
| [`ndarray.__copy__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__copy__.html#numpy.ndarray.__copy__ "numpy.ndarray.__copy__")<br>() | Used if [`copy.copy`](https://docs.python.org/3/library/copy.html#copy.copy "(in Python v3.14)")<br> is called on an array. |
| [`ndarray.__deepcopy__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__deepcopy__.html#numpy.ndarray.__deepcopy__ "numpy.ndarray.__deepcopy__")<br>(memo, /) | Used if [`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.14)")<br> is called on an array. |
| [`ndarray.__reduce__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__reduce__.html#numpy.ndarray.__reduce__ "numpy.ndarray.__reduce__")<br>() | For pickling. |
| [`ndarray.__setstate__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__setstate__.html#numpy.ndarray.__setstate__ "numpy.ndarray.__setstate__")<br>(state, /) | For unpickling. |

Basic customization:

|     |     |
| --- | --- |
| [`ndarray.__new__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__new__.html#numpy.ndarray.__new__ "numpy.ndarray.__new__")<br>(\*args, \*\*kwargs) |     |
| [`ndarray.__array__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__array__.html#numpy.ndarray.__array__ "numpy.ndarray.__array__")<br>(\[dtype\], \*\[, copy\]) | For `dtype` parameter it returns a new reference to self if `dtype` is not given or it matches array's data type. |
| [`ndarray.__array_wrap__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__array_wrap__.html#numpy.ndarray.__array_wrap__ "numpy.ndarray.__array_wrap__")<br>(array\[, context\[, ...) | Returns a view of [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")<br> with the same type as self. |\
\
Container customization: (see [Indexing](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)\
)\
\
|     |     |\
| --- | --- |\
| [`ndarray.__len__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__len__.html#numpy.ndarray.__len__ "numpy.ndarray.__len__")<br>(/) | Return len(self). |\
| [`ndarray.__getitem__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__getitem__.html#numpy.ndarray.__getitem__ "numpy.ndarray.__getitem__")<br>(key, /) | Return self\[key\]. |\
| [`ndarray.__setitem__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__setitem__.html#numpy.ndarray.__setitem__ "numpy.ndarray.__setitem__")<br>(key, value, /) | Set self\[key\] to value. |\
| [`ndarray.__contains__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__contains__.html#numpy.ndarray.__contains__ "numpy.ndarray.__contains__")<br>(key, /) | Return bool(key in self). |\
\
Conversion; the operations [`int()`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")\
, [`float()`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")\
 and [`complex()`](https://docs.python.org/3/library/functions.html#complex "(in Python v3.14)")\
. They work only on arrays that have one element in them and return the appropriate scalar.\
\
|     |     |\
| --- | --- |\
| [`ndarray.__int__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__int__.html#numpy.ndarray.__int__ "numpy.ndarray.__int__")<br>(self) |     |\
| [`ndarray.__float__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__float__.html#numpy.ndarray.__float__ "numpy.ndarray.__float__")<br>(self) |     |\
| [`ndarray.__complex__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__complex__.html#numpy.ndarray.__complex__ "numpy.ndarray.__complex__")<br>(self) |     |\
\
String representations:\
\
|     |     |\
| --- | --- |\
| [`ndarray.__str__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__str__.html#numpy.ndarray.__str__ "numpy.ndarray.__str__")<br>(/) | Return str(self). |\
| [`ndarray.__repr__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__repr__.html#numpy.ndarray.__repr__ "numpy.ndarray.__repr__")<br>(/) | Return repr(self). |\
\
Utility method for typing:\
\
|     |     |\
| --- | --- |\
| [`ndarray.__class_getitem__`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__class_getitem__.html#numpy.ndarray.__class_getitem__ "numpy.ndarray.__class_getitem__")<br>($cls, item, /) | ndarray\[shape, dtype\] |\
\
Structural pattern matching[#](https://numpy.org/doc/stable/reference/arrays.ndarray.html#structural-pattern-matching "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------\
\
Arrays support [**structural pattern matching**](https://peps.python.org/pep-0634/)\
. The array is matched as a sequence, so you can unpack arrays along the first dimension in `match`/`case` statements:\
\
\>>> arr \= np.array(\[\[1, 2\], \[3, 4\]\])\
\>>> match arr:\
...     case \[row1, row2\]:\
...         print(f"row1={row1}, row2={row2}")\
row1=\[1 2\], row2=\[3 4\]\
\
Copy to clipboard\
\
Nested patterns work too, matching inner dimensions:\
\
\>>> match arr:\
...     case \[\[a, b\], \[c, d\]\]:\
...         print(f"a={a}, b={b}, c={c}, d={d}")\
a=1, b=2, c=3, d=4\
\
Copy to clipboard\
\
All ndarray subclasses inherit this behavior.\
\
On this page