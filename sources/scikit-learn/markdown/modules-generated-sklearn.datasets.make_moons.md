[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_moons.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_moons.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_moons.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_moons.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_moons.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_moons.html)

Collapse Sidebar Expand Sidebar

make\_moons[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#make-moons "Link to this heading")

=====================================================================================================================================

sklearn.datasets.make\_moons(_n\_samples\=100_, _\*_, _shuffle\=True_, _noise\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L902)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "Link to this definition")

Make two interleaving half circles.

A simple toy dataset to visualize clustering and classification algorithms. Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int or tuple of shape (2,), dtype=int, default=100

If int, the total number of points generated. If two-element tuple, number of points in each of two moons.

Changed in version 0.23: Added two-element tuple.

**shuffle**bool, default=True

Whether to shuffle the samples.

**noise**float, default=None

Standard deviation of Gaussian noise added to the data.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset shuffling and noise. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, 2)

The generated samples.

**y**ndarray of shape (n\_samples,)

The integer labels (0 or 1) for class membership of each sample.

Examples

\>>> from sklearn.datasets import make\_moons
\>>> X, y \= make\_moons(n\_samples\=200, noise\=0.2, random\_state\=42)
\>>> X.shape
(200, 2)
\>>> y.shape
(200,)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)

[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Classifier comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_thumb.png)

[Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html)

Statistical comparison of models using grid search

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_thumb.png)

[Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)

Compare Stochastic learning strategies for MLPClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)