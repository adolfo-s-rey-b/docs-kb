[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.array.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.array.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.array.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.array.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.array.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.array.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.array.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.array.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.array.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.array.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.array.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.array.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.array.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.array.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.array.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.array.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.array.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.array.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.array.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.array.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.array[#](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy-char-array "Link to this heading")

====================================================================================================================================

char.array(_obj_, _itemsize\=None_, _copy\=True_, _unicode\=None_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/defchararray.py#L1220-L1364)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array "Link to this definition")

Create a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
.

Deprecated since version 2.5: `chararray` is deprecated. Use an `ndarray` with a string or bytes dtype instead.

Note

This class is provided for numarray backward-compatibility. New code (not concerned with numarray compatibility) should use arrays of type [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 or [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
 and use the free functions in [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
 for fast vectorized string operations instead.

Versus a NumPy array of dtype [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 or [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
, this class adds the following functionality:

1.  values automatically have whitespace removed from the end when indexed
    
2.  comparison operators automatically remove whitespace from the end when comparing values
    
3.  vectorized string operations are provided as methods (e.g. [`chararray.endswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.endswith.html#numpy.char.chararray.endswith "numpy.char.chararray.endswith")
    ) and infix operators (e.g. `+, *, %`)
    

Parameters:

**obj**array of str or unicode-like

**itemsize**int, optional

_itemsize_ is the number of characters per scalar in the resulting array. If _itemsize_ is None, and _obj_ is an object array or a Python list, the _itemsize_ will be automatically determined. If _itemsize_ is provided and _obj_ is of type str or unicode, then the _obj_ string will be chunked into _itemsize_ pieces.

**copy**bool, optional

If true (default), then the object is copied. Otherwise, a copy will only be made if `__array__` returns a copy, if obj is a nested sequence, or if a copy is needed to satisfy any of the other requirements (_itemsize_, unicode, _order_, etc.).

**unicode**bool, optional

When true, the resulting [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 can contain Unicode characters, when false only 8-bit characters. If unicode is None and _obj_ is one of the following:

*   a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
    ,
    
*   an ndarray of type [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
     or [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
    
*   a Python [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
     or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")
     object,
    

then the unicode setting of the output array will be automatically determined.

**order**{‘C’, ‘F’, ‘A’}, optional

Specify the order of the array. If order is ‘C’ (default), then the array will be in C-contiguous order (last-index varies the fastest). If order is ‘F’, then the returned array will be in Fortran-contiguous order (first-index varies the fastest). If order is ‘A’, then the returned array may be in any order (either C-, Fortran-contiguous, or even discontiguous).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> char\_array \= np.char.array(\['hello', 'world', 'numpy','array'\])
\>>> char\_array
chararray(\['hello', 'world', 'numpy', 'array'\], dtype='<U5')

Copy to clipboard

Go BackOpen In Tab

On this page