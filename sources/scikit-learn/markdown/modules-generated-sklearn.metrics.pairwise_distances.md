[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise_distances.html)

Collapse Sidebar Expand Sidebar

pairwise\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#pairwise-distances "Link to this heading")

============================================================================================================================================================

sklearn.metrics.pairwise\_distances(_X_, _Y\=None_, _metric\='euclidean'_, _\*_, _n\_jobs\=None_, _ensure\_all\_finite\=True_, _\*\*kwds_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L2299)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "Link to this definition")

Compute the distance matrix from a feature array X and optional Y.

This function takes one or two feature arrays or a distance matrix, and returns a distance matrix.

*   If `X` is a feature array, of shape (n\_samples\_X, n\_features), and:
    
    *   `Y` is `None` and `metric` is not ‘precomputed’, the pairwise distances between `X` and itself are returned.
        
    *   `Y` is a feature array of shape (n\_samples\_Y, n\_features), the pairwise distances between `X` and `Y` is returned.
        
*   If `X` is a distance matrix, of shape (n\_samples\_X, n\_samples\_X), `metric` should be ‘precomputed’. `Y` is thus ignored and `X` is returned as is.
    

If the input is a collection of non-numeric data (e.g. a list of strings or a boolean array), a custom metric must be passed.

This method provides a safe way to take a distance matrix as input, while preserving compatibility with many other algorithms that take a vector array.

Valid values for metric are:

*   From scikit-learn: \[‘cityblock’, ‘cosine’, ‘euclidean’, ‘l1’, ‘l2’, ‘manhattan’, ‘nan\_euclidean’\]. All metrics support sparse matrix inputs except ‘nan\_euclidean’.
    
*   From [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
    : \[‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘correlation’, ‘dice’, ‘hamming’, ‘jaccard’, ‘kulsinski’, ‘mahalanobis’, ‘minkowski’, ‘rogerstanimoto’, ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’\]. These metrics do not support sparse matrix inputs.
    

Note

`'kulsinski'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

Note

`'matching'` has been removed in SciPy 1.9 (use `'hamming'` instead).

Note that in the case of ‘cityblock’, ‘cosine’ and ‘euclidean’ (which are valid [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 metrics), the scikit-learn implementation will be used, which is faster and has support for sparse matrices (except for ‘cityblock’). For a verbose description of the metrics from scikit-learn, see [`sklearn.metrics.pairwise.distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 function.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_samples\_X) or (n\_samples\_X, n\_features)

Array of pairwise distances between samples, or a feature array. The shape of the array should be (n\_samples\_X, n\_samples\_X) if metric == “precomputed” and (n\_samples\_X, n\_features) otherwise.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. Only allowed if metric != “precomputed”.

**metric**str or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options allowed by [`scipy.spatial.distance.pdist`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist "(in SciPy v1.18.0)")
 for its metric parameter, or a metric listed in `pairwise.PAIRWISE_DISTANCE_FUNCTIONS`. If metric is “precomputed”, X is assumed to be a distance matrix. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays from X as input and return a value indicating the distance between them.

**n\_jobs**int, default=None

The number of jobs to use for the computation. This works by breaking down the pairwise matrix into n\_jobs even slices and computing them using multithreading.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

The “euclidean” and “cosine” metrics rely heavily on BLAS which is already multithreaded. So, increasing `n_jobs` would likely cause oversubscription and quickly degrade performance.

**ensure\_all\_finite**bool or ‘allow-nan’, default=True

Whether to raise an error on np.inf, np.nan, pd.NA in array. Ignored for a metric listed in `pairwise.PAIRWISE_DISTANCE_FUNCTIONS`. The possibilities are:

*   True: Force all values of array to be finite.
    
*   False: accepts np.inf, np.nan, pd.NA in array.
    
*   ‘allow-nan’: accepts only np.nan and pd.NA values in array. Values cannot be infinite.
    

Added in version 1.6: `force_all_finite` was renamed to `ensure_all_finite`.

**\*\*kwds**optional keyword parameters

Any further parameters are passed directly to the distance function. If using a scipy.spatial.distance metric, the parameters are still metric dependent. See the scipy docs for usage examples.

Returns:

**D**ndarray of shape (n\_samples\_X, n\_samples\_X) or (n\_samples\_X, n\_samples\_Y)

A distance matrix D such that D\_{i, j} is the distance between the ith and jth vectors of the given matrix X, if Y is None. If Y is not None, then D\_{i, j} is the distance between the ith array from X and the jth array from Y.

See also

[`pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked")

Performs the same calculation as this function, but returns a generator of chunks of the distance matrix, in order to limit memory usage.

[`sklearn.metrics.pairwise.paired_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "sklearn.metrics.pairwise.paired_distances")

Computes the distances between corresponding elements of two arrays.

Notes

If metric is a callable, no restrictions are placed on `X` and `Y` dimensions.

Examples

\>>> from sklearn.metrics.pairwise import pairwise\_distances
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> pairwise\_distances(X, Y, metric\='sqeuclidean')
array(\[\[1., 2.\],\
       \[2., 1.\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_thumb.png)

[Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Agglomerative clustering with different metrics

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)