[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.svd[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#numpy-linalg-svd "Link to this heading")

====================================================================================================================================

linalg.svd(_a_, _full\_matrices\=True_, _compute\_uv\=True_, _hermitian\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1666-L1852)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd "Link to this definition")

Singular Value Decomposition.

When _a_ is a 2D array, and `full_matrices=False`, then it is factorized as `u @ np.diag(s) @ vh = (u * s) @ vh`, where _u_ and the Hermitian transpose of _vh_ are 2D arrays with orthonormal columns and _s_ is a 1D array of _a_’s singular values. When _a_ is higher-dimensional, SVD is applied in stacked mode as explained below.

Parameters:

**a**(…, M, N) array\_like

A real or complex array with `a.ndim >= 2`.

**full\_matrices**bool, optional

If True (default), _u_ and _vh_ have the shapes `(..., M, M)` and `(..., N, N)`, respectively. Otherwise, the shapes are `(..., M, K)` and `(..., K, N)`, respectively, where `K = min(M, N)`.

**compute\_uv**bool, optional

Whether or not to compute _u_ and _vh_ in addition to _s_. True by default.

**hermitian**bool, optional

If True, _a_ is assumed to be Hermitian (symmetric if real-valued), enabling a more efficient method for finding singular values. Defaults to False.

Returns:

**U**{ (…, M, M), (…, M, K) } array

Unitary array(s). The first `a.ndim - 2` dimensions have the same size as those of the input _a_. The size of the last two dimensions depends on the value of _full\_matrices_. Only returned when _compute\_uv_ is True.

**S**(…, K) array

Vector(s) with the singular values, within each vector sorted in descending order. The first `a.ndim - 2` dimensions have the same size as those of the input _a_.

**Vh**{ (…, N, N), (…, K, N) } array

Unitary array(s). The first `a.ndim - 2` dimensions have the same size as those of the input _a_. The size of the last two dimensions depends on the value of _full\_matrices_. Only returned when _compute\_uv_ is True.

Raises:

LinAlgError

If SVD computation does not converge.

See also

[`scipy.linalg.svd`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html#scipy.linalg.svd "(in SciPy v1.18.0)")

Similar function in SciPy.

[`scipy.linalg.svdvals`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svdvals.html#scipy.linalg.svdvals "(in SciPy v1.18.0)")

Compute singular values of a matrix.

Notes

When _compute\_uv_ is True, the result is a namedtuple with the following attribute names: _U_, _S_, and _Vh_.

The decomposition is performed using LAPACK routine `_gesdd`.

SVD is usually described for the factorization of a 2D matrix \\(A\\). The higher-dimensional case will be discussed below. In the 2D case, SVD is written as \\(A = U S V^H\\), where \\(A = a\\), \\(U= u\\), \\(S= \\mathtt{np.diag}(s)\\) and \\(V^H = vh\\). The 1D array _s_ contains the singular values of _a_ and _u_ and _vh_ are unitary. The rows of _vh_ are the eigenvectors of \\(A^H A\\) and the columns of _u_ are the eigenvectors of \\(A A^H\\). In both cases the corresponding (possibly non-zero) eigenvalues are given by `s**2`.

If _a_ has more than two dimensions, then broadcasting rules apply, as explained in [Linear algebra on several matrices at once](https://numpy.org/doc/stable/reference/routines.linalg.html#routines-linalg-broadcasting)
. This means that SVD is working in “stacked” mode: it iterates over all indices of the first `a.ndim - 2` dimensions and for each combination SVD is applied to the last two indices. The matrix _a_ can be reconstructed from the decomposition with either `(u * s[..., None, :]) @ vh` or `u @ (s[..., None] * vh)`. (The `@` operator can be replaced by the function `np.matmul` for python versions below 3.5.)

If _a_ is a `matrix` object (as opposed to an `ndarray`), then so are all the return values.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> rng \= np.random.default\_rng()
\>>> a \= rng.normal(size\=(9, 6)) + 1j\*rng.normal(size\=(9, 6))
\>>> b \= rng.normal(size\=(2, 7, 8, 3)) + 1j\*rng.normal(size\=(2, 7, 8, 3))

Copy to clipboard

Reconstruction based on full SVD, 2D case:

\>>> U, S, Vh \= np.linalg.svd(a, full\_matrices\=True)
\>>> U.shape, S.shape, Vh.shape
((9, 9), (6,), (6, 6))
\>>> np.allclose(a, np.dot(U\[:, :6\] \* S, Vh))
True
\>>> smat \= np.zeros((9, 6), dtype\=np.complex128)
\>>> smat\[:6, :6\] \= np.diag(S)
\>>> np.allclose(a, np.dot(U, np.dot(smat, Vh)))
True

Copy to clipboard

Reconstruction based on reduced SVD, 2D case:

\>>> U, S, Vh \= np.linalg.svd(a, full\_matrices\=False)
\>>> U.shape, S.shape, Vh.shape
((9, 6), (6,), (6, 6))
\>>> np.allclose(a, np.dot(U \* S, Vh))
True
\>>> smat \= np.diag(S)
\>>> np.allclose(a, np.dot(U, np.dot(smat, Vh)))
True

Copy to clipboard

Reconstruction based on full SVD, 4D case:

\>>> U, S, Vh \= np.linalg.svd(b, full\_matrices\=True)
\>>> U.shape, S.shape, Vh.shape
((2, 7, 8, 8), (2, 7, 3), (2, 7, 3, 3))
\>>> np.allclose(b, np.matmul(U\[..., :3\] \* S\[..., None, :\], Vh))
True
\>>> np.allclose(b, np.matmul(U\[..., :3\], S\[..., None\] \* Vh))
True

Copy to clipboard

Reconstruction based on reduced SVD, 4D case:

\>>> U, S, Vh \= np.linalg.svd(b, full\_matrices\=False)
\>>> U.shape, S.shape, Vh.shape
((2, 7, 8, 3), (2, 7, 3), (2, 7, 3, 3))
\>>> np.allclose(b, np.matmul(U \* S\[..., None, :\], Vh))
True
\>>> np.allclose(b, np.matmul(U, S\[..., None\] \* Vh))
True

Copy to clipboard

Go BackOpen In Tab

On this page