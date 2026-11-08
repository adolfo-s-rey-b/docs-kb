[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.kmeans_plusplus.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.kmeans_plusplus.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.kmeans_plusplus.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.kmeans_plusplus.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.kmeans_plusplus.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.kmeans_plusplus.html)

Collapse Sidebar Expand Sidebar

kmeans\_plusplus[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#kmeans-plusplus "Link to this heading")

===================================================================================================================================================

sklearn.cluster.kmeans\_plusplus(_X_, _n\_clusters_, _\*_, _sample\_weight\=None_, _x\_squared\_norms\=None_, _random\_state\=None_, _n\_local\_trials\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L63)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "Link to this definition")

Init n\_clusters seeds according to k-means++.

Added in version 0.24.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to pick seeds from.

**n\_clusters**int

The number of centroids to initialize.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in `X`. If `None`, all observations are assigned equal weight. `sample_weight` is ignored if `init` is a callable or a user provided array.

Added in version 1.3.

**x\_squared\_norms**array-like of shape (n\_samples,), default=None

Squared Euclidean norm of each data point.

**random\_state**int or RandomState instance, default=None

Determines random number generation for centroid initialization. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_local\_trials**int, default=None

The number of seeding trials for each center (except the first), of which the one reducing inertia the most is greedily chosen. Set to None to make the number of trials depend logarithmically on the number of seeds (2+log(k)) which is the recommended setting. Setting to 1 disables the greedy cluster selection and recovers the vanilla k-means++ algorithm which was empirically shown to work less well than its greedy variant.

Returns:

**centers**ndarray of shape (n\_clusters, n\_features)

The initial centers for k-means.

**indices**ndarray of shape (n\_clusters,)

The index location of the chosen centers in the data array X. For a given index and center, X\[index\] = center.

Notes

Selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. see: Arthur, D. and Vassilvitskii, S. “k-means++: the advantages of careful seeding”. ACM-SIAM symposium on Discrete algorithms. 2007

Examples

\>>> from sklearn.cluster import kmeans\_plusplus
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[10, 2\], \[10, 4\], \[10, 0\]\])
\>>> centers, indices \= kmeans\_plusplus(X, n\_clusters\=2, random\_state\=0)
\>>> centers
array(\[\[10,  2\],\
       \[ 1,  0\]\])
\>>> indices
array(\[3, 2\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_plusplus_thumb.png)

[An example of K-Means++ initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html)

An example of K-Means++ initialization

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)