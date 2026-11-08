[Skip to main content](https://numpy.org/doc/stable/reference/c-api/array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/array.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/array.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/array.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/array.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/array.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/array.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/array.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/array.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/array.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/array.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/array.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/array.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/array.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/array.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/array.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/array.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/array.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/array.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/array.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/array.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/array.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Array API[#](https://numpy.org/doc/stable/reference/c-api/array.html#array-api "Link to this heading")

=======================================================================================================

The test of a first-rate intelligence is the ability to hold two

opposed ideas in the mind at the same time, and still retain the

ability to function.

— _F. Scott Fitzgerald_

For a successful technology, reality must take precedence over public

relations, for Nature cannot be fooled.

— _Richard P. Feynman_

Array structure and data access[#](https://numpy.org/doc/stable/reference/c-api/array.html#array-structure-and-data-access "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

These macros access the [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 structure members and are defined in `ndarraytypes.h`. The input argument, _arr_, can be any [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
\* that is directly interpretable as a [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
\* (any instance of the [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 and its sub-types).

int PyArray\_NDIM([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NDIM "Link to this definition")
  

The number of dimensions in the array.

int PyArray\_FLAGS([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FLAGS "Link to this definition")
  

Returns an integer representing the [array-flags](https://numpy.org/doc/stable/reference/c-api/array.html#array-flags)
.

int PyArray\_TYPE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_TYPE "Link to this definition")
  

Return the (builtin) typenumber for the elements of this array.

int PyArray\_Pack(const [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, void \*item, const [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*value)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Pack "Link to this definition")
  

New in version 2.0.

Sets the memory location `item` of dtype `descr` to `value`.

The function is equivalent to setting a single array element with a Python assignment. Returns 0 on success and -1 with an error set on failure.

Note

If the `descr` has the [`NPY_NEEDS_INIT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_INIT "NPY_NEEDS_INIT")
 flag set, the data must be valid or the memory zeroed.

int PyArray\_SETITEM([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, void \*itemptr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SETITEM "Link to this definition")
  

Convert obj and place it in the ndarray, _arr_, at the place pointed to by itemptr. Return -1 if an error occurs or 0 on success.

Note

In general, prefer the use of [`PyArray_Pack`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Pack "PyArray_Pack")
 when handling arbitrary Python objects. Setitem is for example not able to handle arbitrary casts between different dtypes.

void PyArray\_ENABLEFLAGS([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int flags)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ENABLEFLAGS "Link to this definition")
  

Enables the specified array flags. This function does no validation, and assumes that you know what you’re doing.

void PyArray\_CLEARFLAGS([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int flags)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CLEARFLAGS "Link to this definition")
  

Clears the specified array flags. This function does no validation, and assumes that you know what you’re doing.

void \*PyArray\_DATA([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DATA "Link to this definition")
  

char \*PyArray\_BYTES([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_BYTES "Link to this definition")
  

These two macros are similar and obtain the pointer to the data-buffer for the array. The first macro can (and should be) assigned to a particular pointer where the second is for generic processing. If you have not guaranteed a contiguous and/or aligned array then be sure you understand how to access the data in the array to avoid memory and/or alignment problems.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*PyArray\_DIMS([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DIMS "Link to this definition")
  

Returns a pointer to the dimensions/shape of the array. The number of elements matches the number of dimensions of the array. Can return `NULL` for 0-dimensional arrays.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*PyArray\_SHAPE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SHAPE "Link to this definition")
  

A synonym for [`PyArray_DIMS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DIMS "PyArray_DIMS")
, named to be consistent with the [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")
 usage within Python.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*PyArray\_STRIDES([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_STRIDES "Link to this definition")
  

Returns a pointer to the strides of the array. The number of elements matches the number of dimensions of the array.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyArray\_DIM([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DIM "Link to this definition")
  

Return the shape in the _n_ \\(^{\\textrm{th}}\\) dimension.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyArray\_STRIDE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_STRIDE "Link to this definition")
  

Return the stride in the _n_ \\(^{\\textrm{th}}\\) dimension.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyArray\_ITEMSIZE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITEMSIZE "Link to this definition")
  

Return the itemsize for the elements of this array.

Note that, in the old API that was deprecated in version 1.7, this function had the return type `int`.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyArray\_SIZE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SIZE "Link to this definition")
  

Returns the total size (in number of elements) of the array.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyArray\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Size "Link to this definition")
  

Returns 0 if _obj_ is not a sub-class of ndarray. Otherwise, returns the total number of elements in the array. Safer version of [`PyArray_SIZE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SIZE "PyArray_SIZE")
 (_obj_).

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyArray\_NBYTES([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NBYTES "Link to this definition")
  

Returns the total number of bytes consumed by the array.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_BASE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_BASE "Link to this definition")
  

This returns the base object of the array. In most cases, this means the object which owns the memory the array is pointing at.

If you are constructing an array using the C API, and specifying your own memory, you should use the function [`PyArray_SetBaseObject`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetBaseObject "PyArray_SetBaseObject")
 to set the base to an object which owns the memory.

If the [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
 flag is set, it has a different meaning, namely base is the array into which the current array will be copied upon copy resolution. This overloading of the base property for two functions is likely to change in a future version of NumPy.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*PyArray\_DESCR([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DESCR "Link to this definition")
  

Returns a borrowed reference to the dtype property of the array.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*PyArray\_DTYPE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DTYPE "Link to this definition")
  

A synonym for PyArray\_DESCR, named to be consistent with the ‘dtype’ usage within Python.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_GETITEM([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, void \*itemptr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GETITEM "Link to this definition")
  

Get a Python object of a builtin type from the ndarray, _arr_, at the location pointed to by itemptr. Return `NULL` on failure.

[`numpy.ndarray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item")
 is identical to PyArray\_GETITEM.

int PyArray\_FinalizeFunc([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FinalizeFunc "Link to this definition")
  

The function pointed to by the [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
 [`__array_finalize__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__")
. The first argument is the newly created sub-type. The second argument (if not NULL) is the “parent” array (if the array was created using slicing or some other operation where a clearly-distinguishable parent is present). This routine can do anything it wants to. It should return a -1 on error and 0 otherwise.

### Data access[#](https://numpy.org/doc/stable/reference/c-api/array.html#data-access "Link to this heading")

These functions and macros provide easy access to elements of the ndarray from C. These work for all arrays. You may need to take care when accessing the data in the array, however, if it is not in machine byte-order, misaligned, or not writeable. In other words, be sure to respect the state of the flags unless you know what you are doing, or have previously guaranteed an array that is writeable, aligned, and in machine byte-order using [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
. If you wish to handle all types of arrays, the copyswap function for each type is useful for handling misbehaved arrays. Some platforms (e.g. Solaris) do not like misaligned data and will crash if you de-reference a misaligned pointer. Other platforms (e.g. x86 Linux) will just work more slowly with misaligned data.

void \*PyArray\_GetPtr([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*aobj, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*ind)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetPtr "Link to this definition")
  

Return a pointer to the data of the ndarray, _aobj_, at the N-dimensional index given by the c-array, _ind_, (which must be at least _aobj_ ->nd in size). You may want to typecast the returned pointer to the data type of the ndarray.

void \*PyArray\_GETPTR1([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 i)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GETPTR1 "Link to this definition")
  

void \*PyArray\_GETPTR2([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 i, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 j)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GETPTR2 "Link to this definition")
  

void \*PyArray\_GETPTR3([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 i, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 j, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 k)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GETPTR3 "Link to this definition")
  

void \*PyArray\_GETPTR4([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 i, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 j, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 k, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 l)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GETPTR4 "Link to this definition")
  

Quick, inline access to the element at the given coordinates in the ndarray, _obj_, which must have respectively 1, 2, 3, or 4 dimensions (this is not checked). The corresponding _i_, _j_, _k_, and _l_ coordinates can be any integer but will be interpreted as `npy_intp`. You may want to typecast the returned pointer to the data type of the ndarray.

Creating arrays[#](https://numpy.org/doc/stable/reference/c-api/array.html#creating-arrays "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

### From scratch[#](https://numpy.org/doc/stable/reference/c-api/array.html#from-scratch "Link to this heading")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_NewFromDescr([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*subtype, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*strides, void \*data, int flags, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NewFromDescr "Link to this definition")
  

This function steals a reference to _descr_. The easiest way to get one is using [`PyArray_DescrFromType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromType "PyArray_DescrFromType")
.

This is the main array creation function. Most new arrays are created with this flexible function.

The returned object is an object of Python-type _subtype_, which must be a subtype of [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
. The array has _nd_ dimensions, described by _dims_. The data-type descriptor of the new array is _descr_.

If _subtype_ is of an array subclass instead of the base [`&PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
, then _obj_ is the object to pass to the [`__array_finalize__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__")
 method of the subclass.

If _data_ is `NULL`, then new unitinialized memory will be allocated and _flags_ can be non-zero to indicate a Fortran-style contiguous array. Use [`PyArray_FILLWBYTE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FILLWBYTE "PyArray_FILLWBYTE")
 to initialize the memory.

If _data_ is not `NULL`, then it is assumed to point to the memory to be used for the array and the _flags_ argument is used as the new flags for the array (except the state of [`NPY_ARRAY_OWNDATA`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_OWNDATA "NPY_ARRAY_OWNDATA")
, [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
 flag of the new array will be reset).

In addition, if _data_ is non-NULL, then _strides_ can also be provided. If _strides_ is `NULL`, then the array strides are computed as C-style contiguous (default) or Fortran-style contiguous (_flags_ is nonzero for _data_ = `NULL` or _flags_ & [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 is nonzero non-NULL _data_). Any provided _dims_ and _strides_ are copied into newly allocated dimension and strides arrays for the new array object.

[`PyArray_CheckStrides`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckStrides "PyArray_CheckStrides")
 can help verify non- `NULL` stride information.

If `data` is provided, it must stay alive for the life of the array. One way to manage this is through [`PyArray_SetBaseObject`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetBaseObject "PyArray_SetBaseObject")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_NewLikeArray([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*prototype, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 order, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, int subok)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NewLikeArray "Link to this definition")
  

This function steals a reference to _descr_ if it is not NULL. This array creation routine allows for the convenient creation of a new array matching an existing array’s shapes and memory layout, possibly changing the layout and/or data type.

When _order_ is [`NPY_ANYORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_ANYORDER "NPY_ANYORDER")
, the result order is [`NPY_FORTRANORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_FORTRANORDER "NPY_FORTRANORDER")
 if _prototype_ is a fortran array, [`NPY_CORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_CORDER "NPY_CORDER")
 otherwise. When _order_ is [`NPY_KEEPORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_KEEPORDER "NPY_KEEPORDER")
, the result order matches that of _prototype_, even when the axes of _prototype_ aren’t in C or Fortran order.

If _descr_ is NULL, the data type of _prototype_ is used.

If _subok_ is 1, the newly created array will use the sub-type of _prototype_ to create the new array, otherwise it will create a base-class array.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_New([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*subtype, int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, int type\_num, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*strides, void \*data, int itemsize, int flags, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_New "Link to this definition")
  

This is similar to [`PyArray_NewFromDescr`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NewFromDescr "PyArray_NewFromDescr")
 (…) except you specify the data-type descriptor with _type\_num_ and _itemsize_, where _type\_num_ corresponds to a builtin (or user-defined) type. If the type always has the same number of bytes, then itemsize is ignored. Otherwise, itemsize specifies the particular size of this array.

Warning

If data is passed to [`PyArray_NewFromDescr`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NewFromDescr "PyArray_NewFromDescr")
 or [`PyArray_New`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_New "PyArray_New")
, this memory must not be deallocated until the new array is deleted. If this data came from another Python object, this can be accomplished using [`Py_INCREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "(in Python v3.14)")
 on that object and setting the base member of the new array to point to that object. If strides are passed in they must be consistent with the dimensions, the itemsize, and the data of the array.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_SimpleNew(int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SimpleNew "Link to this definition")
  

Create a new uninitialized array of type, _typenum_, whose size in each of _nd_ dimensions is given by the integer array, _dims_.The memory for the array is uninitialized (unless typenum is [`NPY_OBJECT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "NPY_OBJECT")
 in which case each element in the array is set to NULL). The _typenum_ argument allows specification of any of the builtin data-types such as [`NPY_FLOAT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT "NPY_FLOAT")
 or [`NPY_LONG`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONG "NPY_LONG")
. The memory for the array can be set to zero if desired using [`PyArray_FILLWBYTE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FILLWBYTE "PyArray_FILLWBYTE")
 (return\_object, 0).This function cannot be used to create a flexible-type array (no itemsize given).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_SimpleNewFromData(int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, int typenum, void \*data)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SimpleNewFromData "Link to this definition")
  

Create an array wrapper around _data_ pointed to by the given pointer. The array flags will have a default that the data area is well-behaved and C-style contiguous. The shape of the array is given by the _dims_ c-array of length _nd_. The data-type of the array is indicated by _typenum_. If data comes from another reference-counted Python object, the reference count on this object should be increased after the pointer is passed in, and the base member of the returned ndarray should point to the Python object that owns the data. This will ensure that the provided memory is not freed while the returned array is in existence.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_SimpleNewFromDescr(int nd, [npy\_int](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int "npy_int")
 const \*dims, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SimpleNewFromDescr "Link to this definition")
  

This function steals a reference to _descr_.

Create a new array with the provided data-type descriptor, _descr_, of the shape determined by _nd_ and _dims_.

void PyArray\_FILLWBYTE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, int val)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FILLWBYTE "Link to this definition")
  

Fill the array pointed to by _obj_ —which must be a (subclass of) ndarray—with the contents of _val_ (evaluated as a byte). This macro calls memset, so obj must be contiguous.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Zeros(int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int fortran)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Zeros "Link to this definition")
  

Construct a new _nd_ -dimensional array with shape given by _dims_ and data type given by _dtype_. If _fortran_ is non-zero, then a Fortran-order array is created, otherwise a C-order array is created. Fill the memory with zeros (or the 0 object if _dtype_ corresponds to [`NPY_OBJECT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "NPY_OBJECT")
 ).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ZEROS(int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, int type\_num, int fortran)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ZEROS "Link to this definition")
  

Macro form of [`PyArray_Zeros`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Zeros "PyArray_Zeros")
 which takes a type-number instead of a data-type object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Empty(int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int fortran)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Empty "Link to this definition")
  

Construct a new _nd_ -dimensional array with shape given by _dims_ and data type given by _dtype_. If _fortran_ is non-zero, then a Fortran-order array is created, otherwise a C-order array is created. The array is uninitialized unless the data type corresponds to [`NPY_OBJECT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "NPY_OBJECT")
 in which case the array is filled with [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "(in Python v3.14)")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_EMPTY(int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dims, int typenum, int fortran)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EMPTY "Link to this definition")
  

Macro form of [`PyArray_Empty`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Empty "PyArray_Empty")
 which takes a type-number, _typenum_, instead of a data-type object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Arange(double start, double stop, double step, int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Arange "Link to this definition")
  

Construct a new 1-dimensional array of data-type, _typenum_, that ranges from _start_ to _stop_ (exclusive) in increments of _step_ . Equivalent to **arange** (_start_, _stop_, _step_, dtype).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ArangeObj([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*stop, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*step, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArangeObj "Link to this definition")
  

Construct a new 1-dimensional array of data-type determined by `descr`, that ranges from `start` to `stop` (exclusive) in increments of `step`. Equivalent to arange( `start`, `stop`, `step`, `typenum` ).

int PyArray\_SetBaseObject([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetBaseObject "Link to this definition")
  

This function **steals a reference** to `obj` and sets it as the base property of `arr`.

If you construct an array by passing in your own memory buffer as a parameter, you need to set the array’s _base_ property to ensure the lifetime of the memory buffer is appropriate.

The return value is 0 on success, -1 on failure.

If the object provided is an array, this function traverses the chain of _base_ pointers so that each array points to the owner of the memory directly. Once the base is set, it may not be changed to another value.

### From other objects[#](https://numpy.org/doc/stable/reference/c-api/array.html#from-other-objects "Link to this heading")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromAny([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int min\_depth, int max\_depth, int requirements, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*context)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "Link to this definition")
  

This is the main function used to obtain an array from any nested sequence, or object that exposes the array interface, _op_. The parameters allow specification of the required _dtype_, the minimum (_min\_depth_) and maximum (_max\_depth_) number of dimensions acceptable, and other _requirements_ for the array. This function **steals a reference** to the dtype argument, which needs to be a [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 structure indicating the desired data-type (including required byteorder). The _dtype_ argument may be `NULL`, indicating that any data-type (and byteorder) is acceptable. Unless [`NPY_ARRAY_FORCECAST`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_FORCECAST "NPY_ARRAY_FORCECAST")
 is present in `flags`, this call will generate an error if the data type cannot be safely obtained from the object. If you want to use `NULL` for the _dtype_ and ensure the array is not swapped then use [`PyArray_CheckFromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckFromAny "PyArray_CheckFromAny")
. A value of 0 for either of the depth parameters causes the parameter to be ignored. Any of the following array flags can be added (_e.g._ using |) to get the _requirements_ argument. If your code can handle general (_e.g._ strided, byte-swapped, or unaligned arrays) then _requirements_ may be 0. Also, if _op_ is not already an array (or does not expose the array interface), then a new array will be created (and filled from _op_ using the sequence protocol). The new array will have [`NPY_ARRAY_DEFAULT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_DEFAULT "NPY_ARRAY_DEFAULT")
 as its flags member. The _context_ argument is unused.

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")

Make sure the returned array is C-style contiguous

[`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")

Make sure the returned array is Fortran-style contiguous.

[`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

Make sure the returned array is aligned on proper boundaries for its data type. An aligned array has the data pointer and every strides factor as a multiple of the alignment factor for the data-type- descriptor.

[`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")

Make sure the returned array can be written to.

[`NPY_ARRAY_ENSURECOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSURECOPY "NPY_ARRAY_ENSURECOPY")

Make sure a copy is made of _op_. If this flag is not present, data is not copied if it can be avoided.

[`NPY_ARRAY_ENSUREARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "NPY_ARRAY_ENSUREARRAY")

Make sure the result is a base-class ndarray. By default, if _op_ is an instance of a subclass of ndarray, an instance of that same subclass is returned. If this flag is set, an ndarray object will be returned instead.

[`NPY_ARRAY_FORCECAST`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_FORCECAST "NPY_ARRAY_FORCECAST")

Force a cast to the output type even if it cannot be done safely. Without this flag, a data cast will occur only if it can be done safely, otherwise an error is raised.

[`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")

If _op_ is already an array, but does not satisfy the requirements, then a copy is made (which will satisfy the requirements). If this flag is present and a copy (of an object that is already an array) must be made, then the corresponding [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
 flag is set in the returned copy and _op_ is made to be read-only. You must be sure to call [`PyArray_ResolveWritebackIfCopy`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "PyArray_ResolveWritebackIfCopy")
 to copy the contents back into _op_ and the _op_ array will be made writeable again. If _op_ is not writeable to begin with, or if it is not already an array, then an error is raised.

[Combinations of array flags](https://numpy.org/doc/stable/reference/c-api/array.html#combinations-of-array-flags)
 can also be added.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_CheckFromAny([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int min\_depth, int max\_depth, int requirements, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*context)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckFromAny "Link to this definition")
  

Nearly identical to [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 (…) except _requirements_ can contain [`NPY_ARRAY_NOTSWAPPED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "NPY_ARRAY_NOTSWAPPED")
 (over-riding the specification in _dtype_) and [`NPY_ARRAY_ELEMENTSTRIDES`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ELEMENTSTRIDES "NPY_ARRAY_ELEMENTSTRIDES")
 which indicates that the array should be aligned in the sense that the strides are multiples of the element size.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromArray([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*op, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*newtype, int requirements)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromArray "Link to this definition")
  

Special case of [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 for when _op_ is already an array but it needs to be of a specific _newtype_ (including byte-order) or has certain _requirements_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromStructInterface([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromStructInterface "Link to this definition")
  

Returns an ndarray object from a Python object that exposes the [`__array_struct__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "object.__array_struct__")
 attribute and follows the array interface protocol. If the object does not contain this attribute then a borrowed reference to [`Py_NotImplemented`](https://docs.python.org/3/c-api/object.html#c.Py_NotImplemented "(in Python v3.14)")
 is returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromInterface([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromInterface "Link to this definition")
  

Returns an ndarray object from a Python object that exposes the [`__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "object.__array_interface__")
 attribute following the array interface protocol. If the object does not contain this attribute then a borrowed reference to [`Py_NotImplemented`](https://docs.python.org/3/c-api/object.html#c.Py_NotImplemented "(in Python v3.14)")
 is returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromArrayAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*context)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromArrayAttr "Link to this definition")
  

Return an ndarray object from a Python object that exposes the [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
 method. The third-party implementations of [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
 must take `dtype` and `copy` keyword arguments. `context` is unused.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ContiguousFromAny([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, int typenum, int min\_depth, int max\_depth)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ContiguousFromAny "Link to this definition")
  

This function returns a (C-style) contiguous and behaved function array from any nested sequence or array interface exporting object, _op_, of (non-flexible) type given by the enumerated _typenum_, of minimum depth _min\_depth_, and of maximum depth _max\_depth_. Equivalent to a call to [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 with requirements set to [`NPY_ARRAY_DEFAULT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_DEFAULT "NPY_ARRAY_DEFAULT")
 and the type\_num member of the type argument set to _typenum_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ContiguousFromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, int typenum, int min\_depth, int max\_depth)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ContiguousFromObject "Link to this definition")
  

This function returns a well-behaved C-style contiguous array from any nested sequence or array-interface exporting object. The minimum number of dimensions the array can have is given by _min\_depth_ while the maximum is _max\_depth_. This is equivalent to call [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 with requirements [`NPY_ARRAY_DEFAULT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_DEFAULT "NPY_ARRAY_DEFAULT")
 and [`NPY_ARRAY_ENSUREARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "NPY_ARRAY_ENSUREARRAY")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, int typenum, int min\_depth, int max\_depth)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromObject "Link to this definition")
  

Return an aligned and in native-byteorder array from any nested sequence or array-interface exporting object, op, of a type given by the enumerated typenum. The minimum number of dimensions the array can have is given by min\_depth while the maximum is max\_depth. This is equivalent to a call to [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 with requirements set to BEHAVED.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_EnsureArray([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EnsureArray "Link to this definition")
  

This function **steals a reference** to `op` and makes sure that `op` is a base-class ndarray. It special cases array scalars, but otherwise calls [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 ( `op`, NULL, 0, 0, [`NPY_ARRAY_ENSUREARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "NPY_ARRAY_ENSUREARRAY")
, NULL).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromString(char \*string, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 slen, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 num, char \*sep)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromString "Link to this definition")
  

Construct a one-dimensional ndarray of a single type from a binary or (ASCII) text `string` of length `slen`. The data-type of the array to-be-created is given by `dtype`. If num is -1, then **copy** the entire string and return an appropriately sized array, otherwise, `num` is the number of items to **copy** from the string. If `sep` is NULL (or “”), then interpret the string as bytes of binary data, otherwise convert the sub-strings separated by `sep` to items of data-type `dtype`. Some data-types may not be readable in text mode and an error will be raised if that occurs. All errors return NULL.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromFile(FILE \*fp, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 num, char \*sep)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromFile "Link to this definition")
  

Construct a one-dimensional ndarray of a single type from a binary or text file. The open file pointer is `fp`, the data-type of the array to be created is given by `dtype`. This must match the data in the file. If `num` is -1, then read until the end of the file and return an appropriately sized array, otherwise, `num` is the number of items to read. If `sep` is NULL (or “”), then read from the file in binary mode, otherwise read from the file in text mode with `sep` providing the item separator. Some array types cannot be read in text mode in which case an error is raised.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FromBuffer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*buf, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 count, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 offset)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromBuffer "Link to this definition")
  

Construct a one-dimensional ndarray of a single type from an object, `buf`, that exports the (single-segment) buffer protocol (or has an attribute \_\_buffer\_\_ that returns an object that exports the buffer protocol). A writeable buffer will be tried first followed by a read- only buffer. The [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 flag of the returned array will reflect which one was successful. The data is assumed to start at `offset` bytes from the start of the memory location for the object. The type of the data in the buffer will be interpreted depending on the data- type descriptor, `dtype.` If `count` is negative then it will be determined from the size of the buffer and the requested itemsize, otherwise, `count` represents how many elements should be converted from the buffer.

int PyArray\_CopyInto([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*dest, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*src)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CopyInto "Link to this definition")
  

Copy from the source array, `src`, into the destination array, `dest`, performing a data-type conversion if necessary. If an error occurs return -1 (otherwise 0). The shape of `src` must be broadcastable to the shape of `dest`. NumPy checks for overlapping memory when copying two arrays.

int PyArray\_CopyObject([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*dest, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*src)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CopyObject "Link to this definition")
  

Assign an object `src` to a NumPy array `dest` according to array-coercion rules. This is basically identical to [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
, but assigns directly to the output array. Returns 0 on success and -1 on failures.

[PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*PyArray\_GETCONTIGUOUS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GETCONTIGUOUS "Link to this definition")
  

If `op` is already (C-style) contiguous and well-behaved then just return a reference, otherwise return a (contiguous and well-behaved) copy of the array. The parameter op must be a (sub-class of an) ndarray and no checking for that is done.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FROM\_O([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_O "Link to this definition")
  

Convert `obj` to an ndarray. The argument can be any nested sequence or object that exports the array interface. This is a macro form of [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 using `NULL`, 0, 0, 0 for the other arguments. Your code must be able to handle any data-type descriptor and any combination of data-flags to use this macro.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FROM\_OF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, int requirements)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_OF "Link to this definition")
  

Similar to [`PyArray_FROM_O`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_O "PyArray_FROM_O")
 except it can take an argument of _requirements_ indicating properties the resulting array must have. Available requirements that can be enforced are [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
, [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
, [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
, [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
, [`NPY_ARRAY_NOTSWAPPED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "NPY_ARRAY_NOTSWAPPED")
, [`NPY_ARRAY_ENSURECOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSURECOPY "NPY_ARRAY_ENSURECOPY")
, [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
, [`NPY_ARRAY_FORCECAST`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_FORCECAST "NPY_ARRAY_FORCECAST")
, and [`NPY_ARRAY_ENSUREARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "NPY_ARRAY_ENSUREARRAY")
. Standard combinations of flags can also be used:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FROM\_OT([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_OT "Link to this definition")
  

Similar to [`PyArray_FROM_O`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_O "PyArray_FROM_O")
 except it can take an argument of _typenum_ specifying the type-number the returned array.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FROM\_OTF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, int typenum, int requirements)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_OTF "Link to this definition")
  

Combination of [`PyArray_FROM_OF`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_OF "PyArray_FROM_OF")
 and [`PyArray_FROM_OT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROM_OT "PyArray_FROM_OT")
 allowing both a _typenum_ and a _flags_ argument to be provided.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_FROMANY([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, int typenum, int min, int max, int requirements)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FROMANY "Link to this definition")
  

Similar to [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 except the data-type is specified using a typenumber. [`PyArray_DescrFromType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromType "PyArray_DescrFromType")
 (_typenum_) is passed directly to [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
. This macro also adds [`NPY_ARRAY_DEFAULT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_DEFAULT "NPY_ARRAY_DEFAULT")
 to requirements if [`NPY_ARRAY_ENSURECOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSURECOPY "NPY_ARRAY_ENSURECOPY")
 is passed in as requirements.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_CheckAxis([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, int \*axis, int requirements)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckAxis "Link to this definition")
  

Encapsulate the functionality of functions and methods that take the axis= keyword and work properly with None as the axis argument. The input array is `obj`, while `*axis` is a converted integer (so that `*axis == NPY_RAVEL_AXIS` is the None value), and `requirements` gives the needed properties of `obj`. The output is a converted version of the input so that requirements are met and if needed a flattening has occurred. On output negative values of `*axis` are converted and the new value is checked to ensure consistency with the shape of `obj`.

Dealing with types[#](https://numpy.org/doc/stable/reference/c-api/array.html#dealing-with-types "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

### General check of Python Type[#](https://numpy.org/doc/stable/reference/c-api/array.html#general-check-of-python-type "Link to this heading")

int PyArray\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Check "Link to this definition")
  

Evaluates true if _op_ is a Python object whose type is a sub-type of [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
.

int PyArray\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckExact "Link to this definition")
  

Evaluates true if _op_ is a Python object with type [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
.

int PyArray\_HasArrayInterface([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_HasArrayInterface "Link to this definition")
  

If `op` implements any part of the array interface, then `out` will contain a new reference to the newly created ndarray using the interface or `out` will contain `NULL` if an error during conversion occurs. Otherwise, out will contain a borrowed reference to [`Py_NotImplemented`](https://docs.python.org/3/c-api/object.html#c.Py_NotImplemented "(in Python v3.14)")
 and no error condition is set.

int PyArray\_HasArrayInterfaceType([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*context, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_HasArrayInterfaceType "Link to this definition")
  

If `op` implements any part of the array interface, then `out` will contain a new reference to the newly created ndarray using the interface or `out` will contain `NULL` if an error during conversion occurs. Otherwise, out will contain a borrowed reference to Py\_NotImplemented and no error condition is set. This version allows setting of the dtype in the part of the array interface that looks for the [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
 attribute. _context_ is unused.

int PyArray\_IsZeroDim([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsZeroDim "Link to this definition")
  

Evaluates true if _op_ is an instance of (a subclass of) [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 and has 0 dimensions.

PyArray\_IsScalar(op, cls)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsScalar "Link to this definition")
  

Evaluates true if _op_ is an instance of `Py{cls}ArrType_Type`.

int PyArray\_CheckScalar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckScalar "Link to this definition")
  

Evaluates true if _op_ is either an array scalar (an instance of a sub-type of [`PyGenericArrType_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyGenericArrType_Type "PyGenericArrType_Type")
 ), or an instance of (a sub-class of) [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 whose dimensionality is 0.

int PyArray\_IsPythonNumber([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsPythonNumber "Link to this definition")
  

Evaluates true if _op_ is an instance of a builtin numeric type (int, float, complex, long, bool)

int PyArray\_IsPythonScalar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsPythonScalar "Link to this definition")
  

Evaluates true if _op_ is a builtin Python scalar object (int, float, complex, bytes, str, long, bool).

int PyArray\_IsAnyScalar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsAnyScalar "Link to this definition")
  

Evaluates true if _op_ is either a Python scalar object (see [`PyArray_IsPythonScalar`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsPythonScalar "PyArray_IsPythonScalar")
) or an array scalar (an instance of a sub- type of [`PyGenericArrType_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyGenericArrType_Type "PyGenericArrType_Type")
 ).

int PyArray\_CheckAnyScalar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckAnyScalar "Link to this definition")
  

Evaluates true if _op_ is a Python scalar object (see [`PyArray_IsPythonScalar`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IsPythonScalar "PyArray_IsPythonScalar")
), an array scalar (an instance of a sub-type of [`PyGenericArrType_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyGenericArrType_Type "PyGenericArrType_Type")
) or an instance of a sub-type of [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 whose dimensionality is 0.

### Data-type accessors[#](https://numpy.org/doc/stable/reference/c-api/array.html#data-type-accessors "Link to this heading")

Some of the descriptor attributes may not always be defined and should or cannot not be accessed directly.

Changed in version 2.0: Prior to NumPy 2.0 the ABI was different but unnecessary large for user DTypes. These accessors were all added in 2.0 and can be backported (see [The PyArray\_Descr struct has been changed](https://numpy.org/doc/stable/numpy_2_0_migration_guide.html#migration-c-descr)
).

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyDataType\_ELSIZE([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ELSIZE "Link to this definition")
  

The element size of the datatype (`itemsize` in Python).

Note

If the `descr` is attached to an array `PyArray_ITEMSIZE(arr)` can be used and is available on all NumPy versions.

void PyDataType\_SET\_ELSIZE([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 size)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_SET_ELSIZE "Link to this definition")
  

Allows setting of the itemsize, this is _only_ relevant for string/bytes datatypes as it is the current pattern to define one with a new size.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 PyDataType\_ALIGNMENT([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ALIGNMENT "Link to this definition")
  

The alignment of the datatype.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyDataType\_METADATA([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_METADATA "Link to this definition")
  

The Metadata attached to a dtype, either `NULL` or a dictionary.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyDataType\_NAMES([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_NAMES "Link to this definition")
  

`NULL` or a tuple of structured field names attached to a dtype.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyDataType\_FIELDS([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_FIELDS "Link to this definition")
  

`NULL`, `None`, or a dict of structured dtype fields, this dict must not be mutated, NumPy may change the way fields are stored in the future.

This is the same dict as returned by _np.dtype.fields_.

[NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")
 \*PyDataType\_C\_METADATA([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_C_METADATA "Link to this definition")
  

C-metadata object attached to a descriptor. This accessor should not be needed usually. The C-Metadata field does provide access to the datetime/timedelta time unit information.

[PyArray\_ArrayDescr](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_SUBARRAY.PyArray_ArrayDescr "PyArray_ArrayDescr")
 \*PyDataType\_SUBARRAY([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_SUBARRAY "Link to this definition")
  

Information about a subarray dtype equivalent to the Python _np.dtype.base_ and _np.dtype.shape_.

If this is non- `NULL`, then this data-type descriptor is a C-style contiguous array of another data-type descriptor. In other-words, each element that this descriptor describes is actually an array of some other base descriptor. This is most useful as the data-type descriptor for a field in another data-type descriptor. The fields member should be `NULL` if this is non- `NULL` (the fields member of the base descriptor can be non- `NULL` however).

type PyArray\_ArrayDescr[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_SUBARRAY.PyArray_ArrayDescr "Link to this definition")
  

typedef struct {
    PyArray\_Descr \*base;
    PyObject \*shape;
} PyArray\_ArrayDescr;

Copy to clipboard

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*base[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_SUBARRAY.PyArray_ArrayDescr.base "Link to this definition")
  

The data-type-descriptor object of the base-type.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*shape[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_SUBARRAY.PyArray_ArrayDescr.shape "Link to this definition")
  

The shape (always C-style contiguous) of the sub-array as a Python tuple.

char PyDataType\_TYPE([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_TYPE "Link to this definition")
  

New in version 2.5.

Data type character code. See [`numpy.dtype.char`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.char.html#numpy.dtype.char "numpy.dtype.char")
. Only set for built-in and legacy user DTypes. Null character (`b'\x00'`) otherwise.

char PyDataType\_KIND([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_KIND "Link to this definition")
  

New in version 2.5.

Data type kind character code. See [`numpy.dtype.kind`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy.dtype.kind "numpy.dtype.kind")
. Only set for built-in and legacy user DTypes. Null character (`b'\x00`) otherwise.

char PyDataType\_BYTEORDER([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_BYTEORDER "Link to this definition")
  

New in version 2.5.

Data type bytorder character code. One of `'='` (native), `'<'` (little-endian), `'>'` (big-endian), or `'|'` (not applicable). See [`numpy.dtype.byteorder`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html#numpy.dtype.byteorder "numpy.dtype.byteorder")
.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*PyDataType\_TYPEOBJ([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_TYPEOBJ "Link to this definition")
  

New in version 2.5.

The type object for the scalar type. See the `typeobj` member of the `PyArray_Descr` struct. See [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 for a full description of the `PyArray_Descr` struct layout.

### Data-type checking[#](https://numpy.org/doc/stable/reference/c-api/array.html#data-type-checking "Link to this heading")

For the typenum macros, the argument is an integer representing an enumerated array data type. For the array type checking macros the argument must be a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
\* that can be directly interpreted as a [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
\*.

int PyTypeNum\_ISUNSIGNED(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISUNSIGNED "Link to this definition")
  

int PyDataType\_ISUNSIGNED([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISUNSIGNED "Link to this definition")
  

int PyArray\_ISUNSIGNED([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISUNSIGNED "Link to this definition")
  

Type represents an unsigned integer.

int PyTypeNum\_ISSIGNED(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISSIGNED "Link to this definition")
  

int PyDataType\_ISSIGNED([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISSIGNED "Link to this definition")
  

int PyArray\_ISSIGNED([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISSIGNED "Link to this definition")
  

Type represents a signed integer.

int PyTypeNum\_ISINTEGER(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISINTEGER "Link to this definition")
  

int PyDataType\_ISINTEGER([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISINTEGER "Link to this definition")
  

int PyArray\_ISINTEGER([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISINTEGER "Link to this definition")
  

Type represents any integer.

int PyTypeNum\_ISFLOAT(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISFLOAT "Link to this definition")
  

int PyDataType\_ISFLOAT([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISFLOAT "Link to this definition")
  

int PyArray\_ISFLOAT([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISFLOAT "Link to this definition")
  

Type represents any floating point number.

int PyTypeNum\_ISCOMPLEX(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISCOMPLEX "Link to this definition")
  

int PyDataType\_ISCOMPLEX([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISCOMPLEX "Link to this definition")
  

int PyArray\_ISCOMPLEX([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISCOMPLEX "Link to this definition")
  

Type represents any complex floating point number.

int PyTypeNum\_ISNUMBER(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISNUMBER "Link to this definition")
  

int PyDataType\_ISNUMBER([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISNUMBER "Link to this definition")
  

int PyArray\_ISNUMBER([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISNUMBER "Link to this definition")
  

Type represents any integer, floating point, or complex floating point number.

int PyTypeNum\_ISSTRING(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISSTRING "Link to this definition")
  

int PyDataType\_ISSTRING([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISSTRING "Link to this definition")
  

int PyArray\_ISSTRING([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISSTRING "Link to this definition")
  

Type represents a string data type.

int PyTypeNum\_ISFLEXIBLE(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISFLEXIBLE "Link to this definition")
  

int PyDataType\_ISFLEXIBLE([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISFLEXIBLE "Link to this definition")
  

int PyArray\_ISFLEXIBLE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISFLEXIBLE "Link to this definition")
  

Type represents one of the flexible array types ( [`NPY_STRING`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_STRING "NPY_STRING")
, [`NPY_UNICODE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UNICODE "NPY_UNICODE")
, or [`NPY_VOID`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_VOID "NPY_VOID")
 ).

int PyDataType\_ISUNSIZED([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISUNSIZED "Link to this definition")
  

Type has no size information attached, and can be resized. Should only be called on flexible dtypes. Types that are attached to an array will always be sized, hence the array form of this macro not existing.

For structured datatypes with no fields this function now returns False.

int PyTypeNum\_ISUSERDEF(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISUSERDEF "Link to this definition")
  

int PyDataType\_ISUSERDEF([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISUSERDEF "Link to this definition")
  

int PyArray\_ISUSERDEF([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISUSERDEF "Link to this definition")
  

Type represents a user-defined type.

int PyTypeNum\_ISEXTENDED(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISEXTENDED "Link to this definition")
  

int PyDataType\_ISEXTENDED([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISEXTENDED "Link to this definition")
  

int PyArray\_ISEXTENDED([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISEXTENDED "Link to this definition")
  

Type is either flexible or user-defined.

int PyTypeNum\_ISOBJECT(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISOBJECT "Link to this definition")
  

int PyDataType\_ISOBJECT([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISOBJECT "Link to this definition")
  

int PyArray\_ISOBJECT([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISOBJECT "Link to this definition")
  

Type represents object data type.

int PyTypeNum\_ISBOOL(int num)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyTypeNum_ISBOOL "Link to this definition")
  

int PyDataType\_ISBOOL([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ISBOOL "Link to this definition")
  

int PyArray\_ISBOOL([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISBOOL "Link to this definition")
  

Type represents Boolean data type.

int PyDataType\_HASFIELDS([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_HASFIELDS "Link to this definition")
  

int PyArray\_HASFIELDS([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_HASFIELDS "Link to this definition")
  

Type has fields associated with it.

int PyArray\_ISNOTSWAPPED([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*m)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISNOTSWAPPED "Link to this definition")
  

Evaluates true if the data area of the ndarray _m_ is in machine byte-order according to the array’s data-type descriptor.

int PyArray\_ISBYTESWAPPED([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*m)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISBYTESWAPPED "Link to this definition")
  

Evaluates true if the data area of the ndarray _m_ is **not** in machine byte-order according to the array’s data-type descriptor.

[npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 PyArray\_EquivTypes([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*type1, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*type2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EquivTypes "Link to this definition")
  

Return [`NPY_TRUE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "NPY_TRUE")
 if _type1_ and _type2_ actually represent equivalent types for this platform (the fortran member of each type is ignored). For example, on 32-bit platforms, [`NPY_LONG`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONG "NPY_LONG")
 and [`NPY_INT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT "NPY_INT")
 are equivalent. Otherwise return [`NPY_FALSE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FALSE "NPY_FALSE")
.

[npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 PyArray\_EquivArrTypes([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*a1, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*a2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EquivArrTypes "Link to this definition")
  

Return [`NPY_TRUE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "NPY_TRUE")
 if _a1_ and _a2_ are arrays with equivalent types for this platform.

[npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 PyArray\_EquivTypenums(int typenum1, int typenum2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EquivTypenums "Link to this definition")
  

Special case of [`PyArray_EquivTypes`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EquivTypes "PyArray_EquivTypes")
 (…) that does not accept flexible data types but may be easier to call.

int PyArray\_EquivByteorders(int b1, int b2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EquivByteorders "Link to this definition")
  

True if byteorder characters _b1_ and _b2_ ( [`NPY_LITTLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_LITTLE "NPY_LITTLE")
, [`NPY_BIG`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BIG "NPY_BIG")
, [`NPY_NATIVE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_NATIVE "NPY_NATIVE")
, [`NPY_IGNORE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_IGNORE "NPY_IGNORE")
 ) are either equal or equivalent as to their specification of a native byte order. Thus, on a little-endian machine [`NPY_LITTLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_LITTLE "NPY_LITTLE")
 and [`NPY_NATIVE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_NATIVE "NPY_NATIVE")
 are equivalent where they are not equivalent on a big-endian machine.

### Converting data types[#](https://numpy.org/doc/stable/reference/c-api/array.html#converting-data-types "Link to this heading")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Cast([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Cast "Link to this definition")
  

Mainly for backwards compatibility to the Numeric C-API and for simple casts to non-flexible types. Return a new array object with the elements of _arr_ cast to the data-type _typenum_ which must be one of the enumerated types and not a flexible type.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_CastToType([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*type, int fortran)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CastToType "Link to this definition")
  

Return a new array of the _type_ specified, casting the elements of _arr_ as appropriate. The fortran argument specifies the ordering of the output array.

int PyArray\_CastTo([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*out, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*in)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CastTo "Link to this definition")
  

As of 1.6, this function simply calls [`PyArray_CopyInto`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CopyInto "PyArray_CopyInto")
, which handles the casting.

Cast the elements of the array _in_ into the array _out_. The output array should be writeable, have an integer-multiple of the number of elements in the input array (more than one copy can be placed in out), and have a data type that is one of the builtin types. Returns 0 on success and -1 if an error occurs.

int PyArray\_CanCastSafely(int fromtype, int totype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCastSafely "Link to this definition")
  

Returns non-zero if an array of data type _fromtype_ can be cast to an array of data type _totype_ without losing information. An exception is that 64-bit integers are allowed to be cast to 64-bit floating point values even though this can lose precision on large integers so as not to proliferate the use of long doubles without explicit requests. Flexible array types are not checked according to their lengths with this function.

int PyArray\_CanCastTo([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*fromtype, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*totype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCastTo "Link to this definition")
  

[`PyArray_CanCastTypeTo`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCastTypeTo "PyArray_CanCastTypeTo")
 supersedes this function in NumPy 1.6 and later.

Equivalent to PyArray\_CanCastTypeTo(fromtype, totype, NPY\_SAFE\_CASTING).

int PyArray\_CanCastTypeTo([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*fromtype, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*totype, [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")
 casting)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCastTypeTo "Link to this definition")
  

Returns non-zero if an array of data type _fromtype_ (which can include flexible types) can be cast safely to an array of data type _totype_ (which can include flexible types) according to the casting rule _casting_. For simple types with [`NPY_SAFE_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_SAFE_CASTING "NPY_SAFE_CASTING")
, this is basically a wrapper around [`PyArray_CanCastSafely`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCastSafely "PyArray_CanCastSafely")
, but for flexible types such as strings or unicode, it produces results taking into account their sizes. Integer and float types can only be cast to a string or unicode type using [`NPY_SAFE_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_SAFE_CASTING "NPY_SAFE_CASTING")
 if the string or unicode type is big enough to hold the max value of the integer/float type being cast from.

int PyArray\_CanCastArrayTo([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*totype, [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")
 casting)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCastArrayTo "Link to this definition")
  

Returns non-zero if _arr_ can be cast to _totype_ according to the casting rule given in _casting_. If _arr_ is an array scalar, its value is taken into account, and non-zero is also returned when the value will not overflow or be truncated to an integer when converting to a smaller type.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*PyArray\_MinScalarType([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MinScalarType "Link to this definition")
  

Note

With the adoption of NEP 50 in NumPy 2, this function is not used internally. It is currently provided for backwards compatibility, but expected to be eventually deprecated.

If _arr_ is an array, returns its data type descriptor, but if _arr_ is an array scalar (has 0 dimensions), it finds the data type of smallest size to which the value may be converted without overflow or truncation to an integer.

This function will not demote complex to float or anything to boolean, but will demote a signed integer to an unsigned integer when the scalar value is positive.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*PyArray\_PromoteTypes([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*type1, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*type2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_PromoteTypes "Link to this definition")
  

Finds the data type of smallest size and kind to which _type1_ and _type2_ may be safely converted. This function is symmetric and associative. A string or unicode result will be the proper size for storing the max value of the input types converted to a string or unicode.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*PyArray\_ResultType([npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 narrs, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*\*arrs, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 ndtypes, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*\*dtypes)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResultType "Link to this definition")
  

This applies type promotion to all the input arrays and dtype objects, using the NumPy rules for combining scalars and arrays, to determine the output type for an operation with the given set of operands. This is the same result type that ufuncs produce.

See the documentation of [`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
 for more detail about the type promotion algorithm.

int PyArray\_ObjectType([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, int mintype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ObjectType "Link to this definition")
  

This function is superseded by [`PyArray_ResultType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResultType "PyArray_ResultType")
.

This function is useful for determining a common type that two or more arrays can be converted to. It only works for non-flexible array types as no itemsize information is passed. The _mintype_ argument represents the minimum type acceptable, and _op_ represents the object that will be converted to an array. The return value is the enumerated typenumber that represents the data-type that _op_ should have.

[PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*\*PyArray\_ConvertToCommonType([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, int \*n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ConvertToCommonType "Link to this definition")
  

The functionality this provides is largely superseded by iterator [`NpyIter`](https://numpy.org/doc/stable/reference/c-api/iterator.html#c.NpyIter "NpyIter")
 introduced in 1.6, with flag [`NPY_ITER_COMMON_DTYPE`](https://numpy.org/doc/stable/reference/c-api/iterator.html#c.NPY_ITER_COMMON_DTYPE "NPY_ITER_COMMON_DTYPE")
 or with the same dtype parameter for all operands.

Convert a sequence of Python objects contained in _op_ to an array of ndarrays each having the same data type. The type is selected in the same way as [`PyArray_ResultType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResultType "PyArray_ResultType")
. The length of the sequence is returned in _n_, and an _n_ -length array of [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 pointers is the return value (or `NULL` if an error occurs). The returned array must be freed by the caller of this routine (using [`PyDataMem_FREE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_FREE "PyDataMem_FREE")
 ) and all the array objects in it `DECREF` ‘d or a memory-leak will occur. The example template-code below shows a typical usage:

mps \= PyArray\_ConvertToCommonType(obj, &n);
if (mps\==NULL) return NULL;
{code}
<before return\>
for (i\=0; i<n; i++) Py\_DECREF(mps\[i\]);
PyDataMem\_FREE(mps);
{return}

Copy to clipboard

char \*PyArray\_Zero([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Zero "Link to this definition")
  

A pointer to newly created memory of size _arr_ ->itemsize that holds the representation of 0 for that type. The returned pointer, _ret_, **must be freed** using [`PyDataMem_FREE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_FREE "PyDataMem_FREE")
 (ret) when it is not needed anymore.

char \*PyArray\_One([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_One "Link to this definition")
  

A pointer to newly created memory of size _arr_ ->itemsize that holds the representation of 1 for that type. The returned pointer, _ret_, **must be freed** using [`PyDataMem_FREE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_FREE "PyDataMem_FREE")
 (ret) when it is not needed anymore.

int PyArray\_ValidType(int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ValidType "Link to this definition")
  

Returns [`NPY_TRUE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "NPY_TRUE")
 if _typenum_ represents a valid type-number (builtin or user-defined or character code). Otherwise, this function returns [`NPY_FALSE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FALSE "NPY_FALSE")
.

### User-defined data types[#](https://numpy.org/doc/stable/reference/c-api/array.html#user-defined-data-types "Link to this heading")

void PyArray\_InitArrFuncs([PyArray\_ArrFuncs](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs "PyArray_ArrFuncs")
 \*f)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_InitArrFuncs "Link to this definition")
  

Initialize all function pointers and members to `NULL`.

int PyArray\_RegisterDataType([PyArray\_DescrProto](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DescrProto "PyArray_DescrProto")
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterDataType "Link to this definition")
  

Note

As of NumPy 2.0 this API is considered legacy, the new DType API is more powerful and provides additional flexibility. The API may eventually be deprecated but support is continued for the time being.

**Compiling for NumPy 1.x and 2.x**

NumPy 2.x requires passing in a `PyArray_DescrProto` typed struct rather than a `PyArray_Descr`. This is necessary to allow changes. To allow code to run and compile on both 1.x and 2.x you need to change the type of your struct to `PyArray_DescrProto` and add:

/\* Allow compiling on NumPy 1.x \*/
#if NPY\_ABI\_VERSION < 0x02000000
#define PyArray\_DescrProto PyArray\_Descr
#endif

Copy to clipboard

for 1.x compatibility. Further, the struct will _not_ be the actual descriptor anymore, only it’s type number will be updated. After successful registration, you must thus fetch the actual dtype with:

int type\_num \= PyArray\_RegisterDataType(&my\_descr\_proto);
if (type\_num < 0) {
    /\* error \*/
}
PyArray\_Descr \*my\_descr \= PyArray\_DescrFromType(type\_num);

Copy to clipboard

With these two changes, the code should compile and work on both 1.x and 2.x or later.

In the unlikely case that you are heap allocating the dtype struct you should free it again on NumPy 2, since a copy is made. The struct is not a valid Python object, so do not use `Py_DECREF` on it.

**Transitioning to the new DType API**

Users currently using the old DType API may not be able to easily transition due to NumPy issues that would cause regressions. While new DTypes may reasonably limit themselves to newer NumPy versions, existing DTypes cannot do so.

You can transition to the new DType API by using the [`NPY_DT_legacy_descriptor_proto`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_legacy_descriptor_proto "NPY_DT_legacy_descriptor_proto")
 slot when registering. This slot is available when compiling with NumPy 2.5 and provides support for NumPy 2.0 and higher (it can also be vendored to compile on older versions of NumPy).

Register a data-type as a new user-defined data type for arrays. The type must have most of its entries filled in. This is not always checked and errors can produce segfaults. In particular, the typeobj member of the `dtype` structure must be filled with a Python type that has a fixed-size element-size that corresponds to the elsize member of _dtype_. Also the `f` member must have the required functions: nonzero, copyswap, copyswapn, getitem, setitem, and cast (some of the cast functions may be `NULL` if no support is desired). To avoid confusion, you should choose a unique character typecode but this is not enforced and not relied on internally.

A user-defined type number is returned that uniquely identifies the type. A pointer to the new structure can then be obtained from [`PyArray_DescrFromType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromType "PyArray_DescrFromType")
 using the returned type number. A -1 is returned if an error occurs. If this _dtype_ has already been registered (checked only by the address of the pointer), then return the previously-assigned type-number.

The number of user DTypes known to numpy is stored in `NPY_NUMUSERTYPES`, a static global variable that is public in the C API. Accessing this symbol is inherently _not_ thread-safe. If for some reason you need to use this API in a multithreaded context, you will need to add your own locking, NumPy does not ensure new data types can be added in a thread-safe manner.

int PyArray\_RegisterCastFunc([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, int totype, [PyArray\_VectorUnaryFunc](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterCastFunc.PyArray_VectorUnaryFunc "PyArray_VectorUnaryFunc")
 \*castfunc)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterCastFunc "Link to this definition")
  

Register a low-level casting function, _castfunc_, to convert from the data-type, _descr_, to the given data-type number, _totype_. Any old casting function is over-written. A `0` is returned on success or a `-1` on failure.

Note

This function will eventually be deprecated. Please migrate to the new DType API for casts. See [`NPY_DT_legacy_descriptor_proto`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_legacy_descriptor_proto "NPY_DT_legacy_descriptor_proto")
 for details.

type PyArray\_VectorUnaryFunc[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterCastFunc.PyArray_VectorUnaryFunc "Link to this definition")
  

The function pointer type for low-level casting functions.

int PyArray\_RegisterCanCast([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, int totype, [NPY\_SCALARKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND "NPY_SCALARKIND")
 scalar)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterCanCast "Link to this definition")
  

Register the data-type number, _totype_, as castable from data-type object, _descr_, of the given _scalar_ kind. Use _scalar_ = [`NPY_NOSCALAR`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "NPY_NOSCALAR")
 to register that an array of data-type _descr_ can be cast safely to a data-type whose type\_number is _totype_. The return value is 0 on success or -1 on failure.

Note

This function will eventually be deprecated. Please migrate to the new DType API for casts. See [`NPY_DT_legacy_descriptor_proto`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_legacy_descriptor_proto "NPY_DT_legacy_descriptor_proto")
 for details. The new DType API provides more flexibility and speed even for dtypes compatible with the legacy API.

### Special functions for NPY\_OBJECT[#](https://numpy.org/doc/stable/reference/c-api/array.html#special-functions-for-npy-object "Link to this heading")

Warning

When working with arrays or buffers filled with objects NumPy tries to ensure such buffers are filled with `None` before any data may be read. However, code paths may existed where an array is only initialized to `NULL`. NumPy itself accepts `NULL` as an alias for `None`, but may `assert` non-`NULL` when compiled in debug mode.

Because NumPy is not yet consistent about initialization with None, users **must** expect a value of `NULL` when working with buffers created by NumPy. Users **should** also ensure to pass fully initialized buffers to NumPy, since NumPy may make this a strong requirement in the future.

There is currently an intention to ensure that NumPy always initializes object arrays before they may be read. Any failure to do so will be regarded as a bug. In the future, users may be able to rely on non-NULL values when reading from any array, although exceptions for writing to freshly created arrays may remain (e.g. for output arrays in ufunc code). As of NumPy 1.23 known code paths exists where proper filling is not done.

int PyArray\_INCREF([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_INCREF "Link to this definition")
  

Used for an array, _op_, that contains any Python objects. It increments the reference count of every object in the array according to the data-type of _op_. A -1 is returned if an error occurs, otherwise 0 is returned.

void PyArray\_Item\_INCREF(char \*ptr, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Item_INCREF "Link to this definition")
  

A function to INCREF all the objects at the location _ptr_ according to the data-type _dtype_. If _ptr_ is the start of a structured type with an object at any offset, then this will (recursively) increment the reference count of all object-like items in the structured type.

int PyArray\_XDECREF([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_XDECREF "Link to this definition")
  

Used for an array, _op_, that contains any Python objects. It decrements the reference count of every object in the array according to the data-type of _op_. Normal return value is 0. A -1 is returned if an error occurs.

void PyArray\_Item\_XDECREF(char \*ptr, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Item_XDECREF "Link to this definition")
  

A function to XDECREF all the object-like items at the location _ptr_ as recorded in the data-type, _dtype_. This works recursively so that if `dtype` itself has fields with data-types that contain object-like items, all the object-like fields will be XDECREF `'d`.

int PyArray\_SetWritebackIfCopyBase([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*base)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetWritebackIfCopyBase "Link to this definition")
  

Precondition: `arr` is a copy of `base` (though possibly with different strides, ordering, etc.) Sets the [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
 flag and `arr->base`, and set `base` to READONLY. Call [`PyArray_ResolveWritebackIfCopy`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "PyArray_ResolveWritebackIfCopy")
 before calling [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "(in Python v3.14)")
 in order to copy any changes back to `base` and reset the READONLY flag.

Returns 0 for success, -1 for failure.

Array flags[#](https://numpy.org/doc/stable/reference/c-api/array.html#array-flags "Link to this heading")

-----------------------------------------------------------------------------------------------------------

The `flags` attribute of the `PyArrayObject` structure contains important information about the memory used by the array (pointed to by the data member) This flag information must be kept accurate or strange results and even segfaults may result.

There are 6 (binary) flags that describe the memory area used by the data buffer. These constants are defined in `arrayobject.h` and determine the bit-position of the flag. Python exposes a nice attribute- based interface as well as a dictionary-like interface for getting (and, if appropriate, setting) these flags.

Memory areas of all kinds can be pointed to by an ndarray, necessitating these flags. If you get an arbitrary `PyArrayObject` in C-code, you need to be aware of the flags that are set. If you need to guarantee a certain kind of array (like [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 and [`NPY_ARRAY_BEHAVED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_BEHAVED "NPY_ARRAY_BEHAVED")
), then pass these requirements into the PyArray\_FromAny function.

In versions 1.6 and earlier of NumPy, the following flags did not have the \_ARRAY\_ macro namespace in them. That form of the constant names is deprecated in 1.7.

### Basic Array Flags[#](https://numpy.org/doc/stable/reference/c-api/array.html#basic-array-flags "Link to this heading")

An ndarray can have a data segment that is not a simple contiguous chunk of well-behaved memory you can manipulate. It may not be aligned with word boundaries (very important on some platforms). It might have its data in a different byte-order than the machine recognizes. It might not be writeable. It might be in Fortran-contiguous order. The array flags are used to indicate what can be said about data associated with an array.

NPY\_ARRAY\_C\_CONTIGUOUS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "Link to this definition")
  

The data area is in C-style contiguous order (last index varies the fastest).

NPY\_ARRAY\_F\_CONTIGUOUS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "Link to this definition")
  

The data area is in Fortran-style contiguous order (first index varies the fastest).

Note

Arrays can be both C-style and Fortran-style contiguous simultaneously. This is clear for 1-dimensional arrays, but can also be true for higher dimensional arrays.

Even for contiguous arrays a stride for a given dimension `arr.strides[dim]` may be _arbitrary_ if `arr.shape[dim] == 1` or the array has no elements. It does _not_ generally hold that `self.strides[-1] == self.itemsize` for C-style contiguous arrays or `self.strides[0] == self.itemsize` for Fortran-style contiguous arrays is true. The correct way to access the `itemsize` of an array from the C API is `PyArray_ITEMSIZE(arr)`.

See also

[Internal memory layout of an ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray)

NPY\_ARRAY\_OWNDATA[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_OWNDATA "Link to this definition")
  

The data area is owned by this array. Should never be set manually, instead create a `PyObject` wrapping the data and set the array’s base to that object. For an example, see the test in `test_mem_policy`.

NPY\_ARRAY\_ALIGNED[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "Link to this definition")
  

The data area and all array elements are aligned appropriately.

NPY\_ARRAY\_WRITEABLE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "Link to this definition")
  

The data area can be written to.

Notice that the above 3 flags are defined so that a new, well- behaved array has these flags defined as true.

NPY\_ARRAY\_WRITEBACKIFCOPY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "Link to this definition")
  

The data area represents a (well-behaved) copy whose information should be transferred back to the original when [`PyArray_ResolveWritebackIfCopy`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "PyArray_ResolveWritebackIfCopy")
 is called.

This is a special flag that is set if this array represents a copy made because a user required certain flags in [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 and a copy had to be made of some other array (and the user asked for this flag to be set in such a situation). The base attribute then points to the “misbehaved” array (which is set read\_only). [`PyArray_ResolveWritebackIfCopy`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "PyArray_ResolveWritebackIfCopy")
 will copy its contents back to the “misbehaved” array (casting if necessary) and will reset the “misbehaved” array to [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
. If the “misbehaved” array was not [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 to begin with then [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 would have returned an error because [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
 would not have been possible.

[`PyArray_UpdateFlags`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_UpdateFlags "PyArray_UpdateFlags")
 (obj, flags) will update the `obj->flags` for `flags` which can be any of [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
, [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
, [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
, or [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
.

### Combinations of array flags[#](https://numpy.org/doc/stable/reference/c-api/array.html#combinations-of-array-flags "Link to this heading")

NPY\_ARRAY\_BEHAVED[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_BEHAVED "Link to this definition")
  

[`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
 | [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")

NPY\_ARRAY\_CARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_CARRAY "Link to this definition")
  

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 | [`NPY_ARRAY_BEHAVED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_BEHAVED "NPY_ARRAY_BEHAVED")

NPY\_ARRAY\_CARRAY\_RO[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_CARRAY_RO "Link to this definition")
  

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

NPY\_ARRAY\_FARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_FARRAY "Link to this definition")
  

[`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 | [`NPY_ARRAY_BEHAVED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_BEHAVED "NPY_ARRAY_BEHAVED")

NPY\_ARRAY\_FARRAY\_RO[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_FARRAY_RO "Link to this definition")
  

[`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

NPY\_ARRAY\_DEFAULT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_DEFAULT "Link to this definition")
  

[`NPY_ARRAY_CARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_CARRAY "NPY_ARRAY_CARRAY")

NPY\_ARRAY\_IN\_ARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_IN_ARRAY "Link to this definition")
  

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

NPY\_ARRAY\_IN\_FARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_IN_FARRAY "Link to this definition")
  

[`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

NPY\_ARRAY\_OUT\_ARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_OUT_ARRAY "Link to this definition")
  

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 | [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

NPY\_ARRAY\_OUT\_FARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_OUT_FARRAY "Link to this definition")
  

[`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 | [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

NPY\_ARRAY\_INOUT\_ARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_INOUT_ARRAY "Link to this definition")
  

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 | [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
 | [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")

NPY\_ARRAY\_INOUT\_FARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_INOUT_FARRAY "Link to this definition")
  

[`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 | [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
 | [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")

NPY\_ARRAY\_UPDATE\_ALL[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_UPDATE_ALL "Link to this definition")
  

[`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 | [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 | [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")

### Flag-like constants[#](https://numpy.org/doc/stable/reference/c-api/array.html#flag-like-constants "Link to this heading")

These constants are used in [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")
 (and its macro forms) to specify desired properties of the new array.

NPY\_ARRAY\_FORCECAST[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_FORCECAST "Link to this definition")
  

Cast to the desired type, even if it can’t be done without losing information.

NPY\_ARRAY\_ENSURECOPY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSURECOPY "Link to this definition")
  

Make sure the resulting array is a copy of the original.

NPY\_ARRAY\_ENSUREARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "Link to this definition")
  

Make sure the resulting object is an actual ndarray, and not a sub-class.

These constants are used in [`PyArray_CheckFromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckFromAny "PyArray_CheckFromAny")
 (and its macro forms) to specify desired properties of the new array.

NPY\_ARRAY\_NOTSWAPPED[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "Link to this definition")
  

Make sure the returned array has a data-type descriptor that is in machine byte-order, over-riding any specification in the _dtype_ argument. Normally, the byte-order requirement is determined by the _dtype_ argument. If this flag is set and the dtype argument does not indicate a machine byte-order descriptor (or is NULL and the object is already an array with a data-type descriptor that is not in machine byte- order), then a new data-type descriptor is created and used with its byte-order field set to native.

NPY\_ARRAY\_BEHAVED\_NS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_BEHAVED_NS "Link to this definition")
  

[`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
 | [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 | [`NPY_ARRAY_NOTSWAPPED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "NPY_ARRAY_NOTSWAPPED")

NPY\_ARRAY\_ELEMENTSTRIDES[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ELEMENTSTRIDES "Link to this definition")
  

Make sure the returned array has strides that are multiples of the element size.

### Flag checking[#](https://numpy.org/doc/stable/reference/c-api/array.html#flag-checking "Link to this heading")

For all of these macros _arr_ must be an instance of a (subclass of) [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
.

int PyArray\_CHKFLAGS(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int flags)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CHKFLAGS "Link to this definition")
  

The first parameter, arr, must be an ndarray or subclass. The parameter, _flags_, should be an integer consisting of bitwise combinations of the possible flags an array can have: [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
, [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
, [`NPY_ARRAY_OWNDATA`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_OWNDATA "NPY_ARRAY_OWNDATA")
, [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
, [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
, [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
.

int PyArray\_IS\_C\_CONTIGUOUS(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IS_C_CONTIGUOUS "Link to this definition")
  

Evaluates true if _arr_ is C-style contiguous.

int PyArray\_IS\_F\_CONTIGUOUS(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IS_F_CONTIGUOUS "Link to this definition")
  

Evaluates true if _arr_ is Fortran-style contiguous.

int PyArray\_ISFORTRAN(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISFORTRAN "Link to this definition")
  

Evaluates true if _arr_ is Fortran-style contiguous and _not_ C-style contiguous. [`PyArray_IS_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IS_F_CONTIGUOUS "PyArray_IS_F_CONTIGUOUS")
 is the correct way to test for Fortran-style contiguity.

int PyArray\_ISWRITEABLE(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISWRITEABLE "Link to this definition")
  

Evaluates true if the data area of _arr_ can be written to

int PyArray\_ISALIGNED(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISALIGNED "Link to this definition")
  

Evaluates true if the data area of _arr_ is properly aligned on the machine.

int PyArray\_ISBEHAVED(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISBEHAVED "Link to this definition")
  

Evaluates true if the data area of _arr_ is aligned and writeable and in machine byte-order according to its descriptor.

int PyArray\_ISBEHAVED\_RO(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISBEHAVED_RO "Link to this definition")
  

Evaluates true if the data area of _arr_ is aligned and in machine byte-order.

int PyArray\_ISCARRAY(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISCARRAY "Link to this definition")
  

Evaluates true if the data area of _arr_ is C-style contiguous, and [`PyArray_ISBEHAVED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISBEHAVED "PyArray_ISBEHAVED")
 (_arr_) is true.

int PyArray\_ISFARRAY(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISFARRAY "Link to this definition")
  

Evaluates true if the data area of _arr_ is Fortran-style contiguous and [`PyArray_ISBEHAVED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISBEHAVED "PyArray_ISBEHAVED")
 (_arr_) is true.

int PyArray\_ISCARRAY\_RO(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISCARRAY_RO "Link to this definition")
  

Evaluates true if the data area of _arr_ is C-style contiguous, aligned, and in machine byte-order.

int PyArray\_ISFARRAY\_RO(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISFARRAY_RO "Link to this definition")
  

Evaluates true if the data area of _arr_ is Fortran-style contiguous, aligned, and in machine byte-order **.**

int PyArray\_ISONESEGMENT(const [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISONESEGMENT "Link to this definition")
  

Evaluates true if the data area of _arr_ consists of a single (C-style or Fortran-style) contiguous segment.

void PyArray\_UpdateFlags([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, int flagmask)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_UpdateFlags "Link to this definition")
  

The [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
, [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
, and [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 array flags can be “calculated” from the array object itself. This routine updates one or more of these flags of _arr_ as specified in _flagmask_ by performing the required calculation.

Warning

It is important to keep the flags updated (using [`PyArray_UpdateFlags`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_UpdateFlags "PyArray_UpdateFlags")
 can help) whenever a manipulation with an array is performed that might cause them to change. Later calculations in NumPy that rely on the state of these flags do not repeat the calculation to update them.

int PyArray\_FailUnlessWriteable([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*obj, const char \*name)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FailUnlessWriteable "Link to this definition")
  

This function does nothing and returns 0 if _obj_ is writeable. It raises an exception and returns -1 if _obj_ is not writeable. It may also do other house-keeping, such as issuing warnings on arrays which are transitioning to become views. Always call this function at some point before writing to an array.

_name_ is a name for the array, used to give better error messages. It can be something like “assignment destination”, “output array”, or even just “array”.

ArrayMethod API[#](https://numpy.org/doc/stable/reference/c-api/array.html#arraymethod-api "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

ArrayMethod loops are intended as a generic mechanism for writing loops over arrays, including ufunc loops and casts. The public API is defined in the `numpy/dtype_api.h` header. See [PyArrayMethod\_Context and PyArrayMethod\_Spec](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#arraymethod-structs)
 for documentation on the C structs exposed in the ArrayMethod API.

### Slots and Typedefs[#](https://numpy.org/doc/stable/reference/c-api/array.html#slots-and-typedefs "Link to this heading")

These are used to identify which kind of function an ArrayMethod slot implements. See [Slots and Typedefs](https://numpy.org/doc/stable/reference/c-api/array.html#arraymethod-typedefs)
 below for documentation on the functions that must be implemented for each slot.

NPY\_METH\_resolve\_descriptors[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_resolve_descriptors "Link to this definition")
  

typedef [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")
 (PyArrayMethod\_ResolveDescriptors)(struct [PyArrayMethodObject\_tag](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethodObject_tag "PyArrayMethodObject_tag")
 \*method, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*const \*dtypes, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*const \*given\_descrs, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*\*loop\_descrs, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*view\_offset)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_ResolveDescriptors "Link to this definition")
  

The function used to set the descriptors for an operation based on the descriptors of the operands. For example, a ufunc operation with two input operands and one output operand that is called without `out` being set in the python API, `resolve_descriptors` will be passed the descriptors for the two operands and determine the correct descriptor to use for the output based on the output DType set for the ArrayMethod. If `out` is set, then the output descriptor would be passed in as well and should not be overridden.

The _method_ is a pointer to the underlying cast or ufunc loop. In the future we may expose this struct publicly but for now this is an opaque pointer and the method cannot be inspected. The _dtypes_ is an `nargs` length array of `PyArray_DTypeMeta` pointers, _given\_descrs_ is an `nargs` length array of input descriptor instances (output descriptors may be NULL if no output was provided by the user), and _loop\_descrs_ is an `nargs` length array of descriptors that must be filled in by the resolve descriptors implementation. _view\_offset_ is currently only interesting for casts and can normally be ignored. When a cast does not require any operation, this can be signalled by setting `view_offset` to 0. On error, you must return `(NPY_CASTING)-1` with an error set.

NPY\_METH\_strided\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_strided_loop "Link to this definition")
  

NPY\_METH\_contiguous\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_contiguous_loop "Link to this definition")
  

NPY\_METH\_unaligned\_strided\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_unaligned_strided_loop "Link to this definition")
  

NPY\_METH\_unaligned\_contiguous\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_unaligned_contiguous_loop "Link to this definition")
  

One dimensional strided loops implementing the behavior (either a ufunc or cast). In most cases, `NPY_METH_strided_loop` is the generic and only version that needs to be implemented. `NPY_METH_contiguous_loop` can be implemented additionally as a more light-weight/faster version and it is used when all inputs and outputs are contiguous.

To deal with possibly unaligned data, NumPy needs to be able to copy unaligned to aligned data. When implementing a new DType, the “cast” or copy for it needs to implement `NPY_METH_unaligned_strided_loop`. Unlike the normal versions, this loop must not assume that the data can be accessed in an aligned fashion. These loops must copy each value before accessing or storing:

type\_in in\_value;
type\_out out\_value
memcpy(&value, in\_data, sizeof(type\_in));
out\_value \= in\_value;
memcpy(out\_data, &out\_value, sizeof(type\_out)

Copy to clipboard

while a normal loop can just use:

\*(type\_out \*)out\_data \= \*(type\_in)in\_data;

Copy to clipboard

The unaligned loops are currently only used in casts and will never be picked in ufuncs (ufuncs create a temporary copy to ensure aligned inputs). These slot IDs are ignored when `NPY_METH_get_loop` is defined, where instead whichever loop returned by the `get_loop` function is used.

NPY\_METH\_contiguous\_indexed\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_contiguous_indexed_loop "Link to this definition")
  

A specialized inner-loop option to speed up common `ufunc.at` computations.

typedef int (PyArrayMethod\_StridedLoop)([PyArrayMethod\_Context](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context "PyArrayMethod_Context")
 \*context, char \*const \*data, const [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*dimensions, const [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*strides, [NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")
 \*auxdata)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_StridedLoop "Link to this definition")
  

An implementation of an ArrayMethod loop. All of the loop slot IDs listed above must provide a `PyArrayMethod_StridedLoop` implementation. The _context_ is a struct containing context for the loop operation - in particular the input descriptors. The _data_ are an array of pointers to the beginning of the input and output array buffers. The _dimensions_ are the loop dimensions for the operation. The _strides_ are an `nargs` length array of strides for each input. The _auxdata_ is an optional set of auxiliary data that can be passed in to the loop - helpful to turn on and off optional behavior or reduce boilerplate by allowing similar ufuncs to share loop implementations or to allocate space that is persistent over multiple strided loop calls.

NPY\_METH\_get\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_get_loop "Link to this definition")
  

Allows more fine-grained control over loop selection. Accepts an implementation of PyArrayMethod\_GetLoop, which in turn returns a strided loop implementation. If `NPY_METH_get_loop` is defined, the other loop slot IDs are ignored, if specified.

typedef int (PyArrayMethod\_GetLoop)([PyArrayMethod\_Context](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context "PyArrayMethod_Context")
 \*context, int aligned, int move\_references, const [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*strides, [PyArrayMethod\_StridedLoop](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_StridedLoop "PyArrayMethod_StridedLoop")
 \*\*out\_loop, [NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")
 \*\*out\_transferdata, [NPY\_ARRAYMETHOD\_FLAGS](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS "NPY_ARRAYMETHOD_FLAGS")
 \*flags);[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_GetLoop "Link to this definition")
  

Sets the loop to use for an operation at runtime. The _context_ is the runtime context for the operation. _aligned_ indicates whether the data access for the loop is aligned (1) or unaligned (0). _move\_references_ indicates whether embedded references in the data should be copied. _strides_ are the strides for the input array, _out\_loop_ is a pointer that must be filled in with a pointer to the loop implementation. _out\_transferdata_ can be optionally filled in to allow passing in extra user-defined context to an operation. _flags_ must be filled in with ArrayMethod flags relevant for the operation. This is for example necessary to indicate if the inner loop requires the Python GIL to be held.

NPY\_METH\_get\_reduction\_initial[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_get_reduction_initial "Link to this definition")
  

typedef int (PyArrayMethod\_GetReductionInitial)([PyArrayMethod\_Context](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context "PyArrayMethod_Context")
 \*context, [npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 reduction\_is\_empty, char \*initial)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_GetReductionInitial "Link to this definition")
  

Query an ArrayMethod for the initial value for use in reduction. The _context_ is the ArrayMethod context, mainly to access the input descriptors. _reduction\_is\_empty_ indicates whether the reduction is empty. When it is, the value returned may differ. In this case it is a “default” value that may differ from the “identity” value normally used. For example:

*   `0.0` is the default for `sum([])`. But `-0.0` is the correct identity otherwise as it preserves the sign for `sum([-0.0])`.
    
*   We use no identity for object, but return the default of `0` and `1` for the empty `sum([], dtype=np.object_)` and `prod([], dtype=np.object_)`. This allows `np.sum(np.array(["a", "b"], dtype=np.object_))` to work.
    
*   `-inf` or `INT_MIN` for `max` is an identity, but at least `INT_MIN` not a good _default_ when there are no items.
    

_initial_ is a pointer to the data for the initial value, which should be filled in. Returns -1, 0, or 1 indicating error, no initial value, and the initial value being successfully filled. Errors must not be given when no initial value is correct, since NumPy may call this even when it is not strictly necessary to do so.

### Flags[#](https://numpy.org/doc/stable/reference/c-api/array.html#flags "Link to this heading")

enum NPY\_ARRAYMETHOD\_FLAGS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS "Link to this definition")
  

These flags allow switching on and off custom runtime behavior for ArrayMethod loops. For example, if a ufunc cannot possibly trigger floating point errors, then the `NPY_METH_NO_FLOATINGPOINT_ERRORS` flag should be set on the ufunc when it is registered.

enumerator NPY\_METH\_REQUIRES\_PYAPI[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS.NPY_METH_REQUIRES_PYAPI "Link to this definition")
  

Indicates the method must hold the GIL. If this flag is not set, the GIL is released before the loop is called.

enumerator NPY\_METH\_NO\_FLOATINGPOINT\_ERRORS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS.NPY_METH_NO_FLOATINGPOINT_ERRORS "Link to this definition")
  

Indicates the method cannot generate floating errors, so checking for floating errors after the loop completes can be skipped.

enumerator NPY\_METH\_SUPPORTS\_UNALIGNED[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS.NPY_METH_SUPPORTS_UNALIGNED "Link to this definition")
  

Indicates the method supports unaligned access.

enumerator NPY\_METH\_IS\_REORDERABLE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS.NPY_METH_IS_REORDERABLE "Link to this definition")
  

Indicates that the result of applying the loop repeatedly (for example, in a reduction operation) does not depend on the order of application.

enumerator NPY\_METH\_RUNTIME\_FLAGS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS.NPY_METH_RUNTIME_FLAGS "Link to this definition")
  

The flags that can be changed at runtime.

### Typedefs[#](https://numpy.org/doc/stable/reference/c-api/array.html#typedefs "Link to this heading")

Typedefs for functions that users of the ArrayMethod API can implement are described below.

typedef int (PyArrayMethod\_TraverseLoop)(void \*traverse\_context, const [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, char \*data, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 size, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 stride, [NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")
 \*auxdata)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_TraverseLoop "Link to this definition")
  

A traverse loop working on a single array. This is similar to the general strided-loop function. This is designed for loops that need to visit every element of a single array.

Currently this is used for array clearing, via the `NPY_DT_get_clear_loop` DType API hook, and zero-filling, via the `NPY_DT_get_fill_zero_loop` DType API hook. These are most useful for handling arrays storing embedded references to python objects or heap-allocated data.

The _descr_ is the descriptor for the array, _data_ is a pointer to the array buffer, _size_ is the 1D size of the array buffer, _stride_ is the stride, and _auxdata_ is optional extra data for the loop.

The _traverse\_context_ is passed in because we may need to pass in Interpreter state or similar in the future, but we don’t want to pass in a full context (with pointers to dtypes, method, caller which all make no sense for a traverse function). We assume for now that this context can be just passed through in the future (for structured dtypes).

typedef int (PyArrayMethod\_GetTraverseLoop)(void \*traverse\_context, const [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr, int aligned, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 fixed\_stride, [PyArrayMethod\_TraverseLoop](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_TraverseLoop "PyArrayMethod_TraverseLoop")
 \*\*out\_loop, [NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")
 \*\*out\_auxdata, [NPY\_ARRAYMETHOD\_FLAGS](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS "NPY_ARRAYMETHOD_FLAGS")
 \*flags)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_GetTraverseLoop "Link to this definition")
  

Simplified get\_loop function specific to dtype traversal

It should set the flags needed for the traversal loop and set _out\_loop_ to the loop function, which must be a valid `PyArrayMethod_TraverseLoop` pointer. Currently this is used for zero-filling and clearing arrays storing embedded references.

### API Functions and Typedefs[#](https://numpy.org/doc/stable/reference/c-api/array.html#api-functions-and-typedefs "Link to this heading")

These functions are part of the main numpy array API and were added along with the rest of the ArrayMethod API.

int PyUFunc\_AddLoopFromSpec([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*ufunc, [PyArrayMethod\_Spec](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec "PyArrayMethod_Spec")
 \*spec)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_AddLoopFromSpec "Link to this definition")
  

Add loop directly to a ufunc from a given ArrayMethod spec. the main ufunc registration function. This adds a new implementation/loop to a ufunc. It replaces _PyUFunc\_RegisterLoopForType_.

type PyUFunc\_LoopSlot[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_LoopSlot "Link to this definition")
  

Structure used to add multiple loops to ufuncs from ArrayMethod specs. This is used in _PyUFunc\_AddLoopsFromSpecs_.

> struct PyUFunc\_LoopSlot[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_LoopSlot.PyUFunc_LoopSlot "Link to this definition")
>   
> 
> const char \*name[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_LoopSlot.PyUFunc_LoopSlot.name "Link to this definition")
>   
> 
> The name of the ufunc to add the loop to, in the form like that of entry points, `(module ':')? (object '.')* name`, with `numpy` the default module. Examples: `sin`, `strings.str_len`, `numpy.strings:str_len`. Note that some names are supported but do not directly correspond to ufuncs: `"sort"`, `"argsort"`, `"real"`, `"imag"`. (These do use ufunc-likes or even ufuncs internally.)
> 
> [PyArrayMethod\_Spec](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec "PyArrayMethod_Spec")
>  \*spec[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_LoopSlot.PyUFunc_LoopSlot.spec "Link to this definition")
>   
> 
> The ArrayMethod spec to use to create the loop.

int PyUFunc\_AddLoopsFromSpecs([PyUFunc\_LoopSlot](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_LoopSlot "PyUFunc_LoopSlot")
 \*slots)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_AddLoopsFromSpecs "Link to this definition")
  

New in version 2.4.

Add multiple loops to ufuncs from ArrayMethod specs. This also handles the registration of methods for the ufunc-like functions `sort` and `argsort` (see [Sorting and Argsorting](https://numpy.org/doc/stable/reference/c-api/array.html#array-methods-sorting)
 for details), as well as for the array attributes `.real` and `.imag` needed for user defined complex DTypes (with `"real"` and `"imag"` as names).

The `slots` argument must be a NULL-terminated array of _PyUFunc\_LoopSlot_ (see above), which give the name of the ufunc and spec needed to create the loop.

int PyUFunc\_AddPromoter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*ufunc, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*DType\_tuple, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*promoter)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_AddPromoter "Link to this definition")
  

Note that currently the output dtypes are always `NULL` unless they are also part of the signature. This is an implementation detail and could change in the future. However, in general promoters should not have a need for output dtypes. Register a new promoter for a ufunc. The first argument is the ufunc to register the promoter with. The second argument is a Python tuple containing DTypes or None matching the number of inputs and outputs for the ufuncs. The last argument is a promoter is a function stored in a PyCapsule. It is passed the operation and requested DType signatures and can mutate it to attempt a new search for a matching loop/promoter.

typedef int (PyArrayMethod\_PromoterFunction)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*ufunc, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*const op\_dtypes\[\], [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*const signature\[\], [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*new\_op\_dtypes\[\])[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_PromoterFunction "Link to this definition")
  

Type of the promoter function, which must be wrapped into a `PyCapsule` with name `"numpy._ufunc_promoter"`. It is passed the operation and requested DType signatures and can mutate the signatures to attempt a search for a new loop or promoter that can accomplish the operation by casting the inputs to the “promoted” DTypes.

> A promoter should honor `signature[]` (if set). A promoter must return `-1` on failure. A Python error may be set but is not required (a general error is set in either paths, although the original error is chained). A promoter must return `0` or `1` on success. NumPy normally checks that `new_op_dtypes` are different from `op_dtypes` to prevent recursion. This check is skipped if the promoter returns `1`, which allows the promoter to add a new loop (when adding a new loop, `new_op_dtypes` should be identical to `op_dtypes`).
> 
> Changed in version 2.5: After 2.5 a return of `1` indicates that the promoter was successful skipping a recursion protection step. This mainly allows the promoter to add new loop to the ufunc that must now match instead of the promoter itself. (Normally, a promoter must modify the DTypes help find the right loop.)

int PyUFunc\_GiveFloatingpointErrors(const char \*name, int fpe\_errors)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_GiveFloatingpointErrors "Link to this definition")
  

Checks for a floating point error after performing a floating point operation in a manner that takes into account the error signaling configured via [`numpy.errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
. Takes the name of the operation to use in the error message and an integer flag that is one of `NPY_FPE_DIVIDEBYZERO`, `NPY_FPE_OVERFLOW`, `NPY_FPE_UNDERFLOW`, `NPY_FPE_INVALID` to indicate which error to check for.

Returns -1 on failure (an error was raised) and 0 on success.

int PyUFunc\_AddWrappingLoop([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*ufunc\_obj, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*new\_dtypes\[\], [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*wrapped\_dtypes\[\], [PyArrayMethod\_TranslateGivenDescriptors](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_TranslateGivenDescriptors "PyArrayMethod_TranslateGivenDescriptors")
 \*translate\_given\_descrs, [PyArrayMethod\_TranslateLoopDescriptors](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_TranslateLoopDescriptors "PyArrayMethod_TranslateLoopDescriptors")
 \*translate\_loop\_descrs)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_AddWrappingLoop "Link to this definition")
  

Allows creating of a fairly lightweight wrapper around an existing ufunc loop. The idea is mainly for units, as this is currently slightly limited in that it enforces that you cannot use a loop from another ufunc.

typedef int (PyArrayMethod\_TranslateGivenDescriptors)(int nin, int nout, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*wrapped\_dtypes\[\], [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*given\_descrs\[\], [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*new\_descrs\[\]);[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_TranslateGivenDescriptors "Link to this definition")
  

The function to convert the given descriptors (passed in to `resolve_descriptors`) and translates them for the wrapped loop. The new descriptors MUST be viewable with the old ones, _NULL_ must be supported (for output arguments) and should normally be forwarded.

The output of of this function will be used to construct views of the arguments as if they were the translated dtypes and does not use a cast. This means this mechanism is mostly useful for DTypes that “wrap” another DType implementation. For example, a unit DType could use this to wrap an existing floating point DType without needing to re-implement low-level ufunc logic. In the unit example, `resolve_descriptors` would handle computing the output unit from the input unit.

typedef int (PyArrayMethod\_TranslateLoopDescriptors)(int nin, int nout, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*new\_dtypes\[\], [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*given\_descrs\[\], [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*original\_descrs\[\], [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*loop\_descrs\[\]);[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_TranslateLoopDescriptors "Link to this definition")
  

The function to convert the actual loop descriptors (as returned by the original _resolve\_descriptors_ function) to the ones the output array should use. This function must return “viewable” types, it must not mutate them in any form that would break the inner-loop logic. Does not need to support NULL.

#### Wrapping Loop Example[#](https://numpy.org/doc/stable/reference/c-api/array.html#wrapping-loop-example "Link to this heading")

Suppose you want to wrap the `float64` multiply implementation for a `WrappedDoubleDType`. You would add a wrapping loop like so:

PyArray\_DTypeMeta \*orig\_dtypes\[3\] \= {
    &WrappedDoubleDType, &WrappedDoubleDType, &WrappedDoubleDType};
PyArray\_DTypeMeta \*wrapped\_dtypes\[3\] \= {
     &PyArray\_Float64DType, &PyArray\_Float64DType, &PyArray\_Float64DType}

PyObject \*mod \= PyImport\_ImportModule("numpy");
if (mod \== NULL) {
    return \-1;
}
PyObject \*multiply \= PyObject\_GetAttrString(mod, "multiply");
Py\_DECREF(mod);

if (multiply \== NULL) {
    return \-1;
}

int res \= PyUFunc\_AddWrappingLoop(
    multiply, orig\_dtypes, wrapped\_dtypes, &translate\_given\_descrs
    &translate\_loop\_descrs);

Py\_DECREF(multiply);

Copy to clipboard

Note that this also requires two functions to be defined above this code:

static int
translate\_given\_descrs(int nin, int nout,
                       PyArray\_DTypeMeta \*NPY\_UNUSED(wrapped\_dtypes\[\]),
                       PyArray\_Descr \*given\_descrs\[\],
                       PyArray\_Descr \*new\_descrs\[\])
{
    for (int i \= 0; i < nin + nout; i++) {
        if (given\_descrs\[i\] \== NULL) {
            new\_descrs\[i\] \= NULL;
        }
        else {
            new\_descrs\[i\] \= PyArray\_DescrFromType(NPY\_DOUBLE);
        }
    }
    return 0;
}

static int
translate\_loop\_descrs(int nin, int NPY\_UNUSED(nout),
                      PyArray\_DTypeMeta \*NPY\_UNUSED(new\_dtypes\[\]),
                      PyArray\_Descr \*given\_descrs\[\],
                      PyArray\_Descr \*original\_descrs\[\],
                      PyArray\_Descr \*loop\_descrs\[\])
{
    // more complicated parametric DTypes may need to
    // to do additional checking, but we know the wrapped
    // DTypes \*have\* to be float64 for this example.
    loop\_descrs\[0\] \= PyArray\_DescrFromType(NPY\_FLOAT64);
    Py\_INCREF(loop\_descrs\[0\]);
    loop\_descrs\[1\] \= PyArray\_DescrFromType(NPY\_FLOAT64);
    Py\_INCREF(loop\_descrs\[1\]);
    loop\_descrs\[2\] \= PyArray\_DescrFromType(NPY\_FLOAT64);
    Py\_INCREF(loop\_descrs\[2\]);
}

Copy to clipboard

### Sorting and Argsorting[#](https://numpy.org/doc/stable/reference/c-api/array.html#sorting-and-argsorting "Link to this heading")

Sorting and argsorting methods for dtypes can be registered using the ArrayMethod API. This is done by adding an ArrayMethod spec with the name `"sort"` or `"argsort"` respectively. The spec must have `nin=1` and `nout=1` for both sort and argsort. Sorting is inplace, hence we enforce that `data[0] == data[1]`. Argsorting returns a new array of indices, so the output must be of `NPY_INTP` type.

The `context` passed to the loop contains the `parameters` field which for these operations is a `PyArrayMethod_SortParameters *` struct. This struct contains a `flags` field which is a bitwise OR of `NPY_SORTKIND` values indicating the kind of sort to perform (that is, whether it is a stable and/or descending sort). If the strided loop depends on the flags, a good way to deal with this is to define [`NPY_METH_get_loop`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_METH_get_loop "NPY_METH_get_loop")
, and not set any of the other loop slots.

struct PyArrayMethod\_SortParameters[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_SortParameters "Link to this definition")
  

[NPY\_SORTKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND "NPY_SORTKIND")
 flags[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayMethod_SortParameters.flags "Link to this definition")
  

The flags passed to the sort operation. This is a bitwise OR of `NPY_SORTKIND` values indicating the kind of sort to perform.

These specs can be registered using [`PyUFunc_AddLoopsFromSpecs`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyUFunc_AddLoopsFromSpecs "PyUFunc_AddLoopsFromSpecs")
 along with other ufunc loops.

API for calling array methods[#](https://numpy.org/doc/stable/reference/c-api/array.html#api-for-calling-array-methods "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

### Conversion[#](https://numpy.org/doc/stable/reference/c-api/array.html#conversion "Link to this heading")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_GetField([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int offset)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetField "Link to this definition")
  

Equivalent to [`ndarray.getfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.getfield.html#numpy.ndarray.getfield "numpy.ndarray.getfield")
 (_self_, _dtype_, _offset_). This function [steals a reference](https://docs.python.org/3/c-api/intro.html?reference-count-details)
 to [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 and returns a new array of the given _dtype_ using the data in the current array at a specified _offset_ in bytes. The _offset_ plus the itemsize of the new array type must be less than `self->descr->elsize` or an error is raised. The same shape and strides as the original array are used. Therefore, this function has the effect of returning a field from a structured array. But, it can also be used to select specific bytes or groups of bytes from any array type.

int PyArray\_SetField([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*val)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetField "Link to this definition")
  

Equivalent to [`ndarray.setfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setfield.html#numpy.ndarray.setfield "numpy.ndarray.setfield")
 (_self_, _val_, _dtype_, _offset_ ). Set the field starting at _offset_ in bytes and of the given _dtype_ to _val_. The _offset_ plus _dtype_ ->elsize must be less than _self_ ->descr->elsize or an error is raised. Otherwise, the _val_ argument is converted to an array and copied into the field pointed to. If necessary, the elements of _val_ are repeated to fill the destination array, But, the number of elements in the destination must be an integer multiple of the number of elements in _val_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Byteswap([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 inplace)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Byteswap "Link to this definition")
  

Equivalent to [`ndarray.byteswap`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.byteswap.html#numpy.ndarray.byteswap "numpy.ndarray.byteswap")
 (_self_, _inplace_). Return an array whose data area is byteswapped. If _inplace_ is non-zero, then do the byteswap inplace and return a reference to self. Otherwise, create a byteswapped copy and leave self unchanged.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_NewCopy([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*old, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 order)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NewCopy "Link to this definition")
  

Equivalent to [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")
 (_self_, _fortran_). Make a copy of the _old_ array. The returned array is always aligned and writeable with data interpreted the same as the old array. If _order_ is [`NPY_CORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_CORDER "NPY_CORDER")
, then a C-style contiguous array is returned. If _order_ is [`NPY_FORTRANORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_FORTRANORDER "NPY_FORTRANORDER")
, then a Fortran-style contiguous array is returned. If _order is_ [`NPY_ANYORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_ANYORDER "NPY_ANYORDER")
, then the array returned is Fortran-style contiguous only if the old one is; otherwise, it is C-style contiguous.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ToList([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ToList "Link to this definition")
  

Equivalent to [`ndarray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist "numpy.ndarray.tolist")
 (_self_). Return a nested Python list from _self_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ToString([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 order)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ToString "Link to this definition")
  

Equivalent to [`ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")
 (_self_, _order_). Return the bytes of this array in a Python string.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_ToFile([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, FILE \*fp, char \*sep, char \*format)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ToFile "Link to this definition")
  

Write the contents of _self_ to the file pointer _fp_ in C-style contiguous fashion. Write the data as binary bytes if _sep_ is the string “”or `NULL`. Otherwise, write the contents of _self_ as text using the _sep_ string as the item separator. Each item will be printed to the file. If the _format_ string is not `NULL` or “”, then it is a Python print statement format string showing how the items are to be written.

int PyArray\_Dump([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*file, int protocol)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Dump "Link to this definition")
  

Pickle the object in _self_ to the given _file_ (either a string or a Python file object). If _file_ is a Python string it is considered to be the name of a file which is then opened in binary mode. The given _protocol_ is used (if _protocol_ is negative, or the highest available is used). This is a simple wrapper around cPickle.dump(_self_, _file_, _protocol_).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Dumps([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*self, int protocol)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Dumps "Link to this definition")
  

Pickle the object in _self_ to a Python string and return it. Use the Pickle _protocol_ provided (or the highest available if _protocol_ is negative).

int PyArray\_FillWithScalar([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FillWithScalar "Link to this definition")
  

Fill the array, _arr_, with the given scalar object, _obj_. The object is first converted to the data type of _arr_, and then copied into every location. A -1 is returned if an error occurs, otherwise 0 is returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_View([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*ptype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_View "Link to this definition")
  

Equivalent to [`ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")
 (_self_, _dtype_). Return a new view of the array _self_ as possibly a different data-type, _dtype_, and different array subclass _ptype_.

If _dtype_ is `NULL`, then the returned array will have the same data type as _self_. The new data-type must be consistent with the size of _self_. Either the itemsizes must be identical, or _self_ must be single-segment and the total number of bytes must be the same. In the latter case the dimensions of the returned array will be altered in the last (or first for Fortran-style contiguous arrays) dimension. The data area of the returned array and self is exactly the same.

### Shape Manipulation[#](https://numpy.org/doc/stable/reference/c-api/array.html#shape-manipulation "Link to this heading")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Newshape([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyArray\_Dims](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims "PyArray_Dims")
 \*newshape, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 order)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Newshape "Link to this definition")
  

Result will be a new array (pointing to the same memory location as _self_ if possible), but having a shape given by _newshape_. If the new shape is not compatible with the strides of _self_, then a copy of the array with the new specified shape will be returned.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Reshape([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*shape)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Reshape "Link to this definition")
  

Equivalent to [`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")
 (_self_, _shape_) where _shape_ is a sequence. Converts _shape_ to a [`PyArray_Dims`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims "PyArray_Dims")
 structure and calls [`PyArray_Newshape`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Newshape "PyArray_Newshape")
 internally. For back-ward compatibility – Not recommended

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Squeeze([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Squeeze "Link to this definition")
  

Equivalent to [`ndarray.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.squeeze.html#numpy.ndarray.squeeze "numpy.ndarray.squeeze")
 (_self_). Return a new view of _self_ with all of the dimensions of length 1 removed from the shape.

Warning

matrix objects are always 2-dimensional. Therefore, [`PyArray_Squeeze`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Squeeze "PyArray_Squeeze")
 has no effect on arrays of matrix sub-class.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_SwapAxes([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, int a1, int a2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SwapAxes "Link to this definition")
  

Equivalent to [`ndarray.swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.swapaxes.html#numpy.ndarray.swapaxes "numpy.ndarray.swapaxes")
 (_self_, _a1_, _a2_). The returned array is a new view of the data in _self_ with the given axes, _a1_ and _a2_, swapped.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Resize([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyArray\_Dims](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims "PyArray_Dims")
 \*newshape, int refcheck, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 fortran)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Resize "Link to this definition")
  

Equivalent to [`ndarray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize")
 (_self_, _newshape_, _refcheck_). This function only works on single-segment arrays. It changes the shape of _self_ inplace and will reallocate the memory for _self_ if _newshape_ has a different total number of elements then the old shape. If reallocation is necessary, then _self_ must own its data, have _self_ - `>base==NULL`, have _self_ - `>weakrefs==NULL`, and (unless refcheck is 0) not be referenced by any other array. The _fortran_ argument has no effect.

On Python 3.13 and older, the check allows uniquely referenced objects and objects with exactly one reference to be reallocated in-place. On Python 3.14 and newer, the array must be uniquely referenced. See the Python 3.14 [What’s New entry](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-refcount)
 on this topic for more information on why there is a behavior difference.

Reallocating arrays in-place can often lead to memory fragmentation and should be avoided. If the goal is to reclaim over-allocated memory, alternatives are to create a view or a copy of just the desired data, or using two passes to build the array: one to cheaply determine the shape and another to allocate and fill. Benchmark your use case to determine what is optimum. You may be surprised to find `resize` actually slows down or bloats your application.

Returns None on success and NULL on error.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Transpose([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyArray\_Dims](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims "PyArray_Dims")
 \*permute)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Transpose "Link to this definition")
  

Equivalent to [`ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose")
 (_self_, _permute_). Permute the axes of the ndarray object _self_ according to the data structure _permute_ and return the result. If _permute_ is `NULL`, then the resulting array has its axes reversed. For example if _self_ has shape \\(10\\times20\\times30\\), and _permute_ `.ptr` is (0,2,1) the shape of the result is \\(10\\times30\\times20.\\) If _permute_ is `NULL`, the shape of the result is \\(30\\times20\\times10.\\)

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Flatten([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 order)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Flatten "Link to this definition")
  

Equivalent to [`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")
 (_self_, _order_). Return a 1-d copy of the array. If _order_ is [`NPY_FORTRANORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_FORTRANORDER "NPY_FORTRANORDER")
 the elements are scanned out in Fortran order (first-dimension varies the fastest). If _order_ is [`NPY_CORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_CORDER "NPY_CORDER")
, the elements of `self` are scanned in C-order (last dimension varies the fastest). If _order_ [`NPY_ANYORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_ANYORDER "NPY_ANYORDER")
, then the result of [`PyArray_ISFORTRAN`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ISFORTRAN "PyArray_ISFORTRAN")
 (_self_) is used to determine which order to flatten.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Ravel([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")
 order)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Ravel "Link to this definition")
  

Equivalent to _self_.ravel(_order_). Same basic functionality as [`PyArray_Flatten`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Flatten "PyArray_Flatten")
 (_self_, _order_) except if _order_ is 0 and _self_ is C-style contiguous, the shape is altered but no copy is performed.

### Item selection and manipulation[#](https://numpy.org/doc/stable/reference/c-api/array.html#item-selection-and-manipulation "Link to this heading")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_TakeFrom([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*indices, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*ret, [NPY\_CLIPMODE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")
 clipmode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_TakeFrom "Link to this definition")
  

Equivalent to [`ndarray.take`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "numpy.ndarray.take")
 (_self_, _indices_, _axis_, _ret_, _clipmode_) except _axis_ =None in Python is obtained by setting _axis_ = [`NPY_MAXDIMS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MAXDIMS "NPY_MAXDIMS")
 in C. Extract the items from self indicated by the integer-valued _indices_ along the given _axis._ The clipmode argument can be [`NPY_RAISE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_RAISE "NPY_RAISE")
, [`NPY_WRAP`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_WRAP "NPY_WRAP")
, or [`NPY_CLIP`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_CLIP "NPY_CLIP")
 to indicate what to do with out-of-bound indices. The _ret_ argument can specify an output array rather than having one created internally.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_PutTo([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*values, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*indices, [NPY\_CLIPMODE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")
 clipmode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_PutTo "Link to this definition")
  

Equivalent to _self_.put(_values_, _indices_, _clipmode_ ). Put _values_ into _self_ at the corresponding (flattened) _indices_. If _values_ is too small it will be repeated as necessary.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_PutMask([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*values, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*mask)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_PutMask "Link to this definition")
  

Place the _values_ in _self_ wherever corresponding positions (using a flattened context) in _mask_ are true. The _mask_ and _self_ arrays must have the same total number of elements. If _values_ is too small, it will be repeated as necessary.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Repeat([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, int axis)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Repeat "Link to this definition")
  

Equivalent to [`ndarray.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.repeat.html#numpy.ndarray.repeat "numpy.ndarray.repeat")
 (_self_, _op_, _axis_). Copy the elements of _self_, _op_ times along the given _axis_. Either _op_ is a scalar integer or a sequence of length _self_ ->dimensions\[ _axis_ \] indicating how many times to repeat each item along the axis.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyArray\_Choose([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*op, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*ret, [NPY\_CLIPMODE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")
 clipmode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Choose "Link to this definition")
  

Equivalent to [`ndarray.choose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.choose.html#numpy.ndarray.choose "numpy.ndarray.choose")
 (_self_, _op_, _ret_, _clipmode_). Create a new array by selecting elements from the sequence of arrays in _op_ based on the integer values in _self_. The arrays must all be broadcastable to the same shape and the entries in _self_ should be between 0 and len(_op_). The output is placed in _ret_ unless it is `NULL` in which case a new output is created. The _clipmode_ argument determines behavior for when entries in _self_ are not between 0 and len(_op_).

NPY\_RAISE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Choose.NPY_RAISE "Link to this definition")
  

raise a ValueError;

NPY\_WRAP[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Choose.NPY_WRAP "Link to this definition")
  

wrap values < 0 by adding len(_op_) and values >=len(_op_) by subtracting len(_op_) until they are in range;

NPY\_CLIP[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Choose.NPY_CLIP "Link to this definition")
  

all values are clipped to the region \[0, len(_op_) ).\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Sort([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [NPY\_SORTKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND "NPY_SORTKIND")\
 kind)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Sort "Link to this definition")\
  \
\
Return an array with the items of `self` sorted along `axis`. The array is sorted using an algorithm whose properties are specified by the value of `kind`, an integer/enum specifying the requirements of the sorting algorithm used. If `self* ->descr` is a data-type with fields defined, then `self->descr->names` is used to determine the sort order. A comparison where the first field is equal will use the second field and so on. To alter the sort order of a structured array, create a new data-type with a different order of names and construct a view of the array with that new data-type.\
\
This is the C level function called by the ndarray method [`ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")\
, though with a different meaning of `kind` – see `NPY_SORTKIND` below.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_ArgSort([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [NPY\_SORTKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND "NPY_SORTKIND")\
 kind)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArgSort "Link to this definition")\
  \
\
Return an array of indices such that selection of these indices along the given `axis` would return a sorted version of `self`. The array is sorted using an algorithm whose properties are specified by `kind`, an integer/enum specifying the requirements of the sorting algorithm used. If `self->descr` is a data-type with fields defined, then `self->descr->names` is used to determine the sort order. A comparison where the first field is equal will use the second field and so on. To alter the sort order of a structured array, create a new data-type with a different order of names and construct a view of the array with that new data-type.\
\
This is the C level function called by the ndarray method [`ndarray.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argsort.html#numpy.ndarray.argsort "numpy.ndarray.argsort")\
, though with a different meaning of `kind` – see `NPY_SORTKIND` below.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_LexSort([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*sort\_keys, int axis)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_LexSort "Link to this definition")\
  \
\
Given a sequence of arrays (_sort\_keys_) of the same shape, return an array of indices (similar to [`PyArray_ArgSort`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArgSort "PyArray_ArgSort")\
 (…)) that would sort the arrays lexicographically. A lexicographic sort specifies that when two keys are found to be equal, the order is based on comparison of subsequent keys. A merge sort (which leaves equal entries unmoved) is required to be defined for the types. The sort is accomplished by sorting the indices first using the first _sort\_key_ and then using the second _sort\_key_ and so forth. This is equivalent to the lexsort(_sort\_keys_, _axis_) Python command. Because of the way the merge-sort works, be sure to understand the order the _sort\_keys_ must be in (reversed from the order you would use when comparing two elements).\
\
If these arrays are all collected in a structured array, then [`PyArray_Sort`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Sort "PyArray_Sort")\
 (…) can also be used to sort the array directly.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_SearchSorted([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*values, [NPY\_SEARCHSIDE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE "NPY_SEARCHSIDE")\
 side, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*perm)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SearchSorted "Link to this definition")\
  \
\
Equivalent to [`ndarray.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.searchsorted.html#numpy.ndarray.searchsorted "numpy.ndarray.searchsorted")\
 (_self_, _values_, _side_, _perm_). Assuming _self_ is a 1-d array in ascending order, then the output is an array of indices the same shape as _values_ such that, if the elements in _values_ were inserted before the indices, the order of _self_ would be preserved. No checking is done on whether or not self is in ascending order.\
\
The _side_ argument indicates whether the index returned should be that of the first suitable location (if [`NPY_SEARCHLEFT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHLEFT "NPY_SEARCHLEFT")\
) or of the last (if [`NPY_SEARCHRIGHT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHRIGHT "NPY_SEARCHRIGHT")\
).\
\
The _sorter_ argument, if not `NULL`, must be a 1D array of integer indices the same length as _self_, that sorts it into ascending order. This is typically the result of a call to [`PyArray_ArgSort`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArgSort "PyArray_ArgSort")\
 (…) Binary search is used to find the required insertion points.\
\
int PyArray\_Partition([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*ktharray, int axis, [NPY\_SELECTKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SELECTKIND "NPY_SELECTKIND")\
 which)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Partition "Link to this definition")\
  \
\
Equivalent to [`ndarray.partition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.partition.html#numpy.ndarray.partition "numpy.ndarray.partition")\
 (_self_, _ktharray_, _axis_, _kind_). Partitions the array so that the values of the element indexed by _ktharray_ are in the positions they would be if the array is fully sorted and places all elements smaller than the kth before and all elements equal or greater after the kth element. The ordering of all elements within the partitions is undefined. If _self_\->descr is a data-type with fields defined, then self->descr->names is used to determine the sort order. A comparison where the first field is equal will use the second field and so on. To alter the sort order of a structured array, create a new data-type with a different order of names and construct a view of the array with that new data-type. Returns zero on success and -1 on failure.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_ArgPartition([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*op, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*ktharray, int axis, [NPY\_SELECTKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SELECTKIND "NPY_SELECTKIND")\
 which)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArgPartition "Link to this definition")\
  \
\
Equivalent to [`ndarray.argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argpartition.html#numpy.ndarray.argpartition "numpy.ndarray.argpartition")\
 (_self_, _ktharray_, _axis_, _kind_). Return an array of indices such that selection of these indices along the given `axis` would return a partitioned version of _self_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Diagonal([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int offset, int axis1, int axis2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Diagonal "Link to this definition")\
  \
\
Equivalent to [`ndarray.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.diagonal.html#numpy.ndarray.diagonal "numpy.ndarray.diagonal")\
 (_self_, _offset_, _axis1_, _axis2_ ). Return the _offset_ diagonals of the 2-d arrays defined by _axis1_ and _axis2_.\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 PyArray\_CountNonzero([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CountNonzero "Link to this definition")\
  \
\
Counts the number of non-zero elements in the array object _self_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Nonzero([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Nonzero "Link to this definition")\
  \
\
Equivalent to [`ndarray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero")\
 (_self_). Returns a tuple of index arrays that select elements of _self_ that are nonzero. If (nd= [`PyArray_NDIM`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NDIM "PyArray_NDIM")\
 ( `self` ))==1, then a single index array is returned. The index arrays have data type [`NPY_INTP`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INTP "NPY_INTP")\
. If a tuple is returned (nd \\(\\neq\\) 1), then its length is nd.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Compress([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*condition, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Compress "Link to this definition")\
  \
\
Equivalent to [`ndarray.compress`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.compress.html#numpy.ndarray.compress "numpy.ndarray.compress")\
 (_self_, _condition_, _axis_ ). Return the elements along _axis_ corresponding to elements of _condition_ that are true.\
\
### Calculation[#](https://numpy.org/doc/stable/reference/c-api/array.html#calculation "Link to this heading")\
\
Tip\
\
Pass in [`NPY_RAVEL_AXIS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_RAVEL_AXIS "NPY_RAVEL_AXIS")\
 for axis in order to achieve the same effect that is obtained by passing in `axis=None` in Python (treating the array as a 1-d array).\
\
Note\
\
The out argument specifies where to place the result. If out is NULL, then the output array is created, otherwise the output is placed in out which must be the correct size and type. A new reference to the output array is always returned even when out is not NULL. The caller of the routine has the responsibility to `Py_DECREF` out if not NULL or a memory-leak will occur.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_ArgMax([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArgMax "Link to this definition")\
  \
\
Equivalent to [`ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")\
 (_self_, _axis_). Return the index of the largest element of _self_ along _axis_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_ArgMin([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ArgMin "Link to this definition")\
  \
\
Equivalent to [`ndarray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "numpy.ndarray.argmin")\
 (_self_, _axis_). Return the index of the smallest element of _self_ along _axis_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Max([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Max "Link to this definition")\
  \
\
Equivalent to [`ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")\
 (_self_, _axis_). Returns the largest element of _self_ along the given _axis_. When the result is a single element, returns a numpy scalar instead of an ndarray.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Min([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Min "Link to this definition")\
  \
\
Equivalent to [`ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")\
 (_self_, _axis_). Return the smallest element of _self_ along the given _axis_. When the result is a single element, returns a numpy scalar instead of an ndarray.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Ptp([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Ptp "Link to this definition")\
  \
\
Return the difference between the largest element of _self_ along _axis_ and the smallest element of _self_ along _axis_. When the result is a single element, returns a numpy scalar instead of an ndarray.\
\
Note\
\
The rtype argument specifies the data-type the reduction should take place over. This is important if the data-type of the array is not “large” enough to handle the output. By default, all integer data-types are made at least as large as [`NPY_LONG`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONG "NPY_LONG")\
 for the “add” and “multiply” ufuncs (which form the basis for mean, sum, cumsum, prod, and cumprod functions).\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Mean([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Mean "Link to this definition")\
  \
\
Equivalent to [`ndarray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#numpy.ndarray.mean "numpy.ndarray.mean")\
 (_self_, _axis_, _rtype_). Returns the mean of the elements along the given _axis_, using the enumerated type _rtype_ as the data type to sum in. Default sum behavior is obtained using [`NPY_NOTYPE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_NOTYPE "NPY_NOTYPE")\
 for _rtype_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Trace([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int offset, int axis1, int axis2, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Trace "Link to this definition")\
  \
\
Equivalent to [`ndarray.trace`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.trace.html#numpy.ndarray.trace "numpy.ndarray.trace")\
 (_self_, _offset_, _axis1_, _axis2_, _rtype_). Return the sum (using _rtype_ as the data type of summation) over the _offset_ diagonal elements of the 2-d arrays defined by _axis1_ and _axis2_ variables. A positive offset chooses diagonals above the main diagonal. A negative offset selects diagonals below the main diagonal.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Clip([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*min, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*max)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Clip "Link to this definition")\
  \
\
Equivalent to [`ndarray.clip`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.clip.html#numpy.ndarray.clip "numpy.ndarray.clip")\
 (_self_, _min_, _max_). Clip an array, _self_, so that values larger than _max_ are fixed to _max_ and values less than _min_ are fixed to _min_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Conjugate([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Conjugate "Link to this definition")\
  \
\
Equivalent to [`ndarray.conjugate`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.conjugate.html#numpy.ndarray.conjugate "numpy.ndarray.conjugate")\
 (_self_). Return the complex conjugate of _self_. If _self_ is not of complex data type, then return _self_ with a reference.\
\
Parameters:\
\
*   **self** – Input array.\
    \
*   **out** – Output array. If provided, the result is placed into this array.\
    \
\
Returns:\
\
The complex conjugate of _self_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Round([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int decimals, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Round "Link to this definition")\
  \
\
Equivalent to [`ndarray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round "numpy.ndarray.round")\
 (_self_, _decimals_, _out_). Returns the array with elements rounded to the nearest decimal place. The decimal place is defined as the \\(10^{-\\textrm{decimals}}\\) digit so that negative _decimals_ cause rounding to the nearest 10’s, 100’s, etc. If out is `NULL`, then the output array is created, otherwise the output is placed in _out_ which must be the correct size and type.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Std([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Std "Link to this definition")\
  \
\
Equivalent to [`ndarray.std`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html#numpy.ndarray.std "numpy.ndarray.std")\
 (_self_, _axis_, _rtype_). Return the standard deviation using data along _axis_ converted to data type _rtype_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Sum([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Sum "Link to this definition")\
  \
\
Equivalent to [`ndarray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")\
 (_self_, _axis_, _rtype_). Return 1-d vector sums of elements in _self_ along _axis_. Perform the sum after converting data to data type _rtype_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_CumSum([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CumSum "Link to this definition")\
  \
\
Equivalent to [`ndarray.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumsum.html#numpy.ndarray.cumsum "numpy.ndarray.cumsum")\
 (_self_, _axis_, _rtype_). Return cumulative 1-d sums of elements in _self_ along _axis_. Perform the sum after converting data to data type _rtype_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Prod([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Prod "Link to this definition")\
  \
\
Equivalent to [`ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")\
 (_self_, _axis_, _rtype_). Return 1-d products of elements in _self_ along _axis_. Perform the product after converting data to data type _rtype_.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_CumProd([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, int rtype, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CumProd "Link to this definition")\
  \
\
Equivalent to [`ndarray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html#numpy.ndarray.cumprod "numpy.ndarray.cumprod")\
 (_self_, _axis_, _rtype_). Return 1-d cumulative products of elements in `self` along `axis`. Perform the product after converting data to data type `rtype`.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_All([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_All "Link to this definition")\
  \
\
Equivalent to [`ndarray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")\
 (_self_, _axis_). Return an array with True elements for every 1-d sub-array of `self` defined by `axis` in which all the elements are True.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Any([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*self, int axis, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Any "Link to this definition")\
  \
\
Equivalent to [`ndarray.any`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html#numpy.ndarray.any "numpy.ndarray.any")\
 (_self_, _axis_). Return an array with True elements for every 1-d sub-array of _self_ defined by _axis_ in which any of the elements are True.\
\
Functions[#](https://numpy.org/doc/stable/reference/c-api/array.html#functions "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------\
\
### Array Functions[#](https://numpy.org/doc/stable/reference/c-api/array.html#array-functions "Link to this heading")\
\
int PyArray\_AsCArray([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*\*op, void \*ptr, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*dims, int nd, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*typedescr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_AsCArray "Link to this definition")\
  \
\
Sometimes it is useful to access a multidimensional array as a C-style multi-dimensional array so that algorithms can be implemented using C’s a\[i\]\[j\]\[k\] syntax. This routine returns a pointer, _ptr_, that simulates this kind of C-style array, for 1-, 2-, and 3-d ndarrays.\
\
Parameters:\
\
*   **op** – The address to any Python object. This Python object will be replaced with an equivalent well-behaved, C-style contiguous, ndarray of the given data type specified by the last two arguments. Be sure that stealing a reference in this way to the input object is justified.\
    \
*   **ptr** – The address to a (ctype\* for 1-d, ctype\*\* for 2-d or ctype\*\*\* for 3-d) variable where ctype is the equivalent C-type for the data type. On return, _ptr_ will be addressable as a 1-d, 2-d, or 3-d array.\
    \
*   **dims** – An output array that contains the shape of the array object. This array gives boundaries on any looping that will take place.\
    \
*   **nd** – The dimensionality of the array (1, 2, or 3).\
    \
*   **typedescr** – A [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
     structure indicating the desired data-type (including required byteorder). The call will steal a reference to the parameter.\
    \
\
Note\
\
The simulation of a C-style array is not complete for 2-d and 3-d arrays. For example, the simulated arrays of pointers cannot be passed to subroutines expecting specific, statically-defined 2-d and 3-d arrays. To pass to functions requiring those kind of inputs, you must statically define the required array and copy data.\
\
int PyArray\_Free([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op, void \*ptr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Free "Link to this definition")\
  \
\
Must be called with the same objects and memory locations returned from [`PyArray_AsCArray`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_AsCArray "PyArray_AsCArray")\
 (…). This function cleans up memory that otherwise would get leaked.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Concatenate([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, int axis)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Concatenate "Link to this definition")\
  \
\
Join the sequence of objects in _obj_ together along _axis_ into a single array. If the dimensions or types are not compatible an error is raised.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_InnerProduct([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_InnerProduct "Link to this definition")\
  \
\
Compute a product-sum over the last dimensions of _obj1_ and _obj2_. Neither array is conjugated.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_MatrixProduct([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MatrixProduct "Link to this definition")\
  \
\
Compute a product-sum over the last dimension of _obj1_ and the second-to-last dimension of _obj2_. For 2-d arrays this is a matrix-product. Neither array is conjugated.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_MatrixProduct2([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MatrixProduct2 "Link to this definition")\
  \
\
Same as PyArray\_MatrixProduct, but store the result in _out_. The output array must have the correct shape, type, and be C-contiguous, or an exception is raised.\
\
[PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*PyArray\_EinsteinSum(char \*subscripts, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 nop, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*\*op\_in, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")\
 order, [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")\
 casting, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_EinsteinSum "Link to this definition")\
  \
\
Applies the Einstein summation convention to the array operands provided, returning a new array or placing the result in _out_. The string in _subscripts_ is a comma separated list of index letters. The number of operands is in _nop_, and _op\_in_ is an array containing those operands. The data type of the output can be forced with _dtype_, the output order can be forced with _order_ ([`NPY_KEEPORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_KEEPORDER "NPY_KEEPORDER")\
 is recommended), and when _dtype_ is specified, _casting_ indicates how permissive the data conversion should be.\
\
See the [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")\
 function for more details.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Correlate([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op2, int mode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Correlate "Link to this definition")\
  \
\
Compute the 1-d correlation of the 1-d arrays _op1_ and _op2_ . The correlation is computed at each output point by multiplying _op1_ by a shifted version of _op2_ and summing the result. As a result of the shift, needed values outside of the defined range of _op1_ and _op2_ are interpreted as zero. The mode determines how many shifts to return: 0 - return only shifts that did not need to assume zero- values; 1 - return an object that is the same size as _op1_, 2 - return all possible shifts (any overlap at all is accepted).\
\
Notes\
\
This does not compute the usual correlation: if op2 is larger than op1, the arguments are swapped, and the conjugate is never taken for complex arrays. See PyArray\_Correlate2 for the usual signal processing correlation.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Correlate2([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op2, int mode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Correlate2 "Link to this definition")\
  \
\
Updated version of PyArray\_Correlate, which uses the usual definition of correlation for 1d arrays. The correlation is computed at each output point by multiplying _op1_ by a shifted version of _op2_ and summing the result. As a result of the shift, needed values outside of the defined range of _op1_ and _op2_ are interpreted as zero. The mode determines how many shifts to return: 0 - return only shifts that did not need to assume zero- values; 1 - return an object that is the same size as _op1_, 2 - return all possible shifts (any overlap at all is accepted).\
\
Notes\
\
Compute z as follows:\
\
z\[k\] \= sum\_n op1\[n\] \* conj(op2\[n+k\])\
\
Copy to clipboard\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Where([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*condition, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*x, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*y)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Where "Link to this definition")\
  \
\
If both `x` and `y` are `NULL`, then return [`PyArray_Nonzero`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Nonzero "PyArray_Nonzero")\
 (_condition_). Otherwise, both _x_ and _y_ must be given and the object returned is shaped like _condition_ and has elements of _x_ and _y_ where _condition_ is respectively True or False.\
\
### Other functions[#](https://numpy.org/doc/stable/reference/c-api/array.html#other-functions "Link to this heading")\
\
[npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")\
 PyArray\_CheckStrides(int elsize, int nd, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 numbytes, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 const \*dims, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 const \*newstrides)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CheckStrides "Link to this definition")\
  \
\
Determine if _newstrides_ is a strides array consistent with the memory of an _nd_ -dimensional array with shape `dims` and element-size, _elsize_. The _newstrides_ array is checked to see if jumping by the provided number of bytes in each direction will ever mean jumping more than _numbytes_ which is the assumed size of the available memory segment. If _numbytes_ is 0, then an equivalent _numbytes_ is computed assuming _nd_, _dims_, and _elsize_ refer to a single-segment array. Return [`NPY_TRUE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "NPY_TRUE")\
 if _newstrides_ is acceptable, otherwise return [`NPY_FALSE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FALSE "NPY_FALSE")\
.\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 PyArray\_MultiplyList([npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 const \*seq, int n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiplyList "Link to this definition")\
  \
\
int PyArray\_MultiplyIntList(int const \*seq, int n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiplyIntList "Link to this definition")\
  \
\
Both of these routines multiply an _n_ -length array, _seq_, of integers and return the result. No overflow checking is performed.\
\
int PyArray\_CompareLists([npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 const \*l1, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 const \*l2, int n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CompareLists "Link to this definition")\
  \
\
Given two _n_ -length arrays of integers, _l1_, and _l2_, return 1 if the lists are identical; otherwise, return 0.\
\
Auxiliary data with object semantics[#](https://numpy.org/doc/stable/reference/c-api/array.html#auxiliary-data-with-object-semantics "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
type NpyAuxData[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "Link to this definition")\
  \
\
When working with more complex dtypes which are composed of other dtypes, such as the struct dtype, creating inner loops that manipulate the dtypes requires carrying along additional data. NumPy supports this idea through a struct [`NpyAuxData`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")\
, mandating a few conventions so that it is possible to do this.\
\
Defining an [`NpyAuxData`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")\
 is similar to defining a class in C++, but the object semantics have to be tracked manually since the API is in C. Here’s an example for a function which doubles up an element using an element copier function as a primitive.\
\
typedef struct {\
    NpyAuxData base;\
    ElementCopier\_Func \*func;\
    NpyAuxData \*funcdata;\
} eldoubler\_aux\_data;\
\
void free\_element\_doubler\_aux\_data(NpyAuxData \*data)\
{\
    eldoubler\_aux\_data \*d \= (eldoubler\_aux\_data \*)data;\
    /\* Free the memory owned by this auxdata \*/\
    NPY\_AUXDATA\_FREE(d\->funcdata);\
    PyArray\_free(d);\
}\
\
NpyAuxData \*clone\_element\_doubler\_aux\_data(NpyAuxData \*data)\
{\
    eldoubler\_aux\_data \*ret \= PyArray\_malloc(sizeof(eldoubler\_aux\_data));\
    if (ret \== NULL) {\
        return NULL;\
    }\
\
    /\* Raw copy of all data \*/\
    memcpy(ret, data, sizeof(eldoubler\_aux\_data));\
\
    /\* Fix up the owned auxdata so we have our own copy \*/\
    ret\->funcdata \= NPY\_AUXDATA\_CLONE(ret\->funcdata);\
    if (ret\->funcdata \== NULL) {\
        PyArray\_free(ret);\
        return NULL;\
    }\
\
    return (NpyAuxData \*)ret;\
}\
\
NpyAuxData \*create\_element\_doubler\_aux\_data(\
                            ElementCopier\_Func \*func,\
                            NpyAuxData \*funcdata)\
{\
    eldoubler\_aux\_data \*ret \= PyArray\_malloc(sizeof(eldoubler\_aux\_data));\
    if (ret \== NULL) {\
        PyErr\_NoMemory();\
        return NULL;\
    }\
    memset(&ret, 0, sizeof(eldoubler\_aux\_data));\
    ret\->base\->free \= &free\_element\_doubler\_aux\_data;\
    ret\->base\->clone \= &clone\_element\_doubler\_aux\_data;\
    ret\->func \= func;\
    ret\->funcdata \= funcdata;\
\
    return (NpyAuxData \*)ret;\
}\
\
Copy to clipboard\
\
type NpyAuxData\_FreeFunc[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData_FreeFunc "Link to this definition")\
  \
\
The function pointer type for NpyAuxData free functions.\
\
type NpyAuxData\_CloneFunc[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData_CloneFunc "Link to this definition")\
  \
\
The function pointer type for NpyAuxData clone functions. These functions should never set the Python exception on error, because they may be called from a multi-threaded context.\
\
void NPY\_AUXDATA\_FREE([NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")\
 \*auxdata)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_AUXDATA_FREE "Link to this definition")\
  \
\
A macro which calls the auxdata’s free function appropriately, does nothing if auxdata is NULL.\
\
[NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")\
 \*NPY\_AUXDATA\_CLONE([NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")\
 \*auxdata)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_AUXDATA_CLONE "Link to this definition")\
  \
\
A macro which calls the auxdata’s clone function appropriately, returning a deep copy of the auxiliary data.\
\
Array iterators[#](https://numpy.org/doc/stable/reference/c-api/array.html#array-iterators "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------\
\
As of NumPy 1.6.0, these array iterators are superseded by the new array iterator, [`NpyIter`](https://numpy.org/doc/stable/reference/c-api/iterator.html#c.NpyIter "NpyIter")\
.\
\
An array iterator is a simple way to access the elements of an N-dimensional array quickly and efficiently, as seen in [the example](https://numpy.org/doc/stable/reference/c-api/iterator.html#iteration-example)\
 which provides more description of this useful approach to looping over an array from C.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_IterNew([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IterNew "Link to this definition")\
  \
\
Return an array iterator object from the array, _arr_. This is equivalent to _arr_. **flat**. The array iterator object makes it easy to loop over an N-dimensional non-contiguous array in C-style contiguous fashion.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_IterAllButAxis([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*arr, int \*axis)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IterAllButAxis "Link to this definition")\
  \
\
Return an array iterator that will iterate over all axes but the one provided in _\*axis_. The returned iterator cannot be used with [`PyArray_ITER_GOTO1D`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO1D "PyArray_ITER_GOTO1D")\
. This iterator could be used to write something similar to what ufuncs do wherein the loop over the largest axis is done by a separate sub-routine. If _\*axis_ is negative then _\*axis_ will be set to the axis having the smallest stride and that axis will be used.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_BroadcastToShape([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*arr, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 const \*dimensions, int nd)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_BroadcastToShape "Link to this definition")\
  \
\
Return an array iterator that is broadcast to iterate as an array of the shape provided by _dimensions_ and _nd_.\
\
int PyArrayIter\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayIter_Check "Link to this definition")\
  \
\
Evaluates true if _op_ is an array iterator (or instance of a subclass of the array iterator type).\
\
void PyArray\_ITER\_RESET([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*iterator)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_RESET "Link to this definition")\
  \
\
Reset an _iterator_ to the beginning of the array.\
\
void PyArray\_ITER\_NEXT([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*iterator)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_NEXT "Link to this definition")\
  \
\
Increment the index and the dataptr members of the _iterator_ to point to the next element of the array. If the array is not (C-style) contiguous, also increment the N-dimensional coordinates array.\
\
void \*PyArray\_ITER\_DATA([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*iterator)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_DATA "Link to this definition")\
  \
\
A pointer to the current element of the array.\
\
void PyArray\_ITER\_GOTO([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*iterator, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*destination)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO "Link to this definition")\
  \
\
Set the _iterator_ index, dataptr, and coordinates members to the location in the array indicated by the N-dimensional c-array, _destination_, which must have size at least _iterator_ ->nd\_m1+1.\
\
void PyArray\_ITER\_GOTO1D([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*iterator, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 index)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO1D "Link to this definition")\
  \
\
Set the _iterator_ index and dataptr to the location in the array indicated by the integer _index_ which points to an element in the C-styled flattened array.\
\
int PyArray\_ITER\_NOTDONE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*iterator)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_NOTDONE "Link to this definition")\
  \
\
Evaluates TRUE as long as the iterator has not looped through all of the elements, otherwise it evaluates FALSE.\
\
Broadcasting (multi-iterators)[#](https://numpy.org/doc/stable/reference/c-api/array.html#broadcasting-multi-iterators "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_MultiIterNew(int num, ...)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIterNew "Link to this definition")\
  \
\
A simplified interface to broadcasting. This function takes the number of arrays to broadcast and then _num_ extra ( [`PyObject *`](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 ) arguments. These arguments are converted to arrays and iterators are created. [`PyArray_Broadcast`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Broadcast "PyArray_Broadcast")\
 is then called on the resulting multi-iterator object. The resulting, broadcasted mult-iterator object is then returned. A broadcasted operation can then be performed using a single loop and using [`PyArray_MultiIter_NEXT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NEXT "PyArray_MultiIter_NEXT")\
 (..)\
\
void PyArray\_MultiIter\_RESET([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_RESET "Link to this definition")\
  \
\
Reset all the iterators to the beginning in a multi-iterator object, _multi_.\
\
void PyArray\_MultiIter\_NEXT([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NEXT "Link to this definition")\
  \
\
Advance each iterator in a multi-iterator object, _multi_, to its next (broadcasted) element.\
\
void \*PyArray\_MultiIter\_DATA([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi, int i)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_DATA "Link to this definition")\
  \
\
Return the data-pointer of the _i_ \\(^{\\textrm{th}}\\) iterator in a multi-iterator object.\
\
void PyArray\_MultiIter\_NEXTi([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi, int i)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NEXTi "Link to this definition")\
  \
\
Advance the pointer of only the _i_ \\(^{\\textrm{th}}\\) iterator.\
\
void PyArray\_MultiIter\_GOTO([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*destination)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_GOTO "Link to this definition")\
  \
\
Advance each iterator in a multi-iterator object, _multi_, to the given \\(N\\) -dimensional _destination_ where \\(N\\) is the number of dimensions in the broadcasted array.\
\
void PyArray\_MultiIter\_GOTO1D([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 index)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_GOTO1D "Link to this definition")\
  \
\
Advance each iterator in a multi-iterator object, _multi_, to the corresponding location of the _index_ into the flattened broadcasted array.\
\
int PyArray\_MultiIter\_NOTDONE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NOTDONE "Link to this definition")\
  \
\
Evaluates TRUE as long as the multi-iterator has not looped through all of the elements (of the broadcasted result), otherwise it evaluates FALSE.\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 PyArray\_MultiIter\_SIZE([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_SIZE "Link to this definition")\
  \
\
New in version 1.26.0.\
\
Returns the total broadcasted size of a multi-iterator object.\
\
int PyArray\_MultiIter\_NDIM([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NDIM "Link to this definition")\
  \
\
New in version 1.26.0.\
\
Returns the number of dimensions in the broadcasted result of a multi-iterator object.\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 PyArray\_MultiIter\_INDEX([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_INDEX "Link to this definition")\
  \
\
New in version 1.26.0.\
\
Returns the current (1-d) index into the broadcasted result of a multi-iterator object.\
\
int PyArray\_MultiIter\_NUMITER([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NUMITER "Link to this definition")\
  \
\
New in version 1.26.0.\
\
Returns the number of iterators that are represented by a multi-iterator object.\
\
void \*\*PyArray\_MultiIter\_ITERS([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_ITERS "Link to this definition")\
  \
\
New in version 1.26.0.\
\
Returns an array of iterator objects that holds the iterators for the arrays to be broadcast together. On return, the iterators are adjusted for broadcasting.\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*PyArray\_MultiIter\_DIMS([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*multi)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_DIMS "Link to this definition")\
  \
\
New in version 1.26.0.\
\
Returns a pointer to the dimensions/shape of the broadcasted result of a multi-iterator object.\
\
int PyArray\_Broadcast([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*mit)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Broadcast "Link to this definition")\
  \
\
This function encapsulates the broadcasting rules. The _mit_ container should already contain iterators for all the arrays that need to be broadcast. On return, these iterators will be adjusted so that iteration over each simultaneously will accomplish the broadcasting. A negative number is returned if an error occurs.\
\
int PyArray\_RemoveSmallest([PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")\
 \*mit)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RemoveSmallest "Link to this definition")\
  \
\
This function takes a multi-iterator object that has been previously “broadcasted,” finds the dimension with the smallest “sum of strides” in the broadcasted result and adapts all the iterators so as not to iterate over that dimension (by effectively making them of length-1 in that dimension). The corresponding dimension is returned unless _mit_ ->nd is 0, then -1 is returned. This function is useful for constructing ufunc-like routines that broadcast their inputs correctly and then call a strided 1-d version of the routine as the inner-loop. This 1-d version is usually optimized for speed and for this reason the loop should be performed over the axis that won’t require large stride jumps.\
\
Neighborhood iterator[#](https://numpy.org/doc/stable/reference/c-api/array.html#neighborhood-iterator "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------\
\
Neighborhood iterators are subclasses of the iterator object, and can be used to iter over a neighborhood of a point. For example, you may want to iterate over every voxel of a 3d image, and for every such voxel, iterate over an hypercube. Neighborhood iterator automatically handle boundaries, thus making this kind of code much easier to write than manual boundaries handling, at the cost of a slight overhead.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_NeighborhoodIterNew([PyArrayIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "PyArrayIterObject")\
 \*iter, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 bounds, int mode, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*fill\_value)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew "Link to this definition")\
  \
\
This function creates a new neighborhood iterator from an existing iterator. The neighborhood will be computed relatively to the position currently pointed by _iter_, the bounds define the shape of the neighborhood iterator, and the mode argument the boundaries handling mode.\
\
The _bounds_ argument is expected to be a (2 \* iter->ao->nd) arrays, such as the range bound\[2\*i\]->bounds\[2\*i+1\] defines the range where to walk for dimension i (both bounds are included in the walked coordinates). The bounds should be ordered for each dimension (bounds\[2\*i\] <= bounds\[2\*i+1\]).\
\
The mode should be one of:\
\
NPY\_NEIGHBORHOOD\_ITER\_ZERO\_PADDING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew.NPY_NEIGHBORHOOD_ITER_ZERO_PADDING "Link to this definition")\
  \
\
Zero padding. Outside bounds values will be 0.\
\
NPY\_NEIGHBORHOOD\_ITER\_ONE\_PADDING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew.NPY_NEIGHBORHOOD_ITER_ONE_PADDING "Link to this definition")\
  \
\
One padding, Outside bounds values will be 1.\
\
NPY\_NEIGHBORHOOD\_ITER\_CONSTANT\_PADDING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew.NPY_NEIGHBORHOOD_ITER_CONSTANT_PADDING "Link to this definition")\
  \
\
Constant padding. Outside bounds values will be the same as the first item in fill\_value.\
\
NPY\_NEIGHBORHOOD\_ITER\_MIRROR\_PADDING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew.NPY_NEIGHBORHOOD_ITER_MIRROR_PADDING "Link to this definition")\
  \
\
Mirror padding. Outside bounds values will be as if the array items were mirrored. For example, for the array \[1, 2, 3, 4\], x\[-2\] will be 2, x\[-2\] will be 1, x\[4\] will be 4, x\[5\] will be 1, etc…\
\
NPY\_NEIGHBORHOOD\_ITER\_CIRCULAR\_PADDING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew.NPY_NEIGHBORHOOD_ITER_CIRCULAR_PADDING "Link to this definition")\
  \
\
Circular padding. Outside bounds values will be as if the array was repeated. For example, for the array \[1, 2, 3, 4\], x\[-2\] will be 3, x\[-2\] will be 4, x\[4\] will be 1, x\[5\] will be 2, etc…\
\
If the mode is constant filling ([`NPY_NEIGHBORHOOD_ITER_CONSTANT_PADDING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NeighborhoodIterNew.NPY_NEIGHBORHOOD_ITER_CONSTANT_PADDING "NPY_NEIGHBORHOOD_ITER_CONSTANT_PADDING")\
), fill\_value should point to an array object which holds the filling value (the first item will be the filling value if the array contains more than one item). For other cases, fill\_value may be NULL.\
\
*   The iterator holds a reference to iter\
    \
*   Return NULL on failure (in which case the reference count of iter is not changed)\
    \
*   iter itself can be a Neighborhood iterator: this can be useful for .e.g automatic boundaries handling\
    \
*   the object returned by this function should be safe to use as a normal iterator\
    \
*   If the position of iter is changed, any subsequent call to PyArrayNeighborhoodIter\_Next is undefined behavior, and PyArrayNeighborhoodIter\_Reset must be called.\
    \
*   If the position of iter is not the beginning of the data and the underlying data for iter is contiguous, the iterator will point to the start of the data instead of position pointed by iter. To avoid this situation, iter should be moved to the required position only after the creation of iterator, and PyArrayNeighborhoodIter\_Reset must be called.\
    \
\
PyArrayIterObject \*iter;\
PyArrayNeighborhoodIterObject \*neigh\_iter;\
iter \= PyArray\_IterNew(x);\
\
/\*For a 3x3 kernel \*/\
bounds \= {\-1, 1, \-1, 1};\
neigh\_iter \= (PyArrayNeighborhoodIterObject\*)PyArray\_NeighborhoodIterNew(\
     iter, bounds, NPY\_NEIGHBORHOOD\_ITER\_ZERO\_PADDING, NULL);\
\
for(i \= 0; i < iter\->size; ++i) {\
     for (j \= 0; j < neigh\_iter\->size; ++j) {\
             /\* Walk around the item currently pointed by iter->dataptr \*/\
             PyArrayNeighborhoodIter\_Next(neigh\_iter);\
     }\
\
     /\* Move to the next point of iter \*/\
     PyArrayIter\_Next(iter);\
     PyArrayNeighborhoodIter\_Reset(neigh\_iter);\
}\
\
Copy to clipboard\
\
int PyArrayNeighborhoodIter\_Reset([PyArrayNeighborhoodIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayNeighborhoodIterObject "PyArrayNeighborhoodIterObject")\
 \*iter)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayNeighborhoodIter_Reset "Link to this definition")\
  \
\
Reset the iterator position to the first point of the neighborhood. This should be called whenever the iter argument given at PyArray\_NeighborhoodIterObject is changed (see example)\
\
int PyArrayNeighborhoodIter\_Next([PyArrayNeighborhoodIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayNeighborhoodIterObject "PyArrayNeighborhoodIterObject")\
 \*iter)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayNeighborhoodIter_Next "Link to this definition")\
  \
\
After this call, iter->dataptr points to the next point of the neighborhood. Calling this function after every point of the neighborhood has been visited is undefined.\
\
Array scalars[#](https://numpy.org/doc/stable/reference/c-api/array.html#array-scalars "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Return([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Return "Link to this definition")\
  \
\
This function steals a reference to _arr_.\
\
This function checks to see if _arr_ is a 0-dimensional array and, if so, returns the appropriate array scalar. It should be used whenever 0-dimensional arrays could be returned to Python.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_Scalar(void \*data, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*base)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Scalar "Link to this definition")\
  \
\
Return an array scalar object of the given _dtype_ by **copying** from memory pointed to by _data_. _base_ is expected to be the array object that is the owner of the data. _base_ is required if _dtype_ is a `void` scalar, or if the `NPY_USE_GETITEM` flag is set and it is known that the `getitem` method uses the `arr` argument without checking if it is `NULL`. Otherwise _base_ may be `NULL`.\
\
If the data is not in native byte order (as indicated by `dtype->byteorder`) then this function will byteswap the data, because array scalars are always in correct machine-byte order.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_ToScalar(void \*data, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ToScalar "Link to this definition")\
  \
\
Return an array scalar object of the type and itemsize indicated by the array object _arr_ copied from the memory pointed to by _data_ and swapping if the data in _arr_ is not in machine byte-order.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_FromScalar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*scalar, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*outcode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromScalar "Link to this definition")\
  \
\
Return a 0-dimensional array of type determined by _outcode_ from _scalar_ which should be an array-scalar object. If _outcode_ is NULL, then the type is determined from _scalar_.\
\
void PyArray\_ScalarAsCtype([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*scalar, void \*ctypeptr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ScalarAsCtype "Link to this definition")\
  \
\
Return in _ctypeptr_ a pointer to the actual value in an array scalar. There is no error checking so _scalar_ must be an array-scalar object, and ctypeptr must have enough space to hold the correct type. For flexible-sized types, a pointer to the data is copied into the memory of _ctypeptr_, for all other types, the actual data is copied into the address pointed to by _ctypeptr_.\
\
int PyArray\_CastScalarToCtype([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*scalar, void \*ctypeptr, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*outcode)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CastScalarToCtype "Link to this definition")\
  \
\
Return the data (cast to the data type indicated by _outcode_) from the array-scalar, _scalar_, into the memory pointed to by _ctypeptr_ (which must be large enough to handle the incoming memory).\
\
Returns -1 on failure, and 0 on success.\
\
[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*PyArray\_TypeObjectFromType(int type)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_TypeObjectFromType "Link to this definition")\
  \
\
Returns a scalar type-object from a type-number, _type_ . Equivalent to [`PyArray_DescrFromType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromType "PyArray_DescrFromType")\
 (_type_)->typeobj except for reference counting and error-checking. Returns a new reference to the typeobject on success or `NULL` on failure.\
\
[NPY\_SCALARKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND "NPY_SCALARKIND")\
 PyArray\_ScalarKind(int typenum, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*\*arr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ScalarKind "Link to this definition")\
  \
\
Legacy way to query special promotion for scalar values. This is not used in NumPy itself anymore and is expected to be deprecated eventually.\
\
New DTypes can define promotion rules specific to Python scalars.\
\
int PyArray\_CanCoerceScalar(char thistype, char neededtype, [NPY\_SCALARKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND "NPY_SCALARKIND")\
 scalar)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CanCoerceScalar "Link to this definition")\
  \
\
Legacy way to query special promotion for scalar values. This is not used in NumPy itself anymore and is expected to be deprecated eventually.\
\
Use `PyArray_ResultType` for similar purposes.\
\
Data-type descriptors[#](https://numpy.org/doc/stable/reference/c-api/array.html#data-type-descriptors "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------\
\
Warning\
\
Data-type objects must be reference counted so be aware of the action on the data-type reference of different C-API calls. The standard rule is that when a data-type object is returned it is a new reference. Functions that take [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
\* objects and return arrays steal references to the data-type their inputs unless otherwise noted. Therefore, you must own a reference to any data-type object used as input to such a function.\
\
int PyArray\_DescrCheck([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrCheck "Link to this definition")\
  \
\
Evaluates as true if _obj_ is a data-type object ( [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
\* ).\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_DescrNew([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrNew "Link to this definition")\
  \
\
Return a new data-type object copied from _obj_ (the fields reference is just updated so that the new object points to the same fields dictionary if any).\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_DescrNewFromType(int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrNewFromType "Link to this definition")\
  \
\
Create a new data-type object from the built-in (or user-registered) data-type indicated by _typenum_. All builtin types should not have any of their fields changed. This creates a new copy of the [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 structure so that you can fill it in as appropriate. This function is especially needed for flexible data-types which need to have a new elsize member in order to be meaningful in array construction.\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_DescrNewByteorder([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*obj, char newendian)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrNewByteorder "Link to this definition")\
  \
\
Create a new data-type object with the byteorder set according to _newendian_. All referenced data-type objects (in subdescr and fields members of the data-type object) are also changed (recursively).\
\
The value of _newendian_ is one of these macros:\
\
NPY\_IGNORE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_IGNORE "Link to this definition")\
  \
\
NPY\_SWAP[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SWAP "Link to this definition")\
  \
\
NPY\_NATIVE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_NATIVE "Link to this definition")\
  \
\
NPY\_LITTLE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_LITTLE "Link to this definition")\
  \
\
NPY\_BIG[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BIG "Link to this definition")\
  \
\
If a byteorder of [`NPY_IGNORE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_IGNORE "NPY_IGNORE")\
 is encountered it is left alone. If newendian is [`NPY_SWAP`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SWAP "NPY_SWAP")\
, then all byte-orders are swapped. Other valid newendian values are [`NPY_NATIVE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_NATIVE "NPY_NATIVE")\
, [`NPY_LITTLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_LITTLE "NPY_LITTLE")\
, and [`NPY_BIG`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BIG "NPY_BIG")\
 which all cause the returned data-typed descriptor (and all it’s referenced data-type descriptors) to have the corresponding byte- order.\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_DescrFromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*mintype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromObject "Link to this definition")\
  \
\
Determine an appropriate data-type object from the object _op_ (which should be a “nested” sequence object) and the minimum data-type descriptor mintype (which can be `NULL` ). Similar in behavior to array(_op_).dtype. Don’t confuse this function with [`PyArray_DescrConverter`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrConverter "PyArray_DescrConverter")\
. This function essentially looks at all the objects in the (nested) sequence and determines the data-type from the elements it finds.\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_DescrFromScalar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*scalar)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromScalar "Link to this definition")\
  \
\
Return a data-type object from an array-scalar object. No checking is done to be sure that _scalar_ is an array scalar. If no suitable data-type can be determined, then a data-type of [`NPY_OBJECT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "NPY_OBJECT")\
 is returned by default.\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_DescrFromType(int typenum)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromType "Link to this definition")\
  \
\
Returns a data-type object corresponding to _typenum_. The _typenum_ can be one of the enumerated types, a character code for one of the enumerated types, or a user-defined type. If you want to use a flexible size array, then you need to `flexible typenum` and set the results `elsize` parameter to the desired size. The typenum is one of the [`NPY_TYPES`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES "NPY_TYPES")\
.\
\
int PyArray\_DescrConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*\*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrConverter "Link to this definition")\
  \
\
Convert any compatible Python object, _obj_, to a data-type object in _dtype_. A large number of Python objects can be converted to data-type objects. See [Data type objects (dtype)](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)\
 for a complete description. This version of the converter converts None objects to a [`NPY_DEFAULT_TYPE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_DEFAULT_TYPE "NPY_DEFAULT_TYPE")\
 data-type object. This function can be used with the “O&” character code in [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "(in Python v3.14)")\
 processing.\
\
int PyArray\_DescrConverter2([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*\*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrConverter2 "Link to this definition")\
  \
\
Convert any compatible Python object, _obj_, to a data-type object in _dtype_. This version of the converter converts None objects so that the returned data-type is `NULL`. This function can also be used with the “O&” character in PyArg\_ParseTuple processing.\
\
int PyArray\_DescrAlignConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*\*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrAlignConverter "Link to this definition")\
  \
\
Like [`PyArray_DescrConverter`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrConverter "PyArray_DescrConverter")\
 except it aligns C-struct-like objects on word-boundaries as the compiler would.\
\
int PyArray\_DescrAlignConverter2([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*\*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrAlignConverter2 "Link to this definition")\
  \
\
Like [`PyArray_DescrConverter2`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrConverter2 "PyArray_DescrConverter2")\
 except it aligns C-struct-like objects on word-boundaries as the compiler would.\
\
Data Type Promotion and Inspection[#](https://numpy.org/doc/stable/reference/c-api/array.html#data-type-promotion-and-inspection "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------\
\
[PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*PyArray\_CommonDType(const [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*dtype1, const [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*dtype2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CommonDType "Link to this definition")\
  \
\
This function defines the common DType operator. Note that the common DType will not be `object` (unless one of the DTypes is `object`). Similar to [`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")\
, but works on the classes and not instances.\
\
[PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*PyArray\_PromoteDTypeSequence([npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 length, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*\*dtypes\_in)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_PromoteDTypeSequence "Link to this definition")\
  \
\
Promotes a list of DTypes with each other in a way that should guarantee stable results even when changing the order. This function is smarter and can often return successful and unambiguous results when `common_dtype(common_dtype(dt1, dt2), dt3)` would depend on the operation order or fail. Nevertheless, DTypes should aim to ensure that their common-dtype implementation is associative and commutative! (Mainly, unsigned and signed integers are not.)\
\
For guaranteed consistent results DTypes must implement common-Dtype “transitively”. If A promotes B and B promotes C, than A must generally also promote C; where “promotes” means implements the promotion. (There are some exceptions for abstract DTypes)\
\
In general this approach always works as long as the most generic dtype is either strictly larger, or compatible with all other dtypes. For example promoting `float16` with any other float, integer, or unsigned integer again gives a floating point number.\
\
[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*PyArray\_GetDefaultDescr(const [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*DType)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetDefaultDescr "Link to this definition")\
  \
\
Given a DType class, returns the default instance (descriptor). This checks for a `singleton` first and only calls the `default_descr` function if necessary.\
\
Custom Data Types[#](https://numpy.org/doc/stable/reference/c-api/array.html#custom-data-types "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------\
\
New in version 2.0.\
\
These functions allow defining custom flexible data types outside of NumPy. See [NEP 42](https://numpy.org/neps/nep-0042-new-dtypes.html#nep42 "(in NumPy Enhancement Proposals)")\
 for more details about the rationale and design of the new DType system. See the [numpy-user-dtypes repository](https://github.com/numpy/numpy-user-dtypes)\
 for a number of example DTypes. Also see [PyArray\_DTypeMeta and PyArrayDTypeMeta\_Spec](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#dtypemeta)\
 for documentation on `PyArray_DTypeMeta` and `PyArrayDTypeMeta_Spec`.\
\
int PyArrayInitDTypeMeta\_FromSpec([PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*Dtype, [PyArrayDTypeMeta\_Spec](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Spec "PyArrayDTypeMeta_Spec")\
 \*spec)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayInitDTypeMeta_FromSpec "Link to this definition")\
  \
\
Initialize a new DType. It must currently be a static Python C type that is declared as [`PyArray_DTypeMeta`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 and not [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")\
. Further, it must subclass _np.dtype_ and set its type to [`PyArrayDTypeMeta_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Type "PyArrayDTypeMeta_Type")\
 (before calling [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "(in Python v3.14)")\
), which has additional fields compared to a normal [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")\
. See the examples in the `numpy-user-dtypes` repository for usage with both parametric and non-parametric data types.\
\
Note\
\
Custom DType registration is expected to happen during module import. The registration API mutates global state and is not thread-safe.\
\
### Flags[#](https://numpy.org/doc/stable/reference/c-api/array.html#dtype-flags "Link to this heading")\
\
Flags that can be set on the `PyArrayDTypeMeta_Spec` to initialize the DType.\
\
NPY\_DT\_ABSTRACT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_ABSTRACT "Link to this definition")\
  \
\
Indicates the DType is an abstract “base” DType in a DType hierarchy and should not be directly instantiated.\
\
NPY\_DT\_PARAMETRIC[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PARAMETRIC "Link to this definition")\
  \
\
Indicates the DType is parametric and does not have a unique singleton instance.\
\
NPY\_DT\_NUMERIC[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_NUMERIC "Link to this definition")\
  \
\
Indicates the DType represents a numerical value.\
\
### Slot IDs and API Function Typedefs[#](https://numpy.org/doc/stable/reference/c-api/array.html#slot-ids-and-api-function-typedefs "Link to this heading")\
\
These IDs correspond to slots in the DType API and are used to identify implementations of each slot from the items of the `slots` array member of `PyArrayDTypeMeta_Spec` struct.\
\
NPY\_DT\_legacy\_descriptor\_proto[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_legacy_descriptor_proto "Link to this definition")\
  \
\
Compatibility slot to transition legacy dtypes to the new DType API. Existing legacy dtypes that currently use `PyArray_RegisterDataType` should use this to transition to the new DType API. The value of this slot is the `PyArray_DescrProto` struct.\
\
This slot allows an _existing_ legacy DType to use the new DType API without breaking backwards compatibility (or with very minor changes). I.e. NumPy will still consider this a “legacy” DType and use old code paths where applicable, but use new features as they become available.\
\
If used, this slot is required to be the first slot. The `ArrFuncs` fields are copied, but you may also set them via the slots below. (This allows backporting e.g. sorts, although NumPy 2.4+ does support a new way to implement sorts.)\
\
New in version 2.5: This feature is added in NumPy 2.5, but is backported to be compatible with NumPy 2.0+. You can vendor this backport from `npy_2_compat.h` if you wish to compile with older NumPy versions.\
\
Note\
\
This slot exists for DTypes that currently use `PyArray_RegisterDataType` allowing them to transition when otherwise regressions would block them from doing so. It is a path for deprecating `PyArray_RegisterDataType`, `PyArray_RegisterCastFunc`, `PyArray_RegisterCanCast` and further slots in the future.\
\
NPY\_DT\_discover\_descr\_from\_pyobject[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_discover_descr_from_pyobject "Link to this definition")\
  \
\
typedef [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*(PyArrayDTypeMeta\_DiscoverDescrFromPyobject)([PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*cls, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_DiscoverDescrFromPyobject "Link to this definition")\
  \
\
Used during DType inference to find the correct DType for a given PyObject. Must return a descriptor instance appropriate to store the data in the python object that is passed in. _obj_ is the python object to inspect and _cls_ is the DType class to create a descriptor for.\
\
NPY\_DT\_default\_descr[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_default_descr "Link to this definition")\
  \
\
typedef [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*(PyArrayDTypeMeta\_DefaultDescriptor)([PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*cls)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_DefaultDescriptor "Link to this definition")\
  \
\
Returns the default descriptor instance for the DType. Must be defined for parametric data types. Non-parametric data types return the singleton by default.\
\
NPY\_DT\_common\_dtype[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_common_dtype "Link to this definition")\
  \
\
typedef [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*(PyArrayDTypeMeta\_CommonDType)([PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*dtype1, [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*dtype2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_CommonDType "Link to this definition")\
  \
\
Given two input DTypes, determines the appropriate “common” DType that can store values for both types. Returns `Py_NotImplemented` if no such type exists.\
\
NPY\_DT\_common\_instance[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_common_instance "Link to this definition")\
  \
\
typedef [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*(PyArrayDTypeMeta\_CommonInstance)([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype1, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_CommonInstance "Link to this definition")\
  \
\
Given two input descriptors, determines the appropriate “common” descriptor that can store values for both instances. Returns `NULL` on error.\
\
NPY\_DT\_ensure\_canonical[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_ensure_canonical "Link to this definition")\
  \
\
typedef [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*(PyArrayDTypeMeta\_EnsureCanonical)([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_EnsureCanonical "Link to this definition")\
  \
\
Returns the “canonical” representation for a descriptor instance. The notion of a canonical descriptor generalizes the concept of byte order, in that a canonical descriptor always has native byte order. If the descriptor is already canonical, this function returns a new reference to the input descriptor.\
\
NPY\_DT\_setitem[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_setitem "Link to this definition")\
  \
\
typedef int (PyArrayDTypeMeta\_SetItem)([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
\*, char\*)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_SetItem "Link to this definition")\
  \
\
Implements scalar setitem for an array element given a PyObject.\
\
NPY\_DT\_getitem[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_getitem "Link to this definition")\
  \
\
typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*(PyArrayDTypeMeta\_GetItem)([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
\*, char\*)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetItem "Link to this definition")\
  \
\
Implements scalar getitem for an array element. Must return a python scalar.\
\
NPY\_DT\_get\_clear\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_get_clear_loop "Link to this definition")\
  \
\
If defined, sets a traversal loop that clears data in the array. This is most useful for arrays of references that must clean up array entries before the array is garbage collected. Implements `PyArrayMethod_GetTraverseLoop`.\
\
NPY\_DT\_get\_fill\_zero\_loop[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_get_fill_zero_loop "Link to this definition")\
  \
\
If defined, sets a traversal loop that fills an array with “zero” values, which may have a DType-specific meaning. This is called inside [`numpy.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")\
 for arrays that need to write a custom sentinel value that represents zero if for some reason a zero-filled array is not sufficient. Implements `PyArrayMethod_GetTraverseLoop`.\
\
NPY\_DT\_finalize\_descr[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_finalize_descr "Link to this definition")\
  \
\
typedef [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*(PyArrayDTypeMeta\_FinalizeDescriptor)([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_FinalizeDescriptor "Link to this definition")\
  \
\
If defined, a function that is called to “finalize” a descriptor instance after an array is created. One use of this function is to force newly created arrays to have a newly created descriptor instance, no matter what input descriptor is provided by a user.\
\
NPY\_DT\_get\_constant[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_get_constant "Link to this definition")\
  \
\
typedef int (PyArrayDTypeMeta\_GetConstant)([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*descr, int constant\_id, void \*out)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant "Link to this definition")\
  \
\
If defined, allows the DType to expose constant values such as machine limits, special values (infinity, NaN), and floating-point characteristics. The _descr_ is the descriptor instance, _constant\_id_ is one of the `NPY_CONSTANT_*` macros, and _out_ is a pointer to uninitialized memory where the constant value should be written. The memory pointed to by _out_ may be unaligned and is uninitialized. Returns 1 on success, 0 if the constant is not available, or -1 with an error set.\
\
**Constant IDs**:\
\
> The following constant IDs are defined for retrieving dtype-specific values:\
> \
> **Basic constants** (available for all numeric types):\
\
NPY\_CONSTANT\_zero[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_zero "Link to this definition")\
  \
\
The zero value for the dtype.\
\
NPY\_CONSTANT\_one[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_one "Link to this definition")\
  \
\
The one value for the dtype.\
\
NPY\_CONSTANT\_minimum\_finite[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_minimum_finite "Link to this definition")\
  \
\
The minimum finite value representable by the dtype. For floating-point types, this is the most negative finite value (e.g., `-FLT_MAX`).\
\
NPY\_CONSTANT\_maximum\_finite[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_maximum_finite "Link to this definition")\
  \
\
The maximum finite value representable by the dtype.\
\
**Floating-point special values**:\
\
NPY\_CONSTANT\_inf[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_inf "Link to this definition")\
  \
\
Positive infinity (only for floating-point types).\
\
NPY\_CONSTANT\_ninf[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_ninf "Link to this definition")\
  \
\
Negative infinity (only for floating-point types).\
\
NPY\_CONSTANT\_nan[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_nan "Link to this definition")\
  \
\
Not-a-Number (only for floating-point types).\
\
**Floating-point characteristics** (values of the dtype’s native type):\
\
NPY\_CONSTANT\_finfo\_radix[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_radix "Link to this definition")\
  \
\
The radix (base) of the floating-point representation. This is 2 for all floating-point types.\
\
NPY\_CONSTANT\_finfo\_eps[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_eps "Link to this definition")\
  \
\
Machine epsilon: the difference between 1.0 and the next representable value greater than 1.0. Corresponds to C macros like `FLT_EPSILON`, `DBL_EPSILON`.\
\
Note\
\
For long double in IBM double-double format (PowerPC), this is defined as `0x1p-105L` (2^-105) based on the ~106 bits of mantissa precision.\
\
NPY\_CONSTANT\_finfo\_epsneg[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_epsneg "Link to this definition")\
  \
\
The difference between 1.0 and the next representable value less than 1.0. Typically `eps / radix` for binary floating-point types.\
\
NPY\_CONSTANT\_finfo\_smallest\_normal[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_smallest_normal "Link to this definition")\
  \
\
The smallest positive normalized floating-point number. Corresponds to C macros like `FLT_MIN`, `DBL_MIN`. This is the smallest value with a leading 1 bit in the mantissa.\
\
NPY\_CONSTANT\_finfo\_smallest\_subnormal[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_smallest_subnormal "Link to this definition")\
  \
\
The smallest positive subnormal (denormalized) floating-point number. Corresponds to C macros like `FLT_TRUE_MIN`, `DBL_TRUE_MIN`. This is the smallest representable positive value, with leading 0 bits in the mantissa.\
\
**Floating-point characteristics** (integer values, type `npy_intp`):\
\
These constants return integer metadata about the floating-point representation. They are marked with the `1 << 16` bit to indicate they return `npy_intp` values rather than the dtype’s native type.\
\
NPY\_CONSTANT\_finfo\_nmant[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_nmant "Link to this definition")\
  \
\
Number of mantissa bits (excluding the implicit leading bit). For example, IEEE 754 binary64 (double) has 52 explicit mantissa bits, so this returns 52. Corresponds to `MANT_DIG - 1` from C standard macros.\
\
NPY\_CONSTANT\_finfo\_min\_exp[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_min_exp "Link to this definition")\
  \
\
Minimum exponent value. This is the minimum negative integer such that the radix raised to the power of one less than that integer is a normalized floating-point number. Corresponds to `MIN_EXP - 1` from C standard macros (e.g., `FLT_MIN_EXP - 1`).\
\
NPY\_CONSTANT\_finfo\_max\_exp[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_max_exp "Link to this definition")\
  \
\
Maximum exponent value. This is the maximum positive integer such that the radix raised to the power of one less than that integer is a representable finite floating-point number. Corresponds to `MAX_EXP` from C standard macros (e.g., `FLT_MAX_EXP`).\
\
NPY\_CONSTANT\_finfo\_decimal\_digits[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayDTypeMeta_GetConstant.NPY_CONSTANT_finfo_decimal_digits "Link to this definition")\
  \
\
The number of decimal digits of precision. Corresponds to `DIG` from C standard macros (e.g., `FLT_DIG`, `DBL_DIG`).\
\
#### PyArray\_ArrFuncs slots[#](https://numpy.org/doc/stable/reference/c-api/array.html#pyarray-arrfuncs-slots "Link to this heading")\
\
In addition the above slots, the following slots are exposed to allow filling the [PyArray\_ArrFuncs](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#arrfuncs-type)\
 struct attached to descriptor instances. Note that in the future these will be replaced by proper DType API slots but for now we have exposed the legacy `PyArray_ArrFuncs` slots.\
\
NPY\_DT\_PyArray\_ArrFuncs\_getitem[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_getitem "Link to this definition")\
  \
\
Allows setting a per-dtype getitem. Note that this is not necessary to define unless the default version calling the function defined with the `NPY_DT_getitem` ID is unsuitable. This version will be slightly faster than using `NPY_DT_getitem` at the cost of sometimes needing to deal with a NULL input array.\
\
NPY\_DT\_PyArray\_ArrFuncs\_setitem[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_setitem "Link to this definition")\
  \
\
Allows setting a per-dtype setitem. Note that this is not necessary to define unless the default version calling the function defined with the `NPY_DT_setitem` ID is unsuitable for some reason.\
\
NPY\_DT\_PyArray\_ArrFuncs\_compare[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_compare "Link to this definition")\
  \
\
Computes a comparison for [`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")\
, implements `PyArray_CompareFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_argmax[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_argmax "Link to this definition")\
  \
\
Computes the argmax for [`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")\
, implements `PyArray_ArgFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_argmin[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_argmin "Link to this definition")\
  \
\
Computes the argmin for [`numpy.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")\
, implements `PyArray_ArgFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_dotfunc[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_dotfunc "Link to this definition")\
  \
\
Computes the dot product for [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")\
, implements `PyArray_DotFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_scanfunc[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_scanfunc "Link to this definition")\
  \
\
A formatted input function for [`numpy.fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")\
, implements `PyArray_ScanFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_fromstr[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_fromstr "Link to this definition")\
  \
\
A string parsing function for [`numpy.fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")\
, implements `PyArray_FromStrFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_nonzero[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_nonzero "Link to this definition")\
  \
\
Computes the nonzero function for [`numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")\
, implements `PyArray_NonzeroFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_fill[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_fill "Link to this definition")\
  \
\
An array filling function for [`numpy.ndarray.fill`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill")\
, implements `PyArray_FillFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_fillwithscalar[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_fillwithscalar "Link to this definition")\
  \
\
A function to fill an array with a scalar value for [`numpy.ndarray.fill`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill")\
, implements `PyArray_FillWithScalarFunc`.\
\
NPY\_DT\_PyArray\_ArrFuncs\_sort[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_sort "Link to this definition")\
  \
\
An array of PyArray\_SortFunc of length `NPY_NSORTS`. If set, allows defining custom sorting implementations for each of the sorting algorithms numpy implements.\
\
NPY\_DT\_PyArray\_ArrFuncs\_argsort[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_PyArray_ArrFuncs_argsort "Link to this definition")\
  \
\
An array of PyArray\_ArgSortFunc of length `NPY_NSORTS`. If set, allows defining custom argsorting implementations for each of the sorting algorithms numpy implements.\
\
### Macros and Static Inline Functions[#](https://numpy.org/doc/stable/reference/c-api/array.html#macros-and-static-inline-functions "Link to this heading")\
\
These macros and static inline functions are provided to allow more understandable and idiomatic code when working with `PyArray_DTypeMeta` instances.\
\
NPY\_DTYPE(descr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DTYPE "Link to this definition")\
  \
\
Returns a `PyArray_DTypeMeta *` pointer to the DType of a given descriptor instance.\
\
static inline [PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*NPY\_DT\_NewRef([PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")\
 \*o)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DT_NewRef "Link to this definition")\
  \
\
Returns a `PyArray_DTypeMeta *` pointer to a new reference to a DType.\
\
Conversion utilities[#](https://numpy.org/doc/stable/reference/c-api/array.html#conversion-utilities "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------\
\
### For use with [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "(in Python v3.14)")\
[#](https://numpy.org/doc/stable/reference/c-api/array.html#for-use-with-pyarg-parsetuple "Link to this heading")\
\
All of these functions can be used in [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "(in Python v3.14)")\
 (…) with the “O&” format specifier to automatically convert any Python object to the required C-object. All of these functions return [`NPY_SUCCEED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SUCCEED "NPY_SUCCEED")\
 if successful and [`NPY_FAIL`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FAIL "NPY_FAIL")\
 if not. The first argument to all of these function is a Python object. The second argument is the **address** of the C-type to convert the Python object to.\
\
Warning\
\
Be sure to understand what steps you should take to manage the memory when using these conversion functions. These functions can require freeing memory, and/or altering the reference counts of specific objects based on your use.\
\
int PyArray\_Converter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*\*address)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Converter "Link to this definition")\
  \
\
Convert any Python object to a [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
. If [`PyArray_Check`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Check "PyArray_Check")\
 (_obj_) is TRUE then its reference count is incremented and a reference placed in _address_. If _obj_ is not an array, then convert it to an array using [`PyArray_FromAny`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny")\
 . No matter what is returned, you must DECREF the object returned by this routine in _address_ when you are done with it.\
\
int PyArray\_OutputConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*\*address)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_OutputConverter "Link to this definition")\
  \
\
This is a default converter for output arrays given to functions. If _obj_ is [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "(in Python v3.14)")\
 or `NULL`, then _\*address_ will be `NULL` but the call will succeed. If [`PyArray_Check`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Check "PyArray_Check")\
 ( _obj_) is TRUE then it is returned in _\*address_ without incrementing its reference count.\
\
int PyArray\_IntpConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArray\_Dims](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims "PyArray_Dims")\
 \*seq)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IntpConverter "Link to this definition")\
  \
\
Convert any Python sequence, _obj_, smaller than [`NPY_MAXDIMS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MAXDIMS "NPY_MAXDIMS")\
 to a C-array of [`npy_intp`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
. The Python object could also be a single number. The _seq_ variable is a pointer to a structure with members ptr and len. On successful return, _seq_ ->ptr contains a pointer to memory that must be freed, by calling [`PyDimMem_FREE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDimMem_FREE "PyDimMem_FREE")\
, to avoid a memory leak. The restriction on memory size allows this converter to be conveniently used for sequences intended to be interpreted as array shapes.\
\
int PyArray\_BufferConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [PyArray\_Chunk](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk "PyArray_Chunk")\
 \*buf)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_BufferConverter "Link to this definition")\
  \
\
Convert any Python object, _obj_, with a (single-segment) buffer interface to a variable with members that detail the object’s use of its chunk of memory. The _buf_ variable is a pointer to a structure with base, ptr, len, and flags members. The [`PyArray_Chunk`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk "PyArray_Chunk")\
 structure is binary compatible with the Python’s buffer object (through its len member on 32-bit platforms and its ptr member on 64-bit platforms). On return, the base member is set to _obj_ (or its base if _obj_ is already a buffer object pointing to another object). If you need to hold on to the memory be sure to INCREF the base member. The chunk of memory is pointed to by _buf_ ->ptr member and has length _buf_ ->len. The flags member of _buf_ is [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")\
 with the [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")\
 flag set if _obj_ has a writeable buffer interface.\
\
int PyArray\_AxisConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, int \*axis)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_AxisConverter "Link to this definition")\
  \
\
Convert a Python object, _obj_, representing an axis argument to the proper value for passing to the functions that take an integer axis. Specifically, if _obj_ is None, _axis_ is set to [`NPY_RAVEL_AXIS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_RAVEL_AXIS "NPY_RAVEL_AXIS")\
 which is interpreted correctly by the C-API functions that take axis arguments.\
\
int PyArray\_BoolConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")\
 \*value)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_BoolConverter "Link to this definition")\
  \
\
Convert any Python object, _obj_, to [`NPY_TRUE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "NPY_TRUE")\
 or [`NPY_FALSE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FALSE "NPY_FALSE")\
, and place the result in _value_.\
\
int PyArray\_ByteorderConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, char \*endian)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ByteorderConverter "Link to this definition")\
  \
\
Convert Python strings into the corresponding byte-order character: ‘>’, ‘<’, ‘s’, ‘=’, or ‘|’.\
\
int PyArray\_SortkindConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [NPY\_SORTKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND "NPY_SORTKIND")\
 \*sort)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SortkindConverter "Link to this definition")\
  \
\
Convert Python strings into one of [`NPY_QUICKSORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_QUICKSORT "NPY_QUICKSORT")\
 (starts with ‘q’ or ‘Q’), [`NPY_HEAPSORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_HEAPSORT "NPY_HEAPSORT")\
 (starts with ‘h’ or ‘H’), [`NPY_MERGESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_MERGESORT "NPY_MERGESORT")\
 (starts with ‘m’ or ‘M’) or [`NPY_STABLESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_STABLESORT "NPY_STABLESORT")\
 (starts with ‘t’ or ‘T’). [`NPY_MERGESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_MERGESORT "NPY_MERGESORT")\
 and [`NPY_STABLESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_STABLESORT "NPY_STABLESORT")\
 are aliased to each other for backwards compatibility and may refer to one of several stable sorting algorithms depending on the data type.\
\
int PyArray\_SearchsideConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [NPY\_SEARCHSIDE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE "NPY_SEARCHSIDE")\
 \*side)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SearchsideConverter "Link to this definition")\
  \
\
Convert Python strings into one of [`NPY_SEARCHLEFT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHLEFT "NPY_SEARCHLEFT")\
 (starts with ‘l’ or ‘L’), or [`NPY_SEARCHRIGHT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHRIGHT "NPY_SEARCHRIGHT")\
 (starts with ‘r’ or ‘R’).\
\
int PyArray\_OrderConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [NPY\_ORDER](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")\
 \*order)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_OrderConverter "Link to this definition")\
  \
\
Convert the Python strings ‘C’, ‘F’, ‘A’, and ‘K’ into the [`NPY_ORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "NPY_ORDER")\
 enumeration [`NPY_CORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_CORDER "NPY_CORDER")\
, [`NPY_FORTRANORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_FORTRANORDER "NPY_FORTRANORDER")\
, [`NPY_ANYORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_ANYORDER "NPY_ANYORDER")\
, and [`NPY_KEEPORDER`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_KEEPORDER "NPY_KEEPORDER")\
.\
\
int PyArray\_CastingConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")\
 \*casting)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_CastingConverter "Link to this definition")\
  \
\
Convert the Python strings ‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, and ‘unsafe’ into the [`NPY_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")\
 enumeration [`NPY_NO_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_NO_CASTING "NPY_NO_CASTING")\
, [`NPY_EQUIV_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_EQUIV_CASTING "NPY_EQUIV_CASTING")\
, [`NPY_SAFE_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_SAFE_CASTING "NPY_SAFE_CASTING")\
, [`NPY_SAME_KIND_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_SAME_KIND_CASTING "NPY_SAME_KIND_CASTING")\
, and [`NPY_UNSAFE_CASTING`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_UNSAFE_CASTING "NPY_UNSAFE_CASTING")\
.\
\
int PyArray\_ClipmodeConverter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*object, [NPY\_CLIPMODE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")\
 \*val)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ClipmodeConverter "Link to this definition")\
  \
\
Convert the Python strings ‘clip’, ‘wrap’, and ‘raise’ into the [`NPY_CLIPMODE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")\
 enumeration [`NPY_CLIP`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_CLIP "NPY_CLIP")\
, [`NPY_WRAP`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_WRAP "NPY_WRAP")\
, and [`NPY_RAISE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_RAISE "NPY_RAISE")\
.\
\
int PyArray\_ConvertClipmodeSequence([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*object, [NPY\_CLIPMODE](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")\
 \*modes, int n)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ConvertClipmodeSequence "Link to this definition")\
  \
\
Converts either a sequence of clipmodes or a single clipmode into a C array of [`NPY_CLIPMODE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "NPY_CLIPMODE")\
 values. The number of clipmodes _n_ must be known before calling this function. This function is provided to help functions allow a different clipmode for each dimension.\
\
### Other conversions[#](https://numpy.org/doc/stable/reference/c-api/array.html#other-conversions "Link to this heading")\
\
int PyArray\_PyIntAsInt([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_PyIntAsInt "Link to this definition")\
  \
\
Convert all kinds of Python objects (including arrays and array scalars) to a standard integer. On error, -1 is returned and an exception set. You may find useful the macro:\
\
#define error\_converting(x) (((x) == -1) && PyErr\_Occurred())\
\
Copy to clipboard\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 PyArray\_PyIntAsIntp([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*op)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_PyIntAsIntp "Link to this definition")\
  \
\
Convert all kinds of Python objects (including arrays and array scalars) to a (platform-pointer-sized) integer. On error, -1 is returned and an exception set.\
\
int PyArray\_IntpFromSequence([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*seq, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*vals, int maxvals)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IntpFromSequence "Link to this definition")\
  \
\
Convert any Python sequence (or single Python number) passed in as _seq_ to (up to) _maxvals_ pointer-sized integers and place them in the _vals_ array. The sequence can be smaller then _maxvals_ as the number of converted objects is returned.\
\
Including and importing the C API[#](https://numpy.org/doc/stable/reference/c-api/array.html#including-and-importing-the-c-api "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------\
\
To use the NumPy C-API you typically need to include the `numpy/ndarrayobject.h` header and `numpy/ufuncobject.h` for some ufunc related functionality (`arrayobject.h` is an alias for `ndarrayobject.h`).\
\
These two headers export most relevant functionality. In general any project which uses the NumPy API must import NumPy using one of the functions `PyArray_ImportNumPyAPI()` or `import_array()`. In some places, functionality which requires `import_array()` is not needed, because you only need type definitions. In this case, it is sufficient to include `numpy/ndarratypes.h`.\
\
For the typical Python project, multiple C or C++ files will be compiled into a single shared object (the Python C-module) and `PyArray_ImportNumPyAPI()` should be called inside it’s module initialization.\
\
When you have a single C-file, this will consist of:\
\
#include "numpy/ndarrayobject.h"\
\
PyMODINIT\_FUNC PyInit\_my\_module(void)\
{\
    if (PyArray\_ImportNumPyAPI() < 0) {\
        return NULL;\
    }\
    /\* Other initialization code. \*/\
}\
\
Copy to clipboard\
\
However, most projects will have additional C files which are all linked together into a single Python module. In this case, the helper C files typically do not have a canonical place where `PyArray_ImportNumPyAPI` should be called (although it is OK and fast to call it often).\
\
To solve this, NumPy provides the following pattern that the main file is modified to define `PY_ARRAY_UNIQUE_SYMBOL` before the include:\
\
/\* Main module file \*/\
#define PY\_ARRAY\_UNIQUE\_SYMBOL MyModule\
#include "numpy/ndarrayobject.h"\
\
PyMODINIT\_FUNC PyInit\_my\_module(void)\
{\
    if (PyArray\_ImportNumPyAPI() < 0) {\
        return NULL;\
    }\
    /\* Other initialization code. \*/\
}\
\
Copy to clipboard\
\
while the other files use:\
\
/\* Second file without any import \*/\
#define NO\_IMPORT\_ARRAY\
#define PY\_ARRAY\_UNIQUE\_SYMBOL MyModule\
#include "numpy/ndarrayobject.h"\
\
Copy to clipboard\
\
You can of course add the defines to a local header used throughout. You just have to make sure that the main file does \_not\_ define `NO_IMPORT_ARRAY`.\
\
For `numpy/ufuncobject.h` the same logic applies, but the unique symbol mechanism is `#define PY_UFUNC_UNIQUE_SYMBOL` (both can match).\
\
Additionally, you will probably wish to add a `#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION` to avoid warnings about possible use of old API.\
\
Note\
\
If you are experiencing access violations make sure that the NumPy API was properly imported and the symbol `PyArray_API` is not `NULL`. When in a debugger, this symbols actual name will be `PY_ARRAY_UNIQUE_SYMBOL``+``PyArray_API`, so for example `MyModulePyArray_API` in the above. (E.g. even a `printf("%p\n", PyArray_API);` just before the crash.)\
\
### Mechanism details and dynamic linking[#](https://numpy.org/doc/stable/reference/c-api/array.html#mechanism-details-and-dynamic-linking "Link to this heading")\
\
The main part of the mechanism is that without NumPy needs to define a `void **PyArray_API` table for you to look up all functions. Depending on your macro setup, this takes different routes depending on whether [`NO_IMPORT_ARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NO_IMPORT_ARRAY "NO_IMPORT_ARRAY")\
 and [`PY_ARRAY_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PY_ARRAY_UNIQUE_SYMBOL "PY_ARRAY_UNIQUE_SYMBOL")\
 are defined:\
\
*   If neither is defined, the C-API is declared to `static void **PyArray_API`, so it is only visible within the compilation unit/file using `#include <numpy/arrayobject.h>`.\
    \
*   If only `PY_ARRAY_UNIQUE_SYMBOL` is defined (it could be empty) then the it is declared to a non-static `void **` allowing it to be used by other files which are linked.\
    \
*   If `NO_IMPORT_ARRAY` is defined, the table is declared as `extern void **`, meaning that it must be linked to a file which does not use `NO_IMPORT_ARRAY`.\
    \
\
The `PY_ARRAY_UNIQUE_SYMBOL` mechanism additionally mangles the names to avoid conflicts.\
\
Changed in version NumPy: 2.1 changed the headers to avoid sharing the table outside of a single shared object/dll (this was always the case on Windows). Please see [`NPY_API_SYMBOL_ATTRIBUTE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_API_SYMBOL_ATTRIBUTE "NPY_API_SYMBOL_ATTRIBUTE")\
 for details.\
\
In order to make use of the C-API from another extension module, the [`import_array`](https://numpy.org/doc/stable/reference/c-api/array.html#c.import_array "import_array")\
 function must be called. If the extension module is self-contained in a single .c file, then that is all that needs to be done. If, however, the extension module involves multiple files where the C-API is needed then some additional steps must be taken.\
\
int PyArray\_ImportNumPyAPI(void)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ImportNumPyAPI "Link to this definition")\
  \
\
Ensures that the NumPy C-API is imported and usable. It returns `0` on success and `-1` with an error set if NumPy couldn’t be imported. While preferable to call it once at module initialization, this function is very light-weight if called multiple times.\
\
New in version 2.0: This function is backported in the `npy_2_compat.h` header.\
\
import\_array(void)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.import_array "Link to this definition")\
  \
\
This function must be called in the initialization section of a module that will make use of the C-API. It imports the module where the function-pointer table is stored and points the correct variable to it. This macro includes a `return NULL;` on error, so that `PyArray_ImportNumPyAPI()` is preferable for custom error checking. You may also see use of `_import_array()` (a function, not a macro, but you may want to raise a better error if it fails) and the variations `import_array1(ret)` which customizes the return value.\
\
PY\_ARRAY\_UNIQUE\_SYMBOL[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PY_ARRAY_UNIQUE_SYMBOL "Link to this definition")\
  \
\
NPY\_API\_SYMBOL\_ATTRIBUTE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_API_SYMBOL_ATTRIBUTE "Link to this definition")\
  \
\
New in version 2.1.\
\
An additional symbol which can be used to share e.g. visibility beyond shared object boundaries. By default, NumPy adds the C visibility hidden attribute (if available): `void __attribute__((visibility("hidden"))) **PyArray_API;`. You can change this by defining `NPY_API_SYMBOL_ATTRIBUTE`, which will make this: `void NPY_API_SYMBOL_ATTRIBUTE **PyArray_API;` (with additional name mangling via the unique symbol).\
\
Adding an empty `#define NPY_API_SYMBOL_ATTRIBUTE` will have the same behavior as NumPy 1.x.\
\
Note\
\
Windows never had shared visibility although you can use this macro to achieve it. We generally discourage sharing beyond shared boundary lines since importing the array API includes NumPy version checks.\
\
NO\_IMPORT\_ARRAY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NO_IMPORT_ARRAY "Link to this definition")\
  \
\
Defining `NO_IMPORT_ARRAY` before the `ndarrayobject.h` include indicates that the NumPy C API import is handled in a different file and the include mechanism will not be added here. You must have one file without `NO_IMPORT_ARRAY` defined.\
\
#define PY\_ARRAY\_UNIQUE\_SYMBOL cool\_ARRAY\_API\
#include <numpy/arrayobject.h>\
\
Copy to clipboard\
\
On the other hand, coolhelper.c would contain at the top:\
\
#define NO\_IMPORT\_ARRAY\
#define PY\_ARRAY\_UNIQUE\_SYMBOL cool\_ARRAY\_API\
#include <numpy/arrayobject.h>\
\
Copy to clipboard\
\
You can also put the common two last lines into an extension-local header file as long as you make sure that NO\_IMPORT\_ARRAY is #defined before #including that file.\
\
Internally, these #defines work as follows:\
\
*   If neither is defined, the C-API is declared to be `static void**`, so it is only visible within the compilation unit that #includes numpy/arrayobject.h.\
    \
*   If [`PY_ARRAY_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PY_ARRAY_UNIQUE_SYMBOL "PY_ARRAY_UNIQUE_SYMBOL")\
     is #defined, but [`NO_IMPORT_ARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NO_IMPORT_ARRAY "NO_IMPORT_ARRAY")\
     is not, the C-API is declared to be `void**`, so that it will also be visible to other compilation units.\
    \
*   If [`NO_IMPORT_ARRAY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NO_IMPORT_ARRAY "NO_IMPORT_ARRAY")\
     is #defined, regardless of whether [`PY_ARRAY_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PY_ARRAY_UNIQUE_SYMBOL "PY_ARRAY_UNIQUE_SYMBOL")\
     is, the C-API is declared to be `extern void**`, so it is expected to be defined in another compilation unit.\
    \
*   Whenever [`PY_ARRAY_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PY_ARRAY_UNIQUE_SYMBOL "PY_ARRAY_UNIQUE_SYMBOL")\
     is #defined, it also changes the name of the variable holding the C-API, which defaults to `PyArray_API`, to whatever the macro is #defined to.\
    \
\
### Checking the API Version[#](https://numpy.org/doc/stable/reference/c-api/array.html#checking-the-api-version "Link to this heading")\
\
Because python extensions are not used in the same way as usual libraries on most platforms, some errors cannot be automatically detected at build time or even runtime. For example, if you build an extension using a function available only for numpy >= 1.3.0, and you import the extension later with numpy 1.2, you will not get an import error (but almost certainly a segmentation fault when calling the function). That’s why several functions are provided to check for numpy versions. The macros [`NPY_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_VERSION "NPY_VERSION")\
 and [`NPY_FEATURE_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FEATURE_VERSION "NPY_FEATURE_VERSION")\
 corresponds to the numpy version used to build the extension, whereas the versions returned by the functions [`PyArray_GetNDArrayCVersion`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetNDArrayCVersion "PyArray_GetNDArrayCVersion")\
 and [`PyArray_GetNDArrayCFeatureVersion`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetNDArrayCFeatureVersion "PyArray_GetNDArrayCFeatureVersion")\
 corresponds to the runtime numpy’s version.\
\
The rules for ABI and API compatibilities can be summarized as follows:\
\
*   Whenever [`NPY_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_VERSION "NPY_VERSION")\
     != `PyArray_GetNDArrayCVersion()`, the extension has to be recompiled (ABI incompatibility).\
    \
*   [`NPY_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_VERSION "NPY_VERSION")\
     == `PyArray_GetNDArrayCVersion()` and [`NPY_FEATURE_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FEATURE_VERSION "NPY_FEATURE_VERSION")\
     <= `PyArray_GetNDArrayCFeatureVersion()` means backward compatible changes.\
    \
\
ABI incompatibility is automatically detected in every numpy’s version. API incompatibility detection was added in numpy 1.4.0. If you want to supported many different numpy versions with one extension binary, you have to build your extension with the lowest [`NPY_FEATURE_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FEATURE_VERSION "NPY_FEATURE_VERSION")\
 as possible.\
\
NPY\_VERSION[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_VERSION "Link to this definition")\
  \
\
The current version of the ndarray object (check to see if this variable is defined to guarantee the `numpy/arrayobject.h` header is being used).\
\
NPY\_FEATURE\_VERSION[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FEATURE_VERSION "Link to this definition")\
  \
\
The current version of the C-API.\
\
unsigned int PyArray\_GetNDArrayCVersion(void)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetNDArrayCVersion "Link to this definition")\
  \
\
This just returns the value [`NPY_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_VERSION "NPY_VERSION")\
. [`NPY_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_VERSION "NPY_VERSION")\
 changes whenever a backward incompatible change at the ABI level. Because it is in the C-API, however, comparing the output of this function from the value defined in the current header gives a way to test if the C-API has changed thus requiring a re-compilation of extension modules that use the C-API. This is automatically checked in the function [`import_array`](https://numpy.org/doc/stable/reference/c-api/array.html#c.import_array "import_array")\
.\
\
unsigned int PyArray\_GetNDArrayCFeatureVersion(void)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetNDArrayCFeatureVersion "Link to this definition")\
  \
\
This just returns the value [`NPY_FEATURE_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FEATURE_VERSION "NPY_FEATURE_VERSION")\
. [`NPY_FEATURE_VERSION`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FEATURE_VERSION "NPY_FEATURE_VERSION")\
 changes whenever the API changes (e.g. a function is added). A changed value does not always require a recompile.\
\
### Memory management[#](https://numpy.org/doc/stable/reference/c-api/array.html#memory-management "Link to this heading")\
\
char \*PyDataMem\_NEW(size\_t nbytes)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_NEW "Link to this definition")\
  \
\
void PyDataMem\_FREE(char \*ptr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_FREE "Link to this definition")\
  \
\
char \*PyDataMem\_RENEW(void \*ptr, size\_t newbytes)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_RENEW "Link to this definition")\
  \
\
Functions to allocate, free, and reallocate memory. These are used internally to manage array data memory unless overridden.\
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*PyDimMem\_NEW(int nd)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDimMem_NEW "Link to this definition")\
  \
\
void PyDimMem\_FREE(char \*ptr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDimMem_FREE "Link to this definition")\
  \
\
[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*PyDimMem\_RENEW(void \*ptr, size\_t newnd)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDimMem_RENEW "Link to this definition")\
  \
\
Macros to allocate, free, and reallocate dimension and strides memory.\
\
void \*PyArray\_malloc(size\_t nbytes)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_malloc "Link to this definition")\
  \
\
void PyArray\_free(void \*ptr)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_free "Link to this definition")\
  \
\
void \*PyArray\_realloc([npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")\
 \*ptr, size\_t nbytes)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_realloc "Link to this definition")\
  \
\
These macros use different memory allocators, depending on the constant [`NPY_USE_PYMEM`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_realloc.NPY_USE_PYMEM "NPY_USE_PYMEM")\
. The system malloc is used when [`NPY_USE_PYMEM`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_realloc.NPY_USE_PYMEM "NPY_USE_PYMEM")\
 is 0, if [`NPY_USE_PYMEM`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_realloc.NPY_USE_PYMEM "NPY_USE_PYMEM")\
 is 1, then the Python memory allocator is used.\
\
NPY\_USE\_PYMEM[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_realloc.NPY_USE_PYMEM "Link to this definition")\
  \
\
int PyArray\_ResolveWritebackIfCopy([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "Link to this definition")\
  \
\
If `obj->flags` has [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")\
, this function clears the flags, `DECREF` s `obj->base` and makes it writeable, and sets `obj->base` to NULL. It then copies `obj->data` to `obj->base->data`, and returns the error state of the copy operation. This is the opposite of [`PyArray_SetWritebackIfCopyBase`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetWritebackIfCopyBase "PyArray_SetWritebackIfCopyBase")\
. Usually this is called once you are finished with `obj`, just before `Py_DECREF(obj)`. It may be called multiple times, or with `NULL` input. See also [`PyArray_DiscardWritebackIfCopy`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DiscardWritebackIfCopy "PyArray_DiscardWritebackIfCopy")\
.\
\
Returns 0 if nothing was done, -1 on error, and 1 if action was taken.\
\
### Threading support[#](https://numpy.org/doc/stable/reference/c-api/array.html#threading-support "Link to this heading")\
\
These macros are only meaningful if [`NPY_ALLOW_THREADS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_THREADS "NPY_ALLOW_THREADS")\
 evaluates True during compilation of the extension module. Otherwise, these macros are equivalent to whitespace. Python uses a single Global Interpreter Lock (GIL) for each Python process so that only a single thread may execute at a time (even on multi-cpu machines). When calling out to a compiled function that may take time to compute (and does not have side-effects for other threads like updated global variables), the GIL should be released so that other Python threads can run while the time-consuming calculations are performed. This can be accomplished using two groups of macros. Typically, if one macro in a group is used in a code block, all of them must be used in the same code block. [`NPY_ALLOW_THREADS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_THREADS "NPY_ALLOW_THREADS")\
 is true (defined as `1`) unless the build option `-Ddisable-threading` is set to `true` - in which case [`NPY_ALLOW_THREADS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_THREADS "NPY_ALLOW_THREADS")\
 is false (`0`).\
\
NPY\_ALLOW\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_THREADS "Link to this definition")\
  \
\
#### Group 1[#](https://numpy.org/doc/stable/reference/c-api/array.html#group-1 "Link to this heading")\
\
This group is used to call code that may take some time but does not use any Python C-API calls. Thus, the GIL should be released during its calculation.\
\
NPY\_BEGIN\_ALLOW\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BEGIN_ALLOW_THREADS "Link to this definition")\
  \
\
Equivalent to [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS "(in Python v3.14)")\
 except it uses [`NPY_ALLOW_THREADS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_THREADS "NPY_ALLOW_THREADS")\
 to determine if the macro if replaced with white-space or not.\
\
NPY\_END\_ALLOW\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_END_ALLOW_THREADS "Link to this definition")\
  \
\
Equivalent to [`Py_END_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_END_ALLOW_THREADS "(in Python v3.14)")\
 except it uses [`NPY_ALLOW_THREADS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_THREADS "NPY_ALLOW_THREADS")\
 to determine if the macro if replaced with white-space or not.\
\
NPY\_BEGIN\_THREADS\_DEF[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BEGIN_THREADS_DEF "Link to this definition")\
  \
\
Place in the variable declaration area. This macro sets up the variable needed for storing the Python state.\
\
NPY\_BEGIN\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BEGIN_THREADS "Link to this definition")\
  \
\
Place right before code that does not need the Python interpreter (no Python C-API calls). This macro saves the Python state and releases the GIL.\
\
NPY\_END\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_END_THREADS "Link to this definition")\
  \
\
Place right after code that does not need the Python interpreter. This macro acquires the GIL and restores the Python state from the saved variable.\
\
void NPY\_BEGIN\_THREADS\_DESCR([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BEGIN_THREADS_DESCR "Link to this definition")\
  \
\
Useful to release the GIL only if _dtype_ does not contain arbitrary Python objects which may need the Python interpreter during execution of the loop.\
\
void NPY\_END\_THREADS\_DESCR([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")\
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_END_THREADS_DESCR "Link to this definition")\
  \
\
Useful to regain the GIL in situations where it was released using the BEGIN form of this macro.\
\
void NPY\_BEGIN\_THREADS\_THRESHOLDED(int loop\_size)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BEGIN_THREADS_THRESHOLDED "Link to this definition")\
  \
\
Useful to release the GIL only if _loop\_size_ exceeds a minimum threshold, currently set to 500. Should be matched with a [`NPY_END_THREADS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_END_THREADS "NPY_END_THREADS")\
 to regain the GIL.\
\
#### Group 2[#](https://numpy.org/doc/stable/reference/c-api/array.html#group-2 "Link to this heading")\
\
This group is used to re-acquire the Python GIL after it has been released. For example, suppose the GIL has been released (using the previous calls), and then some path in the code (perhaps in a different subroutine) requires use of the Python C-API, then these macros are useful to acquire the GIL. These macros accomplish essentially a reverse of the previous three (acquire the LOCK saving what state it had) and then re-release it with the saved state.\
\
NPY\_ALLOW\_C\_API\_DEF[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_C_API_DEF "Link to this definition")\
  \
\
Place in the variable declaration area to set up the necessary variable.\
\
NPY\_ALLOW\_C\_API[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ALLOW_C_API "Link to this definition")\
  \
\
Place before code that needs to call the Python C-API (when it is known that the GIL has already been released).\
\
NPY\_DISABLE\_C\_API[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_DISABLE_C_API "Link to this definition")\
  \
\
Place after code that needs to call the Python C-API (to re-release the GIL).\
\
Tip\
\
Never use semicolons after the threading support macros.\
\
### Priority[#](https://numpy.org/doc/stable/reference/c-api/array.html#priority "Link to this heading")\
\
NPY\_PRIORITY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_PRIORITY "Link to this definition")\
  \
\
Default priority for arrays.\
\
NPY\_SUBTYPE\_PRIORITY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SUBTYPE_PRIORITY "Link to this definition")\
  \
\
Default subtype priority.\
\
NPY\_SCALAR\_PRIORITY[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALAR_PRIORITY "Link to this definition")\
  \
\
Default scalar priority (very small)\
\
double PyArray\_GetPriority([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")\
 \*obj, double def)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_GetPriority "Link to this definition")\
  \
\
Return the [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")\
 attribute (converted to a double) of _obj_ or _def_ if no attribute of that name exists. Fast returns that avoid the attribute lookup are provided for objects of type [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")\
.\
\
### Default buffers[#](https://numpy.org/doc/stable/reference/c-api/array.html#default-buffers "Link to this heading")\
\
NPY\_BUFSIZE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BUFSIZE "Link to this definition")\
  \
\
Default size of the user-settable internal buffers.\
\
NPY\_MIN\_BUFSIZE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MIN_BUFSIZE "Link to this definition")\
  \
\
Smallest size of user-settable internal buffers.\
\
NPY\_MAX\_BUFSIZE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MAX_BUFSIZE "Link to this definition")\
  \
\
Largest size allowed for the user-settable buffers.\
\
### Other constants[#](https://numpy.org/doc/stable/reference/c-api/array.html#other-constants "Link to this heading")\
\
NPY\_NUM\_FLOATTYPE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_NUM_FLOATTYPE "Link to this definition")\
  \
\
The number of floating-point types\
\
NPY\_MAXDIMS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MAXDIMS "Link to this definition")\
  \
\
The maximum number of dimensions that may be used by NumPy. This is set to 64 and was 32 before NumPy 2.\
\
Note\
\
We encourage you to avoid `NPY_MAXDIMS`. A future version of NumPy may wish to remove any dimension limitation (and thus the constant). The limitation was created so that NumPy can use stack allocations internally for scratch space.\
\
If your algorithm has a reasonable maximum number of dimension you could check and use that locally.\
\
NPY\_MAXARGS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MAXARGS "Link to this definition")\
  \
\
The maximum number of array arguments that can be used in some functions. This used to be 32 before NumPy 2 and is now 64. To continue to allow using it as a check whether a number of arguments is compatible ufuncs, this macro is now runtime dependent.\
\
Note\
\
We discourage any use of `NPY_MAXARGS` that isn’t explicitly tied to checking for known NumPy limitations.\
\
NPY\_FALSE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FALSE "Link to this definition")\
  \
\
Defined as 0 for use with Bool.\
\
NPY\_TRUE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_TRUE "Link to this definition")\
  \
\
Defined as 1 for use with Bool.\
\
NPY\_FAIL[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_FAIL "Link to this definition")\
  \
\
The return value of failed converter functions which are called using the “O&” syntax in [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "(in Python v3.14)")\
\-like functions.\
\
NPY\_SUCCEED[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SUCCEED "Link to this definition")\
  \
\
The return value of successful converter functions which are called using the “O&” syntax in [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "(in Python v3.14)")\
\-like functions.\
\
NPY\_RAVEL\_AXIS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_RAVEL_AXIS "Link to this definition")\
  \
\
Some NumPy functions (mainly the C-entrypoints for Python functions) have an `axis` argument. This macro may be passed for `axis=None`.\
\
Note\
\
This macro is NumPy version dependent at runtime. The value is now the minimum integer. However, on NumPy 1.x `NPY_MAXDIMS` was used (at the time set to 32).\
\
### Miscellaneous Macros[#](https://numpy.org/doc/stable/reference/c-api/array.html#miscellaneous-macros "Link to this heading")\
\
int PyArray\_SAMESHAPE([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*a1, [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*a2)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SAMESHAPE "Link to this definition")\
  \
\
Evaluates as True if arrays _a1_ and _a2_ have the same shape.\
\
PyArray\_MAX(a, b)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MAX "Link to this definition")\
  \
\
Returns the maximum of _a_ and _b_. If (_a_) or (_b_) are expressions they are evaluated twice.\
\
PyArray\_MIN(a, b)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MIN "Link to this definition")\
  \
\
Returns the minimum of _a_ and _b_. If (_a_) or (_b_) are expressions they are evaluated twice.\
\
void PyArray\_DiscardWritebackIfCopy([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")\
 \*obj)[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DiscardWritebackIfCopy "Link to this definition")\
  \
\
If `obj->flags` has [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")\
, this function clears the flags, _DECREF_ s `obj->base` and makes it writeable, and sets `obj->base` to NULL. In contrast to [`PyArray_ResolveWritebackIfCopy`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "PyArray_ResolveWritebackIfCopy")\
 it makes no attempt to copy the data from `obj->base`. This undoes [`PyArray_SetWritebackIfCopyBase`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_SetWritebackIfCopyBase "PyArray_SetWritebackIfCopyBase")\
. Usually this is called after an error when you are finished with `obj`, just before `Py_DECREF(obj)`. It may be called multiple times, or with `NULL` input.\
\
### Enumerated Types[#](https://numpy.org/doc/stable/reference/c-api/array.html#enumerated-types "Link to this heading")\
\
enum NPY\_SORTKIND[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND "Link to this definition")\
  \
\
A special variable-type which can take on different values to indicate the sorting algorithm being used. These algorithm types have not been treated strictly for some time, but rather treated as stable/not stable. In NumPy 2.4 they are replaced by requirements (see below), but done in a backwards compatible way. These values will continue to work, except that that NPY\_HEAPSORT will do the same thing as NPY\_QUICKSORT.\
\
enumerator NPY\_QUICKSORT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_QUICKSORT "Link to this definition")\
  \
\
enumerator NPY\_HEAPSORT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_HEAPSORT "Link to this definition")\
  \
\
enumerator NPY\_MERGESORT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_MERGESORT "Link to this definition")\
  \
\
enumerator NPY\_STABLESORT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_STABLESORT "Link to this definition")\
  \
\
Used as an alias of [`NPY_MERGESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_MERGESORT "NPY_MERGESORT")\
 and vice versa.\
\
enumerator NPY\_NSORTS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_NSORTS "Link to this definition")\
  \
\
Defined to be the number of sorts. It is fixed at three by the need for backwards compatibility, and consequently [`NPY_MERGESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_MERGESORT "NPY_MERGESORT")\
 and [`NPY_STABLESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_STABLESORT "NPY_STABLESORT")\
 are aliased to each other and may refer to one of several stable sorting algorithms depending on the data type.\
\
In NumPy 2.4 the algorithm names are replaced by requirements. You can still use the old values, a recompile is not needed, but they are reinterpreted such that\
\
*   NPY\_QUICKSORT and NPY\_HEAPSORT -> NPY\_SORT\_DEFAULT\
    \
*   NPY\_MERGESORT and NPY\_STABLE -> NPY\_SORT\_STABLE\
    \
\
enumerator NPY\_SORT\_DEFAULT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_SORT_DEFAULT "Link to this definition")\
  \
\
The default sort for the type. For the NumPy builtin types it may be stable or not, but will be ascending and sort NaN types to the end. It is usually chosen for speed and/or low memory.\
\
enumerator NPY\_SORT\_STABLE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_SORT_STABLE "Link to this definition")\
  \
\
(Requirement) Specifies that the sort must be stable.\
\
enumerator NPY\_SORT\_DESCENDING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_SORT_DESCENDING "Link to this definition")\
  \
\
(Requirement) Specifies that the sort must be in descending order. This functionality is not yet implemented for any of the NumPy types and cannot yet be set from the Python interface.\
\
enum NPY\_SCALARKIND[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND "Link to this definition")\
  \
\
A special variable type indicating the number of “kinds” of scalars distinguished in determining scalar-coercion rules. This variable can take on the values:\
\
enumerator NPY\_NOSCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "Link to this definition")\
  \
\
enumerator NPY\_BOOL\_SCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_BOOL_SCALAR "Link to this definition")\
  \
\
enumerator NPY\_INTPOS\_SCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_INTPOS_SCALAR "Link to this definition")\
  \
\
enumerator NPY\_INTNEG\_SCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_INTNEG_SCALAR "Link to this definition")\
  \
\
enumerator NPY\_FLOAT\_SCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_FLOAT_SCALAR "Link to this definition")\
  \
\
enumerator NPY\_COMPLEX\_SCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_COMPLEX_SCALAR "Link to this definition")\
  \
\
enumerator NPY\_OBJECT\_SCALAR[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_OBJECT_SCALAR "Link to this definition")\
  \
\
enumerator NPY\_NSCALARKINDS[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NSCALARKINDS "Link to this definition")\
  \
\
Defined to be the number of scalar kinds (not including [`NPY_NOSCALAR`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "NPY_NOSCALAR")\
).\
\
enum NPY\_ORDER[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER "Link to this definition")\
  \
\
An enumeration type indicating the element order that an array should be interpreted in. When a brand new array is created, generally only **NPY\_CORDER** and **NPY\_FORTRANORDER** are used, whereas when one or more inputs are provided, the order can be based on them.\
\
enumerator NPY\_ANYORDER[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_ANYORDER "Link to this definition")\
  \
\
Fortran order if all the inputs are Fortran, C otherwise.\
\
enumerator NPY\_CORDER[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_CORDER "Link to this definition")\
  \
\
C order.\
\
enumerator NPY\_FORTRANORDER[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_FORTRANORDER "Link to this definition")\
  \
\
Fortran order.\
\
enumerator NPY\_KEEPORDER[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ORDER.NPY_KEEPORDER "Link to this definition")\
  \
\
An order as close to the order of the inputs as possible, even if the input is in neither C nor Fortran order.\
\
enum NPY\_CLIPMODE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE "Link to this definition")\
  \
\
A variable type indicating the kind of clipping that should be applied in certain functions.\
\
enumerator NPY\_RAISE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_RAISE "Link to this definition")\
  \
\
The default for most operations, raises an exception if an index is out of bounds.\
\
enumerator NPY\_CLIP[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_CLIP "Link to this definition")\
  \
\
Clips an index to the valid range if it is out of bounds.\
\
enumerator NPY\_WRAP[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CLIPMODE.NPY_WRAP "Link to this definition")\
  \
\
Wraps an index to the valid range if it is out of bounds.\
\
enum NPY\_SEARCHSIDE[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE "Link to this definition")\
  \
\
A variable type indicating whether the index returned should be that of the first suitable location (if [`NPY_SEARCHLEFT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHLEFT "NPY_SEARCHLEFT")\
) or of the last (if [`NPY_SEARCHRIGHT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHRIGHT "NPY_SEARCHRIGHT")\
).\
\
enumerator NPY\_SEARCHLEFT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHLEFT "Link to this definition")\
  \
\
enumerator NPY\_SEARCHRIGHT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SEARCHSIDE.NPY_SEARCHRIGHT "Link to this definition")\
  \
\
enum NPY\_SELECTKIND[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SELECTKIND "Link to this definition")\
  \
\
A variable type indicating the selection algorithm being used.\
\
enumerator NPY\_INTROSELECT[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SELECTKIND.NPY_INTROSELECT "Link to this definition")\
  \
\
enum NPY\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "Link to this definition")\
  \
\
An enumeration type indicating how permissive data conversions should be. This is used by the iterator added in NumPy 1.6, and is intended to be used more broadly in a future version.\
\
enumerator NPY\_NO\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_NO_CASTING "Link to this definition")\
  \
\
Only allow identical types.\
\
enumerator NPY\_EQUIV\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_EQUIV_CASTING "Link to this definition")\
  \
\
Allow identical and casts involving byte swapping.\
\
enumerator NPY\_SAFE\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_SAFE_CASTING "Link to this definition")\
  \
\
Only allow casts which will not cause values to be rounded, truncated, or otherwise changed.\
\
enumerator NPY\_SAME\_KIND\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_SAME_KIND_CASTING "Link to this definition")\
  \
\
Allow any safe casts, and casts between types of the same kind. For example, float64 -> float32 is permitted with this rule.\
\
enumerator NPY\_UNSAFE\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING.NPY_UNSAFE_CASTING "Link to this definition")\
  \
\
Allow any cast, no matter what kind of data loss may occur.\
\
NPY\_SAME\_VALUE\_CASTING[#](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SAME_VALUE_CASTING "Link to this definition")\
  \
\
Error if any values change during a cast. Currently supported only in `ndarray.astype(... casting='same_value')`\
\
New in version 2.4.\
\
On this page