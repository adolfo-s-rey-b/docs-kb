[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html)

Collapse Sidebar Expand Sidebar

RadiusNeighborsTransformer[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#radiusneighborstransformer "Link to this heading")

=====================================================================================================================================================================================

class sklearn.neighbors.RadiusNeighborsTransformer(_\*_, _mode\='distance'_, _radius\=1.0_, _algorithm\='auto'_, _leaf\_size\=30_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L489)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "Link to this definition")

Transform X into a (weighted) graph of neighbors nearer than a radius.

The transformed data is a sparse graph as returned by `radius_neighbors_graph`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#neighbors-transformer)
.

Added in version 0.22.

Parameters:

**mode**{‘distance’, ‘connectivity’}, default=’distance’

Type of returned matrix: ‘connectivity’ will return the connectivity matrix with ones and zeros, and ‘distance’ will return the distances between neighbors according to the given metric.

**radius**float, default=1.0

Radius of neighborhood in the transformed sparse graph.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.fit "sklearn.neighbors.RadiusNeighborsTransformer.fit")
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

[`KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")

Transform X into a weighted graph of k nearest neighbors.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import load\_wine
\>>> from sklearn.cluster import DBSCAN
\>>> from sklearn.neighbors import RadiusNeighborsTransformer
\>>> from sklearn.pipeline import make\_pipeline
\>>> X, \_ \= load\_wine(return\_X\_y\=True)
\>>> estimator \= make\_pipeline(
...     RadiusNeighborsTransformer(radius\=42.0, mode\='distance'),
...     DBSCAN(eps\=25.0, metric\='precomputed'))
\>>> X\_clustered \= estimator.fit\_predict(X)
\>>> clusters, counts \= np.unique(X\_clustered, return\_counts\=True)
\>>> print(counts)
\[ 29  15 111  11  12\]

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L643)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.fit "Link to this definition")

Fit the radius neighbors transformer from the training dataset.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples) if metric=’precomputed’

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**RadiusNeighborsTransformer

The fitted radius neighbors transformer.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L687)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

radius\_neighbors(_X\=None_, _radius\=None_, _return\_distance\=True_, _sort\_results\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L1086)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.radius_neighbors "Link to this definition")

Find the neighbors within a given radius of a point or points.

Return the indices and distances of each point from the dataset lying in a ball with size `radius` around the points of the query array. Points lying on the boundary are included in the results.

The result points are _not_ necessarily sorted by distance to their query point.

Parameters:

**X**{array-like, sparse matrix} of (n\_samples, n\_features), default=None

The query point or points. If not provided, neighbors of each indexed point are returned. In this case, the query point is not considered its own neighbor.

**radius**float, default=None

Limiting distance of neighbors to return. The default is the value passed to the constructor.

**return\_distance**bool, default=True

Whether or not to return the distances.

**sort\_results**bool, default=False

If True, the distances and indices will be sorted by increasing distances before being returned. If False, the results may not be sorted. If `return_distance=False`, setting `sort_results=True` will result in an error.

Added in version 0.22.

Returns:

**neigh\_dist**ndarray of shape (n\_samples,) of arrays

Array representing the distances to each point, only present if `return_distance=True`. The distance values are computed according to the `metric` constructor parameter.

**neigh\_ind**ndarray of shape (n\_samples,) of arrays

An array of arrays of indices of the approximate nearest points from the population matrix that lie within a ball of size `radius` around the query points.

Notes

Because the number of neighbors of each point is not necessarily equal, the results for multiple query points cannot be fit in a standard data array. For efficiency, `radius_neighbors` returns arrays of objects, where each object is a 1D array of indices or distances.

Examples

In the following example, we construct a NeighborsClassifier class from an array representing our data set and ask who’s the closest point to \[1, 1, 1\]:

\>>> import numpy as np
\>>> samples \= \[\[0., 0., 0.\], \[0., .5, 0.\], \[1., 1., .5\]\]
\>>> from sklearn.neighbors import NearestNeighbors
\>>> neigh \= NearestNeighbors(radius\=1.6)
\>>> neigh.fit(samples)
NearestNeighbors(radius=1.6)
\>>> rng \= neigh.radius\_neighbors(\[\[1., 1., 1.\]\])
\>>> print(np.asarray(rng\[0\]\[0\]))
\[1.5 0.5\]
\>>> print(np.asarray(rng\[1\]\[0\]))
\[1 2\]

Copy to clipboard

The first array returned contains the distances to all points which are closer than 1.6, while the second array returned contains their indices. In general, multiple points can be queried at the same time.

radius\_neighbors\_graph(_X\=None_, _radius\=None_, _mode\='connectivity'_, _sort\_results\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L1309)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.radius_neighbors_graph "Link to this definition")

Compute the (weighted) graph of Neighbors for points in X.

Neighborhoods are restricted the points at a distance lower than radius.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), default=None

The query point or points. If not provided, neighbors of each indexed point are returned. In this case, the query point is not considered its own neighbor.

**radius**float, default=None

Radius of neighborhoods. The default is the value passed to the constructor.

**mode**{‘connectivity’, ‘distance’}, default=’connectivity’

Type of returned matrix: ‘connectivity’ will return the connectivity matrix with ones and zeros, in ‘distance’ the edges are distances between points, type of distance depends on the selected metric parameter in NearestNeighbors class.

**sort\_results**bool, default=False

If True, in each row of the result, the non-zero entries will be sorted by increasing distances. If False, the non-zero entries may not be sorted. Only used with mode=’distance’.

Added in version 0.22.

Returns:

**A**sparse-matrix of shape (n\_queries, n\_samples\_fit)

`n_samples_fit` is the number of samples in the fitted data. `A[i, j]` gives the weight of the edge connecting `i` to `j`. The matrix is of CSR format.

See also

[`kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")

Compute the (weighted) graph of k-Neighbors for points in X.

Examples

\>>> X \= \[\[0\], \[3\], \[1\]\]
\>>> from sklearn.neighbors import NearestNeighbors
\>>> neigh \= NearestNeighbors(radius\=1.5)
\>>> neigh.fit(X)
NearestNeighbors(radius=1.5)
\>>> A \= neigh.radius\_neighbors\_graph(X)
\>>> A.toarray()
array(\[\[1., 0., 1.\],\
       \[0., 1., 0.\],\
       \[1., 0., 1.\]\])

Copy to clipboard

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L668)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer.transform "Link to this definition")

Compute the (weighted) graph of Neighbors for points in X.

Parameters:

**X**array-like of shape (n\_samples\_transform, n\_features)

Sample data.

Returns:

**Xt**sparse matrix of shape (n\_samples\_transform, n\_samples\_fit)

Xt\[i, j\] is assigned the weight of edge that connects i to j. Only the neighbors have an explicit value. The diagonal is always explicit. The matrix is of CSR format.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)