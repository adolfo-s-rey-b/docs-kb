[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_sparse_coded_signal.html)

Collapse Sidebar Expand Sidebar

make\_sparse\_coded\_signal[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#make-sparse-coded-signal "Link to this heading")

=================================================================================================================================================================================

sklearn.datasets.make\_sparse\_coded\_signal(_n\_samples_, _\*_, _n\_components_, _n\_features_, _n\_nonzero\_coefs_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1527)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "Link to this definition")

Generate a signal as a sparse combination of dictionary elements.

Returns matrices `Y`, `D` and `X` such that `Y = XD` where `X` is of shape `(n_samples, n_components)`, `D` is of shape `(n_components, n_features)`, and each row of `X` has exactly `n_nonzero_coefs` non-zero elements.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int

Number of samples to generate.

**n\_components**int

Number of components in the dictionary.

**n\_features**int

Number of features of the dataset to generate.

**n\_nonzero\_coefs**int

Number of active (non-zero) coefficients in each sample.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**data**ndarray of shape (n\_samples, n\_features)

The encoded signal (Y).

**dictionary**ndarray of shape (n\_components, n\_features)

The dictionary with normalized components (D).

**code**ndarray of shape (n\_samples, n\_components)

The sparse code such that each column of this matrix has exactly n\_nonzero\_coefs non-zero items (X).

Examples

\>>> from sklearn.datasets import make\_sparse\_coded\_signal
\>>> data, dictionary, code \= make\_sparse\_coded\_signal(
...     n\_samples\=50,
...     n\_components\=100,
...     n\_features\=10,
...     n\_nonzero\_coefs\=4,
...     random\_state\=0
... )
\>>> data.shape
(50, 10)
\>>> dictionary.shape
(100, 10)
\>>> code.shape
(50, 100)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_omp_thumb.png)

[Orthogonal Matching Pursuit](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html)

Orthogonal Matching Pursuit

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)