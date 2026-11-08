[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.NearestNeighbors.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.NearestNeighbors.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.NearestNeighbors.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.NearestNeighbors.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.NearestNeighbors.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.NearestNeighbors.html)

Collapse Sidebar Expand Sidebar

NearestNeighbors[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#nearestneighbors "Link to this heading")

=======================================================================================================================================================

class sklearn.neighbors.NearestNeighbors(_\*_, _n\_neighbors\=5_, _radius\=1.0_, _algorithm\='auto'_, _leaf\_size\=30_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_unsupervised.py#L10)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "Link to this definition")

Unsupervised learner for implementing neighbor searches.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#unsupervised-neighbors)
.

Added in version 0.9.

Parameters:

**n\_neighbors**int, default=5

Number of neighbors to use by default for [`kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors "sklearn.neighbors.NearestNeighbors.kneighbors")
 queries.

**radius**float, default=1.0

Range of parameter space to use by default for [`radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "sklearn.neighbors.NearestNeighbors.radius_neighbors")
 queries.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.fit "sklearn.neighbors.NearestNeighbors.fit")
     method.
    

Note: fitting on sparse input will override the setting of this parameter, using brute force.

**leaf\_size**int, default=30

Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**metric**str or callable, default=’minkowski’

Metric to use for distance computation. Default is “minkowski”, which results in the standard Euclidean distance when p = 2. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for valid metric values.

If metric is “precomputed”, X is assumed to be a distance matrix and must be square during fit. X may be a [sparse graph](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
, in which case only “nonzero” elements may be considered neighbors.

If metric is a callable function, it takes two arrays representing 1D vectors as inputs and must return one value indicating the distance between those vectors. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

**p**float (positive), default=2

Parameter for the Minkowski metric from sklearn.metrics.pairwise.pairwise\_distances. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**effective\_metric\_**str

Metric used to compute distances to neighbors.

**effective\_metric\_params\_**dict

Parameters for the metric used to compute distances to neighbors.

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

[`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")

Classifier implementing the k-nearest neighbors vote.

[`RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")

Classifier implementing a vote among neighbors within a given radius.

[`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")

Regression based on k-nearest neighbors.

[`RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")

Regression based on neighbors within a fixed radius.

[`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")

Space partitioning data structure for organizing points in a multi-dimensional space, used for nearest neighbor search.

Notes

See [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
 in the online documentation for a discussion of the choice of `algorithm` and `leaf_size`.

[https://en.wikipedia.org/wiki/K-nearest\_neighbors\_algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)

Examples

\>>> import numpy as np
\>>> from sklearn.neighbors import NearestNeighbors
\>>> samples \= \[\[0, 0, 2\], \[1, 0, 0\], \[0, 0, 1\]\]
\>>> neigh \= NearestNeighbors(n\_neighbors\=2, radius\=0.4)
\>>> neigh.fit(samples)
NearestNeighbors(...)
\>>> neigh.kneighbors(\[\[0, 0, 1.3\]\], 2, return\_distance\=False)
array(\[\[2, 0\]\]...)
\>>> nbrs \= neigh.radius\_neighbors(
...    \[\[0, 0, 1.3\]\], 0.4, return\_distance\=False
... )
\>>> np.asarray(nbrs\[0\]\[0\])
array(2)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_unsupervised.py#L158)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.fit "Link to this definition")

Fit the nearest neighbors estimator from the training dataset.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples) if metric=’precomputed’

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**NearestNeighbors

The fitted nearest neighbors estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

kneighbors(_X\=None_, _n\_neighbors\=None_, _return\_distance\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L756)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors_graph "Link to this definition")

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

radius\_neighbors(_X\=None_, _radius\=None_, _return\_distance\=True_, _sort\_results\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L1086)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors_graph "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)