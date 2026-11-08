[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.argmax.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.argmax.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.argmax.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.argmax.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.argmax.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.argmax.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.argmax.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.argmax.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.argmax.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.argmax.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.argmax.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.argmax.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.argmax.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.argmax.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.argmax.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.argmax.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.argmax.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.argmax.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.argmax.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.argmax.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.argmax[#](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy-argmax "Link to this heading")

========================================================================================================================

numpy.argmax(_a_, _axis=None_, _out=None_, _\*_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1259-L1352)
[#](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "Link to this definition")

Returns the indices of the maximum values along an axis.

Parameters:

**a**array\_like

Input array.

**axis**int, optional

By default, the index is into the flattened array, otherwise along the specified axis.

**out**array, optional

If provided, the result will be inserted into this array. It should be of the appropriate shape and dtype.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the array.

New in version 1.22.0.

Returns:

**index\_array**ndarray of ints

Array of indices into the array. It has the same shape as `a.shape` with the dimension along _axis_ removed. If _keepdims_ is set to True, then the size of _axis_ will be 1 with the resulting array having same shape as `a.shape`.

See also

[`ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")
, [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")

[`amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")

The maximum value along a given axis.

[`unravel_index`](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html#numpy.unravel_index "numpy.unravel_index")

Convert a flat index into an index tuple.

[`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Apply `np.expand_dims(index_array, axis)` from argmax to an array as if by calling max.

Notes

In case of multiple occurrences of the maximum values, the indices corresponding to the first occurrence are returned.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(6).reshape(2,3) + 10
\>>> a
array(\[\[10, 11, 12\],\
       \[13, 14, 15\]\])
\>>> np.argmax(a)
5
\>>> np.argmax(a, axis\=0)
array(\[1, 1, 1\])
\>>> np.argmax(a, axis\=1)
array(\[2, 2\])

Copy to clipboard

Indexes of the maximal elements of an N-dimensional array:

\>>> a.flat\[np.argmax(a)\]
15
\>>> ind \= np.unravel\_index(np.argmax(a, axis\=None), a.shape)
\>>> ind
(1, 2)
\>>> a\[ind\]
15

Copy to clipboard

\>>> b \= np.arange(6)
\>>> b\[1\] \= 5
\>>> b
array(\[0, 5, 2, 3, 4, 5\])
\>>> np.argmax(b)  \# Only the first occurrence is returned.
1

Copy to clipboard

\>>> x \= np.array(\[\[4,2,3\], \[1,0,3\]\])
\>>> index\_array \= np.argmax(x, axis\=-1)
\>>> \# Same as np.amax(x, axis=-1, keepdims=True)
\>>> np.take\_along\_axis(x, np.expand\_dims(index\_array, axis\=-1), axis\=-1)
array(\[\[4\],\
       \[3\]\])
\>>> \# Same as np.amax(x, axis=-1)
\>>> np.take\_along\_axis(x, np.expand\_dims(index\_array, axis\=-1),
...     axis\=-1).squeeze(axis\=-1)
array(\[4, 3\])

Copy to clipboard

Setting _keepdims_ to _True_,

\>>> x \= np.arange(24).reshape((2, 3, 4))
\>>> res \= np.argmax(x, axis\=1, keepdims\=True)
\>>> res.shape
(2, 1, 4)

Copy to clipboard

Go BackOpen In Tab

On this page