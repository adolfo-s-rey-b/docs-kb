[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.PCA.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.PCA.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.PCA.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.PCA.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.PCA.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.PCA.html)

Collapse Sidebar Expand Sidebar

PCA[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#pca "Link to this heading")

====================================================================================================================

class sklearn.decomposition.PCA(_n\_components\=None_, _\*_, _copy\=True_, _whiten\=False_, _svd\_solver\='auto'_, _tol\=0.0_, _iterated\_power\='auto'_, _n\_oversamples\=10_, _power\_iteration\_normalizer\='auto'_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_pca.py#L113)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "Link to this definition")

Principal component analysis (PCA).

Linear dimensionality reduction using Singular Value Decomposition of the data to project it to a lower dimensional space. The input data is centered but not scaled for each feature before applying the SVD.

It uses the LAPACK implementation of the full SVD or a randomized truncated SVD by the method of Halko et al. 2009, depending on the shape of the input data and the number of components to extract.

With sparse inputs, the ARPACK implementation of the truncated SVD can be used (i.e. through [`scipy.sparse.linalg.svds`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.svds.html#scipy.sparse.linalg.svds "(in SciPy v1.18.0)")
). Alternatively, one may consider [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
 where the data are not centered.

Notice that this class only supports sparse inputs for some solvers such as “arpack” and “covariance\_eigh”. See [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
 for an alternative with sparse data.

For a usage example, see [Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-auto-examples-decomposition-plot-pca-iris-py)

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#pca)
.

Parameters:

**n\_components**int, float or ‘mle’, default=None

Number of components to keep. if n\_components is not set all components are kept:

n\_components \== min(n\_samples, n\_features)

Copy to clipboard

If `n_components == 'mle'` and `svd_solver == 'full'`, Minka’s MLE is used to guess the dimension. Use of `n_components == 'mle'` will interpret `svd_solver == 'auto'` as `svd_solver == 'full'`.

If `0 < n_components < 1` and `svd_solver == 'full'`, select the number of components such that the amount of variance that needs to be explained is greater than the percentage specified by n\_components.

If `svd_solver == 'arpack'`, the number of components must be strictly less than the minimum of n\_features and n\_samples.

Hence, the None case results in:

n\_components \== min(n\_samples, n\_features) \- 1

Copy to clipboard

**copy**bool, default=True

If False, data passed to fit are overwritten and running fit(X).transform(X) will not yield the expected results, use fit\_transform(X) instead.

**whiten**bool, default=False

When True (False by default) the `components_` vectors are multiplied by the square root of n\_samples and then divided by the singular values to ensure uncorrelated outputs with unit component-wise variances.

Whitening will remove some information from the transformed signal (the relative variance scales of the components) but can sometime improve the predictive accuracy of the downstream estimators by making their data respect some hard-wired assumptions.

**svd\_solver**{‘auto’, ‘full’, ‘covariance\_eigh’, ‘arpack’, ‘randomized’}, default=’auto’

“auto” :

The solver is selected by a default ‘auto’ policy is based on `X.shape` and `n_components`: if the input data has fewer than 1000 features and more than 10 times as many samples, then the “covariance\_eigh” solver is used. Otherwise, if the input data is larger than 500x500 and the number of components to extract is lower than 80% of the smallest dimension of the data, then the more efficient “randomized” method is selected. Otherwise the exact “full” SVD is computed and optionally truncated afterwards.

“full” :

Run exact full SVD calling the standard LAPACK solver via `scipy.linalg.svd` and select the components by postprocessing

“covariance\_eigh” :

Precompute the covariance matrix (on centered data), run a classical eigenvalue decomposition on the covariance matrix typically using LAPACK and select the components by postprocessing. This solver is very efficient for n\_samples >> n\_features and small n\_features. It is, however, not tractable otherwise for large n\_features (large memory footprint required to materialize the covariance matrix). Also note that compared to the “full” solver, this solver effectively doubles the condition number and is therefore less numerical stable (e.g. on input data with a large range of singular values).

“arpack” :

Run SVD truncated to `n_components` calling ARPACK solver via `scipy.sparse.linalg.svds`. It requires strictly `0 < n_components < min(X.shape)`

“randomized” :

Run randomized SVD by the method of Halko et al.

Added in version 0.18.0.

Changed in version 1.5: Added the ‘covariance\_eigh’ solver.

**tol**float, default=0.0

Tolerance for singular values computed by svd\_solver == ‘arpack’. Must be of range \[0.0, infinity).\
\
Added in version 0.18.0.\
\
**iterated\_power**int or ‘auto’, default=’auto’\
\
Number of iterations for the power method computed by svd\_solver == ‘randomized’. Must be of range \[0, infinity).\
\
Added in version 0.18.0.\
\
**n\_oversamples**int, default=10\
\
This parameter is only relevant when `svd_solver="randomized"`. It corresponds to the additional number of random vectors to sample the range of `X` so as to ensure proper conditioning. See [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")\
 for more details.\
\
Added in version 1.1.\
\
**power\_iteration\_normalizer**{‘auto’, ‘QR’, ‘LU’, ‘none’}, default=’auto’\
\
Power iteration normalizer for randomized SVD solver. Not used by ARPACK. See [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")\
 for more details.\
\
Added in version 1.1.\
\
**random\_state**int, RandomState instance or None, default=None\
\
Used when the ‘arpack’ or ‘randomized’ solvers are used. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
.\
\
Added in version 0.18.0.\
\
Attributes:\
\
**components\_**ndarray of shape (n\_components, n\_features)\
\
Principal axes in feature space, representing the directions of maximum variance in the data. Equivalently, the right singular vectors of the centered input data, parallel to its eigenvectors. The components are sorted by decreasing `explained_variance_`.\
\
**explained\_variance\_**ndarray of shape (n\_components,)\
\
The amount of variance explained by each of the selected components. The variance estimation uses `n_samples - 1` degrees of freedom.\
\
Equal to n\_components largest eigenvalues of the covariance matrix of X.\
\
Added in version 0.18.\
\
**explained\_variance\_ratio\_**ndarray of shape (n\_components,)\
\
Percentage of variance explained by each of the selected components.\
\
If `n_components` is not set then all components are stored and the sum of the ratios is equal to 1.0.\
\
**singular\_values\_**ndarray of shape (n\_components,)\
\
The singular values corresponding to each of the selected components. The singular values are equal to the 2-norms of the `n_components` variables in the lower-dimensional space.\
\
Added in version 0.19.\
\
**mean\_**ndarray of shape (n\_features,)\
\
Per-feature empirical mean, estimated from the training set.\
\
Equal to `X.mean(axis=0)`.\
\
**n\_components\_**int\
\
The estimated number of components. When n\_components is set to ‘mle’ or a number between 0 and 1 (with svd\_solver == ‘full’) this number is estimated from input data. Otherwise it equals the parameter n\_components, or the lesser value of n\_features and n\_samples if n\_components is None.\
\
**n\_samples\_**int\
\
Number of samples in the training data.\
\
**noise\_variance\_**float\
\
The estimated noise covariance following the Probabilistic PCA model from Tipping and Bishop 1999. See “Pattern Recognition and Machine Learning” by C. Bishop, 12.2.1 p. 574 or [http://www.miketipping.com/papers/met-mppca.pdf](http://www.miketipping.com/papers/met-mppca.pdf)\
. It is required to compute the estimated data covariance and score samples.\
\
Equal to the average of (min(n\_features, n\_samples) - n\_components) smallest eigenvalues of the covariance matrix of X.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
See also\
\
[`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")\
\
Kernel Principal Component Analysis.\
\
[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")\
\
Sparse Principal Component Analysis.\
\
[`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")\
\
Dimensionality reduction using truncated SVD.\
\
[`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")\
\
Incremental Principal Component Analysis.\
\
References\
\
For n\_components == ‘mle’, this class uses the method from: [Minka, T. P.. “Automatic choice of dimensionality for PCA”. In NIPS, pp. 598-604](https://tminka.github.io/papers/pca/minka-pca.pdf)\
\
Implements the probabilistic PCA model from: [Tipping, M. E., and Bishop, C. M. (1999). “Probabilistic principal component analysis”. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 61(3), 611-622.](http://www.miketipping.com/papers/met-mppca.pdf)\
 via the score and score\_samples methods.\
\
For svd\_solver == ‘arpack’, refer to `scipy.sparse.linalg.svds`.\
\
For svd\_solver == ‘randomized’, see: [Halko, N., Martinsson, P. G., and Tropp, J. A. (2011). “Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions”. SIAM review, 53(2), 217-288.](https://doi.org/10.1137/090771806)\
 and also [Martinsson, P. G., Rokhlin, V., and Tygert, M. (2011). “A randomized algorithm for the decomposition of matrices”. Applied and Computational Harmonic Analysis, 30(1), 47-68.](https://doi.org/10.1016/j.acha.2010.02.003)\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn.decomposition import PCA\
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[\-3, \-2\], \[1, 1\], \[2, 1\], \[3, 2\]\])\
\>>> pca \= PCA(n\_components\=2)\
\>>> pca.fit(X)\
PCA(n\_components=2)\
\>>> print(pca.explained\_variance\_ratio\_)\
\[0.9924 0.0075\]\
\>>> print(pca.singular\_values\_)\
\[6.30061 0.54980\]\
\
Copy to clipboard\
\
\>>> pca \= PCA(n\_components\=2, svd\_solver\='full')\
\>>> pca.fit(X)\
PCA(n\_components=2, svd\_solver='full')\
\>>> print(pca.explained\_variance\_ratio\_)\
\[0.9924 0.00755\]\
\>>> print(pca.singular\_values\_)\
\[6.30061 0.54980\]\
\
Copy to clipboard\
\
\>>> pca \= PCA(n\_components\=1, svd\_solver\='arpack')\
\>>> pca.fit(X)\
PCA(n\_components=1, svd\_solver='arpack')\
\>>> print(pca.explained\_variance\_ratio\_)\
\[0.99244\]\
\>>> print(pca.singular\_values\_)\
\[6.30061\]\
\
Copy to clipboard\
\
fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_pca.py#L422)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit "Link to this definition")\
\
Fit the model with X.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Training data, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
**y**Ignored\
\
Ignored.\
\
Returns:\
\
**self**object\
\
Returns the instance itself.\
\
fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_pca.py#L443)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.fit_transform "Link to this definition")\
\
Fit the model with X and apply the dimensionality reduction on X.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Training data, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
**y**Ignored\
\
Ignored.\
\
Returns:\
\
**X\_new**ndarray of shape (n\_samples, n\_components)\
\
Transformed values.\
\
Notes\
\
This method returns a Fortran-ordered array. To convert it to a C-ordered array, use ‘np.ascontiguousarray’.\
\
get\_covariance()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L34)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.get_covariance "Link to this definition")\
\
Compute data covariance with the generative model.\
\
`cov = components_.T * S**2 * components_ + sigma2 * eye(n_features)` where S\*\*2 contains the explained variances, and sigma2 contains the noise variances.\
\
Returns:\
\
**cov**array of shape=(n\_features, n\_features)\
\
Estimated covariance of data.\
\
get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.get_feature_names_out "Link to this definition")\
\
Get output feature names for transformation.\
\
The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.\
\
Parameters:\
\
**input\_features**array-like of str or None, default=None\
\
Only used to validate feature names with the names seen in `fit`.\
\
Returns:\
\
**feature\_names\_out**ndarray of str objects\
\
Transformed feature names.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Returns:\
\
**routing**MetadataRequest\
\
A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
get\_precision()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L62)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.get_precision "Link to this definition")\
\
Compute data precision matrix with the generative model.\
\
Equals the inverse of the covariance but computed with the matrix inversion lemma for efficiency.\
\
Returns:\
\
**precision**array, shape=(n\_features, n\_features)\
\
Estimated precision of data.\
\
inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L177)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.inverse_transform "Link to this definition")\
\
Transform data back to its original space.\
\
In other words, return an input `X_original` whose transform would be X.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_components)\
\
New data, where `n_samples` is the number of samples and `n_components` is the number of components.\
\
Returns:\
\
**X\_original**array-like of shape (n\_samples, n\_features)\
\
Original data, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
Notes\
\
If whitening is enabled, inverse\_transform will compute the exact inverse operation, which includes reversing whitening.\
\
score(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_pca.py#L817)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.score "Link to this definition")\
\
Return the average log-likelihood of all samples.\
\
See. “Pattern Recognition and Machine Learning” by C. Bishop, 12.2.1 p. 574 or [http://www.miketipping.com/papers/met-mppca.pdf](http://www.miketipping.com/papers/met-mppca.pdf)\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
The data.\
\
**y**Ignored\
\
Ignored.\
\
Returns:\
\
**ll**float\
\
Average log-likelihood of the samples under the current model.\
\
score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_pca.py#L790)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.score_samples "Link to this definition")\
\
Return the log-likelihood of each sample.\
\
See. “Pattern Recognition and Machine Learning” by C. Bishop, 12.2.1 p. 574 or [http://www.miketipping.com/papers/met-mppca.pdf](http://www.miketipping.com/papers/met-mppca.pdf)\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
The data.\
\
Returns:\
\
**ll**ndarray of shape (n\_samples,)\
\
Log-likelihood of each sample under the current model.\
\
set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.set_output "Link to this definition")\
\
Set output container.\
\
Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)\
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)\
 for an example on how to use the API.\
