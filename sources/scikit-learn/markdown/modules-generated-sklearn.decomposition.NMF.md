[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.NMF.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.NMF.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.NMF.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.NMF.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.NMF.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.NMF.html)

Collapse Sidebar Expand Sidebar

NMF[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#nmf "Link to this heading")

====================================================================================================================

class sklearn.decomposition.NMF(_n\_components\='auto'_, _\*_, _init\=None_, _solver\='cd'_, _beta\_loss\='frobenius'_, _tol\=0.0001_, _max\_iter\=200_, _random\_state\=None_, _alpha\_W\=0.0_, _alpha\_H\='same'_, _l1\_ratio\=0.0_, _verbose\=0_, _shuffle\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1320)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "Link to this definition")

Non-Negative Matrix Factorization (NMF).

Find two non-negative matrices, i.e. matrices with all non-negative elements, (W, H) whose product approximates the non-negative matrix X. This factorization can be used for example for dimensionality reduction, source separation or topic extraction.

The objective function is:

L(W,H)\=0.5∗||X−WH||loss2+alpha\_W∗l1\_ratio∗n\_features∗||vec(W)||1+alpha\_H∗l1\_ratio∗n\_samples∗||vec(H)||1+0.5∗alpha\_W∗(1−l1\_ratio)∗n\_features∗||W||Fro2+0.5∗alpha\_H∗(1−l1\_ratio)∗n\_samples∗||H||Fro2,

where ||A||Fro2\=∑i,jAij2 (Frobenius norm) and ||vec(A)||1\=∑i,jabs(Aij) (Elementwise L1 norm).

The generic norm ||X−WH||loss may represent the Frobenius norm or another supported beta-divergence loss. The choice between options is controlled by the `beta_loss` parameter.

The regularization terms are scaled by `n_features` for `W` and by `n_samples` for `H` to keep their impact balanced with respect to one another and to the data fit term as independent as possible of the size `n_samples` of the training set.

The objective function is minimized with an alternating minimization of W and H.

Note that the transformed data is named W and the components matrix is named H. In the NMF literature, the naming convention is usually the opposite since the data matrix X is transposed.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#nmf)
.

Parameters:

**n\_components**int or {‘auto’} or None, default=’auto’

Number of components. If `None`, all features are kept. If `n_components='auto'`, the number of components is automatically inferred from W or H shapes.

Changed in version 1.4: Added `'auto'` value.

Changed in version 1.6: Default value changed from `None` to `'auto'`.

**init**{‘random’, ‘nndsvd’, ‘nndsvda’, ‘nndsvdar’, ‘custom’}, default=None

Method used to initialize the procedure. Valid options:

*   `None`: ‘nndsvda’ if n\_components <= min(n\_samples, n\_features), otherwise random.
    
*   `'random'`: non-negative random matrices, scaled with: `sqrt(X.mean() / n_components)`
    
*   `'nndsvd'`: Nonnegative Double Singular Value Decomposition (NNDSVD) initialization (better for sparseness)
    
*   `'nndsvda'`: NNDSVD with zeros filled with the average of X (better when sparsity is not desired)
    
*   `'nndsvdar'` NNDSVD with zeros filled with small random values (generally faster, less accurate alternative to NNDSVDa for when sparsity is not desired)
    
*   `'custom'`: Use custom matrices `W` and `H` which must both be provided.
    

Changed in version 1.1: When `init=None` and n\_components is less than n\_samples and n\_features defaults to `nndsvda` instead of `nndsvd`.

**solver**{‘cd’, ‘mu’}, default=’cd’

Numerical solver to use:

*   ‘cd’ is a Coordinate Descent solver.
    
*   ‘mu’ is a Multiplicative Update solver.
    

Added in version 0.17: Coordinate Descent solver.

Added in version 0.19: Multiplicative Update solver.

**beta\_loss**float or {‘frobenius’, ‘kullback-leibler’, ‘itakura-saito’}, default=’frobenius’

Beta divergence to be minimized, measuring the distance between X and the dot product WH. Note that values different from ‘frobenius’ (or 2) and ‘kullback-leibler’ (or 1) lead to significantly slower fits. Note that for beta\_loss <= 0 (or ‘itakura-saito’), the input matrix X cannot contain zeros. Used only in ‘mu’ solver.

