[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.FeatureAgglomeration.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.FeatureAgglomeration.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.FeatureAgglomeration.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.FeatureAgglomeration.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.FeatureAgglomeration.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.FeatureAgglomeration.html)

Collapse Sidebar Expand Sidebar

FeatureAgglomeration[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#featureagglomeration "Link to this heading")

=================================================================================================================================================================

class sklearn.cluster.FeatureAgglomeration(_n\_clusters\=2_, _\*_, _metric\='euclidean'_, _memory\=None_, _connectivity\=None_, _compute\_full\_tree\='auto'_, _linkage\='ward'_, _pooling\_func\=<function mean>_, _distance\_threshold\=None_, _compute\_distances\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_agglomerative.py#L1120)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "Link to this definition")

Agglomerate features.

Recursively merges pair of clusters of features.

Refer to [Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html#sphx-glr-auto-examples-cluster-plot-feature-agglomeration-vs-univariate-selection-py)
 for an example comparison of [`FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
 strategy with a univariate feature selection strategy (based on ANOVA).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
.

Parameters:

**n\_clusters**int or None, default=2

The number of clusters to find. It must be `None` if `distance_threshold` is not `None`.

**metric**str or callable, default=”euclidean”

Metric used to compute the linkage. Can be “euclidean”, “l1”, “l2”, “manhattan”, “cosine”, or “precomputed”. If linkage is “ward”, only “euclidean” and “l2” are accepted. If “precomputed”, a distance matrix is needed as input for the fit method.

Added in version 1.2.

**memory**str or object with the joblib.Memory interface, default=None

Used to cache the output of the computation of the tree. By default, no caching is done. If a string is given, it is the path to the caching directory.

**connectivity**array-like, sparse matrix, or callable, default=None

Connectivity matrix. Defines for each feature the neighboring features following a given structure of the data. This can be a connectivity matrix itself or a callable that transforms the data into a connectivity matrix, such as derived from `kneighbors_graph`. Default is `None`, i.e, the hierarchical clustering algorithm is unstructured.

**compute\_full\_tree**‘auto’ or bool, default=’auto’

Stop early the construction of the tree at `n_clusters`. This is useful to decrease computation time if the number of clusters is not small compared to the number of features. This option is useful only when specifying a connectivity matrix. Note also that when varying the number of clusters and using caching, it may be advantageous to compute the full tree. It must be `True` if `distance_threshold` is not `None`. By default `compute_full_tree` is “auto”, which is equivalent to `True` when `distance_threshold` is not `None` or that `n_clusters` is inferior to the maximum between 100 or `0.02 * n_samples`. Otherwise, “auto” is equivalent to `False`.

**linkage**{“ward”, “complete”, “average”, “single”}, default=”ward”

Which linkage criterion to use. The linkage criterion determines which distance to use between sets of features. The algorithm will merge the pairs of cluster that minimize this criterion.

*   “ward” minimizes the variance of the clusters being merged.
    
*   “complete” or maximum linkage uses the maximum distances between all features of the two sets.
    
*   “average” uses the average of the distances of each feature of the two sets.
    
*   “single” uses the minimum of the distances between all features of the two sets.
    

**pooling\_func**callable, default=np.mean

This combines the values of agglomerated features into a single value, and should accept an array of shape \[M, N\] and the keyword argument `axis=1`, and reduce it to an array of size \[M\].

**distance\_threshold**float, default=None

The linkage distance threshold at or above which clusters will not be merged. If not `None`, `n_clusters` must be `None` and `compute_full_tree` must be `True`.

Added in version 0.21.

**compute\_distances**bool, default=False

Computes distances between clusters even if `distance_threshold` is not used. This can be used to make dendrogram visualization, but introduces a computational and memory overhead.

Added in version 0.24.

Attributes:

**n\_clusters\_**int

The number of clusters found by the algorithm. If `distance_threshold=None`, it will be equal to the given `n_clusters`.

**labels\_**array-like of (n\_features,)

Cluster labels for each feature.

**n\_leaves\_**int

Number of leaves in the hierarchical tree.

**n\_connected\_components\_**int

The estimated number of connected components in the graph.

Added in version 0.21: `n_connected_components_` was added to replace `n_components_`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**children\_**array-like of shape (n\_nodes-1, 2)

The children of each non-leaf node. Values less than `n_features` correspond to leaves of the tree which are the original samples. A node `i` greater than or equal to `n_features` is a non-leaf node and has children `children_[i - n_features]`. Alternatively at the i-th iteration, children\[i\]\[0\] and children\[i\]\[1\] are merged to form node `n_features + i`.

**distances\_**array-like of shape (n\_nodes-1,)

Distances between nodes in the corresponding place in `children_`. Only computed if `distance_threshold` is used or `compute_distances` is set to `True`.

See also

[`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")

Agglomerative clustering samples instead of features.

[`ward_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#sklearn.cluster.ward_tree "sklearn.cluster.ward_tree")

Hierarchical clustering with ward linkage.

Examples

\>>> import numpy as np
\>>> from sklearn import datasets, cluster
\>>> digits \= datasets.load\_digits()
\>>> images \= digits.images
\>>> X \= np.reshape(images, (len(images), \-1))
\>>> agglo \= cluster.FeatureAgglomeration(n\_clusters\=32)
\>>> agglo.fit(X)
FeatureAgglomeration(n\_clusters=32)
\>>> X\_reduced \= agglo.transform(X)
\>>> X\_reduced.shape
(1797, 32)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_agglomerative.py#L1309)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.fit "Link to this definition")

Fit the hierarchical clustering on the data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Returns the transformer.

property fit\_predict[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.fit_predict "Link to this definition")

Fit and return the result of each sample’s clustering assignment.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_feature_agglomeration.py#L58)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.inverse_transform "Link to this definition")

Inverse the transformation and return a vector of size `n_features`.

Parameters:

**X**array-like of shape (n\_samples, n\_clusters) or (n\_clusters,)

The values to be assigned to each cluster of samples.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features) or (n\_features,)

A vector of size `n_samples` with the values of `X` assigned to each of the cluster of samples.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_feature_agglomeration.py#L24)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.transform "Link to this definition")

Transform a new matrix using the built clustering.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

An M by N array of M observations in N dimensions or a length M array of M one-dimensional observations.

Returns:

**Y**ndarray of shape (n\_samples, n\_clusters) or (n\_clusters,)

The pooled values for each feature cluster.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)