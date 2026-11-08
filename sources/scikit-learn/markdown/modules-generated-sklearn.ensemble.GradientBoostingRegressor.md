[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

GradientBoostingRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#gradientboostingregressor "Link to this heading")

=================================================================================================================================================================================

class sklearn.ensemble.GradientBoostingRegressor(_\*_, _loss\='squared\_error'_, _learning\_rate\=0.1_, _n\_estimators\=100_, _subsample\=1.0_, _criterion\='deprecated'_, _min\_samples\_split\=2_, _min\_samples\_leaf\=1_, _min\_weight\_fraction\_leaf\=0.0_, _max\_depth\=3_, _min\_impurity\_decrease\=0.0_, _init\=None_, _random\_state\=None_, _max\_features\=None_, _alpha\=0.9_, _verbose\=0_, _max\_leaf\_nodes\=None_, _warm\_start\=False_, _validation\_fraction\=0.1_, _n\_iter\_no\_change\=None_, _tol\=0.0001_, _ccp\_alpha\=0.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1756)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "Link to this definition")

Gradient Boosting for regression.

This estimator builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage a regression tree is fit on the negative gradient of the given loss function.

[`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 is a much faster variant of this algorithm for intermediate and large datasets (`n_samples >= 10_000`) and supports monotonic constraints.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting)
.

Parameters:

**loss**{‘squared\_error’, ‘absolute\_error’, ‘huber’, ‘quantile’}, default=’squared\_error’

Loss function to be optimized. ‘squared\_error’ refers to the squared error for regression. ‘absolute\_error’ refers to the absolute error of regression and is a robust loss function. ‘huber’ is a combination of the two. ‘quantile’ allows quantile regression (use `alpha` to specify the quantile). See [Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-quantile-py)
 for an example that demonstrates quantile regression for creating prediction intervals with `loss='quantile'`.

**learning\_rate**float, default=0.1

Learning rate shrinks the contribution of each tree by `learning_rate`. There is a trade-off between learning\_rate and n\_estimators. Values must be in the range `[0.0, inf)`.\
\
**n\_estimators**int, default=100\
\
The number of boosting stages to perform. Gradient boosting is fairly robust to over-fitting so a large number usually results in better performance. Values must be in the range `[1, inf)`.\
\
**subsample**float, default=1.0\
\
The fraction of samples to be used for fitting the individual base learners. If smaller than 1.0 this results in Stochastic Gradient Boosting. `subsample` interacts with the parameter `n_estimators`. Choosing `subsample < 1.0` leads to a reduction of variance and an increase in bias. Values must be in the range `(0.0, 1.0]`.\
\
**criterion**{‘friedman\_mse’, ‘squared\_error’}, default=’friedman\_mse’\
\
This parameter has no effect.\
\
Added in version 0.18.\
\
Deprecated since version 1.9: `criterion` is deprecated and will be removed in 1.11.\
\
**min\_samples\_split**int or float, default=2\
\
The minimum number of samples required to split an internal node:\
\
*   If int, values must be in the range `[2, inf)`.\
    \
*   If float, values must be in the range `(0.0, 1.0]` and `min_samples_split` will be `ceil(min_samples_split * n_samples)`.\
    \
\
Changed in version 0.18: Added float values for fractions.\
\
**min\_samples\_leaf**int or float, default=1\
\
The minimum number of samples required to be at a leaf node. A split point at any depth will only be considered if it leaves at least `min_samples_leaf` training samples in each of the left and right branches. This may have the effect of smoothing the model, especially in regression.\
\
*   If int, values must be in the range `[1, inf)`.\
    \
*   If float, values must be in the range `(0.0, 1.0)` and `min_samples_leaf` will be `ceil(min_samples_leaf * n_samples)`.\
    \
\
Changed in version 0.18: Added float values for fractions.\
\
**min\_weight\_fraction\_leaf**float, default=0.0\
\
The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node. Samples have equal weight when sample\_weight is not provided. Values must be in the range `[0.0, 0.5]`.\
\
**max\_depth**int or None, default=3\
\
Maximum depth of the individual regression estimators. The maximum depth limits the number of nodes in the tree. Tune this parameter for best performance; the best value depends on the interaction of the input variables. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min\_samples\_split samples. If int, values must be in the range `[1, inf)`.\
\
**min\_impurity\_decrease**float, default=0.0\
\
A node will be split if this split induces a decrease of the impurity greater than or equal to this value. Values must be in the range `[0.0, inf)`.\
\
The weighted impurity decrease equation is the following:\
\
N\_t / N \* (impurity \- N\_t\_R / N\_t \* right\_impurity\
                    \- N\_t\_L / N\_t \* left\_impurity)\
\
Copy to clipboard\
\
where `N` is the total number of samples, `N_t` is the number of samples at the current node, `N_t_L` is the number of samples in the left child, and `N_t_R` is the number of samples in the right child.\
\
`N`, `N_t`, `N_t_R` and `N_t_L` all refer to the weighted sum, if `sample_weight` is passed.\
\
Added in version 0.19.\
\
**init**estimator or ‘zero’, default=None\
\
An estimator object that is used to compute the initial predictions. `init` has to provide [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
 and [predict](https://scikit-learn.org/stable/glossary.html#term-predict)\
. If ‘zero’, the initial raw predictions are set to zero. By default a `DummyEstimator` is used, predicting either the average target value (for loss=’squared\_error’), or a quantile for the other losses.\
\
**random\_state**int, RandomState instance or None, default=None\
\
Controls the random seed given to each Tree estimator at each boosting iteration. In addition, it controls the random permutation of the features at each split (see Notes for more details). It also controls the random splitting of the training data to obtain a validation set if `n_iter_no_change` is not None. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
.\
\
**max\_features**{‘sqrt’, ‘log2’}, int or float, default=None\
\
The number of features to consider when looking for the best split:\
\
*   If int, values must be in the range `[1, inf)`.\
    \
*   If float, values must be in the range `(0.0, 1.0]` and the features considered at each split will be `max(1, int(max_features * n_features_in_))`.\
    \
*   If “sqrt”, then `max_features=sqrt(n_features)`.\
    \
*   If “log2”, then `max_features=log2(n_features)`.\
    \
*   If None, then `max_features=n_features`.\
    \
\
Choosing `max_features < n_features` leads to a reduction of variance and an increase in bias.\
\
Note: the search for a split does not stop until at least one valid partition of the node samples is found, even if it requires to effectively inspect more than `max_features` features.\
\
**alpha**float, default=0.9\
\
The alpha-quantile of the huber loss function and the quantile loss function. Only if `loss='huber'` or `loss='quantile'`. Values must be in the range `(0.0, 1.0)`.\
\
**verbose**int, default=0\
\
Enable verbose output. If 1 then it prints progress and performance once in a while (the more trees the lower the frequency). If greater than 1 then it prints progress and performance for every tree. Values must be in the range `[0, inf)`.\
\
**max\_leaf\_nodes**int, default=None\
\
Grow trees with `max_leaf_nodes` in best-first fashion. Best nodes are defined as relative reduction in impurity. Values must be in the range `[2, inf)`. If None, then unlimited number of leaf nodes.\
\
**warm\_start**bool, default=False\
\
When set to `True`, reuse the solution of the previous call to fit and add more estimators to the ensemble, otherwise, just erase the previous solution. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)\
.\
\
**validation\_fraction**float, default=0.1\
\
The proportion of training data to set aside as validation set for early stopping. Values must be in the range `(0.0, 1.0)`. Only used if `n_iter_no_change` is set to an integer.\
\
Added in version 0.20.\
\
**n\_iter\_no\_change**int, default=None\
\
`n_iter_no_change` is used to decide if early stopping will be used to terminate training when validation score is not improving. By default it is set to None to disable early stopping. If set to a number, it will set aside `validation_fraction` size of the training data as validation and terminate training when validation score is not improving in all of the previous `n_iter_no_change` numbers of iterations. Values must be in the range `[1, inf)`. See [Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-early-stopping-py)\
.\
\
Added in version 0.20.\
\
**tol**float, default=1e-4\
\
Tolerance for the early stopping. When the loss is not improving by at least tol for `n_iter_no_change` iterations (if set to a number), the training stops. Values must be in the range `[0.0, inf)`.\
\
Added in version 0.20.\
\
**ccp\_alpha**non-negative float, default=0.0\
\
Complexity parameter used for Minimal Cost-Complexity Pruning. The subtree with the largest cost complexity that is smaller than `ccp_alpha` will be chosen. By default, no pruning is performed. Values must be in the range `[0.0, inf)`. See [Minimal Cost-Complexity Pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)\
 for details. See [Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py)\
 for an example of such pruning.\
\
Added in version 0.22.\
\
Attributes:\
\
**n\_estimators\_**int\
\
The number of estimators as selected by early stopping (if `n_iter_no_change` is specified). Otherwise it is set to `n_estimators`.\
\
**n\_trees\_per\_iteration\_**int\
\
The number of trees that are built at each iteration. For regressors, this is always 1.\
\
Added in version 1.4.0.\
\
`feature_importances_`ndarray of shape (n\_features,)\
\
The impurity-based feature importances.\
\
**oob\_improvement\_**ndarray of shape (n\_estimators,)\
\
The improvement in loss on the out-of-bag samples relative to the previous iteration. `oob_improvement_[0]` is the improvement in loss of the first stage over the `init` estimator. Only available if `subsample < 1.0`.\
\
**oob\_scores\_**ndarray of shape (n\_estimators,)\
\
The full history of the loss values on the out-of-bag samples. Only available if `subsample < 1.0`.\
\
Added in version 1.3.\
\
**oob\_score\_**float\
\
The last value of the loss on the out-of-bag samples. It is the same as `oob_scores_[-1]`. Only available if `subsample < 1.0`.\
\
Added in version 1.3.\
\
**train\_score\_**ndarray of shape (n\_estimators,)\
\
The i-th score `train_score_[i]` is the loss of the model at iteration `i` on the in-bag sample. If `subsample == 1` this is the loss on the training data.\
\
**init\_**estimator\
\
The estimator that provides the initial predictions. Set via the `init` argument.\
\
**estimators\_**ndarray of DecisionTreeRegressor of shape (n\_estimators, 1)\
\
The collection of fitted sub-estimators.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
**max\_features\_**int\
\
The inferred value of max\_features.\
\
See also\
\
[`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")\
\
Histogram-based Gradient Boosting Classification Tree.\
\
[`sklearn.tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
\
A decision tree regressor.\
\
[`sklearn.ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")\
\
A random forest regressor.\
\
Notes\
\
The features are always randomly permuted at each split. Therefore, the best found split may vary, even with the same training data and `max_features=n_features`, if the improvement of the MSE is identical for several splits enumerated during the search of the best split. To obtain a deterministic behaviour during fitting, `random_state` has to be fixed.\
\
References\
\
J. Friedman, Greedy Function Approximation: A Gradient Boosting Machine, The Annals of Statistics, Vol. 29, No. 5, 2001.\
\
10.  Friedman, Stochastic Gradient Boosting, 1999\
    \
\
T. Hastie, R. Tibshirani and J. Friedman. Elements of Statistical Learning Ed. 2, Springer, 2009.\
\
Examples\
\
\>>> from sklearn.datasets import make\_regression\
\>>> from sklearn.ensemble import GradientBoostingRegressor\
\>>> from sklearn.model\_selection import train\_test\_split\
\>>> X, y \= make\_regression(random\_state\=0)\
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(\
...     X, y, random\_state\=0)\
\>>> reg \= GradientBoostingRegressor(random\_state\=0)\
\>>> reg.fit(X\_train, y\_train)\
GradientBoostingRegressor(random\_state=0)\
\>>> reg.predict(X\_test\[1:2\])\
array(\[-61.1\])\
\>>> reg.score(X\_test, y\_test)\
0.4...\
\
Copy to clipboard\
\
For a detailed example of utilizing [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")\
 to fit an ensemble of weak predictive models, please refer to [Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-regression-py)\
.\
\
apply(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L2192)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.apply "Link to this definition")\
\
Apply trees in the ensemble to X, return leaf indices.\
\
Added in version 0.17.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, its dtype will be converted to `dtype=np.float32`. If a sparse matrix is provided, it will be converted to a sparse `csr_array`.\
\
Returns:\
\
**X\_leaves**array-like of shape (n\_samples, n\_estimators)\
\
For each datapoint x in X and for each tree in the ensemble, return the index of the leaf x ends up in each estimator.\
\
fit(_X_, _y_, _sample\_weight\=None_, _monitor\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L622)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.fit "Link to this definition")\
\
Fit the gradient boosting model.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_array`.\
\
**y**array-like of shape (n\_samples,)\
\
Target values (strings or integers in classification, real numbers in regression) For classification, labels must correspond to classes.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights. If None, then samples are equally weighted. Splits that would create child nodes with net zero or negative weight are ignored while searching for a split in each node. In the case of classification, splits are also ignored if they would result in any single class carrying a negative weight in either child node.\
\
**monitor**callable, default=None\
\
The monitor is called after each iteration with the current iteration, a reference to the estimator and the local variables of `_fit_stages` as keyword arguments `callable(i, self, locals())`. If the callable returns `True` the fitting procedure is stopped. The monitor can be used for various things such as computing held-out estimates, early stopping, model introspect, and snapshotting.\
\
Returns:\
\
**self**object\
\
Fitted estimator.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Returns:\
\
**routing**MetadataRequest\
\
A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L2150)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.predict "Link to this definition")\
\
Predict regression target for X.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_array`.\
\
Returns:\
\
**y**ndarray of shape (n\_samples,)\
\
The predicted values.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.score "Link to this definition")\
\
Return [coefficient of determination](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)\
 on test data.\
\
The coefficient of determination, R2, is defined as (1−uv), where u is the residual sum of squares `((y_true - y_pred)** 2).sum()` and v is the total sum of squares `((y_true - y_true.mean()) ** 2).sum()`. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of `y`, disregarding the input features, would get a R2 score of 0.0.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
Test samples. For some estimators this may be a precomputed kernel matrix or a list of generic objects instead with shape `(n_samples, n_samples_fitted)`, where `n_samples_fitted` is the number of samples used in the fitting for the estimator.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
True values for `X`.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Returns:\
\
**score**float\
\
R2 of `self.predict(X)` w.r.t. `y`.\
\
Notes\
\
The R2 score used when calling `score` on a regressor uses `multioutput='uniform_average'` from version 0.23 to keep consistent with default value of [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")\
. This influences the `score` method of all the multioutput regressors (except for [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")\
).\
\
set\_fit\_request(_\*_, _monitor: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble._gb.GradientBoostingRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.set_fit_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `fit` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**monitor**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `monitor` parameter in `fit`.\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `fit`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble._gb.GradientBoostingRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.set_score_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `score` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `score`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
staged\_predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L2171)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.staged_predict "Link to this definition")\
\
Predict regression target at each stage for X.\
\
This method allows monitoring (i.e. determine error on testing set) after each stage.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_array`.\
\
Yields:\
\
**y**generator of ndarray of shape (n\_samples,)\
\
The predicted value of the input samples.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#gallery-examples "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)\
\
[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)\
\
Model Complexity Influence\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)\
\
[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)\
\
Early stopping in Gradient Boosting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)\
\
[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)\
\
Prediction Intervals for Gradient Boosting Regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)\
\
[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)\
\
Gradient Boosting regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_thumb.png)\
\
[Plot individual and voting regression predictions](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)\
\
Plot individual and voting regression predictions\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)