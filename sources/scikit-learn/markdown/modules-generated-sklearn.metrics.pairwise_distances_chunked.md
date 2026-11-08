[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise_distances_chunked.html)

Collapse Sidebar Expand Sidebar

pairwise\_distances\_chunked[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#pairwise-distances-chunked "Link to this heading")

=====================================================================================================================================================================================

sklearn.metrics.pairwise\_distances\_chunked(_X_, _Y\=None_, _\*_, _reduce\_func\=None_, _metric\='euclidean'_, _n\_jobs\=None_, _working\_memory\=None_, _\*\*kwds_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L2115)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "Link to this definition")

Generate a distance matrix chunk by chunk with optional reduction.

In cases where not all of a pairwise distance matrix needs to be stored at once, this is used to calculate pairwise distances in `working_memory`\-sized chunks. If `reduce_func` is given, it is run on each chunk and its return values are concatenated into lists, arrays or sparse matrices.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_samples\_X) or (n\_samples\_X, n\_features)

Array of pairwise distances between samples, or a feature array. The shape the array should be (n\_samples\_X, n\_samples\_X) if metric=’precomputed’ and (n\_samples\_X, n\_features) otherwise.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. Only allowed if metric != “precomputed”.

**reduce\_func**callable, default=None

The function which is applied on each chunk of the distance matrix, reducing it to needed values. `reduce_func(D_chunk, start)` is called repeatedly, where `D_chunk` is a contiguous vertical slice of the pairwise distance matrix, starting at row `start`. It should return one of: None; an array, a list, or a sparse matrix of length `D_chunk.shape[0]`; or a tuple of such objects. Returning None is useful for in-place operations, rather than reductions.

If None, pairwise\_distances\_chunked returns a generator of vertical chunks of the distance matrix.

**metric**str or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options allowed by [`scipy.spatial.distance.pdist`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist "(in SciPy v1.18.0)")
 for its metric parameter, or a metric listed in pairwise.PAIRWISE\_DISTANCE\_FUNCTIONS. If metric is “precomputed”, X is assumed to be a distance matrix. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays from X as input and return a value indicating the distance between them.

**n\_jobs**int, default=None

The number of jobs to use for the computation. This works by breaking down the pairwise matrix into n\_jobs even slices and computing them in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**working\_memory**float, default=None

The sought maximum memory for temporary distance matrix chunks. When None (default), the value of `sklearn.get_config()['working_memory']` is used.

**\*\*kwds**optional keyword parameters

Any further parameters are passed directly to the distance function. If using a [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 metric, the parameters are still metric dependent. See the scipy docs for usage examples.

Yields:

**D\_chunk**{ndarray, sparse matrix}

A contiguous slice of distance matrix, optionally processed by `reduce_func`.

Examples

Without reduce\_func:

\>>> import numpy as np
\>>> from sklearn.metrics import pairwise\_distances\_chunked
\>>> X \= np.random.RandomState(0).rand(5, 3)
\>>> D\_chunk \= next(pairwise\_distances\_chunked(X))
\>>> D\_chunk
array(\[\[0.   , 0.295, 0.417, 0.197, 0.572\],\
       \[0.295, 0.   , 0.576, 0.419, 0.764\],\
       \[0.417, 0.576, 0.   , 0.449, 0.903\],\
       \[0.197, 0.419, 0.449, 0.   , 0.512\],\
       \[0.572, 0.764, 0.903, 0.512, 0.   \]\])

Copy to clipboard

Retrieve all neighbors and average distance within radius r:

\>>> r \= .2
\>>> def reduce\_func(D\_chunk, start):
...     neigh \= \[np.flatnonzero(d < r) for d in D\_chunk\]
...     avg\_dist \= (D\_chunk \* (D\_chunk < r)).mean(axis\=1)
...     return neigh, avg\_dist
\>>> gen \= pairwise\_distances\_chunked(X, reduce\_func\=reduce\_func)
\>>> neigh, avg\_dist \= next(gen)
\>>> neigh
\[array(\[0, 3\]), array(\[1\]), array(\[2\]), array(\[0, 3\]), array(\[4\])\]
\>>> avg\_dist
array(\[0.039, 0.        , 0.        , 0.039, 0.        \])

Copy to clipboard

Where r is defined per sample, we need to make use of `start`:

\>>> r \= \[.2, .4, .4, .3, .1\]
\>>> def reduce\_func(D\_chunk, start):
...     neigh \= \[np.flatnonzero(d < r\[i\])\
...              for i, d in enumerate(D\_chunk, start)\]
...     return neigh
\>>> neigh \= next(pairwise\_distances\_chunked(X, reduce\_func\=reduce\_func))
\>>> neigh
\[array(\[0, 3\]), array(\[0, 1\]), array(\[2\]), array(\[0, 3\]), array(\[4\])\]

Copy to clipboard

Force row-by-row generation by reducing `working_memory`:

\>>> gen \= pairwise\_distances\_chunked(X, reduce\_func\=reduce\_func,
...                                  working\_memory\=0)
\>>> next(gen)
\[array(\[0, 3\])\]
\>>> next(gen)
\[array(\[0, 1\])\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)