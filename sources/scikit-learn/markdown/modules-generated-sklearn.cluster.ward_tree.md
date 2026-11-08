[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.ward_tree.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.ward_tree.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.ward_tree.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.ward_tree.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.ward_tree.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.ward_tree.html)

Collapse Sidebar Expand Sidebar

ward\_tree[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#ward-tree "Link to this heading")

=================================================================================================================================

sklearn.cluster.ward\_tree(_X_, _\*_, _connectivity\=None_, _n\_clusters\=None_, _return\_distance\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_agglomerative.py#L183)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#sklearn.cluster.ward_tree "Link to this definition")

Ward clustering based on a Feature matrix.

Recursively merges the pair of clusters that minimally increases within-cluster variance.

The inertia matrix uses a Heapq-based representation.

This is the structured version, that takes into account some topological structure between samples.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Feature matrix representing `n_samples` samples to be clustered.

**connectivity**{array-like, sparse matrix}, default=None

Connectivity matrix. Defines for each sample the neighboring samples following a given structure of the data. The matrix is assumed to be symmetric and only the upper triangular half is used. Default is None, i.e, the Ward algorithm is unstructured.

**n\_clusters**int, default=None

`n_clusters` should be less than `n_samples`. Stop early the construction of the tree at `n_clusters.` This is useful to decrease computation time if the number of clusters is not small compared to the number of samples. In this case, the complete tree is not computed, thus the ‘children’ output is of limited use, and the ‘parents’ output should rather be used. This option is valid only when specifying a connectivity matrix.

**return\_distance**bool, default=False

If `True`, return the distance between the clusters.

Returns:

**children**ndarray of shape (n\_nodes-1, 2)

The children of each non-leaf node. Values less than `n_samples` correspond to leaves of the tree which are the original samples. A node `i` greater than or equal to `n_samples` is a non-leaf node and has children `children_[i - n_samples]`. Alternatively at the i-th iteration, children\[i\]\[0\] and children\[i\]\[1\] are merged to form node `n_samples + i`.

**n\_connected\_components**int

The number of connected components in the graph.

**n\_leaves**int

The number of leaves in the tree.

**parents**ndarray of shape (n\_nodes,) or None

The parent of each node. Only returned when a connectivity matrix is specified, elsewhere ‘None’ is returned.

**distances**ndarray of shape (n\_nodes-1,)

Only returned if `return_distance` is set to `True` (for compatibility). The distances between the centers of the nodes. `distances[i]` corresponds to a weighted Euclidean distance between the nodes `children[i, 1]` and `children[i, 2]`. If the nodes refer to leaves of the tree, then `distances[i]` is their unweighted Euclidean distance. Distances are updated in the following way (from scipy.hierarchy.linkage):

The new entry d(u,v) is computed as follows,

d(u,v)\=|v|+|s|Td(v,s)2+|v|+|t|Td(v,t)2−|v|Td(s,t)2

where u is the newly joined cluster consisting of clusters s and t, v is an unused cluster in the forest, T\=|v|+|s|+|t|, and |∗| is the cardinality of its argument. This is also known as the incremental algorithm.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import ward\_tree
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[4, 2\], \[4, 4\], \[4, 0\]\])
\>>> children, n\_connected\_components, n\_leaves, parents \= ward\_tree(X)
\>>> children
array(\[\[0, 1\],\
       \[3, 5\],\
       \[2, 6\],\
       \[4, 7\],\
       \[8, 9\]\])
\>>> n\_connected\_components
1
\>>> n\_leaves
6

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)