[Skip to main content](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.ctypeslib.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.ctypeslib.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.ctypeslib.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.ctypeslib.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.ctypeslib.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.ctypeslib.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.ctypeslib.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.ctypeslib.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.ctypeslib.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.ctypeslib.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.ctypeslib.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.ctypeslib.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.ctypeslib.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.ctypeslib.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.ctypeslib.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.ctypeslib.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.ctypeslib.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.ctypeslib.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.ctypeslib.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.ctypeslib.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.ctypeslib.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

ctypes foreign function interface ([`numpy.ctypeslib`](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#module-numpy.ctypeslib "numpy.ctypeslib")
)[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#ctypes-foreign-function-interface-numpy-ctypeslib "Link to this heading")

==============================================================================================================================================================================================================================================================================================================

numpy.ctypeslib.as\_array(_obj_, _shape\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ctypeslib/_ctypeslib.py#L520-L559)
[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.as_array "Link to this definition")

Create a numpy array from a ctypes array or POINTER.

The numpy array shares the memory with the ctypes object.

The shape parameter must be given if converting from a ctypes POINTER. The shape parameter is ignored if converting from a ctypes array

Examples

Try it in your browser!

Converting a ctypes integer array:

\>>> import ctypes
\>>> ctypes\_array \= (ctypes.c\_int \* 5)(0, 1, 2, 3, 4)
\>>> np\_array \= np.ctypeslib.as\_array(ctypes\_array)
\>>> np\_array
array(\[0, 1, 2, 3, 4\], dtype=int32)

Copy to clipboard

Converting a ctypes POINTER:

\>>> import ctypes
\>>> buffer \= (ctypes.c\_int \* 5)(0, 1, 2, 3, 4)
\>>> pointer \= ctypes.cast(buffer, ctypes.POINTER(ctypes.c\_int))
\>>> np\_array \= np.ctypeslib.as\_array(pointer, (5,))
\>>> np\_array
array(\[0, 1, 2, 3, 4\], dtype=int32)

Copy to clipboard

Go BackOpen In Tab

numpy.ctypeslib.as\_ctypes(_obj_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ctypeslib/_ctypeslib.py#L561-L603)
[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.as_ctypes "Link to this definition")

Create and return a ctypes object from a numpy array. Actually anything that exposes the \_\_array\_interface\_\_ is accepted.

Examples

Try it in your browser!

Create ctypes object from inferred int `np.array`:

\>>> inferred\_int\_array \= np.array(\[1, 2, 3\])
\>>> c\_int\_array \= np.ctypeslib.as\_ctypes(inferred\_int\_array)
\>>> type(c\_int\_array)
<class 'c\_long\_Array\_3'>
\>>> c\_int\_array\[:\]
\[1, 2, 3\]

Copy to clipboard

Create ctypes object from explicit 8 bit unsigned int `np.array` :

\>>> exp\_int\_array \= np.array(\[1, 2, 3\], dtype\=np.uint8)
\>>> c\_int\_array \= np.ctypeslib.as\_ctypes(exp\_int\_array)
\>>> type(c\_int\_array)
<class 'c\_ubyte\_Array\_3'>
\>>> c\_int\_array\[:\]
\[1, 2, 3\]

Copy to clipboard

Go BackOpen In Tab

numpy.ctypeslib.as\_ctypes\_type(_dtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ctypeslib/_ctypeslib.py#L463-L518)
[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.as_ctypes_type "Link to this definition")

Convert a dtype into a ctypes type.

Parameters:

**dtype**dtype

The dtype to convert

Returns:

ctype

A ctype scalar, union, array, or struct

Raises:

NotImplementedError

If the conversion is not possible

Notes

This function does not losslessly round-trip in either direction.

`np.dtype(as_ctypes_type(dt))` will:

*   insert padding fields
    
*   reorder fields to be sorted by offset
    
*   discard field titles
    

`as_ctypes_type(np.dtype(ctype))` will:

*   discard the class names of [`ctypes.Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "(in Python v3.14)")
    s and [`ctypes.Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "(in Python v3.14)")
    s
    
*   convert single-element [`ctypes.Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "(in Python v3.14)")
    s into single-element [`ctypes.Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "(in Python v3.14)")
    s
    
*   insert padding fields
    

Examples

Try it in your browser!

Converting a simple dtype:

\>>> dt \= np.dtype(np.int8)
\>>> ctype \= np.ctypeslib.as\_ctypes\_type(dt)
\>>> ctype
<class 'ctypes.c\_byte'>

Copy to clipboard

Converting a structured dtype:

\>>> dt \= np.dtype(\[('x', 'i4'), ('y', 'f4')\])
\>>> ctype \= np.ctypeslib.as\_ctypes\_type(dt)
\>>> ctype
<class 'struct'>

Copy to clipboard

Go BackOpen In Tab

numpy.ctypeslib.load\_library(_libname_, _loader\_path_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ctypeslib/_ctypeslib.py#L93-L165)
[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.load_library "Link to this definition")

It is possible to load a library using

\>>> lib \= ctypes.cdll\[<full\_path\_name\>\] 

Copy to clipboard

But there are cross-platform considerations, such as library file extensions, plus the fact Windows will just load the first library it finds with that name. NumPy supplies the load\_library function as a convenience.

Changed in version 1.20.0: Allow libname and loader\_path to take any [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object "(in Python v3.14)")
.

Parameters:

**libname**path-like

Name of the library, which can have ‘lib’ as a prefix, but without an extension.

**loader\_path**path-like

Where the library can be found.

Returns:

**ctypes.cdll\[libpath\]**library object

A ctypes library object

Raises:

OSError

If there is no library with the expected extension, or the library is defective and cannot be loaded.

numpy.ctypeslib.ndpointer(_dtype\=None_, _ndim\=None_, _shape\=None_, _flags\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ctypeslib/_ctypeslib.py#L238-L353)
[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.ndpointer "Link to this definition")

Array-checking restype/argtypes.

An ndpointer instance is used to describe an ndarray in restypes and argtypes specifications. This approach is more flexible than using, for example, `POINTER(c_double)`, since several restrictions can be specified, which are verified upon calling the ctypes function. These include data type, number of dimensions, shape and flags. If a given array does not satisfy the specified restrictions, a `TypeError` is raised.

Parameters:

**dtype**data-type, optional

Array data-type.

**ndim**int, optional

Number of array dimensions.

**shape**tuple of ints, optional

Array shape.

**flags**str or tuple of str

Array flags; may be one or more of:

*   C\_CONTIGUOUS / C / CONTIGUOUS
    
*   F\_CONTIGUOUS / F / FORTRAN
    
*   OWNDATA / O
    
*   WRITEABLE / W
    
*   ALIGNED / A
    
*   WRITEBACKIFCOPY / X
    

Returns:

**klass**ndpointer type object

A type object, which is an `_ndtpr` instance containing dtype, ndim, shape and flags information.

Raises:

TypeError

If a given array does not satisfy the specified restrictions.

Examples

Try it in your browser!

\>>> clib.somefunc.argtypes \= \[np.ctypeslib.ndpointer(dtype\=np.float64,\
...                                                  ndim\=1,\
...                                                  flags\='C\_CONTIGUOUS')\]
... 
\>>> clib.somefunc(np.array(\[1, 2, 3\], dtype\=np.float64))
... 

Copy to clipboard

Go BackOpen In Tab

_class_ numpy.ctypeslib.c\_intp[#](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.c_intp "Link to this definition")

A [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.14)")
 signed integer type of the same size as [`numpy.intp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intp "numpy.intp")
.

Depending on the platform, it can be an alias for either [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "(in Python v3.14)")
, [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "(in Python v3.14)")
 or [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "(in Python v3.14)")
.

On this page