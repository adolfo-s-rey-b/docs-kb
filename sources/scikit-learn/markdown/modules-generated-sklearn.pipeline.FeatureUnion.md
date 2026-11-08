[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.pipeline.FeatureUnion.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.FeatureUnion.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.pipeline.FeatureUnion.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.pipeline.FeatureUnion.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.pipeline.FeatureUnion.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.pipeline.FeatureUnion.html)

Collapse Sidebar Expand Sidebar

FeatureUnion[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#featureunion "Link to this heading")

==========================================================================================================================================

class sklearn.pipeline.FeatureUnion(_transformer\_list_, _\*_, _n\_jobs\=None_, _transformer\_weights\=None_, _verbose\=False_, _verbose\_feature\_names\_out\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1610)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "Link to this definition")

Concatenates results of multiple transformer objects.

This estimator applies a list of transformer objects in parallel to the input data, then concatenates the results. This is useful to combine several feature extraction mechanisms into a single transformer.

Parameters of the transformers may be set using its name and the parameter name separated by a ‘\_\_’. A transformer may be replaced entirely by setting the parameter with its name to another transformer, removed by setting to ‘drop’ or disabled by setting to ‘passthrough’ (features are passed without transformation).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/compose.html#feature-union)
.

Added in version 0.13.

Parameters:

**transformer\_list**list of (str, transformer) tuples

List of transformer objects to be applied to the data. The first half of each tuple is the name of the transformer. The transformer can be ‘drop’ for it to be ignored or can be ‘passthrough’ for features to be passed unchanged.

Added in version 1.1: Added the option `"passthrough"`.

Changed in version 0.22: Deprecated `None` as a transformer in favor of ‘drop’.

**n\_jobs**int, default=None

Number of jobs to run in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Changed in version v0.20: `n_jobs` default changed from 1 to None

**transformer\_weights**dict, default=None

Multiplicative weights for features per transformer. Keys are transformer names, values the weights. Raises ValueError if key not present in `transformer_list`.

**verbose**bool, default=False

If True, the time elapsed while fitting each transformer will be printed as it is completed.

**verbose\_feature\_names\_out**bool, default=True

If True, [`get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.get_feature_names_out "sklearn.pipeline.FeatureUnion.get_feature_names_out")
 will prefix all feature names with the name of the transformer that generated that feature. If False, [`get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.get_feature_names_out "sklearn.pipeline.FeatureUnion.get_feature_names_out")
 will not prefix any feature names and will error if feature names are not unique.

Added in version 1.5.

Attributes:

**named\_transformers**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes. Read-only attribute to access any transformer parameter by user given name. Keys are transformer names and values are transformer parameters.

Added in version 1.2.

`n_features_in_`int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

`feature_names_in_`ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

See also

[`make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union")

Convenience function for simplified feature union construction.

Examples

\>>> from sklearn.pipeline import FeatureUnion
\>>> from sklearn.decomposition import PCA, TruncatedSVD
\>>> union \= FeatureUnion(\[("pca", PCA(n\_components\=1)),\
...                       ("svd", TruncatedSVD(n\_components\=2))\])
\>>> X \= \[\[0., 1., 3\], \[2., 2., 5\]\]
\>>> union.fit\_transform(X)
array(\[\[-1.5       ,  3.04, -0.872\],\
       \[ 1.5       ,  5.72,  0.463\]\])
\>>> \# An estimator's parameter can be set using '\_\_' syntax
\>>> union.set\_params(svd\_\_n\_components\=1).fit\_transform(X)
array(\[\[-1.5       ,  3.04\],\
       \[ 1.5       ,  5.72\]\])

Copy to clipboard

For a more detailed example of usage, see [Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html#sphx-glr-auto-examples-compose-plot-feature-union-py)
.

fit(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1928)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.fit "Link to this definition")

Fit all transformers using X.

Parameters:

**X**iterable or array-like, depending on transformers

Input data, used to fit transformers.

**y**array-like of shape (n\_samples, n\_outputs), default=None

Targets for supervised learning.

**\*\*fit\_params**dict, default=None

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` methods of the sub-transformers.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` methods of the sub-transformers. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
     for more details.
    

Changed in version 1.5: `**fit_params` can be routed via metadata routing API.

Returns:

**self**object

FeatureUnion class instance.

fit\_transform(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1974)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.fit_transform "Link to this definition")

Fit all transformers, transform the data and concatenate results.

Parameters:

**X**iterable or array-like, depending on transformers

Input data to be transformed.

**y**array-like of shape (n\_samples, n\_outputs), default=None

Targets for supervised learning.

**\*\*params**dict, default=None

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` methods of the sub-transformers.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` methods of the sub-transformers. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
     for more details.
    

Changed in version 1.5: `**params` can now be routed via metadata routing API.

Returns:

**X\_t**array-like or sparse matrix of shape (n\_samples, sum\_n\_components)

The `hstack` of results of transformers. `sum_n_components` is the sum of `n_components` (output dimension) over transformers.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1847)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L2167)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1759)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.get_params "Link to this definition")

Get parameters for this estimator.

Returns the parameters given in the constructor as well as the estimators contained within the `transformer_list` of the `FeatureUnion`.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**mapping of string to any

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1729)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.set_output "Link to this definition")

Set the output container when `"transform"` and `"fit_transform"` are called.

`set_output` will set the output of all estimators in `transformer_list`.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1779)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.set_params "Link to this definition")

Set the parameters of this estimator.

Valid parameter keys can be listed with `get_params()`. Note that you can directly set the parameters of the estimators contained in `transformer_list`.

Parameters:

**\*\*kwargs**dict

Parameters of this estimator or parameters of estimators contained in `transform_list`. Parameters of the transformers may be set using its name and the parameter name separated by a ‘\_\_’.

Returns:

**self**object

FeatureUnion class instance.

transform(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L2054)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.transform "Link to this definition")

Transform X separately by each transformer, concatenate results.

Parameters:

**X**iterable or array-like, depending on transformers

Input data to be transformed.

**\*\*params**dict, default=None

Parameters routed to the `transform` method of the sub-transformers via the metadata routing API. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Added in version 1.5.

Returns:

**X\_t**array-like or sparse matrix of shape (n\_samples, sum\_n\_components)

The `hstack` of results of transformers. `sum_n_components` is the sum of `n_components` (output dimension) over transformers.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)