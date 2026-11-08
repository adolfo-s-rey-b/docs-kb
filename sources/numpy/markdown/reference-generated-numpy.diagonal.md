[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.diagonal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.diagonal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.diagonal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.diagonal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.diagonal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.diagonal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.diagonal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.diagonal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.diagonal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.diagonal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.diagonal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.diagonal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.diagonal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.diagonal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.diagonal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.diagonal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.diagonal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.diagonal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.diagonal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.diagonal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.diagonal[#](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy-diagonal "Link to this heading")

==============================================================================================================================

numpy.diagonal(_a_, _offset\=0_, _axis1\=0_, _axis2\=1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1708-L1836)
[#](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "Link to this definition")

Return specified diagonals.

If _a_ is 2-D, returns the diagonal of _a_ with the given offset, i.e., the collection of elements of the form `a[i, i+offset]`. If _a_ has more than two dimensions, then the axes specified by _axis1_ and _axis2_ are used to determine the 2-D sub-array whose diagonal is returned. The shape of the resulting array can be determined by removing _axis1_ and _axis2_ and appending an index to the right equal to the size of the resulting diagonals.

In versions of NumPy prior to 1.7, this function always returned a new, independent array containing a copy of the values in the diagonal.

In NumPy 1.7 and 1.8, it continues to return a copy of the diagonal, but depending on this fact is deprecated. Writing to the resulting array continues to work as it used to, but a FutureWarning is issued.

Starting in NumPy 1.9 it returns a read-only view on the original array. Attempting to write to the resulting array will produce an error.

In some future release, it will return a read/write view and writing to the returned array will alter your original array. The returned array will have the same type as the input array.

If you don’t write to the array returned by this function, then you can just ignore all of the above.

If you depend on the current behavior, then we suggest copying the returned array explicitly, i.e., use `np.diagonal(a).copy()` instead of just `np.diagonal(a)`. This will work with both past and future versions of NumPy.

Parameters:

**a**array\_like

Array from which the diagonals are taken.

**offset**int, optional

Offset of the diagonal from the main diagonal. Can be positive or negative. Defaults to main diagonal (0).

**axis1**int, optional

Axis to be used as the first axis of the 2-D sub-arrays from which the diagonals should be taken. Defaults to first axis (0).

**axis2**int, optional

Axis to be used as the second axis of the 2-D sub-arrays from which the diagonals should be taken. Defaults to second axis (1).

Returns:

**array\_of\_diagonals**ndarray

If _a_ is 2-D, then a 1-D array containing the diagonal and of the same type as _a_ is returned unless _a_ is a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
, in which case a 1-D array rather than a (2-D) [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 is returned in order to maintain backward compatibility.

If `a.ndim > 2`, then the dimensions specified by _axis1_ and _axis2_ are removed, and a new axis inserted at the end corresponding to the diagonal.

Raises:

ValueError

If the dimension of _a_ is less than 2.

See also

[`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")

MATLAB work-a-like for 1-D and 2-D arrays.

[`diagflat`](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy.diagflat "numpy.diagflat")

Create diagonal arrays.

[`trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")

Sum along diagonals.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(4).reshape(2,2)
\>>> a
array(\[\[0, 1\],\
       \[2, 3\]\])
\>>> a.diagonal()
array(\[0, 3\])
\>>> a.diagonal(1)
array(\[1\])

Copy to clipboard

A 3-D example:

\>>> a \= np.arange(8).reshape(2,2,2); a
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> a.diagonal(0,  \# Main diagonals of two arrays created by skipping
...            0,  \# across the outer(left)-most axis last and
...            1)  \# the "middle" (row) axis first.
array(\[\[0, 6\],\
       \[1, 7\]\])

Copy to clipboard

The sub-arrays whose main diagonals we just obtained; note that each corresponds to fixing the right-most (column) axis, and that the diagonals are “packed” in rows.

\>>> a\[:,:,0\]  \# main diagonal is \[0 6\]
array(\[\[0, 2\],\
       \[4, 6\]\])
\>>> a\[:,:,1\]  \# main diagonal is \[1 7\]
array(\[\[1, 3\],\
       \[5, 7\]\])

Copy to clipboard

The anti-diagonal can be obtained by reversing the order of elements using either [`numpy.flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")
 or [`numpy.fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")
.

\>>> a \= np.arange(9).reshape(3, 3)
\>>> a
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> np.fliplr(a).diagonal()  \# Horizontal flip
array(\[2, 4, 6\])
\>>> np.flipud(a).diagonal()  \# Vertical flip
array(\[6, 4, 2\])

Copy to clipboard

Note that the order in which the diagonal is retrieved varies depending on the flip function.

Go BackOpen In Tab

On this page