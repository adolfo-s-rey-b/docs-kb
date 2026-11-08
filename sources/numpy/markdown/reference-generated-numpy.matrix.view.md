[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.view.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.view.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.view.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.view.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.view.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.view.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.view.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.view.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.view.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.view.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.view.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.view.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.view.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.view.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.view.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.view.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.view.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.view.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.view.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.view.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.view.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.view.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.view[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.view.html#numpy-matrix-view "Link to this heading")

=======================================================================================================================================

method

matrix.view(_\[dtype\]\[, type\]_)[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.view.html#numpy.matrix.view "Link to this definition")

New view of array with the same data.

Note

Passing None for `dtype` is different from omitting the parameter, since the former invokes `dtype(None)` which is an alias for `dtype(np.float64)`.

Parameters:

**dtype**data-type or ndarray sub-class, optional

Data-type descriptor of the returned view, e.g., float32 or int16. Omitting it results in the view having the same data-type as _a_. This argument can also be specified as an ndarray sub-class, which then specifies the type of the returned object (this is equivalent to setting the `type` parameter).

**type**Python type, optional

Type of the returned view, e.g., ndarray or matrix. Again, omission of the parameter results in type preservation.

Notes

`a.view()` is used two different ways:

`a.view(some_dtype)` or `a.view(dtype=some_dtype)` constructs a view of the array’s memory with a different data-type. This can cause a reinterpretation of the bytes of memory.

`a.view(ndarray_subclass)` or `a.view(type=ndarray_subclass)` just returns an instance of _ndarray\_subclass_ that looks at the same array (same shape, dtype, etc.) This does not cause a reinterpretation of the memory.

For `a.view(some_dtype)`, if `some_dtype` has a different number of bytes per entry than the previous dtype (for example, converting a regular array to a structured array), then the last axis of `a` must be contiguous. This axis will be resized in the result.

Changed in version 1.23.0: Only the last axis needs to be contiguous. Previously, the entire array had to be C-contiguous.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[(\-1, 2)\], dtype\=\[('a', np.int8), ('b', np.int8)\])

Copy to clipboard

Viewing array data using a different type and dtype:

\>>> nonneg \= np.dtype(\[("a", np.uint8), ("b", np.uint8)\])
\>>> y \= x.view(dtype\=nonneg, type\=np.recarray)
\>>> x\["a"\]
array(\[-1\], dtype=int8)
\>>> y.a
array(\[255\], dtype=uint8)

Copy to clipboard

Creating a view on a structured array so it can be used in calculations

\>>> x \= np.array(\[(1, 2),(3,4)\], dtype\=\[('a', np.int8), ('b', np.int8)\])
\>>> xv \= x.view(dtype\=np.int8).reshape(\-1,2)
\>>> xv
array(\[\[1, 2\],\
       \[3, 4\]\], dtype=int8)
\>>> xv.mean(0)
array(\[2.,  3.\])

Copy to clipboard

Making changes to the view changes the underlying array

\>>> xv\[0,1\] \= 20
\>>> x
array(\[(1, 20), (3,  4)\], dtype=\[('a', 'i1'), ('b', 'i1')\])

Copy to clipboard

Using a view to convert an array to a recarray:

\>>> z \= x.view(np.recarray)
\>>> z.a
array(\[1, 3\], dtype=int8)

Copy to clipboard

Views share data:

\>>> x\[0\] \= (9, 10)
\>>> z\[0\]
np.record((9, 10), dtype=\[('a', 'i1'), ('b', 'i1')\])

Copy to clipboard

Views that change the dtype size (bytes per entry) should normally be avoided on arrays defined by slices, transposes, fortran-ordering, etc.:

\>>> x \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\], dtype\=np.int16)
\>>> y \= x\[:, ::2\]
\>>> y
array(\[\[1, 3\],\
       \[4, 6\]\], dtype=int16)
\>>> y.view(dtype\=\[('width', np.int16), ('length', np.int16)\])
Traceback (most recent call last):
    ...
ValueError: To change to a dtype of a different size, the last axis must be contiguous
\>>> z \= y.copy()
\>>> z.view(dtype\=\[('width', np.int16), ('length', np.int16)\])
array(\[\[(1, 3)\],\
       \[(4, 6)\]\], dtype=\[('width', '<i2'), ('length', '<i2')\])

Copy to clipboard

However, views that change dtype are totally fine for arrays with a contiguous last axis, even if the rest of the axes are not C-contiguous:

\>>> x \= np.arange(2 \* 3 \* 4, dtype\=np.int8).reshape(2, 3, 4)
\>>> x.transpose(1, 0, 2).view(np.int16)
array(\[\[\[ 256,  770\],\
        \[3340, 3854\]\],\
\
       \[\[1284, 1798\],\
        \[4368, 4882\]\],\
\
       \[\[2312, 2826\],\
        \[5396, 5910\]\]\], dtype=int16)

Copy to clipboard

Go BackOpen In Tab

On this page