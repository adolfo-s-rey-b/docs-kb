[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_checkerboard.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_checkerboard.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_checkerboard.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_checkerboard.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_checkerboard.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_checkerboard.html)

Collapse Sidebar Expand Sidebar

make\_checkerboard[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#make-checkerboard "Link to this heading")

==========================================================================================================================================================

sklearn.datasets.make\_checkerboard(_shape_, _n\_clusters_, _\*_, _noise\=0.0_, _minval\=10_, _maxval\=100_, _shuffle\=True_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L2251)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "Link to this definition")

Generate an array with block checkerboard structure for biclustering.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**shape**tuple of shape (n\_rows, n\_cols)

The shape of the result.

**n\_clusters**int or array-like or shape (n\_row\_clusters, n\_column\_clusters)

The number of row and column clusters.

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

[`make_biclusters`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters")

Generate an array with constant block diagonal structure for biclustering.

References

\[1\]

Kluger, Y., Basri, R., Chang, J. T., & Gerstein, M. (2003). Spectral biclustering of microarray data: coclustering genes and conditions. Genome research, 13(4), 703-716.

Examples

\>>> from sklearn.datasets import make\_checkerboard
\>>> data, rows, columns \= make\_checkerboard(shape\=(300, 300), n\_clusters\=10,
...                                         random\_state\=42)
\>>> data.shape
(300, 300)
\>>> rows.shape
(100, 300)
\>>> columns.shape
(100, 300)
\>>> print(rows\[0\]\[:5\], columns\[0\]\[:5\])
\[False False False  True False\] \[False False False False False\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_thumb.png)

[A demo of the Spectral Biclustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html)

A demo of the Spectral Biclustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)