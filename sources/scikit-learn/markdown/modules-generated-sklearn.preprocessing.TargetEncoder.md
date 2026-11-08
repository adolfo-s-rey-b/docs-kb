[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.TargetEncoder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.TargetEncoder.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.TargetEncoder.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.TargetEncoder.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.TargetEncoder.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.TargetEncoder.html)

Collapse Sidebar Expand Sidebar

TargetEncoder[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#targetencoder "Link to this heading")

==================================================================================================================================================

class sklearn.preprocessing.TargetEncoder(_categories\='auto'_, _target\_type\='auto'_, _smooth\='auto'_, _cv\=5_, _shuffle\='deprecated'_, _random\_state\='deprecated'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_target_encoder.py#L34)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "Link to this definition")

Target Encoder for regression and classification targets.

Each category is encoded based on a shrunk estimate of the average target values for observations belonging to the category. The encoding scheme mixes the global target mean with the target mean conditioned on the value of the category (see [\[MIC\]](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#rf862141e5a0c-mic)
).

When the target type is “multiclass”, encodings are based on the conditional probability estimate for each class. The target is first binarized using the “one-vs-all” scheme via [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
, then the average target value for each class and each category is used for encoding, resulting in `n_features` \* `n_classes` encoded output features.

[`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
 considers missing values, such as `np.nan` or `None`, as another category and encodes them like any other category. Categories that are not seen during [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit "sklearn.preprocessing.TargetEncoder.fit")
 are encoded with the target mean, i.e. `target_mean_`.

For a demo on the importance of the `TargetEncoder` internal [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
, see [Target Encoder’s Internal Cross fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html#sphx-glr-auto-examples-preprocessing-plot-target-encoder-cross-val-py)
. For a comparison of different encoders, refer to [Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#sphx-glr-auto-examples-preprocessing-plot-target-encoder-py)
. Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
.

Note

`fit(X, y).transform(X)` does not equal `fit_transform(X, y)` because a [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
 scheme is used in `fit_transform` for encoding. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
 for details.

Added in version 1.3.

Parameters:

**categories**“auto” or list of shape (n\_features,) of array-like, default=”auto”

Categories (unique values) per feature:

*   `"auto"` : Determine categories automatically from the training data.
    
*   list : `categories[i]` holds the categories expected in the i-th column. The passed categories should not mix strings and numeric values within a single feature, and should be sorted in case of numeric values.
    

The used categories are stored in the `categories_` fitted attribute.

**target\_type**{“auto”, “continuous”, “binary”, “multiclass”}, default=”auto”

Type of target.

*   `"auto"` : Type of target is inferred with [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
    .
    
*   `"continuous"` : Continuous target
    
*   `"binary"` : Binary target
    
*   `"multiclass"` : Multiclass target
    

Note

The type of target inferred with `"auto"` may not be the desired target type used for modeling. For example, if the target consisted of integers between 0 and 100, then [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 will infer the target as `"multiclass"`. In this case, setting `target_type="continuous"` will specify the target as a regression problem. The `target_type_` attribute gives the target type used by the encoder.

Changed in version 1.4: Added the option ‘multiclass’.

**smooth**“auto” or float, default=”auto”

The amount of mixing of the target mean conditioned on the value of the category with the global target mean. A larger `smooth` value will put more weight on the global target mean. If `"auto"`, then `smooth` is set to an empirical Bayes estimate.

**cv**int, cross-validation generator or an iterable, default=5

Determines the splitting strategy used in the internal [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
 during [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit_transform "sklearn.preprocessing.TargetEncoder.fit_transform")
. Splitters where each sample index doesn’t appear in the validation fold exactly once, raise a `ValueError`. Possible inputs for cv are:

*   `None`, to use a 5-fold cross-validation chosen internally based on
    
    `target_type`,
    
*   integer, to specify the number of folds for the cross-validation chosen
    
    internally based on `target_type`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
     that does not repeat samples across validation folds,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, if `target_type` is `"continuous"`, `KFold` is used, otherwise `StratifiedKFold` is used.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for more information on cross-validation strategies.

Changed in version 1.9: Cross-validation generators and iterables can also be passed as `cv`.

**shuffle**bool, default=True

Whether to shuffle the data in [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit_transform "sklearn.preprocessing.TargetEncoder.fit_transform")
 before splitting into folds. Note that the samples within each split will not be shuffled. Only applies if `cv` is an int or `None`. If `cv` is a cross-validation generator or an iterable, `shuffle` is ignored.

Deprecated since version 1.9: `shuffle` is deprecated and will be removed in 1.11. Pass a cross-validation generator as `cv` argument to specify the shuffling instead.

**random\_state**int, RandomState instance or None, default=None

When `shuffle` is True, `random_state` affects the ordering of the indices, which controls the randomness of each fold. Otherwise, this parameter has no effect. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Deprecated since version 1.9: `random_state` is deprecated and will be removed in 1.11. Pass a cross-validation generator as `cv` argument to specify the random state of the shuffling instead.

Attributes:

**encodings\_**list of shape (n\_features,) or (n\_features \* n\_classes) of ndarray

Encodings learnt on all of `X`. For feature `i`, `encodings_[i]` are the encodings matching the categories listed in `categories_[i]`. When `target_type_` is “multiclass”, the encoding for feature `i` and class `j` is stored in `encodings_[j + (i * len(classes_))]`. E.g., for 2 features (f) and 3 classes (c), encodings are ordered: f0\_c0, f0\_c1, f0\_c2, f1\_c0, f1\_c1, f1\_c2,

**categories\_**list of shape (n\_features,) of ndarray

The categories of each input feature determined during fitting or specified in `categories` (in order of the features in `X` and corresponding with the output of [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.transform "sklearn.preprocessing.TargetEncoder.transform")
).

**target\_type\_**str

Type of target.

**target\_mean\_**float

The overall mean of the target. This value is only used in [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.transform "sklearn.preprocessing.TargetEncoder.transform")
 to encode categories.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

**classes\_**ndarray or None

If `target_type_` is ‘binary’ or ‘multiclass’, holds the label for each class, otherwise `None`.

See also

[`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

Performs an ordinal (integer) encoding of the categorical features. Contrary to TargetEncoder, this encoding is not supervised. Treating the resulting encoding as a numerical features therefore lead arbitrarily ordered values and therefore typically lead to lower predictive performance when used as preprocessing for a classifier or regressor.

[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

Performs a one-hot encoding of categorical features. This unsupervised encoding is better suited for low cardinality categorical variables as it generate one new feature per unique category.

References

\[[MIC](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#id1)\
\]

[Micci-Barreca, Daniele. “A preprocessing scheme for high-cardinality categorical attributes in classification and prediction problems” SIGKDD Explor. Newsl. 3, 1 (July 2001), 27–32.](https://doi.org/10.1145/507533.507538)

Examples

With `smooth="auto"`, the smoothing parameter is set to an empirical Bayes estimate:

\>>> import numpy as np
\>>> from sklearn.preprocessing import TargetEncoder
\>>> X \= np.array(\[\["dog"\] \* 20 + \["cat"\] \* 30 + \["snake"\] \* 38\], dtype\=object).T
\>>> y \= \[90.3\] \* 5 + \[80.1\] \* 15 + \[20.4\] \* 5 + \[20.1\] \* 25 + \[21.2\] \* 8 + \[49\] \* 30
\>>> enc\_auto \= TargetEncoder(smooth\="auto")
\>>> X\_trans \= enc\_auto.fit\_transform(X, y)

Copy to clipboard

\>>> \# A high \`smooth\` parameter puts more weight on global mean on the categorical
\>>> \# encodings:
\>>> enc\_high\_smooth \= TargetEncoder(smooth\=5000.0).fit(X, y)
\>>> enc\_high\_smooth.target\_mean\_
np.float64(44.3)
\>>> enc\_high\_smooth.encodings\_
\[array(\[44.1, 44.4, 44.3\])\]

Copy to clipboard

\>>> \# On the other hand, a low \`smooth\` parameter puts more weight on target
\>>> \# conditioned on the value of the categorical:
\>>> enc\_low\_smooth \= TargetEncoder(smooth\=1.0).fit(X, y)
\>>> enc\_low\_smooth.encodings\_
\[array(\[21, 80.8, 43.2\])\]

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_target_encoder.py#L256)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit "Link to this definition")

Fit the [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
 to X and y.

It is discouraged to use this method because it can introduce data leakage. Use `fit_transform` on training data instead.

Note

`fit(X, y).transform(X)` does not equal `fit_transform(X, y)` because a [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
 scheme is used in `fit_transform` for encoding. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
 for details.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to determine the categories of each feature.

**y**array-like of shape (n\_samples,)

The target data used to encode the categories.

Returns:

**self**object

Fitted encoder.

fit\_transform(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_target_encoder.py#L284)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit_transform "Link to this definition")

Fit [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
 and transform `X` with the target encoding.

This method uses a [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
 scheme to prevent target leakage and overfitting in downstream predictors. It is the recommended method for encoding training data.

Note

`fit(X, y).transform(X)` does not equal `fit_transform(X, y)` because a [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
 scheme is used in `fit_transform` for encoding. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
 for details.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to determine the categories of each feature.

**y**array-like of shape (n\_samples,)

The target data used to encode the categories.

**\*\*params**dict

Parameters to route to the internal CV object.

Can only be used in conjunction with a cross-validation generator as CV object.

For instance, `groups` (array-like of shape `(n_samples,)`) can be routed to a CV splitter that accepts `groups`, such as `GroupKFold` or `StratifiedGroupKFold`.

Added in version 1.9: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**X\_trans**ndarray of shape (n\_samples, n\_features) or (n\_samples, (n\_features \* n\_classes))

Transformed input.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_target_encoder.py#L619)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Not used, present here for API consistency by convention.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names. `feature_names_in_` is used unless it is not defined, in which case the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`. When `type_of_target_` is “multiclass” the names are of the format ‘<feature\_name>\_<class\_name>’.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_target_encoder.py#L648)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.9.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_target_encoder.py#L425)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.transform "Link to this definition")

Transform X with the target encoding.

This method internally uses the `encodings_` attribute learnt during [`TargetEncoder.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit_transform "sklearn.preprocessing.TargetEncoder.fit_transform")
 to transform test data.

Note

`fit(X, y).transform(X)` does not equal `fit_transform(X, y)` because a [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
 scheme is used in `fit_transform` for encoding. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
 for details.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to determine the categories of each feature.

Returns:

**X\_trans**ndarray of shape (n\_samples, n\_features) or (n\_samples, (n\_features \* n\_classes))

Transformed input.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)

[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)

Comparing Target Encoder with Other Encoders

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_cross_val_thumb.png)

[Target Encoder’s Internal Cross fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html)

Target Encoder's Internal Cross fitting

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