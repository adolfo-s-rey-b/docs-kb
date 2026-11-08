[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.trace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.trace[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.trace.html#numpy-linalg-trace "Link to this heading")

==========================================================================================================================================

linalg.trace(_x_, _/_, _\*_, _offset\=0_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3161-L3237)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.trace.html#numpy.linalg.trace "Link to this definition")

Returns the sum along the specified diagonals of a matrix (or a stack of matrices) `x`.

This function is Array API compatible, contrary to [`numpy.trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")
.

Parameters:

**x**(…,M,N) array\_like

Input array having shape (…, M, N) and whose innermost two dimensions form MxN matrices.

**offset**int, optional

Offset specifying the off-diagonal relative to the main diagonal, where:

\* offset \= 0: the main diagonal.
\* offset \> 0: off\-diagonal above the main diagonal.
\* offset < 0: off\-diagonal below the main diagonal.

Copy to clipboard

**dtype**dtype, optional

Data type of the returned array.

Returns:

**out**ndarray

An array containing the traces and whose shape is determined by removing the last two dimensions and storing the traces in the last array dimension. For example, if x has rank k and shape: (I, J, K, …, L, M, N), then an output array has rank k-2 and shape: (I, J, K, …, L) where:

out\[i, j, k, ..., l\] \= trace(a\[i, j, k, ..., l, :, :\])

Copy to clipboard

The returned array must have a data type as described by the dtype parameter above.

See also

[`numpy.trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")

Examples

Try it in your browser!

\>>> np.linalg.trace(np.eye(3))
3.0
\>>> a \= np.arange(8).reshape((2, 2, 2))
\>>> np.linalg.trace(a)
array(\[3, 11\])

Copy to clipboard

Trace is computed with the last two axes as the 2-d sub-arrays. This behavior differs from [`numpy.trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")
 which uses the first two axes by default.

\>>> a \= np.arange(24).reshape((3, 2, 2, 2))
\>>> np.linalg.trace(a).shape
(3, 2)

Copy to clipboard

Traces adjacent to the main diagonal can be obtained by using the _offset_ argument:

\>>> a \= np.arange(9).reshape((3, 3)); a
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> np.linalg.trace(a, offset\=1)  \# First superdiagonal
6
\>>> np.linalg.trace(a, offset\=2)  \# Second superdiagonal
2
\>>> np.linalg.trace(a, offset\=-1)  \# First subdiagonal
10
\>>> np.linalg.trace(a, offset\=-2)  \# Second subdiagonal
6

Copy to clipboard

Go BackOpen In Tab

On this page