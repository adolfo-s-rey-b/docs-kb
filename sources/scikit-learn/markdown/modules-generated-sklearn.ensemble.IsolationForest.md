[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.IsolationForest.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.IsolationForest.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.IsolationForest.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.IsolationForest.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.IsolationForest.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.IsolationForest.html)

Collapse Sidebar Expand Sidebar

IsolationForest[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#isolationforest "Link to this heading")

===================================================================================================================================================

class sklearn.ensemble.IsolationForest(_\*_, _n\_estimators\=100_, _max\_samples\='auto'_, _contamination\='auto'_, _max\_features\=1.0_, _bootstrap\=False_, _n\_jobs\=None_, _random\_state\=None_, _verbose\=0_, _warm\_start\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_iforest.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "Link to this definition")

Isolation Forest Algorithm.

Return the anomaly score of each sample using the IsolationForest algorithm

The IsolationForest ‘isolates’ observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature.

Since recursive partitioning can be represented by a tree structure, the number of splittings required to isolate a sample is equivalent to the path length from the root node to the terminating node.

This path length, averaged over a forest of such random trees, is a measure of normality and our decision function.

Random partitioning produces noticeably shorter paths for anomalies. Hence, when a forest of random trees collectively produce shorter path lengths for particular samples, they are highly likely to be anomalies.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/outlier_detection.html#isolation-forest)
.

Added in version 0.18.

Parameters:

**n\_estimators**int, default=100

The number of base estimators in the ensemble.

**max\_samples**“auto”, int or float, default=”auto”

The number of samples to draw from X to train each base estimator.

*   If int, then draw `max_samples` samples.
    
*   If float, then draw `max_samples * X.shape[0]` samples.
    
*   If “auto”, then `max_samples=min(256, n_samples)`.
    

If max\_samples is larger than the number of samples provided, all samples will be used for all trees (no sampling).

**contamination**‘auto’ or float, default=’auto’

The amount of contamination of the data set, i.e. the proportion of outliers in the data set. Used when fitting to define the threshold on the scores of the samples.

*   If ‘auto’, the threshold is determined as in the original paper.
    
*   If float, the contamination should be in the range (0, 0.5\].
    

Changed in version 0.22: The default value of `contamination` changed from 0.1 to `'auto'`.

**max\_features**int or float, default=1.0

The number of features to draw from X to train each base estimator.

*   If int, then draw `max_features` features.
    
*   If float, then draw `max(1, int(max_features * n_features_in_))` features.
    

Note: using a float number less than 1.0 or integer less than number of features will enable feature subsampling and leads to a longer runtime.

**bootstrap**bool, default=False

If True, individual trees are fit on random subsets of the training data sampled with replacement. If False, sampling without replacement is performed.

**n\_jobs**int, default=None

The number of jobs to run in parallel for [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.fit "sklearn.ensemble.IsolationForest.fit")
. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance or None, default=None

Controls the pseudo-randomness of the selection of the feature and split values for each branching step and each tree in the forest.

Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**verbose**int, default=0

Controls the verbosity of the tree building process.

**warm\_start**bool, default=False

When set to `True`, reuse the solution of the previous call to fit and add more estimators to the ensemble, otherwise, just fit a whole new forest. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

Added in version 0.21.

Attributes:

**estimator\_**[`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
 instance

The child estimator template used to create the collection of fitted sub-estimators.

Added in version 1.2: `base_estimator_` was renamed to `estimator_`.

**estimators\_**list of ExtraTreeRegressor instances

The collection of fitted sub-estimators.

**estimators\_features\_**list of ndarray

The subset of drawn features for each base estimator.

`estimators_samples_`list of ndarray

The subset of drawn samples for each base estimator.

**max\_samples\_**int

The actual number of samples.

**offset\_**float

Offset used to define the decision function from the raw scores. We have the relation: `decision_function = score_samples - offset_`. `offset_` is defined as follows. When the contamination parameter is set to “auto”, the offset is equal to -0.5 as the scores of inliers are close to 0 and the scores of outliers are close to -1. When a contamination parameter different than “auto” is provided, the offset is defined in such a way we obtain the expected number of outliers (samples with decision function < 0) in training.

Added in version 0.20.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`sklearn.covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")

An object for detecting outliers in a Gaussian distributed dataset.

[`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")

Unsupervised Outlier Detection. Estimate the support of a high-dimensional distribution. The implementation is based on libsvm.

[`sklearn.neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")

Unsupervised Outlier Detection using Local Outlier Factor (LOF).

Notes

The implementation is based on an ensemble of ExtraTreeRegressor. The maximum depth of each tree is set to `ceil(log_2(n))` where n is the number of samples used to build the tree (see [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#rd7ae0a2ae688-1)
 for more details).

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#id1)\
\]

F. T. Liu, K. M. Ting and Z. -H. Zhou. [“Isolation forest.”](https://doi.org/10.1109/ICDM.2008.17)
 2008 Eighth IEEE International Conference on Data Mining (ICDM), 2008, pp. 413-422.

\[2\]

F. T. Liu, K. M. Ting and Z. -H. Zhou. [“Isolation-based anomaly detection.”](https://doi.org/10.1145/2133360.2133363)
 ACM Transactions on Knowledge Discovery from Data (TKDD) 6.1 (2012): 1-39.

Examples

\>>> from sklearn.ensemble import IsolationForest
\>>> X \= \[\[\-1.1\], \[0.3\], \[0.5\], \[100\]\]
\>>> clf \= IsolationForest(random\_state\=0).fit(X)
\>>> clf.predict(\[\[0.1\], \[0\], \[90\]\])
array(\[ 1,  1, -1\])

Copy to clipboard

For an example of using isolation forest for anomaly detection see [IsolationForest example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#sphx-glr-auto-examples-ensemble-plot-isolation-forest-py)
.

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_iforest.py#L432)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.decision_function "Link to this definition")

Average anomaly score of X of the base classifiers.

The anomaly score of an input sample is computed as the mean anomaly score of the trees in the forest.

The measure of normality of an observation given a tree is the depth of the leaf containing this observation, which is equivalent to the number of splittings required to isolate this point. In case of several observations n\_left in the leaf, the average path length of an n\_left samples isolation tree is added.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

Returns:

**scores**ndarray of shape (n\_samples,)

The anomaly score of the input samples. The lower, the more abnormal. Negative scores represent outliers, positive scores represent inliers.

Notes

The decision\_function method can be parallelized by setting a joblib context. This inherently does NOT use the `n_jobs` parameter initialized in the class, which is used during `fit`. This is because, calculating the score may actually be faster without parallelization for a small number of samples, such as for 1000 samples or less. The user can set the number of jobs in the joblib context to control the number of parallel jobs.

from joblib import parallel\_backend

\# Note, we use threading here as the decision\_function method is
\# not CPU bound.
with parallel\_backend("threading", n\_jobs\=4):
    model.decision\_function(X)

Copy to clipboard

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_iforest.py#L297)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.fit "Link to this definition")

Fit estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Use `dtype=np.float32` for maximum efficiency. Sparse matrices are also supported, use sparse `csc_matrix` for maximum efficiency.

**y**Ignored

Not used, present for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If None, then samples are equally weighted.

Returns:

**self**object

Fitted estimator.

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1141)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.fit_predict "Link to this definition")

Perform fit on X and returns labels for X.

Returns -1 for outliers and 1 for inliers.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**y**ndarray of shape (n\_samples,)

1 for inliers, -1 for outliers.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_bagging.py#L614)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_iforest.py#L392)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.predict "Link to this definition")

Predict if a particular sample is an outlier or not.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

Returns:

**is\_inlier**ndarray of shape (n\_samples,)

For each observation, tells whether or not (+1 or -1) it should be considered as an inlier according to the fitted model.

Notes

The predict method can be parallelized by setting a joblib context. This inherently does NOT use the `n_jobs` parameter initialized in the class, which is used during `fit`. This is because, predict may actually be faster without parallelization for a small number of samples, such as for 1000 samples or less. The user can set the number of jobs in the joblib context to control the number of parallel jobs.

from joblib import parallel\_backend

\# Note, we use threading here as the predict method is not CPU bound.
with parallel\_backend("threading", n\_jobs\=4):
    model.predict(X)

Copy to clipboard

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_iforest.py#L483)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.score_samples "Link to this definition")

Opposite of the anomaly score defined in the original paper.

The anomaly score of an input sample is computed as the mean anomaly score of the trees in the forest.

The measure of normality of an observation given a tree is the depth of the leaf containing this observation, which is equivalent to the number of splittings required to isolate this point. In case of several observations n\_left in the leaf, the average path length of an n\_left samples isolation tree is added.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples.

Returns:

**scores**ndarray of shape (n\_samples,)

The anomaly score of the input samples. The lower, the more abnormal.

Notes

The score function method can be parallelized by setting a joblib context. This inherently does NOT use the `n_jobs` parameter initialized in the class, which is used during `fit`. This is because, calculating the score may actually be faster without parallelization for a small number of samples, such as for 1000 samples or less. The user can set the number of jobs in the joblib context to control the number of parallel jobs.

from joblib import parallel\_backend

\# Note, we use threading here as the score\_samples method is not CPU bound.
with parallel\_backend("threading", n\_jobs\=4):
    model.score(X)

Copy to clipboard

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble._iforest.IsolationForest")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.set_fit_request "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_thumb.png)

[IsolationForest example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html)

IsolationForest example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)