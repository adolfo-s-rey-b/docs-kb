[Skip to main content](https://scikit-learn.org/stable/api/sklearn.random_projection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

sklearn.random\_projection[#](https://scikit-learn.org/stable/api/sklearn.random_projection.html#module-sklearn.random_projection "Link to this heading")

==========================================================================================================================================================

Random projection transformers.

Random projections are a simple and computationally efficient way to reduce the dimensionality of the data by trading a controlled amount of accuracy (as additional variance) for faster processing times and smaller model sizes.

The dimensions and distribution of random projections matrices are controlled so as to preserve the pairwise distances between any two samples of the dataset.

The main theoretical result behind the efficiency of random projection is the [Johnson-Lindenstrauss lemma (quoting Wikipedia)](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma)
:

> In mathematics, the Johnson-Lindenstrauss lemma is a result concerning low-distortion embeddings of points from high-dimensional into low-dimensional Euclidean space. The lemma states that a small set of points in a high-dimensional space can be embedded into a space of much lower dimension in such a way that distances between the points are nearly preserved. The map used for the embedding is at least Lipschitz, and can even be taken to be an orthogonal projection.

**User guide.** See the [Random Projection](https://scikit-learn.org/stable/modules/random_projection.html#random-projection)
 section for further details.

|     |     |
| --- | --- |
| [`GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection") | Reduce dimensionality through Gaussian random projection. |
| [`SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection") | Reduce dimensionality through sparse random projection. |
| [`johnson_lindenstrauss_min_dim`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim") | Find a 'safe' number of components to randomly project to. |