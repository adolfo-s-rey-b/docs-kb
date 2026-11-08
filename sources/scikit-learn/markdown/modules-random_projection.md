[Skip to main content](https://scikit-learn.org/stable/modules/random_projection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/random_projection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/random_projection.html)
[1.8.0](https://scikit-learn.org/1.8/modules/random_projection.html)
[1.7.2](https://scikit-learn.org/1.7/modules/random_projection.html)
[1.6.1](https://scikit-learn.org/1.6/modules/random_projection.html)
[1.5.2](https://scikit-learn.org/1.5/modules/random_projection.html)
[1.4.2](https://scikit-learn.org/1.4/modules/random_projection.html)

Collapse Sidebar Expand Sidebar

8.6. Random Projection[#](https://scikit-learn.org/stable/modules/random_projection.html#random-projection "Link to this heading")

===================================================================================================================================

The [`sklearn.random_projection`](https://scikit-learn.org/stable/api/sklearn.random_projection.html#module-sklearn.random_projection "sklearn.random_projection")
 module implements a simple and computationally efficient way to reduce the dimensionality of the data by trading a controlled amount of accuracy (as additional variance) for faster processing times and smaller model sizes. This module implements two types of unstructured random matrix: [Gaussian random matrix](https://scikit-learn.org/stable/modules/random_projection.html#gaussian-random-matrix)
 and [sparse random matrix](https://scikit-learn.org/stable/modules/random_projection.html#sparse-random-matrix)
.

The dimensions and distribution of random projections matrices are controlled so as to preserve the pairwise distances between any two samples of the dataset. Thus random projection is a suitable approximation technique for distance based method.

References

*   Sanjoy Dasgupta. 2000. [Experiments with random projection.](https://cseweb.ucsd.edu/~dasgupta/papers/randomf.pdf)
     In Proceedings of the Sixteenth conference on Uncertainty in artificial intelligence (UAI’00), Craig Boutilier and Moisés Goldszmidt (Eds.). Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 143-151.
    
*   Ella Bingham and Heikki Mannila. 2001. [Random projection in dimensionality reduction: applications to image and text data.](https://cs-people.bu.edu/evimaria/cs565/kdd-rp.pdf)
     In Proceedings of the seventh ACM SIGKDD international conference on Knowledge discovery and data mining (KDD ‘01). ACM, New York, NY, USA, 245-250.
    

8.6.1. The Johnson-Lindenstrauss lemma[#](https://scikit-learn.org/stable/modules/random_projection.html#the-johnson-lindenstrauss-lemma "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The main theoretical result behind the efficiency of random projection is the [Johnson-Lindenstrauss lemma (quoting Wikipedia)](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma)
:

> In mathematics, the Johnson-Lindenstrauss lemma is a result concerning low-distortion embeddings of points from high-dimensional into low-dimensional Euclidean space. The lemma states that a small set of points in a high-dimensional space can be embedded into a space of much lower dimension in such a way that distances between the points are nearly preserved. The map used for the embedding is at least Lipschitz, and can even be taken to be an orthogonal projection.

Knowing only the number of samples, the [`johnson_lindenstrauss_min_dim`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim")
 estimates conservatively the minimal size of the random subspace to guarantee a bounded distortion introduced by the random projection:

\>>> from sklearn.random\_projection import johnson\_lindenstrauss\_min\_dim
\>>> johnson\_lindenstrauss\_min\_dim(n\_samples\=1e6, eps\=0.5)
np.int64(663)
\>>> johnson\_lindenstrauss\_min\_dim(n\_samples\=1e6, eps\=\[0.5, 0.1, 0.01\])
array(\[    663,   11841, 1112658\])
\>>> johnson\_lindenstrauss\_min\_dim(n\_samples\=\[1e4, 1e5, 1e6\], eps\=0.1)
array(\[ 7894,  9868, 11841\])

Copy to clipboard

[![../_images/sphx_glr_plot_johnson_lindenstrauss_bound_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_001.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

[![../_images/sphx_glr_plot_johnson_lindenstrauss_bound_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_002.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

Examples

*   See [The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#sphx-glr-auto-examples-miscellaneous-plot-johnson-lindenstrauss-bound-py)
     for a theoretical explication on the Johnson-Lindenstrauss lemma and an empirical validation using sparse random matrices.
    

References

*   Sanjoy Dasgupta and Anupam Gupta, 1999. [An elementary proof of the Johnson-Lindenstrauss Lemma.](https://cseweb.ucsd.edu/~dasgupta/papers/jl.pdf)
    

8.6.2. Gaussian random projection[#](https://scikit-learn.org/stable/modules/random_projection.html#gaussian-random-projection "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

The [`GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
 reduces the dimensionality by projecting the original input space on a randomly generated matrix where components are drawn from the following distribution N(0,1ncomponents).

Here is a small excerpt which illustrates how to use the Gaussian random projection transformer:

\>>> import numpy as np
\>>> from sklearn import random\_projection
\>>> X \= np.random.rand(100, 10000)
\>>> transformer \= random\_projection.GaussianRandomProjection()
\>>> X\_new \= transformer.fit\_transform(X)
\>>> X\_new.shape
(100, 3947)

Copy to clipboard

8.6.3. Sparse random projection[#](https://scikit-learn.org/stable/modules/random_projection.html#sparse-random-projection "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The [`SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
 reduces the dimensionality by projecting the original input space using a sparse random matrix.

Sparse random matrices are an alternative to dense Gaussian random projection matrix that guarantees similar embedding quality while being much more memory efficient and allowing faster computation of the projected data.

If we define `s = 1 / density`, the elements of the random matrix are drawn from

{−sncomponents1/2s0with probability1−1/s+sncomponents1/2s

where ncomponents is the size of the projected subspace. By default the density of non zero elements is set to the minimum density as recommended by Ping Li et al.: 1/nfeatures.

Here is a small excerpt which illustrates how to use the sparse random projection transformer:

\>>> import numpy as np
\>>> from sklearn import random\_projection
\>>> X \= np.random.rand(100, 10000)
\>>> transformer \= random\_projection.SparseRandomProjection()
\>>> X\_new \= transformer.fit\_transform(X)
\>>> X\_new.shape
(100, 3947)

Copy to clipboard

References

*   D. Achlioptas. 2003. [Database-friendly random projections: Johnson-Lindenstrauss with binary coins](https://www.sciencedirect.com/science/article/pii/S0022000003000254)
    . Journal of Computer and System Sciences 66 (2003) 671-687.
    
*   Ping Li, Trevor J. Hastie, and Kenneth W. Church. 2006. [Very sparse random projections.](https://web.stanford.edu/~hastie/Papers/Ping/KDD06_rp.pdf)
     In Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining (KDD ‘06). ACM, New York, NY, USA, 287-296.
    

8.6.4. Inverse Transform[#](https://scikit-learn.org/stable/modules/random_projection.html#inverse-transform "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

The random projection transformers have `compute_inverse_components` parameter. When set to True, after creating the random `components_` matrix during fitting, the transformer computes the pseudo-inverse of this matrix and stores it as `inverse_components_`. The `inverse_components_` matrix has shape nfeatures×ncomponents, and it is always a dense matrix, regardless of whether the components matrix is sparse or dense. So depending on the number of features and components, it may use a lot of memory.

When the `inverse_transform` method is called, it computes the product of the input `X` and the transpose of the inverse components. If the inverse components have been computed during fit, they are reused at each call to `inverse_transform`. Otherwise they are recomputed each time, which can be costly. The result is always dense, even if `X` is sparse.

Here is a small code example which illustrates how to use the inverse transform feature:

\>>> import numpy as np
\>>> from sklearn.random\_projection import SparseRandomProjection
\>>> X \= np.random.rand(100, 10000)
\>>> transformer \= SparseRandomProjection(
...   compute\_inverse\_components\=True
... )
...
\>>> X\_new \= transformer.fit\_transform(X)
\>>> X\_new.shape
(100, 3947)
\>>> X\_new\_inversed \= transformer.inverse\_transform(X\_new)
\>>> X\_new\_inversed.shape
(100, 10000)
\>>> X\_new\_again \= transformer.transform(X\_new\_inversed)
\>>> np.allclose(X\_new, X\_new\_again)
True

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)