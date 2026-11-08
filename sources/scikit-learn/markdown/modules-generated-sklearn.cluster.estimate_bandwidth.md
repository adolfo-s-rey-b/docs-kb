[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.estimate_bandwidth.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.estimate_bandwidth.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.estimate_bandwidth.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.estimate_bandwidth.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.estimate_bandwidth.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.estimate_bandwidth.html)

Collapse Sidebar Expand Sidebar

estimate\_bandwidth[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#estimate-bandwidth "Link to this heading")

============================================================================================================================================================

sklearn.cluster.estimate\_bandwidth(_X_, _\*_, _quantile\=0.3_, _n\_samples\=None_, _random\_state\=0_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_mean_shift.py#L31)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#sklearn.cluster.estimate_bandwidth "Link to this definition")

Estimate the bandwidth to use with the mean-shift algorithm.

This function takes time at least quadratic in `n_samples`. For large datasets, it is wise to subsample by setting `n_samples`. Alternatively, the parameter `bandwidth` can be set to a small value without estimating it.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input points.

**quantile**float, default=0.3

Should be between \[0, 1\] 0.5 means that the median of all pairwise distances is used.

**n\_samples**int, default=None

The number of samples to use. If not given, all samples are used.

**random\_state**int, RandomState instance, default=0

The generator used to randomly select the samples from input points for bandwidth estimation. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Returns:

**bandwidth**float

The bandwidth parameter.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import estimate\_bandwidth
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> estimate\_bandwidth(X, quantile\=0.5)
np.float64(1.61)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_thumb.png)

[A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)

A demo of the mean-shift clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)