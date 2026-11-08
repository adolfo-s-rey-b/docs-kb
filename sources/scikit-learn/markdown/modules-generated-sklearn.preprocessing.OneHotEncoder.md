[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.OneHotEncoder.html)

Collapse Sidebar Expand Sidebar

OneHotEncoder[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#onehotencoder "Link to this heading")

==================================================================================================================================================

class sklearn.preprocessing.OneHotEncoder(_\*_, _categories\='auto'_, _drop\=None_, _sparse\_output\=True_, _dtype\=<class 'numpy.float64'>_, _handle\_unknown\='error'_, _min\_frequency\=None_, _max\_categories\=None_, _feature\_name\_combiner\='concat'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L474)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "Link to this definition")

Encode categorical features as a one-hot numeric array.

The input to this transformer should be an array-like of integers or strings, denoting the values taken on by categorical (discrete) features. The features are encoded using a one-hot (aka ‘one-of-K’ or ‘dummy’) encoding scheme. This creates a binary column for each category and returns a sparse matrix or dense array (depending on the `sparse_output` parameter).

By default, the encoder derives the categories based on the unique values in each feature. Alternatively, you can also specify the `categories` manually.

This encoding is needed for feeding categorical data to many scikit-learn estimators, notably linear models and SVMs with the standard kernels.

Note: a one-hot encoding of y labels should use a LabelBinarizer instead.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features)
. For a comparison of different encoders, refer to: [Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#sphx-glr-auto-examples-preprocessing-plot-target-encoder-py)
.

Parameters:

**categories**‘auto’ or a list of array-like, default=’auto’

Categories (unique values) per feature:

*   ‘auto’ : Determine categories automatically from the training data.
    
*   list : `categories[i]` holds the categories expected in the ith column. The passed categories should not mix strings and numeric values within a single feature, and should be sorted in case of numeric values.
    

The used categories can be found in the `categories_` attribute.

Added in version 0.20.

**drop**{‘first’, ‘if\_binary’} or an array-like of shape (n\_features,), default=None

Specifies a methodology to use to drop one of the categories per feature. This is useful in situations where perfectly collinear features cause problems, such as when feeding the resulting data into an unregularized linear regression model.

However, dropping one category breaks the symmetry of the original representation and can therefore induce a bias in downstream models, for instance for penalized linear classification or regression models.

*   None : retain all features (the default).
    
*   ‘first’ : drop the first category in each feature. If only one category is present, the feature will be dropped entirely.
    
*   ‘if\_binary’ : drop the first category in each feature with two categories. Features with 1 or more than 2 categories are left intact.
    
*   array : `drop[i]` is the category in feature `X[:, i]` that should be dropped.
    

When `max_categories` or `min_frequency` is configured to group infrequent categories, the dropping behavior is handled after the grouping.

Added in version 0.21: The parameter `drop` was added in 0.21.

Changed in version 0.23: The option `drop='if_binary'` was added in 0.23.

Changed in version 1.1: Support for dropping infrequent categories.

**sparse\_output**bool, default=True

When `True`, it returns a SciPy sparse matrix/array in “Compressed Sparse Row” (CSR) format.

Added in version 1.2: `sparse` was renamed to `sparse_output`

**dtype**number type, default=np.float64

Desired dtype of output.

**handle\_unknown**{‘error’, ‘ignore’, ‘infrequent\_if\_exist’, ‘warn’}, default=’error’

Specifies the way unknown categories are handled during [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.transform "sklearn.preprocessing.OneHotEncoder.transform")
.

*   ‘error’ : Raise an error if an unknown category is present during transform.
    
*   ‘ignore’ : When an unknown category is encountered during transform, the resulting one-hot encoded columns for this feature will be all zeros. In the inverse transform, an unknown category will be denoted as None.
    
*   ‘infrequent\_if\_exist’ : When an unknown category is encountered during transform, the resulting one-hot encoded columns for this feature will map to the infrequent category if it exists. The infrequent category will be mapped to the last position in the encoding. During inverse transform, an unknown category will be mapped to the category denoted `'infrequent'` if it exists. If the `'infrequent'` category does not exist, then [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.transform "sklearn.preprocessing.OneHotEncoder.transform")
     and [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.inverse_transform "sklearn.preprocessing.OneHotEncoder.inverse_transform")
     will handle an unknown category as with `handle_unknown='ignore'`. Infrequent categories exist based on `min_frequency` and `max_categories`. Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)
    .
    
