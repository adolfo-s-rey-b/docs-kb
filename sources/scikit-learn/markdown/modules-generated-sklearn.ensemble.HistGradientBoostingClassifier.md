[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)

Collapse Sidebar Expand Sidebar

HistGradientBoostingClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#histgradientboostingclassifier "Link to this heading")

================================================================================================================================================================================================

class sklearn.ensemble.HistGradientBoostingClassifier(_loss\='log\_loss'_, _\*_, _learning\_rate\=0.1_, _max\_iter\=100_, _max\_leaf\_nodes\=31_, _max\_depth\=None_, _min\_samples\_leaf\=20_, _l2\_regularization\=0.0_, _max\_features\=1.0_, _max\_bins\=255_, _categorical\_features\='from\_dtype'_, _monotonic\_cst\=None_, _interaction\_cst\=None_, _warm\_start\=False_, _early\_stopping\='auto'_, _scoring\='loss'_, _validation\_fraction\=0.1_, _n\_iter\_no\_change\=10_, _tol\=1e-07_, _verbose\=0_, _random\_state\=None_, _class\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L1762)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "Link to this definition")

Histogram-based Gradient Boosting Classification Tree.

This estimator is much faster than [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 for big datasets (n\_samples >= 10 000).

This estimator has native support for missing values (NaNs). During training, the tree grower learns at each split point whether samples with missing values should go to the left or right child, based on the potential gain. When predicting, samples with missing values are assigned to the left or right child consequently. If no missing values were encountered for a given feature during training, then samples with missing values are mapped to whichever child has the most samples.

This implementation is inspired by [LightGBM](https://github.com/lightgbm-org/LightGBM)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#histogram-based-gradient-boosting)
.

Added in version 0.21.

Parameters:

**loss**{‘log\_loss’}, default=’log\_loss’

The loss function to use in the boosting process.

For binary classification problems, ‘log\_loss’ is also known as logistic loss, binomial deviance or binary crossentropy. Internally, the model fits one tree per boosting iteration and uses the logistic sigmoid function (expit) as inverse link function to compute the predicted positive class probability.

For multiclass classification problems, ‘log\_loss’ is also known as multinomial deviance or categorical crossentropy. Internally, the model fits one tree per boosting iteration and per class and uses the softmax function as inverse link function to compute the predicted probabilities of the classes.

**learning\_rate**float, default=0.1

The learning rate, also known as _shrinkage_. This is used as a multiplicative factor for the leaves values. Use `1` for no shrinkage.

**max\_iter**int, default=100

The maximum number of iterations of the boosting process, i.e. the maximum number of trees for binary classification. For multiclass classification, `n_classes` trees per iteration are built.

**max\_leaf\_nodes**int or None, default=31

The maximum number of leaves for each tree. Must be strictly greater than 1. If None, there is no maximum limit.

**max\_depth**int or None, default=None

The maximum depth of each tree. The depth of a tree is the number of edges to go from the root to the deepest leaf. Depth isn’t constrained by default.

**min\_samples\_leaf**int, default=20

The minimum number of samples per leaf. For small datasets with less than a few hundred samples, it is recommended to lower this value since only very shallow trees would be built.

**l2\_regularization**float, default=0

The L2 regularization parameter penalizing leaves with small hessians. Use `0` for no regularization (default).

**max\_features**float, default=1.0

Proportion of randomly chosen features in each and every node split. This is a form of regularization, smaller values make the trees weaker learners and might prevent overfitting. If interaction constraints from `interaction_cst` are present, only allowed features are taken into account for the subsampling.

Added in version 1.4.

**max\_bins**int, default=255

The maximum number of bins to use for non-missing values. Before training, each feature of the input array `X` is binned into integer-valued bins, which allows for a much faster training stage. Features with a small number of unique values may use less than `max_bins` bins. In addition to the `max_bins` bins, one more bin is always reserved for missing values. Must be no larger than 255.

**categorical\_features**array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default=’from\_dtype’

Indicates the categorical features.

*   None : no feature will be considered categorical.
    
*   boolean array-like : boolean mask indicating categorical features.
    
*   integer array-like : integer indices indicating categorical features.
    
*   str array-like: names of categorical features (assuming the training data has feature names).
    
*   `"from_dtype"`: dataframe columns with dtype “Categorical” and “Enum” are considered to be categorical features. The input must be a dataframe that is supported by narwhals (or supports it): [`narwhals.from_native`](https://narwhals-dev.github.io/narwhals/api-reference/narwhals/#narwhals.from_native "(in Narwhals v0.0.0)")
     must work. This is the case, for instance, for pandas and polars DataFrames.
    

For each categorical feature, there must be at most `max_bins` unique categories. Negative values for categorical features encoded as numeric dtypes are treated as missing values. All categorical values are converted to floating point numbers. This means that categorical values of 1.0 and 1 are treated as the same category.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#categorical-support-gbdt)
.

Added in version 0.24.

Changed in version 1.2: Added support for feature names.

Changed in version 1.4: Added `"from_dtype"` option.

Changed in version 1.6: The default value changed from `None` to `"from_dtype"`.

**monotonic\_cst**array-like of int of shape (n\_features) or dict, default=None

Monotonic constraint to enforce on each feature are specified using the following integer values:

*   1: monotonic increase
    
*   0: no constraint
    
*   \-1: monotonic decrease
    

If a dict with str keys, map feature to monotonic constraints by name. If an array, the features are mapped to constraints by position. See [Using feature names to specify monotonic constraints](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html#monotonic-cst-features-names)
 for a usage example.

The constraints are only valid for binary classifications and hold over the probability of the positive class. Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#monotonic-cst-gbdt)
.

Added in version 0.23.

Changed in version 1.2: Accept dict of constraints with feature names as keys.

**interaction\_cst**{“pairwise”, “no\_interactions”} or sequence of lists/tuples/sets of int, default=None

Specify interaction constraints, the sets of features which can interact with each other in child node splits.

Each item specifies the set of feature indices that are allowed to interact with each other. If there are more features than specified in these constraints, they are treated as if they were specified as an additional set.

The strings “pairwise” and “no\_interactions” are shorthands for allowing only pairwise or no interactions, respectively.

For instance, with 5 features in total, `interaction_cst=[{0, 1}]` is equivalent to `interaction_cst=[{0, 1}, {2, 3, 4}]`, and specifies that each branch of a tree will either only split on features 0 and 1 or only split on features 2, 3 and 4.

See [this example](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#ice-vs-pdp)
 on how to use `interaction_cst`.

Added in version 1.2.

**warm\_start**bool, default=False

When set to `True`, reuse the solution of the previous call to fit and add more estimators to the ensemble. For results to be valid, the estimator should be re-trained on the same data only. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**early\_stopping**‘auto’ or bool, default=’auto’

If ‘auto’, early stopping is enabled if the sample size is larger than 10000 or if `X_val` and `y_val` are passed to `fit`. If True, early stopping is enabled, otherwise early stopping is disabled.

Added in version 0.23.

**scoring**str or callable or None, default=’loss’

Scoring method to use for early stopping. Only used if `early_stopping` is enabled. Options:

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
     is used.
    
*   ‘loss’: early stopping is checked w.r.t the loss value.
    

**validation\_fraction**int or float or None, default=0.1

Proportion (or absolute size) of training data to set aside as validation data for early stopping. If None, early stopping is done on the training data. The value is ignored if either early stopping is not performed, e.g. `early_stopping=False`, or if `X_val` and `y_val` are passed to fit.

**n\_iter\_no\_change**int, default=10

Used to determine when to “early stop”. The fitting process is stopped when none of the last `n_iter_no_change` scores are better than the `n_iter_no_change - 1` -th-to-last one, up to some tolerance. Only used if early stopping is performed.

**tol**float, default=1e-7

The absolute tolerance to use when comparing scores. The higher the tolerance, the more likely we are to early stop: higher tolerance means that it will be harder for subsequent iterations to be considered an improvement upon the reference score.

**verbose**int, default=0

The verbosity level. If not zero, print some information about the fitting process. `1` prints only summary info, `2` prints info per iteration.

**random\_state**int, RandomState instance or None, default=None

Pseudo-random number generator to control the subsampling in the binning process, and the train/validation data split if early stopping is enabled. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**class\_weight**dict or ‘balanced’, default=None

Weights associated with classes in the form `{class_label: weight}`. If not given, all classes are supposed to have weight one. The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as `n_samples / (n_classes * np.bincount(y))`. Note that these weights will be multiplied with sample\_weight (passed through the fit method) if `sample_weight` is specified.

Added in version 1.2.

Attributes:

**classes\_**array, shape = (n\_classes,)

Class labels.

**do\_early\_stopping\_**bool

Indicates whether early stopping is used during training.

`n_iter_`int

Number of iterations of the boosting process.

**n\_trees\_per\_iteration\_**int

The number of tree that are built at each iteration. This is equal to 1 for binary classification, and to `n_classes` for multiclass classification.

**train\_score\_**ndarray, shape (n\_iter\_+1,)

The scores at each iteration on the training data. The first entry is the score of the ensemble before the first iteration. Scores are computed according to the `scoring` parameter. If `scoring` is not ‘loss’, scores are computed on a subset of at most 10 000 samples. Empty if no early stopping.

**validation\_score\_**ndarray, shape (n\_iter\_+1,)

The scores at each iteration on the held-out validation data. The first entry is the score of the ensemble before the first iteration. Scores are computed according to the `scoring` parameter. Empty if no early stopping or if `validation_fraction` is None.

**is\_categorical\_**ndarray, shape (n\_features, ) or None

Boolean mask for the categorical features. `None` if there are no categorical features.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")

Exact gradient boosting method that does not scale as good on datasets with a large number of samples.

[`sklearn.tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

A decision tree classifier.

[`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

A meta-estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

[`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")

A meta-estimator that begins by fitting a classifier on the original dataset and then fits additional copies of the classifier on the same dataset where the weights of incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.

Examples

\>>> from sklearn.ensemble import HistGradientBoostingClassifier
\>>> from sklearn.datasets import load\_iris
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> clf \= HistGradientBoostingClassifier().fit(X, y)
\>>> clf.score(X, y)
1.0

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L2186)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.decision_function "Link to this definition")

Compute the decision function of `X`.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

The input samples.

Returns:

**decision**ndarray, shape (n\_samples,) or (n\_samples, n\_trees\_per\_iteration)

The raw predicted values (i.e. the sum of the trees leaves) for each sample. n\_trees\_per\_iteration is equal to the number of classes in multiclass classification.

fit(_X_, _y_, _sample\_weight\=None_, _\*_, _X\_val\=None_, _y\_val\=None_, _sample\_weight\_val\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L393)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.fit "Link to this definition")

Fit the gradient boosting model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

**y**array-like of shape (n\_samples,)

Target values.

**sample\_weight**array-like of shape (n\_samples,) default=None

Weights of training data.

Added in version 0.23.

**X\_val**array-like of shape (n\_val, n\_features)

Additional sample of features for validation used in early stopping. In a `Pipeline`, `X_val` can be transformed the same way as `X` with `Pipeline(..., transform_input=["X_val"])`.

Added in version 1.7.

**y\_val**array-like of shape (n\_samples,)

Additional sample of target values for validation used in early stopping.

Added in version 1.7.

**sample\_weight\_val**array-like of shape (n\_samples,) default=None

Additional weights for validation used in early stopping.

Added in version 1.7.

Returns:

**self**object

Fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L2101)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.predict "Link to this definition")

Predict classes for X.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

The input samples.

Returns:

**y**ndarray, shape (n\_samples,)

The predicted classes.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L2150)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.predict_proba "Link to this definition")

Predict class probabilities for X.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

The input samples.

Returns:

**p**ndarray, shape (n\_samples, n\_classes)

The class probabilities of the input samples.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.score "Link to this definition")

Return [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
 on provided data and labels.

In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True labels for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

Mean accuracy of `self.predict(X)` w.r.t. `y`.

set\_fit\_request(_\*_, _X\_val: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_, _sample\_weight\_val: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_, _y\_val: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.set_fit_request "Link to this definition")

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

**X\_val**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `X_val` parameter in `fit`.

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

**sample\_weight\_val**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight_val` parameter in `fit`.

**y\_val**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `y_val` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.set_score_request "Link to this definition")

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

staged\_decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L2207)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.staged_decision_function "Link to this definition")

Compute decision function of `X` for each iteration.

This method allows monitoring (i.e. determine error on testing set) after each stage.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Yields:

**decision**generator of ndarray of shape (n\_samples,) or (n\_samples, n\_trees\_per\_iteration)

The decision function of the input samples, which corresponds to the raw values predicted from the trees of the ensemble . The classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

staged\_predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L2124)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.staged_predict "Link to this definition")

Predict classes at each iteration.

This method allows monitoring (i.e. determine error on testing set) after each stage.

Added in version 0.24.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Yields:

**y**generator of ndarray of shape (n\_samples,)

The predicted classes of the input samples, for each iteration.

staged\_predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py#L2166)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier.staged_predict_proba "Link to this definition")

Predict class probabilities at each iteration.

This method allows monitoring (i.e. determine error on testing set) after each stage.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Yields:

**y**generator of ndarray of shape (n\_samples,)

The predicted class probabilities of the input samples, for each iteration.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)