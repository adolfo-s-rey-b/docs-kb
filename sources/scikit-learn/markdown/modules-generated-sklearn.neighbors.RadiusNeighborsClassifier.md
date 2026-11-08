[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html)

Collapse Sidebar Expand Sidebar

RadiusNeighborsClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#radiusneighborsclassifier "Link to this heading")

==================================================================================================================================================================================

class sklearn.neighbors.RadiusNeighborsClassifier(_radius\=1.0_, _\*_, _weights\='uniform'_, _algorithm\='auto'_, _leaf\_size\=30_, _p\=2_, _metric\='minkowski'_, _outlier\_label\=None_, _metric\_params\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_classification.py#L459)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "Link to this definition")

Classifier implementing a vote among neighbors within a given radius.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#classification)
.

Parameters:

**radius**float, default=1.0

Range of parameter space to use by default for [`radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.radius_neighbors "sklearn.neighbors.RadiusNeighborsClassifier.radius_neighbors")
 queries.

**weights**{‘uniform’, ‘distance’}, callable or None, default=’uniform’

Weight function used in prediction. Possible values:

*   ‘uniform’ : uniform weights. All points in each neighborhood are weighted equally.
    
*   ‘distance’ : weight points by the inverse of their distance. in this case, closer neighbors of a query point will have a greater influence than neighbors which are further away.
    
*   \[callable\] : a user-defined function which accepts an array of distances, and returns an array of the same shape containing the weights.
    

Uniform weights are used by default.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.fit "sklearn.neighbors.RadiusNeighborsClassifier.fit")
     method.
    

Note: fitting on sparse input will override the setting of this parameter, using brute force.

**leaf\_size**int, default=30

Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**p**float, default=2

Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used. This parameter is expected to be positive.

**metric**str or callable, default=’minkowski’

Metric to use for distance computation. Default is “minkowski”, which results in the standard Euclidean distance when p = 2. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for valid metric values.

If metric is “precomputed”, X is assumed to be a distance matrix and must be square during fit. X may be a [sparse graph](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
, in which case only “nonzero” elements may be considered neighbors.

If metric is a callable function, it takes two arrays representing 1D vectors as inputs and must return one value indicating the distance between those vectors. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

**outlier\_label**{manual label, ‘most\_frequent’}, default=None

Label for outlier samples (samples with no neighbors in given radius).

*   manual label: str or int label (should be the same type as y) or list of manual labels if multi-output is used.
    
*   ‘most\_frequent’ : assign the most frequent label of y to outliers.
    
*   None : when any outlier is detected, ValueError will be raised.
    

The outlier label should be selected from among the unique ‘Y’ labels. If it is specified with a different value a warning will be raised and all class probabilities of outliers will be assigned to be 0.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**classes\_**ndarray of shape (n\_classes,)

Class labels known to the classifier.

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

**outlier\_label\_**int or array-like of shape (n\_class,)

Label which is given for outlier samples (samples with no neighbors on given radius).

**outputs\_2d\_**bool

False when `y`’s shape is (n\_samples, ) or (n\_samples, 1) during fit otherwise True.

See also

[`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")

Classifier implementing the k-nearest neighbors vote.

[`RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")

Regression based on neighbors within a fixed radius.

[`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")

Regression based on k-nearest neighbors.

[`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")

Unsupervised learner for implementing neighbor searches.

Notes

See [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
 in the online documentation for a discussion of the choice of `algorithm` and `leaf_size`.

[https://en.wikipedia.org/wiki/K-nearest\_neighbor\_algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbor_algorithm)

Examples

\>>> X \= \[\[0\], \[1\], \[2\], \[3\]\]
\>>> y \= \[0, 0, 1, 1\]
\>>> from sklearn.neighbors import RadiusNeighborsClassifier
\>>> neigh \= RadiusNeighborsClassifier(radius\=1.0)
\>>> neigh.fit(X, y)
RadiusNeighborsClassifier(...)
\>>> print(neigh.predict(\[\[1.5\]\]))
\[0\]
\>>> print(neigh.predict\_proba(\[\[1.0\]\]))
\[\[0.66666667 0.33333333\]\]

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_classification.py#L648)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.fit "Link to this definition")

Fit the radius neighbors classifier from the training dataset.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples) if metric=’precomputed’

Training data.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_outputs)

Target values.

Returns:

**self**RadiusNeighborsClassifier

The fitted radius neighbors classifier.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_classification.py#L723)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.predict "Link to this definition")

Predict the class labels for the provided data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_queries, n\_features), or (n\_queries, n\_indexed) if metric == ‘precomputed’, or None

Test samples. If `None`, predictions for all indexed points are returned; in this case, points are not considered their own neighbors.

Returns:

**y**ndarray of shape (n\_queries,) or (n\_queries, n\_outputs)

Class labels for each data sample.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_classification.py#L767)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.predict_proba "Link to this definition")

Return probability estimates for the test data X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_queries, n\_features), or (n\_queries, n\_indexed) if metric == ‘precomputed’, or None

Test samples. If `None`, predictions for all indexed points are returned; in this case, points are not considered their own neighbors.

Returns:

**p**ndarray of shape (n\_queries, n\_classes), or a list of n\_outputs of such arrays if n\_outputs > 1.

The class probabilities of the input samples. Classes are ordered by lexicographic order.

radius\_neighbors(_X\=None_, _radius\=None_, _return\_distance\=True_, _sort\_results\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L1086)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.radius_neighbors "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.radius_neighbors_graph "Link to this definition")

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

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_classification.py#L889)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.score "Link to this definition")

Return the mean accuracy on the given test data and labels.

In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.

Parameters:

**X**array-like of shape (n\_samples, n\_features), or None

Test samples. If `None`, predictions for all indexed points are used; in this case, points are not considered their own neighbors. This means that `knn.fit(X, y).score(None, y)` implicitly performs a leave-one-out cross-validation procedure and is equivalent to `cross_val_score(knn, X, y, cv=LeaveOneOut())` but typically much faster.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True labels for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

Mean accuracy of `self.predict(X)` w.r.t. `y`.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [RadiusNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors._classification.RadiusNeighborsClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.set_score_request "Link to this definition")

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

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)