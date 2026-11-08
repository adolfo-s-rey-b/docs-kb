[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.put_along_axis.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.put_along_axis.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.put_along_axis.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.put_along_axis.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.put_along_axis.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.put_along_axis.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.put_along_axis.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.put_along_axis.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.put_along_axis.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.put_along_axis.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.put_along_axis.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.put_along_axis.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.put_along_axis.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.put_along_axis.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.put_along_axis.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.put_along_axis.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.put_along_axis.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.put_along_axis.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.put_along_axis.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.put_along_axis.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.put\_along\_axis[#](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html#numpy-put-along-axis "Link to this heading")

==================================================================================================================================================

numpy.put\_along\_axis(_arr_, _indices_, _values_, _axis_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L186-L269)
[#](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html#numpy.put_along_axis "Link to this definition")

Put values into the destination array by matching 1d index and data slices.

This iterates over matching 1d slices oriented along the specified axis in the index and data arrays, and uses the former to place values into the latter. These slices can be different lengths.

Functions returning an index along an axis, like [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
 and [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")
, produce suitable indices for this function.

Parameters:

**arr**ndarray (Ni…, M, Nk…)

Destination array.

**indices**ndarray (Ni…, J, Nk…)

Indices to change along each 1d slice of _arr_. This must match the dimension of arr, but dimensions in Ni and Nj may be 1 to broadcast against _arr_.

**values**array\_like (Ni…, J, Nk…)

values to insert at those indices. Its shape and dimension are broadcast to match that of [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
.

**axis**int

The axis to take 1d slices along. If axis is None, the destination array is treated as if a flattened 1d view had been created of it.

See also

[`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Take values from the input array by matching 1d index and data slices

Notes

This is equivalent to (but faster than) the following use of [`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")
 and [`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")
, which sets each of `ii` and `kk` to a tuple of indices:

Ni, M, Nk \= a.shape\[:axis\], a.shape\[axis\], a.shape\[axis+1:\]
J \= indices.shape\[axis\]  \# Need not equal M

for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        a\_1d       \= a      \[ii + s\_\[:,\] + kk\]
        indices\_1d \= indices\[ii + s\_\[:,\] + kk\]
        values\_1d  \= values \[ii + s\_\[:,\] + kk\]
        for j in range(J):
            a\_1d\[indices\_1d\[j\]\] \= values\_1d\[j\]

Copy to clipboard

Equivalently, eliminating the inner loop, the last two lines would be:

a\_1d\[indices\_1d\] \= values\_1d

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

For this sample array

\>>> a \= np.array(\[\[10, 30, 20\], \[60, 40, 50\]\])

Copy to clipboard

We can replace the maximum values with:

\>>> ai \= np.argmax(a, axis\=1, keepdims\=True)
\>>> ai
array(\[\[1\],\
       \[0\]\])
\>>> np.put\_along\_axis(a, ai, 99, axis\=1)
\>>> a
array(\[\[10, 99, 20\],\
       \[99, 40, 50\]\])

Copy to clipboard

Go BackOpen In Tab

On this page