[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.LogisticRegressionCV.html)

Collapse Sidebar Expand Sidebar

LogisticRegressionCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#logisticregressioncv "Link to this heading")

======================================================================================================================================================================

class sklearn.linear\_model.LogisticRegressionCV(_\*_, _Cs\=10_, _l1\_ratios\='warn'_, _fit\_intercept\=True_, _cv\=None_, _dual\=False_, _penalty\='deprecated'_, _scoring\='warn'_, _solver\='lbfgs'_, _tol\=0.0001_, _max\_iter\=100_, _class\_weight\=None_, _n\_jobs\=None_, _verbose\=0_, _refit\=True_, _intercept\_scaling\=1.0_, _random\_state\=None_, _use\_legacy\_attributes\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1638)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "Link to this definition")

Logistic Regression CV (aka logit, MaxEnt) classifier.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

This class implements regularized logistic regression with implicit cross validation for the penalty parameters `C` and `l1_ratio`, see [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
, using a set of available solvers.

The solvers ‘lbfgs’, ‘newton-cg’, ‘newton-cholesky’ and ‘sag’ support only L2 regularization with primal formulation. The ‘liblinear’ solver supports both L1 and L2 regularization (but not both, i.e. elastic-net), with a dual formulation only for the L2 penalty. The Elastic-Net (combination of L1 and L2) regularization is only supported by the ‘saga’ solver.

For the grid of `Cs` values and `l1_ratios` values, the best hyperparameter is selected by the cross-validator [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
, but it can be changed using the [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 parameter. All solvers except ‘liblinear’ can warm-start the coefficients (see [Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
.

Parameters:

**Cs**int or list of floats, default=10

Each of the values in Cs describes the inverse of regularization strength. If Cs is as an int, then a grid of Cs values are chosen in a logarithmic scale between 1e-4 and 1e4. Like in support vector machines, smaller values specify stronger regularization.

**l1\_ratios**array-like of shape (n\_l1\_ratios), default=None

Floats between 0 and 1 passed as Elastic-Net mixing parameter (scaling between L1 and L2 penalties). For `l1_ratio = 0` the penalty is an L2 penalty. For `l1_ratio = 1` it is an L1 penalty. For `0 < l1_ratio < 1`, the penalty is a combination of L1 and L2. All the values of the given array-like are tested by cross-validation and the one giving the best prediction score is used.

Warning

Certain values of `l1_ratios`, i.e. some penalties, may not work with some solvers. See the parameter `solver` below, to know the compatibility between the penalty and solver.

Deprecated since version 1.8: `l1_ratios=None` is deprecated in 1.8 and will raise an error in version 1.10. Default value will change from `None` to `(0.0,)` in version 1.10.

**fit\_intercept**bool, default=True

Specifies if a constant (a.k.a. bias or intercept) should be added to the decision function.

**cv**int or cross-validation generator, default=None

The default cross-validation generator used is Stratified K-Folds. If an integer is provided, it specifies the number of folds, `n_folds`, used. See the module [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
 module for the list of possible cross-validation objects.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**dual**bool, default=False

Dual (constrained) or primal (regularized, see also [this equation](https://scikit-learn.org/stable/modules/linear_model.html#regularized-logistic-loss)
) formulation. Dual formulation is only implemented for l2 penalty with liblinear solver. Prefer dual=False when n\_samples > n\_features.

**penalty**{‘l1’, ‘l2’, ‘elasticnet’}, default=’l2’

Specify the norm of the penalty:

*   `'l2'`: add an L2 penalty term (used by default);
    
*   `'l1'`: add an L1 penalty term;
    
*   `'elasticnet'`: both L1 and L2 penalty terms are added.
    

Warning

Some penalties may not work with some solvers. See the parameter `solver` below, to know the compatibility between the penalty and solver.

Deprecated since version 1.8: `penalty` was deprecated in version 1.8 and will be removed in 1.10. Use `l1_ratio` and `C` instead. `l1_ratio=0` for `penalty='l2'`, `l1_ratio=1` for `penalty='l1'`, `l1_ratio` set to any float between 0 and 1 for `penalty='elasticnet'`, and `C=np.inf` for `penalty=None`.

**scoring**str or callable, default=None

The scoring method to use for cross-validation. Options:

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
     is used.
    

Changed in version 1.11: The default will change from None, i.e. accuracy, to ‘neg\_log\_loss’ in version 1.11.

**solver**{‘lbfgs’, ‘liblinear’, ‘newton-cg’, ‘newton-cholesky’, ‘sag’, ‘saga’}, default=’lbfgs’

Algorithm to use in the optimization problem. Default is ‘lbfgs’. To choose a solver, you might want to consider the following aspects:

*   ‘lbfgs’ is a good default solver because it works reasonably well for a wide class of problems.
    
*   For [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
     problems (`n_classes >= 3`), all solvers except ‘liblinear’ minimize the full multinomial loss, ‘liblinear’ will raise an error.
    
*   ‘newton-cholesky’ is a good choice for `n_samples` >> `n_features * n_classes`, especially with one-hot encoded categorical features with rare categories. Be aware that the memory usage of this solver has a quadratic dependency on `n_features * n_classes` because it explicitly computes the full Hessian matrix.
    
*   For small datasets, ‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones;
    
*   ‘liblinear’ might be slower in [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     because it does not handle warm-starting.
    
*   ‘liblinear’ can only handle binary classification by default. To apply a one-versus-rest scheme for the multiclass setting one can wrap it with the [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
    .
    

Warning

The choice of the algorithm depends on the penalty (`l1_ratio=0` for L2-penalty, `l1_ratio=1` for L1-penalty and `0 < l1_ratio < 1` for Elastic-Net) chosen and on (multinomial) multiclass support:

| solver | l1\_ratio | multinomial multiclass |
| --- | --- | --- |
| ‘lbfgs’ | l1\_ratio=0 | yes |
| ‘liblinear’ | l1\_ratio=1 or l1\_ratio=0 | no  |
| ‘newton-cg’ | l1\_ratio=0 | yes |
| ‘newton-cholesky’ | l1\_ratio=0 | yes |
| ‘sag’ | l1\_ratio=0 | yes |
| ‘saga’ | 0<=l1\_ratio<=1 | yes |

Note

‘sag’ and ‘saga’ fast convergence is only guaranteed on features with approximately the same scale. You can preprocess the data with a scaler from [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
.

Added in version 0.17: Stochastic Average Gradient (SAG) descent solver. Multinomial support in version 0.18.

Added in version 0.19: SAGA solver.

Added in version 1.2: newton-cholesky solver. Multinomial support in version 1.6.

**tol**float, default=1e-4

Tolerance for stopping criteria.

**max\_iter**int, default=100

Maximum number of iterations of the optimization algorithm.

**class\_weight**dict or ‘balanced’, default=None

Weights associated with classes in the form `{class_label: weight}`. If not given, all classes are supposed to have weight one.

The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as `n_samples / (n_classes * np.bincount(y))`.

Note that these weights will be multiplied with sample\_weight (passed through the fit method) if sample\_weight is specified.

Added in version 0.17: class\_weight == ‘balanced’

**n\_jobs**int, default=None

Number of CPU cores used during the cross-validation loop. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int, default=0

For the ‘liblinear’, ‘sag’ and ‘lbfgs’ solvers set verbose to any positive number for verbosity.

**refit**bool, default=True

If set to True, the scores are averaged across all folds, and the coefs and the C that corresponds to the best score is taken, and a final refit is done using these parameters. Otherwise the coefs, intercepts and C that correspond to the best scores across folds are averaged.

**intercept\_scaling**float, default=1

Useful only when the solver `liblinear` is used and `self.fit_intercept` is set to `True`. In this case, `x` becomes `[x, self.intercept_scaling]`, i.e. a “synthetic” feature with constant value equal to `intercept_scaling` is appended to the instance vector. The intercept becomes `intercept_scaling * synthetic_feature_weight`.

Note

The synthetic feature weight is subject to L1 or L2 regularization as all other features. To lessen the effect of regularization on synthetic feature weight (and therefore on the intercept) `intercept_scaling` has to be increased.

**random\_state**int, RandomState instance, default=None

Only used for `solver` == ‘sag’, ‘saga’ or ‘liblinear’ to shuffle the data. It has no effect on the other solvers. Note that this only applies to the solver and not the cross-validation generator. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

**use\_legacy\_attributes**bool, default=True

If True, use legacy values for attributes:

*   `C_` is an ndarray of shape (n\_classes,) with the same value repeated
    
*   `l1_ratio_` is an ndarray of shape (n\_classes,) with the same value repeated
    
*   `coefs_paths_` is a dict with class labels as keys and ndarrays as values
    
*   `scores_` is a dict with class labels as keys and ndarrays as values
    
*   `n_iter_` is an ndarray of shape (1, n\_folds, n\_cs) or similar
    

If False, use new values for attributes:

*   `C_` is a float
    
*   `l1_ratio_` is a float
    
*   `coefs_paths_` is an ndarray of shape (n\_folds, n\_l1\_ratios, n\_cs, n\_classes, n\_features) For binary problems (n\_classes=2), the 2nd last dimension is 1.
    
*   `scores_` is an ndarray of shape (n\_folds, n\_l1\_ratios, n\_cs)
    
*   `n_iter_` is an ndarray of shape (n\_folds, n\_l1\_ratios, n\_cs)
    

Changed in version 1.10: The default will change from True to False in version 1.10.

Deprecated since version 1.10: `use_legacy_attributes` will be deprecated in version 1.10 and be removed in 1.12.

Attributes:

**classes\_**ndarray of shape (n\_classes, )

A list of class labels known to the classifier.

**coef\_**ndarray of shape (1, n\_features) or (n\_classes, n\_features)

Coefficient of the features in the decision function.

`coef_` is of shape (1, n\_features) when the given problem is binary.

**intercept\_**ndarray of shape (1,) or (n\_classes,)

Intercept (a.k.a. bias) added to the decision function.

If `fit_intercept` is set to False, the intercept is set to zero. `intercept_` is of shape (1,) when the problem is binary.

**Cs\_**ndarray of shape (n\_cs)

Array of C i.e. inverse of regularization parameter values used for cross-validation.

**l1\_ratios\_**ndarray of shape (n\_l1\_ratios)

Array of l1\_ratios used for cross-validation. If l1\_ratios=None is used (i.e. penalty is not ‘elasticnet’), this is set to `[None]`

**coefs\_paths\_**dict of ndarray of shape (n\_folds, n\_cs, n\_dof) or (n\_folds, n\_cs, n\_l1\_ratios, n\_dof)

A dict with classes as the keys, and the path of coefficients obtained during cross-validating across each fold (`n_folds`) and then across each Cs (`n_cs`). The size of the coefficients is the number of degrees of freedom (`n_dof`), i.e. without intercept `n_dof=n_features` and with intercept `n_dof=n_features+1`. If `penalty='elasticnet'`, there is an additional dimension for the number of l1\_ratio values (`n_l1_ratios`), which gives a shape of `(n_folds, n_cs, n_l1_ratios_, n_dof)`. See also parameter `use_legacy_attributes`.

**scores\_**dict

A dict with classes as the keys, and the values as the grid of scores obtained during cross-validating each fold. The same score is repeated across all classes. Each dict value has shape `(n_folds, n_cs)` or `(n_folds, n_cs, n_l1_ratios)` if `penalty='elasticnet'`. See also parameter `use_legacy_attributes`.

**C\_**ndarray of shape (n\_classes,) or (1,)

The value of C that maps to the best score, repeated n\_classes times. If refit is set to False, the best C is the average of the C’s that correspond to the best score for each fold. `C_` is of shape (1,) when the problem is binary. See also parameter `use_legacy_attributes`.

**l1\_ratio\_**ndarray of shape (n\_classes,) or (n\_classes - 1,)

The value of l1\_ratio that maps to the best score, repeated n\_classes times. If refit is set to False, the best l1\_ratio is the average of the l1\_ratio’s that correspond to the best score for each fold. `l1_ratio_` is of shape (1,) when the problem is binary. See also parameter `use_legacy_attributes`.

**n\_iter\_**ndarray of shape (1, n\_folds, n\_cs) or (1, n\_folds, n\_cs, n\_l1\_ratios)

Actual number of iterations for all classes, folds and Cs. If `penalty='elasticnet'`, the shape is `(1, n_folds, n_cs, n_l1_ratios)`. See also parameter `use_legacy_attributes`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")

Logistic regression without tuning the hyperparameter `C`.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.linear\_model import LogisticRegressionCV
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> clf \= LogisticRegressionCV(
...     cv\=5, random\_state\=0,
...     use\_legacy\_attributes\=False,
...     l1\_ratios\=(0,),
...     scoring\="neg\_log\_loss",
... ).fit(X, y)
\>>> clf.predict(X\[:2, :\])
array(\[0, 0\])
\>>> clf.predict\_proba(X\[:2, :\]).shape
(2, 3)
\>>> clf.score(X, y)
\-0.041...

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L366)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.decision_function "Link to this definition")

Predict confidence scores for samples.

The confidence score for a sample is proportional to the signed distance of that sample to the hyperplane.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the confidence scores.

Returns:

**scores**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Confidence scores per `(n_samples, n_classes)` combination. In the binary case, confidence score for `self.classes_[1]` where >0 means this class would be predicted.

densify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.densify "Link to this definition")

Convert coefficient matrix to dense array format.

Converts the `coef_` member (back) to a numpy.ndarray. This is the default format of `coef_` and is required for fitting, so calling this method is only required on models that have previously been sparsified; otherwise, it is a no-op.

Returns:

self

Fitted estimator.

fit(_X_, _y_, _sample\_weight\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L2040)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.fit "Link to this definition")

Fit the model according to the given training data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target vector relative to X.

**sample\_weight**array-like of shape (n\_samples,) default=None

Array of weights that are assigned to individual samples. If not provided, then each sample is given unit weight.

**\*\*params**dict

Parameters to pass to the underlying splitter and scorer.

Added in version 1.4.

Returns:

**self**object

Fitted LogisticRegressionCV estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L2522)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L398)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.predict "Link to this definition")

Predict class labels for samples in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the predictions.

Returns:

**y\_pred**ndarray of shape (n\_samples,)

Vector containing the class labels for each sample.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1605)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.predict_log_proba "Link to this definition")

Predict logarithm of probability estimates.

The returned estimates for all classes are ordered by the label of classes.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Vector to be scored, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**T**array-like of shape (n\_samples, n\_classes)

Returns the log-probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1573)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.predict_proba "Link to this definition")

