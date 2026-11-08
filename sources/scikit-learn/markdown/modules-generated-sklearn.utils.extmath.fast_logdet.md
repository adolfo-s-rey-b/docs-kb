[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.fast_logdet.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.extmath.fast_logdet.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.fast_logdet.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.extmath.fast_logdet.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.extmath.fast_logdet.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.extmath.fast_logdet.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.extmath.fast_logdet.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.extmath.fast_logdet.html)

Collapse Sidebar Expand Sidebar

fast\_logdet[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.fast_logdet.html#fast-logdet "Link to this heading")

=============================================================================================================================================

sklearn.utils.extmath.fast\_logdet(_A_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L98)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.fast_logdet.html#sklearn.utils.extmath.fast_logdet "Link to this definition")

Compute logarithm of determinant of a square matrix.

The (natural) logarithm of the determinant of a square matrix is returned if det(A) is non-negative and well defined. If the determinant is zero or negative returns -Inf.

Equivalent to : np.log(np.det(A)) but more robust.

Parameters:

**A**array\_like of shape (n, n)

The square matrix.

Returns:

**logdet**float

When det(A) is strictly positive, log(det(A)) is returned. When det(A) is non-positive or not defined, then -inf is returned.

See also

[`numpy.linalg.slogdet`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html#numpy.linalg.slogdet "(in NumPy v2.5)")

Compute the sign and (natural) logarithm of the determinant of an array.

Examples

\>>> import numpy as np
\>>> from sklearn.utils.extmath import fast\_logdet
\>>> a \= np.array(\[\[5, 1\], \[2, 8\]\])
\>>> fast\_logdet(a)
np.float64(3.6375861597263857)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)