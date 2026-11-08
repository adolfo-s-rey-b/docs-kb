[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.KNeighborsTransformer.html)

Collapse Sidebar Expand Sidebar

KNeighborsTransformer[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#kneighborstransformer "Link to this heading")

======================================================================================================================================================================

class sklearn.neighbors.KNeighborsTransformer(_\*_, _mode\='distance'_, _n\_neighbors\=5_, _algorithm\='auto'_, _leaf\_size\=30_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "Link to this definition")

Transform X into a (weighted) graph of k nearest neighbors.

The transformed data is a sparse graph as returned by kneighbors\_graph.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#neighbors-transformer)
.

Added in version 0.22.

Parameters:

**mode**{‘distance’, ‘connectivity’}, default=’distance’

Type of returned matrix: ‘connectivity’ will return the connectivity matrix with ones and zeros, and ‘distance’ will return the distances between neighbors according to the given metric.

**n\_neighbors**int, default=5

Number of neighbors for each sample in the transformed sparse graph. For compatibility reasons, as each sample is considered as its own neighbor, one extra neighbor will be computed when mode == ‘distance’. In this case, the sparse graph contains (n\_neighbors + 1) neighbors.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.fit "sklearn.neighbors.KNeighborsTransformer.fit")
     method.
    

Note: fitting on sparse input will override the setting of this parameter, using brute force.

**leaf\_size**int, default=30

Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**metric**str or callable, default=’minkowski’

Metric to use for distance computation. Default is “minkowski”, which results in the standard Euclidean distance when p = 2. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for valid metric values.

If metric is a callable function, it takes two arrays representing 1D vectors as inputs and must return one value indicating the distance between those vectors. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

Distance matrices are not supported.

**p**float, default=2

Parameter for the Minkowski metric from sklearn.metrics.pairwise.pairwise\_distances. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used. This parameter is expected to be positive.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. If `-1`, then the number of jobs is set to the number of CPU cores.

Attributes:

**effective\_metric\_**str or callable

The distance metric used. It will be same as the `metric` parameter or a synonym of it, e.g. ‘euclidean’ if the `metric` parameter set to ‘minkowski’ and `p` parameter set to 2.

**effective\_metric\_params\_**dict

Additional keyword arguments for the metric function. For most metrics will be same with `metric_params` parameter, but may also contain the `p` parameter value if the `effective_metric_` attribute is set to ‘minkowski’.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_samples\_fit\_**int

Number of samples in the fitted data.

See also

