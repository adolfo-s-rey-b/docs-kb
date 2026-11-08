[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rec.array.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rec.array.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rec.array.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rec.array.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rec.array.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rec.array.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rec.array.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rec.array.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rec.array.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rec.array.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rec.array.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rec.array.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rec.array.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rec.array.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rec.array.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rec.array.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rec.array.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rec.array.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rec.array.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rec.array.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rec.array[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#numpy-rec-array "Link to this heading")

=================================================================================================================================

rec.array(_obj_, _dtype\=None_, _shape\=None_, _offset\=0_, _strides\=None_, _formats\=None_, _names\=None_, _titles\=None_, _aligned\=False_, _byteorder\=None_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L942-L1089)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#numpy.rec.array "Link to this definition")

Construct a record array from a wide-variety of objects.

A general-purpose record array constructor that dispatches to the appropriate [`recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 creation function based on the inputs (see Notes).

Parameters:

**obj**any

Input object. See Notes for details on how various input types are treated.

**dtype**data-type, optional

Valid dtype for array.

**shape**int or tuple of ints, optional

Shape of each array.

**offset**int, optional

Position in the file or buffer to start reading from.

**strides**tuple of ints, optional

Buffer (_buf_) is interpreted according to these strides (strides define how many bytes each array element, row, column, etc. occupy in memory).

**formats, names, titles, aligned, byteorder**

If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is `None`, these arguments are passed to _numpy.format\_parser_ to construct a dtype. See that function for detailed documentation.

**copy**bool, optional

Whether to copy the input object (True), or to use a reference instead. This option only applies when the input is an ndarray or recarray. Defaults to True.

Returns:

np.recarray

Record array created from the specified object.

Notes

If _obj_ is `None`, then call the [`recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 constructor. If _obj_ is a string, then call the [`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")
 constructor. If _obj_ is a list or a tuple, then if the first object is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, call [`fromarrays`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html#numpy.rec.fromarrays "numpy.rec.fromarrays")
, otherwise call [`fromrecords`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#numpy.rec.fromrecords "numpy.rec.fromrecords")
. If _obj_ is a [`recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
, then make a copy of the data in the recarray (if `copy=True`) and use the new formats, names, and titles. If _obj_ is a file, then call [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")
. Finally, if obj is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, then return `obj.view(recarray)`, making a copy of the data if `copy=True`.

Examples

Try it in your browser!

\>>> a \= np.array(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\])
\>>> a
array(\[\[1, 2, 3\],\
       \[4, 5, 6\],\
       \[7, 8, 9\]\])

Copy to clipboard

\>>> np.rec.array(a)
rec.array(\[\[1, 2, 3\],\
           \[4, 5, 6\],\
           \[7, 8, 9\]\],
          dtype=int64)

Copy to clipboard

\>>> b \= \[(1, 1), (2, 4), (3, 9)\]
\>>> c \= np.rec.array(b, formats \= \['i2', 'f2'\], names \= ('x', 'y'))
\>>> c
rec.array(\[(1, 1.), (2, 4.), (3, 9.)\],
          dtype=\[('x', '<i2'), ('y', '<f2')\])

Copy to clipboard

\>>> c.x
array(\[1, 2, 3\], dtype=int16)

Copy to clipboard

\>>> c.y
array(\[1.,  4.,  9.\], dtype=float16)

Copy to clipboard

\>>> r \= np.rec.array(\['abc','def'\], names\=\['col1','col2'\])
\>>> print(r.col1)
abc

Copy to clipboard

\>>> r.col1
array('abc', dtype='<U3')

Copy to clipboard

\>>> r.col2
array('def', dtype='<U3')

Copy to clipboard

Go BackOpen In Tab

On this page