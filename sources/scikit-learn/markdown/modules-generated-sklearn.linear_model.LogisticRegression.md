[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.LogisticRegression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.LogisticRegression.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LogisticRegression.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.LogisticRegression.html)

Collapse Sidebar Expand Sidebar

LogisticRegression[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#logisticregression "Link to this heading")

================================================================================================================================================================

class sklearn.linear\_model.LogisticRegression(_penalty\='deprecated'_, _\*_, _C\=1.0_, _l1\_ratio\=0.0_, _dual\=False_, _tol\=0.0001_, _fit\_intercept\=True_, _intercept\_scaling\=1_, _class\_weight\=None_, _random\_state\=None_, _solver\='lbfgs'_, _max\_iter\=100_, _verbose\=0_, _warm\_start\=False_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L974)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "Link to this definition")

Logistic Regression (aka logit, MaxEnt) classifier.

This class implements regularized logistic regression using a set of available solvers. **Note that regularization is applied by default**. It can handle both dense and sparse input `X`. Use C-ordered arrays or CSR matrices containing 64-bit floats for optimal performance; any other input format will be converted (and copied).

The solvers ‘lbfgs’, ‘newton-cg’, ‘newton-cholesky’ and ‘sag’ support only L2 regularization with primal formulation, or no regularization. The ‘liblinear’ solver supports both L1 and L2 regularization (but not both, i.e. elastic-net), with a dual formulation only for the L2 penalty. The Elastic-Net (combination of L1 and L2) regularization is only supported by the ‘saga’ solver.

