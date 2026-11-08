[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.SpectralEmbedding.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.SpectralEmbedding.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.SpectralEmbedding.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.SpectralEmbedding.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.SpectralEmbedding.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.SpectralEmbedding.html)

Collapse Sidebar Expand Sidebar

SpectralEmbedding[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#spectralembedding "Link to this heading")

=========================================================================================================================================================

class sklearn.manifold.SpectralEmbedding(_n\_components\=2_, _\*_, _affinity\='nearest\_neighbors'_, _gamma\=None_, _random\_state\=None_, _eigen\_solver\=None_, _eigen\_tol\='auto'_, _n\_neighbors\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_spectral_embedding.py#L480)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "Link to this definition")

Spectral embedding for non-linear dimensionality reduction.

Forms an affinity matrix given by the specified function and applies spectral decomposition to the corresponding graph laplacian. The resulting transformation is given by the value of the eigenvectors for each data point.

Note : Laplacian Eigenmaps is the actual algorithm implemented here.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#spectral-embedding)
.

Parameters:

**n\_components**int, default=2

The dimension of the projected subspace.

**affinity**{‘nearest\_neighbors’, ‘rbf’, ‘precomputed’, ‘precomputed\_nearest\_neighbors’} or callable, default=’nearest\_neighbors’

How to construct the affinity matrix.

*   ‘nearest\_neighbors’ : construct the affinity matrix by computing a graph of nearest neighbors.
    
*   ‘rbf’ : construct the affinity matrix by computing a radial basis function (RBF) kernel.
    
*   ‘precomputed’ : interpret `X` as a precomputed affinity matrix.
    
*   ‘precomputed\_nearest\_neighbors’ : interpret `X` as a sparse graph of precomputed nearest neighbors, and constructs the affinity matrix by selecting the `n_neighbors` nearest neighbors.
    
*   callable : use passed in function as affinity the function takes in data matrix (n\_samples, n\_features) and return affinity matrix (n\_samples, n\_samples).
    

**gamma**float, default=None

Kernel coefficient for rbf kernel. If None, gamma will be set to 1/n\_features.

**random\_state**int, RandomState instance or None, default=None

A pseudo random number generator used for the initialization of the lobpcg eigen vectors decomposition when `eigen_solver == 'amg'`, and for the K-Means initialization. Use an int to make the results deterministic across calls (See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
).

Note

When using `eigen_solver == 'amg'`, it is necessary to also fix the global numpy seed with `np.random.seed(int)` to get deterministic results. See [pyamg/pyamg#139](https://github.com/pyamg/pyamg/issues/139)
 for further information.

**eigen\_solver**{‘arpack’, ‘lobpcg’, ‘amg’}, default=None

The eigenvalue decomposition strategy to use. AMG requires pyamg to be installed. It can be faster on very large, sparse problems. If None, then `'arpack'` is used.

**eigen\_tol**float, default=”auto”

Stopping criterion for eigendecomposition of the Laplacian matrix. If `eigen_tol="auto"` then the passed tolerance will depend on the `eigen_solver`:

*   If `eigen_solver="arpack"`, then `eigen_tol=0.0`;
    
*   If `eigen_solver="lobpcg"` or `eigen_solver="amg"`, then `eigen_tol=None` which configures the underlying `lobpcg` solver to automatically resolve the value according to their heuristics. See, [`scipy.sparse.linalg.lobpcg`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lobpcg.html#scipy.sparse.linalg.lobpcg "(in SciPy v1.18.0)")
     for details.
    

Note that when using `eigen_solver="lobpcg"` or `eigen_solver="amg"` values of `tol<1e-5` may lead to convergence issues and should be avoided.

Added in version 1.2.

**n\_neighbors**int, default=None

Number of nearest neighbors for nearest\_neighbors graph building. If None, n\_neighbors will be set to max(n\_samples/10, 1).

**n\_jobs**int, default=None

The number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**embedding\_**ndarray of shape (n\_samples, n\_components)

Spectral embedding of the training matrix.

**affinity\_matrix\_**ndarray of shape (n\_samples, n\_samples)

Affinity\_matrix constructed from samples or precomputed.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_neighbors\_**int

Number of nearest neighbors effectively used.

See also

[`Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")

Non-linear dimensionality reduction through Isometric Mapping.

References

*   [A Tutorial on Spectral Clustering, 2007 Ulrike von Luxburg](https://doi.org/10.1007/s11222-007-9033-z)
    
*   [On Spectral Clustering: Analysis and an algorithm, 2001 Andrew Y. Ng, Michael I. Jordan, Yair Weiss](https://citeseerx.ist.psu.edu/doc_view/pid/796c5d6336fc52aa84db575fb821c78918b65f58)
    
*   [Normalized cuts and image segmentation, 2000 Jianbo Shi, Jitendra Malik](https://doi.org/10.1109/34.868688)
    

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.manifold import SpectralEmbedding
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X.shape
(1797, 64)
\>>> embedding \= SpectralEmbedding(n\_components\=2)
\>>> X\_transformed \= embedding.fit\_transform(X\[:100\])
\>>> X\_transformed.shape
(100, 2)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_spectral_embedding.py#L726)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding.fit "Link to this definition")

Fit the model from data in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

If affinity is “precomputed” X : {array-like, sparse matrix}, shape (n\_samples, n\_samples), Interpret X as precomputed adjacency graph computed from samples.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_spectral_embedding.py#L763)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding.fit_transform "Link to this definition")

Fit the model from data in X and transform X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

If affinity is “precomputed” X : {array-like, sparse matrix} of shape (n\_samples, n\_samples), Interpret X as precomputed adjacency graph computed from samples.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**X\_new**array-like of shape (n\_samples, n\_components)

Spectral embedding of the training matrix.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)