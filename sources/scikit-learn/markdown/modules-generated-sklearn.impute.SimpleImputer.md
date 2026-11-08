[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.impute.SimpleImputer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.impute.SimpleImputer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.impute.SimpleImputer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.impute.SimpleImputer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.impute.SimpleImputer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.impute.SimpleImputer.html)

Collapse Sidebar Expand Sidebar

SimpleImputer[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#simpleimputer "Link to this heading")

===========================================================================================================================================

class sklearn.impute.SimpleImputer(_\*_, _missing\_values\=nan_, _strategy\='mean'_, _fill\_value\=None_, _copy\=True_, _add\_indicator\=False_, _keep\_empty\_features\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L171)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "Link to this definition")

Univariate imputer for completing missing values with simple strategies.

Replace missing values using a descriptive statistic (e.g. mean, median, or most frequent) along each column, or using a constant value.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/impute.html#impute)
.

Added in version 0.20: `SimpleImputer` replaces the previous `sklearn.preprocessing.Imputer` estimator which is now removed.

Parameters:

**missing\_values**int, float, str, np.nan, None or pandas.NA, default=np.nan

The placeholder for the missing values. All occurrences of `missing_values` will be imputed. For pandas’ dataframes with nullable integer dtypes with missing values, `missing_values` can be set to either `np.nan` or `pd.NA`.

**strategy**str or Callable, default=’mean’

The imputation strategy.

*   If “mean”, then replace missing values using the mean along each column. Can only be used with numeric data.
    
*   If “median”, then replace missing values using the median along each column. Can only be used with numeric data.
    
*   If “most\_frequent”, then replace missing using the most frequent value along each column. Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.
    
*   If “constant”, then replace missing values with fill\_value. Can be used with strings or numeric data.
    
*   If an instance of Callable, then replace missing values using the scalar statistic returned by running the callable over a dense 1d array containing non-missing values of each column.
    

Added in version 0.20: strategy=”constant” for fixed value imputation.

Added in version 1.5: strategy=callable for custom value imputation.

**fill\_value**str or numerical value, default=None

When strategy == “constant”, `fill_value` is used to replace all occurrences of missing\_values. For string or object data types, `fill_value` must be a string. If `None`, `fill_value` will be 0 when imputing numerical data and “missing\_value” for strings or object data types.

**copy**bool, default=True

If True, a copy of X will be created. If False, imputation will be done in-place whenever possible. Note that, in the following cases, a new copy will always be made, even if `copy=False`:

*   If `X` is not an array of floating values;
    
*   If `X` is encoded as a CSR matrix;
    
*   If `add_indicator=True`.
    

**add\_indicator**bool, default=False

If True, a [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
 transform will stack onto output of the imputer’s transform. This allows a predictive estimator to account for missingness despite imputation. If a feature has no missing values at fit/train time, the feature won’t appear on the missing indicator even if there are missing values at transform/test time.

**keep\_empty\_features**bool, default=False

If True, features that consist exclusively of missing values when `fit` is called are returned in results when `transform` is called. The imputed value is always `0` except when `strategy="constant"` in which case `fill_value` will be used instead.

Added in version 1.2.

Attributes:

**statistics\_**array of shape (n\_features,)

The imputation fill value for each feature. Computing statistics can result in `np.nan` values. During [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.transform "sklearn.impute.SimpleImputer.transform")
, features corresponding to `np.nan` statistics will be discarded.

**indicator\_**[`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")

Indicator used to add binary indicators for missing values. `None` if `add_indicator=False`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")

Multivariate imputer that estimates values to impute for each feature with missing values from all the others.

[`KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")

Multivariate imputer that estimates missing features using nearest samples.

Notes

Columns which only contained missing values at [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit "sklearn.impute.SimpleImputer.fit")
 are discarded upon [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.transform "sklearn.impute.SimpleImputer.transform")
 if strategy is not `"constant"`.

In a prediction context, simple imputation usually performs poorly when associated with a weak learner. However, with a powerful learner, it can lead to as good or better performance than complex imputation such as [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 or [`KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
.

Examples

\>>> import numpy as np
\>>> from sklearn.impute import SimpleImputer
\>>> imp\_mean \= SimpleImputer(missing\_values\=np.nan, strategy\='mean')
\>>> imp\_mean.fit(\[\[7, 2, 3\], \[4, np.nan, 6\], \[10, 5, 9\]\])
SimpleImputer()
\>>> X \= \[\[np.nan, 2, 3\], \[4, np.nan, 6\], \[10, np.nan, 9\]\]
\>>> print(imp\_mean.transform(X))
\[\[ 7.   2.   3. \]\
 \[ 4.   3.5  6. \]\
 \[10.   3.5  9. \]\]

Copy to clipboard

For a more detailed example see [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)
.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L430)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit "Link to this definition")

Fit the imputer on `X`.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)

Input data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L760)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L690)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.inverse_transform "Link to this definition")

Convert the data back to the original representation.

Inverts the `transform` operation performed on an array. This operation can only be performed after [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 is instantiated with `add_indicator=True`.

Note that `inverse_transform` can only invert the transform in features that have binary indicators for missing values. If a feature has no missing values at `fit` time, the feature won’t have a binary indicator, and the imputation done at `transform` time won’t be inverted.

Added in version 0.24.

Parameters:

**X**array-like of shape (n\_samples, n\_features + n\_features\_missing\_indicator)

The imputed data to be reverted to original data. It has to be an augmented array of imputed data and the missing indicator mask.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

The original `X` with missing values as it was prior to imputation.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L601)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.transform "Link to this definition")

Impute all missing values in `X`.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)

The input data to complete.

Returns:

**X\_imputed**{ndarray, sparse matrix} of shape (n\_samples, n\_features\_out)

`X` with imputed values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_estimator_representation_thumb.png)

[Displaying estimators and complex pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_estimator_representation.html)

Displaying estimators and complex pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)

[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)

Displaying Pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)