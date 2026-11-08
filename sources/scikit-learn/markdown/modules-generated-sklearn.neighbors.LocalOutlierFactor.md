[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)

Collapse Sidebar Expand Sidebar

LocalOutlierFactor[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#localoutlierfactor "Link to this heading")

=============================================================================================================================================================

class sklearn.neighbors.LocalOutlierFactor(_n\_neighbors\=20_, _\*_, _algorithm\='auto'_, _leaf\_size\=30_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_, _contamination\='auto'_, _novelty\=False_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_lof.py#L19)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "Link to this definition")

Unsupervised Outlier Detection using the Local Outlier Factor (LOF).

The anomaly score of each sample is called the Local Outlier Factor. It measures the local deviation of the density of a given sample with respect to its neighbors. It is local in that the anomaly score depends on how isolated the object is with respect to the surrounding neighborhood. More precisely, locality is given by k-nearest neighbors, whose distance is used to estimate the local density. By comparing the local density of a sample to the local densities of its neighbors, one can identify samples that have a substantially lower density than their neighbors. These are considered outliers.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor)
.

Added in version 0.19.

Parameters:

**n\_neighbors**int, default=20

Number of neighbors to use by default for [`kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.kneighbors "sklearn.neighbors.LocalOutlierFactor.kneighbors")
 queries. If n\_neighbors is larger than the number of samples provided, all samples will be used.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.fit "sklearn.neighbors.LocalOutlierFactor.fit")
     method.
    

Note: fitting on sparse input will override the setting of this parameter, using brute force.

**leaf\_size**int, default=30

Leaf is size passed to [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 or [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**metric**str or callable, default=’minkowski’

Metric to use for distance computation. Default is “minkowski”, which results in the standard Euclidean distance when p = 2. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for valid metric values.

If metric is “precomputed”, X is assumed to be a distance matrix and must be square during fit. X may be a [sparse graph](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
, in which case only “nonzero” elements may be considered neighbors.

If metric is a callable function, it takes two arrays representing 1D vectors as inputs and must return one value indicating the distance between those vectors. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

**p**float, default=2

Parameter for the Minkowski metric from [`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**contamination**‘auto’ or float, default=’auto’

The amount of contamination of the data set, i.e. the proportion of outliers in the data set. When fitting this is used to define the threshold on the scores of the samples.

*   if ‘auto’, the threshold is determined as in the original paper,
    
*   if a float, the contamination should be in the range (0, 0.5\].
    

Changed in version 0.22: The default value of `contamination` changed from 0.1 to `'auto'`.

**novelty**bool, default=False

By default, LocalOutlierFactor is only meant to be used for outlier detection (novelty=False). Set novelty to True if you want to use LocalOutlierFactor for novelty detection. In this case be aware that you should only use predict, decision\_function and score\_samples on new unseen data and not on the training set; and note that the results obtained this way may differ from the standard LOF results.

Added in version 0.20.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**negative\_outlier\_factor\_**ndarray of shape (n\_samples,)

The opposite LOF of the training samples. The higher, the more normal. Inliers tend to have a LOF score close to 1 (`negative_outlier_factor_` close to -1), while outliers tend to have a larger LOF score.

The local outlier factor (LOF) of a sample captures its supposed ‘degree of abnormality’. It is the average of the ratio of the local reachability density of a sample and those of its k-nearest neighbors.

**n\_neighbors\_**int

The actual number of neighbors used for [`kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.kneighbors "sklearn.neighbors.LocalOutlierFactor.kneighbors")
 queries.

**offset\_**float

Offset used to obtain binary labels from the raw scores. Observations having a negative\_outlier\_factor smaller than `offset_` are detected as abnormal. The offset is set to -1.5 (inliers score around -1), except when a contamination parameter different than “auto” is provided. In that case, the offset is defined in such a way we obtain the expected number of outliers in training.

Added in version 0.20.

**effective\_metric\_**str

The effective metric used for the distance computation.

**effective\_metric\_params\_**dict

The effective additional keyword arguments for the metric function.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_samples\_fit\_**int

It is the number of samples in the fitted data.

See also

[`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")

Unsupervised Outlier Detection using Support Vector Machine.

References

\[1\]

Breunig, M. M., Kriegel, H. P., Ng, R. T., & Sander, J. (2000, May). [LOF: identifying density-based local outliers.](https://dl.acm.org/doi/pdf/10.1145/342009.335388)
 In Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data, pp. 93-104.

Examples

\>>> import numpy as np
\>>> from sklearn.neighbors import LocalOutlierFactor
\>>> X \= \[\[\-1.1\], \[0.2\], \[101.1\], \[0.3\]\]
\>>> clf \= LocalOutlierFactor(n\_neighbors\=2)
\>>> clf.fit\_predict(X)
array(\[ 1,  1, -1,  1\])
\>>> clf.negative\_outlier\_factor\_
array(\[ -0.9821,  -1.0370, -73.3697,  -0.9821\])

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_lof.py#L410)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.decision_function "Link to this definition")

Shifted opposite of the Local Outlier Factor of X.

Bigger is better, i.e. large values correspond to inliers.

**Only available for novelty detection (when novelty is set to True).** The shift offset allows a zero threshold for being an outlier. The argument X is supposed to contain _new data_: if X contains a point from training, it considers the later in its own neighborhood. Also, the samples in X are not considered in the neighborhood of any point.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The query sample or samples to compute the Local Outlier Factor w.r.t. the training samples.

Returns:

**shifted\_opposite\_lof\_scores**ndarray of shape (n\_samples,)

The shifted opposite of the Local Outlier Factor of each input samples. The lower, the more abnormal. Negative scores represent outliers, positive scores represent inliers.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_lof.py#L262)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.fit "Link to this definition")

Fit the local outlier factor detector from the training dataset.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples) if metric=’precomputed’

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**LocalOutlierFactor

The fitted local outlier factor detector.

fit\_predict(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_lof.py#L234)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.fit_predict "Link to this definition")

Fit the model to the training set X and return the labels.

**Not available for novelty detection (when novelty is set to True).** Label is 1 for an inlier and -1 for an outlier according to the LOF score and the contamination parameter.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), default=None

The query sample or samples to compute the Local Outlier Factor w.r.t. the training samples.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**is\_inlier**ndarray of shape (n\_samples,)

Returns -1 for anomalies/outliers and 1 for inliers.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

kneighbors(_X\=None_, _n\_neighbors\=None_, _return\_distance\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_base.py#L756)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.kneighbors "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.kneighbors_graph "Link to this definition")

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

predict(_X\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_lof.py#L345)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.predict "Link to this definition")

Predict the labels (1 inlier, -1 outlier) of X according to LOF.

**Only available for novelty detection (when novelty is set to True).** This method allows to generalize prediction to _new observations_ (not in the training set). Note that the result of `clf.fit(X)` then `clf.predict(X)` with `novelty=True` may differ from the result obtained by `clf.fit_predict(X)` with `novelty=False`.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The query sample or samples to compute the Local Outlier Factor w.r.t. the training samples.

Returns:

**is\_inlier**ndarray of shape (n\_samples,)

Returns -1 for anomalies/outliers and +1 for inliers.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_lof.py#L450)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.score_samples "Link to this definition")

Opposite of the Local Outlier Factor of X.

It is the opposite as bigger is better, i.e. large values correspond to inliers.

**Only available for novelty detection (when novelty is set to True).** The argument X is supposed to contain _new data_: if X contains a point from training, it considers the later in its own neighborhood. Also, the samples in X are not considered in the neighborhood of any point. Because of this, the scores obtained via `score_samples` may differ from the standard LOF scores. The standard LOF scores for the training data is available via the `negative_outlier_factor_` attribute.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The query sample or samples to compute the Local Outlier Factor w.r.t. the training samples.

Returns:

**opposite\_lof\_scores**ndarray of shape (n\_samples,)

The opposite of the Local Outlier Factor of each input samples. The lower, the more abnormal.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_outlier_detection_thumb.png)

[Outlier detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html)

Outlier detection with Local Outlier Factor (LOF)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)