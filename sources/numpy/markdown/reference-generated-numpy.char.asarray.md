[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.asarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.asarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.asarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.asarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.asarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.asarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.asarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.asarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.asarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.asarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.asarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.asarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.asarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.asarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.asarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.asarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.asarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.asarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.asarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.asarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.asarray[#](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html#numpy-char-asarray "Link to this heading")

==========================================================================================================================================

char.asarray(_obj_, _itemsize\=None_, _unicode\=None_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/defchararray.py#L1367-L1429)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html#numpy.char.asarray "Link to this definition")

Convert the input to a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
, copying the data only if necessary.

Deprecated since version 2.5: `chararray` is deprecated. Use an `ndarray` with a string or bytes dtype instead.

Versus a NumPy array of dtype [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 or [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
, this class adds the following functionality:

1.  values automatically have whitespace removed from the end when indexed
    
2.  comparison operators automatically remove whitespace from the end when comparing values
    
3.  vectorized string operations are provided as methods (e.g. [`chararray.endswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.endswith.html#numpy.char.chararray.endswith "numpy.char.chararray.endswith")
    ) and infix operators (e.g. `+`, `*`, `%`)
    

Parameters:

**obj**array of str or unicode-like

**itemsize**int, optional

_itemsize_ is the number of characters per scalar in the resulting array. If _itemsize_ is None, and _obj_ is an object array or a Python list, the _itemsize_ will be automatically determined. If _itemsize_ is provided and _obj_ is of type str or unicode, then the _obj_ string will be chunked into _itemsize_ pieces.

**unicode**bool, optional

When true, the resulting [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 can contain Unicode characters, when false only 8-bit characters. If unicode is None and _obj_ is one of the following:

*   a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
    ,
    
*   an ndarray of type [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
     or _unicode\__
    
*   a Python str or unicode object,
    

then the unicode setting of the output array will be automatically determined.

**order**{‘C’, ‘F’}, optional

Specify the order of the array. If order is ‘C’ (default), then the array will be in C-contiguous order (last-index varies the fastest). If order is ‘F’, then the returned array will be in Fortran-contiguous order (first-index varies the fastest).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.char.asarray(\['hello', 'world'\])
chararray(\['hello', 'world'\], dtype='<U5')

Copy to clipboard

Go BackOpen In Tab

On this page