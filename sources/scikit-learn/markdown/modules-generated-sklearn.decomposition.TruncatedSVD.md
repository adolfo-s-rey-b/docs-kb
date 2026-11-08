[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.TruncatedSVD.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.TruncatedSVD.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.TruncatedSVD.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.TruncatedSVD.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.TruncatedSVD.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.TruncatedSVD.html)

Collapse Sidebar Expand Sidebar

TruncatedSVD[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#truncatedsvd "Link to this heading")

===============================================================================================================================================

class sklearn.decomposition.TruncatedSVD(_n\_components\=2_, _\*_, _algorithm\='randomized'_, _n\_iter\=5_, _n\_oversamples\=10_, _power\_iteration\_normalizer\='auto'_, _random\_state\=None_, _tol\=0.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_truncated_svd.py#L28)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "Link to this definition")

Dimensionality reduction using truncated SVD (aka LSA).

This transformer performs linear dimensionality reduction by means of truncated singular value decomposition (SVD). Contrary to PCA, this estimator does not center the data before computing the singular value decomposition. This means it can work with sparse matrices efficiently.

In particular, truncated SVD works on term count/tf-idf matrices as returned by the vectorizers in [`sklearn.feature_extraction.text`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.text "sklearn.feature_extraction.text")
. In that context, it is known as latent semantic analysis (LSA).

This estimator supports two algorithms: a fast randomized SVD solver, and a “naive” algorithm that uses ARPACK as an eigensolver on `X * X.T` or `X.T * X`, whichever is more efficient.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#lsa)
.

Parameters:

**n\_components**int, default=2

Desired dimensionality of output data. If algorithm=’arpack’, must be strictly less than the number of features. If algorithm=’randomized’, must be less than or equal to the number of features. The default value is useful for visualisation. For LSA, a value of 100 is recommended.

**algorithm**{‘arpack’, ‘randomized’}, default=’randomized’

SVD solver to use. Either “arpack” for the ARPACK wrapper in SciPy (scipy.sparse.linalg.svds), or “randomized” for the randomized algorithm due to Halko (2009).

**n\_iter**int, default=5

Number of iterations for randomized SVD solver. Not used by ARPACK. The default is larger than the default in [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
 to handle sparse matrices that may have large slowly decaying spectrum.

**n\_oversamples**int, default=10

Number of oversamples for randomized SVD solver. Not used by ARPACK. See [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
 for a complete description.

Added in version 1.1.

**power\_iteration\_normalizer**{‘auto’, ‘QR’, ‘LU’, ‘none’}, default=’auto’

Power iteration normalizer for randomized SVD solver. Not used by ARPACK. See [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
 for more details.

Added in version 1.1.

**random\_state**int, RandomState instance or None, default=None

Used during randomized svd. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**tol**float, default=0.0

Tolerance for ARPACK. 0 means machine precision. Ignored by randomized SVD solver.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

The right singular vectors of the input data.

**explained\_variance\_**ndarray of shape (n\_components,)

The variance of the training samples transformed by a projection to each component.

**explained\_variance\_ratio\_**ndarray of shape (n\_components,)

Percentage of variance explained by each of the selected components.

**singular\_values\_**ndarray of shape (n\_components,)

The singular values corresponding to each of the selected components. The singular values are equal to the 2-norms of the `n_components` variables in the lower-dimensional space.

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

[`FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")

A simple linear generative model with Gaussian latent variables.

[`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")

Incremental principal components analysis.

[`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

Kernel Principal component analysis.

[`NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")

Non-Negative Matrix Factorization.

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis.

Notes

SVD suffers from a problem called “sign indeterminacy”, which means the sign of the `components_` and the output from transform depend on the algorithm and random state. To work around this, fit instances of this class to data once, then keep the instance around to do transformations.

References

[Halko, et al. (2009). “Finding structure with randomness: Stochastic algorithms for constructing approximate matrix decompositions”](https://arxiv.org/abs/0909.4061)

Examples

\>>> from sklearn.decomposition import TruncatedSVD
\>>> from scipy.sparse import csr\_array
\>>> import numpy as np
\>>> np.random.seed(0)
\>>> X\_dense \= np.random.rand(100, 100)
\>>> X\_dense\[:, 2 \* np.arange(50)\] \= 0
\>>> X \= csr\_array(X\_dense)
\>>> svd \= TruncatedSVD(n\_components\=5, n\_iter\=7, random\_state\=42)
\>>> svd.fit(X)
TruncatedSVD(n\_components=5, n\_iter=7, random\_state=42)
\>>> print(svd.explained\_variance\_ratio\_)
\[0.0157 0.0512 0.0499 0.0479 0.0453\]
\>>> print(svd.explained\_variance\_ratio\_.sum())
0.2102
\>>> print(svd.singular\_values\_)
\[35.2410  4.5981   4.5420  4.4486  4.3288\]

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_truncated_svd.py#L190)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.fit "Link to this definition")

Fit model on training data X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Returns the transformer object.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_truncated_svd.py#L209)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.fit_transform "Link to this definition")

Fit model to X and perform dimensionality reduction on X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Reduced version of X. This will always be a dense array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_truncated_svd.py#L295)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.inverse_transform "Link to this definition")

Transform X back to its original space.

Returns an array X\_original whose transform would be X.

Parameters:

**X**array-like of shape (n\_samples, n\_components)

New data.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Note that this is always a dense array.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_truncated_svd.py#L278)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.transform "Link to this definition")

Perform dimensionality reduction on X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

New data.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Reduced version of X. This will always be a dense array.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_embedding_thumb.png)

[Hashing feature transformation using Totally Random Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html)

Hashing feature transformation using Totally Random Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)