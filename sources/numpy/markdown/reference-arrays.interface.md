[Skip to main content](https://numpy.org/doc/stable/reference/arrays.interface.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.interface.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.interface.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.interface.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.interface.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.interface.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.interface.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.interface.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.interface.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.interface.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.interface.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.interface.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.interface.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.interface.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.interface.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.interface.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.interface.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.interface.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.interface.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.interface.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.interface.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.interface.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

The array interface protocol[#](https://numpy.org/doc/stable/reference/arrays.interface.html#the-array-interface-protocol "Link to this heading")

==================================================================================================================================================

Note

This page describes the NumPy-specific API for accessing the contents of a NumPy array from other C extensions. [**PEP 3118**](https://peps.python.org/pep-3118/)
 – [`The Revised Buffer Protocol`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "(in Python v3.14)")
 introduces similar, standardized API for any extension module to use. [Cython](https://cython.org/)
’s buffer array support uses the [**PEP 3118**](https://peps.python.org/pep-3118/)
 API; see the [Cython NumPy tutorial](https://github.com/cython/cython/wiki/tutorials-numpy)
.

version:

3

The array interface (sometimes called array protocol) was created in 2005 as a means for array-like Python objects to reuse each other’s data buffers intelligently whenever possible. The homogeneous N-dimensional array interface is a default mechanism for objects to share N-dimensional array memory and information. The interface consists of a Python-side and a C-side using two attributes. Objects wishing to be considered an N-dimensional array in application code should support at least one of these attributes. Objects wishing to support an N-dimensional array in application code should look for at least one of these attributes and use the information provided appropriately.

This interface describes homogeneous arrays in the sense that each item of the array has the same “type”. This type can be very simple or it can be a quite arbitrary and complicated C-like structure.

There are two ways to use the interface: A Python side and a C-side. Both are separate attributes.

Python side[#](https://numpy.org/doc/stable/reference/arrays.interface.html#python-side "Link to this heading")

----------------------------------------------------------------------------------------------------------------

This approach to the interface consists of the object having an [`__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "object.__array_interface__")
 attribute.

object.\_\_array\_interface\_\_[#](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "Link to this definition")

A dictionary of items (3 required and 5 optional). The optional keys in the dictionary have implied defaults if they are not provided.

The keys are:

**shape** (required)

Tuple whose elements are the array size in each dimension. Each entry is an integer (a Python [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
). Note that these integers could be larger than the platform `int` or `long` could hold (a Python [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 is a C `long`). It is up to the code using this attribute to handle this appropriately; either by raising an error when overflow is possible, or by using `long long` as the C type for the shapes.

**typestr** (required)

A string providing the basic type of the homogeneous array The basic string format consists of 3 parts: a character describing the byteorder of the data (`<`: little-endian, `>`: big-endian, `|`: not-relevant), a character code giving the basic type of the array, and an integer providing the number of bytes the type uses.

The basic type character codes are:

|     |     |
| --- | --- |
| `t` | Bit field (following integer gives the number of bits in the bit field). |
| `b` | Boolean (integer type where all values are only `True` or `False`) |
| `i` | Integer |
| `u` | Unsigned integer |
| `f` | Floating point |
| `c` | Complex floating point |
| `m` | Timedelta |
| `M` | Datetime |
| `O` | Object (i.e. the memory contains a pointer to [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")<br>) |
| `S` | String (fixed-length sequence of char) |
| `U` | Unicode (fixed-length sequence of [`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "(in Python v3.14)")<br>) |
| `V` | Other (void \* – each item is a fixed-size chunk of memory) |

**descr** (optional)

A list of tuples providing a more detailed description of the memory layout for each item in the homogeneous array. Each tuple in the list has two or three elements. Normally, this attribute would be used when _typestr_ is `V[0-9]+`, but this is not a requirement. The only requirement is that the number of bytes represented in the _typestr_ key is the same as the total number of bytes represented here. The idea is to support descriptions of C-like structs that make up array elements. The elements of each tuple in the list are

1.  A string providing a name associated with this portion of the datatype. This could also be a tuple of `('full name', 'basic_name')` where basic name would be a valid Python variable name representing the full name of the field.
    
2.  Either a basic-type description string as in _typestr_ or another list (for nested structured types)
    
3.  An optional shape tuple providing how many times this part of the structure should be repeated. No repeats are assumed if this is not given. Very complicated structures can be described using this generic interface. Notice, however, that each element of the array is still of the same data-type. Some examples of using this interface are given below.
    

**Default**: `[('', typestr)]`

**data**

A 2-tuple whose first argument is a [Python integer](https://docs.python.org/3/c-api/long.html "(in Python v3.14)")
 that points to the data-area storing the array contents.

Note

When converting from C/C++ via `PyLong_From*` or high-level bindings such as Cython or pybind11, make sure to use an integer of sufficiently large bitness.

This pointer must point to the first element of data (in other words any offset is always ignored in this case). The second entry in the tuple is a read-only flag (true means the data area is read-only).

This attribute can also be an object exposing the [buffer interface](https://docs.python.org/3/c-api/buffer.html#bufferobjects "(in Python v3.14)")
 which will be used to share the data. If this key is `None`, then memory sharing will be done through the buffer interface of the object itself. In this case, the offset key can be used to indicate the start of the buffer. A reference to the object exposing the array interface must be stored by the new object if the memory area is to be secured.

> Note
> 
> Not specifying this field uses a “scalar” path that we may remove in the future as we are not aware of any users. In this case, NumPy assigns the original object as a scalar into the array.
> 
> Changed in version 2.4: Prior to NumPy 2.4 a `NULL` pointer used the undocumented “scalar” path and was thus usually not accepted (and triggered crashes on some paths). After NumPy 2.4, `NULL` is accepted, although NumPy will create a 1-byte sized new allocation for the array.

**strides** (optional)

Either `None` to indicate a C-style contiguous array or a tuple of strides which provides the number of bytes needed to jump to the next array element in the corresponding dimension. Each entry must be an integer (a Python [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
). As with shape, the values may be larger than can be represented by a C `int` or `long`; the calling code should handle this appropriately, either by raising an error, or by using `long long` in C. The default is `None` which implies a C-style contiguous memory buffer. In this model, the last dimension of the array varies the fastest. For example, the default strides tuple for an object whose array entries are 8 bytes long and whose shape is `(10, 20, 30)` would be `(4800, 240, 8)`.

**Default**: `None` (C-style contiguous)

**mask** (optional)

`None` or an object exposing the array interface. All elements of the mask array should be interpreted only as true or not true indicating which elements of this array are valid. The shape of this object should be _“broadcastable”_ to the shape of the original array.

**Default**: `None` (All array values are valid)

**offset** (optional)

An integer offset into the array data region. This can only be used when data is `None` or returns a [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)")
 object.

**Default**: `0`.

**version** (required)

An integer showing the version of the interface (i.e. 3 for this version). Be careful not to use this to invalidate objects exposing future versions of the interface.

C-struct access[#](https://numpy.org/doc/stable/reference/arrays.interface.html#c-struct-access "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

This approach to the array interface allows for faster access to an array using only one attribute lookup and a well-defined C-structure.

object.\_\_array\_struct\_\_[#](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "Link to this definition")

A [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
 whose `pointer` member contains a pointer to a filled [`PyArrayInterface`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "PyArrayInterface")
 structure. Memory for the structure is dynamically created and the [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
 is also created with an appropriate destructor so the retriever of this attribute simply has to apply [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "(in Python v3.14)")
 to the object returned by this attribute when it is finished. Also, either the data needs to be copied out, or a reference to the object exposing this attribute must be held to ensure the data is not freed. Objects exposing the [`__array_struct__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "object.__array_struct__")
 interface must also not reallocate their memory if other objects are referencing them.

The [`PyArrayInterface`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "PyArrayInterface")
 structure is defined in `numpy/ndarrayobject.h` as:

typedef struct {
  int two;              /\* contains the integer 2 \-- simple sanity check \*/
  int nd;               /\* number of dimensions \*/
  char typekind;        /\* kind in array \--- character code of typestr \*/
  int itemsize;         /\* size of each element \*/
  int flags;            /\* flags indicating how the data should be interpreted \*/
                        /\*   must set ARR\_HAS\_DESCR bit to validate descr \*/
  Py\_ssize\_t \*shape;    /\* A length\-nd array of shape information \*/
  Py\_ssize\_t \*strides;  /\* A length\-nd array of stride information \*/
  void \*data;           /\* A pointer to the first element of the array \*/
  PyObject \*descr;      /\* NULL or data\-description (same as descr key
                                of \_\_array\_interface\_\_) \-- must set ARR\_HAS\_DESCR
                                flag or this will be ignored. \*/
} PyArrayInterface;

Copy to clipboard

The flags member may consist of 5 bits showing how the data should be interpreted and one bit showing how the Interface should be interpreted. The data-bits are [`NPY_ARRAY_C_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS")
 (0x1), [`NPY_ARRAY_F_CONTIGUOUS`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")
 (0x2), [`NPY_ARRAY_ALIGNED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_ALIGNED "NPY_ARRAY_ALIGNED")
 (0x100), [`NPY_ARRAY_NOTSWAPPED`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "NPY_ARRAY_NOTSWAPPED")
 (0x200), and [`NPY_ARRAY_WRITEABLE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_ARRAY_WRITEABLE "NPY_ARRAY_WRITEABLE")
 (0x400). A final flag [`NPY_ARR_HAS_DESCR`](https://numpy.org/doc/stable/reference/arrays.interface.html#c.NPY_ARR_HAS_DESCR "NPY_ARR_HAS_DESCR")
 (0x800) indicates whether or not this structure has the arrdescr field. The field should not be accessed unless this flag is present.

NPY\_ARR\_HAS\_DESCR[#](https://numpy.org/doc/stable/reference/arrays.interface.html#c.NPY_ARR_HAS_DESCR "Link to this definition")
  

New since June 16, 2006:

In the past most implementations used the `desc` member of the `PyCObject` (now [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
) itself (do not confuse this with the “descr” member of the [`PyArrayInterface`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayInterface "PyArrayInterface")
 structure above — they are two separate things) to hold the pointer to the object exposing the interface. This is now an explicit part of the interface. Be sure to take a reference to the object and call [`PyCapsule_SetContext`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetContext "(in Python v3.14)")
 before returning the [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
, and configure a destructor to decref this reference.

Note

[`__array_struct__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_struct__ "object.__array_struct__")
 is considered legacy and should not be used for new code. Use the [buffer protocol](https://docs.python.org/3/c-api/buffer.html "(in Python v3.14)")
 or the DLPack protocol [`numpy.from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")
 instead.

Type description examples[#](https://numpy.org/doc/stable/reference/arrays.interface.html#type-description-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

For clarity it is useful to provide some examples of the type description and corresponding [`__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__ "object.__array_interface__")
 ‘descr’ entries. Thanks to Scott Gilbert for these examples:

In every case, the ‘descr’ key is optional, but of course provides more information which may be important for various applications:

\* Float data
    typestr \== '>f4'
    descr \== \[('','>f4')\]

\* Complex double
    typestr \== '>c8'
    descr \== \[('real','>f4'), ('imag','>f4')\]

\* RGB Pixel data
    typestr \== '|V3'
    descr \== \[('r','|u1'), ('g','|u1'), ('b','|u1')\]

\* Mixed endian (weird but could happen).
    typestr \== '|V8' (or '>u8')
    descr \== \[('big','>i4'), ('little','<i4')\]

\* Nested structure
    struct {
        int ival;
        struct {
            unsigned short sval;
            unsigned char bval;
            unsigned char cval;
        } sub;
    }
    typestr \== '|V8' (or '<u8' if you want)
    descr \== \[('ival','<i4'), ('sub', \[('sval','<u2'), ('bval','|u1'), ('cval','|u1') \]) \]

\* Nested array
    struct {
        int ival;
        double data\[16\*4\];
    }
    typestr \== '|V516'
    descr \== \[('ival','>i4'), ('data','>f8',(16,4))\]

\* Padded structure
    struct {
        int ival;
        double dval;
    }
    typestr \== '|V16'
    descr \== \[('ival','>i4'),('','|V4'),('dval','>f8')\]

Copy to clipboard

It should be clear that any structured type could be described using this interface.

Differences with array interface (version 2)[#](https://numpy.org/doc/stable/reference/arrays.interface.html#differences-with-array-interface-version-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The version 2 interface was very similar. The differences were largely aesthetic. In particular:

1.  The PyArrayInterface structure had no descr member at the end (and therefore no flag ARR\_HAS\_DESCR)
    
2.  The `context` member of the [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
     (formally the `desc` member of the `PyCObject`) returned from `__array_struct__` was not specified. Usually, it was the object exposing the array (so that a reference to it could be kept and destroyed when the C-object was destroyed). It is now an explicit requirement that this field be used in some way to hold a reference to the owning object.
    
    Note
    
    Until August 2020, this said:
    
    > Now it must be a tuple whose first element is a string with “PyArrayInterface Version #” and whose second element is the object exposing the array.
    
    This design was retracted almost immediately after it was proposed, in <[https://mail.python.org/pipermail/numpy-discussion/2006-June/020995.html](https://mail.python.org/pipermail/numpy-discussion/2006-June/020995.html)
    \>. Despite 14 years of documentation to the contrary, at no point was it valid to assume that `__array_interface__` capsules held this tuple content.
    
3.  The tuple returned from `__array_interface__['data']` used to be a hex-string (now it is an integer or a long integer).
    
4.  There was no `__array_interface__` attribute instead all of the keys (except for version) in the `__array_interface__` dictionary were their own attribute: Thus to obtain the Python-side information you had to access separately the attributes:
    
    *   `__array_data__`
        
    *   `__array_shape__`
        
    *   `__array_strides__`
        
    *   `__array_typestr__`
        
    *   `__array_descr__`
        
    *   `__array_offset__`
        
    *   `__array_mask__`
        

On this page