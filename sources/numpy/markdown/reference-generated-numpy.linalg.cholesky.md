[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.cholesky.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.cholesky.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.cholesky.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.cholesky.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.cholesky.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.cholesky.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.cholesky.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.cholesky.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.cholesky.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.cholesky.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.cholesky.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.cholesky.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.cholesky.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.cholesky.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.cholesky.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.cholesky.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.cholesky.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.cholesky.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.cholesky.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.cholesky.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.cholesky[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html#numpy-linalg-cholesky "Link to this heading")

===================================================================================================================================================

linalg.cholesky(_a_, _/_, _\*_, _upper\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L789-L888)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html#numpy.linalg.cholesky "Link to this definition")

Cholesky decomposition.

Return the lower or upper Cholesky decomposition, `L * L.H` or `U.H * U`, of the square matrix `a`, where `L` is lower-triangular, `U` is upper-triangular, and `.H` is the conjugate transpose operator (which is the ordinary transpose if `a` is real-valued). `a` must be Hermitian (symmetric if real-valued) and positive-definite. No checking is performed to verify whether `a` is Hermitian or not. In addition, only the lower or upper-triangular and diagonal elements of `a` are used. Only `L` or `U` is actually returned.

Parameters:

**a**(…, M, M) array\_like

Hermitian (symmetric if all elements are real), positive-definite input matrix.

**upper**bool

If `True`, the result must be the upper-triangular Cholesky factor. If `False`, the result must be the lower-triangular Cholesky factor. Default: `False`.

Returns:

**L**(…, M, M) array\_like

Lower or upper-triangular Cholesky factor of _a_. Returns a matrix object if _a_ is a matrix object.

Raises:

LinAlgError

If the decomposition fails, for example, if _a_ is not positive-definite.

See also

[`scipy.linalg.cholesky`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky.html#scipy.linalg.cholesky "(in SciPy v1.18.0)")

Similar function in SciPy.

[`scipy.linalg.cholesky_banded`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky_banded.html#scipy.linalg.cholesky_banded "(in SciPy v1.18.0)")

Cholesky decompose a banded Hermitian positive-definite matrix.

[`scipy.linalg.cho_factor`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_factor.html#scipy.linalg.cho_factor "(in SciPy v1.18.0)")

Cholesky decomposition of a matrix, to use in [`scipy.linalg.cho_solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cho_solve.html#scipy.linalg.cho_solve "(in SciPy v1.18.0)")
.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

The Cholesky decomposition is often used as a fast way of solving

\\\[A \\mathbf{x} = \\mathbf{b}\\\]

(when _A_ is both Hermitian/symmetric and positive-definite).

First, we solve for \\(\\mathbf{y}\\) in

\\\[L \\mathbf{y} = \\mathbf{b},\\\]

and then for \\(\\mathbf{x}\\) in

\\\[L^{H} \\mathbf{x} = \\mathbf{y}.\\\]

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.array(\[\[1,\-2j\],\[2j,5\]\])
\>>> A
array(\[\[ 1.+0.j, -0.-2.j\],\
       \[ 0.+2.j,  5.+0.j\]\])
\>>> L \= np.linalg.cholesky(A)
\>>> L
array(\[\[1.+0.j, 0.+0.j\],\
       \[0.+2.j, 1.+0.j\]\])
\>>> np.dot(L, L.T.conj()) \# verify that L \* L.H = A
array(\[\[1.+0.j, 0.-2.j\],\
       \[0.+2.j, 5.+0.j\]\])
\>>> A \= \[\[1,\-2j\],\[2j,5\]\] \# what happens if A is only array\_like?
\>>> np.linalg.cholesky(A) \# an ndarray object is returned
array(\[\[1.+0.j, 0.+0.j\],\
       \[0.+2.j, 1.+0.j\]\])
\>>> \# But a matrix object is returned if A is a matrix object
\>>> np.linalg.cholesky(np.matrix(A))
matrix(\[\[ 1.+0.j,  0.+0.j\],\
        \[ 0.+2.j,  1.+0.j\]\])
\>>> \# The upper-triangular Cholesky factor can also be obtained.
\>>> np.linalg.cholesky(A, upper\=True)
array(\[\[1.-0.j, 0.-2.j\],\
       \[0.-0.j, 1.-0.j\]\])

Copy to clipboard

Go BackOpen In Tab

On this page