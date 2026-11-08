[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.eig.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.eig.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.eig.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.eig.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eig.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.eig.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.eig.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.eig.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.eig.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.eig.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.eig.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.eig.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.eig.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.eig.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.eig.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.eig.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.eig.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.eig.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.eig.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.eig[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy-linalg-eig "Link to this heading")

====================================================================================================================================

linalg.eig(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1366-L1510)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "Link to this definition")

Compute the eigenvalues and right eigenvectors of a square array.

Parameters:

**a**(…, M, M) array

Matrices for which the eigenvalues and right eigenvectors will be computed

Returns:

A namedtuple with the following attributes:

**eigenvalues**(…, M) array

The eigenvalues, each repeated according to its multiplicity. The eigenvalues are not necessarily ordered. The resulting array will be of complex type, unless the imaginary part is zero in which case it will be cast to a real type. When _a_ is real the resulting eigenvalues will be real (0 imaginary part) or occur in conjugate pairs

**eigenvectors**(…, M, M) array

The normalized (unit “length”) eigenvectors, such that the column `eigenvectors[:,i]` is the eigenvector corresponding to the eigenvalue `eigenvalues[i]`.

Raises:

LinAlgError

If the eigenvalue computation does not converge.

See also

[`eigvals`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "numpy.linalg.eigvals")

eigenvalues of a non-symmetric array.

[`eigh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")

eigenvalues and eigenvectors of a real symmetric or complex Hermitian (conjugate symmetric) array.

[`eigvalsh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "numpy.linalg.eigvalsh")

eigenvalues of a real symmetric or complex Hermitian (conjugate symmetric) array.

[`scipy.linalg.eig`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig.html#scipy.linalg.eig "(in SciPy v1.18.0)")

Similar function in SciPy that also solves the generalized eigenvalue problem.

[`scipy.linalg.schur`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.schur.html#scipy.linalg.schur "(in SciPy v1.18.0)")

Best choice for unitary and other non-Hermitian normal matrices.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

This is implemented using the `_geev` LAPACK routines which compute the eigenvalues and eigenvectors of general square arrays.

The number _w_ is an eigenvalue of _a_ if there exists a vector _v_ such that `a @ v = w * v`. Thus, the arrays _a_, _eigenvalues_, and _eigenvectors_ satisfy the equations `a @ eigenvectors[:,i] = eigenvalues[i] * eigenvectors[:,i]` for \\(i \\in \\{0,...,M-1\\}\\).

The array _eigenvectors_ may not be of maximum rank, that is, some of the columns may be linearly dependent, although round-off error may obscure that fact. If the eigenvalues are all different, then theoretically the eigenvectors are linearly independent and _a_ can be diagonalized by a similarity transformation using _eigenvectors_, i.e, `inv(eigenvectors) @ a @ eigenvectors` is diagonal.

For non-Hermitian normal matrices the SciPy function [`scipy.linalg.schur`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.schur.html#scipy.linalg.schur "(in SciPy v1.18.0)")
 is preferred because the matrix _eigenvectors_ is guaranteed to be unitary, which is not the case when using [`eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "numpy.linalg.eig")
. The Schur factorization produces an upper triangular matrix rather than a diagonal matrix, but for normal matrices only the diagonal of the upper triangular matrix is needed, the rest is roundoff error.

Finally, it is emphasized that _eigenvectors_ consists of the _right_ (as in right-hand side) eigenvectors of _a_. A vector _y_ satisfying `y.T @ a = z * y.T` for some number _z_ is called a _left_ eigenvector of _a_, and, in general, the left and right eigenvectors of a matrix are not necessarily the (perhaps conjugate) transposes of each other.

References

G. Strang, _Linear Algebra and Its Applications_, 2nd Ed., Orlando, FL, Academic Press, Inc., 1980, Various pp.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy import linalg as LA

Copy to clipboard

(Almost) trivial example with real eigenvalues and eigenvectors.

\>>> eigenvalues, eigenvectors \= LA.eig(np.diag((1, 2, 3)))
\>>> eigenvalues
array(\[1. + 0j, 2. + 0j, 3. + 0j\])
\>>> eigenvectors.real
array(\[\[1., 0., 0.\],\
       \[0., 1., 0.\],\
       \[0., 0., 1.\]\])

Copy to clipboard

Real matrix possessing complex eigenvalues and eigenvectors; note that the eigenvalues are complex conjugates of each other.

\>>> eigenvalues, eigenvectors \= LA.eig(np.array(\[\[1, \-1\], \[1, 1\]\]))
\>>> eigenvalues
array(\[1.+1.j, 1.-1.j\])
\>>> eigenvectors
array(\[\[0.70710678+0.j        , 0.70710678-0.j        \],\
       \[0.        -0.70710678j, 0.        +0.70710678j\]\])

Copy to clipboard

Complex-valued matrix with real eigenvalues (but complex-valued eigenvectors); note that `a.conj().T == a`, i.e., _a_ is Hermitian.

\>>> a \= np.array(\[\[1, 1j\], \[\-1j, 1\]\])
\>>> eigenvalues, eigenvectors \= LA.eig(a)
\>>> eigenvalues
array(\[2.+0.j, 0.+0.j\])
\>>> eigenvectors
array(\[\[ 0.        +0.70710678j,  0.70710678+0.j        \], # may vary\
       \[ 0.70710678+0.j        , -0.        +0.70710678j\]\])

Copy to clipboard

Be careful about round-off error!

\>>> a \= np.array(\[\[1 + 1e-9, 0\], \[0, 1 \- 1e-9\]\])
\>>> \# Theor. eigenvalues are 1 +/- 1e-9
\>>> eigenvalues, eigenvectors \= LA.eig(a)
\>>> eigenvalues
array(\[1.+0j, 1.+0j\])
\>>> eigenvectors.real
array(\[\[1., 0.\],\
       \[0., 1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page