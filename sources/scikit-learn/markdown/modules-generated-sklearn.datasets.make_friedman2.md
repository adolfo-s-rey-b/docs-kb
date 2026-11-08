[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_friedman2.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_friedman2.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_friedman2.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_friedman2.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_friedman2.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_friedman2.html)

Collapse Sidebar Expand Sidebar

make\_friedman2[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html#make-friedman2 "Link to this heading")

=================================================================================================================================================

sklearn.datasets.make\_friedman2(_n\_samples\=100_, _\*_, _noise\=0.0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1253)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html#sklearn.datasets.make_friedman2 "Link to this definition")

Generate the “Friedman #2” regression problem.

This dataset is described in Friedman \[1\] and Breiman \[2\].

Inputs `X` are 4 independent features uniformly distributed on the intervals:

0 <= X\[:, 0\] <= 100,
40 \* pi <= X\[:, 1\] <= 560 \* pi,
0 <= X\[:, 2\] <= 1,
1 <= X\[:, 3\] <= 11.

Copy to clipboard

The output `y` is created according to the formula:

y(X) \= (X\[:, 0\] \*\* 2 + (X\[:, 1\] \* X\[:, 2\]  \- 1 / (X\[:, 1\] \* X\[:, 3\])) \*\* 2) \*\* 0.5 + noise \* N(0, 1).

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=100

The number of samples.

**noise**float, default=0.0

The standard deviation of the gaussian noise applied to the output.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset noise. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, 4)

The input samples.

**y**ndarray of shape (n\_samples,)

The output values.

References

\[1\]

J. Friedman, “Multivariate adaptive regression splines”, The Annals of Statistics 19 (1), pages 1-67, 1991.

\[2\]

L. Breiman, “Bagging predictors”, Machine Learning 24, pages 123-140, 1996.

Examples

\>>> from sklearn.datasets import make\_friedman2
\>>> X, y \= make\_friedman2(random\_state\=42)
\>>> X.shape
(100, 4)
\>>> y.shape
(100,)
\>>> list(y\[:3\])
\[np.float64(1229.4), np.float64(27.0), np.float64(65.6)\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)