*   ‘warn’ : When an unknown category is encountered during transform a warning is issued, and the encoding then proceeds as described for `handle_unknown="infrequent_if_exist"`.
    

Changed in version 1.1: `'infrequent_if_exist'` was added to automatically handle unknown categories and infrequent categories.

Added in version 1.6: The option `"warn"` was added in 1.6.

**min\_frequency**int or float, default=None

Specifies the minimum frequency below which a category will be considered infrequent.

*   If `int`, categories with a smaller cardinality will be considered infrequent.
    
*   If `float`, categories with a smaller cardinality than `min_frequency * n_samples` will be considered infrequent.
    

Added in version 1.1: Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)
.

**max\_categories**int, default=None

Specifies an upper limit to the number of output features for each input feature when considering infrequent categories. If there are infrequent categories, `max_categories` includes the category representing the infrequent categories along with the frequent categories. If `None`, there is no limit to the number of output features.

Added in version 1.1: Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)
.

**feature\_name\_combiner**“concat” or callable, default=”concat”

Callable with signature `def callable(input_feature, category)` that returns a string. This is used to create feature names to be returned by [`get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.get_feature_names_out "sklearn.preprocessing.OneHotEncoder.get_feature_names_out")
.

`"concat"` concatenates encoded feature name and category with `feature + "_" + str(category)`.E.g. feature X with values 1, 6, 7 create feature names `X_1, X_6, X_7`.

Added in version 1.3.

Attributes:

**categories\_**list of arrays

The categories of each feature determined during fitting (in order of the features in X and corresponding with the output of `transform`). This includes the category specified in `drop` (if any).

**drop\_idx\_**array of shape (n\_features,)

*   `drop_idx_[i]` is the index in `categories_[i]` of the category to be dropped for each feature.
    
*   `drop_idx_[i] = None` if no category is to be dropped from the feature with index `i`, e.g. when `drop='if_binary'` and the feature isn’t binary.
    
*   `drop_idx_ = None` if all the transformed features will be retained.
    

If infrequent categories are enabled by setting `min_frequency` or `max_categories` to a non-default value and `drop_idx[i]` corresponds to an infrequent category, then the entire infrequent category is dropped.

Changed in version 0.23: Added the possibility to contain `None` values.

`infrequent_categories_`list of ndarray

Infrequent categories for each feature.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 1.0.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**feature\_name\_combiner**callable or None

Callable with signature `def callable(input_feature, category)` that returns a string. This is used to create feature names to be returned by [`get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.get_feature_names_out "sklearn.preprocessing.OneHotEncoder.get_feature_names_out")
.

Added in version 1.3.

See also

