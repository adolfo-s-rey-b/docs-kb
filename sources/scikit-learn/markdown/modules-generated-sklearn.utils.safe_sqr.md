[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_sqr.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.safe_sqr.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_sqr.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.safe_sqr.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.safe_sqr.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.safe_sqr.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.safe_sqr.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.safe_sqr.html)

Collapse Sidebar Expand Sidebar

safe\_sqr[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_sqr.html#safe-sqr "Link to this heading")

============================================================================================================================

sklearn.utils.safe\_sqr(_X_, _\*_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L1381)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_sqr.html#sklearn.utils.safe_sqr "Link to this definition")

Element wise squaring of array-likes and sparse matrices.

Parameters:

**X**{array-like, ndarray, sparse matrix}

**copy**bool, default=True

Whether to create a copy of X and operate on it or to perform inplace computation (default behaviour).

Returns:

**X \*\* 2**element wise square

Return the element-wise square of the input.

Examples

\>>> from sklearn.utils import safe\_sqr
\>>> safe\_sqr(\[1, 2, 3\])
array(\[1, 4, 9\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)