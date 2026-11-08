[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.mean_shift.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.mean_shift.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.mean_shift.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.mean_shift.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.mean_shift.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.mean_shift.html)

Collapse Sidebar Expand Sidebar

mean\_shift[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html#mean-shift "Link to this heading")

====================================================================================================================================

sklearn.cluster.mean\_shift(_X_, _\*_, _bandwidth\=None_, _seeds\=None_, _bin\_seeding\=False_, _min\_bin\_freq\=1_, _cluster\_all\=True_, _max\_iter\=300_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_mean_shift.py#L131)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html#sklearn.cluster.mean_shift "Link to this definition")

Perform mean shift clustering of data using a flat kernel.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#mean-shift)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

**bandwidth**float, default=None

Kernel bandwidth. If not None, must be in the range \[0, +inf).\
\
If None, the bandwidth is determined using a heuristic based on the median of all pairwise distances. This will take quadratic time in the number of samples. The sklearn.cluster.estimate\_bandwidth function can be used to do this more efficiently.\
\
**seeds**array-like of shape (n\_seeds, n\_features) or None\
\
Point used as initial kernel locations. If None and bin\_seeding=False, each data point is used as a seed. If None and bin\_seeding=True, see bin\_seeding.\
\
**bin\_seeding**bool, default=False\
\
If true, initial kernel locations are not locations of all points, but rather the location of the discretized version of points, where points are binned onto a grid whose coarseness corresponds to the bandwidth. Setting this option to True will speed up the algorithm because fewer seeds will be initialized. Ignored if seeds argument is not None.\
\
**min\_bin\_freq**int, default=1\
\
To speed up the algorithm, accept only those bins with at least min\_bin\_freq points as seeds.\
\
**cluster\_all**bool, default=True\
\
If true, then all points are clustered, even those orphans that are not within any kernel. Orphans are assigned to the nearest kernel. If false, then orphans are given cluster label -1.\
\
**max\_iter**int, default=300\
\
Maximum number of iterations, per seed point before the clustering operation terminates (for that seed point), if has not converged yet.\
\
**n\_jobs**int, default=None\
\
The number of jobs to use for the computation. The following tasks benefit from the parallelization:\
\
*   The search of nearest neighbors for bandwidth estimation and label assignments. See the details in the docstring of the `NearestNeighbors` class.\
    \
*   Hill-climbing optimization for all seeds.\
    \
\
See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)\
 for more details.\
\
`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")\
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)\
 for more details.\
\
Added in version 0.17: Parallel Execution using _n\_jobs_.\
\
Returns:\
\
**cluster\_centers**ndarray of shape (n\_clusters, n\_features)\
\
Coordinates of cluster centers.\
\
**labels**ndarray of shape (n\_samples,)\
\
Cluster labels for each point.\
\
Notes\
\
For a usage example, see [A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#sphx-glr-auto-examples-cluster-plot-mean-shift-py)\
.\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn.cluster import mean\_shift\
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])\
\>>> cluster\_centers, labels \= mean\_shift(X, bandwidth\=2)\
\>>> cluster\_centers\
array(\[\[3.33, 6.     \],\
       \[1.33, 0.66\]\])\
\>>> labels\
array(\[1, 1, 1, 0, 0, 0\])\
\
Copy to clipboard\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)