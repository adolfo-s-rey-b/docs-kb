[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.eigvalsh.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.eigvalsh.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.eigvalsh.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.eigvalsh.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eigvalsh.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigvalsh.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.eigvalsh.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.eigvalsh.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.eigvalsh.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.eigvalsh.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.eigvalsh.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.eigvalsh.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.eigvalsh.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.eigvalsh.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.eigvalsh.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.eigvalsh.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.eigvalsh.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.eigvalsh.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.eigvalsh.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.eigvalsh.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.eigvalsh[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy-linalg-eigvalsh "Link to this heading")

===================================================================================================================================================

linalg.eigvalsh(_a_, _UPLO\='L'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L1269-L1360)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "Link to this definition")

Compute the eigenvalues of a complex Hermitian or real symmetric matrix.

Main difference from eigh: the eigenvectors are not computed.

Parameters:

**a**(…, M, M) array\_like

A complex- or real-valued matrix whose eigenvalues are to be computed.

**UPLO**{‘L’, ‘U’}, optional

Specifies whether the calculation is done with the lower triangular part of _a_ (‘L’, default) or the upper triangular part (‘U’). Irrespective of this value only the real parts of the diagonal will be considered in the computation to preserve the notion of a Hermitian matrix. It therefore follows that the imaginary part of the diagonal will always be treated as zero.

Returns:

**w**(…, M,) ndarray

The eigenvalues in ascending order, each repeated according to its multiplicity.

Raises:

LinAlgError

If the eigenvalue computation does not converge.

See also

[`eigh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")

eigenvalues and eigenvectors of real symmetric or complex Hermitian (conjugate symmetric) arrays.

[`eigvals`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "numpy.linalg.eigvals")

eigenvalues of general real or complex arrays.

[`eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "numpy.linalg.eig")

eigenvalues and right eigenvectors of general real or complex arrays.

[`scipy.linalg.eigvalsh`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigvalsh.html#scipy.linalg.eigvalsh "(in SciPy v1.18.0)")

Similar function in SciPy.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

The eigenvalues are computed using LAPACK routines `_syevd`, `_heevd`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy import linalg as LA
\>>> a \= np.array(\[\[1, \-2j\], \[2j, 5\]\])
\>>> LA.eigvalsh(a)
array(\[ 0.17157288,  5.82842712\]) # may vary

Copy to clipboard

\>>> \# demonstrate the treatment of the imaginary part of the diagonal
\>>> a \= np.array(\[\[5+2j, 9\-2j\], \[0+2j, 2\-1j\]\])
\>>> a
array(\[\[5.+2.j, 9.-2.j\],\
       \[0.+2.j, 2.-1.j\]\])
\>>> \# with UPLO='L' this is numerically equivalent to using LA.eigvals()
\>>> \# with:
\>>> b \= np.array(\[\[5.+0.j, 0.\-2.j\], \[0.+2.j, 2.\-0.j\]\])
\>>> b
array(\[\[5.+0.j, 0.-2.j\],\
       \[0.+2.j, 2.+0.j\]\])
\>>> wa \= LA.eigvalsh(a)
\>>> wb \= LA.eigvals(b)
\>>> wa
array(\[1., 6.\])
\>>> wb
array(\[6.+0.j, 1.+0.j\])

Copy to clipboard

Go BackOpen In Tab

On this page