\
Parameters:\
\
**transform**{“default”, “pandas”, “polars”}, default=None\
\
Configure output of `transform` and `fit_transform`.\
\
*   `"default"`: Default output format of a transformer\
    \
*   `"pandas"`: DataFrame output\
    \
*   `"polars"`: Polars output\
    \
*   `None`: Transform configuration is unchanged\
    \
\
Added in version 1.4: `"polars"` option was added.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_base.py#L125)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA.transform "Link to this definition")\
\
Apply dimensionality reduction to X.\
\
X is projected on the first principal components previously extracted from a training set.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
New data, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
Returns:\
\
**X\_new**array-like of shape (n\_samples, n\_components)\
\
Projection of X in the first principal components, where `n_samples` is the number of samples and `n_components` is the number of the components.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#gallery-examples "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)\
\
[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)\
\
Image denoising using kernel PCA\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)\
\
[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)\
\
Faces recognition example using eigenfaces and kernel approximation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)\
\
[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)\
\
A demo of K-Means clustering on the handwritten digits data\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)\
\
[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)\
\
Column Transformer with Heterogeneous Data Sources\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)\
\
[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)\
\
Selecting dimensionality reduction with Pipeline and GridSearchCV\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)\
\
[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)\
\
Pipelining: chaining a PCA and a logistic regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)\
\
[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)\
\
Concatenating multiple feature extraction methods\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_thumb.png)\
\
[Principal Component Regression vs Partial Least Squares Regression](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)\
\
Principal Component Regression vs Partial Least Squares Regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)\
\
[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)\
\
Faces dataset decompositions\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_blind_source_separation_thumb.png)\
\
[Blind source separation using FastICA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html)\
\
Blind source separation using FastICA\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_vs_pca_thumb.png)\
\
[FastICA on 2D point clouds](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html)\
\
FastICA on 2D point clouds\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)\
\
[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)\
\
Incremental PCA\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_thumb.png)\
\
[Kernel PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html)\
\
Kernel PCA\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)\
\
[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)\
\
Principal Component Analysis (PCA) on Iris Dataset\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_thumb.png)\
\
[Model selection with Probabilistic PCA and Factor Analysis (FA)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)\
\
Model selection with Probabilistic PCA and Factor Analysis (FA)\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)\
\
[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)\
\
Comparison of LDA and PCA 2D projection of Iris dataset\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_thumb.png)\
\
[Factor Analysis (with rotation) to visualize patterns](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html)\
\
Factor Analysis (with rotation) to visualize patterns\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mds_thumb.png)\
\
[Multi-dimensional scaling](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html)\
\
Multi-dimensional scaling\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_thumb.png)\
\
[Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)\
\
Explicit feature map approximation for RBF kernels\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_thumb.png)\
\
[Multilabel classification](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)\
\
Multilabel classification\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)\
\
[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)\
\
Displaying Pipelines\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)\
\
[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)\
\
Balance model complexity and cross-validated score\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_thumb.png)\
\
[Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)\
\
Kernel Density Estimation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_thumb.png)\
\
[Dimensionality Reduction with Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)\
\
Dimensionality Reduction with Neighborhood Components Analysis\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)\
\
[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)\
\
Importance of Feature Scaling\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)\
\
Release Highlights for scikit-learn 1.4\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)\
\
Release Highlights for scikit-learn 1.5\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)