[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

affinity\_propagation[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#affinity-propagation "Link to this heading")

==================================================================================================================================================================

sklearn.cluster.affinity\_propagation(_S_, _\*_, _preference\=None_, _convergence\_iter\=15_, _max\_iter\=200_, _damping\=0.5_, _copy\=True_, _verbose\=False_, _return\_n\_iter\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_affinity_propagation.py#L182)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#sklearn.cluster.affinity_propagation "Link to this definition")

Perform Affinity Propagation Clustering of data.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation)
.

Parameters:

**S**array-like of shape (n\_samples, n\_samples)

Matrix of similarities between points.

**preference**array-like of shape (n\_samples,) or float, default=None

Preferences for each point - points with larger values of preferences are more likely to be chosen as exemplars. The number of exemplars, i.e. of clusters, is influenced by the input preferences value. If the preferences are not passed as arguments, they will be set to the median of the input similarities (resulting in a moderate number of clusters). For a smaller amount of clusters, this can be set to the minimum value of the similarities.

**convergence\_iter**int, default=15

Number of iterations with no change in the number of estimated clusters that stops the convergence.

**max\_iter**int, default=200

Maximum number of iterations.

**damping**float, default=0.5

Damping factor between 0.5 and 1.

**copy**bool, default=True

If copy is False, the affinity matrix is modified inplace by the algorithm, for memory efficiency.

**verbose**bool, default=False

The verbosity level.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

**random\_state**int, RandomState instance or None, default=None

Pseudo-random number generator to control the starting state. Use an int for reproducible results across function calls. See the [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Added in version 0.23: this parameter was previously hardcoded as 0.

Returns:

**cluster\_centers\_indices**ndarray of shape (n\_clusters,)

Index of clusters centers.

**labels**ndarray of shape (n\_samples,)

Cluster labels for each point.

**n\_iter**int

Number of iterations run. Returned only if `return_n_iter` is set to True.

Notes

For an example usage, see [Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#sphx-glr-auto-examples-cluster-plot-affinity-propagation-py)
. You may also check out, [Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#sphx-glr-auto-examples-applications-plot-stock-market-py)

When the algorithm does not converge, it will still return an array of `cluster_center_indices` and labels if there are any exemplars/clusters, however they may be degenerate and should be used with caution.

When all training samples have equal similarities and equal preferences, the assignment of cluster centers and labels depends on the preference. If the preference is smaller than the similarities, a single cluster center and label `0` for every sample will be returned. Otherwise, every training sample becomes its own cluster center and is assigned a unique label.

References

Brendan J. Frey and Delbert Dueck, “Clustering by Passing Messages Between Data Points”, Science Feb. 2007

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import affinity\_propagation
\>>> from sklearn.metrics.pairwise import euclidean\_distances
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[4, 2\], \[4, 4\], \[4, 0\]\])
\>>> S \= \-euclidean\_distances(X, squared\=True)
\>>> cluster\_centers\_indices, labels \= affinity\_propagation(S, random\_state\=0)
\>>> cluster\_centers\_indices
array(\[0, 3\])
\>>> labels
array(\[0, 0, 0, 1, 1, 1\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)