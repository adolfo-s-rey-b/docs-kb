[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.MiniBatchNMF.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.MiniBatchNMF.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.MiniBatchNMF.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.MiniBatchNMF.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.MiniBatchNMF.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.MiniBatchNMF.html)

Collapse Sidebar Expand Sidebar

MiniBatchNMF[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#minibatchnmf "Link to this heading")

===============================================================================================================================================

class sklearn.decomposition.MiniBatchNMF(_n\_components\='auto'_, _\*_, _init\=None_, _batch\_size\=1024_, _beta\_loss\='frobenius'_, _tol\=0.0001_, _max\_no\_improvement\=10_, _max\_iter\=200_, _alpha\_W\=0.0_, _alpha\_H\='same'_, _l1\_ratio\=0.0_, _forget\_factor\=0.7_, _fresh\_restarts\=False_, _fresh\_restarts\_max\_iter\=30_, _transform\_max\_iter\=None_, _random\_state\=None_, _verbose\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1761)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "Link to this definition")

Mini-Batch Non-Negative Matrix Factorization (NMF).

Added in version 1.1.

Find two non-negative matrices, i.e. matrices with all non-negative elements, (`W`, `H`) whose product approximates the non-negative matrix `X`. This factorization can be used for example for dimensionality reduction, source separation or topic extraction.

The objective function is:

L(W,H)\=0.5∗||X−WH||loss2+alpha\_W∗l1\_ratio∗n\_features∗||vec(W)||1+alpha\_H∗l1\_ratio∗n\_samples∗||vec(H)||1+0.5∗alpha\_W∗(1−l1\_ratio)∗n\_features∗||W||Fro2+0.5∗alpha\_H∗(1−l1\_ratio)∗n\_samples∗||H||Fro2,

where ||A||Fro2\=∑i,jAij2 (Frobenius norm) and ||vec(A)||1\=∑i,jabs(Aij) (Elementwise L1 norm).

The generic norm ||X−WH||loss2 may represent the Frobenius norm or another supported beta-divergence loss. The choice between options is controlled by the `beta_loss` parameter.

The objective function is minimized with an alternating minimization of `W` and `H`.

Note that the transformed data is named `W` and the components matrix is named `H`. In the NMF literature, the naming convention is usually the opposite since the data matrix `X` is transposed.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#minibatchnmf)
.

Parameters:

**n\_components**int or {‘auto’} or None, default=’auto’

Number of components. If `None`, all features are kept. If `n_components='auto'`, the number of components is automatically inferred from W or H shapes.

Changed in version 1.4: Added `'auto'` value.

Changed in version 1.6: Default value changed from `None` to `'auto'`.

**init**{‘random’, ‘nndsvd’, ‘nndsvda’, ‘nndsvdar’, ‘custom’}, default=None

Method used to initialize the procedure. Valid options:

*   `None`: ‘nndsvda’ if `n_components <= min(n_samples, n_features)`, otherwise random.
    
*   `'random'`: non-negative random matrices, scaled with: `sqrt(X.mean() / n_components)`
    
*   `'nndsvd'`: Nonnegative Double Singular Value Decomposition (NNDSVD) initialization (better for sparseness).
    
*   `'nndsvda'`: NNDSVD with zeros filled with the average of X (better when sparsity is not desired).
    
*   `'nndsvdar'` NNDSVD with zeros filled with small random values (generally faster, less accurate alternative to NNDSVDa for when sparsity is not desired).
    
*   `'custom'`: Use custom matrices `W` and `H` which must both be provided.
    

**batch\_size**int, default=1024

Number of samples in each mini-batch. Large batch sizes give better long-term convergence at the cost of a slower start.

**beta\_loss**float or {‘frobenius’, ‘kullback-leibler’, ‘itakura-saito’}, default=’frobenius’

Beta divergence to be minimized, measuring the distance between `X` and the dot product `WH`. Note that values different from ‘frobenius’ (or 2) and ‘kullback-leibler’ (or 1) lead to significantly slower fits. Note that for `beta_loss <= 0` (or ‘itakura-saito’), the input matrix `X` cannot contain zeros.

**tol**float, default=1e-4

Control early stopping based on the norm of the differences in `H` between 2 steps. To disable early stopping based on changes in `H`, set `tol` to 0.0.

**max\_no\_improvement**int, default=10

Control early stopping based on the consecutive number of mini batches that does not yield an improvement on the smoothed cost function. To disable convergence detection based on cost function, set `max_no_improvement` to None.

**max\_iter**int, default=200

Maximum number of iterations over the complete dataset before timing out.

**alpha\_W**float, default=0.0

Constant that multiplies the regularization terms of `W`. Set it to zero (default) to have no regularization on `W`.

**alpha\_H**float or “same”, default=”same”

Constant that multiplies the regularization terms of `H`. Set it to zero to have no regularization on `H`. If “same” (default), it takes the same value as `alpha_W`.

**l1\_ratio**float, default=0.0

The regularization mixing parameter, with 0 <= l1\_ratio <= 1. For l1\_ratio = 0 the penalty is an elementwise L2 penalty (aka Frobenius Norm). For l1\_ratio = 1 it is an elementwise L1 penalty. For 0 < l1\_ratio < 1, the penalty is a combination of L1 and L2.

