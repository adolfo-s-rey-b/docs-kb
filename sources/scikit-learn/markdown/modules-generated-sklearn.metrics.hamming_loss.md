[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.hamming_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.hamming_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.hamming_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.hamming_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.hamming_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.hamming_loss.html)

Collapse Sidebar Expand Sidebar

hamming\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#hamming-loss "Link to this heading")

==========================================================================================================================================

sklearn.metrics.hamming\_loss(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L3195)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "Link to this definition")

Compute the average Hamming loss.

The Hamming loss is the fraction of labels that are incorrectly predicted.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#hamming-loss)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) labels. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Predicted labels, as returned by a classifier. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Added in version 0.18.

Returns:

**loss**float

Returns the average Hamming loss between element of `y_true` and `y_pred`.

See also

[`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")

Compute the accuracy score. By default, the function will return the fraction of correct predictions divided by the total number of predictions.

[`jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")

Compute the Jaccard similarity coefficient score.

[`zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")

Compute the Zero-one classification loss. By default, the function will return the percentage of imperfectly predicted subsets.

Notes

In multiclass classification, the Hamming loss corresponds to the Hamming distance between `y_true` and `y_pred` which is equivalent to the subset `zero_one_loss` function, when `normalize` parameter is set to True.

In multilabel classification, the Hamming loss is different from the subset zero-one loss. The zero-one loss considers the entire set of labels for a given sample incorrect if it does not entirely match the true set of labels. Hamming loss is more forgiving in that it penalizes only the individual labels.

The Hamming loss is upperbounded by the subset zero-one loss, when `normalize` parameter is set to True. It is always between 0 and 1, lower being better.

References

\[1\]

Grigorios Tsoumakas, Ioannis Katakis. [Multi-Label Classification: An Overview](https://people.iee.ihu.gr/~stoug/odep/papers/Multi-Label%20Classification:%20An%20Overview.pdf)
. International Journal of Data Warehousing & Mining, 3(3), 1-13, July-September 2007.

\[2\]

[Wikipedia entry on the Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
.

Examples

\>>> from sklearn.metrics import hamming\_loss
\>>> y\_pred \= \[1, 2, 3, 4\]
\>>> y\_true \= \[2, 2, 3, 4\]
\>>> hamming\_loss(y\_true, y\_pred)
0.25

Copy to clipboard

In the multilabel case with binary label indicators:

\>>> import numpy as np
\>>> hamming\_loss(np.array(\[\[0, 1\], \[1, 1\]\]), np.zeros((2, 2)))
0.75

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)