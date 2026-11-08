[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.cosine_distances.html)

Collapse Sidebar Expand Sidebar

cosine\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#cosine-distances "Link to this heading")

===============================================================================================================================================================

sklearn.metrics.pairwise.cosine\_distances(_X_, _Y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1129)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "Link to this definition")

Compute cosine distance between samples in X and Y.

Cosine distance is defined as 1.0 minus the cosine similarity.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

Matrix `X`.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

Matrix `Y`.

Returns:

**distances**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Returns the cosine distance between samples in X and Y.

See also

[`cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity")

Compute cosine similarity between samples in X and Y.

[`scipy.spatial.distance.cosine`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html#scipy.spatial.distance.cosine "(in SciPy v1.18.0)")

Dense matrices only.

Examples

\>>> from sklearn.metrics.pairwise import cosine\_distances
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> cosine\_distances(X, Y)
array(\[\[1.   , 1.   \],\
       \[0.422, 0.183\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)