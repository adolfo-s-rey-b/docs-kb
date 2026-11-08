[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.locally_linear_embedding.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.locally_linear_embedding.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.locally_linear_embedding.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.locally_linear_embedding.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.locally_linear_embedding.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.locally_linear_embedding.html)

Collapse Sidebar Expand Sidebar

locally\_linear\_embedding[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#locally-linear-embedding "Link to this heading")

================================================================================================================================================================================

sklearn.manifold.locally\_linear\_embedding(_X_, _\*_, _n\_neighbors_, _n\_components_, _reg\=0.001_, _eigen\_solver\='auto'_, _tol\=1e-06_, _max\_iter\=100_, _method\='standard'_, _hessian\_tol\=0.0001_, _modified\_tol\=1e-12_, _random\_state\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_locally_linear.py#L454)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#sklearn.manifold.locally_linear_embedding "Link to this definition")

Perform a Locally Linear Embedding analysis on the data.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#locally-linear-embedding)
.

Parameters:

**X**{array-like, NearestNeighbors}

Sample data, shape = (n\_samples, n\_features), in the form of a numpy array or a NearestNeighbors object.

**n\_neighbors**int

Number of neighbors to consider for each point.

**n\_components**int

Number of coordinates for the manifold.

**reg**float, default=1e-3

Regularization constant, multiplies the trace of the local covariance matrix of the distances.

**eigen\_solver**{‘auto’, ‘arpack’, ‘dense’}, default=’auto’

auto : algorithm will attempt to choose the best method for input data

arpackuse arnoldi iteration in shift-invert mode.

For this method, M may be a dense matrix, sparse matrix, or general linear operator. Warning: ARPACK can be unstable for some problems. It is best to try several random seeds in order to check results.

denseuse standard dense matrix operations for the eigenvalue

decomposition. For this method, M must be an array or matrix type. This method should be avoided for large problems.

**tol**float, default=1e-6

Tolerance for ‘arpack’ method Not used if eigen\_solver==’dense’.

**max\_iter**int, default=100

Maximum number of iterations for the arpack solver.

**method**{‘standard’, ‘hessian’, ‘modified’, ‘ltsa’}, default=’standard’

standarduse the standard locally linear embedding algorithm.

see reference [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#rb2a5641379f7-1)

hessianuse the Hessian eigenmap method. This method requires

n\_neighbors > n\_components \* (1 + (n\_components + 1) / 2. see reference [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#rb2a5641379f7-2)

modifieduse the modified locally linear embedding algorithm.

see reference [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#rb2a5641379f7-3)

ltsause local tangent space alignment algorithm

see reference [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#rb2a5641379f7-4)

**hessian\_tol**float, default=1e-4

Tolerance for Hessian eigenmapping method. Only used if method == ‘hessian’.

**modified\_tol**float, default=1e-12

Tolerance for modified LLE method. Only used if method == ‘modified’.

**random\_state**int, RandomState instance, default=None

Determines the random number generator when `solver` == ‘arpack’. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int or None, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Returns:

**Y**ndarray of shape (n\_samples, n\_components)

Embedding vectors.

**squared\_error**float

Reconstruction error for the embedding vectors. Equivalent to `norm(Y - W Y, 'fro')**2`, where W are the reconstruction weights.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#id1)\
\]

Roweis, S. & Saul, L. Nonlinear dimensionality reduction by locally linear embedding. Science 290:2323 (2000).

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#id2)\
\]

Donoho, D. & Grimes, C. Hessian eigenmaps: Locally linear embedding techniques for high-dimensional data. Proc Natl Acad Sci U S A. 100:5591 (2003).

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#id3)\
\]

[Zhang, Z. & Wang, J. MLLE: Modified Locally Linear Embedding Using Multiple Weights.](https://citeseerx.ist.psu.edu/doc_view/pid/0b060fdbd92cbcc66b383bcaa9ba5e5e624d7ee3)

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#id4)\
\]

Zhang, Z. & Zha, H. Principal manifolds and nonlinear dimensionality reduction via tangent space alignment. Journal of Shanghai Univ. 8:406 (2004)

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.manifold import locally\_linear\_embedding
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X.shape
(1797, 64)
\>>> embedding, \_ \= locally\_linear\_embedding(X\[:100\],n\_neighbors\=5, n\_components\=2)
\>>> embedding.shape
(100, 2)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_thumb.png)

[Swiss Roll And Swiss-Hole Reduction](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html)

Swiss Roll And Swiss-Hole Reduction

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)