**forget\_factor**float, default=0.7

Amount of rescaling of past information. Its value could be 1 with finite datasets. Choosing values < 1 is recommended with online learning as more recent batches will weight more than past batches.

**fresh\_restarts**bool, default=False

Whether to completely solve for W at each step. Doing fresh restarts will likely lead to a better solution for a same number of iterations but it is much slower.

**fresh\_restarts\_max\_iter**int, default=30

Maximum number of iterations when solving for W at each step. Only used when doing fresh restarts. These iterations may be stopped early based on a small change of W controlled by `tol`.

**transform\_max\_iter**int, default=None

Maximum number of iterations when solving for W at transform time. If None, it defaults to `max_iter`.

**random\_state**int, RandomState instance or None, default=None

Used for initialisation (when `init` == ‘nndsvdar’ or ‘random’), and in Coordinate Descent. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**verbose**int, default=0

Whether to be verbose.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Factorization matrix, sometimes called ‘dictionary’.

**n\_components\_**int

The number of components. It is same as the `n_components` parameter if it was given. Otherwise, it will be same as the number of features.

**reconstruction\_err\_**float

Frobenius norm of the matrix difference, or beta-divergence, between the training data `X` and the reconstructed data `WH` from the fitted model.

**n\_iter\_**int

Actual number of started iterations over the whole dataset.

**n\_steps\_**int

Number of mini-batches processed.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

See also

[`NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")

Non-negative matrix factorization.

[`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")

Finds a dictionary that can best be used to represent data using a sparse code.

References

\[1\]

[“Fast local algorithms for large scale nonnegative matrix and tensor factorizations”](https://doi.org/10.1587/transfun.E92.A.708)
 Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals of electronics, communications and computer sciences 92.3: 708-721, 2009.

\[2\]

[“Algorithms for nonnegative matrix factorization with the beta-divergence”](https://doi.org/10.1162/NECO_a_00168)
 Fevotte, C., & Idier, J. (2011). Neural Computation, 23(9).

\[3\]

[“Online algorithms for nonnegative matrix factorization with the Itakura-Saito divergence”](https://doi.org/10.1109/ASPAA.2011.6082314)
 Lefevre, A., Bach, F., Fevotte, C. (2011). WASPA.

Examples

\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[3, 1.2\], \[4, 1\], \[5, 0.8\], \[6, 1\]\])
\>>> from sklearn.decomposition import MiniBatchNMF
\>>> model \= MiniBatchNMF(n\_components\=2, init\='random', random\_state\=0)
\>>> W \= model.fit\_transform(X)
\>>> H \= model.components\_

Copy to clipboard

fit(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1262)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.fit "Link to this definition")

Learn a NMF model for the data X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*params**kwargs

Parameters (keyword arguments) and values passed to the fit\_transform instance.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _W\=None_, _H\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L2177)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.fit_transform "Link to this definition")

Learn a NMF model for the data X and returns the transformed data.

This is more efficient than calling fit followed by transform.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data matrix to be decomposed.

**y**Ignored

Not used, present here for API consistency by convention.

**W**array-like of shape (n\_samples, n\_components), default=None

If `init='custom'`, it is used as initial guess for the solution. If `None`, uses the initialisation method specified in `init`.

**H**array-like of shape (n\_components, n\_features), default=None

If `init='custom'`, it is used as initial guess for the solution. If `None`, uses the initialisation method specified in `init`.

Returns:

**W**ndarray of shape (n\_samples, n\_components)

Transformed data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1288)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.inverse_transform "Link to this definition")

Transform data back to its original space.

Added in version 0.18.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_components)

Transformed data matrix.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Returns a data matrix of the original shape.

partial\_fit(_X_, _y\=None_, _W\=None_, _H\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L2345)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.partial_fit "Link to this definition")

Update the model using the data in `X` as a mini-batch.

This method is expected to be called several times consecutively on different chunks of a dataset so as to implement out-of-core or online learning.

This is especially useful when the whole dataset is too big to fit in memory at once (see [Strategies to scale computationally: bigger data](https://scikit-learn.org/stable/computing/scaling_strategies.html#scaling-strategies)
).

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data matrix to be decomposed.

**y**Ignored

Not used, present here for API consistency by convention.

**W**array-like of shape (n\_samples, n\_components), default=None

If `init='custom'`, it is used as initial guess for the solution. Only used for the first call to `partial_fit`.

**H**array-like of shape (n\_components, n\_features), default=None

If `init='custom'`, it is used as initial guess for the solution. Only used for the first call to `partial_fit`.

Returns:

self

Returns the instance itself.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_partial\_fit\_request(_\*_, _H: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_, _W: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition._nmf.MiniBatchNMF")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.set_partial_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `partial_fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `partial_fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `partial_fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**H**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `H` parameter in `partial_fit`.

**W**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `W` parameter in `partial_fit`.

Returns:

**self**object

The updated object.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L2319)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.transform "Link to this definition")

Transform the data X according to the fitted MiniBatchNMF model.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data matrix to be transformed by the model.

Returns:

**W**ndarray of shape (n\_samples, n\_components)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_thumb.png)

[Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)

Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)