[`kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")

Compute the weighted graph of k-neighbors for points in X.

[`RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")

Transform X into a weighted graph of neighbors nearer than a radius.

Notes

For an example of using [`KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
 in combination with [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 see [Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html#sphx-glr-auto-examples-neighbors-approximate-nearest-neighbors-py)
.

Examples

\>>> from sklearn.datasets import load\_wine
\>>> from sklearn.neighbors import KNeighborsTransformer
\>>> X, \_ \= load\_wine(return\_X\_y\=True)
\>>> X.shape
(178, 13)
\>>> transformer \= KNeighborsTransformer(n\_neighbors\=5, mode\='distance')
\>>> X\_dist\_graph \= transformer.fit\_transform(X)
\>>> X\_dist\_graph.shape
(178, 178)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L418)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.fit "Link to this definition")

Fit the k-nearest neighbors transformer from the training dataset.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples) if metric=’precomputed’

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**KNeighborsTransformer

The fitted k-nearest neighbors transformer.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L464)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to X and y with optional parameters fit\_params and returns a transformed version of X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training set.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**Xt**sparse matrix of shape (n\_samples, n\_samples)

Xt\[i, j\] is assigned the weight of edge that connects i to j. Only the neighbors have an explicit value. The diagonal is always explicit. The matrix is of CSR format.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

kneighbors(_X\=None_, _n\_neighbors\=None_, _return\_distance\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L756)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.kneighbors "Link to this definition")

Find the K-neighbors of a point.

Returns indices of and distances to the neighbors of each point.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_queries, n\_features), or (n\_queries, n\_indexed) if metric == ‘precomputed’, default=None

The query point or points. If not provided, neighbors of each indexed point are returned. In this case, the query point is not considered its own neighbor.

**n\_neighbors**int, default=None

Number of neighbors required for each sample. The default is the value passed to the constructor.

**return\_distance**bool, default=True

Whether or not to return the distances.

Returns:

**neigh\_dist**ndarray of shape (n\_queries, n\_neighbors)

Array representing the lengths to points, only present if return\_distance=True.

**neigh\_ind**ndarray of shape (n\_queries, n\_neighbors)

Indices of the nearest points in the population matrix.

Examples

In the following example, we construct a NearestNeighbors class from an array representing our data set and ask who’s the closest point to \[1,1,1\]

\>>> samples \= \[\[0., 0., 0.\], \[0., .5, 0.\], \[1., 1., .5\]\]
\>>> from sklearn.neighbors import NearestNeighbors
\>>> neigh \= NearestNeighbors(n\_neighbors\=1)
\>>> neigh.fit(samples)
NearestNeighbors(n\_neighbors=1)
\>>> print(neigh.kneighbors(\[\[1., 1., 1.\]\]))
(array(\[\[0.5\]\]), array(\[\[2\]\]))

Copy to clipboard

As you can see, it returns \[\[0.5\]\], and \[\[2\]\], which means that the element is at distance 0.5 and is the third element of samples (indexes start at 0). You can also query for multiple points:

\>>> X \= \[\[0., 1., 0.\], \[1., 0., 1.\]\]
\>>> neigh.kneighbors(X, return\_distance\=False)
array(\[\[1\],\
       \[2\]\]...)

Copy to clipboard

kneighbors\_graph(_X\=None_, _n\_neighbors\=None_, _mode\='connectivity'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L960)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.kneighbors_graph "Link to this definition")

Compute the (weighted) graph of k-Neighbors for points in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_queries, n\_features), or (n\_queries, n\_indexed) if metric == ‘precomputed’, default=None

The query point or points. If not provided, neighbors of each indexed point are returned. In this case, the query point is not considered its own neighbor. For `metric='precomputed'` the shape should be (n\_queries, n\_indexed). Otherwise the shape should be (n\_queries, n\_features).

**n\_neighbors**int, default=None

Number of neighbors for each sample. The default is the value passed to the constructor.

**mode**{‘connectivity’, ‘distance’}, default=’connectivity’

Type of returned matrix: ‘connectivity’ will return the connectivity matrix with ones and zeros, in ‘distance’ the edges are distances between points, type of distance depends on the selected metric parameter in NearestNeighbors class.

Returns:

**A**sparse-matrix of shape (n\_queries, n\_samples\_fit)

`n_samples_fit` is the number of samples in the fitted data. `A[i, j]` gives the weight of the edge connecting `i` to `j`. The matrix is of CSR format.

See also

[`NearestNeighbors.radius_neighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors_graph "sklearn.neighbors.NearestNeighbors.radius_neighbors_graph")

Compute the (weighted) graph of Neighbors for points in X.

Examples

\>>> X \= \[\[0\], \[3\], \[1\]\]
\>>> from sklearn.neighbors import NearestNeighbors
\>>> neigh \= NearestNeighbors(n\_neighbors\=2)
\>>> neigh.fit(X)
NearestNeighbors(n\_neighbors=2)
\>>> A \= neigh.kneighbors\_graph(X)
\>>> A.toarray()
array(\[\[1., 0., 1.\],\
       \[0., 1., 1.\],\
       \[1., 0., 1.\]\])

Copy to clipboard

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L442)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer.transform "Link to this definition")

Compute the (weighted) graph of Neighbors for points in X.

Parameters:

**X**array-like of shape (n\_samples\_transform, n\_features)

Sample data.

Returns:

**Xt**sparse matrix of shape (n\_samples\_transform, n\_samples\_fit)

Xt\[i, j\] is assigned the weight of edge that connects i to j. Only the neighbors have an explicit value. The diagonal is always explicit. The matrix is of CSR format.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

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