[`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

Performs an ordinal (integer) encoding of the categorical features.

[`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")

Encodes categorical features using the target.

[`sklearn.feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")

Performs a one-hot encoding of dictionary items (also handles string-valued features).

[`sklearn.feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")

Performs an approximate one-hot encoding of dictionary items or strings.

[`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")

Binarizes labels in a one-vs-all fashion.

[`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")

Transforms between iterable of iterables and a multilabel format, e.g. a (samples x classes) binary matrix indicating the presence of a class label.

Examples

Given a dataset with two features, we let the encoder find the unique values per feature and transform the data to a binary one-hot encoding.

\>>> from sklearn.preprocessing import OneHotEncoder

Copy to clipboard

One can discard categories not seen during `fit`:

\>>> enc \= OneHotEncoder(handle\_unknown\='ignore')
\>>> X \= \[\['Male', 1\], \['Female', 3\], \['Female', 2\]\]
\>>> enc.fit(X)
OneHotEncoder(handle\_unknown='ignore')
\>>> enc.categories\_
\[array(\['Female', 'Male'\], dtype=object), array(\[1, 2, 3\], dtype=object)\]
\>>> enc.transform(\[\['Female', 1\], \['Male', 4\]\]).toarray()
array(\[\[1., 0., 1., 0., 0.\],\
       \[0., 1., 0., 0., 0.\]\])
\>>> enc.inverse\_transform(\[\[0, 1, 1, 0, 0\], \[0, 0, 0, 1, 0\]\])
array(\[\['Male', 1\],\
       \[None, 2\]\], dtype=object)
\>>> enc.get\_feature\_names\_out(\['gender', 'group'\])
array(\['gender\_Female', 'gender\_Male', 'group\_1', 'group\_2', 'group\_3'\], ...)

Copy to clipboard

One can always drop the first column for each feature:

\>>> drop\_enc \= OneHotEncoder(drop\='first').fit(X)
\>>> drop\_enc.categories\_
\[array(\['Female', 'Male'\], dtype=object), array(\[1, 2, 3\], dtype=object)\]
\>>> drop\_enc.transform(\[\['Female', 1\], \['Male', 2\]\]).toarray()
array(\[\[0., 0., 0.\],\
       \[1., 1., 0.\]\])

Copy to clipboard

Or drop a column for feature only having 2 categories:

\>>> drop\_binary\_enc \= OneHotEncoder(drop\='if\_binary').fit(X)
\>>> drop\_binary\_enc.transform(\[\['Female', 1\], \['Male', 2\]\]).toarray()
array(\[\[0., 1., 0., 0.\],\
       \[1., 0., 1., 0.\]\])

Copy to clipboard

One can change the way feature names are created.

\>>> def custom\_combiner(feature, category):
...     return str(feature) + "\_" + type(category).\_\_name\_\_ + "\_" + str(category)
\>>> custom\_fnames\_enc \= OneHotEncoder(feature\_name\_combiner\=custom\_combiner).fit(X)
\>>> custom\_fnames\_enc.get\_feature\_names\_out()
array(\['x0\_str\_Female', 'x0\_str\_Male', 'x1\_int\_1', 'x1\_int\_2', 'x1\_int\_3'\],
      dtype=object)

Copy to clipboard

Infrequent categories are enabled by setting `max_categories` or `min_frequency`.

\>>> import numpy as np
\>>> X \= np.array(\[\["a"\] \* 5 + \["b"\] \* 20 + \["c"\] \* 10 + \["d"\] \* 3\], dtype\=object).T
\>>> ohe \= OneHotEncoder(max\_categories\=3, sparse\_output\=False).fit(X)
\>>> ohe.infrequent\_categories\_
\[array(\['a', 'd'\], dtype=object)\]
\>>> ohe.transform(\[\["a"\], \["b"\]\])
array(\[\[0., 0., 1.\],\
       \[1., 0., 0.\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L981)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.fit "Link to this definition")

Fit OneHotEncoder to X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to determine the categories of each feature.

**y**None

Ignored. This parameter exists only for compatibility with [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
.

Returns:

self

Fitted encoder.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1215)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.get_feature_names_out "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1096)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.inverse_transform "Link to this definition")

Convert the data back to the original representation.

When unknown categories are encountered (all zeros in the one-hot encoding), `None` is used to represent this category. If the feature with the unknown category has a dropped category, the dropped category will be its inverse.

For a given input feature, if there is an infrequent category, ‘infrequent\_sklearn’ will be used to represent the infrequent category.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_encoded\_features)

The transformed data.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Inverse transformed array.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_encoders.py#L1009)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.transform "Link to this definition")

Transform X using one-hot encoding.

If `sparse_output=True` (default), it returns a SciPy sparse in CSR format.

If there are infrequent categories for a feature, set by specifying `max_categories` or `min_frequency`, the infrequent categories are grouped into a single category.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to encode.

Returns:

**X\_out**{ndarray, sparse matrix} of shape (n\_samples, n\_encoded\_features)

Transformed input. If `sparse_output=True`, a sparse matrix will be returned.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)

[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)

Partial Dependence and Individual Conditional Expectation Plots

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_estimator_representation_thumb.png)

[Displaying estimators and complex pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_estimator_representation.html)

Displaying estimators and complex pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)

[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)

Displaying Pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)

[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)

Comparing Target Encoder with Other Encoders

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_0_0_thumb.png)

[Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html)

Release Highlights for scikit-learn 1.0

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)