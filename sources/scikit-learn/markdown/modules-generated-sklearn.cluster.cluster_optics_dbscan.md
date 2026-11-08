[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.cluster_optics_dbscan.html)

Collapse Sidebar Expand Sidebar

cluster\_optics\_dbscan[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#cluster-optics-dbscan "Link to this heading")

======================================================================================================================================================================

sklearn.cluster.cluster\_optics\_dbscan(_\*_, _reachability_, _core\_distances_, _ordering_, _eps_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_optics.py#L720)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#sklearn.cluster.cluster_optics_dbscan "Link to this definition")

Perform DBSCAN extraction for an arbitrary epsilon.

Extracting the clusters runs in linear time. Note that this results in `labels_` which are close to a [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
 with similar settings and `eps`, only if `eps` is close to `max_eps`.

Parameters:

**reachability**ndarray of shape (n\_samples,)

Reachability distances calculated by OPTICS (`reachability_`).

**core\_distances**ndarray of shape (n\_samples,)

Distances at which points become core (`core_distances_`).

**ordering**ndarray of shape (n\_samples,)

OPTICS ordered point indices (`ordering_`).

**eps**float

DBSCAN `eps` parameter. Must be set to < `max_eps`. Results will be close to DBSCAN algorithm if `eps` and `max_eps` are close to one another.

Returns:

**labels\_**array of shape (n\_samples,)

The estimated labels.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import cluster\_optics\_dbscan, compute\_optics\_graph
\>>> X \= np.array(\[\[1, 2\], \[2, 5\], \[3, 6\],\
...               \[8, 7\], \[8, 8\], \[7, 3\]\])
\>>> ordering, core\_distances, reachability, predecessor \= compute\_optics\_graph(
...     X,
...     min\_samples\=2,
...     max\_eps\=np.inf,
...     metric\="minkowski",
...     p\=2,
...     metric\_params\=None,
...     algorithm\="auto",
...     leaf\_size\=30,
...     n\_jobs\=None,
... )
\>>> eps \= 4.5
\>>> labels \= cluster\_optics\_dbscan(
...     reachability\=reachability,
...     core\_distances\=core\_distances,
...     ordering\=ordering,
...     eps\=eps,
... )
\>>> labels
array(\[0, 0, 0, 1, 1, 1\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_optics_thumb.png)

[Demo of OPTICS clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html)

Demo of OPTICS clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)