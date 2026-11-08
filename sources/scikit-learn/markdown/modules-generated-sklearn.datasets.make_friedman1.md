[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_friedman1.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_friedman1.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_friedman1.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_friedman1.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_friedman1.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_friedman1.html)

Collapse Sidebar Expand Sidebar

make\_friedman1[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html#make-friedman1 "Link to this heading")

=================================================================================================================================================

sklearn.datasets.make\_friedman1(_n\_samples\=100_, _n\_features\=10_, _\*_, _noise\=0.0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1169)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html#sklearn.datasets.make_friedman1 "Link to this definition")

Generate the “Friedman #1” regression problem.

This dataset is described in Friedman \[1\] and Breiman \[2\].

Inputs `X` are independent features uniformly distributed on the interval \[0, 1\]. The output `y` is created according to the formula:

y(X) \= 10 \* sin(pi \* X\[:, 0\] \* X\[:, 1\]) + 20 \* (X\[:, 2\] \- 0.5) \*\* 2 + 10 \* X\[:, 3\] + 5 \* X\[:, 4\] + noise \* N(0, 1).

Copy to clipboard

Out of the `n_features` features, only 5 are actually used to compute `y`. The remaining features are independent of `y`.

The number of features has to be >= 5.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=100

The number of samples.

**n\_features**int, default=10

The number of features. Should be at least 5.

**noise**float, default=0.0

The standard deviation of the gaussian noise applied to the output.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset noise. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, n\_features)

The input samples.

**y**ndarray of shape (n\_samples,)

The output values.

References

\[1\]

J. Friedman, “Multivariate adaptive regression splines”, The Annals of Statistics 19 (1), pages 1-67, 1991.

\[2\]

L. Breiman, “Bagging predictors”, Machine Learning 24, pages 123-140, 1996.

Examples

\>>> from sklearn.datasets import make\_friedman1
\>>> X, y \= make\_friedman1(random\_state\=42)
\>>> X.shape
(100, 10)
\>>> y.shape
(100,)
\>>> list(y\[:3\])
\[np.float64(16.8), np.float64(5.87), np.float64(9.46)\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)