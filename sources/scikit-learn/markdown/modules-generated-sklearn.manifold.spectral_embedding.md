[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.manifold.spectral_embedding.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.manifold.spectral_embedding.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.spectral_embedding.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.manifold.spectral_embedding.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.manifold.spectral_embedding.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.manifold.spectral_embedding.html)

Collapse Sidebar Expand Sidebar

spectral\_embedding[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#spectral-embedding "Link to this heading")

=============================================================================================================================================================

sklearn.manifold.spectral\_embedding(_adjacency_, _\*_, _n\_components\=8_, _eigen\_solver\=None_, _random\_state\=None_, _eigen\_tol\='auto'_, _norm\_laplacian\=True_, _drop\_first\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/manifold/_spectral_embedding.py#L150)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "Link to this definition")

Project the sample on the first eigenvectors of the graph Laplacian.

The adjacency matrix is used to compute a normalized graph Laplacian whose spectrum (especially the eigenvectors associated to the smallest eigenvalues) has an interpretation in terms of minimal number of cuts necessary to split the graph into comparably sized components.

This embedding can also ‘work’ even if the `adjacency` variable is not strictly the adjacency matrix of a graph but more generally an affinity or similarity matrix between samples (for instance the heat kernel of a euclidean distance matrix or a k-NN matrix).

However care must taken to always make the affinity matrix symmetric so that the eigenvector decomposition works as expected.

Note : Laplacian Eigenmaps is the actual algorithm implemented here.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#spectral-embedding)
.

Parameters:

**adjacency**{array-like, sparse graph} of shape (n\_samples, n\_samples)

The adjacency matrix of the graph to embed.

**n\_components**int, default=8

The dimension of the projection subspace.

**eigen\_solver**{‘arpack’, ‘lobpcg’, ‘amg’}, default=None

The eigenvalue decomposition strategy to use. AMG requires pyamg to be installed. It can be faster on very large, sparse problems, but may also lead to instabilities. If None, then `'arpack'` is used.

**random\_state**int, RandomState instance or None, default=None

A pseudo random number generator used for the initialization of the lobpcg eigen vectors decomposition when `eigen_solver == 'amg'`, and for the K-Means initialization. Use an int to make the results deterministic across calls (See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
).

Note

When using `eigen_solver == 'amg'`, it is necessary to also fix the global numpy seed with `np.random.seed(int)` to get deterministic results. See [pyamg/pyamg#139](https://github.com/pyamg/pyamg/issues/139)
 for further information.

**eigen\_tol**float, default=”auto”

Stopping criterion for eigendecomposition of the Laplacian matrix. If `eigen_tol="auto"` then the passed tolerance will depend on the `eigen_solver`:

*   If `eigen_solver="arpack"`, then `eigen_tol=0.0`;
    
*   If `eigen_solver="lobpcg"` or `eigen_solver="amg"`, then `eigen_tol=None` which configures the underlying `lobpcg` solver to automatically resolve the value according to their heuristics. See, [`scipy.sparse.linalg.lobpcg`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lobpcg.html#scipy.sparse.linalg.lobpcg "(in SciPy v1.18.0)")
     for details.
    

Note that when using `eigen_solver="amg"` values of `tol<1e-5` may lead to convergence issues and should be avoided.

Added in version 1.2: Added ‘auto’ option.

**norm\_laplacian**bool, default=True

If True, then compute symmetric normalized Laplacian.

**drop\_first**bool, default=True

Whether to drop the first eigenvector. For spectral embedding, this should be True as the first eigenvector should be constant vector for connected graph, but for spectral clustering, this should be kept as False to retain the first eigenvector.

Returns:

**embedding**ndarray of shape (n\_samples, n\_components)

The reduced samples.

Notes

Spectral Embedding (Laplacian Eigenmaps) is most useful when the graph has one connected component. If there graph has many components, the first few eigenvectors will simply uncover the connected components of the graph.

References

*   [https://en.wikipedia.org/wiki/LOBPCG](https://en.wikipedia.org/wiki/LOBPCG)
    
*   [“Toward the Optimal Preconditioned Eigensolver: Locally Optimal Block Preconditioned Conjugate Gradient Method”, Andrew V. Knyazev](https://doi.org/10.1137/S1064827500366124)
    

Examples

\>>> from sklearn.datasets import load\_digits
\>>> from sklearn.neighbors import kneighbors\_graph
\>>> from sklearn.manifold import spectral\_embedding
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> X \= X\[:100\]
\>>> affinity\_matrix \= kneighbors\_graph(
...     X, n\_neighbors\=int(X.shape\[0\] / 10), include\_self\=True
... )
\>>> \# make the matrix symmetric
\>>> affinity\_matrix \= 0.5 \* (affinity\_matrix + affinity\_matrix.T)
\>>> embedding \= spectral\_embedding(affinity\_matrix, n\_components\=2, random\_state\=42)
\>>> embedding.shape
(100, 2)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)