Probability estimates.

The returned estimates for all classes are ordered by the label of classes.

For a multiclass / multinomial problem the softmax function is used to find the predicted probability of each class.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Vector to be scored, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**T**array-like of shape (n\_samples, n\_classes)

Returns the probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.

score(_X_, _y_, _\*_, _sample\_weight\=None_, _\*\*score\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L2462)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.score "Link to this definition")

Score using the `scoring` option on the given test data and labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples,)

True labels for X.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Deprecated since version 1.9: `sample_weight` needs to be passed as a keyword argument and not as a positional argument.

**\*\*score\_params**dict

Parameters to pass to the `score` method of the underlying scorer.

Added in version 1.4.

Returns:

**score**float

Score of self.predict(X) w.r.t. y.

set\_callbacks(_\*callbacks_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1311)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.set_callbacks "Link to this definition")

Set callbacks for the estimator.

Parameters:

**\*callbacks**callback instances

The callbacks to set.

Returns:

**self**estimator instance

The estimator instance itself.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model._logistic.LogisticRegressionCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_score\_request() → [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model._logistic.LogisticRegressionCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.set_score_request "Link to this definition")

No-op.

Calling this method has no effect.

Returns:

**self**object

The updated object.

sparsify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L480)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.sparsify "Link to this definition")

Convert coefficient matrix to sparse format.

Converts the `coef_` member to a scipy.sparse matrix, which for L1-regularized models can be much more memory- and storage-efficient than the usual numpy.ndarray representation.

The `intercept_` member is not converted.

Warning

This method is not supported for estimators fitted with array API inputs (i.e. when [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
 is used with `array_api_dispatch=True`). The call may succeed but subsequent calls to [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.predict "sklearn.linear_model.LogisticRegressionCV.predict")
 and other methods involving passing arrays may raise or return unexpected results.

Returns:

self

Fitted estimator.

Notes

For non-sparse models, i.e. when there are not many zeros in `coef_`, this may actually _increase_ memory usage, so use this method with care. A rule of thumb is that the number of zero elements, which can be computed with `(coef_ == 0).sum()`, must be more than 50% for this to provide significant benefits.

After calling this method, further fitting with the partial\_fit method (if any) will not work until you call densify.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)