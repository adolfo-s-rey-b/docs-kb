### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/memoryview.html "MemoryView objects")
     |
*   [previous](https://docs.python.org/3/c-api/descriptor.html "Descriptor Objects")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Slice Objects](https://docs.python.org/3/c-api/slice.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Slice Objects[¶](https://docs.python.org/3/c-api/slice.html#slice-objects "Link to this heading")

==================================================================================================

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PySlice\_Type[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for slice objects. This is the same as [`slice`](https://docs.python.org/3/builtins/functions.html#slice "slice")
 in the Python layer.

int PySlice\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_Check "Link to this definition")
  

Return true if _ob_ is a slice object; _ob_ must not be `NULL`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySlice\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*stop, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*step)[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new slice object with the given values. The _start_, _stop_, and _step_ parameters are used as the values of the slice object attributes of the same names. Any of the values may be `NULL`, in which case the `None` will be used for the corresponding attribute.

Return `NULL` with an exception set if the new object could not be allocated.

int PySlice\_GetIndices([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*slice, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*stop, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*step)[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndices "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Retrieve the start, stop and step indices from the slice object _slice_, assuming a sequence of length _length_. Treats indices greater than _length_ as errors.

Returns `0` on success and `-1` on error with no exception set (unless one of the indices was not `None` and failed to be converted to an integer, in which case `-1` is returned with an exception set).

You probably do not want to use this function.

Changed in version 3.2: The parameter type for the _slice_ parameter was `PySliceObject*` before.

int PySlice\_GetIndicesEx([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*slice, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*stop, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*step, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*slicelength)[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndicesEx "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Usable replacement for [`PySlice_GetIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndices "PySlice_GetIndices")
. Retrieve the start, stop, and step indices from the slice object _slice_ assuming a sequence of length _length_, and store the length of the slice in _slicelength_. Out of bounds indices are clipped in a manner consistent with the handling of normal slices. _length_ must not be negative.

Return `0` on success and `-1` on error with an exception set.

Note

This function is considered not safe for resizable sequences. Its invocation should be replaced by a combination of [`PySlice_Unpack()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack")
 and [`PySlice_AdjustIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_AdjustIndices "PySlice_AdjustIndices")
 where

if (PySlice\_GetIndicesEx(slice, length, &start, &stop, &step, &slicelength) < 0) {
    // return error
}

is replaced by

if (PySlice\_Unpack(slice, &start, &stop, &step) < 0) {
    // return error
}
slicelength \= PySlice\_AdjustIndices(length, &start, &stop, step);

Changed in version 3.2: The parameter type for the _slice_ parameter was `PySliceObject*` before.

Changed in version 3.6.1: If `Py_LIMITED_API` is not set or set to the value between `0x03050400` and `0x03060000` (not including) or `0x03060100` or higher `PySlice_GetIndicesEx()` is implemented as a macro using `PySlice_Unpack()` and `PySlice_AdjustIndices()`. Arguments _start_, _stop_ and _step_ are evaluated more than once.

Deprecated since version 3.6.1: If `Py_LIMITED_API` is set to the value less than `0x03050400` or between `0x03060000` and `0x03060100` (not including) `PySlice_GetIndicesEx()` is a deprecated function.

int PySlice\_Unpack([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*slice, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*stop, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*step)[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Extract the start, stop and step data members from a slice object as C integers. Silently reduce values larger than `PY_SSIZE_T_MAX` to `PY_SSIZE_T_MAX`, silently boost the start and stop values less than `PY_SSIZE_T_MIN` to `PY_SSIZE_T_MIN`, and silently boost the step values less than `-PY_SSIZE_T_MAX` to `-PY_SSIZE_T_MAX`.

Return `-1` with an exception set on error, `0` on success.

Added in version 3.6.1.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PySlice\_AdjustIndices([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*stop, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 step)[¶](https://docs.python.org/3/c-api/slice.html#c.PySlice_AdjustIndices "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Adjust start/end slice indices assuming a sequence of the specified length. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.

_length_ must not be negative. _step_ must not be zero and must not be less than `-PY_SSIZE_T_MAX`, as guaranteed by [`PySlice_Unpack()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack")
.

Return the length of the slice. Always successful. Doesn’t call Python code.

Added in version 3.6.1.

Ellipsis Object[¶](https://docs.python.org/3/c-api/slice.html#ellipsis-object "Link to this heading")

------------------------------------------------------------------------------------------------------

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyEllipsis\_Type[¶](https://docs.python.org/3/c-api/slice.html#c.PyEllipsis_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type of Python [`Ellipsis`](https://docs.python.org/3/builtins/constants.html#Ellipsis "Ellipsis")
 object. Same as [`types.EllipsisType`](https://docs.python.org/3/library/types.html#types.EllipsisType "types.EllipsisType")
 in the Python layer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_Ellipsis[¶](https://docs.python.org/3/c-api/slice.html#c.Py_Ellipsis "Link to this definition")
  

The Python `Ellipsis` object. This object has no methods. Like [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")
, it is an [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 singleton object.

Changed in version 3.12: [`Py_Ellipsis`](https://docs.python.org/3/c-api/slice.html#c.Py_Ellipsis "Py_Ellipsis")
 is immortal.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Slice Objects](https://docs.python.org/3/c-api/slice.html#)
    *   [Ellipsis Object](https://docs.python.org/3/c-api/slice.html#ellipsis-object)
        

#### Previous topic

[Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html "previous chapter")

#### Next topic

[MemoryView objects](https://docs.python.org/3/c-api/memoryview.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Slice+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fslice.html&pagesource=c-api%2Fslice.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/slice.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/memoryview.html "MemoryView objects")
     |
*   [previous](https://docs.python.org/3/c-api/descriptor.html "Descriptor Objects")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Slice Objects](https://docs.python.org/3/c-api/slice.html)
    
*    
    
    |
*   Theme Auto Light Dark |