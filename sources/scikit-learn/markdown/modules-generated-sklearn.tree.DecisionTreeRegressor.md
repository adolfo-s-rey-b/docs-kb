[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.tree.DecisionTreeRegressor.html)

Collapse Sidebar Expand Sidebar

DecisionTreeRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#decisiontreeregressor "Link to this heading")

=================================================================================================================================================================

class sklearn.tree.DecisionTreeRegressor(_\*_, _criterion\='squared\_error'_, _splitter\='best'_, _max\_depth\=None_, _min\_samples\_split\=2_, _min\_samples\_leaf\=1_, _min\_weight\_fraction\_leaf\=0.0_, _max\_features\=None_, _random\_state\=None_, _max\_leaf\_nodes\=None_, _min\_impurity\_decrease\=0.0_, _ccp\_alpha\=0.0_, _monotonic\_cst\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L1097)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "Link to this definition")

A decision tree regressor.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#tree)
.

Parameters:

**criterion**{“squared\_error”, “absolute\_error”, “poisson”}, default=”squared\_error”

The function to measure the quality of a split. Supported criteria are “squared\_error” for the mean squared error, which is equal to variance reduction as feature selection criterion and minimizes the L2 loss using the mean of each terminal node, “absolute\_error” for the mean absolute error, which minimizes the L1 loss using the median of each terminal node, and “poisson” which uses reduction in Poisson deviance to find splits, also using the mean of each terminal node.

Added in version 0.18: Mean Absolute Error (MAE) criterion.

Added in version 0.24: Poisson deviance criterion.

Changed in version 1.9: Criterion `"friedman_mse"` was deprecated.

**splitter**{“best”, “random”}, default=”best”

The strategy used to choose the split at each node. Supported strategies are “best” to choose the best split and “random” to choose the best random split among considered features for this split.

**max\_depth**int, default=None

The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min\_samples\_split samples.

For an example of how `max_depth` influences the model, see [Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py)
.

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

**max\_features**int, float or {“sqrt”, “log2”}, default=None

The number of features to consider when looking for the best split:

*   If int, then consider `max_features` features at each split.
    
*   If float, then `max_features` is a fraction and `max(1, int(max_features * n_features_in_))` features are considered at each split.
    
*   If “sqrt”, then `max_features=sqrt(n_features)`.
    
*   If “log2”, then `max_features=log2(n_features)`.
    
*   If None, then `max_features=n_features`.
    

Note: splitting may inspect more than `max_features` features if needed to find a valid split.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of the estimator. The features are always randomly permuted at each split, even if `splitter` is set to `"best"`. When `max_features < n_features`, the algorithm will select `max_features` at random at each split before finding the best split among them. But the best found split may vary across different runs, even if `max_features=n_features`. That is the case, if the improvement of the criterion is identical for several splits and one split has to be selected at random. To obtain a deterministic behaviour during fitting, `random_state` has to be fixed to an integer. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

**max\_leaf\_nodes**int, default=None

Grow a tree with `max_leaf_nodes` in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.

**min\_impurity\_decrease**float, default=0.0

A node will be split if this split induces a decrease of the impurity greater than or equal to this value.

The weighted impurity decrease equation is the following:

N\_t / N \* (impurity \- N\_t\_R / N\_t \* right\_impurity
                    \- N\_t\_L / N\_t \* left\_impurity)

Copy to clipboard

where `N` is the total number of samples, `N_t` is the number of samples at the current node, `N_t_L` is the number of samples in the left child, and `N_t_R` is the number of samples in the right child.

`N`, `N_t`, `N_t_R` and `N_t_L` all refer to the weighted sum, if `sample_weight` is passed.

Added in version 0.19.

**ccp\_alpha**non-negative float, default=0.0

