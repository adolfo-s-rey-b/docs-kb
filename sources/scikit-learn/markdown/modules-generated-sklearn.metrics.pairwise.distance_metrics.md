[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.distance_metrics.html)

Collapse Sidebar Expand Sidebar

distance\_metrics[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#distance-metrics "Link to this heading")

===============================================================================================================================================================

sklearn.metrics.pairwise.distance\_metrics()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1934)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "Link to this definition")

Valid metrics for pairwise\_distances.

This function simply returns the valid pairwise distance metrics. It exists to allow for a description of the mapping for each of the valid strings.

The valid distance metrics, and the function they map to, are:

| metric | Function |
| --- | --- |
| ‘cityblock’ | metrics.pairwise.manhattan\_distances |
| ‘cosine’ | metrics.pairwise.cosine\_distances |
| ‘euclidean’ | metrics.pairwise.euclidean\_distances |
| ‘haversine’ | metrics.pairwise.haversine\_distances |
| ‘l1’ | metrics.pairwise.manhattan\_distances |
| ‘l2’ | metrics.pairwise.euclidean\_distances |
| ‘manhattan’ | metrics.pairwise.manhattan\_distances |
| ‘nan\_euclidean’ | metrics.pairwise.nan\_euclidean\_distances |

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Returns:

**distance\_metrics**dict

Returns valid metrics for pairwise\_distances.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)