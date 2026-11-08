[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.k_means.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.k_means.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.k_means.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.k_means.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.k_means.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.k_means.html)

Collapse Sidebar Expand Sidebar

k\_means[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#k-means "Link to this heading")

===========================================================================================================================

sklearn.cluster.k\_means(_X_, _n\_clusters_, _\*_, _sample\_weight\=None_, _init\='k-means++'_, _n\_init\='auto'_, _max\_iter\=300_, _verbose\=False_, _tol\=0.0001_, _random\_state\=None_, _copy\_x\=True_, _algorithm\='lloyd'_, _return\_n\_iter\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L296)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "Link to this definition")

Perform K-means clustering algorithm.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#k-means)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The observations to cluster. It must be noted that the data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous.

**n\_clusters**int

The number of clusters to form as well as the number of centroids to generate.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in `X`. If `None`, all observations are assigned equal weight. `sample_weight` is not used during initialization if `init` is a callable or a user provided array.

**init**{‘k-means++’, ‘random’}, callable or array-like of shape (n\_clusters, n\_features), default=’k-means++’

Method for initialization:

*   `'k-means++'` : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. See section Notes in k\_init for more details.
    
*   `'random'`: choose `n_clusters` observations (rows) at random from data for the initial centroids.
    
*   If an array is passed, it should be of shape `(n_clusters, n_features)` and gives the initial centers.
    
*   If a callable is passed, it should take arguments `X`, `n_clusters` and a random state and return an initialization.
    

**n\_init**‘auto’ or int, default=”auto”

Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n\_init consecutive runs in terms of inertia.

When `n_init='auto'`, the number of runs depends on the value of init: 10 if using `init='random'` or `init` is a callable; 1 if using `init='k-means++'` or `init` is an array-like.

Added in version 1.2: Added ‘auto’ option for `n_init`.

Changed in version 1.4: Default value for `n_init` changed to `'auto'`.

**max\_iter**int, default=300

Maximum number of iterations of the k-means algorithm to run.

**verbose**bool, default=False

Verbosity mode.

**tol**float, default=1e-4

Relative tolerance with regards to Frobenius norm of the difference in the cluster centers of two consecutive iterations to declare convergence.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for centroid initialization. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**copy\_x**bool, default=True

When pre-computing distances it is more numerically accurate to center the data first. If `copy_x` is True (default), then the original data is not modified. If False, the original data is modified, and put back before the function returns, but small numerical differences may be introduced by subtracting and then adding the data mean. Note that if the original data is not C-contiguous, a copy will be made even if `copy_x` is False. If the original data is sparse, but not in CSR format, a copy will be made even if `copy_x` is False.

**algorithm**{“lloyd”, “elkan”}, default=”lloyd”

K-means algorithm to use. The classical EM-style algorithm is `"lloyd"`. The `"elkan"` variation can be more efficient on some datasets with well-defined clusters, by using the triangle inequality. However it’s more memory intensive due to the allocation of an extra array of shape `(n_samples, n_clusters)`.

Changed in version 0.18: Added Elkan algorithm

Changed in version 1.1: Renamed “full” to “lloyd”, and deprecated “auto” and “full”. Changed “auto” to use “lloyd” instead of “elkan”.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

Returns:

**centroid**ndarray of shape (n\_clusters, n\_features)

Centroids found at the last iteration of k-means.

**label**ndarray of shape (n\_samples,)

The `label[i]` is the code or index of the centroid the i’th observation is closest to.

**inertia**float

The final value of the inertia criterion (sum of squared distances to the closest centroid for all observations in the training set).

**best\_n\_iter**int

Number of iterations corresponding to the best results. Returned only if `return_n_iter` is set to True.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import k\_means
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[10, 2\], \[10, 4\], \[10, 0\]\])
\>>> centroid, label, inertia \= k\_means(
...     X, n\_clusters\=2, n\_init\="auto", random\_state\=0
... )
\>>> centroid
array(\[\[10.,  2.\],\
       \[ 1.,  2.\]\])
\>>> label
array(\[1, 1, 1, 0, 0, 0\], dtype=int32)
\>>> inertia
16.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)