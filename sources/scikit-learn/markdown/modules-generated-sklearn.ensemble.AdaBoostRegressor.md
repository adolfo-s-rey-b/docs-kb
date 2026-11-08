[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)

Collapse Sidebar Expand Sidebar

AdaBoostRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#adaboostregressor "Link to this heading")

=========================================================================================================================================================

class sklearn.ensemble.AdaBoostRegressor(_estimator\=None_, _\*_, _n\_estimators\=50_, _learning\_rate\=1.0_, _loss\='linear'_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L823)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "Link to this definition")

An AdaBoost regressor.

An AdaBoost [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#r0c261b7dee9d-1)
 regressor is a meta-estimator that begins by fitting a regressor on the original dataset and then fits additional copies of the regressor on the same dataset but where the weights of instances are adjusted according to the error of the current prediction. As such, subsequent regressors focus more on difficult cases.

This class implements the algorithm known as AdaBoost.R2 [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#r0c261b7dee9d-2)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#adaboost)
.

Added in version 0.14.

Parameters:

**estimator**object, default=None

The base estimator from which the boosted ensemble is built. If `None`, then the base estimator is [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
 initialized with `max_depth=3`.

Added in version 1.2: `base_estimator` was renamed to `estimator`.

**n\_estimators**int, default=50

The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early. Values must be in the range `[1, inf)`.\
\
**learning\_rate**float, default=1.0\
\
Weight applied to each regressor at each boosting iteration. A higher learning rate increases the contribution of each regressor. There is a trade-off between the `learning_rate` and `n_estimators` parameters. Values must be in the range `(0.0, inf)`.\
\
**loss**{‘linear’, ‘square’, ‘exponential’}, default=’linear’\
\
The loss function to use when updating the weights after each boosting iteration.\
\
**random\_state**int, RandomState instance or None, default=None\
\
Controls the random seed given at each `estimator` at each boosting iteration. Thus, it is only used when `estimator` exposes a `random_state`. In addition, it controls the bootstrap of the weights used to train the `estimator` at each boosting iteration. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
.\
\
Attributes:\
\
**estimator\_**estimator\
\
The base estimator from which the ensemble is grown.\
\
Added in version 1.2: `base_estimator_` was renamed to `estimator_`.\
\
**estimators\_**list of regressors\
\
The collection of fitted sub-estimators.\
\
**estimator\_weights\_**ndarray of floats\
\
Weights for each estimator in the boosted ensemble.\
\
**estimator\_errors\_**ndarray of floats\
\
Regression error for each estimator in the boosted ensemble.\
\
`feature_importances_`ndarray of shape (n\_features,)\
\
The impurity-based feature importances.\
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
See also\
\
[`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")\
\
An AdaBoost classifier.\
\
[`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")\
\
Gradient Boosting Classification Tree.\
\
[`sklearn.tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
\
A decision tree regressor.\
\
References\
\
\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#id1)\
\]\
\
Y. Freund, R. Schapire, “A Decision-Theoretic Generalization of on-Line Learning and an Application to Boosting”, 1995.\
\
\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#id2)\
\]\
\
[H. Drucker, “Improving Regressors using Boosting Techniques”, 1997.](https://dl.acm.org/doi/10.5555/645526.657132)\
\
Examples\
\
\>>> from sklearn.ensemble import AdaBoostRegressor\
\>>> from sklearn.datasets import make\_regression\
\>>> X, y \= make\_regression(n\_features\=4, n\_informative\=2,\
...                        random\_state\=0, shuffle\=False)\
\>>> regr \= AdaBoostRegressor(random\_state\=0, n\_estimators\=100)\
\>>> regr.fit(X, y)\
AdaBoostRegressor(n\_estimators=100, random\_state=0)\
\>>> regr.predict(\[\[0, 0, 0, 0\]\])\
array(\[4.7972\])\
\>>> regr.score(X, y)\
0.9771\
\
Copy to clipboard\
\
For a detailed example of utilizing [`AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")\
 to fit a sequence of decision trees as weak learners, please refer to [Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#sphx-glr-auto-examples-ensemble-plot-adaboost-regression-py)\
.\
\
fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L104)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.fit "Link to this definition")\
\
Build a boosted classifier/regressor from the training set (X, y).\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
**y**array-like of shape (n\_samples,)\
\
The target values.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights. If None, the sample weights are initialized to 1 / n\_samples.\
\
Returns:\
\
**self**object\
\
Fitted estimator.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L252)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.get_metadata_routing "Link to this definition")\
\
Raise `NotImplementedError`.\
\
This estimator does not support metadata routing yet.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.get_params "Link to this definition")\
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
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L1084)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.predict "Link to this definition")\
\
Predict regression value for X.\
\
The predicted regression value of an input sample is computed as the weighted median prediction of the regressors in the ensemble.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Returns:\
\
**y**ndarray of shape (n\_samples,)\
\
The predicted regression values.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.score "Link to this definition")\
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
set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble._weight_boosting.AdaBoostRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.set_fit_request "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.set_params "Link to this definition")\
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
 \= '$UNCHANGED$'_) → [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble._weight_boosting.AdaBoostRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.set_score_request "Link to this definition")\
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
staged\_predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L1106)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.staged_predict "Link to this definition")\
\
Return staged predictions for X.\
\
The predicted regression value of an input sample is computed as the weighted median prediction of the regressors in the ensemble.\
\
This generator method yields the ensemble prediction after each iteration of boosting and therefore allows monitoring, such as to determine the prediction on a test set after each boost.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples.\
\
Yields:\
\
**y**generator of ndarray of shape (n\_samples,)\
\
The predicted regression values.\
\
staged\_score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L244)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.staged_score "Link to this definition")\
\
Return staged scores for X, y.\
\
This generator method yields the ensemble score after each iteration of boosting and therefore allows monitoring, such as to determine the score on a test set after each boost.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
**y**array-like of shape (n\_samples,)\
\
Labels for X.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Yields:\
\
**z**float\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#gallery-examples "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)\
\
[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)\
\
Decision Tree Regression with AdaBoost\
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