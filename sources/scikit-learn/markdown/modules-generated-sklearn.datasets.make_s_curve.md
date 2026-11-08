[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_s_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_s_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_s_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_s_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_s_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_s_curve.html)

Collapse Sidebar Expand Sidebar

make\_s\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#make-s-curve "Link to this heading")

============================================================================================================================================

sklearn.datasets.make\_s\_curve(_n\_samples\=100_, _\*_, _noise\=0.0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1943)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "Link to this definition")

Generate an S curve dataset.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=100

The number of sample points on the S curve.

**noise**float, default=0.0

The standard deviation of the gaussian noise.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, 3)

The points.

**t**ndarray of shape (n\_samples,)

The univariate position of the sample according to the main dimension of the points in the manifold.

Examples

\>>> from sklearn.datasets import make\_s\_curve
\>>> X, t \= make\_s\_curve(noise\=0.05, random\_state\=0)
\>>> X.shape
(100, 3)
\>>> t.shape
(100,)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_t_sne_perplexity_thumb.png)

[t-SNE: The effect of various perplexity values on the shape](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html)

t-SNE: The effect of various perplexity values on the shape

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)

[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)

Release Highlights for scikit-learn 1.8

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)