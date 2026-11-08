[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_spd_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_spd_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_spd_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_spd_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_spd_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_spd_matrix.html)

Collapse Sidebar Expand Sidebar

make\_spd\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#make-spd-matrix "Link to this heading")

=====================================================================================================================================================

sklearn.datasets.make\_spd\_matrix(_n\_dim_, _\*_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1692)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#sklearn.datasets.make_spd_matrix "Link to this definition")

Generate a random symmetric, positive-definite matrix.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_dim**int

The matrix dimension.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_dim, n\_dim)

The random symmetric, positive-definite matrix.

See also

[`make_sparse_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")

Generate a sparse symmetric definite positive matrix.

Examples

\>>> from sklearn.datasets import make\_spd\_matrix
\>>> make\_spd\_matrix(n\_dim\=2, random\_state\=42)
array(\[\[2.093, 0.346\],\
       \[0.346, 0.218\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)