[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.diagonal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.diagonal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.diagonal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.diagonal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.diagonal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.diagonal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.diagonal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.diagonal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.diagonal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.diagonal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.diagonal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.diagonal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.diagonal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.diagonal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.diagonal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.diagonal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.diagonal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.diagonal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.diagonal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.diagonal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.diagonal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.diagonal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.diagonal[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.diagonal.html#numpy-linalg-diagonal "Link to this heading")

===================================================================================================================================================

linalg.diagonal(_x_, _/_, _\*_, _offset\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3065-L3152)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.diagonal.html#numpy.linalg.diagonal "Link to this definition")

Returns specified diagonals of a matrix (or a stack of matrices) `x`.

This function is Array API compatible, contrary to [`numpy.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")
, the matrix is assumed to be defined by the last two dimensions.

Parameters:

**x**(…,M,N) array\_like

Input array having shape (…, M, N) and whose innermost two dimensions form MxN matrices.

**offset**int, optional

Offset specifying the off-diagonal relative to the main diagonal, where:

\* offset \= 0: the main diagonal.
\* offset \> 0: off\-diagonal above the main diagonal.
\* offset < 0: off\-diagonal below the main diagonal.

Copy to clipboard

Returns:

**out**(…,min(N,M)) ndarray

An array containing the diagonals and whose shape is determined by removing the last two dimensions and appending a dimension equal to the size of the resulting diagonals. The returned array must have the same data type as `x`.

See also

[`numpy.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")

Examples

Try it in your browser!

\>>> a \= np.arange(4).reshape(2, 2); a
array(\[\[0, 1\],\
       \[2, 3\]\])
\>>> np.linalg.diagonal(a)
array(\[0, 3\])

Copy to clipboard

A 3-D example:

\>>> a \= np.arange(8).reshape(2, 2, 2); a
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> np.linalg.diagonal(a)
array(\[\[0, 3\],\
       \[4, 7\]\])

Copy to clipboard

Diagonals adjacent to the main diagonal can be obtained by using the _offset_ argument:

\>>> a \= np.arange(9).reshape(3, 3)
\>>> a
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> np.linalg.diagonal(a, offset\=1)  \# First superdiagonal
array(\[1, 5\])
\>>> np.linalg.diagonal(a, offset\=2)  \# Second superdiagonal
array(\[2\])
\>>> np.linalg.diagonal(a, offset\=-1)  \# First subdiagonal
array(\[3, 7\])
\>>> np.linalg.diagonal(a, offset\=-2)  \# Second subdiagonal
array(\[6\])

Copy to clipboard

The anti-diagonal can be obtained by reversing the order of elements using either [`numpy.flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")
 or [`numpy.fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")
.

\>>> a \= np.arange(9).reshape(3, 3)
\>>> a
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> np.linalg.diagonal(np.fliplr(a))  \# Horizontal flip
array(\[2, 4, 6\])
\>>> np.linalg.diagonal(np.flipud(a))  \# Vertical flip
array(\[6, 4, 2\])

Copy to clipboard

Note that the order in which the diagonal is retrieved varies depending on the flip function.

Go BackOpen In Tab

On this page