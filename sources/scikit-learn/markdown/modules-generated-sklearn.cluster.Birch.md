[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.Birch.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.Birch.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.Birch.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.Birch.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.Birch.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.Birch.html)

Collapse Sidebar Expand Sidebar

Birch[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#birch "Link to this heading")

====================================================================================================================

class sklearn.cluster.Birch(_\*_, _threshold\=0.5_, _branching\_factor\=50_, _n\_clusters\=3_, _compute\_labels\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_birch.py#L359)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "Link to this definition")

Implements the BIRCH clustering algorithm.

It is a memory-efficient, online-learning algorithm provided as an alternative to [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
. It constructs a tree data structure with the cluster centroids being read off the leaf. These can be either the final cluster centroids or can be provided as input to another clustering algorithm such as [`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#birch)
.

Added in version 0.16.

Parameters:

**threshold**float, default=0.5

The radius of the subcluster obtained by merging a new sample and the closest subcluster should be lesser than the threshold. Otherwise a new subcluster is started. Setting this value to be very low promotes splitting and vice-versa.

**branching\_factor**int, default=50

Maximum number of CF subclusters in each node. If a new samples enters such that the number of subclusters exceed the branching\_factor then that node is split into two nodes with the subclusters redistributed in each. The parent subcluster of that node is removed and two new subclusters are added as parents of the 2 split nodes.

**n\_clusters**int, instance of sklearn.cluster model or None, default=3

Number of clusters after the final clustering step, which treats the subclusters from the leaves as new samples.

*   `None` : the final clustering step is not performed and the subclusters are returned as they are.
    
*   [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
     Estimator : If a model is provided, the model is fit treating the subclusters as new samples and the initial data is mapped to the label of the closest subcluster.
    
*   `int` : the model fit is [`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     with `n_clusters` set to be equal to the int.
    

**compute\_labels**bool, default=True

Whether or not to compute labels for each fit.

Attributes:

**root\_**\_CFNode

Root of the CFTree.

**dummy\_leaf\_**\_CFNode

Start pointer to all the leaves.

**subcluster\_centers\_**ndarray

Centroids of all subclusters read directly from the leaves.

**subcluster\_labels\_**ndarray

Labels assigned to the centroids of the subclusters after they are clustered globally.

**labels\_**ndarray of shape (n\_samples,)

Array of labels assigned to the input data. if partial\_fit is used instead of fit, they are assigned to the last batch of data.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")

Alternative implementation that does incremental updates of the centers’ positions using mini-batches.

Notes

The tree data structure consists of nodes with each node consisting of a number of subclusters. The maximum number of subclusters in a node is determined by the branching factor. Each subcluster maintains a linear sum, squared sum and the number of samples in that subcluster. In addition, each subcluster can also have a node as its child, if the subcluster is not a member of a leaf node.

For a new point entering the root, it is merged with the subcluster closest to it and the linear sum, squared sum and the number of samples of that subcluster are updated. This is done recursively till the properties of the leaf node are updated.

See [Compare BIRCH and MiniBatchKMeans](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html#sphx-glr-auto-examples-cluster-plot-birch-vs-minibatchkmeans-py)
 for a comparison with [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
.

References

*   Tian Zhang, Raghu Ramakrishnan, Maron Livny BIRCH: An efficient data clustering method for large databases. [https://www.cs.sfu.ca/CourseCentral/459/han/papers/zhang96.pdf](https://www.cs.sfu.ca/CourseCentral/459/han/papers/zhang96.pdf)
    
*   Roberto Perdisci JBirch - Java implementation of BIRCH clustering algorithm [https://code.google.com/archive/p/jbirch](https://code.google.com/archive/p/jbirch)
    

Examples

\>>> from sklearn.cluster import Birch
\>>> X \= \[\[0, 1\], \[0.3, 1\], \[\-0.3, 1\], \[0, \-1\], \[0.3, \-1\], \[\-0.3, \-1\]\]
\>>> brc \= Birch(n\_clusters\=None)
\>>> brc.fit(X)
Birch(n\_clusters=None)
\>>> brc.predict(X)
array(\[0, 0, 0, 1, 1, 1\])

Copy to clipboard

For a comparison of the BIRCH clustering algorithm with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_birch.py#L503)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.fit "Link to this definition")

Build a CF Tree for the input data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

self

Fitted estimator.

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L745)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.fit_predict "Link to this definition")

Perform clustering on `X` and returns cluster labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**labels**ndarray of shape (n\_samples,), dtype=np.int64

Cluster labels.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X\=None_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_birch.py#L610)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.partial_fit "Link to this definition")

Online learning. Prevents rebuilding of CFTree from scratch.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), default=None

Input data. If X is not provided, only the global clustering step is done.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

self

Fitted estimator.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_birch.py#L637)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.predict "Link to this definition")

Predict data using the `centroids_` of subclusters.

Avoid computation of the row norms of X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

Returns:

**labels**ndarray of shape(n\_samples,)

Labelled data.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_birch.py#L667)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch.transform "Link to this definition")

Transform X into subcluster centroids dimension.

Each dimension represents the distance from the sample point to each cluster centroid.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

Returns:

**X\_trans**{array-like, sparse matrix} of shape (n\_samples, n\_clusters)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_birch_vs_minibatchkmeans_thumb.png)

[Compare BIRCH and MiniBatchKMeans](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)

Compare BIRCH and MiniBatchKMeans

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