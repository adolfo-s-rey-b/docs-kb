[Skip to main content](https://numpy.org/doc/stable/user/basics.copies.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/basics.copies.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/basics.copies.html)
[2.4](https://numpy.org/doc/2.4/user/basics.copies.html)
[2.3](https://numpy.org/doc/2.3/user/basics.copies.html)
[2.2](https://numpy.org/doc/2.2/user/basics.copies.html)
[2.1](https://numpy.org/doc/2.1/user/basics.copies.html)
[2.0](https://numpy.org/doc/2.0/user/basics.copies.html)
[1.26](https://numpy.org/doc/1.26/user/basics.copies.html)
[1.25](https://numpy.org/doc/1.25/user/basics.copies.html)
[1.24](https://numpy.org/doc/1.24/user/basics.copies.html)
[1.23](https://numpy.org/doc/1.23/user/basics.copies.html)
[1.22](https://numpy.org/doc/1.22/user/basics.copies.html)
[1.21](https://numpy.org/doc/1.21/user/basics.copies.html)
[1.20](https://numpy.org/doc/1.20/user/basics.copies.html)
[1.19](https://numpy.org/doc/1.19/user/basics.copies.html)
[1.18](https://numpy.org/doc/1.18/user/basics.copies.html)
[1.17](https://numpy.org/doc/1.17/user/basics.copies.html)
[1.16](https://numpy.org/doc/1.16/user/basics.copies.html)
[1.15](https://numpy.org/doc/1.15/user/basics.copies.html)
[1.14](https://numpy.org/doc/1.14/user/basics.copies.html)
[1.13](https://numpy.org/doc/1.13/user/basics.copies.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Copies and views[#](https://numpy.org/doc/stable/user/basics.copies.html#copies-and-views "Link to this heading")

==================================================================================================================

When operating on NumPy arrays, it is possible to access the internal data buffer directly using a [view](https://numpy.org/doc/stable/user/basics.copies.html#view)
 without copying data around. This ensures good performance but can also cause unwanted problems if the user is not aware of how this works. Hence, it is important to know the difference between these two terms and to know which operations return copies and which return views.

The NumPy array is a data structure consisting of two parts: the [contiguous](https://numpy.org/doc/stable/glossary.html#term-contiguous)
 data buffer with the actual data elements and the metadata that contains information about the data buffer. The metadata includes data type, strides, and other important information that helps manipulate the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 easily. See the [Internal organization of NumPy arrays](https://numpy.org/doc/stable/dev/internals.html#numpy-internals)
 section for a detailed look.

View[#](https://numpy.org/doc/stable/user/basics.copies.html#view "Link to this heading")

------------------------------------------------------------------------------------------

It is possible to access the array differently by just changing certain metadata like [stride](https://numpy.org/doc/stable/glossary.html#term-stride)
 and [dtype](https://numpy.org/doc/stable/glossary.html#term-dtype)
 without changing the data buffer. This creates a new way of looking at the data and these new arrays are called views. The data buffer remains the same, so any changes made to a view reflects in the original copy. A view can be forced through the [`ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")
 method.

Copy[#](https://numpy.org/doc/stable/user/basics.copies.html#copy "Link to this heading")

------------------------------------------------------------------------------------------

When a new array is created by duplicating the data buffer as well as the metadata, it is called a copy. Changes made to the copy do not reflect on the original array. Making a copy is slower and memory-consuming but sometimes necessary. A copy can be forced by using [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")
.

Indexing operations[#](https://numpy.org/doc/stable/user/basics.copies.html#indexing-operations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

See also

[Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing)

Views are created when elements can be addressed with offsets and strides in the original array. Hence, basic indexing always creates views. For example:

\>>> import numpy as np
\>>> x \= np.arange(10)
\>>> x
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> y \= x\[1:3\]  \# creates a view
\>>> y
array(\[1, 2\])
\>>> x\[1:3\] \= \[10, 11\]
\>>> x
array(\[ 0, 10, 11,  3,  4,  5,  6,  7,  8,  9\])
\>>> y
array(\[10, 11\])

Copy to clipboard

Here, `y` gets changed when `x` is changed because it is a view.

[Advanced indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing)
, on the other hand, always creates copies. For example:

\>>> import numpy as np
\>>> x \= np.arange(9).reshape(3, 3)
\>>> x
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> y \= x\[\[1, 2\]\]
\>>> y
array(\[\[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> y.base is None
True

Copy to clipboard

Here, `y` is a copy, as signified by the [`base`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base")
 attribute. We can also confirm this by assigning new values to `x[[1, 2]]` which in turn will not affect `y` at all:

\>>> x\[\[1, 2\]\] \= \[\[10, 11, 12\], \[13, 14, 15\]\]
\>>> x
array(\[\[ 0,  1,  2\],\
       \[10, 11, 12\],\
       \[13, 14, 15\]\])
\>>> y
array(\[\[3, 4, 5\],\
       \[6, 7, 8\]\])

Copy to clipboard

It must be noted here that during the assignment of `x[[1, 2]]` no view or copy is created as the assignment happens in-place.

Other operations[#](https://numpy.org/doc/stable/user/basics.copies.html#other-operations "Link to this heading")

------------------------------------------------------------------------------------------------------------------

The [`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
 function creates a view where possible or a copy otherwise. In most cases, the strides can be modified to reshape the array with a view. However, in some cases where the array becomes non-contiguous (perhaps after a [`ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose")
 operation), the reshaping cannot be done by modifying strides and requires a copy.

Taking the example of another operation, [`numpy.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
 returns a contiguous flattened view of the array wherever possible. On the other hand, [`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")
 always returns a flattened copy of the array. However, to guarantee a view in most cases, `x.reshape(-1)` may be preferable.

How to tell if the array is a view or a copy[#](https://numpy.org/doc/stable/user/basics.copies.html#how-to-tell-if-the-array-is-a-view-or-a-copy "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`base`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base")
 attribute of the ndarray makes it easy to tell if an array is a view or a copy. The base attribute of a view returns the original array while it returns `None` for a copy.

\>>> import numpy as np
\>>> x \= np.arange(9)
\>>> x
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8\])
\>>> y \= x.reshape(3, 3)
\>>> y
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> y.base  \# .reshape() creates a view
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8\])
\>>> z \= y\[\[2, 1\]\]
\>>> z
array(\[\[6, 7, 8\],\
       \[3, 4, 5\]\])
\>>> z.base is None  \# advanced indexing creates a copy
True

Copy to clipboard

Note that the `base` attribute should not be used to determine if an ndarray object is _new_; only if it is a view or a copy of another ndarray.

On this page