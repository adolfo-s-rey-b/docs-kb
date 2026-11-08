[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.Isomap.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.Isomap.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.Isomap.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.Isomap.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.Isomap.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.Isomap.html)

Collapse Sidebar Expand Sidebar

Isomap[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#isomap "Link to this heading")

========================================================================================================================

class sklearn.manifold.Isomap(_\*_, _n\_neighbors\=5_, _radius\=None_, _n\_components\=2_, _eigen\_solver\='auto'_, _tol\=0_, _max\_iter\=None_, _path\_method\='auto'_, _neighbors\_algorithm\='auto'_, _n\_jobs\=None_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_isomap.py#L29)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "Link to this definition")

Isomap Embedding.

Non-linear dimensionality reduction through Isometric Mapping

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#isomap)
.

Parameters:

**n\_neighbors**int or None, default=5

Number of neighbors to consider for each point. If `n_neighbors` is an int, then `radius` must be `None`.

**radius**float or None, default=None

Limiting distance of neighbors to return. If `radius` is a float, then `n_neighbors` must be set to `None`.

Added in version 1.1.

**n\_components**int, default=2

Number of coordinates for the manifold.

**eigen\_solver**{‘auto’, ‘arpack’, ‘dense’}, default=’auto’

‘auto’ : Attempt to choose the most efficient solver for the given problem.

‘arpack’ : Use Arnoldi decomposition to find the eigenvalues and eigenvectors.

‘dense’ : Use a direct solver (i.e. LAPACK) for the eigenvalue decomposition.

**tol**float, default=0

Convergence tolerance passed to arpack or lobpcg. not used if eigen\_solver == ‘dense’.

**max\_iter**int, default=None

Maximum number of iterations for the arpack solver. not used if eigen\_solver == ‘dense’.

**path\_method**{‘auto’, ‘FW’, ‘D’}, default=’auto’

Method to use in finding shortest path.

‘auto’ : attempt to choose the best algorithm automatically.

‘FW’ : Floyd-Warshall algorithm.

‘D’ : Dijkstra’s algorithm.

**neighbors\_algorithm**{‘auto’, ‘brute’, ‘kd\_tree’, ‘ball\_tree’}, default=’auto’

Algorithm to use for nearest neighbors search, passed to neighbors.NearestNeighbors instance.

**n\_jobs**int or None, default=None

The number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**metric**str, or callable, default=”minkowski”

The metric to use when calculating distance between instances in a feature array. If metric is a string or callable, it must be one of the options allowed by [`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
 for its metric parameter. If metric is “precomputed”, X is assumed to be a distance matrix and must be square. X may be a [Glossary](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
.

Added in version 0.22.

**p**float, default=2

Parameter for the Minkowski metric from sklearn.metrics.pairwise.pairwise\_distances. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used.

Added in version 0.22.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

Added in version 0.22.

Attributes:

**embedding\_**array-like, shape (n\_samples, n\_components)

Stores the embedding vectors.

**kernel\_pca\_**object

[`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
 object used to implement the embedding.

**nbrs\_**sklearn.neighbors.NearestNeighbors instance

Stores nearest neighbors instance, including BallTree or KDtree if applicable.

**dist\_matrix\_**array-like, shape (n\_samples, n\_samples)

Stores the geodesic distance matrix of training data.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis that is a linear dimensionality reduction method.

[`sklearn.decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

Non-linear dimensionality reduction using kernels and PCA.

[`MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")

Manifold learning using multidimensional scaling.

[`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")

T-distributed Stochastic Neighbor Embedding.

[`LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")

Manifold learning using Locally Linear Embedding.

[`SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")

Spectral embedding for non-linear dimensionality.

References

\[1\]

Tenenbaum, J.B.; De Silva, V.; & Langford, J.C. A global geometric framework for nonlinear dimensionality reduction. Science 290 (5500)

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.manifold import Isomap
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X.shape
(1797, 64)
\>>> embedding \= Isomap(n\_components\=2)
\>>> X\_transformed \= embedding.fit\_transform(X\[:100\])
\>>> X\_transformed.shape
(100, 2)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_isomap.py#L340)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.fit "Link to this definition")

Compute the embedding vectors for data X.

Parameters:

**X**{array-like, sparse matrix, BallTree, KDTree, NearestNeighbors}

Sample data, shape = (n\_samples, n\_features), in the form of a numpy array, sparse matrix, precomputed tree, or NearestNeighbors object.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns a fitted instance of self.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_isomap.py#L365)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.fit_transform "Link to this definition")

Fit the model from data in X and transform X.

Parameters:

**X**{array-like, sparse matrix, BallTree, KDTree}

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**X\_new**array-like, shape (n\_samples, n\_components)

X transformed in the new space.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

reconstruction\_error()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_isomap.py#L315)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.reconstruction_error "Link to this definition")

Compute the reconstruction error for the embedding.

Returns:

**reconstruction\_error**float

Reconstruction error.

Notes

The cost function of an isomap embedding is

`E = frobenius_norm[K(D) - K(D_fit)] / n_samples`

Where D is the matrix of distances for the input data X, D\_fit is the matrix of distances for the output embedding X\_fit, and K is the isomap kernel:

`K(D) = -0.5 * (I - 1/n_samples) * D^2 * (I - 1/n_samples)`

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_isomap.py#L389)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.transform "Link to this definition")

Transform X.

This is implemented by linking the points X into the graph of geodesic distances of the training data. First the `n_neighbors` nearest neighbors of X are found in the training data, and from these the shortest geodesic distances from each point in X to each point in the training data are computed in order to construct the kernel. The embedding of X is the projection of this kernel onto the embedding vectors of the training set.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_queries, n\_features)

If neighbors\_algorithm=’precomputed’, X is assumed to be a distance matrix or a sparse graph of shape (n\_queries, n\_samples\_fit).

Returns:

**X\_new**array-like, shape (n\_queries, n\_components)

X transformed in the new space.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)