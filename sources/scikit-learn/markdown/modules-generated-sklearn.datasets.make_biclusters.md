[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_biclusters.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_biclusters.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_biclusters.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_biclusters.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_biclusters.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_biclusters.html)

Collapse Sidebar Expand Sidebar

make\_biclusters[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#make-biclusters "Link to this heading")

====================================================================================================================================================

sklearn.datasets.make\_biclusters(_shape_, _n\_clusters_, _\*_, _noise\=0.0_, _minval\=10_, _maxval\=100_, _shuffle\=True_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L2129)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "Link to this definition")

Generate a constant block diagonal structure array for biclustering.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**shape**tuple of shape (n\_rows, n\_cols)

The shape of the result.

**n\_clusters**int

The number of biclusters.

**noise**float, default=0.0

The standard deviation of the gaussian noise.

**minval**float, default=10

Minimum value of a bicluster.

**maxval**float, default=100

Maximum value of a bicluster.

**shuffle**bool, default=True

Shuffle the samples.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape `shape`

The generated array.

**rows**ndarray of shape (n\_clusters, X.shape\[0\])

The indicators for cluster membership of each row.

**cols**ndarray of shape (n\_clusters, X.shape\[1\])

The indicators for cluster membership of each column.

See also

[`make_checkerboard`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")

Generate an array with block checkerboard structure for biclustering.

References

\[1\]

Dhillon, I. S. (2001, August). Co-clustering documents and words using bipartite spectral graph partitioning. In Proceedings of the seventh ACM SIGKDD international conference on Knowledge discovery and data mining (pp. 269-274). ACM.

Examples

\>>> from sklearn.datasets import make\_biclusters
\>>> data, rows, cols \= make\_biclusters(
...     shape\=(10, 20), n\_clusters\=2, random\_state\=42
... )
\>>> data.shape
(10, 20)
\>>> rows.shape
(2, 10)
\>>> cols.shape
(2, 20)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_thumb.png)

[A demo of the Spectral Co-Clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html)

A demo of the Spectral Co-Clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)