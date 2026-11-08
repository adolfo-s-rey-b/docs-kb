[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_swiss_roll.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_swiss_roll.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_swiss_roll.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_swiss_roll.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_swiss_roll.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_swiss_roll.html)

Collapse Sidebar Expand Sidebar

make\_swiss\_roll[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#make-swiss-roll "Link to this heading")

=====================================================================================================================================================

sklearn.datasets.make\_swiss\_roll(_n\_samples\=100_, _\*_, _noise\=0.0_, _random\_state\=None_, _hole\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1858)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "Link to this definition")

Generate a swiss roll dataset.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Adapted with permission from Stephen Marsland’s code [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#r780fa7921e77-1)
.

Parameters:

**n\_samples**int, default=100

The number of sample points on the Swiss Roll.

**noise**float, default=0.0

The standard deviation of the gaussian noise.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**hole**bool, default=False

If True generates the swiss roll with hole dataset.

Returns:

**X**ndarray of shape (n\_samples, 3)

The points.

**t**ndarray of shape (n\_samples,)

The univariate position of the sample according to the main dimension of the points in the manifold.

Notes

The algorithm is from Marsland [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#r780fa7921e77-1)
.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#id1)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#id2)
)

S. Marsland, “Machine Learning: An Algorithmic Perspective”, 2nd edition, Chapter 6, 2014. [https://homepages.ecs.vuw.ac.nz/~marslast/Code/Ch6/lle.py](https://homepages.ecs.vuw.ac.nz/~marslast/Code/Ch6/lle.py)

Examples

\>>> from sklearn.datasets import make\_swiss\_roll
\>>> X, t \= make\_swiss\_roll(noise\=0.05, random\_state\=0)
\>>> X.shape
(100, 3)
\>>> t.shape
(100,)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_thumb.png)

[Swiss Roll And Swiss-Hole Reduction](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html)

Swiss Roll And Swiss-Hole Reduction

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)