For [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 problems (whenever `n_classes >= 3`), all solvers except ‘liblinear’ optimize the (penalized) multinomial loss. ‘liblinear’ only handles binary classification but can be extended to handle multiclass by using [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
.

Parameters:

**penalty**{‘l1’, ‘l2’, ‘elasticnet’, None}, default=’l2’

Specify the norm of the penalty:

*   `None`: no penalty is added;
    
*   `'l2'`: add an L2 penalty term and it is the default choice;
    
*   `'l1'`: add an L1 penalty term;
    
*   `'elasticnet'`: both L1 and L2 penalty terms are added.
    

Warning

Some penalties may not work with some solvers. See the parameter `solver` below, to know the compatibility between the penalty and solver.

Added in version 0.19: l1 penalty with SAGA solver (allowing ‘multinomial’ + L1)

Deprecated since version 1.8: `penalty` was deprecated in version 1.8 and will be removed in 1.10. Use `l1_ratio` and `C` instead. `l1_ratio=0` for `penalty='l2'`, `l1_ratio=1` for `penalty='l1'`, `l1_ratio` set to any float between 0 and 1 for `penalty='elasticnet'`, and `C=np.inf` for `penalty=None`.

**C**float, default=1.0

Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization. `C=np.inf` results in unpenalized logistic regression. For a visual example on the effect of tuning the `C` parameter with an L1 penalty, see: [Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#sphx-glr-auto-examples-linear-model-plot-logistic-path-py)
.

**l1\_ratio**float, default=0.0

The Elastic-Net mixing parameter, with `0 <= l1_ratio <= 1`. Setting `l1_ratio=1` gives a pure L1-penalty, setting `l1_ratio=0` a pure L2-penalty. Any value between 0 and 1 gives an Elastic-Net penalty of the form `l1_ratio * L1 + (1 - l1_ratio) * L2`.

Warning

Certain values of `l1_ratio`, i.e. some penalties, may not work with some solvers. See the parameter `solver` below, to know the compatibility between the penalty and solver.

Changed in version 1.8: Default value changed from None to 0.0.

Deprecated since version 1.8: `None` is deprecated and will be removed in version 1.10. Always use `l1_ratio` to specify the penalty type.

**dual**bool, default=False

Dual (constrained) or primal (regularized, see also [this equation](https://scikit-learn.org/stable/modules/linear_model.html#regularized-logistic-loss)
) formulation. Dual formulation is only implemented for l2 penalty with liblinear solver. Prefer `dual=False` when n\_samples > n\_features.

**tol**float, default=1e-4

Tolerance for stopping criteria.

**fit\_intercept**bool, default=True

Specifies if a constant (a.k.a. bias or intercept) should be added to the decision function.

**intercept\_scaling**float, default=1

Useful only when the solver `liblinear` is used and `self.fit_intercept` is set to `True`. In this case, `x` becomes `[x, self.intercept_scaling]`, i.e. a “synthetic” feature with constant value equal to `intercept_scaling` is appended to the instance vector. The intercept becomes `intercept_scaling * synthetic_feature_weight`.

Note

The synthetic feature weight is subject to L1 or L2 regularization as all other features. To lessen the effect of regularization on synthetic feature weight (and therefore on the intercept) `intercept_scaling` has to be increased.

**class\_weight**dict or ‘balanced’, default=None

Weights associated with classes in the form `{class_label: weight}`. If not given, all classes are supposed to have weight one.

The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as `n_samples / (n_classes * np.bincount(y))`.

Note that these weights will be multiplied with sample\_weight (passed through the fit method) if sample\_weight is specified.

Added in version 0.17: _class\_weight=’balanced’_

**random\_state**int, RandomState instance, default=None

Only used for `solver` == ‘sag’, ‘saga’ or ‘liblinear’ to shuffle the data. It has no effect on the other solvers. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

**solver**{‘lbfgs’, ‘liblinear’, ‘newton-cg’, ‘newton-cholesky’, ‘sag’, ‘saga’}, default=’lbfgs’

Algorithm to use in the optimization problem. Default is ‘lbfgs’. To choose a solver, you might want to consider the following aspects:

*   ‘lbfgs’ is a good default solver because it works reasonably well for a wide class of problems.
    
*   For [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
     problems (`n_classes >= 3`), all solvers except ‘liblinear’ minimize the full multinomial loss, ‘liblinear’ will raise an error.
    
*   ‘newton-cholesky’ is a good choice for `n_samples` >> `n_features * n_classes`, especially with one-hot encoded categorical features with rare categories. Be aware that the memory usage of this solver has a quadratic dependency on `n_features * n_classes` because it explicitly computes the full Hessian matrix.
    
*   For small datasets, ‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones;
    
*   ‘liblinear’ can only handle binary classification by default. To apply a one-versus-rest scheme for the multiclass setting one can wrap it with the [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
    .
    

Warning

The choice of the algorithm depends on the penalty chosen (`l1_ratio=0` for L2-penalty, `l1_ratio=1` for L1-penalty and `0 < l1_ratio < 1` for Elastic-Net) and on (multinomial) multiclass support:

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

See also

Refer to the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
 for more information regarding [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 and more specifically the [Table](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression-solvers)
 summarizing solver/penalty supports.

Added in version 0.17: Stochastic Average Gradient (SAG) descent solver. Multinomial support in version 0.18.

Added in version 0.19: SAGA solver.

Changed in version 0.22: The default solver changed from ‘liblinear’ to ‘lbfgs’ in 0.22.

Added in version 1.2: newton-cholesky solver. Multinomial support in version 1.6.

**max\_iter**int, default=100

Maximum number of iterations taken for the solvers to converge.

**verbose**int, default=0

For the liblinear and lbfgs solvers set verbose to any positive number for verbosity.

**warm\_start**bool, default=False

When set to True, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution. Useless for liblinear solver. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

Added in version 0.17: _warm\_start_ to support _lbfgs_, _newton-cg_, _sag_, _saga_ solvers.

**n\_jobs**int, default=None

Does not have any effect.

Deprecated since version 1.8: `n_jobs` is deprecated in version 1.8 and will be removed in 1.10.

Attributes:

**classes\_**ndarray of shape (n\_classes, )

A list of class labels known to the classifier.

**coef\_**ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)

Coefficients of the features in the decision function.

`coef_` is of shape (1, n\_features) when the given problem is binary.

By default, it will be created as a dense array, but can be turned to sparse (CSR format) through [`sparsify`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.sparsify "sklearn.linear_model.LogisticRegression.sparsify")
 (which can be beneficial under L1 regularization when many coefficients are zero), and back to dense through [`densify`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.densify "sklearn.linear_model.LogisticRegression.densify")
.

**intercept\_**ndarray of shape (1,) or (n\_classes,)

Intercept (a.k.a. bias) added to the decision function.

If `fit_intercept` is set to False, the intercept is set to zero. `intercept_` is of shape (1,) when the given problem is binary.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**ndarray of shape (1, )

Actual number of iterations for all classes.

Changed in version 0.20: In SciPy <= 1.0.0 the number of lbfgs iterations may exceed `max_iter`. `n_iter_` will now report at most `max_iter`.

See also

[`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")

Incrementally trained logistic regression (when given the parameter `loss="log_loss"`).

[`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")

Logistic regression with built-in cross validation.

Notes

For several reasons (floating point arithmetic, random number generators, etc.) the coefficients of a fitted model might differ slightly (among machines, scikit-learn versions, etc.) for the same input data. If that happens and you want to avoid it, you can try with a smaller `tol` parameter.

Predict output may not match that of standalone liblinear in certain cases. See [differences from liblinear](https://scikit-learn.org/stable/modules/linear_model.html#liblinear-differences)
 in the narrative documentation.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> clf \= LogisticRegression(random\_state\=0).fit(X, y)
\>>> clf.predict(X\[:2, :\])
array(\[0, 0\])
\>>> clf.predict\_proba(X\[:2, :\])
array(\[\[9.82e-01, 1.82e-02, 1.44e-08\],\
       \[9.72e-01, 2.82e-02, 3.02e-08\]\])
\>>> clf.score(X, y)
0.97

Copy to clipboard

For a comparison of the LogisticRegression with other classifiers see: [Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-auto-examples-classification-plot-classification-probability-py)
.

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L366)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.decision_function "Link to this definition")

Predict confidence scores for samples.

The confidence score for a sample is proportional to the signed distance of that sample to the hyperplane.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the confidence scores.

Returns:

**scores**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Confidence scores per `(n_samples, n_classes)` combination. In the binary case, confidence score for `self.classes_[1]` where >0 means this class would be predicted.

densify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.densify "Link to this definition")

Convert coefficient matrix to dense array format.

Converts the `coef_` member (back) to a numpy.ndarray. This is the default format of `coef_` and is required for fitting, so calling this method is only required on models that have previously been sparsified; otherwise, it is a no-op.

Returns:

self

Fitted estimator.

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1332)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.fit "Link to this definition")

Fit the model according to the given training data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target vector relative to X.

**sample\_weight**array-like of shape (n\_samples,) default=None

Array of weights that are assigned to individual samples. If not provided, then each sample is given unit weight.

Added in version 0.17: _sample\_weight_ support to LogisticRegression.

Returns:

self

Fitted estimator.

Notes

The SAGA solver supports both float64 and float32 bit arrays.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L398)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict "Link to this definition")

Predict class labels for samples in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the predictions.

Returns:

**y\_pred**ndarray of shape (n\_samples,)

Vector containing the class labels for each sample.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1605)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict_log_proba "Link to this definition")

