[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html)

Collapse Sidebar Expand Sidebar

paired\_manhattan\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#paired-manhattan-distances "Link to this heading")

==============================================================================================================================================================================================

sklearn.metrics.pairwise.paired\_manhattan\_distances(_X_, _Y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1224)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#sklearn.metrics.pairwise.paired_manhattan_distances "Link to this definition")

Compute the paired L1 distances between X and Y.

Distances are calculated between (X\[0\], Y\[0\]), (X\[1\], Y\[1\]), …, etc.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

An array-like where each row is a sample and each column is a feature.

**Y**{array-like, sparse matrix} of shape (n\_samples, n\_features)

An array-like where each row is a sample and each column is a feature.

Returns:

**distances**ndarray of shape (n\_samples,)

Returns the manhattan distances between the row vectors of `X` and the row vectors of `Y`, where `distances[i]` is the distance between `X[i]` and `Y[i]`.

Examples

\>>> from sklearn.metrics.pairwise import paired\_manhattan\_distances
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1, 0\], \[0, 1, 0\], \[0, 0, 1\]\])
\>>> Y \= np.array(\[\[0, 1, 0\], \[0, 0, 1\], \[0, 0, 0\]\])
\>>> paired\_manhattan\_distances(X, Y)
array(\[1., 2., 1.\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)