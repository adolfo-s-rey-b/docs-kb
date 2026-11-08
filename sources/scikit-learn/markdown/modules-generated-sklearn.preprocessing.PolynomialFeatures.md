[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

Collapse Sidebar Expand Sidebar

PolynomialFeatures[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#polynomialfeatures "Link to this heading")

=================================================================================================================================================================

class sklearn.preprocessing.PolynomialFeatures(_degree\=2_, _\*_, _interaction\_only\=False_, _include\_bias\=True_, _order\='C'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_polynomial.py#L92)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "Link to this definition")

Generate polynomial and interaction features.

Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree. For example, if an input sample is two dimensional and of the form \[a, b\], the degree-2 polynomial features are \[1, a, b, a^2, ab, b^2\].

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#polynomial-features)
.

Parameters:

**degree**int or tuple (min\_degree, max\_degree), default=2

If a single int is given, it specifies the maximal degree of the polynomial features. If a tuple `(min_degree, max_degree)` is passed, then `min_degree` is the minimum and `max_degree` is the maximum polynomial degree of the generated features. Note that `min_degree=0` and `min_degree=1` are equivalent as outputting the degree zero term is determined by `include_bias`.

**interaction\_only**bool, default=False

If `True`, only interaction features are produced: features that are products of at most `degree` _distinct_ input features, i.e. terms with power of 2 or higher of the same input feature are excluded:

*   included: `x[0]`, `x[1]`, `x[0] * x[1]`, etc.
    
*   excluded: `x[0] ** 2`, `x[0] ** 2 * x[1]`, etc.
    

**include\_bias**bool, default=True

If `True` (default), then include a bias column, the feature in which all polynomial powers are zero (i.e. a column of ones - acts as an intercept term in a linear model).

**order**{‘C’, ‘F’}, default=’C’

Order of output array in the dense case. `'F'` order is faster to compute, but may slow down subsequent estimators.

Added in version 0.21.

Attributes:

`powers_`ndarray of shape (`n_output_features_`, `n_features_in_`)

Exponent for each of the inputs in the output.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_output\_features\_**int

The total number of polynomial output features. The number of output features is computed by iterating over all suitably sized combinations of input features.

See also

[`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")

Transformer that generates univariate B-spline bases for features.

Notes

Be aware that the number of features in the output array scales polynomially in the number of features of the input array, and exponentially in the degree. High degrees can cause overfitting.

See [examples/linear\_model/plot\_polynomial\_interpolation.py](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html#sphx-glr-auto-examples-linear-model-plot-polynomial-interpolation-py)

Examples

\>>> import numpy as np
\>>> from sklearn.preprocessing import PolynomialFeatures
\>>> X \= np.arange(6).reshape(3, 2)
\>>> X
array(\[\[0, 1\],\
       \[2, 3\],\
       \[4, 5\]\])
\>>> poly \= PolynomialFeatures(2)
\>>> poly.fit\_transform(X)
array(\[\[ 1.,  0.,  1.,  0.,  0.,  1.\],\
       \[ 1.,  2.,  3.,  4.,  6.,  9.\],\
       \[ 1.,  4.,  5., 16., 20., 25.\]\])
\>>> poly \= PolynomialFeatures(interaction\_only\=True)
\>>> poly.fit\_transform(X)
array(\[\[ 1.,  0.,  1.,  0.\],\
       \[ 1.,  2.,  3.,  6.\],\
       \[ 1.,  4.,  5., 20.\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_polynomial.py#L298)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.fit "Link to this definition")

Compute number of output features.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Fitted transformer.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_polynomial.py#L259)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features is None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_polynomial.py#L395)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures.transform "Link to this definition")

Transform data to polynomial features.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to transform, row by row.

Prefer CSR over CSC for sparse input (for speed), but CSC is required if the degree is 4 or higher. If the degree is less than 4 and the input format is CSC, it will be converted to CSR, have its polynomial features generated, then converted back to CSC.

If the degree is 2 or 3, the method described in “Leveraging Sparsity to Speed Up Polynomial Feature Expansions of CSR Matrices Using K-Simplex Numbers” by Andrew Nystrom and John Hughes is used, which is much faster than the method used on CSC input. For this reason, a CSC input will be converted to CSR, and the output will be converted back to CSC prior to being returned, hence the preference of CSR.

Returns:

**XP**{ndarray, sparse matrix} of shape (n\_samples, NP)

The matrix of features, where `NP` is the number of polynomial features generated from the combination of inputs. If a sparse matrix is provided, it will be converted into CSR format.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_thumb.png)

[Polynomial and Spline interpolation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)

Polynomial and Spline interpolation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)

[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)

Robust linear estimator fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)

[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)

Displaying Pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_underfitting_overfitting_thumb.png)

[Underfitting vs. Overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)

Underfitting vs. Overfitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_thumb.png)

[Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html)

Plot classification boundaries with different SVM Kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)