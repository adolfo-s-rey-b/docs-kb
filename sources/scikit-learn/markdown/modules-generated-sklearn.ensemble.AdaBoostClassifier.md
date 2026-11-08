[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)

Collapse Sidebar Expand Sidebar

AdaBoostClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#adaboostclassifier "Link to this heading")

============================================================================================================================================================

class sklearn.ensemble.AdaBoostClassifier(_estimator\=None_, _\*_, _n\_estimators\=50_, _learning\_rate\=1.0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L321)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "Link to this definition")

An AdaBoost classifier.

An AdaBoost [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#r33e4ec8c4ad5-1)
 classifier is a meta-estimator that begins by fitting a classifier on the original dataset and then fits additional copies of the classifier on the same dataset but where the weights of incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.

This class implements the algorithm based on [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#r33e4ec8c4ad5-2)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#adaboost)
.

Added in version 0.14.

Parameters:

**estimator**object, default=None

The base estimator from which the boosted ensemble is built. Support for sample weighting is required, as well as proper `classes_` and `n_classes_` attributes. If `None`, then the base estimator is [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 initialized with `max_depth=1`.

Added in version 1.2: `base_estimator` was renamed to `estimator`.

**n\_estimators**int, default=50

The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early. Values must be in the range `[1, inf)`.\
\
**learning\_rate**float, default=1.0\
\
Weight applied to each classifier at each boosting iteration. A higher learning rate increases the contribution of each classifier. There is a trade-off between the `learning_rate` and `n_estimators` parameters. Values must be in the range `(0.0, inf)`.\
\
**random\_state**int, RandomState instance or None, default=None\
\
Controls the random seed given at each `estimator` at each boosting iteration. Thus, it is only used when `estimator` exposes a `random_state`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
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
**estimators\_**list of classifiers\
\
The collection of fitted sub-estimators.\
\
**classes\_**ndarray of shape (n\_classes,)\
\
The classes labels.\
\
**n\_classes\_**int\
\
The number of classes.\
\
**estimator\_weights\_**ndarray of floats\
\
Weights for each estimator in the boosted ensemble.\
\
**estimator\_errors\_**ndarray of floats\
\
Classification error for each estimator in the boosted ensemble.\
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
[`AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")\
\
An AdaBoost regressor that begins by fitting a regressor on the original dataset and then fits additional copies of the regressor on the same dataset but where the weights of instances are adjusted according to the error of the current prediction.\
\
[`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")\
\
GB builds an additive model in a forward stage-wise fashion. Regression trees are fit on the negative gradient of the binomial or multinomial deviance loss function. Binary classification is a special case where only a single regression tree is induced.\
\
[`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")\
\
A non-parametric supervised learning method used for classification. Creates a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.\
\
References\
\
\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#id1)\
\]\
\
Y. Freund, R. Schapire, “A Decision-Theoretic Generalization of on-Line Learning and an Application to Boosting”, 1995.\
\
\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#id2)\
\]\
\
[J. Zhu, H. Zou, S. Rosset, T. Hastie, “Multi-class adaboost.” Statistics and its Interface 2.3 (2009): 349-360.](https://doi.org/10.4310/SII.2009.v2.n3.a8)\
\
Examples\
\
\>>> from sklearn.ensemble import AdaBoostClassifier\
\>>> from sklearn.datasets import make\_classification\
\>>> X, y \= make\_classification(n\_samples\=1000, n\_features\=4,\
...                            n\_informative\=2, n\_redundant\=0,\
...                            random\_state\=0, shuffle\=False)\
\>>> clf \= AdaBoostClassifier(n\_estimators\=100, random\_state\=0)\
\>>> clf.fit(X, y)\
AdaBoostClassifier(n\_estimators=100, random\_state=0)\
\>>> clf.predict(\[\[0, 0, 0, 0\]\])\
array(\[1\])\
\>>> clf.score(X, y)\
0.96\
\
Copy to clipboard\
\
For a detailed example of using AdaBoost to fit a sequence of DecisionTrees as weaklearners, please refer to [Multi-class AdaBoosted Decision Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#sphx-glr-auto-examples-ensemble-plot-adaboost-multiclass-py)\
.\
\
For a detailed example of using AdaBoost to fit a non-linearly separable classification dataset composed of two Gaussian quantiles clusters, please refer to [Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html#sphx-glr-auto-examples-ensemble-plot-adaboost-twoclass-py)\
.\
\
decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L630)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.decision_function "Link to this definition")\
\
Compute the decision function of `X`.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Returns:\
\
**score**ndarray of shape of (n\_samples, k)\
\
The decision function of the input samples. The order of outputs is the same as in the [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
 attribute. Binary classification is a special case with `k == 1`, otherwise `k==n_classes`. For binary classification, values closer to -1 or 1 mean more like the first or second class in `classes_`, respectively.\
\
fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L104)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.fit "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.get_metadata_routing "Link to this definition")\
\
Raise `NotImplementedError`.\
\
This estimator does not support metadata routing yet.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.get_params "Link to this definition")\
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
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L572)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.predict "Link to this definition")\
\
Predict classes for X.\
\
The predicted class of an input sample is computed as the weighted mean prediction of the classifiers in the ensemble.\
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
The predicted classes.\
\
predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L801)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.predict_log_proba "Link to this definition")\
\
Predict class log-probabilities for X.\
\
The predicted class log-probabilities of an input sample is computed as the weighted mean predicted class log-probabilities of the classifiers in the ensemble.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Returns:\
\
**p**ndarray of shape (n\_samples, n\_classes)\
\
The class probabilities of the input samples. The order of outputs is the same as in the [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
 attribute.\
\
predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.predict_proba "Link to this definition")\
\
Predict class probabilities for X.\
\
The predicted class probabilities of an input sample is computed as the weighted mean predicted class probabilities of the classifiers in the ensemble.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Returns:\
\
**p**ndarray of shape (n\_samples, n\_classes)\
\
The class probabilities of the input samples. The order of outputs is the same as in the [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
 attribute.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.score "Link to this definition")\