Added in version 0.19.

**tol**float, default=1e-4

Tolerance of the stopping condition.

**max\_iter**int, default=200

Maximum number of iterations before timing out.

**random\_state**int, RandomState instance or None, default=None

Used for initialisation (when `init` == ‘nndsvdar’ or ‘random’), and in Coordinate Descent. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**alpha\_W**float, default=0.0

Constant that multiplies the regularization terms of `W`. Set it to zero (default) to have no regularization on `W`.

Added in version 1.0.

**alpha\_H**float or “same”, default=”same”

Constant that multiplies the regularization terms of `H`. Set it to zero to have no regularization on `H`. If “same” (default), it takes the same value as `alpha_W`.

Added in version 1.0.

**l1\_ratio**float, default=0.0

The regularization mixing parameter, with 0 <= l1\_ratio <= 1. For l1\_ratio = 0 the penalty is an elementwise L2 penalty (aka Frobenius Norm). For l1\_ratio = 1 it is an elementwise L1 penalty. For 0 < l1\_ratio < 1, the penalty is a combination of L1 and L2.

Added in version 0.17: Regularization parameter _l1\_ratio_ used in the Coordinate Descent solver.

**verbose**int, default=0

Whether to be verbose.

**shuffle**bool, default=False

If true, randomize the order of coordinates in the CD solver.

Added in version 0.17: _shuffle_ parameter used in the Coordinate Descent solver.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Factorization matrix, sometimes called ‘dictionary’.

**n\_components\_**int

The number of components. It is same as the `n_components` parameter if it was given. Otherwise, it will be same as the number of features.

**reconstruction\_err\_**float

Frobenius norm of the matrix difference, or beta-divergence, between the training data `X` and the reconstructed data `WH` from the fitted model.

**n\_iter\_**int

Actual number of iterations.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")

Find a dictionary that sparsely encodes data.

[`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")

Mini-batch Sparse Principal Components Analysis.

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis.

[`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")

Find a sparse representation of data from a fixed, precomputed dictionary.

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis.

[`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")

Dimensionality reduction using truncated SVD.

References

\[1\]

[“Fast local algorithms for large scale nonnegative matrix and tensor factorizations”](https://doi.org/10.1587/transfun.E92.A.708)
 Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals of electronics, communications and computer sciences 92.3: 708-721, 2009.

\[2\]

[“Algorithms for nonnegative matrix factorization with the beta-divergence”](https://doi.org/10.1162/NECO_a_00168)
 Fevotte, C., & Idier, J. (2011). Neural Computation, 23(9).

Examples

\>>> import numpy as np
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[3, 1.2\], \[4, 1\], \[5, 0.8\], \[6, 1\]\])
\>>> from sklearn.decomposition import NMF
\>>> model \= NMF(n\_components\=2, init\='random', random\_state\=0)
\>>> W \= model.fit\_transform(X)
\>>> H \= model.components\_

Copy to clipboard

fit(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1262)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.fit "Link to this definition")

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

fit\_transform(_X_, _y\=None_, _W\=None_, _H\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1588)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.fit_transform "Link to this definition")

Learn a NMF model for the data X and returns the transformed data.

This is more efficient than calling fit followed by transform.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

**W**array-like of shape (n\_samples, n\_components), default=None

If `init='custom'`, it is used as initial guess for the solution. If `None`, uses the initialisation method specified in `init`.

**H**array-like of shape (n\_components, n\_features), default=None

If `init='custom'`, it is used as initial guess for the solution. If `None`, uses the initialisation method specified in `init`.

Returns:

**W**ndarray of shape (n\_samples, n\_components)

Transformed data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1288)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.inverse_transform "Link to this definition")

Transform data back to its original space.

Added in version 0.18.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_components)

Transformed data matrix.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Returns a data matrix of the original shape.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_nmf.py#L1731)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.transform "Link to this definition")

Transform the data X according to the fitted NMF model.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**W**ndarray of shape (n\_samples, n\_components)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_thumb.png)

[Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)

Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)