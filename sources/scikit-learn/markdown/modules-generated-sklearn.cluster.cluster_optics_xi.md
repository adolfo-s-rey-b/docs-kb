[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.cluster_optics_xi.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.cluster_optics_xi.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.cluster_optics_xi.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.cluster_optics_xi.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.cluster_optics_xi.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.cluster_optics_xi.html)

Collapse Sidebar Expand Sidebar

cluster\_optics\_xi[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html#cluster-optics-xi "Link to this heading")

==========================================================================================================================================================

sklearn.cluster.cluster\_optics\_xi(_\*_, _reachability_, _predecessor_, _ordering_, _min\_samples_, _min\_cluster\_size\=None_, _xi\=0.05_, _predecessor\_correction\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_optics.py#L794)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html#sklearn.cluster.cluster_optics_xi "Link to this definition")

Automatically extract clusters according to the Xi-steep method.

Parameters:

**reachability**ndarray of shape (n\_samples,)

Reachability distances calculated by OPTICS (`reachability_`).

**predecessor**ndarray of shape (n\_samples,)

Predecessors calculated by OPTICS.

**ordering**ndarray of shape (n\_samples,)

OPTICS ordered point indices (`ordering_`).

**min\_samples**int > 1 or float between 0 and 1

The same as the min\_samples given to OPTICS. Up and down steep regions can’t have more then `min_samples` consecutive non-steep points. Expressed as an absolute number or a fraction of the number of samples (rounded to be at least 2).

**min\_cluster\_size**int > 1 or float between 0 and 1, default=None

Minimum number of samples in an OPTICS cluster, expressed as an absolute number or a fraction of the number of samples (rounded to be at least 2). If `None`, the value of `min_samples` is used instead.

**xi**float between 0 and 1, default=0.05

Determines the minimum steepness on the reachability plot that constitutes a cluster boundary. For example, an upwards point in the reachability plot is defined by the ratio from one point to its successor being at most 1-xi.

**predecessor\_correction**bool, default=True

Correct clusters based on the calculated predecessors.

Returns:

**labels**ndarray of shape (n\_samples,)

The labels assigned to samples. Points which are not included in any cluster are labeled as -1.

**clusters**ndarray of shape (n\_clusters, 2)

The list of clusters in the form of `[start, end]` in each row, with all indices inclusive. The clusters are ordered according to `(end, -start)` (ascending) so that larger clusters encompassing smaller clusters come after such nested smaller clusters. Since `labels` does not reflect the hierarchy, usually `len(clusters) > np.unique(labels)`.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import cluster\_optics\_xi, compute\_optics\_graph
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
...     n\_jobs\=None
... )
\>>> min\_samples \= 2
\>>> labels, clusters \= cluster\_optics\_xi(
...     reachability\=reachability,
...     predecessor\=predecessor,
...     ordering\=ordering,
...     min\_samples\=min\_samples,
... )
\>>> labels
array(\[0, 0, 0, 1, 1, 1\])
\>>> clusters
array(\[\[0, 2\],\
       \[3, 5\],\
       \[0, 5\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)