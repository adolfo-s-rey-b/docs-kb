[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_hastie_10_2.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_hastie_10_2.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_hastie_10_2.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_hastie_10_2.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_hastie_10_2.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_hastie_10_2.html)

Collapse Sidebar Expand Sidebar

make\_hastie\_10\_2[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#make-hastie-10-2 "Link to this heading")

=========================================================================================================================================================

sklearn.datasets.make\_hastie\_10\_2(_n\_samples\=12000_, _\*_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L574)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "Link to this definition")

Generate data for binary classification used in Hastie et al. 2009, Example 10.2.

The ten features are standard independent Gaussian and the target `y` is defined by:

y\[i\] \= 1 if np.sum(X\[i\] \*\* 2) \> 9.34 else \-1

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=12000

The number of samples.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, 10)

The input samples.

**y**ndarray of shape (n\_samples,)

The output values.

See also

[`make_gaussian_quantiles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")

A generalization of this dataset approach.

References

\[1\]

T. Hastie, R. Tibshirani and J. Friedman, “Elements of Statistical Learning Ed. 2”, Springer, 2009.

Examples

\>>> from sklearn.datasets import make\_hastie\_10\_2
\>>> X, y \= make\_hastie\_10\_2(n\_samples\=24000, random\_state\=42)
\>>> X.shape
(24000, 10)
\>>> y.shape
(24000,)
\>>> list(y\[:5\])
\[np.float64(-1.0), np.float64(1.0), np.float64(-1.0), np.float64(1.0),\
np.float64(-1.0)\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)

[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Gradient Boosting regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_metric_evaluation_thumb.png)

[Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html)

Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)