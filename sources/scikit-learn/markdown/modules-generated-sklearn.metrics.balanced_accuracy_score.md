[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.balanced_accuracy_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.balanced_accuracy_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.balanced_accuracy_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.balanced_accuracy_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.balanced_accuracy_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.balanced_accuracy_score.html)

Collapse Sidebar Expand Sidebar

balanced\_accuracy\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#balanced-accuracy-score "Link to this heading")

============================================================================================================================================================================

sklearn.metrics.balanced\_accuracy\_score(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _adjusted\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L2846)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "Link to this definition")

Compute the balanced accuracy.

The balanced accuracy in binary and multiclass classification problems to deal with imbalanced datasets. It is defined as the average of recall obtained on each class.

The best value is 1 and the worst value is 0 when `adjusted=False`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#balanced-accuracy-score)
.

Added in version 0.20.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,)

Estimated targets as returned by a classifier.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**adjusted**bool, default=False

When true, the result is adjusted for chance, so that random performance would score 0, while keeping perfect performance at a score of 1.

Returns:

**balanced\_accuracy**float

Balanced accuracy score.

See also

[`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")

Compute average precision (AP) from prediction scores.

[`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")

Compute the precision score.

[`recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")

Compute the recall score.

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores.

Notes

Some literature promotes alternative definitions of balanced accuracy. Our definition is equivalent to [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
 with class-balanced sample weights, and shares desirable properties with the binary case. See the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#balanced-accuracy-score)
.

References

\[1\]

Brodersen, K.H.; Ong, C.S.; Stephan, K.E.; Buhmann, J.M. (2010). The balanced accuracy and its posterior distribution. Proceedings of the 20th International Conference on Pattern Recognition, 3121-24.

\[2\]

John. D. Kelleher, Brian Mac Namee, Aoife D’Arcy, (2015). [Fundamentals of Machine Learning for Predictive Data Analytics: Algorithms, Worked Examples, and Case Studies](https://mitpress.mit.edu/books/fundamentals-machine-learning-predictive-data-analytics)
.

Examples

\>>> from sklearn.metrics import balanced\_accuracy\_score
\>>> y\_true \= \[0, 1, 0, 0, 1, 0\]
\>>> y\_pred \= \[0, 1, 0, 0, 0, 1\]
\>>> balanced\_accuracy\_score(y\_true, y\_pred)
0.625

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)