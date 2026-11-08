[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)

Collapse Sidebar Expand Sidebar

GradientBoostingClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#gradientboostingclassifier "Link to this heading")

====================================================================================================================================================================================

class sklearn.ensemble.GradientBoostingClassifier(_\*_, _loss\='log\_loss'_, _learning\_rate\=0.1_, _n\_estimators\=100_, _subsample\=1.0_, _criterion\='deprecated'_, _min\_samples\_split\=2_, _min\_samples\_leaf\=1_, _min\_weight\_fraction\_leaf\=0.0_, _max\_depth\=3_, _min\_impurity\_decrease\=0.0_, _init\=None_, _random\_state\=None_, _max\_features\=None_, _verbose\=0_, _max\_leaf\_nodes\=None_, _warm\_start\=False_, _validation\_fraction\=0.1_, _n\_iter\_no\_change\=None_, _tol\=0.0001_, _ccp\_alpha\=0.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1145)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "Link to this definition")

Gradient Boosting for classification.

This algorithm builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage `n_classes_` regression trees are fit on the negative gradient of the loss function, e.g. binary or multiclass log loss. Binary classification is a special case where only a single regression tree is induced.

[`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 is a much faster variant of this algorithm for intermediate and large datasets (`n_samples >= 10_000`) and supports monotonic constraints.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting)
.

Parameters:

**loss**{‘log\_loss’, ‘exponential’}, default=’log\_loss’

The loss function to be optimized. ‘log\_loss’ refers to binomial and multinomial deviance, the same as used in logistic regression. It is a good choice for classification with probabilistic outputs. For loss ‘exponential’, gradient boosting recovers the AdaBoost algorithm.

**learning\_rate**float, default=0.1

Learning rate shrinks the contribution of each tree by `learning_rate`. There is a trade-off between learning\_rate and n\_estimators. Values must be in the range `[0.0, inf)`.\
\
For an example of the effects of this parameter and its interaction with `subsample`, see [Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-regularization-py)\
.\
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
 and [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)\
. If ‘zero’, the initial raw predictions are set to zero. By default, a `DummyEstimator` predicting the classes priors is used.\
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
*   If ‘sqrt’, then `max_features=sqrt(n_features)`.\
    \
*   If ‘log2’, then `max_features=log2(n_features)`.\
    \
*   If None, then `max_features=n_features`.\
    \
\
Choosing `max_features < n_features` leads to a reduction of variance and an increase in bias.\
\
Note: the search for a split does not stop until at least one valid partition of the node samples is found, even if it requires to effectively inspect more than `max_features` features.\
\
**verbose**int, default=0\
\
Enable verbose output. If 1 then it prints progress and performance once in a while (the more trees the lower the frequency). If greater than 1 then it prints progress and performance for every tree. Values must be in the range `[0, inf)`.\
\
**max\_leaf\_nodes**int, default=None\
\
Grow trees with `max_leaf_nodes` in best-first fashion. Best nodes are defined as relative reduction in impurity. Values must be in the range `[2, inf)`. If `None`, then unlimited number of leaf nodes.\
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
`n_iter_no_change` is used to decide if early stopping will be used to terminate training when validation score is not improving. By default it is set to None to disable early stopping. If set to a number, it will set aside `validation_fraction` size of the training data as validation and terminate training when validation score is not improving in all of the previous `n_iter_no_change` numbers of iterations. The split is stratified. Values must be in the range `[1, inf)`. See [Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-early-stopping-py)\
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
Added in version 0.20.\
\
**n\_trees\_per\_iteration\_**int\
\
The number of trees that are built at each iteration. For binary classifiers, this is always 1.\
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
**estimators\_**ndarray of DecisionTreeRegressor of shape (n\_estimators, `n_trees_per_iteration_`)\
\
The collection of fitted sub-estimators. `n_trees_per_iteration_` is 1 for binary classification, otherwise `n_classes`.\
\
**classes\_**ndarray of shape (n\_classes,)\
\
The classes labels.\
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
**n\_classes\_**int\
\
The number of classes.\
\
**max\_features\_**int\
\
The inferred value of max\_features.\
\
See also\
\
[`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")\
\
Histogram-based Gradient Boosting Classification Tree.\
\
[`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")\
\
A decision tree classifier.\
\
[`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
\
A meta-estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.\
\
[`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")\
\
A meta-estimator that begins by fitting a classifier on the original dataset and then fits additional copies of the classifier on the same dataset where the weights of incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.\
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
The following example shows how to fit a gradient boosting classifier with 100 decision stumps as weak learners.\
\
\>>> from sklearn.datasets import make\_hastie\_10\_2\
\>>> from sklearn.ensemble import GradientBoostingClassifier\
\
Copy to clipboard\
\
\>>> X, y \= make\_hastie\_10\_2(random\_state\=0)\
\>>> X\_train, X\_test \= X\[:2000\], X\[2000:\]\
\>>> y\_train, y\_test \= y\[:2000\], y\[2000:\]\
\
Copy to clipboard\
\
\>>> clf \= GradientBoostingClassifier(n\_estimators\=100, learning\_rate\=1.0,\
...     max\_depth\=1, random\_state\=0).fit(X\_train, y\_train)\
\>>> clf.score(X\_test, y\_test)\
0.913\
\
Copy to clipboard\
\
apply(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1104)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.apply "Link to this definition")\
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
**X\_leaves**array-like of shape (n\_samples, n\_estimators, n\_classes)\
\
For each datapoint x in X and for each tree in the ensemble, return the index of the leaf x ends up in each estimator. In the case of binary classification n\_classes is 1.\
\
decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1579)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.decision_function "Link to this definition")\
\
Compute the decision function of `X`.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_array`.\
\
Returns:\
\
**score**ndarray of shape (n\_samples, n\_classes) or (n\_samples,)\
\
The decision function of the input samples, which corresponds to the raw values predicted from the trees of the ensemble . The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
. Regression and binary classification produce an array of shape (n\_samples,).\
\
fit(_X_, _y_, _sample\_weight\=None_, _monitor\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L622)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.fit "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.get_metadata_routing "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.get_params "Link to this definition")\
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
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1630)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict "Link to this definition")\
\
Predict class for X.\
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
predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1703)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict_log_proba "Link to this definition")\
\
Predict class log-probabilities for X.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_array`.\
\
Returns:\
\
**p**ndarray of shape (n\_samples, n\_classes)\
\
The class log-probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
.\
\
Raises:\
\
AttributeError\
\
If the `loss` does not support probabilities.\
\
predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1679)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict_proba "Link to this definition")\
\
Predict class probabilities for X.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_array`.\
\
Returns:\
\
**p**ndarray of shape (n\_samples, n\_classes)\
\
The class probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
.\
\
Raises:\
\
AttributeError\
\
If the `loss` does not support probabilities.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.score "Link to this definition")\
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
set\_fit\_request(_\*_, _monitor: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble._gb.GradientBoostingClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.set_fit_request "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.set_params "Link to this definition")\
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
 \= '$UNCHANGED$'_) → [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble._gb.GradientBoostingClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.set_score_request "Link to this definition")\
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
staged\_decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1606)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_decision_function "Link to this definition")\
\
Compute decision function of `X` for each iteration.\
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
**score**generator of ndarray of shape (n\_samples, k)\
\
The decision function of the input samples, which corresponds to the raw values predicted from the trees of the ensemble . The classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)\
. Regression and binary classification are special cases with `k == 1`, otherwise `k==n_classes`.\
\
staged\_predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1652)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict "Link to this definition")\
\
Predict class at each stage for X.\
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
staged\_predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_gb.py#L1727)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict_proba "Link to this definition")\
\
Predict class probabilities at each stage for X.\
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
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#gallery-examples "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)\
\
[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)\
\
Feature transformations with ensembles of trees\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_oob_thumb.png)\
\
[Gradient Boosting Out-of-Bag estimates](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html)\
\
Gradient Boosting Out-of-Bag estimates\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)\
\
[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)\
\
Gradient Boosting regularization\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)\
\
[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)\
\
Feature discretization\
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