\
Return [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)\
 on provided data and labels.\
\
In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
Test samples.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
True labels for `X`.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Returns:\
\
**score**float\
\
Mean accuracy of `self.predict(X)` w.r.t. `y`.\
\
set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble._weight_boosting.AdaBoostClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.set_fit_request "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.set_params "Link to this definition")\
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
 \= '$UNCHANGED$'_) → [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble._weight_boosting.AdaBoostClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.set_score_request "Link to this definition")\
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
staged\_decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L673)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_decision_function "Link to this definition")\
\
Compute decision function of `X` for each boosting iteration.\
\
This method allows monitoring (i.e. determine error on testing set) after each boosting iteration.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Yields:\
\
**score**generator of ndarray of shape (n\_samples, k)\
\
The decision function of the input samples. The order of outputs is the same as in the [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
 attribute. Binary classification is a special case with `k == 1`, otherwise `k==n_classes`. For binary classification, values closer to -1 or 1 mean more like the first or second class in `classes_`, respectively.\
\
staged\_predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L596)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_predict "Link to this definition")\
\
Return staged predictions for X.\
\
The predicted class of an input sample is computed as the weighted mean prediction of the classifiers in the ensemble.\
\
This generator method yields the ensemble prediction after each iteration of boosting and therefore allows monitoring, such as to determine the prediction on a test set after each boost.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
The input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Yields:\
\
**y**generator of ndarray of shape (n\_samples,)\
\
The predicted classes.\
\
staged\_predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L771)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_predict_proba "Link to this definition")\
\
Predict class probabilities for X.\
\
The predicted class probabilities of an input sample is computed as the weighted mean predicted class probabilities of the classifiers in the ensemble.\
\
This generator method yields the ensemble predicted class probabilities after each iteration of boosting and therefore allows monitoring, such as to determine the predicted class probabilities on a test set after each boost.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Sparse matrix can be CSC, CSR, COO, DOK, or LIL. COO, DOK, and LIL are converted to CSR.\
\
Yields:\
\
**p**generator of ndarray of shape (n\_samples,)\
\
The class probabilities of the input samples. The order of outputs is the same as in the [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
 attribute.\
\
staged\_score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_weight_boosting.py#L244)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_score "Link to this definition")\
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
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#gallery-examples "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)\
\
[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)\
\
Classifier comparison\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_multiclass_thumb.png)\
\
[Multi-class AdaBoosted Decision Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html)\
\
Multi-class AdaBoosted Decision Trees\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_thumb.png)\
\
[Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)\
\
Two-class AdaBoost\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)\
\
[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)\
\
Plot the decision surfaces of ensembles of trees on the iris dataset\
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