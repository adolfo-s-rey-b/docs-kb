[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.MiniBatchKMeans.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.MiniBatchKMeans.html)

Collapse Sidebar Expand Sidebar

MiniBatchKMeans[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#minibatchkmeans "Link to this heading")

==================================================================================================================================================

class sklearn.cluster.MiniBatchKMeans(_n\_clusters\=8_, _\*_, _init\='k-means++'_, _max\_iter\=100_, _batch\_size\=1024_, _verbose\=0_, _compute\_labels\=True_, _random\_state\=None_, _tol\=0.0_, _max\_no\_improvement\=10_, _init\_size\=None_, _n\_init\='auto'_, _reassignment\_ratio\=0.01_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1680)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "Link to this definition")

Mini-Batch K-Means clustering.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#mini-batch-kmeans)
.

Parameters:

**n\_clusters**int, default=8

The number of clusters to form as well as the number of centroids to generate.

**init**{‘k-means++’, ‘random’}, callable or array-like of shape (n\_clusters, n\_features), default=’k-means++’

Method for initialization:

‘k-means++’ : selects initial cluster centroids using sampling based on an empirical probability distribution of the points’ contribution to the overall inertia. This technique speeds up convergence. The algorithm implemented is “greedy k-means++”. It differs from the vanilla k-means++ by making several trials at each sampling step and choosing the best centroid among them.

‘random’: choose `n_clusters` observations (rows) at random from data for the initial centroids.

If an array is passed, it should be of shape (n\_clusters, n\_features) and gives the initial centers.

If a callable is passed, it should take arguments X, n\_clusters and a random state and return an initialization.

For an evaluation of the impact of initialization, see the example [Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html#sphx-glr-auto-examples-cluster-plot-kmeans-stability-low-dim-dense-py)
.

**max\_iter**int, default=100

Maximum number of iterations over the complete dataset before stopping independently of any early stopping criterion heuristics.

**batch\_size**int, default=1024

Size of the mini batches. For faster computations, you can set `batch_size > 256 * number_of_cores` to enable [parallelism](https://scikit-learn.org/stable/computing/parallelism.html#lower-level-parallelism-with-openmp)
 on all cores.

Changed in version 1.0: `batch_size` default changed from 100 to 1024.

**verbose**int, default=0

Verbosity mode.

**compute\_labels**bool, default=True

Compute label assignment and inertia for the complete dataset once the minibatch optimization has converged in fit.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for centroid initialization and random reassignment. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**tol**float, default=0.0

Control early stopping based on the relative center changes as measured by a smoothed, variance-normalized of the mean center squared position changes. This early stopping heuristics is closer to the one used for the batch variant of the algorithms but induces a slight computational and memory overhead over the inertia heuristic.

To disable convergence detection based on normalized center change, set tol to 0.0 (default).

**max\_no\_improvement**int, default=10

Control early stopping based on the consecutive number of mini batches that does not yield an improvement on the smoothed inertia.

To disable convergence detection based on inertia, set max\_no\_improvement to None.

**init\_size**int, default=None

Number of samples to randomly sample for speeding up the initialization (sometimes at the expense of accuracy): the only algorithm is initialized by running a batch KMeans on a random subset of the data. This needs to be larger than n\_clusters.

If `None`, the heuristic is `init_size = 3 * batch_size` if `3 * batch_size < n_clusters`, else `init_size = 3 * n_clusters`.

**n\_init**‘auto’ or int, default=”auto”

Number of random initializations that are tried. In contrast to KMeans, the algorithm is only run once, using the best of the `n_init` initializations as measured by inertia. Several runs are recommended for sparse high-dimensional problems (see [Clustering sparse data with k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#kmeans-sparse-high-dim)
).

When `n_init='auto'`, the number of runs depends on the value of init: 3 if using `init='random'` or `init` is a callable; 1 if using `init='k-means++'` or `init` is an array-like.

Added in version 1.2: Added ‘auto’ option for `n_init`.

Changed in version 1.4: Default value for `n_init` changed to `'auto'` in version.

**reassignment\_ratio**float, default=0.01

Control the fraction of the maximum number of counts for a center to be reassigned. A higher value means that low count centers are more easily reassigned, which means that the model will take longer to converge, but should converge in a better clustering. However, too high a value may cause convergence issues, especially with a small batch size.

Attributes:

**cluster\_centers\_**ndarray of shape (n\_clusters, n\_features)

Coordinates of cluster centers.

**labels\_**ndarray of shape (n\_samples,)

Labels of each point (if compute\_labels is set to True).

**inertia\_**float

The value of the inertia criterion associated with the chosen partition if compute\_labels is set to True. If compute\_labels is set to False, it’s an approximation of the inertia based on an exponentially weighted average of the batch inertiae. The inertia is defined as the sum of square distances of samples to their cluster center, weighted by the sample weights if provided.

**n\_iter\_**int

Number of iterations over the full dataset.

**n\_steps\_**int

Number of minibatches processed.

Added in version 1.0.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

The classic implementation of the clustering method based on the Lloyd’s algorithm. It consumes the whole set of input data at each iteration.

Notes

See [https://www.eecs.tufts.edu/~dsculley/papers/fastkmeans.pdf](https://www.eecs.tufts.edu/~dsculley/papers/fastkmeans.pdf)

When there are too few points in the dataset, some centers may be duplicated, which means that a proper clustering in terms of the number of requesting clusters and the number of returned clusters will not always match. One solution is to set `reassignment_ratio=0`, which prevents reassignments of clusters that are too small.

See [Compare BIRCH and MiniBatchKMeans](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html#sphx-glr-auto-examples-cluster-plot-birch-vs-minibatchkmeans-py)
 for a comparison with `BIRCH`.

Examples

\>>> from sklearn.cluster import MiniBatchKMeans
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[4, 2\], \[4, 0\], \[4, 4\],\
...               \[4, 5\], \[0, 1\], \[2, 2\],\
...               \[3, 2\], \[5, 5\], \[1, \-1\]\])
\>>> \# manually fit on batches
\>>> kmeans \= MiniBatchKMeans(n\_clusters\=2,
...                          random\_state\=0,
...                          batch\_size\=6,
...                          n\_init\="auto")
\>>> kmeans \= kmeans.partial\_fit(X\[0:6,:\])
\>>> kmeans \= kmeans.partial\_fit(X\[6:12,:\])
\>>> kmeans.cluster\_centers\_
array(\[\[3.375, 3.  \],\
       \[0.75 , 0.5 \]\])
\>>> kmeans.predict(\[\[0, 0\], \[4, 4\]\])
array(\[1, 0\], dtype=int32)
\>>> \# fit on the whole data
\>>> kmeans \= MiniBatchKMeans(n\_clusters\=2,
...                          random\_state\=0,
...                          batch\_size\=6,
...                          max\_iter\=10,
...                          n\_init\="auto").fit(X)
\>>> kmeans.cluster\_centers\_
array(\[\[3.20967742, 3.56451613\],\
       \[1.32758621, 0.77586207\]\])
\>>> kmeans.predict(\[\[0, 0\], \[4, 4\]\])
array(\[1, 0\], dtype=int32)

Copy to clipboard

For a comparison of Mini-Batch K-Means clustering with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L2048)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.fit "Link to this definition")

Compute the centroids on X by chunking it into mini-batches.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training instances to cluster. It must be noted that the data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous. If a sparse matrix is passed, a copy will be made if it’s not in CSR format.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in X. If None, all observations are assigned equal weight. `sample_weight` is not used during initialization if `init` is a callable or a user provided array.

Added in version 0.20.

Returns:

**self**object

Fitted estimator.

fit\_predict(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.fit_predict "Link to this definition")

Compute cluster centers and predict cluster index for each sample.

Convenience method; equivalent to calling fit(X) followed by predict(X).

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data to transform.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in X. If None, all observations are assigned equal weight.

Returns:

**labels**ndarray of shape (n\_samples,)

Index of the cluster each sample belongs to.

fit\_transform(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1105)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.fit_transform "Link to this definition")

