[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.take.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.take.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.take.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.take.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.take.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.take.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.take.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.take.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.take.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.take.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.take.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.take.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.take.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.take.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.take.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.take.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.take.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.take.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.take.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.take.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.take.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.take.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.take[#](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy-take "Link to this heading")

==================================================================================================================

numpy.take(_a_, _indices_, _axis\=None_, _out\=None_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L106-L200)
[#](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "Link to this definition")

Take elements from an array along an axis.

When axis is not None, this function does the same thing as “fancy” indexing (indexing arrays using arrays); however, it can be easier to use if you need elements along a given axis. A call such as `np.take(arr, indices, axis=3)` is equivalent to `arr[:,:,:,indices,...]`.

Explained without fancy indexing, this is equivalent to the following use of [`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")
, which sets each of `ii`, `jj`, and `kk` to a tuple of indices:

Ni, Nk \= a.shape\[:axis\], a.shape\[axis+1:\]
Nj \= indices.shape
for ii in ndindex(Ni):
    for jj in ndindex(Nj):
        for kk in ndindex(Nk):
            out\[ii + jj + kk\] \= a\[ii + (indices\[jj\],) + kk\]

Copy to clipboard

Parameters:

**a**array\_like (Ni…, M, Nk…)

The source array.

**indices**array\_like (Nj…)

The indices of the values to extract. Also allow scalars for indices.

**axis**int, optional

The axis over which to select values. By default, the flattened input array is used.

**out**ndarray, optional (Ni…, Nj…, Nk…)

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype. Note that _out_ is always buffered if _mode=’raise’_; use other modes for better performance.

**mode**{‘raise’, ‘wrap’, ‘clip’}, optional

Specifies how out-of-bounds indices will behave.

*   ‘raise’ – raise an error (default)
    
*   ‘wrap’ – wrap around
    
*   ‘clip’ – clip to the range
    

‘clip’ mode means that all indices that are too large are replaced by the index that addresses the last element along that axis. Note that this disables indexing with negative numbers.

Returns:

**out**ndarray (Ni…, Nj…, Nk…)

The returned array has the same type as _a_.

See also

[`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")

Take elements using a boolean mask

[`ndarray.take`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "numpy.ndarray.take")

equivalent method

[`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Take elements by matching the array and the index arrays

Notes

By eliminating the inner loop in the description above, and using [`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")
 to build simple slice objects, [`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
 can be expressed in terms of applying fancy indexing to each 1-d slice:

Ni, Nk \= a.shape\[:axis\], a.shape\[axis+1:\]
for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        out\[ii + s\_\[...,\] + kk\] \= a\[ii + s\_\[:,\] + kk\]\[indices\]

Copy to clipboard

For this reason, it is equivalent to (but faster than) the following use of [`apply_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis")
:

out \= np.apply\_along\_axis(lambda a\_1d: a\_1d\[indices\], axis, a)

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= \[4, 3, 5, 7, 6, 8\]
\>>> indices \= \[0, 1, 4\]
\>>> np.take(a, indices)
array(\[4, 3, 6\])

Copy to clipboard

In this example if _a_ is an ndarray, “fancy” indexing can be used.

\>>> a \= np.array(a)
\>>> a\[indices\]
array(\[4, 3, 6\])

Copy to clipboard

If [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
 is not one dimensional, the output also has these dimensions.

\>>> np.take(a, \[\[0, 1\], \[2, 3\]\])
array(\[\[4, 3\],\
       \[5, 7\]\])

Copy to clipboard

Go BackOpen In Tab

On this page