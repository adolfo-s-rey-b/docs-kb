[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.calinski_harabasz_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.calinski_harabasz_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.calinski_harabasz_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.calinski_harabasz_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.calinski_harabasz_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.calinski_harabasz_score.html)

Collapse Sidebar Expand Sidebar

calinski\_harabasz\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#calinski-harabasz-score "Link to this heading")

============================================================================================================================================================================

sklearn.metrics.calinski\_harabasz\_score(_X_, _labels_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_unsupervised.py#L326)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score "Link to this definition")

Compute the Calinski and Harabasz score.

It is also known as the Variance Ratio Criterion.

The score is defined as ratio of the sum of between-cluster dispersion and of within-cluster dispersion.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

A list of `n_features`\-dimensional data points. Each row corresponds to a single data point.

**labels**array-like of shape (n\_samples,)

Predicted labels for each sample.

Returns:

**score**float

The resulting Calinski-Harabasz score.

References

\[1\]

[T. Calinski and J. Harabasz, 1974. “A dendrite method for cluster analysis”. Communications in Statistics](https://www.tandfonline.com/doi/abs/10.1080/03610927408827101)

Examples

\>>> from sklearn.datasets import make\_blobs
\>>> from sklearn.cluster import KMeans
\>>> from sklearn.metrics import calinski\_harabasz\_score
\>>> X, \_ \= make\_blobs(random\_state\=0)
\>>> kmeans \= KMeans(n\_clusters\=3, random\_state\=0,).fit(X)
\>>> calinski\_harabasz\_score(X, kmeans.labels\_)
114.8...

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)