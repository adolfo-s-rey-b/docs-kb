[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html)

Collapse Sidebar Expand Sidebar

manhattan\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#manhattan-distances "Link to this heading")

========================================================================================================================================================================

sklearn.metrics.pairwise.manhattan\_distances(_X_, _Y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1048)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "Link to this definition")

Compute the L1 distances between the vectors in X and Y.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

An array where each row is a sample and each column is a feature.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An array where each row is a sample and each column is a feature. If `None`, method uses `Y=X`.

Returns:

**distances**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Pairwise L1 distances.

Notes

When X and/or Y are CSR sparse matrices and they are not already in canonical format, this function modifies them in-place to make them canonical.

Examples

\>>> from sklearn.metrics.pairwise import manhattan\_distances
\>>> manhattan\_distances(\[\[3\]\], \[\[3\]\])
array(\[\[0.\]\])
\>>> manhattan\_distances(\[\[3\]\], \[\[2\]\])
array(\[\[1.\]\])
\>>> manhattan\_distances(\[\[2\]\], \[\[3\]\])
array(\[\[1.\]\])
\>>> manhattan\_distances(\[\[1, 2\], \[3, 4\]\],         \[\[1, 2\], \[0, 3\]\])
array(\[\[0., 2.\],\
       \[4., 4.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)