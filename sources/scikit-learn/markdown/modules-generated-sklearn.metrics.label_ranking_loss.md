[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.label_ranking_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.label_ranking_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.label_ranking_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.label_ranking_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.label_ranking_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.label_ranking_loss.html)

Collapse Sidebar Expand Sidebar

label\_ranking\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html#label-ranking-loss "Link to this heading")

=============================================================================================================================================================

sklearn.metrics.label\_ranking\_loss(_y\_true_, _y\_score_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1553)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html#sklearn.metrics.label_ranking_loss "Link to this definition")

Compute Ranking loss measure.

Compute the average number of label pairs that are incorrectly ordered given y\_score weighted by the size of the label set and the number of labels not in the label set.

This is similar to the error set size, but weighted by the number of relevant and irrelevant labels. The best performance is achieved with a ranking loss of zero.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#label-ranking-loss)
.

Added in version 0.17: A function _label\_ranking\_loss_

Parameters:

**y\_true**{array-like, sparse matrix} of shape (n\_samples, n\_labels)

True binary labels in [label indicator format](https://scikit-learn.org/stable/glossary.html#term-label-indicator-format)
.

**y\_score**array-like of shape (n\_samples, n\_labels)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**loss**float

Average number of label pairs that are incorrectly ordered given y\_score weighted by the size of the label set and the number of labels not in the label set.

References

\[1\]

Tsoumakas, G., Katakis, I., & Vlahavas, I. (2010). Mining multi-label data. In Data mining and knowledge discovery handbook (pp. 667-685). Springer US.

Examples

\>>> from sklearn.metrics import label\_ranking\_loss
\>>> y\_true \= \[\[1, 0, 0\], \[0, 0, 1\]\]
\>>> y\_score \= \[\[0.75, 0.5, 1\], \[1, 0.2, 0.1\]\]
\>>> label\_ranking\_loss(y\_true, y\_score)
0.75

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)