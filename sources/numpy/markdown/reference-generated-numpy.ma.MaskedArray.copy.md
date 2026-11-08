[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.copy.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.copy.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.copy.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.copy.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.copy.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.copy.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.copy.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.copy.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.copy.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.copy[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.copy.html#numpy-ma-maskedarray-copy "Link to this heading")

===============================================================================================================================================================

method

ma.MaskedArray.copy(_order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2642-L2652)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.copy.html#numpy.ma.MaskedArray.copy "Link to this definition")

Return a copy of the array.

Parameters:

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

Controls the memory layout of the copy. ‘C’ means C-order, ‘F’ means F-order, ‘A’ means ‘F’ if _a_ is Fortran contiguous, ‘C’ otherwise. ‘K’ means match the layout of _a_ as closely as possible. (Note that this function and [`numpy.copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 are very similar but have different default values for their order= arguments, and this function always passes sub-classes through.)

See also

[`numpy.copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")

Similar function with different default behavior

[`numpy.copyto`](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "numpy.copyto")

Notes

This function is the preferred method for creating an array copy. The function [`numpy.copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 is similar, but it defaults to using order ‘K’, and will not pass sub-classes through by default.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[1,2,3\],\[4,5,6\]\], order\='F')

Copy to clipboard

\>>> y \= x.copy()

Copy to clipboard

\>>> x.fill(0)

Copy to clipboard

\>>> x
array(\[\[0, 0, 0\],\
       \[0, 0, 0\]\])

Copy to clipboard

\>>> y
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])

Copy to clipboard

\>>> y.flags\['C\_CONTIGUOUS'\]
True

Copy to clipboard

For arrays containing Python objects (e.g. dtype=np.object\_), the copy is a shallow one. The new array will contain the same object which may lead to surprises if that object can be modified (is mutable):

\>>> a \= np.array(\[1, 'm', \[2, 3, 4\]\], dtype\=np.object\_)
\>>> b \= a.copy()
\>>> b\[2\]\[0\] \= 10
\>>> a
array(\[1, 'm', list(\[10, 3, 4\])\], dtype=object)

Copy to clipboard

To ensure all elements within an `object` array are copied, use [`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.14)")
:

\>>> import copy
\>>> a \= np.array(\[1, 'm', \[2, 3, 4\]\], dtype\=np.object\_)
\>>> c \= copy.deepcopy(a)
\>>> c\[2\]\[0\] \= 10
\>>> c
array(\[1, 'm', list(\[10, 3, 4\])\], dtype=object)
\>>> a
array(\[1, 'm', list(\[2, 3, 4\])\], dtype=object)

Copy to clipboard

Go BackOpen In Tab

On this page