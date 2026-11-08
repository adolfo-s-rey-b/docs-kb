[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_gaussian_quantiles.html)

Collapse Sidebar Expand Sidebar

make\_gaussian\_quantiles[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#make-gaussian-quantiles "Link to this heading")

=============================================================================================================================================================================

sklearn.datasets.make\_gaussian\_quantiles(_\*_, _mean\=None_, _cov\=1.0_, _n\_samples\=100_, _n\_features\=2_, _n\_classes\=3_, _shuffle\=True_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L2000)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "Link to this definition")

Generate isotropic Gaussian and label samples by quantile.

This classification dataset is constructed by taking a multi-dimensional standard normal distribution and defining classes separated by nested concentric multi-dimensional spheres such that roughly equal numbers of samples are in each class (quantiles of the χ2 distribution).

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**mean**array-like of shape (n\_features,), default=None

The mean of the multi-dimensional normal distribution. If None then use the origin (0, 0, …).

**cov**float, default=1.0

The covariance matrix will be this value times the unit matrix. This dataset only produces symmetric normal distributions.

**n\_samples**int, default=100

The total number of points equally divided among classes.

**n\_features**int, default=2

The number of features for each sample.

**n\_classes**int, default=3

The number of classes.

**shuffle**bool, default=True

Shuffle the samples.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, n\_features)

The generated samples.

**y**ndarray of shape (n\_samples,)

The integer labels for quantile membership of each sample.

Notes

The dataset is from Zhu et al [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#r71e05e3f0cb4-1)
.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#id1)\
\]

[J. Zhu, H. Zou, S. Rosset, T. Hastie, “Multi-class AdaBoost.” Statistics and its Interface 2.3 (2009): 349-360.](https://doi.org/10.4310/SII.2009.v2.n3.a8)

Examples

\>>> from sklearn.datasets import make\_gaussian\_quantiles
\>>> X, y \= make\_gaussian\_quantiles(random\_state\=42)
\>>> X.shape
(100, 2)
\>>> y.shape
(100,)
\>>> list(y\[:5\])
\[np.int64(2), np.int64(0), np.int64(1), np.int64(0), np.int64(2)\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_multiclass_thumb.png)

[Multi-class AdaBoosted Decision Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html)

Multi-class AdaBoosted Decision Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_thumb.png)

[Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)

Two-class AdaBoost

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)