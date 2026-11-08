[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.spectral_clustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.spectral_clustering.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.spectral_clustering.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.spectral_clustering.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.spectral_clustering.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.spectral_clustering.html)

Collapse Sidebar Expand Sidebar

spectral\_clustering[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#spectral-clustering "Link to this heading")

===============================================================================================================================================================

sklearn.cluster.spectral\_clustering(_affinity_, _\*_, _n\_clusters\=8_, _n\_components\=None_, _eigen\_solver\=None_, _random\_state\=None_, _n\_init\=10_, _eigen\_tol\='auto'_, _assign\_labels\='kmeans'_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_spectral.py#L190)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "Link to this definition")

Apply clustering to a projection of the normalized Laplacian.

In practice Spectral Clustering is very useful when the structure of the individual clusters is highly non-convex or more generally when a measure of the center and spread of the cluster is not a suitable description of the complete cluster. For instance, when clusters are nested circles on the 2D plane.

If affinity is the adjacency matrix of a graph, this method can be used to find normalized graph cuts [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-1)
, [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-2)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering)
.

Parameters:

**affinity**{array-like, sparse matrix} of shape (n\_samples, n\_samples)

The affinity matrix describing the relationship of the samples to embed. **Must be symmetric**.

Possible examples:

*   adjacency matrix of a graph,
    
*   heat kernel of the pairwise distance matrix of the samples,
    
*   symmetric k-nearest neighbours connectivity matrix of the samples.
    

**n\_clusters**int, default=8

Number of clusters to extract.

**n\_components**int, default=None

Number of eigenvectors to use for the spectral embedding. If None, defaults to `n_clusters`.

**eigen\_solver**{None, ‘arpack’, ‘lobpcg’, or ‘amg’}

The eigenvalue decomposition method. If None then `'arpack'` is used. See [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-4)
 for more details regarding `'lobpcg'`. Eigensolver `'amg'` runs `'lobpcg'` with optional Algebraic MultiGrid preconditioning and requires pyamg to be installed. It can be faster on very large sparse problems [\[6\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-6)
 and [\[7\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-7)
.

**random\_state**int, RandomState instance, default=None

A pseudo random number generator used for the initialization of the lobpcg eigenvectors decomposition when `eigen_solver == 'amg'`, and for the K-Means initialization. Use an int to make the results deterministic across calls (See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
).

Note

When using `eigen_solver == 'amg'`, it is necessary to also fix the global numpy seed with `np.random.seed(int)` to get deterministic results. See [pyamg/pyamg#139](https://github.com/pyamg/pyamg/issues/139)
 for further information.

**n\_init**int, default=10

Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n\_init consecutive runs in terms of inertia. Only used if `assign_labels='kmeans'`.

**eigen\_tol**float, default=”auto”

Stopping criterion for eigendecomposition of the Laplacian matrix. If `eigen_tol="auto"` then the passed tolerance will depend on the `eigen_solver`:

*   If `eigen_solver="arpack"`, then `eigen_tol=0.0`;
    
*   If `eigen_solver="lobpcg"` or `eigen_solver="amg"`, then `eigen_tol=None` which configures the underlying `lobpcg` solver to automatically resolve the value according to their heuristics. See, [`scipy.sparse.linalg.lobpcg`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lobpcg.html#scipy.sparse.linalg.lobpcg "(in SciPy v1.18.0)")
     for details.
    

Note that when using `eigen_solver="lobpcg"` or `eigen_solver="amg"` values of `tol<1e-5` may lead to convergence issues and should be avoided.

Added in version 1.2: Added ‘auto’ option.

**assign\_labels**{‘kmeans’, ‘discretize’, ‘cluster\_qr’}, default=’kmeans’

The strategy to use to assign labels in the embedding space. There are three ways to assign labels after the Laplacian embedding. k-means can be applied and is a popular choice. But it can also be sensitive to initialization. Discretization is another approach which is less sensitive to random initialization [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-3)
. The cluster\_qr method [\[5\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#r89dec4780971-5)
 directly extracts clusters from eigenvectors in spectral clustering. In contrast to k-means and discretization, cluster\_qr has no tuning parameters and is not an iterative method, yet may outperform k-means and discretization in terms of both quality and speed. For a detailed comparison of clustering strategies, refer to the following example: [Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html#sphx-glr-auto-examples-cluster-plot-coin-segmentation-py)
.

Changed in version 1.1: Added new labeling method ‘cluster\_qr’.

**verbose**bool, default=False

Verbosity mode.

Added in version 0.24.

Returns:

**labels**array of integers, shape: n\_samples

The labels of the clusters.

Notes

The graph should contain only one connected component, elsewhere the results make little sense.

This algorithm solves the normalized cut for `k=2`: it is a normalized spectral clustering.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id1)\
\]

[Normalized cuts and image segmentation, 2000 Jianbo Shi, Jitendra Malik](https://doi.org/10.1109/34.868688)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id2)\
\]

[A Tutorial on Spectral Clustering, 2007 Ulrike von Luxburg](https://doi.org/10.1007/s11222-007-9033-z)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id6)\
\]

[Multiclass spectral clustering, 2003 Stella X. Yu, Jianbo Shi](https://people.eecs.berkeley.edu/~jordan/courses/281B-spring04/readings/yu-shi.pdf)

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id3)\
\]

[Toward the Optimal Preconditioned Eigensolver: Locally Optimal Block Preconditioned Conjugate Gradient Method, 2001 A. V. Knyazev SIAM Journal on Scientific Computing 23, no. 2, pp. 517-541.](https://doi.org/10.1137/S1064827500366124)

\[[5](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id7)\
\]

[Simple, direct, and efficient multi-way spectral clustering, 2019 Anil Damle, Victor Minden, Lexing Ying](https://doi.org/10.1093/imaiai/iay008)

\[[6](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id4)\
\]

[Multiscale Spectral Image Segmentation Multiscale preconditioning for computing eigenvalues of graph Laplacians in image segmentation, 2006 Andrew Knyazev](https://doi.org/10.13140/RG.2.2.35280.02565)

\[[7](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#id5)\
\]

[Preconditioned spectral clustering for stochastic block partition streaming graph challenge (Preliminary version at arXiv.) David Zhuzhunashvili, Andrew Knyazev](https://doi.org/10.1109/HPEC.2017.8091045)

Examples

\>>> import numpy as np
\>>> from sklearn.metrics.pairwise import pairwise\_kernels
\>>> from sklearn.cluster import spectral\_clustering
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> affinity \= pairwise\_kernels(X, metric\='rbf')
\>>> spectral\_clustering(
...     affinity\=affinity, n\_clusters\=2, assign\_labels\="discretize", random\_state\=0
... )
array(\[1, 1, 1, 0, 0, 0\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_segmentation_toy_thumb.png)

[Spectral clustering for image segmentation](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html)

Spectral clustering for image segmentation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)