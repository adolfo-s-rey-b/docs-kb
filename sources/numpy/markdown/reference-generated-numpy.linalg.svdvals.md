[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svdvals.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.svdvals.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svdvals.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.svdvals.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.svdvals.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.svdvals.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.svdvals.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.svdvals.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.svdvals.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.svdvals.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.svdvals.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.svdvals.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.svdvals.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.svdvals.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.svdvals.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.svdvals.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.svdvals.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.svdvals.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.svdvals.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.svdvals.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.svdvals.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.svdvals.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.svdvals[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svdvals.html#numpy-linalg-svdvals "Link to this heading")

================================================================================================================================================

linalg.svdvals(_x_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1859-L1906)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svdvals.html#numpy.linalg.svdvals "Link to this definition")

Returns the singular values of a matrix (or a stack of matrices) `x`. When x is a stack of matrices, the function will compute the singular values for each matrix in the stack.

This function is Array API compatible.

Calling `np.svdvals(x)` to get singular values is the same as `np.svd(x, compute_uv=False, hermitian=False)`.

Parameters:

**x**(…, M, N) array\_like

Input array having shape (…, M, N) and whose last two dimensions form matrices on which to perform singular value decomposition. Should have a floating-point data type.

Returns:

**out**ndarray

An array with shape (…, K) that contains the vector(s) of singular values of length K, where K = min(M, N).

See also

[`scipy.linalg.svdvals`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svdvals.html#scipy.linalg.svdvals "(in SciPy v1.18.0)")

Compute singular values of a matrix.

Examples

Try it in your browser!

\>>> np.linalg.svdvals(\[\[1, 2, 3, 4, 5\],\
...                    \[1, 4, 9, 16, 25\],\
...                    \[1, 8, 27, 64, 125\]\])
array(\[146.68862757,   5.57510612,   0.60393245\])

Copy to clipboard

Determine the rank of a matrix using singular values:

\>>> s \= np.linalg.svdvals(\[\[1, 2, 3\],\
...                        \[2, 4, 6\],\
...                        \[\-1, 1, \-1\]\]); s
array(\[8.38434191e+00, 1.64402274e+00, 2.31534378e-16\])
\>>> np.count\_nonzero(s \> 1e-10)  \# Matrix of rank 2
2

Copy to clipboard

Go BackOpen In Tab

On this page