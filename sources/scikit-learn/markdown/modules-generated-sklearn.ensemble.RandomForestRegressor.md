[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

Collapse Sidebar Expand Sidebar

RandomForestRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#randomforestregressor "Link to this heading")

=====================================================================================================================================================================

class sklearn.ensemble.RandomForestRegressor(_n\_estimators\=100_, _\*_, _criterion\='squared\_error'_, _max\_depth\=None_, _min\_samples\_split\=2_, _min\_samples\_leaf\=1_, _min\_weight\_fraction\_leaf\=0.0_, _max\_features\=1.0_, _max\_leaf\_nodes\=None_, _min\_impurity\_decrease\=0.0_, _bootstrap\=True_, _oob\_score\=False_, _n\_jobs\=None_, _random\_state\=None_, _verbose\=0_, _warm\_start\=False_, _ccp\_alpha\=0.0_, _max\_samples\=None_, _monotonic\_cst\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_forest.py#L1576)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "Link to this definition")

A random forest regressor.

A random forest is a meta estimator that fits a number of decision tree regressors on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. Trees in the forest use the best split strategy, i.e. equivalent to passing `splitter="best"` to the underlying [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
. The sub-sample size is controlled with the `max_samples` parameter if `bootstrap=True` (default), otherwise the whole dataset is used to build each tree.

This estimator has native support for missing values (NaNs). During training, the tree grower learns at each split point whether samples with missing values should go to the left or right child, based on the potential gain. When predicting, samples with missing values are assigned to the left or right child consequently. If no missing values were encountered for a given feature during training, then samples with missing values are mapped to whichever child has the most samples.

For a comparison between tree-based ensemble models see the example [Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#sphx-glr-auto-examples-ensemble-plot-forest-hist-grad-boosting-comparison-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#forest)
.

Parameters:

**n\_estimators**int, default=100

The number of trees in the forest.

Changed in version 0.22: The default value of `n_estimators` changed from 10 to 100 in 0.22.

**criterion**{“squared\_error”, “absolute\_error”, “poisson”}, default=”squared\_error”

The function to measure the quality of a split. Supported criteria are “squared\_error” for the mean squared error, which is equal to variance reduction as feature selection criterion and minimizes the L2 loss using the mean of each terminal node, “absolute\_error” for the mean absolute error, which minimizes the L1 loss using the median of each terminal node, and “poisson” which uses reduction in Poisson deviance to find splits, also using the mean of each terminal node.

Added in version 0.18: Mean Absolute Error (MAE) criterion.

Added in version 1.0: Poisson criterion.

Changed in version 1.9: Criterion `"friedman_mse"` was deprecated.

**max\_depth**int, default=None

The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min\_samples\_split samples.

**min\_samples\_split**int or float, default=2

The minimum number of samples required to split an internal node:

*   If int, then consider `min_samples_split` as the minimum number.
    
*   If float, then `min_samples_split` is a fraction and `ceil(min_samples_split * n_samples)` are the minimum number of samples for each split.
    

Changed in version 0.18: Added float values for fractions.

**min\_samples\_leaf**int or float, default=1

The minimum number of samples required to be at a leaf node. A split point at any depth will only be considered if it leaves at least `min_samples_leaf` training samples in each of the left and right branches. This may have the effect of smoothing the model, especially in regression.

*   If int, then consider `min_samples_leaf` as the minimum number.
    
*   If float, then `min_samples_leaf` is a fraction and `ceil(min_samples_leaf * n_samples)` are the minimum number of samples for each node.
    

Changed in version 0.18: Added float values for fractions.

**min\_weight\_fraction\_leaf**float, default=0.0

The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node. Samples have equal weight when sample\_weight is not provided.

**max\_features**{“sqrt”, “log2”, None}, int or float, default=1.0

The number of features to consider when looking for the best split:

*   If int, then consider `max_features` features at each split.
    
*   If float, then `max_features` is a fraction and `max(1, int(max_features * n_features_in_))` features are considered at each split.
    
*   If “sqrt”, then `max_features=sqrt(n_features)`.
    
*   If “log2”, then `max_features=log2(n_features)`.
    
*   If None or 1.0, then `max_features=n_features`.
    

Note

The default of 1.0 is equivalent to bagged trees and more randomness can be achieved by setting smaller values, e.g. 0.3.

Changed in version 1.1: The default of `max_features` changed from `"auto"` to 1.0.

Note: the search for a split does not stop until at least one valid partition of the node samples is found, even if it requires to effectively inspect more than `max_features` features.

**max\_leaf\_nodes**int, default=None

Grow trees with `max_leaf_nodes` in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.

**min\_impurity\_decrease**float, default=0.0

A node will be split if this split induces a decrease of the impurity greater than or equal to this value.

The weighted impurity decrease equation is the following:

N\_t / N \* (impurity \- N\_t\_R / N\_t \* right\_impurity
                    \- N\_t\_L / N\_t \* left\_impurity)

Copy to clipboard

where `N` is the total number of samples, `N_t` is the number of samples at the current node, `N_t_L` is the number of samples in the left child, and `N_t_R` is the number of samples in the right child.

`N`, `N_t`, `N_t_R` and `N_t_L` all refer to the weighted sum, if `sample_weight` is passed.

Added in version 0.19.

**bootstrap**bool, default=True

Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.

**oob\_score**bool or callable, default=False

Whether to use out-of-bag samples to estimate the generalization score. By default, [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
 is used. Provide a callable with signature `metric(y_true, y_pred)` to use a custom metric. Only available if `bootstrap=True`.

For an illustration of out-of-bag (OOB) error estimation, see the example [OOB Errors for Random Forests](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html#sphx-glr-auto-examples-ensemble-plot-ensemble-oob-py)
.

**n\_jobs**int, default=None

The number of jobs to run in parallel. [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.fit "sklearn.ensemble.RandomForestRegressor.fit")
, [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.predict "sklearn.ensemble.RandomForestRegressor.predict")
, [`decision_path`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.decision_path "sklearn.ensemble.RandomForestRegressor.decision_path")
 and [`apply`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.apply "sklearn.ensemble.RandomForestRegressor.apply")
 are all parallelized over the trees. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance or None, default=None

Controls both the randomness of the bootstrapping of the samples used when building trees (if `bootstrap=True`) and the sampling of the features to consider when looking for the best split at each node (if `max_features < n_features`). See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

**verbose**int, default=0

Controls the verbosity when fitting and predicting.

**warm\_start**bool, default=False

When set to `True`, reuse the solution of the previous call to fit and add more estimators to the ensemble, otherwise, just fit a whole new forest. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
 and [Fitting additional trees](https://scikit-learn.org/stable/modules/ensemble.html#tree-ensemble-warm-start)
 for details.

**ccp\_alpha**non-negative float, default=0.0

Complexity parameter used for Minimal Cost-Complexity Pruning. The subtree with the largest cost complexity that is smaller than `ccp_alpha` will be chosen. By default, no pruning is performed. See [Minimal Cost-Complexity Pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)
 for details. See [Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py)
 for an example of such pruning.

Added in version 0.22.

**max\_samples**int or float, default=None

If bootstrap is True, the number of samples to draw from X to train each base estimator.

*   If None (default), then draw `X.shape[0]` samples irrespective of `sample_weight`.
    
*   If int, then draw `max_samples` samples.
    
*   If float, then draw `max_samples * X.shape[0]` unweighted samples or `max_samples * sample_weight.sum()` weighted samples.
    

Added in version 0.22.

Changed in version 1.9: Float `max_samples` is relative to `sample_weight.sum()` instead of `X.shape[0]` for weighted samples.

**monotonic\_cst**array-like of int of shape (n\_features,), default=None

Indicates the monotonicity constraint to enforce on each feature.

*   1: monotonically increasing
    
*   0: no constraint
    
*   \-1: monotonically decreasing
    

If monotonic\_cst is None, no constraints are applied.

Monotonicity constraints are not supported for:

*   multioutput regressions (i.e. when `n_outputs_ > 1`).
    

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#monotonic-cst-gbdt)
.

Added in version 1.4.

Attributes:

**estimator\_**[`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

The child estimator template used to create the collection of fitted sub-estimators.

Added in version 1.2: `base_estimator_` was renamed to `estimator_`.

**estimators\_**list of DecisionTreeRegressor

The collection of fitted sub-estimators.

`feature_importances_`ndarray of shape (n\_features,)

The impurity-based feature importances.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_outputs\_**int

The number of outputs when `fit` is performed.

**oob\_score\_**float

Score of the training dataset obtained using an out-of-bag estimate. This attribute exists only when `oob_score` is True.

**oob\_prediction\_**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Prediction computed with out-of-bag estimate on the training set. This attribute exists only when `oob_score` is True.

`estimators_samples_`list of arrays

The subset of drawn samples for each base estimator.

See also

[`sklearn.tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

A decision tree regressor.

[`sklearn.ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")

Ensemble of extremely randomized tree regressors.

[`sklearn.ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")

A Histogram-based Gradient Boosting Regression Tree, very fast for big datasets (n\_samples >= 10\_000).

Notes

The default values for the parameters controlling the size of the trees (e.g. `max_depth`, `min_samples_leaf`, etc.) lead to fully grown and unpruned trees which can potentially be very large on some data sets. To reduce memory consumption, the complexity and size of the trees should be controlled by setting those parameter values.

The features are always randomly permuted at each split. Therefore, the best found split may vary, even with the same training data, `max_features=n_features` and `bootstrap=False`, if the improvement of the criterion is identical for several splits enumerated during the search of the best split. To obtain a deterministic behaviour during fitting, `random_state` has to be fixed.

The default value `max_features=1.0` uses `n_features` rather than `n_features / 3`. The latter was originally suggested in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#rf91cab2dc427-1)
, whereas the former was more recently justified empirically in [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#rf91cab2dc427-2)
.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#id1)\
\]

[L. Breiman, “Random Forests”, Machine Learning, 45(1), 5-32, 2001.](https://doi.org/10.1023/A:1010933404324)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#id2)\
\]

P. Geurts, D. Ernst., and L. Wehenkel, “Extremely randomized trees”, Machine Learning, 63(1), 3-42, 2006.

Examples

\>>> from sklearn.ensemble import RandomForestRegressor
\>>> from sklearn.datasets import make\_regression
\>>> X, y \= make\_regression(n\_features\=4, n\_informative\=2,
...                        random\_state\=0, shuffle\=False)
\>>> regr \= RandomForestRegressor(max\_depth\=2, random\_state\=0)
\>>> regr.fit(X, y)
RandomForestRegressor(...)
\>>> print(regr.predict(\[\[0, 0, 0, 0\]\]))
\[-8.32987858\]

Copy to clipboard

apply(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_forest.py#L236)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.apply "Link to this definition")

Apply trees in the forest to X, return leaf indices.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, its dtype will be converted to `dtype=np.float32`. If a sparse matrix is provided, it will be converted into a sparse `csr_matrix`.

Returns:

**X\_leaves**ndarray of shape (n\_samples, n\_estimators)

For each datapoint x in X and for each tree in the forest, return the index of the leaf x ends up in.

decision\_path(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_forest.py#L262)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.decision_path "Link to this definition")

Return the decision path in the forest.

Added in version 0.18.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, its dtype will be converted to `dtype=np.float32`. If a sparse matrix is provided, it will be converted into a sparse `csr_matrix`.

Returns:

**indicator**sparse matrix of shape (n\_samples, n\_nodes)

Return a node indicator matrix where non zero elements indicates that the samples goes through the nodes. The matrix is of CSR format.

**n\_nodes\_ptr**ndarray of shape (n\_estimators + 1,)

The columns from indicator\[n\_nodes\_ptr\[i\]:n\_nodes\_ptr\[i+1\]\] gives the indicator value for the i-th estimator.

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_forest.py#L302)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.fit "Link to this definition")

Build a forest of trees from the training set (X, y).

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The training input samples. Internally, its dtype will be converted to `dtype=np.float32`. If a sparse matrix is provided, it will be converted into a sparse `csc_matrix`.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

The target values (class labels in classification, real numbers in regression).

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If None, then samples are equally weighted. Splits that would create child nodes with net zero or negative weight are ignored while searching for a split in each node. In the case of classification, splits are also ignored if they would result in any single class carrying a negative weight in either child node.

Returns:

**self**object

Fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_forest.py#L1044)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.predict "Link to this definition")

Predict regression target for X.

The predicted regression target of an input sample is computed as the mean predicted regression targets of the trees in the forest.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, its dtype will be converted to `dtype=np.float32`. If a sparse matrix is provided, it will be converted into a sparse `csr_matrix`.

Returns:

**y**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

The predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.score "Link to this definition")

Return [coefficient of determination](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)
 on test data.

The coefficient of determination, R2, is defined as (1−uv), where u is the residual sum of squares `((y_true - y_pred)** 2).sum()` and v is the total sum of squares `((y_true - y_true.mean()) ** 2).sum()`. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of `y`, disregarding the input features, would get a R2 score of 0.0.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples. For some estimators this may be a precomputed kernel matrix or a list of generic objects instead with shape `(n_samples, n_samples_fitted)`, where `n_samples_fitted` is the number of samples used in the fitting for the estimator.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True values for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

R2 of `self.predict(X)` w.r.t. `y`.

Notes

The R2 score used when calling `score` on a regressor uses `multioutput='uniform_average'` from version 0.23 to keep consistent with default value of [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
. This influences the `score` method of all the multioutput regressors (except for [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
).

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble._forest.RandomForestRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble._forest.RandomForestRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_thumb.png)

[Prediction Latency](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html)

Prediction Latency

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_regression_multioutput_thumb.png)

[Comparing random forests and the multi-output meta estimator](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)

Comparing random forests and the multi-output meta estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_thumb.png)

[Plot individual and voting regression predictions](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)

Plot individual and voting regression predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)