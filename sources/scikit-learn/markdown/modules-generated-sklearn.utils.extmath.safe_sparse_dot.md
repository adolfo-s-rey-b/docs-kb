[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html)

Collapse Sidebar Expand Sidebar

safe\_sparse\_dot[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#safe-sparse-dot "Link to this heading")

==========================================================================================================================================================

sklearn.utils.extmath.safe\_sparse\_dot(_a_, _b_, _\*_, _dense\_output\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L166)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#sklearn.utils.extmath.safe_sparse_dot "Link to this definition")

Dot product that handle the sparse matrix case correctly.

Parameters:

**a**{ndarray, sparse matrix}

First operand of the dot product.

**b**{ndarray, sparse matrix}

Second operand of the dot product.

**dense\_output**bool, default=False

When False, `a` and `b` both being sparse will yield sparse output. When True, output will always be a dense array.

Returns:

**dot\_product**{ndarray, sparse matrix}

Sparse if `a` and `b` are sparse and `dense_output=False`.

Examples

\>>> from scipy.sparse import csr\_array
\>>> from sklearn.utils.extmath import safe\_sparse\_dot
\>>> X \= csr\_array(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
\>>> dot\_product \= safe\_sparse\_dot(X, X.T)
\>>> dot\_product.toarray()
array(\[\[ 5, 11, 17\],\
       \[11, 25, 39\],\
       \[17, 39, 61\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)