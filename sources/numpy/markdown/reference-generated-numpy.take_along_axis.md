[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.take_along_axis.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.take_along_axis.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.take_along_axis.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.take_along_axis.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.take_along_axis.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.take_along_axis.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.take_along_axis.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.take_along_axis.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.take_along_axis.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.take_along_axis.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.take_along_axis.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.take_along_axis.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.take_along_axis.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.take_along_axis.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.take_along_axis.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.take_along_axis.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.take_along_axis.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.take_along_axis.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.take_along_axis.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.take_along_axis.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.take\_along\_axis[#](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy-take-along-axis "Link to this heading")

=====================================================================================================================================================

numpy.take\_along\_axis(_arr_, _indices_, _axis\=\-1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L60-L179)
[#](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "Link to this definition")

Take values from the input array by matching 1d index and data slices.

This iterates over matching 1d slices oriented along the specified axis in the index and data arrays, and uses the former to look up values in the latter. These slices can be different lengths.

Functions returning an index along an axis, like [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
 and [`argpartition`](https://numpy.org/doc/stable/reference/generated/numpy.argpartition.html#numpy.argpartition "numpy.argpartition")
, produce suitable indices for this function.

Parameters:

**arr**ndarray (Ni…, M, Nk…)

Source array

**indices**ndarray (Ni…, J, Nk…)

Indices to take along each 1d slice of `arr`. This must match the dimension of `arr`, but dimensions Ni and Nj only need to broadcast against `arr`.

**axis**int or None, optional

The axis to take 1d slices along. If axis is None, the input array is treated as if it had first been flattened to 1d, for consistency with [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
 and [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
.

Changed in version 2.3: The default value is now `-1`.

Returns:

out: ndarray (Ni…, J, Nk…)

The indexed result.

See also

[`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")

Take along an axis, using the same indices for every 1d slice

[`put_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html#numpy.put_along_axis "numpy.put_along_axis")

Put values into the destination array by matching 1d index and data slices

Notes

This is equivalent to (but faster than) the following use of [`ndindex`](https://numpy.org/doc/stable/reference/generated/numpy.ndindex.html#numpy.ndindex "numpy.ndindex")
 and [`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")
, which sets each of `ii` and `kk` to a tuple of indices:

Ni, M, Nk \= a.shape\[:axis\], a.shape\[axis\], a.shape\[axis+1:\]
J \= indices.shape\[axis\]  \# Need not equal M
out \= np.empty(Ni + (J,) + Nk)

for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        a\_1d       \= a      \[ii + s\_\[:,\] + kk\]
        indices\_1d \= indices\[ii + s\_\[:,\] + kk\]
        out\_1d     \= out    \[ii + s\_\[:,\] + kk\]
        for j in range(J):
            out\_1d\[j\] \= a\_1d\[indices\_1d\[j\]\]

Copy to clipboard

Equivalently, eliminating the inner loop, the last two lines would be:

out\_1d\[:\] \= a\_1d\[indices\_1d\]

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

For this sample array

\>>> a \= np.array(\[\[10, 30, 20\], \[60, 40, 50\]\])

Copy to clipboard

We can sort either by using sort directly, or argsort and this function

\>>> np.sort(a, axis\=1)
array(\[\[10, 20, 30\],\
       \[40, 50, 60\]\])
\>>> ai \= np.argsort(a, axis\=1)
\>>> ai
array(\[\[0, 2, 1\],\
       \[1, 2, 0\]\])
\>>> np.take\_along\_axis(a, ai, axis\=1)
array(\[\[10, 20, 30\],\
       \[40, 50, 60\]\])

Copy to clipboard

The same works for max and min, if you maintain the trivial dimension with `keepdims`:

\>>> np.max(a, axis\=1, keepdims\=True)
array(\[\[30\],\
       \[60\]\])
\>>> ai \= np.argmax(a, axis\=1, keepdims\=True)
\>>> ai
array(\[\[1\],\
       \[0\]\])
\>>> np.take\_along\_axis(a, ai, axis\=1)
array(\[\[30\],\
       \[60\]\])

Copy to clipboard

If we want to get the max and min at the same time, we can stack the indices first

\>>> ai\_min \= np.argmin(a, axis\=1, keepdims\=True)
\>>> ai\_max \= np.argmax(a, axis\=1, keepdims\=True)
\>>> ai \= np.concatenate(\[ai\_min, ai\_max\], axis\=1)
\>>> ai
array(\[\[0, 1\],\
       \[1, 0\]\])
\>>> np.take\_along\_axis(a, ai, axis\=1)
array(\[\[10, 30\],\
       \[40, 60\]\])

Copy to clipboard

Go BackOpen In Tab

On this page