[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.matrix_rank.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.matrix_rank.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.matrix_rank.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.matrix_rank.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.matrix_rank.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.matrix_rank.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.matrix_rank.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.matrix_rank.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.matrix_rank.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.matrix_rank.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.matrix_rank.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.matrix_rank.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.matrix_rank.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.matrix_rank.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.matrix_rank.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.matrix_rank.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.matrix_rank.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.matrix_rank.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.matrix_rank.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.matrix_rank.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.matrix\_rank[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#numpy-linalg-matrix-rank "Link to this heading")

=============================================================================================================================================================

linalg.matrix\_rank(_A_, _tol\=None_, _hermitian\=False_, _\*_, _rtol\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L2034-L2144)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#numpy.linalg.matrix_rank "Link to this definition")

Return matrix rank of array using SVD method

Rank of the array is the number of singular values of the array that are greater than _tol_.

Parameters:

**A**{(M,), (…, M, N)} array\_like

Input vector or stack of matrices.

**tol**(…) array\_like, float, optional

Threshold below which SVD values are considered zero. If _tol_ is None, and `S` is an array with singular values for _M_, and `eps` is the epsilon value for datatype of `S`, then _tol_ is set to `S.max() * max(M, N) * eps`.

**hermitian**bool, optional

If True, _A_ is assumed to be Hermitian (symmetric if real-valued), enabling a more efficient method for finding singular values. Defaults to False.

**rtol**(…) array\_like, float, optional

Parameter for the relative tolerance component. Only `tol` or `rtol` can be set at a time. Defaults to `max(M, N) * eps`.

New in version 2.0.0.

Returns:

**rank**(…) array\_like

Rank of A.

Notes

The default threshold to detect rank deficiency is a test on the magnitude of the singular values of _A_. By default, we identify singular values less than `S.max() * max(M, N) * eps` as indicating rank deficiency (with the symbols defined above). This is the algorithm MATLAB uses [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#ra43e662d710b-1)
. It also appears in _Numerical recipes_ in the discussion of SVD solutions for linear least squares [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#ra43e662d710b-2)
.

This default threshold is designed to detect rank deficiency accounting for the numerical errors of the SVD computation. Imagine that there is a column in _A_ that is an exact (in floating point) linear combination of other columns in _A_. Computing the SVD on _A_ will not produce a singular value exactly equal to 0 in general: any difference of the smallest SVD value from 0 will be caused by numerical imprecision in the calculation of the SVD. Our threshold for small SVD values takes this numerical imprecision into account, and the default threshold will detect such numerical rank deficiency. The threshold may declare a matrix _A_ rank deficient even if the linear combination of some columns of _A_ is not exactly equal to another column of _A_ but only numerically very close to another column of _A_.

We chose our default threshold because it is in wide use. Other thresholds are possible. For example, elsewhere in the 2007 edition of _Numerical recipes_ there is an alternative threshold of `S.max() * np.finfo(A.dtype).eps / 2. * np.sqrt(m + n + 1.)`. The authors describe this threshold as being based on “expected roundoff error” (p 71).

The thresholds above deal with floating point roundoff error in the calculation of the SVD. However, you may have more information about the sources of error in _A_ that would make you consider other tolerance values to detect _effective_ rank deficiency. The most useful measure of the tolerance depends on the operations you intend to use on your matrix. For example, if your data come from uncertain measurements with uncertainties greater than floating point epsilon, choosing a tolerance near that uncertainty may be preferable. The tolerance may be absolute if the uncertainties are absolute rather than relative.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#id1)\
\]

MATLAB reference documentation, “Rank” [https://www.mathworks.com/help/techdoc/ref/rank.html](https://www.mathworks.com/help/techdoc/ref/rank.html)

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#id2)\
\]

W. H. Press, S. A. Teukolsky, W. T. Vetterling and B. P. Flannery, “Numerical Recipes (3rd edition)”, Cambridge University Press, 2007, page 795.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.linalg import matrix\_rank
\>>> matrix\_rank(np.eye(4)) \# Full rank matrix
4
\>>> I\=np.eye(4); I\[\-1,\-1\] \= 0. \# rank deficient matrix
\>>> matrix\_rank(I)
3
\>>> matrix\_rank(np.ones((4,))) \# 1 dimension - rank 1 unless all 0
1
\>>> matrix\_rank(np.zeros((4,)))
0

Copy to clipboard

Go BackOpen In Tab

On this page