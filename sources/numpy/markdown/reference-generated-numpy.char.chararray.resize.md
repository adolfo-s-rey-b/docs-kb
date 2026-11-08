[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.chararray.resize.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.chararray.resize.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.chararray.resize.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.chararray.resize.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.chararray.resize.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.chararray.resize.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.chararray.resize.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.chararray.resize.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.chararray.resize.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.chararray.resize.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.chararray.resize.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.chararray.resize.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.chararray.resize.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.chararray.resize.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.chararray.resize.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.chararray.resize.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.chararray.resize.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.chararray.resize.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.chararray.resize.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.chararray.resize.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray.resize[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html#numpy-char-chararray-resize "Link to this heading")

=====================================================================================================================================================================

method

char.chararray.resize(_new\_shape_, _/_, _\*_, _refcheck=True) a.resize(\*new\_shape_, _refcheck=True_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html#numpy.char.chararray.resize "Link to this definition")

char.chararray.resize(_\*new\_shape_, _refcheck\=True_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

Change shape and size of array in-place.

Parameters:

**new\_shape**tuple of ints, or _n_ ints

Shape of resized array.

**refcheck**bool, optional

If False, reference count will not be checked. Default is True. See Notes below for more explanation.

Returns:

None

Raises:

ValueError

If _a_ does not own its own data or references or views to may exist.

See also

[`resize`](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "numpy.resize")

Return a new array with the specified shape.

Notes

This reallocates space for the data area if necessary.

Only contiguous arrays (data elements consecutive in memory) can be resized.

Reallocating arrays in-place can often lead to memory fragmentation and should be avoided. If the goal is to reclaim over-allocated memory, alternatives are to create a view or a copy of just the desired data, or using two passes to build the array: one to cheaply determine the shape and another to allocate and fill. Benchmark your use case to determine what is optimum. You may be surprised to find `resize` actually slows down or bloats your application.

The purpose of the reference count check is to make sure you do not use this array as a buffer for another Python object and then reallocate the memory.

On Python 3.13 and older, the check allows objects with exactly one reference to be reallocated in-place. On Python 3.14 and newer, the array must be uniquely referenced. See [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html#rc6eae7383568-1)
 for more details.

If you are sure that you have not shared the memory for this array with another Python object, then you may safely set _refcheck_ to False.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html#id1)\
\]

Python 3.14 What’s New, [https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-refcount](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-refcount)

Examples

Try it in your browser!

Shrinking an array: array is flattened (in the order that the data are stored in memory), resized, and reshaped:

\>>> import numpy as np

Copy to clipboard

\>>> a \= np.array(\[\[0, 1\], \[2, 3\]\], order\='C')
\>>> a.resize((2, 1))
\>>> a
array(\[\[0\],\
       \[1\]\])

Copy to clipboard

\>>> a \= np.array(\[\[0, 1\], \[2, 3\]\], order\='F')
\>>> a.resize((2, 1))
\>>> a
array(\[\[0\],\
       \[2\]\])

Copy to clipboard

Enlarging an array: as above, but missing entries are filled with zeros:

\>>> b \= np.array(\[\[0, 1\], \[2, 3\]\])
\>>> b.resize(2, 3) \# new\_shape parameter doesn't have to be a tuple
\>>> b
array(\[\[0, 1, 2\],\
       \[3, 0, 0\]\])

Copy to clipboard

Referencing an array prevents resizing…

\>>> c \= a
\>>> a.resize((1, 1))
Traceback (most recent call last):
...
ValueError: cannot resize an array that references or is referenced ...

Copy to clipboard

Unless _refcheck_ is False:

\>>> a.resize((1, 1), refcheck\=False)
\>>> a
array(\[\[0\]\])
\>>> c
array(\[\[0\]\])

Copy to clipboard

Go BackOpen In Tab

On this page