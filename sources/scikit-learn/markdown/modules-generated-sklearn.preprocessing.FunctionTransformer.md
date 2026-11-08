[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.FunctionTransformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.FunctionTransformer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.FunctionTransformer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.FunctionTransformer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.FunctionTransformer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.FunctionTransformer.html)

Collapse Sidebar Expand Sidebar

FunctionTransformer[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#functiontransformer "Link to this heading")

====================================================================================================================================================================

class sklearn.preprocessing.FunctionTransformer(_func\=None_, _inverse\_func\=None_, _\*_, _validate\=False_, _accept\_sparse\=False_, _check\_inverse\=True_, _feature\_names\_out\=None_, _kw\_args\=None_, _inv\_kw\_args\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_function_transformer.py#L29)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "Link to this definition")

Constructs a transformer from an arbitrary callable.

A FunctionTransformer forwards its X (and optionally y) arguments to a user-defined function or function object and returns the result of this function. This is useful for stateless transformations such as taking the log of frequencies, doing custom scaling, etc.

Note: If a lambda is used as the function, then the resulting transformer will not be pickleable.

Added in version 0.17.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#function-transformer)
.

Parameters:

**func**callable, default=None

The callable to use for the transformation. This will be passed the same arguments as transform, with args and kwargs forwarded. If func is None, then func will be the identity function.

**inverse\_func**callable, default=None

The callable to use for the inverse transformation. This will be passed the same arguments as inverse transform, with args and kwargs forwarded. If inverse\_func is None, then inverse\_func will be the identity function.

**validate**bool, default=False

Indicate that the input X array should be checked before calling `func`. The possibilities are:

*   If False, there is no input validation.
    
*   If True, then X will be converted to a 2-dimensional NumPy array or sparse matrix. If the conversion is not possible an exception is raised.
    

Changed in version 0.22: The default of `validate` changed from True to False.

**accept\_sparse**bool, default=False

Indicate that func accepts a sparse matrix as input. If validate is False, this has no effect. Otherwise, if accept\_sparse is false, sparse matrix inputs will cause an exception to be raised.

**check\_inverse**bool, default=True

Whether to check that or `func` followed by `inverse_func` leads to the original inputs. It can be used for a sanity check, raising a warning when the condition is not fulfilled.

Added in version 0.20.

**feature\_names\_out**callable, ‘one-to-one’ or None, default=None

Determines the list of feature names that will be returned by the `get_feature_names_out` method. If it is ‘one-to-one’, then the output feature names will be equal to the input feature names. If it is a callable, then it must take two positional arguments: this `FunctionTransformer` (`self`) and an array-like of input feature names (`input_features`). It must return an array-like of output feature names. The `get_feature_names_out` method is only defined if `feature_names_out` is not None.

See `get_feature_names_out` for more details.

Added in version 1.1.

**kw\_args**dict, default=None

Dictionary of additional keyword arguments to pass to func.

Added in version 0.18.

**inv\_kw\_args**dict, default=None

Dictionary of additional keyword arguments to pass to inverse\_func.

Added in version 0.18.

Attributes:

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")

Scale each feature by its maximum absolute value.

[`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

Standardize features by removing the mean and scaling to unit variance.

[`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")

Binarize labels in a one-vs-all fashion.

[`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")

Transform between iterable of iterables and a multilabel format.

Notes

If `func` returns an output with a `columns` attribute, then the columns is enforced to be consistent with the output of `get_feature_names_out`.

Examples

\>>> import numpy as np
\>>> from sklearn.preprocessing import FunctionTransformer
\>>> transformer \= FunctionTransformer(np.log1p)
\>>> X \= np.array(\[\[0, 1\], \[2, 3\]\])
\>>> transformer.transform(X)
array(\[\[0.       , 0.6931\],\
       \[1.0986, 1.3862\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_function_transformer.py#L206)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.fit "Link to this definition")

Fit transformer by checking X.

If `validate` is `True`, `X` will be checked.

Parameters:

**X**{array-like, sparse-matrix} of shape (n\_samples, n\_features) if `validate=True` else any object that `func` can handle

Input array.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

FunctionTransformer class instance.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_function_transformer.py#L329)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

This method is only defined if `feature_names_out` is not None.

Parameters:

**input\_features**array-like of str or None, default=None

Input feature names.

*   If `input_features` is None, then `feature_names_in_` is used as the input feature names. If `feature_names_in_` is not defined, then names are generated: `[x0, x1, ..., x(n_features_in_ - 1)]`.
    
*   If `input_features` is array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

*   If `feature_names_out` is ‘one-to-one’, the input feature names are returned (see `input_features` above). This requires `feature_names_in_` and/or `n_features_in_` to be defined, which is done automatically if `validate=True`. Alternatively, you can set them in `func`.
    
*   If `feature_names_out` is a callable, then it is called with two arguments, `self` and `input_features`, and its return value is returned by this method.
    

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_function_transformer.py#L311)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.inverse_transform "Link to this definition")

Transform X using the inverse function.

Parameters:

**X**{array-like, sparse-matrix} of shape (n\_samples, n\_features) if `validate=True` else any object that `inverse_func` can handle

Input array.

Returns:

**X\_original**array-like, shape (n\_samples, n\_features)

Transformed input.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_function_transformer.py#L394)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_function_transformer.py#L237)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.transform "Link to this definition")

Transform X using the forward function.

Parameters:

**X**{array-like, sparse-matrix} of shape (n\_samples, n\_features) if `validate=True` else any object that `func` can handle

Input array.

Returns:

**X\_out**array-like, shape (n\_samples, n\_features)

Transformed input.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)