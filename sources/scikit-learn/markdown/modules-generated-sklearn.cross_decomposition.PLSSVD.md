[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cross_decomposition.PLSSVD.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cross_decomposition.PLSSVD.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cross_decomposition.PLSSVD.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cross_decomposition.PLSSVD.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cross_decomposition.PLSSVD.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cross_decomposition.PLSSVD.html)

Collapse Sidebar Expand Sidebar

PLSSVD[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#plssvd "Link to this heading")

===================================================================================================================================

class sklearn.cross\_decomposition.PLSSVD(_n\_components\=2_, _\*_, _scale\=True_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cross_decomposition/_pls.py#L903)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "Link to this definition")

Partial Least Square SVD.

This transformer simply performs an SVD on the cross-covariance matrix `X'y`. It is able to project both the training data `X` and the targets `y`. The training data `X` is projected on the left singular vectors, while the targets are projected on the right singular vectors.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_decomposition.html#cross-decomposition)
.

Added in version 0.8.

Parameters:

**n\_components**int, default=2

The number of components to keep. Should be in `[1, min(n_samples, n_features, n_targets)]`.

**scale**bool, default=True

Whether to scale `X` and `y`.

**copy**bool, default=True

Whether to copy `X` and `y` in fit before applying centering, and potentially scaling. If `False`, these operations will be done inplace, modifying both arrays.

Attributes:

**x\_weights\_**ndarray of shape (n\_features, n\_components)

The left singular vectors of the SVD of the cross-covariance matrix. Used to project `X` in [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.transform "sklearn.cross_decomposition.PLSSVD.transform")
.

**y\_weights\_**ndarray of (n\_targets, n\_components)

The right singular vectors of the SVD of the cross-covariance matrix. Used to project `X` in [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.transform "sklearn.cross_decomposition.PLSSVD.transform")
.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")

Partial Least Squares transformer and regressor.

[`CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")

Canonical Correlation Analysis.

Examples

\>>> import numpy as np
\>>> from sklearn.cross\_decomposition import PLSSVD
\>>> X \= np.array(\[\[0., 0., 1.\],\
...               \[1., 0., 0.\],\
...               \[2., 2., 2.\],\
...               \[2., 5., 4.\]\])
\>>> y \= np.array(\[\[0.1, \-0.2\],\
...               \[0.9, 1.1\],\
...               \[6.2, 5.9\],\
...               \[11.9, 12.3\]\])
\>>> pls \= PLSSVD(n\_components\=2).fit(X, y)
\>>> X\_c, y\_c \= pls.transform(X, y)
\>>> X\_c.shape, y\_c.shape
((4, 2), (4, 2))

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cross_decomposition/_pls.py#L982)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.fit "Link to this definition")

Fit model to data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Targets.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cross_decomposition/_pls.py#L1079)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.fit_transform "Link to this definition")

Learn and apply the dimensionality reduction.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets), default=None

Targets.

Returns:

**out**array-like or tuple of array-like

The transformed data `X_transformed` if `y is not None`, `(X_transformed, y_transformed)` otherwise.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cross_decomposition/_pls.py#L1047)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD.transform "Link to this definition")

Apply the dimensionality reduction.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Samples to be transformed.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets), default=None

Targets.

Returns:

**x\_scores**array-like or tuple of array-like

The transformed data `X_transformed` if `y is not None`, `(X_transformed, y_transformed)` otherwise.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)