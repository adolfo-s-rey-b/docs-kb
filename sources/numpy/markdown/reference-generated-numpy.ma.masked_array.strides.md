[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.strides.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.strides.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.strides.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.strides.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.strides.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.strides.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.strides.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.strides.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.strides.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.strides.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.strides.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.strides.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.strides.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.strides.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.strides.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.strides.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.strides.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.strides.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.strides.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.strides.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.strides.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.strides.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.strides[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.strides.html#numpy-ma-masked-array-strides "Link to this heading")

============================================================================================================================================================================

attribute

ma.masked\_array.strides[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.strides.html#numpy.ma.masked_array.strides "Link to this definition")

Tuple of bytes to step in each dimension when traversing an array.

The byte offset of element `(i[0], i[1], ..., i[n])` in an array _a_ is:

offset \= sum(np.array(i) \* a.strides)

Copy to clipboard

A more detailed explanation of strides can be found in [The N-dimensional array (ndarray)](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray)
.

Warning

Setting `arr.strides` is discouraged and may be deprecated in the future. [`numpy.lib.stride_tricks.as_strided`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "numpy.lib.stride_tricks.as_strided")
 should be preferred to create a new view of the same data in a safer way.

See also

[`numpy.lib.stride_tricks.as_strided`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "numpy.lib.stride_tricks.as_strided")

Notes

Imagine an array of 32-bit integers (each 4 bytes):

x \= np.array(\[\[0, 1, 2, 3, 4\],\
              \[5, 6, 7, 8, 9\]\], dtype\=np.int32)

Copy to clipboard

This array is stored in memory as 40 bytes, one after the other (known as a contiguous block of memory). The strides of an array tell us how many bytes we have to skip in memory to move to the next position along a certain axis. For example, we have to skip 4 bytes (1 value) to move to the next column, but 20 bytes (5 values) to get to the same position in the next row. As such, the strides for the array _x_ will be `(20, 4)`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> y \= np.reshape(np.arange(2 \* 3 \* 4, dtype\=np.int32), (2, 3, 4))
\>>> y
array(\[\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\],\
       \[\[12, 13, 14, 15\],\
        \[16, 17, 18, 19\],\
        \[20, 21, 22, 23\]\]\], dtype=np.int32)
\>>> y.strides
(48, 16, 4)
\>>> y\[1, 1, 1\]
np.int32(17)
\>>> offset \= sum(y.strides \* np.array((1, 1, 1)))
\>>> offset // y.itemsize
np.int64(17)

Copy to clipboard

\>>> x \= np.reshape(np.arange(5\*6\*7\*8, dtype\=np.int32), (5, 6, 7, 8))
\>>> x \= x.transpose(2, 3, 1, 0)
\>>> x.strides
(32, 4, 224, 1344)
\>>> i \= np.array(\[3, 5, 2, 2\], dtype\=np.int32)
\>>> offset \= sum(i \* x.strides)
\>>> x\[3, 5, 2, 2\]
np.int32(813)
\>>> offset // x.itemsize
np.int64(813)

Copy to clipboard

Go BackOpen In Tab

On this page