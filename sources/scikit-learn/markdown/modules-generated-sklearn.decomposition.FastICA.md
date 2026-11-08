[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.FastICA.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.FastICA.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.FastICA.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.FastICA.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.FastICA.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.FastICA.html)

Collapse Sidebar Expand Sidebar

FastICA[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#fastica "Link to this heading")

================================================================================================================================

class sklearn.decomposition.FastICA(_n\_components\=None_, _\*_, _algorithm\='parallel'_, _whiten\='unit-variance'_, _fun\='logcosh'_, _fun\_args\=None_, _max\_iter\=200_, _tol\=0.0001_, _w\_init\=None_, _whiten\_solver\='svd'_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_fastica.py#L375)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "Link to this definition")

FastICA: a fast algorithm for Independent Component Analysis.

The implementation is based on [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#r44c805292efc-1)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#ica)
.

Parameters:

**n\_components**int, default=None

Number of components to use. If None is passed, all are used.

**algorithm**{‘parallel’, ‘deflation’}, default=’parallel’

Specify which algorithm to use for FastICA.

**whiten**str or bool, default=’unit-variance’

Specify the whitening strategy to use.

*   If ‘arbitrary-variance’, a whitening with variance arbitrary is used.
    
*   If ‘unit-variance’, the whitening matrix is rescaled to ensure that each recovered source has unit variance.
    
*   If False, the data is already considered to be whitened, and no whitening is performed.
    

Changed in version 1.3: The default value of `whiten` changed to ‘unit-variance’ in 1.3.

**fun**{‘logcosh’, ‘exp’, ‘cube’} or callable, default=’logcosh’

The functional form of the G function used in the approximation to neg-entropy. Could be either ‘logcosh’, ‘exp’, or ‘cube’. You can also provide your own function. It should return a tuple containing the value of the function, and of its derivative, in the point. The derivative should be averaged along its last dimension. Example:

def my\_g(x):
    return x \*\* 3, (3 \* x \*\* 2).mean(axis\=-1)

Copy to clipboard

**fun\_args**dict, default=None

Arguments to send to the functional form. If empty or None and if fun=’logcosh’, fun\_args will take value {‘alpha’ : 1.0}.

**max\_iter**int, default=200

Maximum number of iterations during fit.

**tol**float, default=1e-4

A positive scalar giving the tolerance at which the un-mixing matrix is considered to have converged.

**w\_init**array-like of shape (n\_components, n\_components), default=None

Initial un-mixing array. If `w_init=None`, then an array of values drawn from a normal distribution is used.

**whiten\_solver**{“eigh”, “svd”}, default=”svd”

The solver to use for whitening.

*   “svd” is more stable numerically if the problem is degenerate, and often faster when `n_samples <= n_features`.
    
*   “eigh” is generally more memory efficient when `n_samples >= n_features`, and can be faster when `n_samples >= 50 * n_features`.
    

Added in version 1.2.

**random\_state**int, RandomState instance or None, default=None

Used to initialize `w_init` when not specified, with a normal distribution. Pass an int, for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

The linear operator to apply to the data to get the independent sources. This is equal to the unmixing matrix when `whiten` is False, and equal to `np.dot(unmixing_matrix, self.whitening_)` when `whiten` is True.

**mixing\_**ndarray of shape (n\_features, n\_components)

The pseudo-inverse of `components_`. It is the linear operator that maps independent sources to the data.

**mean\_**ndarray of shape(n\_features,)

The mean over features. Only set if `self.whiten` is True.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

If the algorithm is “deflation”, n\_iter is the maximum number of iterations run across all components. Else they are just the number of iterations taken to converge.

**whitening\_**ndarray of shape (n\_components, n\_features)

Only set if whiten is ‘True’. This is the pre-whitening matrix that projects data onto the first `n_components` principal components.

See also

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis (PCA).

[`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")

Incremental principal components analysis (IPCA).

[`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

Kernel Principal component analysis (KPCA).

[`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")

Mini-batch Sparse Principal Components Analysis.

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis (SparsePCA).

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#id1)\
\]

A. Hyvarinen and E. Oja, Independent Component Analysis: Algorithms and Applications, Neural Networks, 13(4-5), 2000, pp. 411-430.

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.decomposition import FastICA
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> transformer \= FastICA(n\_components\=7,
...         random\_state\=0,
...         whiten\='unit-variance')
\>>> X\_transformed \= transformer.fit\_transform(X)
\>>> X\_transformed.shape
(1797, 7)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_fastica.py#L726)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.fit "Link to this definition")

Fit the model to X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_fastica.py#L705)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.fit_transform "Link to this definition")

Fit the model and recover the sources from X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Estimated sources obtained by transforming the data with the estimated unmixing matrix.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_fastica.py#L779)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.inverse_transform "Link to this definition")

Transform the sources back to the mixed data (apply mixing matrix).

Parameters:

**X**array-like of shape (n\_samples, n\_components)

Sources, where `n_samples` is the number of samples and `n_components` is the number of components.

**copy**bool, default=True

If False, data passed to fit are overwritten. Defaults to True.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Reconstructed data obtained with the mixing matrix.

set\_inverse\_transform\_request(_\*_, _copy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition._fastica.FastICA")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.set_inverse_transform_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `inverse_transform` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `inverse_transform` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `inverse_transform`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**copy**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `copy` parameter in `inverse_transform`.

Returns:

**self**object

The updated object.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_transform\_request(_\*_, _copy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition._fastica.FastICA")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.set_transform_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `transform` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `transform` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `transform`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**copy**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `copy` parameter in `transform`.

Returns:

**self**object

The updated object.

transform(_X_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_fastica.py#L747)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.transform "Link to this definition")

Recover the sources from X (apply the unmixing matrix).

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data to transform, where `n_samples` is the number of samples and `n_features` is the number of features.

**copy**bool, default=True

If False, data passed to fit can be overwritten. Defaults to True.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Estimated sources obtained by transforming the data with the estimated unmixing matrix.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_blind_source_separation_thumb.png)

[Blind source separation using FastICA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html)

Blind source separation using FastICA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_vs_pca_thumb.png)

[FastICA on 2D point clouds](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html)

FastICA on 2D point clouds

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)