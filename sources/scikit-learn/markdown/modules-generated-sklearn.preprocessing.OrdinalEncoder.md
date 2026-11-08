[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)

Collapse Sidebar Expand Sidebar

OrdinalEncoder[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#ordinalencoder "Link to this heading")

=====================================================================================================================================================

class sklearn.preprocessing.OrdinalEncoder(_\*_, _categories\='auto'_, _dtype\=<class 'numpy.float64'>_, _handle\_unknown\='error'_, _unknown\_value\=None_, _encoded\_missing\_value\=nan_, _min\_frequency\=None_, _max\_categories\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "Link to this definition")

Encode categorical features as an integer array.

The input to this transformer should be an array-like of integers or strings, denoting the values taken on by categorical (discrete) features. The features are converted to ordinal integers. This results in a single column of integers (0 to n\_categories - 1) per feature.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features)
. For a comparison of different encoders, refer to: [Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#sphx-glr-auto-examples-preprocessing-plot-target-encoder-py)
.

Added in version 0.20.

Parameters:

**categories**‘auto’ or a list of array-like, default=’auto’

Categories (unique values) per feature:

*   ‘auto’ : Determine categories automatically from the training data.
    
*   list : `categories[i]` holds the categories expected in the ith column. The passed categories should not mix strings and numeric values, and should be sorted in case of numeric values.
    

The used categories can be found in the `categories_` attribute.

**dtype**number type, default=np.float64

Desired dtype of output.

**handle\_unknown**{‘error’, ‘use\_encoded\_value’}, default=’error’

When set to ‘error’ an error will be raised in case an unknown categorical feature is present during transform. When set to ‘use\_encoded\_value’, the encoded value of unknown categories will be set to the value given for the parameter `unknown_value`. In [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.inverse_transform "sklearn.preprocessing.OrdinalEncoder.inverse_transform")
, an unknown category will be denoted as None.

Added in version 0.24.

**unknown\_value**int or np.nan, default=None

When the parameter handle\_unknown is set to ‘use\_encoded\_value’, this parameter is required and will set the encoded value of unknown categories. It has to be distinct from the values used to encode any of the categories in `fit`. If set to np.nan, the `dtype` parameter must be a float dtype.

Added in version 0.24.

**encoded\_missing\_value**int or np.nan, default=np.nan

Encoded value of missing categories. If set to `np.nan`, then the `dtype` parameter must be a float dtype.

Added in version 1.1.

**min\_frequency**int or float, default=None

Specifies the minimum frequency below which a category will be considered infrequent.

*   If `int`, categories with a smaller cardinality will be considered infrequent.
    
*   If `float`, categories with a smaller cardinality than `min_frequency * n_samples` will be considered infrequent.
    

Added in version 1.3: Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)
.

**max\_categories**int, default=None

Specifies an upper limit to the number of output categories for each input feature when considering infrequent categories. If there are infrequent categories, `max_categories` includes the category representing the infrequent categories along with the frequent categories. If `None`, there is no limit to the number of output features.

`max_categories` do **not** take into account missing or unknown categories. Setting `unknown_value` or `encoded_missing_value` to an integer will increase the number of unique integer codes by one each. This can result in up to `max_categories + 2` integer codes.

Added in version 1.3: Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)
.

Attributes:

**categories\_**list of arrays

The categories of each feature determined during `fit` (in order of the features in X and corresponding with the output of `transform`). This does not include categories that weren’t seen during `fit`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 1.0.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

`infrequent_categories_`list of ndarray

Infrequent categories for each feature.

See also

[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

Performs a one-hot encoding of categorical features. This encoding is suitable for low to medium cardinality categorical variables, both in supervised and unsupervised settings.

[`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")

Encodes categorical features using supervised signal in a classification or regression pipeline. This encoding is typically suitable for high cardinality categorical variables.

[`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")

Encodes target labels with values between 0 and `n_classes-1`.

Examples

Given a dataset with two features, we let the encoder find the unique values per feature and transform the data to an ordinal encoding.

\>>> from sklearn.preprocessing import OrdinalEncoder
\>>> enc \= OrdinalEncoder()
\>>> X \= \[\['Male', 1\], \['Female', 3\], \['Female', 2\]\]
\>>> enc.fit(X)
OrdinalEncoder()
\>>> enc.categories\_
\[array(\['Female', 'Male'\], dtype=object), array(\[1, 2, 3\], dtype=object)\]
\>>> enc.transform(\[\['Female', 3\], \['Male', 1\]\])
array(\[\[0., 2.\],\
       \[1., 0.\]\])

Copy to clipboard

\>>> enc.inverse\_transform(\[\[1, 0\], \[0, 1\]\])
array(\[\['Male', 1\],\
       \['Female', 2\]\], dtype=object)

Copy to clipboard

By default, [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
 is lenient towards missing values by propagating them.

\>>> import numpy as np
\>>> X \= \[\['Male', 1\], \['Female', 3\], \['Female', np.nan\]\]
\>>> enc.fit\_transform(X)
array(\[\[ 1.,  0.\],\
       \[ 0.,  1.\],\
       \[ 0., nan\]\])

Copy to clipboard

You can use the parameter `encoded_missing_value` to encode missing values.

\>>> enc.set\_params(encoded\_missing\_value\=-1).fit\_transform(X)
array(\[\[ 1.,  0.\],\
       \[ 0.,  1.\],\
       \[ 0., -1.\]\])

Copy to clipboard

Infrequent categories are enabled by setting `max_categories` or `min_frequency`. In the following example, “a” and “d” are considered infrequent and grouped together into a single category, “b” and “c” are their own categories, unknown values are encoded as 3 and missing values are encoded as 4.

\>>> X\_train \= np.array(
...     \[\["a"\] \* 5 + \["b"\] \* 20 + \["c"\] \* 10 + \["d"\] \* 3 + \[np.nan\]\],
...     dtype\=object).T
\>>> enc \= OrdinalEncoder(
...     handle\_unknown\="use\_encoded\_value", unknown\_value\=3,
...     max\_categories\=3, encoded\_missing\_value\=4)
\>>> \_ \= enc.fit(X\_train)
\>>> X\_test \= np.array(\[\["a"\], \["b"\], \["c"\], \["d"\], \["e"\], \[np.nan\]\], dtype\=object)
\>>> enc.transform(X\_test)
array(\[\[2.\],\
       \[0.\],\
       \[1.\],\
       \[2.\],\
       \[3.\],\
       \[4.\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1475)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.fit "Link to this definition")

Fit the OrdinalEncoder to X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to determine the categories of each feature.

**y**None

Ignored. This parameter exists only for compatibility with [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
.

Returns:

**self**object

Fitted encoder.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L994)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Same as input features.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1616)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.inverse_transform "Link to this definition")

Convert the data back to the original representation.

Parameters:

**X**array-like of shape (n\_samples, n\_encoded\_features)

The transformed data.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Inverse transformed array.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1584)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.transform "Link to this definition")

Transform X to ordinal codes.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to encode.

Returns:

**X\_out**ndarray of shape (n\_samples, n\_features)

Transformed input.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)

[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)

Partial Dependence and Individual Conditional Expectation Plots

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)

[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)

Comparing Target Encoder with Other Encoders

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)