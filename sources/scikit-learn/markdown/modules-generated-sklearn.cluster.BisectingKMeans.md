[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.BisectingKMeans.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.BisectingKMeans.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.BisectingKMeans.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.BisectingKMeans.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.BisectingKMeans.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.BisectingKMeans.html)

Collapse Sidebar Expand Sidebar

BisectingKMeans[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#bisectingkmeans "Link to this heading")

==================================================================================================================================================

class sklearn.cluster.BisectingKMeans(_n\_clusters\=8_, _\*_, _init\='random'_, _n\_init\=1_, _random\_state\=None_, _max\_iter\=300_, _verbose\=0_, _tol\=0.0001_, _copy\_x\=True_, _algorithm\='lloyd'_, _bisecting\_strategy\='biggest\_inertia'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bisect_k_means.py#L83)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "Link to this definition")

Bisecting K-Means clustering.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#bisect-k-means)
.

Added in version 1.1.

Parameters:

**n\_clusters**int, default=8

The number of clusters to form as well as the number of centroids to generate.

**init**{‘k-means++’, ‘random’} or callable, default=’random’

Method for initialization for each bisection.

‘k-means++’ : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. See section Notes in k\_init for more details.

‘random’: choose `n_clusters` observations (rows) at random from data for the initial centroids.

If a callable is passed, it should take arguments X, n\_clusters and a random state and return an initialization. Note that the bisecting algorithm always performs a 2-way split, so the callable will always be called with `n_clusters=2` and should return 2 centroids.

**n\_init**int, default=1

Number of time the inner k-means algorithm will be run with different centroid seeds in each bisection. That will result producing for each bisection best output of n\_init consecutive runs in terms of inertia.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for centroid initialization in inner K-Means. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**max\_iter**int, default=300

Maximum number of iterations of the inner k-means algorithm at each bisection.

**verbose**int, default=0

Verbosity mode.

**tol**float, default=1e-4

Relative tolerance with regards to Frobenius norm of the difference in the cluster centers of two consecutive iterations to declare convergence. Used in inner k-means algorithm at each bisection to pick best possible clusters.

**copy\_x**bool, default=True

When pre-computing distances it is more numerically accurate to center the data first. If copy\_x is True (default), then the original data is not modified. If False, the original data is modified, and put back before the function returns, but small numerical differences may be introduced by subtracting and then adding the data mean. Note that if the original data is not C-contiguous, a copy will be made even if copy\_x is False. If the original data is sparse, but not in CSR format, a copy will be made even if copy\_x is False.

**algorithm**{“lloyd”, “elkan”}, default=”lloyd”

Inner K-means algorithm used in bisection. The classical EM-style algorithm is `"lloyd"`. The `"elkan"` variation can be more efficient on some datasets with well-defined clusters, by using the triangle inequality. However it’s more memory intensive due to the allocation of an extra array of shape `(n_samples, n_clusters)`.

**bisecting\_strategy**{“biggest\_inertia”, “largest\_cluster”}, default=”biggest\_inertia”

Defines how bisection should be performed:

*   “biggest\_inertia” means that BisectingKMeans will always check all calculated cluster for cluster with biggest SSE (Sum of squared errors) and bisect it. This approach concentrates on precision, but may be costly in terms of execution time (especially for larger amount of data points).
    
*   “largest\_cluster” - BisectingKMeans will always split cluster with largest amount of points assigned to it from all clusters previously calculated. That should work faster than picking by SSE (‘biggest\_inertia’) and may produce similar results in most cases.
    

Attributes:

**cluster\_centers\_**ndarray of shape (n\_clusters, n\_features)

Coordinates of cluster centers. If the algorithm stops before fully converging (see `tol` and `max_iter`), these will not be consistent with `labels_`.

**labels\_**ndarray of shape (n\_samples,)

Labels of each point.

**inertia\_**float

Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

See also

[`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

Original implementation of K-Means algorithm.

Notes

It might be inefficient when n\_cluster is less than 3, due to unnecessary calculations for that case.

Examples

\>>> from sklearn.cluster import BisectingKMeans
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[10, 1\], \[3, 1\],\
...               \[10, 0\], \[2, 1\], \[10, 2\],\
...               \[10, 8\], \[10, 9\], \[10, 10\]\])
\>>> bisect\_means \= BisectingKMeans(n\_clusters\=3, random\_state\=0).fit(X)
\>>> bisect\_means.labels\_
array(\[0, 2, 0, 2, 0, 2, 1, 1, 1\], dtype=int32)
\>>> bisect\_means.predict(\[\[0, 0\], \[12, 3\]\])
array(\[0, 2\], dtype=int32)
\>>> bisect\_means.cluster\_centers\_
array(\[\[ 2., 1.\],\
       \[10., 9.\],\
       \[10., 1.\]\])

Copy to clipboard

For a comparison between BisectingKMeans and K-Means refer to example [Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html#sphx-glr-auto-examples-cluster-plot-bisect-kmeans-py)
.

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bisect_k_means.py#L364)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.fit "Link to this definition")

Compute bisecting k-means clustering.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training instances to cluster.

Note

The data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

The weights for each observation in X. If None, all observations are assigned equal weight. `sample_weight` is not used during initialization if `init` is a callable.

Returns:

self

Fitted estimator.

fit\_predict(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.fit_predict "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_bisect_k_means.py#L458)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.predict "Link to this definition")

Predict which cluster each sample in X belongs to.

Prediction is made by going down the hierarchical tree in searching of closest leaf cluster.

In the vector quantization literature, `cluster_centers_` is called the code book and each value returned by `predict` is the index of the closest code in the code book.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data to predict.

Returns:

**labels**ndarray of shape (n\_samples,)

Index of the cluster each sample belongs to.

score(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_kmeans.py#L1155)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster._bisect_k_means.BisectingKMeans")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster._bisect_k_means.BisectingKMeans")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.set_score_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans.transform "Link to this definition")

Transform X to a cluster-distance space.

In the new space, each dimension is the distance to the cluster centers. Note that even if X is sparse, the array returned by `transform` will typically be dense.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data to transform.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_clusters)

X transformed in the new space.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)