[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.extmath.randomized_svd.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.extmath.randomized_svd.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.extmath.randomized_svd.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.extmath.randomized_svd.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.extmath.randomized_svd.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.extmath.randomized_svd.html)

Collapse Sidebar Expand Sidebar

randomized\_svd[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#randomized-svd "Link to this heading")

======================================================================================================================================================

sklearn.utils.extmath.randomized\_svd(_M_, _n\_components_, _\*_, _n\_oversamples\=10_, _n\_iter\='auto'_, _power\_iteration\_normalizer\='auto'_, _transpose\='auto'_, _flip\_sign\=True_, _random\_state\=None_, _svd\_lapack\_driver\='gesdd'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L388)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "Link to this definition")

Compute a truncated randomized SVD.

This method solves the fixed-rank approximation problem described in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#rf38c2b656ebc-1)
 (problem (1.5), p5).

Refer to [Wikipedia principal eigenvector](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#sphx-glr-auto-examples-applications-plot-wikipedia-principal-eigenvector-py)
 for a typical example where the power iteration algorithm is used to rank web pages. This algorithm is also known to be used as a building block in Google’s PageRank algorithm.

Parameters:

**M**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Matrix to decompose.

**n\_components**int

Number of singular values and vectors to extract.

**n\_oversamples**int, default=10

Additional number of random vectors to sample the range of `M` so as to ensure proper conditioning. The total number of random vectors used to find the range of `M` is `n_components + n_oversamples`. Smaller number can improve speed but can negatively impact the quality of approximation of singular vectors and singular values. Users might wish to increase this parameter up to `2*k - n_components` where k is the effective rank, for large matrices, noisy problems, matrices with slowly decaying spectrums, or to increase precision accuracy. See [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#rf38c2b656ebc-1)
 (pages 5, 23 and 26).

**n\_iter**int or ‘auto’, default=’auto’

Number of power iterations. It can be used to deal with very noisy problems. When ‘auto’, it is set to 4, unless `n_components` is small (< .1 \* min(X.shape)) in which case `n_iter` is set to 7. This improves precision with few components. Note that in general users should rather increase `n_oversamples` before increasing `n_iter` as the principle of the randomized method is to avoid usage of these more costly power iterations steps. When `n_components` is equal or greater to the effective matrix rank and the spectrum does not present a slow decay, `n_iter=0` or `1` should even work fine in theory (see [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#rf38c2b656ebc-1)
 page 9).

Changed in version 0.18.

**power\_iteration\_normalizer**{‘auto’, ‘QR’, ‘LU’, ‘none’}, default=’auto’

Whether the power iterations are normalized with step-by-step QR factorization (the slowest but most accurate), ‘none’ (the fastest but numerically unstable when `n_iter` is large, e.g. typically 5 or larger), or ‘LU’ factorization (numerically stable but can lose slightly in accuracy). The ‘auto’ mode applies no normalization if `n_iter` <= 2 and switches to LU otherwise.

Added in version 0.18.

**transpose**bool or ‘auto’, default=’auto’

Whether the algorithm should be applied to M.T instead of M. The result should approximately be the same. The ‘auto’ mode will trigger the transposition if M.shape\[1\] > M.shape\[0\] since this implementation of randomized SVD tend to be a little faster in that case.

Changed in version 0.18.

**flip\_sign**bool, default=True

The output of a singular value decomposition is only unique up to a permutation of the signs of the singular vectors. If `flip_sign` is set to `True`, the sign ambiguity is resolved by making the largest loadings for each component in the left singular vectors positive.

**random\_state**int, RandomState instance or None, default=None

The seed of the pseudo random number generator to use when shuffling the data, i.e. getting the random vectors to initialize the algorithm. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Changed in version 1.2: The default value changed from 0 to None.

**svd\_lapack\_driver**{“gesdd”, “gesvd”}, default=”gesdd”

Whether to use the more efficient divide-and-conquer approach (`"gesdd"`) or more general rectangular approach (`"gesvd"`) to compute the SVD of the matrix B, which is the projection of M into a low dimensional subspace, as described in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#rf38c2b656ebc-1)
.

Added in version 1.2.

Returns:

**u**ndarray of shape (n\_samples, n\_components)

Unitary matrix having left singular vectors with signs flipped as columns.

**s**ndarray of shape (n\_components,)

The singular values, sorted in non-increasing order.

**vh**ndarray of shape (n\_components, n\_features)

Unitary matrix having right singular vectors with signs flipped as rows.

Notes

This algorithm finds a (usually very good) approximate truncated singular value decomposition using randomization to speed up the computations. It is particularly fast on large matrices on which you wish to extract only a small number of components. In order to obtain further speed up, `n_iter` can be set <=2 (at the cost of loss of precision). To increase the precision it is recommended to increase `n_oversamples`, up to `2*k-n_components` where k is the effective rank. Usually, `n_components` is chosen to be greater than k so increasing `n_oversamples` up to `n_components` should be enough.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#id1)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#id2)
,[3](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#id3)
,[4](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#id4)
)

[“Finding structure with randomness: Stochastic algorithms for constructing approximate matrix decompositions”](https://arxiv.org/abs/0909.4061)
 Halko, et al. (2009)

\[2\]

[“A randomized algorithm for the decomposition of matrices”](https://doi.org/10.1016/j.acha.2010.02.003)
 Per-Gunnar Martinsson, Vladimir Rokhlin and Mark Tygert (2011)

\[3\]

[“An implementation of a randomized algorithm for principal component analysis”](https://arxiv.org/abs/1412.3510)
 A. Szlam et al. (2014)

Examples

\>>> import numpy as np
\>>> from sklearn.utils.extmath import randomized\_svd
\>>> a \= np.array(\[\[1, 2, 3, 5\],\
...               \[3, 4, 5, 6\],\
...               \[7, 8, 9, 10\]\])
\>>> U, s, Vh \= randomized\_svd(a, n\_components\=2, random\_state\=0)
\>>> U.shape, s.shape, Vh.shape
((3, 2), (2,), (2, 4))

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)