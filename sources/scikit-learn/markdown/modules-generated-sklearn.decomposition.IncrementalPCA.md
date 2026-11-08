[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.IncrementalPCA.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.IncrementalPCA.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.IncrementalPCA.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.IncrementalPCA.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.IncrementalPCA.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.IncrementalPCA.html)

Collapse Sidebar Expand Sidebar

IncrementalPCA[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#incrementalpca "Link to this heading")

=====================================================================================================================================================

class sklearn.decomposition.IncrementalPCA(_n\_components\=None_, _\*_, _whiten\=False_, _copy\=True_, _batch\_size\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_incremental_pca.py#L19)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "Link to this definition")

Incremental principal components analysis (IPCA).

Linear dimensionality reduction using Singular Value Decomposition of the data, keeping only the most significant singular vectors to project the data to a lower dimensional space. The input data is centered but not scaled for each feature before applying the SVD.

Depending on the size of the input data, this algorithm can be much more memory efficient than a PCA, and allows sparse input.

This algorithm has constant memory complexity, on the order of `batch_size * n_features`, enabling use of np.memmap files without loading the entire file into memory. For sparse matrices, the input is converted to dense in batches (in order to be able to subtract the mean) which avoids storing the entire dense matrix at any one time.

The computational overhead of each SVD is `O(batch_size * n_features ** 2)`, but only 2 \* batch\_size samples remain in memory at a time. There will be `n_samples / batch_size` SVD computations to get the principal components, versus 1 large SVD of complexity `O(n_samples * n_features ** 2)` for PCA.

For a usage example, see [Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html#sphx-glr-auto-examples-decomposition-plot-incremental-pca-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#incrementalpca)
.

Added in version 0.16.

Parameters:

**n\_components**int, default=None

Number of components to keep. If `n_components` is `None`, then `n_components` is set to `min(n_samples, n_features)`.

**whiten**bool, default=False

When True (False by default) the `components_` vectors are divided by `n_samples` times `components_` to ensure uncorrelated outputs with unit component-wise variances.

Whitening will remove some information from the transformed signal (the relative variance scales of the components) but can sometimes improve the predictive accuracy of the downstream estimators by making data respect some hard-wired assumptions.

**copy**bool, default=True

If False, X will be overwritten. `copy=False` can be used to save memory but is unsafe for general use.

**batch\_size**int, default=None

The number of samples to use for each batch. Only used when calling `fit`. If `batch_size` is `None`, then `batch_size` is inferred from the data and set to `5 * n_features`, to provide a balance between approximation accuracy and memory consumption.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Principal axes in feature space, representing the directions of maximum variance in the data. Equivalently, the right singular vectors of the centered input data, parallel to its eigenvectors. The components are sorted by decreasing `explained_variance_`.

**explained\_variance\_**ndarray of shape (n\_components,)

Variance explained by each of the selected components.

**explained\_variance\_ratio\_**ndarray of shape (n\_components,)

Percentage of variance explained by each of the selected components. If all components are stored, the sum of explained variances is equal to 1.0.

**singular\_values\_**ndarray of shape (n\_components,)

The singular values corresponding to each of the selected components. The singular values are equal to the 2-norms of the `n_components` variables in the lower-dimensional space.

**mean\_**ndarray of shape (n\_features,)

Per-feature empirical mean, aggregate over calls to `partial_fit`.

**var\_**ndarray of shape (n\_features,)

Per-feature empirical variance, aggregate over calls to `partial_fit`.

**noise\_variance\_**float

The estimated noise covariance following the Probabilistic PCA model from Tipping and Bishop 1999. See “Pattern Recognition and Machine Learning” by C. Bishop, 12.2.1 p. 574 or [http://www.miketipping.com/papers/met-mppca.pdf](http://www.miketipping.com/papers/met-mppca.pdf)
.

**n\_components\_**int

The estimated number of components. Relevant when `n_components=None`.

**n\_samples\_seen\_**int

The number of samples processed by the estimator. Will be reset on new calls to fit, but increments across `partial_fit` calls.

**batch\_size\_**int

Inferred batch size from `batch_size`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis (PCA).

[`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

Kernel Principal component analysis (KPCA).

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis (SparsePCA).

[`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")

Dimensionality reduction using truncated SVD.

Notes

Implements the incremental PCA model from Ross et al. (2008) [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#rd9b26913bb25-1)
. This model is an extension of the Sequential Karhunen-Loeve Transform from Levy and Lindenbaum (2000) [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#rd9b26913bb25-2)
.

We have specifically abstained from an optimization used by authors of both papers, a QR decomposition used in specific situations to reduce the algorithmic complexity of the SVD. The source for this technique is _Matrix Computations_ (Golub and Van Loan 1997 [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#rd9b26913bb25-3)
). This technique has been omitted because it is advantageous only when decomposing a matrix with `n_samples` (rows) >= 5/3 \* `n_features` (columns), and hurts the readability of the implemented algorithm. This would be a good opportunity for future optimization, if it is deemed necessary.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#id1)\
\]

D. Ross, J. Lim, R. Lin, M. Yang. Incremental Learning for Robust Visual Tracking, International Journal of Computer Vision, Volume 77, Issue 1-3, pp. 125-141, May 2008. [https://www.cs.toronto.edu/~dross/ivt/RossLimLinYang\_ijcv.pdf](https://www.cs.toronto.edu/~dross/ivt/RossLimLinYang_ijcv.pdf)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#id2)\
\]

[A. Levy and M. Lindenbaum, Sequential Karhunen-Loeve Basis Extraction and its Application to Images, IEEE Transactions on Image Processing, Volume 9, Number 8, pp. 1371-1374, August 2000.](https://doi.org/10.1109/83.855432)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#id3)\
\]

G. Golub and C. Van Loan. Matrix Computations, Third Edition, Chapter 5, Section 5.4.4, pp. 252-253, 1997.

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.decomposition import IncrementalPCA
\>>> from scipy import sparse
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> transformer \= IncrementalPCA(n\_components\=7, batch\_size\=200)
\>>> \# either partially fit on smaller batches of data
\>>> transformer.partial\_fit(X\[:100, :\])
IncrementalPCA(batch\_size=200, n\_components=7)
\>>> \# or let the fit function itself divide the data into batches
\>>> X\_sparse \= sparse.csr\_array(X)
\>>> X\_transformed \= transformer.fit\_transform(X\_sparse)
\>>> X\_transformed.shape
(1797, 7)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_incremental_pca.py#L201)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.fit "Link to this definition")

Fit the model with X, using minibatches of size batch\_size.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.fit_transform "Link to this definition")

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

get\_covariance()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L34)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.get_covariance "Link to this definition")

Compute data covariance with the generative model.

`cov = components_.T * S**2 * components_ + sigma2 * eye(n_features)` where S\*\*2 contains the explained variances, and sigma2 contains the noise variances.

Returns:

**cov**array of shape=(n\_features, n\_features)

Estimated covariance of data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_precision()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L62)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.get_precision "Link to this definition")

Compute data precision matrix with the generative model.

Equals the inverse of the covariance but computed with the matrix inversion lemma for efficiency.

Returns:

**precision**array, shape=(n\_features, n\_features)

Estimated precision of data.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L177)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.inverse_transform "Link to this definition")

