[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.LassoLarsIC.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LassoLarsIC.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.LassoLarsIC.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LassoLarsIC.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LassoLarsIC.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.LassoLarsIC.html)

Collapse Sidebar Expand Sidebar

LassoLarsIC[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#lassolarsic "Link to this heading")

===========================================================================================================================================

class sklearn.linear\_model.LassoLarsIC(_criterion\='aic'_, _\*_, _fit\_intercept\=True_, _verbose\=False_, _precompute\='auto'_, _max\_iter\=500_, _eps\=np.float64(2.220446049250313e-16)_, _copy\_X\=True_, _positive\=False_, _noise\_variance\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_least_angle.py#L2032)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "Link to this definition")

Lasso model fit with Lars using BIC or AIC for model selection.

The optimization objective for Lasso is:

(1 / (2 \* n\_samples)) \* ||y \- Xw||^2\_2 + alpha \* ||w||\_1

Copy to clipboard

AIC is the Akaike information criterion [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#rde9cc43d0d41-2)
 and BIC is the Bayes Information criterion [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#rde9cc43d0d41-3)
. Such criteria are useful to select the value of the regularization parameter by making a trade-off between the goodness of fit and the complexity of the model. A good model should explain well the data while being simple.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#lasso-lars-ic)
.

Parameters:

**criterion**{‘aic’, ‘bic’}, default=’aic’

The type of criterion to use.

**fit\_intercept**bool, default=True

Whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations (i.e. data is expected to be centered).

**verbose**bool or int, default=False

Sets the verbosity amount.

**precompute**bool, ‘auto’ or array-like, default=’auto’

Whether to use a precomputed Gram matrix to speed up calculations. If set to `'auto'` let us decide. The Gram matrix can also be passed as argument.

**max\_iter**int, default=500

Maximum number of iterations to perform. Can be used for early stopping.

**eps**float, default=np.finfo(float).eps

The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Unlike the `tol` parameter in some iterative optimization-based algorithms, this parameter does not control the tolerance of the optimization.

**copy\_X**bool, default=True

If True, X will be copied; else, it may be overwritten.

**positive**bool, default=False

Restrict coefficients to be >= 0. Be aware that you might want to remove fit\_intercept which is set True by default. Under the positive restriction the model coefficients do not converge to the ordinary-least-squares solution for small values of alpha. Only coefficients up to the smallest alpha value (`alphas_[alphas_ > 0.].min()` when fit\_path=True) reached by the stepwise Lars-Lasso algorithm are typically in congruence with the solution of the coordinate descent Lasso estimator. As a consequence using LassoLarsIC only makes sense for problems where a sparse solution is expected and/or reached.

**noise\_variance**float, default=None

The estimated noise variance of the data. If `None`, an unbiased estimate is computed by an OLS model. However, it is only possible in the case where `n_samples > n_features + fit_intercept`.

Added in version 1.1.

Attributes:

**coef\_**array-like of shape (n\_features,)

parameter vector (w in the formulation formula)

**intercept\_**float

independent term in decision function.

**alpha\_**float

the alpha parameter chosen by the information criterion

**alphas\_**array-like of shape (n\_alphas + 1,) or list of such arrays

Maximum of covariances (in absolute value) at each iteration. `n_alphas` is either `max_iter`, `n_features` or the number of nodes in the path with `alpha >= alpha_min`, whichever is smaller. If a list, it will be of length `n_targets`.

**n\_iter\_**int

number of iterations run by lars\_path to find the grid of alphas.

**criterion\_**array-like of shape (n\_alphas,)

The value of the information criteria (‘aic’, ‘bic’) across all alphas. The alpha which has the smallest information criterion is chosen, as specified in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#rde9cc43d0d41-1)
.

**noise\_variance\_**float

The estimated noise variance from the data used to compute the criterion.

Added in version 1.1.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")

Compute Lasso path with coordinate descent.

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

Linear Model trained with L1 prior as regularizer (aka the Lasso).

[`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")

Lasso linear model with iterative fitting along a regularization path.

[`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")

Lasso model fit with Least Angle Regression a.k.a. Lars.

[`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")

Cross-validated Lasso, using the LARS algorithm.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Sparse coding.

Notes

The number of degrees of freedom is computed as in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#rde9cc43d0d41-1)
.

To have more details regarding the mathematical formulation of the AIC and BIC criteria, please refer to [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#lasso-lars-ic)
.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#id3)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#id4)
)

[Zou, Hui, Trevor Hastie, and Robert Tibshirani. “On the degrees of freedom of the lasso.” The Annals of Statistics 35.5 (2007): 2173-2192.](https://arxiv.org/abs/0712.0881)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#id1)\
\]

[Wikipedia entry on the Akaike information criterion](https://en.wikipedia.org/wiki/Akaike_information_criterion)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#id2)\
\]

[Wikipedia entry on the Bayesian information criterion](https://en.wikipedia.org/wiki/Bayesian_information_criterion)

Examples

\>>> from sklearn import linear\_model
\>>> reg \= linear\_model.LassoLarsIC(criterion\='bic')
\>>> X \= \[\[\-2, 2\], \[\-1, 1\], \[0, 0\], \[1, 1\], \[2, 2\]\]
\>>> y \= \[\-2.2222, \-1.1111, 0, \-1.1111, \-2.2222\]
\>>> reg.fit(X, y)
LassoLarsIC(criterion='bic')
\>>> print(reg.coef\_)
\[ 0.  -1.11\]

Copy to clipboard

For a detailed example of using this class, see [Lasso model selection via information criteria](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#sphx-glr-auto-examples-linear-model-plot-lasso-lars-ic-py)
.

fit(_X_, _y_, _copy\_X\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_least_angle.py#L2227)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.fit "Link to this definition")

Fit the model using X, y as training data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,)

Target values. Will be cast to X’s dtype if necessary.

**copy\_X**bool, default=None

If provided, this parameter will override the choice of copy\_X made at instance creation. If `True`, X will be copied; else, it may be overwritten.

Returns:

**self**object

Returns an instance of self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.score "Link to this definition")

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

set\_fit\_request(_\*_, _copy\_X: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model._least_angle.LassoLarsIC")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.set_fit_request "Link to this definition")

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

**copy\_X**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `copy_X` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model._least_angle.LassoLarsIC")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lars_ic_thumb.png)

[Lasso model selection via information criteria](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html)

Lasso model selection via information criteria

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_thumb.png)

[Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)

Lasso model selection: AIC-BIC / cross-validation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)