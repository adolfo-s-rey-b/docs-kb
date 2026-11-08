[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.eigh.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.eigh.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.eigh.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.eigh.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eigh.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.eigh.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.eigh.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.eigh.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.eigh.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.eigh.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.eigh.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.eigh.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.eigh.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.eigh.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.eigh.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.eigh.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.eigh.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.eigh.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.eigh.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.eigh[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy-linalg-eigh "Link to this heading")

=======================================================================================================================================

linalg.eigh(_a_, _UPLO\='L'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1513-L1657)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "Link to this definition")

Return the eigenvalues and eigenvectors of a complex Hermitian (conjugate symmetric) or a real symmetric matrix.

Returns two objects, a 1-D array containing the eigenvalues of _a_, and a 2-D square array or matrix (depending on the input type) of the corresponding eigenvectors (in columns).

Parameters:

**a**(…, M, M) array

Hermitian or real symmetric matrices whose eigenvalues and eigenvectors are to be computed.

**UPLO**{‘L’, ‘U’}, optional

Specifies whether the calculation is done with the lower triangular part of _a_ (‘L’, default) or the upper triangular part (‘U’). Irrespective of this value only the real parts of the diagonal will be considered in the computation to preserve the notion of a Hermitian matrix. It therefore follows that the imaginary part of the diagonal will always be treated as zero.

Returns:

A namedtuple with the following attributes:

**eigenvalues**(…, M) ndarray

The eigenvalues in ascending order, each repeated according to its multiplicity.

**eigenvectors**{(…, M, M) ndarray, (…, M, M) matrix}

The column `eigenvectors[:, i]` is the normalized eigenvector corresponding to the eigenvalue `eigenvalues[i]`. Will return a matrix object if _a_ is a matrix object.

Raises:

LinAlgError

If the eigenvalue computation does not converge.

See also

[`eigvalsh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "numpy.linalg.eigvalsh")

eigenvalues of real symmetric or complex Hermitian (conjugate symmetric) arrays.

[`eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "numpy.linalg.eig")

eigenvalues and right eigenvectors for non-symmetric arrays.

[`eigvals`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "numpy.linalg.eigvals")

eigenvalues of non-symmetric arrays.

[`scipy.linalg.eigh`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html#scipy.linalg.eigh "(in SciPy v1.18.0)")

Similar function in SciPy (but also solves the generalized eigenvalue problem).

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

The eigenvalues/eigenvectors are computed using LAPACK routines `_syevd`, `_heevd`.

The eigenvalues of real symmetric or complex Hermitian matrices are always real. [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#rc702e98a756a-1)
 The array _eigenvalues_ of (column) eigenvectors is unitary and _a_, _eigenvalues_, and _eigenvectors_ satisfy the equations `dot(a, eigenvectors[:, i]) = eigenvalues[i] * eigenvectors[:, i]`.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#id1)\
\]

G. Strang, _Linear Algebra and Its Applications_, 2nd Ed., Orlando, FL, Academic Press, Inc., 1980, pg. 222.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy import linalg as LA
\>>> a \= np.array(\[\[1, \-2j\], \[2j, 5\]\])
\>>> a
array(\[\[ 1.+0.j, -0.-2.j\],\
       \[ 0.+2.j,  5.+0.j\]\])
\>>> eigenvalues, eigenvectors \= LA.eigh(a)
\>>> eigenvalues
array(\[0.17157288, 5.82842712\])
\>>> eigenvectors
array(\[\[-0.92387953+0.j        , -0.38268343+0.j        \], # may vary\
       \[ 0.        +0.38268343j,  0.        -0.92387953j\]\])

Copy to clipboard

\>>> (np.dot(a, eigenvectors\[:, 0\]) \-
... eigenvalues\[0\] \* eigenvectors\[:, 0\])  \# verify 1st eigenval/vec pair
array(\[5.55111512e-17+0.0000000e+00j, 0.00000000e+00+1.2490009e-16j\])
\>>> (np.dot(a, eigenvectors\[:, 1\]) \-
... eigenvalues\[1\] \* eigenvectors\[:, 1\])  \# verify 2nd eigenval/vec pair
array(\[0.+0.j, 0.+0.j\])

Copy to clipboard

\>>> A \= np.matrix(a) \# what happens if input is a matrix object
\>>> A
matrix(\[\[ 1.+0.j, -0.-2.j\],\
        \[ 0.+2.j,  5.+0.j\]\])
\>>> eigenvalues, eigenvectors \= LA.eigh(A)
\>>> eigenvalues
array(\[0.17157288, 5.82842712\])
\>>> eigenvectors
matrix(\[\[-0.92387953+0.j        , -0.38268343+0.j        \], # may vary\
        \[ 0.        +0.38268343j,  0.        -0.92387953j\]\])

Copy to clipboard

\>>> \# demonstrate the treatment of the imaginary part of the diagonal
\>>> a \= np.array(\[\[5+2j, 9\-2j\], \[0+2j, 2\-1j\]\])
\>>> a
array(\[\[5.+2.j, 9.-2.j\],\
       \[0.+2.j, 2.-1.j\]\])
\>>> \# with UPLO='L' this is numerically equivalent to using LA.eig() with:
\>>> b \= np.array(\[\[5.+0.j, 0.\-2.j\], \[0.+2.j, 2.\-0.j\]\])
\>>> b
array(\[\[5.+0.j, 0.-2.j\],\
       \[0.+2.j, 2.+0.j\]\])
\>>> wa, va \= LA.eigh(a)
\>>> wb, vb \= LA.eig(b)
\>>> wa
array(\[1., 6.\])
\>>> wb
array(\[6.+0.j, 1.+0.j\])
\>>> va
array(\[\[-0.4472136 +0.j        , -0.89442719+0.j        \], # may vary\
       \[ 0.        +0.89442719j,  0.        -0.4472136j \]\])
\>>> vb
array(\[\[ 0.89442719+0.j       , -0.        +0.4472136j\],\
       \[-0.        +0.4472136j,  0.89442719+0.j       \]\])

Copy to clipboard

Go BackOpen In Tab

On this page