Transform data back to its original space.

In other words, return an input `X_original` whose transform would be X.

Parameters:

**X**array-like of shape (n\_samples, n\_components)

New data, where `n_samples` is the number of samples and `n_components` is the number of components.

Returns:

**X\_original**array-like of shape (n\_samples, n\_features)

Original data, where `n_samples` is the number of samples and `n_features` is the number of features.

Notes

If whitening is enabled, inverse\_transform will compute the exact inverse operation, which includes reversing whitening.

partial\_fit(_X_, _y\=None_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_incremental_pca.py#L253)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.partial_fit "Link to this definition")

Incremental fit with X. All of X is processed as a single batch.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

**check\_input**bool, default=True

Run check\_array on X.

Returns:

**self**object

Returns the instance itself.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_incremental_pca.py#L378)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.transform "Link to this definition")

Apply dimensionality reduction to X.

X is projected on the first principal components previously extracted from a training set, using minibatches of size batch\_size if X is sparse.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Projection of X in the first principal components.

Examples

\>>> import numpy as np
\>>> from sklearn.decomposition import IncrementalPCA
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[\-3, \-2\],\
...               \[1, 1\], \[2, 1\], \[3, 2\]\])
\>>> ipca \= IncrementalPCA(n\_components\=2, batch\_size\=3)
\>>> ipca.fit(X)
IncrementalPCA(batch\_size=3, n\_components=2)
\>>> ipca.transform(X)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)