Predict logarithm of probability estimates.

The returned estimates for all classes are ordered by the label of classes.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Vector to be scored, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**T**array-like of shape (n\_samples, n\_classes)

Returns the log-probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1573)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict_proba "Link to this definition")

Probability estimates.

The returned estimates for all classes are ordered by the label of classes.

For a multiclass / multinomial problem the softmax function is used to find the predicted probability of each class.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Vector to be scored, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**T**array-like of shape (n\_samples, n\_classes)

Returns the probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.score "Link to this definition")

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

set\_callbacks(_\*callbacks_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_logistic.py#L1311)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.set_callbacks "Link to this definition")

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
 \= '$UNCHANGED$'_) → [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model._logistic.LogisticRegression")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model._logistic.LogisticRegression")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.set_score_request "Link to this definition")

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

sparsify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L480)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.sparsify "Link to this definition")

Convert coefficient matrix to sparse format.

Converts the `coef_` member to a scipy.sparse matrix, which for L1-regularized models can be much more memory- and storage-efficient than the usual numpy.ndarray representation.

The `intercept_` member is not converted.

Warning

This method is not supported for estimators fitted with array API inputs (i.e. when [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
 is used with `array_api_dispatch=True`). The call may succeed but subsequent calls to [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.predict "sklearn.linear_model.LogisticRegression.predict")
 and other methods involving passing arrays may raise or return unexpected results.

Returns:

self

Fitted estimator.

Notes

For non-sparse models, i.e. when there are not many zeros in `coef_`, this may actually _increase_ memory usage, so use this method with care. A rule of thumb is that the number of zero elements, which can be computed with `(coef_ == 0).sum()`, must be more than 50% for this to provide significant benefits.

After calling this method, further fitting with the partial\_fit method (if any) will not work until you call densify.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)

[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)

Pipelining: chaining a PCA and a logistic regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_digits_thumb.png)

[Recursive feature elimination](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html)

Recursive feature elimination

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)

[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Recursive feature elimination with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_thumb.png)

[Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_estimator_representation_thumb.png)

[Displaying estimators and complex pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_estimator_representation.html)

Displaying estimators and complex pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)

[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)

Displaying Pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_likelihood_ratios_thumb.png)

[Class Likelihood Ratios to measure classification performance](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html)

Class Likelihood Ratios to measure classification performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_thumb.png)

[Multilabel classification using a classifier chain](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Multilabel classification using a classifier chain

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_0_0_thumb.png)

[Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html)

Release Highlights for scikit-learn 1.0

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)

[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)

Release Highlights for scikit-learn 1.8

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)