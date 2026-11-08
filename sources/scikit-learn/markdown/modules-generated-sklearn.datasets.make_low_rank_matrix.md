[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_low_rank_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_low_rank_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_low_rank_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_low_rank_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_low_rank_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_low_rank_matrix.html)

Collapse Sidebar Expand Sidebar

make\_low\_rank\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#make-low-rank-matrix "Link to this heading")

=====================================================================================================================================================================

sklearn.datasets.make\_low\_rank\_matrix(_n\_samples\=100_, _n\_features\=100_, _\*_, _effective\_rank\=10_, _tail\_strength\=0.5_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1421)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "Link to this definition")

Generate a mostly low rank matrix with bell-shaped singular values.

Most of the variance can be explained by a bell-shaped curve of width effective\_rank: the low rank part of the singular values profile is:

(1 \- tail\_strength) \* exp(\-1.0 \* (i / effective\_rank) \*\* 2)

Copy to clipboard

The remaining singular values’ tail is fat, decreasing as:

tail\_strength \* exp(\-0.1 \* i / effective\_rank).

Copy to clipboard

The low rank part of the profile can be considered the structured signal part of the data while the tail can be considered the noisy part of the data that cannot be summarized by a low number of linear components (singular vectors).

This kind of singular profiles is often seen in practice, for instance:

*   gray level pictures of faces
    
*   TF-IDF vectors of text documents crawled from the web
    

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=100

The number of samples.

**n\_features**int, default=100

The number of features.

**effective\_rank**int, default=10

The approximate number of singular vectors required to explain most of the data by linear combinations.

**tail\_strength**float, default=0.5

The relative importance of the fat noisy tail of the singular values profile. The value should be between 0 and 1.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, n\_features)

The matrix.

Examples

\>>> from numpy.linalg import svd
\>>> from sklearn.datasets import make\_low\_rank\_matrix
\>>> X \= make\_low\_rank\_matrix(
...     n\_samples\=50,
...     n\_features\=25,
...     effective\_rank\=5,
...     tail\_strength\=0.01,
...     random\_state\=0,
... )
\>>> X.shape
(50, 25)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)