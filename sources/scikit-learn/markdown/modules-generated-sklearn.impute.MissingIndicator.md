[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.impute.MissingIndicator.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.impute.MissingIndicator.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.impute.MissingIndicator.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.impute.MissingIndicator.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.impute.MissingIndicator.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.impute.MissingIndicator.html)

Collapse Sidebar Expand Sidebar

MissingIndicator[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#missingindicator "Link to this heading")

====================================================================================================================================================

class sklearn.impute.MissingIndicator(_\*_, _missing\_values\=nan_, _features\='missing-only'_, _sparse\='auto'_, _error\_on\_new\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L787)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "Link to this definition")

Binary indicators for missing values.

Note that this component typically should not be used in a vanilla [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 consisting of transformers and a classifier, but rather could be added using a [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 or [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/impute.html#impute)
.

Added in version 0.20.

Parameters:

**missing\_values**int, float, str, np.nan or None, default=np.nan

The placeholder for the missing values. All occurrences of `missing_values` will be imputed. For pandas’ dataframes with nullable integer dtypes with missing values, `missing_values` should be set to `np.nan`, since `pd.NA` will be converted to `np.nan`.

**features**{‘missing-only’, ‘all’}, default=’missing-only’

Whether the imputer mask should represent all or a subset of features.

*   If `'missing-only'` (default), the imputer mask will only represent features containing missing values during fit time.
    
*   If `'all'`, the imputer mask will represent all features.
    

**sparse**bool or ‘auto’, default=’auto’

Whether the imputer mask format should be sparse or dense.

*   If `'auto'` (default), the imputer mask will be of same type as input.
    
*   If `True`, the imputer mask will be a sparse matrix.
    
*   If `False`, the imputer mask will be a numpy array.
    

**error\_on\_new**bool, default=True

If `True`, [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.transform "sklearn.impute.MissingIndicator.transform")
 will raise an error when there are features with missing values that have no missing values in [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.fit "sklearn.impute.MissingIndicator.fit")
. This is applicable only when `features='missing-only'`.

Attributes:

**features\_**ndarray of shape (n\_missing\_features,) or (n\_features,)

The features indices which will be returned when calling [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.transform "sklearn.impute.MissingIndicator.transform")
. They are computed during [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.fit "sklearn.impute.MissingIndicator.fit")
. If `features='all'`, `features_` is equal to `range(n_features)`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")

Univariate imputation of missing values.

[`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")

Multivariate imputation of missing values.

Examples

\>>> import numpy as np
\>>> from sklearn.impute import MissingIndicator
\>>> X1 \= np.array(\[\[np.nan, 1, 3\],\
...                \[4, 0, np.nan\],\
...                \[8, 1, 0\]\])
\>>> X2 \= np.array(\[\[5, 1, np.nan\],\
...                \[np.nan, 2, 3\],\
...                \[2, 4, 0\]\])
\>>> indicator \= MissingIndicator()
\>>> indicator.fit(X1)
MissingIndicator()
\>>> X2\_tr \= indicator.transform(X2)
\>>> X2\_tr
array(\[\[False,  True\],\
       \[ True, False\],\
       \[False, False\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L1023)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.fit "Link to this definition")

Fit the transformer on `X`.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L1086)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.fit_transform "Link to this definition")

Generate missing values indicator for `X`.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data to complete.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**Xt**{ndarray, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_features\_with\_missing)

The missing indicator for input data. The data type of `Xt` will be boolean.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L1112)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.get_feature_names_out "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_base.py#L1045)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.transform "Link to this definition")

Generate missing values indicator for `X`.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data to complete.

Returns:

**Xt**{ndarray, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_features\_with\_missing)

The missing indicator for input data. The data type of `Xt` will be boolean.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)