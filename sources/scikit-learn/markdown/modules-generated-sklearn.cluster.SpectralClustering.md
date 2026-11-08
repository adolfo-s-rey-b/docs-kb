[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.SpectralClustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.SpectralClustering.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.SpectralClustering.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.SpectralClustering.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.SpectralClustering.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.SpectralClustering.html)

Collapse Sidebar Expand Sidebar

SpectralClustering[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#spectralclustering "Link to this heading")

===========================================================================================================================================================

class sklearn.cluster.SpectralClustering(_n\_clusters\=8_, _\*_, _eigen\_solver\=None_, _n\_components\=None_, _random\_state\=None_, _n\_init\=10_, _gamma\=1.0_, _affinity\='rbf'_, _n\_neighbors\=10_, _eigen\_tol\='auto'_, _assign\_labels\='kmeans'_, _degree\=3_, _coef0\=1_, _kernel\_params\=None_, _n\_jobs\=None_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_spectral.py#L380)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "Link to this definition")

Apply clustering to a projection of the normalized Laplacian.

In practice Spectral Clustering is very useful when the structure of the individual clusters is highly non-convex, or more generally when a measure of the center and spread of the cluster is not a suitable description of the complete cluster, such as when clusters are nested circles on the 2D plane.

If the affinity matrix is the adjacency matrix of a graph, this method can be used to find normalized graph cuts [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#r5f6cbeb1558e-1)
, [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#r5f6cbeb1558e-2)
.

When calling `fit`, an affinity matrix is constructed using either a kernel function such the Gaussian (aka RBF) kernel with Euclidean distance `d(X, X)`:

np.exp(\-gamma \* d(X,X) \*\* 2)

Copy to clipboard

or a k-nearest neighbors connectivity matrix.

Alternatively, a user-provided affinity matrix can be specified by setting `affinity='precomputed'`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering)
.

Parameters:

**n\_clusters**int, default=8

Number of clusters to extract.

**eigen\_solver**{‘arpack’, ‘lobpcg’, ‘amg’}, default=None

The eigenvalue decomposition strategy to use. AMG requires pyamg to be installed. It can be faster on very large, sparse problems, but may also lead to instabilities. If None, then `'arpack'` is used. See [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#r5f6cbeb1558e-4)
 for more details regarding `'lobpcg'`.

**n\_components**int, default=None

Number of eigenvectors to use for the spectral embedding. If None, defaults to `n_clusters`.

**random\_state**int, RandomState instance, default=None

A pseudo random number generator used for the initialization of the lobpcg eigenvectors decomposition when `eigen_solver == 'amg'`, and for the K-Means initialization. Use an int to make the results deterministic across calls (See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
).

Note

When using `eigen_solver == 'amg'`, it is necessary to also fix the global numpy seed with `np.random.seed(int)` to get deterministic results. See [pyamg/pyamg#139](https://github.com/pyamg/pyamg/issues/139)
 for further information.

**n\_init**int, default=10

Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n\_init consecutive runs in terms of inertia. Only used if `assign_labels='kmeans'`.

**gamma**float, default=1.0

Kernel coefficient for rbf, poly, sigmoid, laplacian and chi2 kernels. Ignored for `affinity='nearest_neighbors'`, `affinity='precomputed'` or `affinity='precomputed_nearest_neighbors'`.

**affinity**str or callable, default=’rbf’

How to construct the affinity matrix.

*   ‘nearest\_neighbors’: construct the affinity matrix by computing a graph of nearest neighbors.
    
*   ‘rbf’: construct the affinity matrix using a radial basis function (RBF) kernel.
    
*   ‘precomputed’: interpret `X` as a precomputed affinity matrix, where larger values indicate greater similarity between instances.
    
*   ‘precomputed\_nearest\_neighbors’: interpret `X` as a sparse graph of precomputed distances, and construct a binary affinity matrix from the `n_neighbors` nearest neighbors of each instance.
    
*   one of the kernels supported by [`pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
    .
    

Only kernels that produce similarity scores (non-negative values that increase with similarity) should be used. This property is not checked by the clustering algorithm.

**n\_neighbors**int, default=10

Number of neighbors to use when constructing the affinity matrix using the nearest neighbors method. Ignored for `affinity='rbf'`.

**eigen\_tol**float, default=”auto”

Stopping criterion for eigen decomposition of the Laplacian matrix. If `eigen_tol="auto"` then the passed tolerance will depend on the `eigen_solver`:

*   If `eigen_solver="arpack"`, then `eigen_tol=0.0`;
    
*   If `eigen_solver="lobpcg"` or `eigen_solver="amg"`, then `eigen_tol=None` which configures the underlying `lobpcg` solver to automatically resolve the value according to their heuristics. See, [`scipy.sparse.linalg.lobpcg`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lobpcg.html#scipy.sparse.linalg.lobpcg "(in SciPy v1.18.0)")
     for details.
    

Note that when using `eigen_solver="lobpcg"` or `eigen_solver="amg"` values of `tol<1e-5` may lead to convergence issues and should be avoided.

Added in version 1.2: Added ‘auto’ option.

**assign\_labels**{‘kmeans’, ‘discretize’, ‘cluster\_qr’}, default=’kmeans’

The strategy for assigning labels in the embedding space. There are two ways to assign labels after the Laplacian embedding. k-means is a popular choice, but it can be sensitive to initialization. Discretization is another approach which is less sensitive to random initialization [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#r5f6cbeb1558e-3)
. The cluster\_qr method [\[5\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#r5f6cbeb1558e-5)
 directly extract clusters from eigenvectors in spectral clustering. In contrast to k-means and discretization, cluster\_qr has no tuning parameters and runs no iterations, yet may outperform k-means and discretization in terms of both quality and speed.

Changed in version 1.1: Added new labeling method ‘cluster\_qr’.

**degree**float, default=3

Degree of the polynomial kernel. Ignored by other kernels.

**coef0**float, default=1

Zero coefficient for polynomial and sigmoid kernels. Ignored by other kernels.

**kernel\_params**dict of str to any, default=None

Parameters (keyword arguments) and values for kernel passed as callable object. Ignored by other kernels.

**n\_jobs**int, default=None

The number of parallel jobs to run when `affinity='nearest_neighbors'` or `affinity='precomputed_nearest_neighbors'`. The neighbors search will be done in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**bool, default=False

Verbosity mode.

Added in version 0.24.

Attributes:

**affinity\_matrix\_**array-like of shape (n\_samples, n\_samples)

Affinity matrix used for clustering. Available only after calling `fit`.

**labels\_**ndarray of shape (n\_samples,)

Labels of each point

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`sklearn.cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

K-Means clustering.

[`sklearn.cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")

Density-Based Spatial Clustering of Applications with Noise.

Notes

A distance matrix for which 0 indicates identical elements and high values indicate very dissimilar elements can be transformed into an affinity / similarity matrix that is well-suited for the algorithm by applying the Gaussian (aka RBF, heat) kernel:

np.exp(\- dist\_matrix \*\* 2 / (2. \* delta \*\* 2))

Copy to clipboard

where `delta` is a free parameter representing the width of the Gaussian kernel.

An alternative is to take a symmetric version of the k-nearest neighbors connectivity matrix of the points.

If the pyamg package is installed, it is used: this greatly speeds up computation.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#id1)\
\]

[Normalized cuts and image segmentation, 2000 Jianbo Shi, Jitendra Malik](https://doi.org/10.1109/34.868688)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#id2)\
\]

[A Tutorial on Spectral Clustering, 2007 Ulrike von Luxburg](https://doi.org/10.1007/s11222-007-9033-z)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#id4)\
\]

[Multiclass spectral clustering, 2003 Stella X. Yu, Jianbo Shi](https://people.eecs.berkeley.edu/~jordan/courses/281B-spring04/readings/yu-shi.pdf)

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#id3)\
\]

[Toward the Optimal Preconditioned Eigensolver: Locally Optimal Block Preconditioned Conjugate Gradient Method, 2001 A. V. Knyazev SIAM Journal on Scientific Computing 23, no. 2, pp. 517-541.](https://doi.org/10.1137/S1064827500366124)

\[[5](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#id5)\
\]

[Simple, direct, and efficient multi-way spectral clustering, 2019 Anil Damle, Victor Minden, Lexing Ying](https://doi.org/10.1093/imaiai/iay008)

Examples

\>>> from sklearn.cluster import SpectralClustering
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> clustering \= SpectralClustering(n\_clusters\=2,
...         assign\_labels\='discretize',
...         random\_state\=0).fit(X)
\>>> clustering.labels\_
array(\[1, 1, 1, 0, 0, 0\])
\>>> clustering
SpectralClustering(assign\_labels='discretize', n\_clusters=2,
    random\_state=0)

Copy to clipboard

For a comparison of Spectral clustering with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_spectral.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering.fit "Link to this definition")

Perform spectral clustering from features, or affinity matrix.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Training instances to cluster, similarities / affinities between instances if `affinity='precomputed'`, or distances between instances if `affinity='precomputed_nearest_neighbors`. If a sparse matrix is provided in a format other than `csr_matrix`, `csc_matrix`, or `coo_matrix`, it will be converted into a sparse `csr_matrix`.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

A fitted instance of the estimator.

fit\_predict(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_spectral.py#L775)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering.fit_predict "Link to this definition")

Perform spectral clustering on `X` and return cluster labels.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Training instances to cluster, similarities / affinities between instances if `affinity='precomputed'`, or distances between instances if `affinity='precomputed_nearest_neighbors`. If a sparse matrix is provided in a format other than `csr_matrix`, `csc_matrix`, or `coo_matrix`, it will be converted into a sparse `csr_matrix`.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**labels**ndarray of shape (n\_samples,)

Cluster labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)