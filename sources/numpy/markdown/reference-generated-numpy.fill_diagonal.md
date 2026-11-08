[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fill_diagonal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fill_diagonal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fill_diagonal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fill_diagonal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fill_diagonal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fill_diagonal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fill_diagonal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fill_diagonal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fill_diagonal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fill_diagonal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fill_diagonal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fill_diagonal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fill_diagonal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fill_diagonal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fill_diagonal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fill_diagonal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fill_diagonal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fill_diagonal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fill_diagonal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fill_diagonal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fill\_diagonal[#](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#numpy-fill-diagonal "Link to this heading")

==============================================================================================================================================

numpy.fill\_diagonal(_a_, _val_, _wrap\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_index_tricks_impl.py#L794-L923)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#numpy.fill_diagonal "Link to this definition")

Fill the main diagonal of the given array of any dimensionality.

For an array _a_ with `a.ndim >= 2`, the diagonal is the list of values `a[i, ..., i]` with indices `i` all identical. This function modifies the input array in-place without returning a value.

Parameters:

**a**array, at least 2-D.

Array whose diagonal is to be filled in-place.

**val**scalar or array\_like

Value(s) to write on the diagonal. If _val_ is scalar, the value is written along the diagonal. If array-like, the flattened _val_ is written along the diagonal, repeating if necessary to fill all diagonal entries.

**wrap**bool

For tall matrices in NumPy version up to 1.6.2, the diagonal “wrapped” after N columns. You can have this behavior with this option. This affects only tall matrices.

See also

[`diag_indices`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy.diag_indices "numpy.diag_indices")
, [`diag_indices_from`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html#numpy.diag_indices_from "numpy.diag_indices_from")

Notes

This functionality can be obtained via [`diag_indices`](https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html#numpy.diag_indices "numpy.diag_indices")
, but internally this version uses a much faster implementation that never constructs the indices and uses simple slicing.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.zeros((3, 3), int)
\>>> np.fill\_diagonal(a, 5)
\>>> a
array(\[\[5, 0, 0\],\
       \[0, 5, 0\],\
       \[0, 0, 5\]\])

Copy to clipboard

The same function can operate on a 4-D array:

\>>> a \= np.zeros((3, 3, 3, 3), int)
\>>> np.fill\_diagonal(a, 4)

Copy to clipboard

We only show a few blocks for clarity:

\>>> a\[0, 0\]
array(\[\[4, 0, 0\],\
       \[0, 0, 0\],\
       \[0, 0, 0\]\])
\>>> a\[1, 1\]
array(\[\[0, 0, 0\],\
       \[0, 4, 0\],\
       \[0, 0, 0\]\])
\>>> a\[2, 2\]
array(\[\[0, 0, 0\],\
       \[0, 0, 0\],\
       \[0, 0, 4\]\])

Copy to clipboard

The wrap option affects only tall matrices:

\>>> \# tall matrices no wrap
\>>> a \= np.zeros((5, 3), int)
\>>> np.fill\_diagonal(a, 4)
\>>> a
array(\[\[4, 0, 0\],\
       \[0, 4, 0\],\
       \[0, 0, 4\],\
       \[0, 0, 0\],\
       \[0, 0, 0\]\])

Copy to clipboard

\>>> \# tall matrices wrap
\>>> a \= np.zeros((5, 3), int)
\>>> np.fill\_diagonal(a, 4, wrap\=True)
\>>> a
array(\[\[4, 0, 0\],\
       \[0, 4, 0\],\
       \[0, 0, 4\],\
       \[0, 0, 0\],\
       \[4, 0, 0\]\])

Copy to clipboard

\>>> \# wide matrices
\>>> a \= np.zeros((3, 5), int)
\>>> np.fill\_diagonal(a, 4, wrap\=True)
\>>> a
array(\[\[4, 0, 0, 0, 0\],\
       \[0, 4, 0, 0, 0\],\
       \[0, 0, 4, 0, 0\]\])

Copy to clipboard

The anti-diagonal can be filled by reversing the order of elements using either [`numpy.flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")
 or [`numpy.fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")
.

\>>> a \= np.zeros((3, 3), int);
\>>> np.fill\_diagonal(np.fliplr(a), \[1,2,3\])  \# Horizontal flip
\>>> a
array(\[\[0, 0, 1\],\
       \[0, 2, 0\],\
       \[3, 0, 0\]\])
\>>> np.fill\_diagonal(np.flipud(a), \[1,2,3\])  \# Vertical flip
\>>> a
array(\[\[0, 0, 3\],\
       \[0, 2, 0\],\
       \[1, 0, 0\]\])

Copy to clipboard

Note that the order in which the diagonal is filled varies depending on the flip function.

Go BackOpen In Tab

On this page