Compute clustering and transform X to cluster-distance space.

Equivalent to fit(X).transform(X), but more efficiently implemented.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data to transform.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in X. If None, all observations are assigned equal weight.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_clusters)

X transformed in the new space.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L2219)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.partial_fit "Link to this definition")

Update k means estimate on a single mini-batch X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training instances to cluster. It must be noted that the data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous. If a sparse matrix is passed, a copy will be made if it’s not in CSR format.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in X. If None, all observations are assigned equal weight. `sample_weight` is not used during initialization if `init` is a callable or a user provided array.

Returns:

**self**object

Return updated estimator.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1071)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.predict "Link to this definition")

Predict the closest cluster each sample in X belongs to.

In the vector quantization literature, `cluster_centers_` is called the code book and each value returned by `predict` is the index of the closest code in the code book.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data to predict.

Returns:

**labels**ndarray of shape (n\_samples,)

Index of the cluster each sample belongs to.

score(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1155)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.score "Link to this definition")

Opposite of the value of X on the K-means objective.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in X. If None, all observations are assigned equal weight.

Returns:

**score**float

Opposite of the value of X on the K-means objective.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster._kmeans.MiniBatchKMeans")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_partial\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster._kmeans.MiniBatchKMeans")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.set_partial_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `partial_fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `partial_fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `partial_fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `partial_fit`.

Returns:

**self**object

The updated object.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster._kmeans.MiniBatchKMeans")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.set_score_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `score` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `score`.

Returns:

**self**object

The updated object.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1129)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.transform "Link to this definition")

Transform X to a cluster-distance space.

In the new space, each dimension is the distance to the cluster centers. Note that even if X is sparse, the array returned by `transform` will typically be dense.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data to transform.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_clusters)

X transformed in the new space.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_birch_vs_minibatchkmeans_thumb.png)

[Compare BIRCH and MiniBatchKMeans](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)

Compare BIRCH and MiniBatchKMeans

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)