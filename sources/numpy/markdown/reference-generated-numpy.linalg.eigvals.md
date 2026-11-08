[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.eigvals.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.eigvals.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.eigvals.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.eigvals.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eigvals.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigvals.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.eigvals.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.eigvals.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.eigvals.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.eigvals.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.eigvals.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.eigvals.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.eigvals.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.eigvals.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.eigvals.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.eigvals.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.eigvals.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.eigvals.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.eigvals.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.eigvals.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.eigvals[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy-linalg-eigvals "Link to this heading")

================================================================================================================================================

linalg.eigvals(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1181-L1262)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "Link to this definition")

Compute the eigenvalues of a general matrix.

Main difference between [`eigvals`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "numpy.linalg.eigvals")
 and [`eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "numpy.linalg.eig")
: the eigenvectors aren’t returned.

Parameters:

**a**(…, M, M) array\_like

A complex- or real-valued matrix whose eigenvalues will be computed.

Returns:

**w**(…, M,) ndarray

The eigenvalues, each repeated according to its multiplicity. They are not necessarily ordered, nor are they necessarily real for real matrices.

Raises:

LinAlgError

If the eigenvalue computation does not converge.

See also

[`eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "numpy.linalg.eig")

eigenvalues and right eigenvectors of general arrays

[`eigvalsh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "numpy.linalg.eigvalsh")

eigenvalues of real symmetric or complex Hermitian (conjugate symmetric) arrays.

[`eigh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")

eigenvalues and eigenvectors of real symmetric or complex Hermitian (conjugate symmetric) arrays.

[`scipy.linalg.eigvals`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvals.html#scipy.linalg.eigvals "(in SciPy v1.18.0)")

Similar function in SciPy.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

This is implemented using the `_geev` LAPACK routines which compute the eigenvalues and eigenvectors of general square arrays.

Examples

Try it in your browser!

Illustration, using the fact that the eigenvalues of a diagonal matrix are its diagonal elements, that multiplying a matrix on the left by an orthogonal matrix, _Q_, and on the right by _Q.T_ (the transpose of _Q_), preserves the eigenvalues of the “middle” matrix. In other words, if _Q_ is orthogonal, then `Q * A * Q.T` has the same eigenvalues as `A`:

\>>> import numpy as np
\>>> from numpy import linalg as LA
\>>> x \= np.random.random()
\>>> Q \= np.array(\[\[np.cos(x), \-np.sin(x)\], \[np.sin(x), np.cos(x)\]\])
\>>> LA.norm(Q\[0, :\]), LA.norm(Q\[1, :\]), np.dot(Q\[0, :\],Q\[1, :\])
(1.0, 1.0, 0.0)

Copy to clipboard

Now multiply a diagonal matrix by `Q` on one side and by `Q.T` on the other:

\>>> D \= np.diag((\-1,1))
\>>> LA.eigvals(D)
array(\[-1. + 0.j,  1. + 0.j\])
\>>> A \= np.dot(Q, D)
\>>> A \= np.dot(A, Q.T)
\>>> LA.eigvals(A)
array(\[ 1., -1.\])  # random

Copy to clipboard

Go BackOpen In Tab

On this page