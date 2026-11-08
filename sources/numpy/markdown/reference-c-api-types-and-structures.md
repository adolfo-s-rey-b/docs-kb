[Skip to main content](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/types-and-structures.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/types-and-structures.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/types-and-structures.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/types-and-structures.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/types-and-structures.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/types-and-structures.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/types-and-structures.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/types-and-structures.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/types-and-structures.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/types-and-structures.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/types-and-structures.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/types-and-structures.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/types-and-structures.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/types-and-structures.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/types-and-structures.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/types-and-structures.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/types-and-structures.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/types-and-structures.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/types-and-structures.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/types-and-structures.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Python types and C-structures[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#python-types-and-c-structures "Link to this heading")

==============================================================================================================================================================

Several new types are defined in the C-code. Most of these are accessible from Python, but a few are not exposed due to their limited use. Every new Python type has an associated [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
\* with an internal structure that includes a pointer to a “method table” that defines how the new object behaves in Python. When you receive a Python object into C code, you always get a pointer to a [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 structure. Because a [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 structure is very generic and defines only [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "(in Python v3.14)")
, by itself it is not very interesting. However, different objects contain more details after the [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "(in Python v3.14)")
 (but you have to cast to the correct type to access them — or use accessor functions or macros).

New Python types defined[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#new-python-types-defined "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

Python types are the functional equivalent in C of classes in Python. By constructing a new Python type you make available a new object for Python. The ndarray object is an example of a new type defined in C. New types are defined in C by two basic steps:

1.  creating a C-structure (usually named `Py{Name}Object`) that is binary- compatible with the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
     structure itself but holds the additional information needed for that particular object;
    
2.  populating the [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
     table (pointed to by the ob\_type member of the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
     structure) with pointers to functions that implement the desired behavior for the type.
    

Instead of special method names which define behavior for Python classes, there are “function tables” which point to functions that implement the desired results. The PyTypeObject itself is dynamic which allows C types that can be “sub-typed” from other C-types in C, and sub-classed in Python. The children types inherit the attributes and methods from their parent(s).

There are two major new types: the ndarray ( [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 ) and the ufunc ( [`PyUFunc_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFunc_Type "PyUFunc_Type")
 ). Additional types play a supportive role: the [`PyArrayIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIter_Type "PyArrayIter_Type")
, the [`PyArrayMultiIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIter_Type "PyArrayMultiIter_Type")
, and the [`PyArrayDescr_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDescr_Type "PyArrayDescr_Type")
 . The [`PyArrayIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIter_Type "PyArrayIter_Type")
 is the type for a flat iterator for an ndarray (the object that is returned when getting the flat attribute). The [`PyArrayMultiIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIter_Type "PyArrayMultiIter_Type")
 is the type of the object returned when calling `broadcast`. It handles iteration and broadcasting over a collection of nested sequences. Also, the [`PyArrayDescr_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDescr_Type "PyArrayDescr_Type")
 is the data-type-descriptor type whose instances describe the data and [`PyArray_DTypeMeta`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 is the metaclass for data-type descriptors. There are also new scalar-array types which are new Python scalars corresponding to each of the fundamental data types available for arrays. Additional types are placeholders that allow the array scalars to fit into a hierarchy of actual Python types. Finally, the [`PyArray_DTypeMeta`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 instances corresponding to the NumPy built-in data types are also publicly visible.

### PyArray\_Type and PyArrayObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarray-type-and-pyarrayobject "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArray\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "Link to this definition")
  

The Python type of the ndarray is [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
. In C, every ndarray is a pointer to a [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 structure. The ob\_type member of this structure contains a pointer to the [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 typeobject.

type PyArrayObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "Link to this definition")
  

type NPY\_AO[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO "Link to this definition")
  

The [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 C-structure contains all of the required information for an array. All instances of an ndarray (and its subclasses) will have this structure. For future compatibility, these structure members should normally be accessed using the provided macros. If you need a shorter name, then you can make use of [`NPY_AO`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO "NPY_AO")
 (deprecated) which is defined to be equivalent to [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
. Direct access to the struct fields are deprecated. Use the `PyArray_*(arr)` form instead. As of NumPy 1.20, the size of this struct is not considered part of the NumPy ABI (see note at the end of the member list).

typedef struct PyArrayObject {
    PyObject\_HEAD
    char \*data;
    int nd;
    npy\_intp \*dimensions;
    npy\_intp \*strides;
    PyObject \*base;
    PyArray\_Descr \*descr;
    int flags;
    PyObject \*weakreflist;
    /\* version dependent private members \*/
} PyArrayObject;

Copy to clipboard

[`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "(in Python v3.14)")

This is needed by all Python objects. It consists of (at least) a reference count member ( `ob_refcnt` ) and a pointer to the typeobject ( `ob_type` ). (Other elements may also be present if Python was compiled with special options see Include/object.h in the Python source tree for more information). The ob\_type member points to a Python type object.

char \*data[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.data "Link to this definition")
  

Accessible via [`PyArray_DATA`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DATA "PyArray_DATA")
, this data member is a pointer to the first element of the array. This pointer can (and normally should) be recast to the data type of the array.

int nd[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.nd "Link to this definition")
  

An integer providing the number of dimensions for this array. When nd is 0, the array is sometimes called a rank-0 array. Such arrays have undefined dimensions and strides and cannot be accessed. Macro [`PyArray_NDIM`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NDIM "PyArray_NDIM")
 defined in `ndarraytypes.h` points to this data member. `NPY_MAXDIMS` is defined as a compile time constant limiting the number of dimensions. This number is 64 since NumPy 2 and was 32 before. However, we may wish to remove this limitations in the future so that it is best to explicitly check dimensionality for code that relies on such an upper bound.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*dimensions[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.dimensions "Link to this definition")
  

An array of integers providing the shape in each dimension as long as nd \\(\\geq\\) 1. The integer is always large enough to hold a pointer on the platform, so the dimension size is only limited by memory. [`PyArray_DIMS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DIMS "PyArray_DIMS")
 is the macro associated with this data member.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*strides[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.strides "Link to this definition")
  

An array of integers providing for each dimension the number of bytes that must be skipped to get to the next element in that dimension. Associated with macro [`PyArray_STRIDES`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_STRIDES "PyArray_STRIDES")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*base[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.base "Link to this definition")
  

Pointed to by [`PyArray_BASE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_BASE "PyArray_BASE")
, this member is used to hold a pointer to another Python object that is related to this array. There are two use cases:

*   If this array does not own its own memory, then base points to the Python object that owns it (perhaps another array object)
    
*   If this array has the [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
     flag set, then this array is a working copy of a “misbehaved” array.
    

When `PyArray_ResolveWritebackIfCopy` is called, the array pointed to by base will be updated with the contents of this array.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*descr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.descr "Link to this definition")
  

A pointer to a data-type descriptor object (see below). The data-type descriptor object is an instance of a new built-in type which allows a generic description of memory. There is a descriptor structure for each data type supported. This descriptor structure contains useful information about the type as well as a pointer to a table of function pointers to implement specific functionality. As the name suggests, it is associated with the macro [`PyArray_DESCR`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DESCR "PyArray_DESCR")
.

int flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.flags "Link to this definition")
  

Pointed to by the macro [`PyArray_FLAGS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FLAGS "PyArray_FLAGS")
, this data member represents the flags indicating how the memory pointed to by data is to be interpreted. Possible flags are [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
, [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
, [`NPY_ARRAY_OWNDATA`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_OWNDATA "NPY_ARRAY_OWNDATA")
, [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
, [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
, [`NPY_ARRAY_WRITEBACKIFCOPY`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*weakreflist[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_AO.weakreflist "Link to this definition")
  

This member allows array objects to have weak references (using the weakref module).

Note

Further members are considered private and version dependent. If the size of the struct is important for your code, special care must be taken. A possible use-case when this is relevant is subclassing in C. If your code relies on `sizeof(PyArrayObject)` to be constant, you must add the following check at import time:

if (sizeof(PyArrayObject) < PyArray\_Type.tp\_basicsize) {
    PyErr\_SetString(PyExc\_ImportError,
       "Binary incompatibility with NumPy, must recompile/update X.");
    return NULL;
}

Copy to clipboard

To ensure that your code does not have to be compiled for a specific NumPy version, you may add a constant, leaving room for changes in NumPy. A solution guaranteed to be compatible with any future NumPy version requires the use of a runtime calculate offset and allocation size.

The [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 typeobject implements many of the features of [`Python objects`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 including the [`tp_as_number`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "(in Python v3.14)")
, [`tp_as_sequence`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_sequence "(in Python v3.14)")
, [`tp_as_mapping`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_mapping "(in Python v3.14)")
, and [`tp_as_buffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer "(in Python v3.14)")
 interfaces. The [`rich comparison`](https://docs.python.org/3/c-api/typeobj.html#c.richcmpfunc "(in Python v3.14)")
) is also used along with new-style attribute lookup for member ([`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "(in Python v3.14)")
) and properties ([`tp_getset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getset "(in Python v3.14)")
). The [`PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 can also be sub-typed.

Tip

The [`tp_as_number`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "(in Python v3.14)")
 methods use a generic approach to call whatever function has been registered for handling the operation. When the `_multiarray_umath` module is imported, it sets the numeric operations for all arrays to the corresponding ufuncs. This choice can be changed with [`PyUFunc_ReplaceLoopBySignature`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ReplaceLoopBySignature "PyUFunc_ReplaceLoopBySignature")
.

### PyGenericArrType\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pygenericarrtype-type "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyGenericArrType\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyGenericArrType_Type "Link to this definition")
  

The [`PyGenericArrType_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyGenericArrType_Type "PyGenericArrType_Type")
 is the PyTypeObject definition which create the [`numpy.generic`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.generic "numpy.generic")
 python type.

### PyArrayDescr\_Type and PyArray\_Descr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarraydescr-type-and-pyarray-descr "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArrayDescr\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDescr_Type "Link to this definition")
  

The [`PyArrayDescr_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDescr_Type "PyArrayDescr_Type")
 is the built-in type of the data-type-descriptor objects used to describe how the bytes comprising the array are to be interpreted. There are 21 statically-defined [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 objects for the built-in data-types. While these participate in reference counting, their reference count should never reach zero. There is also a dynamic table of user-defined [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 objects that is also maintained. Once a data-type-descriptor object is “registered” it should never be deallocated either. The function [`PyArray_DescrFromType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_DescrFromType "PyArray_DescrFromType")
 (…) can be used to retrieve a [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 object from an enumerated type-number (either built-in or user- defined).

type PyArray\_DescrProto[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DescrProto "Link to this definition")
  

Identical structure to [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
. This struct is used for static definition of a prototype for registering a new legacy DType by [`PyArray_RegisterDataType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterDataType "PyArray_RegisterDataType")
.

See the note in [`PyArray_RegisterDataType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterDataType "PyArray_RegisterDataType")
 for details.

type PyArray\_Descr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "Link to this definition")
  

The [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 structure lies at the heart of the [`PyArrayDescr_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDescr_Type "PyArrayDescr_Type")
. While it is described here for completeness, it should be considered internal to NumPy and manipulated via `PyArrayDescr_*` or `PyDataType*` functions and macros. The size of this structure is subject to change across versions of NumPy. To ensure compatibility:

*   Never declare a non-pointer instance of the struct
    
*   Never perform pointer arithmetic
    
*   Never use `sizeof(PyArray_Descr)`
    

It has the following structure:

typedef struct {
    PyObject\_HEAD
    PyTypeObject \*typeobj;
    char kind;
    char type;
    char byteorder;
    char \_former\_flags;  // unused field
    int type\_num;
    /\*
     \* Definitions after this one must be accessed through accessor
     \* functions (see below) when compiling with NumPy 1.x support.
     \*/
    npy\_uint64 flags;
    npy\_intp elsize;
    npy\_intp alignment;
    NpyAuxData \*c\_metadata;
    npy\_hash\_t hash;
    void \*reserved\_null\[2\];  // unused field, must be NULLed.
} PyArray\_Descr;

Copy to clipboard

Some dtypes have additional members which are accessible through _PyDataType\_NAMES_, _PyDataType\_FIELDS_, _PyDataType\_SUBARRAY_, and in some cases (times) _PyDataType\_C\_METADATA_.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*typeobj[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.typeobj "Link to this definition")
  

Pointer to a typeobject that is the corresponding Python type for the elements of this array. For the builtin types, this points to the corresponding array scalar. For user-defined types, this should point to a user-defined typeobject. This typeobject can either inherit from array scalars or not. If it does not inherit from array scalars, then the [`NPY_USE_GETITEM`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_GETITEM "NPY_USE_GETITEM")
 and [`NPY_USE_SETITEM`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_SETITEM "NPY_USE_SETITEM")
 flags should be set in the `flags` member.

char kind[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.kind "Link to this definition")
  

A character code indicating the kind of array (using the array interface typestring notation). A ‘b’ represents Boolean, a ‘i’ represents signed integer, a ‘u’ represents unsigned integer, ‘f’ represents floating point, ‘c’ represents complex floating point, ‘S’ represents 8-bit zero-terminated bytes, ‘U’ represents 32-bit/character unicode string, and ‘V’ represents arbitrary.

char type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.type "Link to this definition")
  

A traditional character code indicating the data type.

char byteorder[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.byteorder "Link to this definition")
  

A character indicating the byte-order: ‘>’ (big-endian), ‘<’ (little- endian), ‘=’ (native), ‘|’ (irrelevant, ignore). All builtin data- types have byteorder ‘=’.

[npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.flags "Link to this definition")
  

A data-type bit-flag that determines if the data-type exhibits object- array like behavior. Each bit in this member is a flag which are named as:

*   [`NPY_ITEM_REFCOUNT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_REFCOUNT "NPY_ITEM_REFCOUNT")
    
*   [`NPY_ITEM_HASOBJECT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_HASOBJECT "NPY_ITEM_HASOBJECT")
    
*   [`NPY_LIST_PICKLE`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_LIST_PICKLE "NPY_LIST_PICKLE")
    
*   [`NPY_ITEM_IS_POINTER`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_IS_POINTER "NPY_ITEM_IS_POINTER")
    
*   [`NPY_NEEDS_INIT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_INIT "NPY_NEEDS_INIT")
    
*   [`NPY_NEEDS_PYAPI`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_PYAPI "NPY_NEEDS_PYAPI")
    
*   [`NPY_USE_GETITEM`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_GETITEM "NPY_USE_GETITEM")
    
*   [`NPY_USE_SETITEM`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_SETITEM "NPY_USE_SETITEM")
    
*   [`NPY_FROM_FIELDS`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_FROM_FIELDS "NPY_FROM_FIELDS")
    
*   [`NPY_OBJECT_DTYPE_FLAGS`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_OBJECT_DTYPE_FLAGS "NPY_OBJECT_DTYPE_FLAGS")
    

int type\_num[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.type_num "Link to this definition")
  

A number that uniquely identifies the data type. For new data-types, this number is assigned when the data-type is registered.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 elsize[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.elsize "Link to this definition")
  

For data types that are always the same size (such as long), this holds the size of the data type. For flexible data types where different arrays can have a different elementsize, this should be 0.

See _PyDataType\_ELSIZE_ and _PyDataType\_SET\_ELSIZE_ for a way to access this field in a NumPy 1.x compatible way.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 alignment[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.alignment "Link to this definition")
  

A number providing alignment information for this data type. Specifically, it shows how far from the start of a 2-element structure (whose first element is a `char` ), the compiler places an item of this type: `offsetof(struct {char c; type v;}, v)`

See [`PyDataType_ALIGNMENT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataType_ALIGNMENT "PyDataType_ALIGNMENT")
 for a way to access this field in a NumPy 1.x compatible way.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*metadata[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.metadata "Link to this definition")
  

Metadata about this dtype.

[NpyAuxData](https://numpy.org/doc/stable/reference/c-api/array.html#c.NpyAuxData "NpyAuxData")
 \*c\_metadata[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.c_metadata "Link to this definition")
  

Metadata specific to the C implementation of the particular dtype. Added for NumPy 1.7.0.

type npy\_hash\_t[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.npy_hash_t "Link to this definition")
  

[npy\_hash\_t](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.npy_hash_t "npy_hash_t")
 \*hash[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr.hash "Link to this definition")
  

Used for caching hash values.

NPY\_ITEM\_REFCOUNT[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_REFCOUNT "Link to this definition")
  

Indicates that items of this data-type must be reference counted (using [`Py_INCREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "(in Python v3.14)")
 and [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "(in Python v3.14)")
 ).

NPY\_ITEM\_HASOBJECT[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_HASOBJECT "Link to this definition")
  

Same as [`NPY_ITEM_REFCOUNT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_REFCOUNT "NPY_ITEM_REFCOUNT")
.

NPY\_LIST\_PICKLE[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_LIST_PICKLE "Link to this definition")
  

Indicates arrays of this data-type must be converted to a list before pickling.

NPY\_ITEM\_IS\_POINTER[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_IS_POINTER "Link to this definition")
  

Indicates the item is a pointer to some other data-type

NPY\_NEEDS\_INIT[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_INIT "Link to this definition")
  

Indicates memory for this data-type must be initialized (set to 0) on creation.

NPY\_NEEDS\_PYAPI[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_PYAPI "Link to this definition")
  

Indicates this data-type requires the Python C-API during access (so don’t give up the GIL if array access is going to be needed).

NPY\_USE\_GETITEM[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_GETITEM "Link to this definition")
  

On array access use the `f->getitem` function pointer instead of the standard conversion to an array scalar. Must use if you don’t define an array scalar to go along with the data-type.

NPY\_USE\_SETITEM[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_SETITEM "Link to this definition")
  

When creating a 0-d array from an array scalar use `f->setitem` instead of the standard copy from an array scalar. Must use if you don’t define an array scalar to go along with the data-type.

NPY\_FROM\_FIELDS[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_FROM_FIELDS "Link to this definition")
  

The bits that are inherited for the parent data-type if these bits are set in any field of the data-type. Currently ( [`NPY_NEEDS_INIT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_INIT "NPY_NEEDS_INIT")
 | [`NPY_LIST_PICKLE`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_LIST_PICKLE "NPY_LIST_PICKLE")
 | [`NPY_ITEM_REFCOUNT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_REFCOUNT "NPY_ITEM_REFCOUNT")
 | [`NPY_NEEDS_PYAPI`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_PYAPI "NPY_NEEDS_PYAPI")
 ).

NPY\_OBJECT\_DTYPE\_FLAGS[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_OBJECT_DTYPE_FLAGS "Link to this definition")
  

Bits set for the object data-type: ( [`NPY_LIST_PICKLE`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_LIST_PICKLE "NPY_LIST_PICKLE")
 | [`NPY_USE_GETITEM`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_USE_GETITEM "NPY_USE_GETITEM")
 | [`NPY_ITEM_IS_POINTER`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_IS_POINTER "NPY_ITEM_IS_POINTER")
 | [`NPY_ITEM_REFCOUNT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_REFCOUNT "NPY_ITEM_REFCOUNT")
 | [`NPY_NEEDS_INIT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_INIT "NPY_NEEDS_INIT")
 | [`NPY_NEEDS_PYAPI`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_NEEDS_PYAPI "NPY_NEEDS_PYAPI")
).

int PyDataType\_FLAGCHK([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype, int flags)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyDataType_FLAGCHK "Link to this definition")
  

Return true if all the given flags are set for the data-type object.

int PyDataType\_REFCHK([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyDataType_REFCHK "Link to this definition")
  

Equivalent to [`PyDataType_FLAGCHK`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyDataType_FLAGCHK "PyDataType_FLAGCHK")
 (_dtype_, [`NPY_ITEM_REFCOUNT`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.NPY_ITEM_REFCOUNT "NPY_ITEM_REFCOUNT")
).

### PyArray\_ArrFuncs[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarray-arrfuncs "Link to this heading")

[PyArray\_ArrFuncs](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs "PyArray_ArrFuncs")
 \*PyDataType\_GetArrFuncs([PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*dtype)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyDataType_GetArrFuncs "Link to this definition")
  

Fetch the legacy _PyArray\_ArrFuncs_ of the datatype (cannot fail).

New in version NumPy: 2.0 This function was added in a backwards compatible and backportable way in NumPy 2.0 (see `npy_2_compat.h`). Any code that previously accessed the `->f` slot of the `PyArray_Descr`, must now use this function and backport it to compile with 1.x. (The `npy_2_compat.h` header can be vendored for this purpose.)

type PyArray\_ArrFuncs[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs "Link to this definition")
  

Functions implementing internal features. Not all of these function pointers must be defined for a given type. The required members are `nonzero`, `copyswap`, `copyswapn`, `setitem`, `getitem`, and `cast`. These are assumed to be non- `NULL` and `NULL` entries will cause a program crash. The other functions may be `NULL` which will just mean reduced functionality for that data-type. (Also, the nonzero function will be filled in with a default function if it is `NULL` when you register a user-defined data-type).

typedef struct {
    PyArray\_VectorUnaryFunc \*cast\[NPY\_NTYPES\_LEGACY\];
    PyArray\_GetItemFunc \*getitem;
    PyArray\_SetItemFunc \*setitem;
    PyArray\_CopySwapNFunc \*copyswapn;
    PyArray\_CopySwapFunc \*copyswap;
    PyArray\_CompareFunc \*compare;
    PyArray\_ArgFunc \*argmax;
    PyArray\_DotFunc \*dotfunc;
    PyArray\_ScanFunc \*scanfunc;
    PyArray\_FromStrFunc \*fromstr;
    PyArray\_NonzeroFunc \*nonzero;
    PyArray\_FillFunc \*fill;
    PyArray\_FillWithScalarFunc \*fillwithscalar;
    PyArray\_SortFunc \*sort\[NPY\_NSORTS\];
    PyArray\_ArgSortFunc \*argsort\[NPY\_NSORTS\];
    PyObject \*castdict;
    PyArray\_ScalarKindFunc \*scalarkind;
    int \*\*cancastscalarkindto;
    int \*cancastto;
    void \*\_unused1;
    void \*\_unused2;
    void \*\_unused3;
    PyArray\_ArgFunc \*argmin;
} PyArray\_ArrFuncs;

Copy to clipboard

The concept of a behaved segment is used in the description of the function pointers. A behaved segment is one that is aligned and in native machine byte-order for the data-type. The `nonzero`, `copyswap`, `copyswapn`, `getitem`, and `setitem` functions can (and must) deal with mis-behaved arrays. The other functions require behaved memory segments.

Note

The functions are largely legacy API, however, some are still used. As of NumPy 2.x they are only available via _PyDataType\_GetArrFuncs_ (see the function for more details). Before using any function defined in the struct you should check whether it is `NULL`. In general, the functions `getitem`, `setitem`, `copyswap`, and `copyswapn` can be expected to be defined, but all functions are expected to be replaced with newer API. For example, `PyArray_Pack` is a more powerful version of `setitem` that for example correctly deals with casts.

void cast(void \*from, void \*to, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 n, void \*fromarr, void \*toarr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.cast "Link to this definition")
  

An array of function pointers to cast from the current type to all of the other builtin types. Each function casts a contiguous, aligned, and notswapped buffer pointed at by _from_ to a contiguous, aligned, and notswapped buffer pointed at by _to_ The number of items to cast is given by _n_, and the arguments _fromarr_ and _toarr_ are interpreted as PyArrayObjects for flexible arrays to get itemsize information.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*getitem(void \*data, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.getitem "Link to this definition")
  

A pointer to a function that returns a standard Python object from a single element of the array object _arr_ pointed to by _data_. This function must be able to deal with “misbehaved “(misaligned and/or swapped) arrays correctly.

int setitem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*item, void \*data, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.setitem "Link to this definition")
  

A pointer to a function that sets the Python object _item_ into the array, _arr_, at the position pointed to by _data_ . This function deals with “misbehaved” arrays. If successful, a zero is returned, otherwise, a negative one is returned (and a Python error set).

void copyswapn(void \*dest, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 dstride, void \*src, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 sstride, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 n, int swap, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.copyswapn "Link to this definition")
  

void copyswap(void \*dest, void \*src, int swap, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.copyswap "Link to this definition")
  

These members are both pointers to functions to copy data from _src_ to _dest_ and _swap_ if indicated. The value of arr is only used for flexible ( [`NPY_STRING`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_STRING "NPY_TYPES.NPY_STRING")
, [`NPY_UNICODE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_UNICODE "NPY_TYPES.NPY_UNICODE")
, and [`NPY_VOID`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_VOID "NPY_TYPES.NPY_VOID")
 ) arrays (and is obtained from `arr->descr->elsize` ). The second function copies a single value, while the first loops over n values with the provided strides. These functions can deal with misbehaved _src_ data. If _src_ is NULL then no copy is performed. If _swap_ is 0, then no byteswapping occurs. It is assumed that _dest_ and _src_ do not overlap. If they overlap, then use `memmove` (…) first followed by `copyswap(n)` with NULL valued `src`.

int compare(const void \*d1, const void \*d2, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.compare "Link to this definition")
  

A pointer to a function that compares two elements of the array, `arr`, pointed to by `d1` and `d2`. This function requires behaved (aligned and not swapped) arrays. The return value is 1 if \* `d1` > \* `d2`, 0 if \* `d1` == \* `d2`, and -1 if \* `d1` < \* `d2`. The array object `arr` is used to retrieve itemsize and field information for flexible arrays.

int argmax(void \*data, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 n, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*max\_ind, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.argmax "Link to this definition")
  

A pointer to a function that retrieves the index of the largest of `n` elements in `arr` beginning at the element pointed to by `data`. This function requires that the memory segment be contiguous and behaved. The return value is always 0. The index of the largest element is returned in `max_ind`.

void dotfunc(void \*ip1, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 is1, void \*ip2, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 is2, void \*op, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 n, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.dotfunc "Link to this definition")
  

A pointer to a function that multiplies two `n` -length sequences together, adds them, and places the result in element pointed to by `op` of `arr`. The start of the two sequences are pointed to by `ip1` and `ip2`. To get to the next element in each sequence requires a jump of `is1` and `is2` _bytes_, respectively. This function requires behaved (though not necessarily contiguous) memory.

int scanfunc(FILE \*fd, void \*ip, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.scanfunc "Link to this definition")
  

A pointer to a function that scans (scanf style) one element of the corresponding type from the file descriptor `fd` into the array memory pointed to by `ip`. The array is assumed to be behaved. The last argument `arr` is the array to be scanned into. Returns number of receiving arguments successfully assigned (which may be zero in case a matching failure occurred before the first receiving argument was assigned), or EOF if input failure occurs before the first receiving argument was assigned. This function should be called without holding the Python GIL, and has to grab it for error reporting.

int fromstr(char \*str, void \*ip, char \*\*endptr, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.fromstr "Link to this definition")
  

A pointer to a function that converts the string pointed to by `str` to one element of the corresponding type and places it in the memory location pointed to by `ip`. After the conversion is completed, `*endptr` points to the rest of the string. The last argument `arr` is the array into which ip points (needed for variable-size data- types). Returns 0 on success or -1 on failure. Requires a behaved array. This function should be called without holding the Python GIL, and has to grab it for error reporting.

[npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 nonzero(void \*data, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.nonzero "Link to this definition")
  

A pointer to a function that returns TRUE if the item of `arr` pointed to by `data` is nonzero. This function can deal with misbehaved arrays.

void fill(void \*data, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 length, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.fill "Link to this definition")
  

A pointer to a function that fills a contiguous array of given length with data. The first two elements of the array must already be filled- in. From these two values, a delta will be computed and the values from item 3 to the end will be computed by repeatedly adding this computed delta. The data buffer must be well-behaved.

void fillwithscalar(void \*buffer, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 length, void \*value, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.fillwithscalar "Link to this definition")
  

A pointer to a function that fills a contiguous `buffer` of the given `length` with a single scalar `value` whose address is given. The final argument is the array which is needed to get the itemsize for variable-length arrays.

int sort(void \*start, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 length, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.sort "Link to this definition")
  

An array of function pointers to a particular sorting algorithms. A particular sorting algorithm is obtained using a key (so far [`NPY_QUICKSORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_QUICKSORT "NPY_SORTKIND.NPY_QUICKSORT")
, [`NPY_HEAPSORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_HEAPSORT "NPY_SORTKIND.NPY_HEAPSORT")
, and [`NPY_MERGESORT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SORTKIND.NPY_MERGESORT "NPY_SORTKIND.NPY_MERGESORT")
 are defined). These sorts are done in-place assuming contiguous and aligned data.

int argsort(void \*start, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*result, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 length, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.argsort "Link to this definition")
  

An array of function pointers to sorting algorithms for this data type. The same sorting algorithms as for sort are available. The indices producing the sort are returned in `result` (which must be initialized with indices 0 to `length-1` inclusive).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*castdict[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.castdict "Link to this definition")
  

Either `NULL` or a dictionary containing low-level casting functions for user- defined data-types. Each function is wrapped in a [PyCapsule](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
\* and keyed by the data-type number.

[NPY\_SCALARKIND](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND "NPY_SCALARKIND")
 scalarkind([PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.scalarkind "Link to this definition")
  

A function to determine how scalars of this type should be interpreted. The argument is `NULL` or a 0-dimensional array containing the data (if that is needed to determine the kind of scalar). The return value must be of type [`NPY_SCALARKIND`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND "NPY_SCALARKIND")
.

int \*\*cancastscalarkindto[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.cancastscalarkindto "Link to this definition")
  

Either `NULL` or an array of [`NPY_NSCALARKINDS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NSCALARKINDS "NPY_SCALARKIND.NPY_NSCALARKINDS")
 pointers. These pointers should each be either `NULL` or a pointer to an array of integers (terminated by [`NPY_NOTYPE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_NOTYPE "NPY_NOTYPE")
) indicating data-types that a scalar of this data-type of the specified kind can be cast to safely (this usually means without losing precision).

int \*cancastto[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.cancastto "Link to this definition")
  

Either `NULL` or an array of integers (terminated by [`NPY_NOTYPE`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_NOTYPE "NPY_NOTYPE")
 ) indicated data-types that this data-type can be cast to safely (this usually means without losing precision).

int argmin(void \*data, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 n, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*min\_ind, void \*arr)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_ArrFuncs.argmin "Link to this definition")
  

A pointer to a function that retrieves the index of the smallest of `n` elements in `arr` beginning at the element pointed to by `data`. This function requires that the memory segment be contiguous and behaved. The return value is always 0. The index of the smallest element is returned in `min_ind`.

### PyArrayMethod\_Context and PyArrayMethod\_Spec[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarraymethod-context-and-pyarraymethod-spec "Link to this heading")

type PyArrayMethodObject\_tag[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethodObject_tag "Link to this definition")
  

An opaque struct used to represent the method “self” in ArrayMethod loops.

type PyArrayMethod\_Context[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context "Link to this definition")
  

A struct that is passed in to ArrayMethod loops to provide context for the runtime usage of the loop.

typedef struct {
    PyObject \*caller;
    struct PyArrayMethodObject\_tag \*method;
    PyArray\_Descr \*const \*descriptors;
    void \*parameters;
} PyArrayMethod\_Context

Copy to clipboard

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*caller[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context.caller "Link to this definition")
  

The caller, which is typically the ufunc that called the loop. May be `NULL` when a call is not from a ufunc (e.g. casts).

struct [PyArrayMethodObject\_tag](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethodObject_tag "PyArrayMethodObject_tag")
 \*method[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context.method "Link to this definition")
  

The method “self”. Currently this object is an opaque pointer.

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*\*descriptors[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context.descriptors "Link to this definition")
  

An array of descriptors for the ufunc loop, filled in by `resolve_descriptors`. The length of the array is `nin` + `nout`.

void \*parameters[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Context.parameters "Link to this definition")
  

> A pointer to a structure containing any runtime parameters needed by the loop. This is `NULL` if no parameters are needed. The type of the struct is specific to the registered function.

Changed in version NumPy: 2.4 The _parameters_ member was added in NumPy 2.4.

type PyArrayMethod\_Spec[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec "Link to this definition")
  

A struct used to register an ArrayMethod with NumPy. We use the slots mechanism used by the Python limited API. See below for the slot definitions.

typedef struct {
   const char \*name;
   int nin, nout;
   NPY\_CASTING casting;
   NPY\_ARRAYMETHOD\_FLAGS flags;
   PyArray\_DTypeMeta \*\*dtypes;
   PyType\_Slot \*slots;
} PyArrayMethod\_Spec;

Copy to clipboard

const char \*name[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.name "Link to this definition")
  

The name of the loop.

int nin[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.nin "Link to this definition")
  

The number of input operands

int nout[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.nout "Link to this definition")
  

The number of output operands.

[NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")
 casting[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.casting "Link to this definition")
  

Used to indicate how minimally permissive a casting operation should be. For example, if a cast operation might in some circumstances be safe, but in others unsafe, then `NPY_UNSAFE_CASTING` should be set. Not used for ufunc loops but must still be set.

[NPY\_ARRAYMETHOD\_FLAGS](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAYMETHOD_FLAGS "NPY_ARRAYMETHOD_FLAGS")
 flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.flags "Link to this definition")
  

The flags set for the method.

[PyArray\_DTypeMeta](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
 \*\*dtypes[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.dtypes "Link to this definition")
  

The DTypes for the loop. Must be `nin` + `nout` in length.

[PyType\_Slot](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "(in Python v3.14)")
 \*slots[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec.slots "Link to this definition")
  

An array of slots for the method. Slot IDs must be one of the values below.

### PyArray\_DTypeMeta and PyArrayDTypeMeta\_Spec[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarray-dtypemeta-and-pyarraydtypemeta-spec "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArrayDTypeMeta\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Type "Link to this definition")
  

The python type object corresponding to [`PyArray_DTypeMeta`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "PyArray_DTypeMeta")
.

type PyArray\_DTypeMeta[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta "Link to this definition")
  

A largely opaque struct representing DType classes. Each instance defines a metaclass for a single NumPy data type. Data types can either be non-parametric or parametric. For non-parametric types, the DType class has a one-to-one correspondence with the descriptor instance created from the DType class. Parametric types can correspond to many different dtype instances depending on the chosen parameters. This type is available in the public `numpy/dtype_api.h` header. Currently use of this struct is not supported in the limited CPython API, so if `Py_LIMITED_API` is set, this type is a typedef for `PyTypeObject`.

typedef struct {
     PyHeapTypeObject super;
     PyArray\_Descr \*singleton;
     int type\_num;
     PyTypeObject \*scalar\_type;
     npy\_uint64 flags;
     void \*dt\_slots;
     void \*reserved\[3\];
} PyArray\_DTypeMeta

Copy to clipboard

PyHeapTypeObject super[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta.super "Link to this definition")
  

The superclass, providing hooks into the python object API. Set members of this struct to fill in the functions implementing the `PyTypeObject` API (e.g. `tp_new`).

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*singleton[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta.singleton "Link to this definition")
  

A descriptor instance suitable for use as a singleton descriptor for the data type. This is useful for non-parametric types representing simple plain old data type where there is only one logical descriptor instance for all data of the type. Can be NULL if a singleton instance is not appropriate.

int type\_num[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta.type_num "Link to this definition")
  

Corresponds to the type number for legacy data types. Data types defined outside of NumPy and possibly future data types shipped with NumPy will have `type_num` set to -1, so this should not be relied on to discriminate between data types.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*scalar\_type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta.scalar_type "Link to this definition")
  

The type of scalar instances for this data type.

[npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta.flags "Link to this definition")
  

Flags can be set to indicate to NumPy that this data type has optional behavior. See [Flags](https://numpy.org/doc/stable/reference/c-api/array.html#dtype-flags)
 for a listing of allowed flag values.

void \*dt\_slots[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_DTypeMeta.dt_slots "Link to this definition")
  

An opaque pointer to a private struct containing implementations of functions in the DType API. This is filled in from the `slots` member of the `PyArrayDTypeMeta_Spec` instance used to initialize the DType.

type PyArrayDTypeMeta\_Spec[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Spec "Link to this definition")
  

A struct used to initialize a new DType with the `PyArrayInitDTypeMeta_FromSpec` function.

typedef struct {
    PyTypeObject \*typeobj;
    int flags;
    PyArrayMethod\_Spec \*\*casts;
    PyType\_Slot \*slots;
    PyTypeObject \*baseclass;
}

Copy to clipboard

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 \*typeobj[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Spec.typeobj "Link to this definition")
  

Either `NULL` or the type of the python scalar associated with the DType. Scalar indexing into an array returns an item with this type.

int flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Spec.flags "Link to this definition")
  

Static flags for the DType class, indicating whether the DType is parametric, abstract, or represents numeric data. The latter is optional but is useful to set to indicate to downstream code if the DType represents data that are numbers (ints, floats, or other numeric data type) or something else (e.g. a string, unit, or date).

[PyArrayMethod\_Spec](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMethod_Spec "PyArrayMethod_Spec")
 \*\*casts;[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Spec.casts "Link to this definition")
  

A `NULL`\-terminated array of ArrayMethod specifications for casts defined by the DType.

[PyType\_Slot](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "(in Python v3.14)")
 \*slots;[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayDTypeMeta_Spec.slots "Link to this definition")
  

A `NULL`\-terminated array of slot specifications for implementations of functions in the DType API. Slot IDs must be one of the DType slot IDs enumerated in [Slot IDs and API Function Typedefs](https://numpy.org/doc/stable/reference/c-api/array.html#dtype-slots)
.

### Exposed DTypes classes (`PyArray_DTypeMeta` objects)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#exposed-dtypes-classes-pyarray-dtypemeta-objects "Link to this heading")

For use with promoters, NumPy exposes a number of Dtypes following the pattern `PyArray_<Name>DType` corresponding to those found in _np.dtypes_.

Additionally, the three DTypes, `PyArray_PyLongDType`, `PyArray_PyFloatDType`, `PyArray_PyComplexDType` correspond to the Python scalar values. These cannot be used in all places, but do allow for example the common dtype operation and implementing promotion with them may be necessary.

Further, the following abstract DTypes are defined which cover both the builtin NumPy ones and the python ones, and users can in principle subclass from them (this does not inherit any DType specific functionality): \* `PyArray_IntAbstractDType` \* `PyArray_FloatAbstractDType` \* `PyArray_ComplexAbstractDType`

Warning

As of NumPy 2.0, the _only_ valid use for these DTypes is registering a promoter conveniently to e.g. match “any integers” (and subclass checks). Because of this, they are not exposed to Python.

### PyUFunc\_Type and PyUFuncObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyufunc-type-and-pyufuncobject "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyUFunc\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFunc_Type "Link to this definition")
  

The ufunc object is implemented by creation of the [`PyUFunc_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFunc_Type "PyUFunc_Type")
. It is a very simple type that implements only basic getattribute behavior, printing behavior, and has call behavior which allows these objects to act like functions. The basic idea behind the ufunc is to hold a reference to fast 1-dimensional (vector) loops for each data type that supports the operation. These one-dimensional loops all have the same signature and are the key to creating a new ufunc. They are called by the generic looping code as appropriate to implement the N-dimensional function. There are also some generic 1-d loops defined for floating and complexfloating arrays that allow you to define a ufunc using a single scalar function (_e.g._ atanh).

type PyUFuncObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject "Link to this definition")
  

The core of the ufunc is the [`PyUFuncObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject "PyUFuncObject")
 which contains all the information needed to call the underlying C-code loops that perform the actual work. While it is described here for completeness, it should be considered internal to NumPy and manipulated via `PyUFunc_*` functions. The size of this structure is subject to change across versions of NumPy. To ensure compatibility:

*   Never declare a non-pointer instance of the struct
    
*   Never perform pointer arithmetic
    
*   Never use `sizeof(PyUFuncObject)`
    

It has the following structure:

typedef struct {
    PyObject\_HEAD
    int nin;
    int nout;
    int nargs;
    int identity;
    PyUFuncGenericFunction \*functions;
    void \*\*data;
    int ntypes;
    int \_ufunc\_flags;
    const char \*name;
    char \*types;
    const char \*doc;
    void \*ptr;
    PyObject \*obj;
    PyObject \*userloops;
    int core\_enabled;
    int core\_num\_dim\_ix;
    int \*core\_num\_dims;
    int \*core\_dim\_ixs;
    int \*core\_offsets;
    char \*core\_signature;
    PyUFunc\_TypeResolutionFunc \*type\_resolver;
    void \*reserved2;
    void \*reserved3;
    npy\_uint32 \*op\_flags;
    npy\_uint32 \*iter\_flags;
    /\* new in API version 0x0000000D \*/
    npy\_intp \*core\_dim\_sizes;
    npy\_uint32 \*core\_dim\_flags;
    PyObject \*identity\_value;
    /\* Further private slots (size depends on the NumPy version) \*/
} PyUFuncObject;

Copy to clipboard

int nin[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.nin "Link to this definition")
  

The number of input arguments.

int nout[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.nout "Link to this definition")
  

The number of output arguments.

int nargs[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.nargs "Link to this definition")
  

The total number of arguments (_nin_ + _nout_). This must be less than [`NPY_MAXARGS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_MAXARGS "NPY_MAXARGS")
.

int identity[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.identity "Link to this definition")
  

Either [`PyUFunc_One`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_One "PyUFunc_One")
, [`PyUFunc_Zero`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_Zero "PyUFunc_Zero")
, [`PyUFunc_MinusOne`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_MinusOne "PyUFunc_MinusOne")
, [`PyUFunc_None`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_None "PyUFunc_None")
, [`PyUFunc_ReorderableNone`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ReorderableNone "PyUFunc_ReorderableNone")
, or [`PyUFunc_IdentityValue`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_IdentityValue "PyUFunc_IdentityValue")
 to indicate the identity for this operation. It is only used for a reduce-like call on an empty array.

void functions(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*dims, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*steps, void \*extradata)[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.functions "Link to this definition")
  

An array of function pointers — one for each data type supported by the ufunc. This is the vector loop that is called to implement the underlying function _dims_ \[0\] times. The first argument, _args_, is an array of _nargs_ pointers to behaved memory. Pointers to the data for the input arguments are first, followed by the pointers to the data for the output arguments. How many bytes must be skipped to get to the next element in the sequence is specified by the corresponding entry in the _steps_ array. The last argument allows the loop to receive extra information. This is commonly used so that a single, generic vector loop can be used for multiple functions. In this case, the actual scalar function to call is passed in as _extradata_. The size of this function pointer array is ntypes.

void \*\*data[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.data "Link to this definition")
  

Extra data to be passed to the 1-d vector loops or `NULL` if no extra-data is needed. This C-array must be the same size ( _i.e._ ntypes) as the functions array. `NULL` is used if extra\_data is not needed. Several C-API calls for UFuncs are just 1-d vector loops that make use of this extra data to receive a pointer to the actual function to call.

int ntypes[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.ntypes "Link to this definition")
  

The number of supported data types for the ufunc. This number specifies how many different 1-d loops (of the builtin data types) are available.

char \*name[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.name "Link to this definition")
  

A string name for the ufunc. This is used dynamically to build the \_\_doc\_\_ attribute of ufuncs.

char \*types[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.types "Link to this definition")
  

An array of \\(nargs \\times ntypes\\) 8-bit type\_numbers which contains the type signature for the function for each of the supported (builtin) data types. For each of the _ntypes_ functions, the corresponding set of type numbers in this array shows how the _args_ argument should be interpreted in the 1-d vector loop. These type numbers do not have to be the same type and mixed-type ufuncs are supported.

char \*doc[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.doc "Link to this definition")
  

Documentation for the ufunc. Should not contain the function signature as this is generated dynamically when \_\_doc\_\_ is retrieved.

void \*ptr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.ptr "Link to this definition")
  

Any dynamically allocated memory. Currently, this is used for dynamic ufuncs created from a python function to store room for the types, data, and name members.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.obj "Link to this definition")
  

For ufuncs dynamically created from python functions, this member holds a reference to the underlying Python function.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*userloops[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.userloops "Link to this definition")
  

A dictionary of user-defined 1-d vector loops (stored as CObject ptrs) for user-defined types. A loop may be registered by the user for any user-defined type. It is retrieved by type number. User defined type numbers are always larger than [`NPY_USERDEF`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_USERDEF "NPY_USERDEF")
.

int core\_enabled[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_enabled "Link to this definition")
  

0 for scalar ufuncs; 1 for generalized ufuncs

int core\_num\_dim\_ix[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_num_dim_ix "Link to this definition")
  

Number of distinct core dimension names in the signature

int \*core\_num\_dims[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_num_dims "Link to this definition")
  

Number of core dimensions of each argument

int \*core\_dim\_ixs[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_dim_ixs "Link to this definition")
  

Dimension indices in a flattened form; indices of argument `k` are stored in `core_dim_ixs[core_offsets[k] : core_offsets[k] + core_numdims[k]]`

int \*core\_offsets[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_offsets "Link to this definition")
  

Position of 1st core dimension of each argument in `core_dim_ixs`, equivalent to cumsum(`core_num_dims`)

char \*core\_signature[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_signature "Link to this definition")
  

Core signature string

[PyUFunc\_TypeResolutionFunc](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.type_resolver.PyUFunc_TypeResolutionFunc "PyUFunc_TypeResolutionFunc")
 \*type\_resolver[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.type_resolver "Link to this definition")
  

A function which resolves the types and fills an array with the dtypes for the inputs and outputs

type PyUFunc\_TypeResolutionFunc[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.type_resolver.PyUFunc_TypeResolutionFunc "Link to this definition")
  

The function pointer type for [`type_resolver`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.type_resolver "type_resolver")

[npy\_uint32](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint32 "npy_uint32")
 op\_flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.op_flags "Link to this definition")
  

Override the default operand flags for each ufunc operand.

[npy\_uint32](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint32 "npy_uint32")
 iter\_flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.iter_flags "Link to this definition")
  

Override the default nditer flags for the ufunc.

Added in API version 0x0000000D

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*core\_dim\_sizes[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_dim_sizes "Link to this definition")
  

For each distinct core dimension, the possible [frozen](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#frozen)
 size if [`UFUNC_CORE_DIM_SIZE_INFERRED`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.UFUNC_CORE_DIM_SIZE_INFERRED "UFUNC_CORE_DIM_SIZE_INFERRED")
 is `0`

[npy\_uint32](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint32 "npy_uint32")
 \*core\_dim\_flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.core_dim_flags "Link to this definition")
  

For each distinct core dimension, a set of flags ( [`UFUNC_CORE_DIM_CAN_IGNORE`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.UFUNC_CORE_DIM_CAN_IGNORE "UFUNC_CORE_DIM_CAN_IGNORE")
 and [`UFUNC_CORE_DIM_SIZE_INFERRED`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.UFUNC_CORE_DIM_SIZE_INFERRED "UFUNC_CORE_DIM_SIZE_INFERRED")
)

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*identity\_value[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.identity_value "Link to this definition")
  

Identity for reduction, when [`PyUFuncObject.identity`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject.identity "PyUFuncObject.identity")
 is equal to [`PyUFunc_IdentityValue`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_IdentityValue "PyUFunc_IdentityValue")
.

UFUNC\_CORE\_DIM\_CAN\_IGNORE[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.UFUNC_CORE_DIM_CAN_IGNORE "Link to this definition")
  

if the dim name ends in `?`

UFUNC\_CORE\_DIM\_SIZE\_INFERRED[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.UFUNC_CORE_DIM_SIZE_INFERRED "Link to this definition")
  

if the dim size will be determined from the operands and not from a [frozen](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#frozen)
 signature

### PyArrayIter\_Type and PyArrayIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarrayiter-type-and-pyarrayiterobject "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArrayIter\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIter_Type "Link to this definition")
  

This is an iterator object that makes it easy to loop over an N-dimensional array. It is the object returned from the flat attribute of an ndarray. It is also used extensively throughout the implementation internals to loop over an N-dimensional array. The tp\_as\_mapping interface is implemented so that the iterator object can be indexed (using 1-d indexing), and a few methods are implemented through the tp\_methods table. This object implements the next method and can be used anywhere an iterator can be used in Python.

type PyArrayIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "Link to this definition")
  

The C-structure corresponding to an object of [`PyArrayIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIter_Type "PyArrayIter_Type")
 is the [`PyArrayIterObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "PyArrayIterObject")
. The [`PyArrayIterObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "PyArrayIterObject")
 is used to keep track of a pointer into an N-dimensional array. It contains associated information used to quickly march through the array. The pointer can be adjusted in three basic ways: 1) advance to the “next” position in the array in a C-style contiguous fashion, 2) advance to an arbitrary N-dimensional coordinate in the array, and 3) advance to an arbitrary one-dimensional index into the array. The members of the [`PyArrayIterObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "PyArrayIterObject")
 structure are used in these calculations. Iterator objects keep their own dimension and strides information about an array. This can be adjusted as needed for “broadcasting,” or to loop over only specific dimensions.

typedef struct {
    PyObject\_HEAD
    int   nd\_m1;
    npy\_intp  index;
    npy\_intp  size;
    npy\_intp  coordinates\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp  dims\_m1\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp  strides\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp  backstrides\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp  factors\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    PyArrayObject \*ao;
    char  \*dataptr;
    npy\_bool  contiguous;
} PyArrayIterObject;

Copy to clipboard

int nd\_m1[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.nd_m1 "Link to this definition")
  

\\(N-1\\) where \\(N\\) is the number of dimensions in the underlying array.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 index[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.index "Link to this definition")
  

The current 1-d index into the array.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 size[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.size "Link to this definition")
  

The total size of the underlying array.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*coordinates[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.coordinates "Link to this definition")
  

An \\(N\\) -dimensional index into the array.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*dims\_m1[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.dims_m1 "Link to this definition")
  

The size of the array minus 1 in each dimension.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*strides[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.strides "Link to this definition")
  

The strides of the array. How many bytes needed to jump to the next element in each dimension.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*backstrides[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.backstrides "Link to this definition")
  

How many bytes needed to jump from the end of a dimension back to its beginning. Note that `backstrides[k] == strides[k] * dims_m1[k]`, but it is stored here as an optimization.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*factors[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.factors "Link to this definition")
  

This array is used in computing an N-d index from a 1-d index. It contains needed products of the dimensions.

[PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 \*ao[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.ao "Link to this definition")
  

A pointer to the underlying ndarray this iterator was created to represent.

char \*dataptr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.dataptr "Link to this definition")
  

This member points to an element in the ndarray indicated by the index.

[npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 contiguous[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject.contiguous "Link to this definition")
  

This flag is true if the underlying array is [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
. It is used to simplify calculations when possible.

How to use an array iterator on a C-level is explained more fully in later sections. Typically, you do not need to concern yourself with the internal structure of the iterator object, and merely interact with it through the use of the macros [`PyArray_ITER_NEXT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_NEXT "PyArray_ITER_NEXT")
 (it), [`PyArray_ITER_GOTO`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO "PyArray_ITER_GOTO")
 (it, dest), or [`PyArray_ITER_GOTO1D`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO1D "PyArray_ITER_GOTO1D")
 (it, index). All of these macros require the argument _it_ to be a [PyArrayIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "PyArrayIterObject")
\*.

### PyArrayMultiIter\_Type and PyArrayMultiIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarraymultiiter-type-and-pyarraymultiiterobject "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArrayMultiIter\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIter_Type "Link to this definition")
  

This type provides an iterator that encapsulates the concept of broadcasting. It allows \\(N\\) arrays to be broadcast together so that the loop progresses in C-style contiguous fashion over the broadcasted array. The corresponding C-structure is the [`PyArrayMultiIterObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")
 whose memory layout must begin any object, _obj_, passed in to the [`PyArray_Broadcast`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Broadcast "PyArray_Broadcast")
 (obj) function. Broadcasting is performed by adjusting array iterators so that each iterator represents the broadcasted shape and size, but has its strides adjusted so that the correct element from the array is used at each iteration.

type PyArrayMultiIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "Link to this definition")
  

typedef struct {
    PyObject\_HEAD
    int numiter;
    npy\_intp size;
    npy\_intp index;
    int nd;
    npy\_intp dimensions\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    PyArrayIterObject \*iters\[\];
} PyArrayMultiIterObject;

Copy to clipboard

int numiter[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject.numiter "Link to this definition")
  

The number of arrays that need to be broadcast to the same shape.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 size[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject.size "Link to this definition")
  

The total broadcasted size.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 index[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject.index "Link to this definition")
  

The current (1-d) index into the broadcasted result.

int nd[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject.nd "Link to this definition")
  

The number of dimensions in the broadcasted result.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*dimensions[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject.dimensions "Link to this definition")
  

The shape of the broadcasted result (only `nd` slots are used).

[PyArrayIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayIterObject "PyArrayIterObject")
 \*\*iters[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject.iters "Link to this definition")
  

An array of iterator objects that holds the iterators for the arrays to be broadcast together. On return, the iterators are adjusted for broadcasting.

### PyArrayNeighborhoodIter\_Type and PyArrayNeighborhoodIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarrayneighborhooditer-type-and-pyarrayneighborhooditerobject "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArrayNeighborhoodIter\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayNeighborhoodIter_Type "Link to this definition")
  

This is an iterator object that makes it easy to loop over an N-dimensional neighborhood.

type PyArrayNeighborhoodIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayNeighborhoodIterObject "Link to this definition")
  

The C-structure corresponding to an object of [`PyArrayNeighborhoodIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayNeighborhoodIter_Type "PyArrayNeighborhoodIter_Type")
 is the [`PyArrayNeighborhoodIterObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayNeighborhoodIterObject "PyArrayNeighborhoodIterObject")
.

typedef struct {
    PyObject\_HEAD
    int nd\_m1;
    npy\_intp index, size;
    npy\_intp coordinates\[NPY\_MAXDIMS\_LEGACY\_ITERS\]
    npy\_intp dims\_m1\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp strides\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp backstrides\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_intp factors\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    PyArrayObject \*ao;
    char \*dataptr;
    npy\_bool contiguous;
    npy\_intp bounds\[NPY\_MAXDIMS\_LEGACY\_ITERS\]\[2\];
    npy\_intp limits\[NPY\_MAXDIMS\_LEGACY\_ITERS\]\[2\];
    npy\_intp limits\_sizes\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    npy\_iter\_get\_dataptr\_t translate;
    npy\_intp nd;
    npy\_intp dimensions\[NPY\_MAXDIMS\_LEGACY\_ITERS\];
    PyArrayIterObject\* \_internal\_iter;
    char\* constant;
    int mode;
} PyArrayNeighborhoodIterObject;

Copy to clipboard

### ScalarArrayTypes[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#scalararraytypes "Link to this heading")

There is a Python type for each of the different built-in data types that can be present in the array. Most of these are simple wrappers around the corresponding data type in C. The C-names for these types are `Py{TYPE}ArrType_Type` where `{TYPE}` can be

> **Bool**, **Byte**, **Short**, **Int**, **Long**, **LongLong**, **UByte**, **UShort**, **UInt**, **ULong**, **ULongLong**, **Half**, **Float**, **Double**, **LongDouble**, **CFloat**, **CDouble**, **CLongDouble**, **String**, **Unicode**, **Void**, **Datetime**, **Timedelta**, and **Object**.

These type names are part of the C-API and can therefore be created in extension C-code. There is also a `PyIntpArrType_Type` and a `PyUIntpArrType_Type` that are simple substitutes for one of the integer types that can hold a pointer on the platform. The structure of these scalar objects is not exposed to C-code. The function [`PyArray_ScalarAsCtype`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ScalarAsCtype "PyArray_ScalarAsCtype")
 (..) can be used to extract the C-type value from the array scalar and the function [`PyArray_Scalar`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_Scalar "PyArray_Scalar")
 (…) can be used to construct an array scalar from a C-value.

Other C-structures[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#other-c-structures "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

A few new C-structures were found to be useful in the development of NumPy. These C-structures are used in at least one C-API call and are therefore documented here. The main reason these structures were defined is to make it easy to use the Python ParseTuple C-API to convert from Python objects to a useful C-Object.

### PyArray\_Dims[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarray-dims "Link to this heading")

type PyArray\_Dims[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims "Link to this definition")
  

This structure is very useful when shape and/or strides information is supposed to be interpreted. The structure is:

typedef struct {
    npy\_intp \*ptr;
    int len;
} PyArray\_Dims;

Copy to clipboard

The members of this structure are

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*ptr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims.ptr "Link to this definition")
  

A pointer to a list of ([`npy_intp`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
) integers which usually represent array shape or array strides.

int len[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Dims.len "Link to this definition")
  

The length of the list of integers. It is assumed safe to access _ptr_ \[0\] to _ptr_ \[len-1\].

### PyArray\_Chunk[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarray-chunk "Link to this heading")

type PyArray\_Chunk[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk "Link to this definition")
  

This is equivalent to the buffer object structure in Python up to the ptr member. On 32-bit platforms (_i.e._ if [`NPY_SIZEOF_INT`](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_INT "NPY_SIZEOF_INT")
 == [`NPY_SIZEOF_INTP`](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_INTP "NPY_SIZEOF_INTP")
), the len member also matches an equivalent member of the buffer object. It is useful to represent a generic single-segment chunk of memory.

typedef struct {
    PyObject\_HEAD
    PyObject \*base;
    void \*ptr;
    npy\_intp len;
    int flags;
} PyArray\_Chunk;

Copy to clipboard

The members are

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*base[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk.base "Link to this definition")
  

The Python object this chunk of memory comes from. Needed so that memory can be accounted for properly.

void \*ptr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk.ptr "Link to this definition")
  

A pointer to the start of the single-segment chunk of memory.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 len[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk.len "Link to this definition")
  

The length of the segment in bytes.

int flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Chunk.flags "Link to this definition")
  

Any data flags (_e.g._ [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 ) that should be used to interpret the memory.

### PyArrayInterface[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#pyarrayinterface "Link to this heading")

See also

[The array interface protocol](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)

type PyArrayInterface[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "Link to this definition")
  

The [`PyArrayInterface`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "PyArrayInterface")
 structure is defined so that NumPy and other extension modules can use the rapid array interface protocol. The [`__array_struct__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "object.__array_struct__")
 method of an object that supports the rapid array interface protocol should return a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
 that contains a pointer to a [`PyArrayInterface`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "PyArrayInterface")
 structure with the relevant details of the array. After the new array is created, the attribute should be `DECREF`’d which will free the [`PyArrayInterface`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "PyArrayInterface")
 structure. Remember to `INCREF` the object (whose [`__array_struct__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "object.__array_struct__")
 attribute was retrieved) and point the base member of the new [`PyArrayObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
 to this same object. In this way the memory for the array will be managed correctly.

typedef struct {
    int two;
    int nd;
    char typekind;
    int itemsize;
    int flags;
    npy\_intp \*shape;
    npy\_intp \*strides;
    void \*data;
    PyObject \*descr;
} PyArrayInterface;

Copy to clipboard

int two[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.two "Link to this definition")
  

the integer 2 as a sanity check.

int nd[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.nd "Link to this definition")
  

the number of dimensions in the array.

char typekind[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.typekind "Link to this definition")
  

A character indicating what kind of array is present according to the typestring convention with ‘t’ -> bitfield, ‘b’ -> Boolean, ‘i’ -> signed integer, ‘u’ -> unsigned integer, ‘f’ -> floating point, ‘c’ -> complex floating point, ‘O’ -> object, ‘S’ -> (byte-)string, ‘U’ -> unicode, ‘V’ -> void.

int itemsize[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.itemsize "Link to this definition")
  

The number of bytes each item in the array requires.

int flags[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.flags "Link to this definition")
  

Any of the bits [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 (1), [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 (2), [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
 (0x100), [`NPY_ARRAY_NOTSWAPPED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "NPY_ARRAY_NOTSWAPPED")
 (0x200), or [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 (0x400) to indicate something about the data. The [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
, [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
, and [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 flags can actually be determined from the other parameters. The flag [`NPY_ARR_HAS_DESCR`](https://numpy.org/doc/stable/reference/arrays.interface.html#c.NPY_ARR_HAS_DESCR "NPY_ARR_HAS_DESCR")
 (0x800) can also be set to indicate to objects consuming the version 3 array interface that the descr member of the structure is present (it will be ignored by objects consuming version 2 of the array interface).

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*shape[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.shape "Link to this definition")
  

An array containing the size of the array in each dimension.

[npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 \*strides[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.strides "Link to this definition")
  

An array containing the number of bytes to jump to get to the next element in each dimension.

void \*data[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.data "Link to this definition")
  

A pointer _to_ the first element of the array.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*descr[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface.descr "Link to this definition")
  

A Python object describing the data-type in more detail (same as the _descr_ key in [`__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "object.__array_interface__")
). This can be `NULL` if _typekind_ and _itemsize_ provide enough information. This field is also ignored unless [`NPY_ARR_HAS_DESCR`](https://numpy.org/doc/stable/reference/arrays.interface.html#c.NPY_ARR_HAS_DESCR "NPY_ARR_HAS_DESCR")
 flag is on in _flags_.

### Internally used structures[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#internally-used-structures "Link to this heading")

Internally, the code uses some additional Python objects primarily for memory management. These types are not accessible directly from Python, and are not exposed to the C-API. They are included here only for completeness and assistance in understanding the code.

type PyUFunc\_Loop1d[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFunc_Loop1d "Link to this definition")
  

A simple linked-list of C-structures containing the information needed to define a 1-d loop for a ufunc for every defined signature of a user-defined data-type.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "(in Python v3.14)")
 PyArrayMapIter\_Type[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMapIter_Type "Link to this definition")
  

Advanced indexing is handled with this Python type. It is simply a loose wrapper around the C-structure containing the variables needed for advanced array indexing.

type PyArrayMapIterObject[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMapIterObject "Link to this definition")
  

The C-structure associated with [`PyArrayMapIter_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMapIter_Type "PyArrayMapIter_Type")
. This structure is useful if you are trying to understand the advanced-index mapping code. It is defined in the `multiarray/mapping.h` header. This type is not exposed to Python and could be replaced with a C-structure. As a Python type it takes advantage of reference- counted memory management.

NumPy C-API and C complex[#](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#numpy-c-api-and-c-complex "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

When you use the NumPy C-API, you will have access to complex real declarations `npy_cdouble` and `npy_cfloat`, which are declared in terms of the C standard types from `complex.h`. Unfortunately, `complex.h` contains `#define I ...` (where the actual definition depends on the compiler), which means that any downstream user that does `#include <numpy/arrayobject.h>` could get `I` defined, and using something like declaring `double I;` in their code will result in an obscure compiler error like

This error can be avoided by adding:

#undef I

Copy to clipboard

to your code.

Changed in version 2.0: The inclusion of `complex.h` was new in NumPy 2, so that code defining a different `I` may not have required the `#undef I` on older versions. NumPy 2.0.1 briefly included the `#under I`

On this page