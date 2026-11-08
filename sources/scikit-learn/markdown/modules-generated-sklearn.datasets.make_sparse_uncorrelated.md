[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html)

Collapse Sidebar Expand Sidebar

make\_sparse\_uncorrelated[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html#make-sparse-uncorrelated "Link to this heading")

================================================================================================================================================================================

sklearn.datasets.make\_sparse\_uncorrelated(_n\_samples\=100_, _n\_features\=10_, _\*_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1624)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html#sklearn.datasets.make_sparse_uncorrelated "Link to this definition")

Generate a random regression problem with sparse uncorrelated design.

This dataset is described in Celeux et al \[1\]. as:

X ~ N(0, 1)
y(X) \= X\[:, 0\] + 2 \* X\[:, 1\] \- 2 \* X\[:, 2\] \- 1.5 \* X\[:, 3\]

Copy to clipboard

Only the first 4 features are informative. The remaining features are useless.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=100

The number of samples.

**n\_features**int, default=10

The number of features.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, n\_features)

The input samples.

**y**ndarray of shape (n\_samples,)

The output values.

References

\[1\]

G. Celeux, M. El Anbari, J.-M. Marin, C. P. Robert, “Regularization in regression: comparing Bayesian and frequentist methods in a poorly informative situation”, 2009.

Examples

\>>> from sklearn.datasets import make\_sparse\_uncorrelated
\>>> X, y \= make\_sparse\_uncorrelated(random\_state\=0)
\>>> X.shape
(100, 10)
\>>> y.shape
(100,)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)