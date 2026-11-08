[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html)

Collapse Sidebar Expand Sidebar

LocallyLinearEmbedding[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#locallylinearembedding "Link to this heading")

========================================================================================================================================================================

class sklearn.manifold.LocallyLinearEmbedding(_\*_, _n\_neighbors\=5_, _n\_components\=2_, _reg\=0.001_, _eigen\_solver\='auto'_, _tol\=1e-06_, _max\_iter\=100_, _method\='standard'_, _hessian\_tol\=0.0001_, _modified\_tol\=1e-12_, _neighbors\_algorithm\='auto'_, _random\_state\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_locally_linear.py#L608)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "Link to this definition")

Locally Linear Embedding.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#locally-linear-embedding)
.

Parameters:

**n\_neighbors**int, default=5

Number of neighbors to consider for each point.

**n\_components**int, default=2

Number of coordinates for the manifold.

**reg**float, default=1e-3

Regularization constant, multiplies the trace of the local covariance matrix of the distances.

**eigen\_solver**{‘auto’, ‘arpack’, ‘dense’}, default=’auto’

The solver used to compute the eigenvectors. The available options are:

*   `'auto'` : algorithm will attempt to choose the best method for input data.
    
*   `'arpack'` : use arnoldi iteration in shift-invert mode. For this method, M may be a dense matrix, sparse matrix, or general linear operator.
    
*   `'dense'` : use standard dense matrix operations for the eigenvalue decomposition. For this method, M must be an array or matrix type. This method should be avoided for large problems.
    

Warning

ARPACK can be unstable for some problems. It is best to try several random seeds in order to check results.

**tol**float, default=1e-6

Tolerance for ‘arpack’ method Not used if eigen\_solver==’dense’.

**max\_iter**int, default=100

Maximum number of iterations for the arpack solver. Not used if eigen\_solver==’dense’.

**method**{‘standard’, ‘hessian’, ‘modified’, ‘ltsa’}, default=’standard’

*   `standard`: use the standard locally linear embedding algorithm. see reference [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#r62e36dd1b056-1)
    
*   `hessian`: use the Hessian eigenmap method. This method requires `n_neighbors > n_components * (1 + (n_components + 1) / 2`. see reference [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#r62e36dd1b056-2)
    
*   `modified`: use the modified locally linear embedding algorithm. see reference [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#r62e36dd1b056-3)
    
*   `ltsa`: use local tangent space alignment algorithm. see reference [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#r62e36dd1b056-4)
    

**hessian\_tol**float, default=1e-4

Tolerance for Hessian eigenmapping method. Only used if `method == 'hessian'`.

**modified\_tol**float, default=1e-12

Tolerance for modified LLE method. Only used if `method == 'modified'`.

**neighbors\_algorithm**{‘auto’, ‘brute’, ‘kd\_tree’, ‘ball\_tree’}, default=’auto’

Algorithm to use for nearest neighbors search, passed to [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
 instance.

**random\_state**int, RandomState instance, default=None

Determines the random number generator when `eigen_solver` == ‘arpack’. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int or None, default=None

The number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**embedding\_**array-like, shape \[n\_samples, n\_components\]

Stores the embedding vectors

**reconstruction\_error\_**float

Reconstruction error associated with `embedding_`

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**nbrs\_**NearestNeighbors object

Stores nearest neighbors instance, including BallTree or KDtree if applicable.

See also

[`SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")

Spectral embedding for non-linear dimensionality reduction.

[`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")

Distributed Stochastic Neighbor Embedding.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#id1)\
\]

Roweis, S. & Saul, L. Nonlinear dimensionality reduction by locally linear embedding. Science 290:2323 (2000).

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#id2)\
\]

Donoho, D. & Grimes, C. Hessian eigenmaps: Locally linear embedding techniques for high-dimensional data. Proc Natl Acad Sci U S A. 100:5591 (2003).

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#id3)\
\]

[Zhang, Z. & Wang, J. MLLE: Modified Locally Linear Embedding Using Multiple Weights.](https://citeseerx.ist.psu.edu/doc_view/pid/0b060fdbd92cbcc66b383bcaa9ba5e5e624d7ee3)

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#id4)\
\]

Zhang, Z. & Zha, H. Principal manifolds and nonlinear dimensionality reduction via tangent space alignment. Journal of Shanghai Univ. 8:406 (2004)

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.manifold import LocallyLinearEmbedding
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X.shape
(1797, 64)
\>>> embedding \= LocallyLinearEmbedding(n\_components\=2)
\>>> X\_transformed \= embedding.fit\_transform(X\[:100\])
\>>> X\_transformed.shape
(100, 2)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_locally_linear.py#L816)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.fit "Link to this definition")

Compute the embedding vectors for data X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training set.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Fitted `LocallyLinearEmbedding` class instance.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_locally_linear.py#L836)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.fit_transform "Link to this definition")

Compute the embedding vectors for data X and transform X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training set.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**X\_new**array-like, shape (n\_samples, n\_components)

Returns the instance itself.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_locally_linear.py#L856)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding.transform "Link to this definition")

Transform new points into embedding space.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training set.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_components)

Returns the instance itself.

Notes

Because of scaling performed by this method, it is discouraged to use it together with methods that are not scale-invariant (like SVMs).

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

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