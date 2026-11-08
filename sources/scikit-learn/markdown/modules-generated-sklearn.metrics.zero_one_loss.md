[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.zero_one_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.zero_one_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.zero_one_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.zero_one_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.zero_one_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.zero_one_loss.html)

Collapse Sidebar Expand Sidebar

zero\_one\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#zero-one-loss "Link to this heading")

==============================================================================================================================================

sklearn.metrics.zero\_one\_loss(_y\_true_, _y\_pred_, _\*_, _normalize\=True_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L1343)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "Link to this definition")

Zero-one classification loss.

If normalize is `True`, returns the fraction of misclassifications, else returns the number of misclassifications. The best performance is 0.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#zero-one-loss)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) labels. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Predicted labels, as returned by a classifier. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**normalize**bool, default=True

If `False`, return the number of misclassifications. Otherwise, return the fraction of misclassifications.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**loss**float

If `normalize == True`, returns the fraction of misclassifications, else returns the number of misclassifications.

See also

[`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")

Compute the accuracy score. By default, the function will return the fraction of correct predictions divided by the total number of predictions.

[`hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")

Compute the average Hamming loss or Hamming distance between two sets of samples.

[`jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")

Compute the Jaccard similarity coefficient score.

Notes

In multilabel classification, the zero\_one\_loss function corresponds to the subset zero-one loss: for each sample, the entire set of labels must be correctly predicted, otherwise the loss for that sample is equal to one.

Examples

\>>> from sklearn.metrics import zero\_one\_loss
\>>> y\_pred \= \[1, 2, 3, 4\]
\>>> y\_true \= \[2, 2, 3, 4\]
\>>> zero\_one\_loss(y\_true, y\_pred)
0.25
\>>> zero\_one\_loss(y\_true, y\_pred, normalize\=False)
1.0

Copy to clipboard

In the multilabel case with binary label indicators:

\>>> import numpy as np
\>>> zero\_one\_loss(np.array(\[\[0, 1\], \[1, 1\]\]), np.ones((2, 2)))
0.5

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)