Complexity parameter used for Minimal Cost-Complexity Pruning. The subtree with the largest cost complexity that is smaller than `ccp_alpha` will be chosen. By default, no pruning is performed. See [Minimal Cost-Complexity Pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)
 for details. See [Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html#sphx-glr-auto-examples-tree-plot-cost-complexity-pruning-py)
 for an example of such pruning.

Added in version 0.22.

**monotonic\_cst**array-like of int of shape (n\_features), default=None

Indicates the monotonicity constraint to enforce on each feature.

*   1: monotonic increase
    
*   0: no constraint
    
*   \-1: monotonic decrease
    

If monotonic\_cst is None, no constraints are applied.

Monotonicity constraints are not supported for:

*   multioutput regressions (i.e. when `n_outputs_ > 1`).
    

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#monotonic-cst-gbdt)
.

Added in version 1.4.

Attributes:

`feature_importances_`ndarray of shape (n\_features,)

Return the feature importances.

**max\_features\_**int

The inferred value of max\_features.

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

**tree\_**Tree instance

The underlying Tree object. Please refer to `help(sklearn.tree._tree.Tree)` for attributes of Tree object and [Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#sphx-glr-auto-examples-tree-plot-unveil-tree-structure-py)
 for basic usage of these attributes.

See also

[`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

A decision tree classifier.

Notes

The default values for the parameters controlling the size of the trees (e.g. `max_depth`, `min_samples_leaf`, etc.) lead to fully grown and unpruned trees which can potentially be very large on some data sets. To reduce memory consumption, the complexity and size of the trees should be controlled by setting those parameter values.

References

\[1\]

[https://en.wikipedia.org/wiki/Decision\_tree\_learning](https://en.wikipedia.org/wiki/Decision_tree_learning)

\[2\]

L. Breiman, J. Friedman, R. Olshen, and C. Stone, “Classification and Regression Trees”, Wadsworth, Belmont, CA, 1984.

\[3\]

T. Hastie, R. Tibshirani and J. Friedman. “Elements of Statistical Learning”, Springer, 2009.

\[4\]

L. Breiman, and A. Cutler, “Random Forests”, [https://www.stat.berkeley.edu/~breiman/RandomForests/cc\_home.htm](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm)

Examples

\>>> from sklearn.datasets import load\_diabetes
\>>> from sklearn.model\_selection import cross\_val\_score
\>>> from sklearn.tree import DecisionTreeRegressor
\>>> X, y \= load\_diabetes(return\_X\_y\=True)
\>>> regressor \= DecisionTreeRegressor(random\_state\=0)
\>>> cross\_val\_score(regressor, X, y, cv\=10)
...
...
array(\[-0.39, -0.46,  0.02,  0.06, -0.50,\
       0.16,  0.11, -0.73, -0.30, -0.00\])

Copy to clipboard

apply(_X_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L552)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.apply "Link to this definition")

Return the index of the leaf that each sample is predicted as.

Added in version 0.17.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

**check\_input**bool, default=True

Allow to bypass several input checking. Don’t use this parameter unless you know what you’re doing.

Returns:

**X\_leaves**array-like of shape (n\_samples,)

For each datapoint x in X, return the index of the leaf x ends up in. Leaves are numbered within `[0; self.tree_.node_count)`, possibly with gaps in the numbering.\
\
cost\_complexity\_pruning\_path(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L627)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.cost_complexity_pruning_path "Link to this definition")\
\
Compute the pruning path during Minimal Cost-Complexity Pruning.\
\
See [Minimal Cost-Complexity Pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)\
 for details on the pruning process.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csc_matrix`.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
The target values (class labels) as integers or strings.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights. If None, then samples are equally weighted. Splits that would create child nodes with net zero or negative weight are ignored while searching for a split in each node. Splits are also ignored if they would result in any single class carrying a negative weight in either child node.\
\
Returns:\
\
**ccp\_path**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")\
\
Dictionary-like object, with the following attributes.\
\
ccp\_alphasndarray\
\
Effective alphas of subtree during pruning.\
\
impuritiesndarray\
\
Sum of the impurities of the subtree leaves for the corresponding alpha value in `ccp_alphas`.\
\
decision\_path(_X_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L580)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.decision_path "Link to this definition")\
\
Return the decision path in the tree.\
\
Added in version 0.18.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.\
\
**check\_input**bool, default=True\
\
Allow to bypass several input checking. Don’t use this parameter unless you know what you’re doing.\
\
Returns:\
\
**indicator**sparse matrix of shape (n\_samples, n\_nodes)\
\
Return a node indicator CSR matrix where non zero elements indicates that the samples goes through the nodes.\
\
fit(_X_, _y_, _sample\_weight\=None_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L1369)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.fit "Link to this definition")\
\
Build a decision tree regressor from the training set (X, y).\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The training input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csc_matrix`.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
The target values (real numbers). Use `dtype=np.float64` and `order='C'` for maximum efficiency.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights. If None, then samples are equally weighted. Splits that would create child nodes with net zero or negative weight are ignored while searching for a split in each node.\
\
**check\_input**bool, default=True\
\
Allow to bypass several input checking. Don’t use this parameter unless you know what you’re doing.\
\
Returns:\
\
**self**DecisionTreeRegressor\
\
Fitted estimator.\
\
get\_depth()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L158)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.get_depth "Link to this definition")\
\
Return the depth of the decision tree.\
\
The depth of a tree is the maximum distance between the root and any leaf.\
\
Returns:\
\
**self.tree\_.max\_depth**int\
\
The maximum depth of the tree.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.get_metadata_routing "Link to this definition")\
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
get\_n\_leaves()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L172)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.get_n_leaves "Link to this definition")\
\
Return the number of leaves of the decision tree.\
\
Returns:\
\
**self.tree\_.n\_leaves**int\
\
Number of leaves.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.get_params "Link to this definition")\
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
predict(_X_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_classes.py#L501)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.predict "Link to this definition")\
\
Predict class or regression value for X.\
\
For a classification model, the predicted class for each sample in X is returned. For a regression model, the predicted value based on X is returned.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.\
\
**check\_input**bool, default=True\
\
Allow to bypass several input checking. Don’t use this parameter unless you know what you’re doing.\
\
Returns:\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
The predicted classes, or the predict values.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.score "Link to this definition")\
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
 \= '$UNCHANGED$'_) → [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree._classes.DecisionTreeRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.set_fit_request "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.set_params "Link to this definition")\
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
 \= '$UNCHANGED$'_) → [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree._classes.DecisionTreeRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.set_score_request "Link to this definition")\
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
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#gallery-examples "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)\
\
[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)\
\
Decision Tree Regression with AdaBoost\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bias_variance_thumb.png)\
\
[Single estimator versus bagging: bias-variance decomposition](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html)\
\
Single estimator versus bagging: bias-variance decomposition\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_thumb.png)\
\
[Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html)\
\
Advanced Plotting With Partial Dependence\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_thumb.png)\
\
[Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)\
\
Using KBinsDiscretizer to discretize continuous features\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)\
\
Release Highlights for scikit-learn 0.22\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)\
\
Release Highlights for scikit-learn 0.24\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)\
\
Release Highlights for scikit-learn 1.8\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)\
\
[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)\
\
Decision Tree Regression\
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