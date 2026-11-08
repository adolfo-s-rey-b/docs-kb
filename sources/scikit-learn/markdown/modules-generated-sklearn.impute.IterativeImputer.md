[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.impute.IterativeImputer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.impute.IterativeImputer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.impute.IterativeImputer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.impute.IterativeImputer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.impute.IterativeImputer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.impute.IterativeImputer.html)

Collapse Sidebar Expand Sidebar

IterativeImputer[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#iterativeimputer "Link to this heading")

====================================================================================================================================================

class sklearn.impute.IterativeImputer(_estimator\=None_, _\*_, _missing\_values\=nan_, _sample\_posterior\=False_, _max\_iter\=10_, _tol\=0.001_, _n\_nearest\_features\=None_, _initial\_strategy\='mean'_, _fill\_value\=None_, _imputation\_order\='ascending'_, _skip\_complete\=False_, _min\_value\=\-inf_, _max\_value\=inf_, _verbose\=0_, _random\_state\=None_, _add\_indicator\=False_, _keep\_empty\_features\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_iterative.py#L60)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "Link to this definition")

Multivariate imputer that estimates each feature from all the others.

A strategy for imputing missing values by modeling each feature with missing values as a function of other features in a round-robin fashion.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/impute.html#iterative-imputer)
.

Added in version 0.21.

Note

This estimator is still **experimental** for now: the predictions and the API might change without any deprecation cycle. To use it, you need to explicitly import `enable_iterative_imputer`:

\>>> \# explicitly require this experimental feature
\>>> from sklearn.experimental import enable\_iterative\_imputer  \# noqa
\>>> \# now you can import normally from sklearn.impute
\>>> from sklearn.impute import IterativeImputer

Copy to clipboard

Parameters:

**estimator**estimator object, default=BayesianRidge()

The estimator to use at each step of the round-robin imputation. If `sample_posterior=True`, the estimator must support `return_std` in its `predict` method.

**missing\_values**int or np.nan, default=np.nan

The placeholder for the missing values. All occurrences of `missing_values` will be imputed. For pandas’ dataframes with nullable integer dtypes with missing values, `missing_values` should be set to `np.nan`, since `pd.NA` will be converted to `np.nan`.

**sample\_posterior**bool, default=False

Whether to sample from the (Gaussian) predictive posterior of the fitted estimator for each imputation. Estimator must support `return_std` in its `predict` method if set to `True`. Set to `True` if using `IterativeImputer` for multiple imputations.

**max\_iter**int, default=10

Maximum number of imputation rounds to perform before returning the imputations computed during the final round. A round is a single imputation of each feature with missing values. The stopping criterion is met once `max(abs(X_t - X_{t-1}))/max(abs(X[known_vals])) < tol`, where `X_t` is `X` at iteration `t`. Note that early stopping is only applied if `sample_posterior=False`.

**tol**float, default=1e-3

Tolerance of the stopping condition.

**n\_nearest\_features**int, default=None

Number of other features to use to estimate the missing values of each feature column. Nearness between features is measured using the absolute correlation coefficient between each feature pair (after initial imputation). To ensure coverage of features throughout the imputation process, the neighbor features are not necessarily nearest, but are drawn with probability proportional to correlation for each imputed target feature. Can provide significant speed-up when the number of features is huge. If `None`, all features will be used.

**initial\_strategy**{‘mean’, ‘median’, ‘most\_frequent’, ‘constant’}, default=’mean’

Which strategy to use to initialize the missing values. Same as the `strategy` parameter in [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
.

**fill\_value**str or numerical value, default=None

When `strategy="constant"`, `fill_value` is used to replace all occurrences of missing\_values. For string or object data types, `fill_value` must be a string. If `None`, `fill_value` will be 0 when imputing numerical data and “missing\_value” for strings or object data types.

Added in version 1.3.

**imputation\_order**{‘ascending’, ‘descending’, ‘roman’, ‘arabic’, ‘random’}, default=’ascending’

The order in which the features will be imputed. Possible values:

*   `'ascending'`: From features with fewest missing values to most.
    
*   `'descending'`: From features with most missing values to fewest.
    
*   `'roman'`: Left to right.
    
*   `'arabic'`: Right to left.
    
*   `'random'`: A random order for each round.
    

**skip\_complete**bool, default=False

If `True` then features with missing values during [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.transform "sklearn.impute.IterativeImputer.transform")
 which did not have any missing values during [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.fit "sklearn.impute.IterativeImputer.fit")
 will be imputed with the initial imputation method only. Set to `True` if you have many features with no missing values at both [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.fit "sklearn.impute.IterativeImputer.fit")
 and [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.transform "sklearn.impute.IterativeImputer.transform")
 time to save compute.

**min\_value**float or array-like of shape (n\_features,), default=-np.inf

Minimum possible imputed value. Broadcast to shape `(n_features,)` if scalar. If array-like, expects shape `(n_features,)`, one min value for each feature. The default is `-np.inf`.

Changed in version 0.23: Added support for array-like.

**max\_value**float or array-like of shape (n\_features,), default=np.inf

Maximum possible imputed value. Broadcast to shape `(n_features,)` if scalar. If array-like, expects shape `(n_features,)`, one max value for each feature. The default is `np.inf`.

Changed in version 0.23: Added support for array-like.

**verbose**int, default=0

Verbosity flag, controls the debug messages that are issued as functions are evaluated. The higher, the more verbose. Can be 0, 1, or 2.

**random\_state**int, RandomState instance or None, default=None

The seed of the pseudo random number generator to use. Randomizes selection of estimator features if `n_nearest_features` is not `None`, the `imputation_order` if `random`, and the sampling from posterior if `sample_posterior=True`. Use an integer for determinism. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**add\_indicator**bool, default=False

If `True`, a [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
 transform will stack onto output of the imputer’s transform. This allows a predictive estimator to account for missingness despite imputation. If a feature has no missing values at fit/train time, the feature won’t appear on the missing indicator even if there are missing values at transform/test time.

**keep\_empty\_features**bool, default=False

If True, features that consist exclusively of missing values when `fit` is called are returned in results when `transform` is called. The imputed value is always `0` except when `initial_strategy="constant"` in which case `fill_value` will be used instead.

Added in version 1.2.

Attributes:

**initial\_imputer\_**object of type [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")

Imputer used to initialize the missing values.

**imputation\_sequence\_**list of tuples

Each tuple has `(feat_idx, neighbor_feat_idx, estimator)`, where `feat_idx` is the current feature to be imputed, `neighbor_feat_idx` is the array of other features used to impute the current feature, and `estimator` is the trained estimator used for the imputation. Length is `self.n_features_with_missing_ * self.n_iter_`.

**n\_iter\_**int

Number of iteration rounds that occurred. Will be less than `self.max_iter` if early stopping criterion was reached.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_features\_with\_missing\_**int

Number of features with missing values.

**indicator\_**[`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")

Indicator used to add binary indicators for missing values. `None` if `add_indicator=False`.

**random\_state\_**RandomState instance

RandomState instance that is generated either from a seed, the random number generator or by `np.random`.

See also

[`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")

Univariate imputer for completing missing values with simple strategies.

[`KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")

Multivariate imputer that estimates missing features using nearest samples.

Notes

To support imputation in inductive mode we store each feature’s estimator during the [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.fit "sklearn.impute.IterativeImputer.fit")
 phase, and predict without refitting (in order) during the [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.transform "sklearn.impute.IterativeImputer.transform")
 phase.

Features which contain all missing values at [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.fit "sklearn.impute.IterativeImputer.fit")
 are discarded upon [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.transform "sklearn.impute.IterativeImputer.transform")
.

Using defaults, the imputer scales in O(knp3min(n,p)) where k = `max_iter`, n the number of samples and p the number of features. It thus becomes prohibitively costly when the number of features increases. Setting `n_nearest_features << n_features`, `skip_complete=True` or increasing `tol` can help to reduce its computational cost.

Depending on the nature of missing values, simple imputers can be preferable in a prediction context.

References

\[1\]

[Stef van Buuren, Karin Groothuis-Oudshoorn (2011). “mice: Multivariate Imputation by Chained Equations in R”. Journal of Statistical Software 45: 1-67.](https://www.jstatsoft.org/article/view/v045i03)

\[2\]

[S. F. Buck, (1960). “A Method of Estimation of Missing Values in Multivariate Data Suitable for use with an Electronic Computer”. Journal of the Royal Statistical Society 22(2): 302-306.](https://www.jstor.org/stable/2984099)

Examples

\>>> import numpy as np
\>>> from sklearn.experimental import enable\_iterative\_imputer
\>>> from sklearn.impute import IterativeImputer
\>>> imp\_mean \= IterativeImputer(random\_state\=0)
\>>> imp\_mean.fit(\[\[7, 2, 3\], \[4, np.nan, 6\], \[10, 5, 9\]\])
IterativeImputer(random\_state=0)
\>>> X \= \[\[np.nan, 2, 3\], \[4, np.nan, 6\], \[10, np.nan, 9\]\]
\>>> imp\_mean.transform(X)
array(\[\[ 6.9584,  2.       ,  3.        \],\
       \[ 4.       ,  2.6000,  6.        \],\
       \[10.       ,  4.9999,  9.        \]\])

Copy to clipboard

For a more detailed example see [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)
 or [Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html#sphx-glr-auto-examples-impute-plot-iterative-imputer-variants-comparison-py)
.

fit(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_iterative.py#L929)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.fit "Link to this definition")

Fit the imputer on `X` and return self.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

Input data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*fit\_params**dict

Parameters routed to the `fit` method of the sub-estimator via the metadata routing API.

Added in version 1.5: Only available if `sklearn.set_config(enable_metadata_routing=True)` is set. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_iterative.py#L719)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.fit_transform "Link to this definition")

Fit the imputer on `X` and return the transformed `X`.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

Input data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*params**dict

Parameters routed to the `fit` method of the sub-estimator via the metadata routing API.

Added in version 1.5: Only available if `sklearn.set_config(enable_metadata_routing=True)` is set. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**Xt**array-like, shape (n\_samples, n\_features)

The imputed input data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_iterative.py#L959)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_iterative.py#L984)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/impute/_iterative.py#L875)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer.transform "Link to this definition")

Impute all missing values in `X`.

Note that this is stochastic, and that if `random_state` is not fixed, repeated calls, or permuted input, results will differ.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input data to complete.

Returns:

**Xt**array-like, shape (n\_samples, n\_features)

The imputed input data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)