[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.pinv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.pinv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.pinv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.pinv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.pinv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.pinv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.pinv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.pinv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.pinv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.pinv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.pinv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.pinv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.pinv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.pinv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.pinv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.pinv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.pinv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.pinv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.pinv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.pinv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.pinv[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#numpy-linalg-pinv "Link to this heading")

=======================================================================================================================================

linalg.pinv(_a_, _rcond=None_, _hermitian=False_, _\*_, _rtol=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L2153-L2265)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#numpy.linalg.pinv "Link to this definition")

Compute the (Moore-Penrose) pseudo-inverse of a matrix.

Calculate the generalized inverse of a matrix using its singular-value decomposition (SVD) and including all _large_ singular values.

Parameters:

**a**(…, M, N) array\_like

Matrix or stack of matrices to be pseudo-inverted.

**rcond**(…) array\_like of float, optional

Cutoff for small singular values. Singular values less than or equal to `rcond * largest_singular_value` are set to zero. Broadcasts against the stack of matrices. Default: `1e-15`.

**hermitian**bool, optional

If True, _a_ is assumed to be Hermitian (symmetric if real-valued), enabling a more efficient method for finding singular values. Defaults to False.

**rtol**(…) array\_like of float, optional

Same as _rcond_, but it’s an Array API compatible parameter name. Only _rcond_ or _rtol_ can be set at a time. If none of them are provided then NumPy’s `1e-15` default is used. If `rtol=None` is passed then the API standard default is used.

New in version 2.0.0.

Returns:

**B**(…, N, M) ndarray

The pseudo-inverse of _a_. If _a_ is a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 instance, then so is _B_.

Raises:

LinAlgError

If the SVD computation does not converge.

See also

[`scipy.linalg.pinv`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.pinv.html#scipy.linalg.pinv "(in SciPy v1.18.0)")

Similar function in SciPy.

[`scipy.linalg.pinvh`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.pinvh.html#scipy.linalg.pinvh "(in SciPy v1.18.0)")

Compute the (Moore-Penrose) pseudo-inverse of a Hermitian matrix.

Notes

The pseudo-inverse of a matrix A, denoted \\(A^+\\), is defined as: “the matrix that ‘solves’ \[the least-squares problem\] \\(Ax = b\\),” i.e., if \\(\\bar{x}\\) is said solution, then \\(A^+\\) is that matrix such that \\(\\bar{x} = A^+b\\).

It can be shown that if \\(Q\_1 \\Sigma Q\_2^T = A\\) is the singular value decomposition of A, then \\(A^+ = Q\_2 \\Sigma^+ Q\_1^T\\), where \\(Q\_{1,2}\\) are orthogonal matrices, \\(\\Sigma\\) is a diagonal matrix consisting of A’s so-called singular values, (followed, typically, by zeros), and then \\(\\Sigma^+\\) is simply the diagonal matrix consisting of the reciprocals of A’s singular values (again, followed by zeros). [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#rec505eafac9d-1)

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#id1)\
\]

G. Strang, _Linear Algebra and Its Applications_, 2nd Ed., Orlando, FL, Academic Press, Inc., 1980, pp. 139-142.

Examples

Try it in your browser!

The following example checks that `a * a+ * a == a` and `a+ * a * a+ == a+`:

\>>> import numpy as np
\>>> rng \= np.random.default\_rng()
\>>> a \= rng.normal(size\=(9, 6))
\>>> B \= np.linalg.pinv(a)
\>>> np.allclose(a, np.dot(a, np.dot(B, a)))
True
\>>> np.allclose(B, np.dot(B, np.dot(a, B)))
True

Copy to clipboard

Go BackOpen In Tab

On this page