[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.trustworthiness.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.trustworthiness.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.trustworthiness.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.trustworthiness.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.trustworthiness.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.trustworthiness.html)

Collapse Sidebar Expand Sidebar

trustworthiness[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#trustworthiness "Link to this heading")

===================================================================================================================================================

sklearn.manifold.trustworthiness(_X_, _X\_embedded_, _\*_, _n\_neighbors\=5_, _metric\='euclidean'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_t_sne.py#L444)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "Link to this definition")

Indicate to what extent the local structure is retained.

The trustworthiness is within \[0, 1\]. It is defined as

T(k)\=1−2nk(2n−3k−1)∑i\=1n∑j∈Nikmax(0,(r(i,j)−k))

where for each sample i, Nik are its k nearest neighbors in the output space, and every sample j is its r(i,j)\-th nearest neighbor in the input space. In other words, any unexpected nearest neighbors in the output space are penalised in proportion to their rank in the input space.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or

(n\_samples, n\_samples) If the metric is ‘precomputed’ X must be a square distance matrix. Otherwise it contains a sample per row.

**X\_embedded**{array-like, sparse matrix} of shape (n\_samples, n\_components)

Embedding of the training data in low-dimensional space.

**n\_neighbors**int, default=5

The number of neighbors that will be considered. Should be fewer than `n_samples / 2` to ensure the trustworthiness to lies within \[0, 1\], as mentioned in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#r5831441d8a57-1)
. An error will be raised otherwise.

**metric**str or callable, default=’euclidean’

Which metric to use for computing pairwise distances between samples from the original input space. If metric is ‘precomputed’, X must be a matrix of pairwise distances or squared distances. Otherwise, for a list of available metrics, see the documentation of argument metric in `sklearn.pairwise.pairwise_distances` and metrics listed in `sklearn.metrics.pairwise.PAIRWISE_DISTANCE_FUNCTIONS`. Note that the “cosine” metric uses [`cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "sklearn.metrics.pairwise.cosine_distances")
.

Added in version 0.20.

Returns:

**trustworthiness**float

Trustworthiness of the low-dimensional embedding.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#id1)\
\]

Jarkko Venna and Samuel Kaski. 2001. Neighborhood Preservation in Nonlinear Projection Methods: An Experimental Study. In Proceedings of the International Conference on Artificial Neural Networks (ICANN ‘01). Springer-Verlag, Berlin, Heidelberg, 485-491.

\[2\]

Laurens van der Maaten. Learning a Parametric Embedding by Preserving Local Structure. Proceedings of the Twelfth International Conference on Artificial Intelligence and Statistics, PMLR 5:384-391, 2009.

Examples

\>>> from sklearn.datasets import make\_blobs
\>>> from sklearn.decomposition import PCA
\>>> from sklearn.manifold import trustworthiness
\>>> X, \_ \= make\_blobs(n\_samples\=100, n\_features\=10, centers\=3, random\_state\=42)
\>>> X\_embedded \= PCA(n\_components\=2).fit\_transform(X)
\>>> print(f"{trustworthiness(X, X\_embedded, n\_neighbors\=5):.2f}")
0.92

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)