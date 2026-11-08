[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html)

Collapse Sidebar Expand Sidebar

kernel\_metrics[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#kernel-metrics "Link to this heading")

=========================================================================================================================================================

sklearn.metrics.pairwise.kernel\_metrics()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L2532)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#sklearn.metrics.pairwise.kernel_metrics "Link to this definition")

Valid metrics for pairwise\_kernels.

This function simply returns the valid pairwise distance metrics. It exists, however, to allow for a verbose description of the mapping for each of the valid strings.

The valid distance metrics, and the function they map to, are:

| metric | Function |
| --- | --- |
| ‘additive\_chi2’ | sklearn.pairwise.additive\_chi2\_kernel |
| ‘chi2’ | sklearn.pairwise.chi2\_kernel |
| ‘linear’ | sklearn.pairwise.linear\_kernel |
| ‘poly’ | sklearn.pairwise.polynomial\_kernel |
| ‘polynomial’ | sklearn.pairwise.polynomial\_kernel |
| ‘rbf’ | sklearn.pairwise.rbf\_kernel |
| ‘laplacian’ | sklearn.pairwise.laplacian\_kernel |
| ‘sigmoid’ | sklearn.pairwise.sigmoid\_kernel |
| ‘cosine’ | sklearn.pairwise.cosine\_similarity |

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Returns:

**kernel\_metrics**dict

Returns valid metrics for pairwise\_kernels.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)