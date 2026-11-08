[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.impute.KNNImputer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.impute.KNNImputer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.impute.KNNImputer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.impute.KNNImputer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.impute.KNNImputer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.impute.KNNImputer.html)

Collapse Sidebar Expand Sidebar

KNNImputer[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#knnimputer "Link to this heading")

==================================================================================================================================

class sklearn.impute.KNNImputer(_\*_, _missing\_values\=nan_, _n\_neighbors\=5_, _weights\='uniform'_, _metric\='nan\_euclidean'_, _copy\=True_, _add\_indicator\=False_, _keep\_empty\_features\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_knn.py#L24)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "Link to this definition")

Imputation for completing missing values using k-Nearest Neighbors.

Each sample’s missing values are imputed using the mean value from `n_neighbors` nearest neighbors found in the training set. Two samples are close if the features that neither is missing are close.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/impute.html#knnimpute)
.

Added in version 0.22.

Parameters:

**missing\_values**int, float, str, np.nan or None, default=np.nan

The placeholder for the missing values. All occurrences of `missing_values` will be imputed. For pandas’ dataframes with nullable integer dtypes with missing values, `missing_values` should be set to np.nan, since `pd.NA` will be converted to np.nan.

**n\_neighbors**int, default=5

Number of neighboring samples to use for imputation.

**weights**{‘uniform’, ‘distance’} or callable, default=’uniform’

Weight function used in prediction. Possible values:

*   ‘uniform’ : uniform weights. All points in each neighborhood are weighted equally.
    
*   ‘distance’ : weight points by the inverse of their distance. in this case, closer neighbors of a query point will have a greater influence than neighbors which are further away.
    
*   callable : a user-defined function which accepts an array of distances, and returns an array of the same shape containing the weights.
    

**metric**{‘nan\_euclidean’} or callable, default=’nan\_euclidean’

Distance metric for searching neighbors. Possible values:

*   ‘nan\_euclidean’
    
*   callable : a user-defined function which conforms to the definition of `func_metric(x, y, *, missing_values=np.nan)`. `x` and `y` corresponds to a row (i.e. 1-D arrays) of `X` and `Y`, respectively. The callable should returns a scalar distance value.
    

**copy**bool, default=True

If True, a copy of X will be created. If False, imputation will be done in-place whenever possible.

**add\_indicator**bool, default=False

If True, a [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
 transform will stack onto the output of the imputer’s transform. This allows a predictive estimator to account for missingness despite imputation. If a feature has no missing values at fit/train time, the feature won’t appear on the missing indicator even if there are missing values at transform/test time.

**keep\_empty\_features**bool, default=False

If True, features that consist exclusively of missing values when `fit` is called are returned in results when `transform` is called. The imputed value is always `0`.

Added in version 1.2.

Attributes:

**indicator\_**[`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")

Indicator used to add binary indicators for missing values. `None` if add\_indicator is False.

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

Univariate imputer for completing missing values with simple strategies.

[`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")

Multivariate imputer that estimates values to impute for each feature with missing values from all the others.

References

*   [Olga Troyanskaya, Michael Cantor, Gavin Sherlock, Pat Brown, Trevor Hastie, Robert Tibshirani, David Botstein and Russ B. Altman, Missing value estimation methods for DNA microarrays, BIOINFORMATICS Vol. 17 no. 6, 2001 Pages 520-525.](https://academic.oup.com/bioinformatics/article/17/6/520/272365)
    

Examples

\>>> import numpy as np
\>>> from sklearn.impute import KNNImputer
\>>> X \= \[\[1, 2, np.nan\], \[3, 4, 3\], \[np.nan, 6, 5\], \[8, 8, 7\]\]
\>>> imputer \= KNNImputer(n\_neighbors\=2)
\>>> imputer.fit\_transform(X)
array(\[\[1. , 2. , 4. \],\
       \[3. , 4. , 3. \],\
       \[5.5, 6. , 5. \],\
       \[8. , 8. , 7. \]\])

Copy to clipboard

For a more detailed example see [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)
.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_knn.py#L213)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.fit "Link to this definition")

Fit the imputer on X.

Parameters:

**X**array-like shape of (n\_samples, n\_features)

Input data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

The fitted `KNNImputer` class instance.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_knn.py#L388)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.get_feature_names_out "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_knn.py#L254)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer.transform "Link to this definition")

Impute all missing values in X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input data to complete.

Returns:

**X**array-like of shape (n\_samples, n\_output\_features)

The imputed dataset. `n_output_features` is the number of features that is not always missing during `fit`.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)