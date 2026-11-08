[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html)

Collapse Sidebar Expand Sidebar

pairwise\_kernels[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#pairwise-kernels "Link to this heading")

===============================================================================================================================================================

sklearn.metrics.pairwise.pairwise\_kernels(_X_, _Y\=None_, _metric\='linear'_, _\*_, _filter\_params\=False_, _n\_jobs\=None_, _\*\*kwds_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L2577)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "Link to this definition")

Compute the kernel between arrays X and optional array Y.

This function takes one or two feature arrays or a kernel matrix, and returns a kernel matrix.

*   If `X` is a feature array, of shape (n\_samples\_X, n\_features), and:
    
    *   `Y` is `None` and `metric` is not ‘precomputed’, the pairwise kernels between `X` and itself are returned.
        
    *   `Y` is a feature array of shape (n\_samples\_Y, n\_features), the pairwise kernels between `X` and `Y` is returned.
        
*   If `X` is a kernel matrix, of shape (n\_samples\_X, n\_samples\_X), `metric` should be ‘precomputed’. `Y` is thus ignored and `X` is returned as is.
    

This method provides a safe way to take a kernel matrix as input, while preserving compatibility with many other algorithms that take a vector array.

Valid values for metric are:

\[‘additive\_chi2’, ‘chi2’, ‘linear’, ‘poly’, ‘polynomial’, ‘rbf’, ‘laplacian’, ‘sigmoid’, ‘cosine’\]

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_samples\_X) or (n\_samples\_X, n\_features)

Array of pairwise kernels between samples, or a feature array. The shape of the array should be (n\_samples\_X, n\_samples\_X) if metric == “precomputed” and (n\_samples\_X, n\_features) otherwise.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

A second feature array only if X has shape (n\_samples\_X, n\_features).

**metric**str or callable, default=”linear”

The metric to use when calculating kernel between instances in a feature array. If metric is a string, it must be one of the metrics in `pairwise.PAIRWISE_KERNEL_FUNCTIONS`. If metric is “precomputed”, X is assumed to be a kernel matrix. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two rows from X as input and return the corresponding kernel value as a single number. This means that callables from [`sklearn.metrics.pairwise`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics.pairwise "sklearn.metrics.pairwise")
 are not allowed, as they operate on matrices, not single samples. Use the string identifying the kernel instead.

**filter\_params**bool, default=False

Whether to filter invalid parameters or not.

**n\_jobs**int, default=None

The number of jobs to use for the computation. This works by breaking down the pairwise matrix into n\_jobs even slices and computing them using multithreading.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**\*\*kwds**optional keyword parameters

Any further parameters are passed directly to the kernel function.

Returns:

**K**ndarray of shape (n\_samples\_X, n\_samples\_X) or (n\_samples\_X, n\_samples\_Y)

A kernel matrix K such that K\_{i, j} is the kernel between the ith and jth vectors of the given matrix X, if Y is None. If Y is not None, then K\_{i, j} is the kernel between the ith array from X and the jth array from Y.

Notes

If metric is a callable, no restrictions are placed on `X` and `Y` dimensions.

Examples

\>>> from sklearn.metrics.pairwise import pairwise\_kernels
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> pairwise\_kernels(X, Y, metric\='linear')
array(\[\[0., 0.\],\
       \[1., 2.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)