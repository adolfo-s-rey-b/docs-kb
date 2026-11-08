[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.confusion_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.confusion_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.confusion_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.confusion_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.confusion_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.confusion_matrix.html)

Collapse Sidebar Expand Sidebar

confusion\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#confusion-matrix "Link to this heading")

======================================================================================================================================================

sklearn.metrics.confusion\_matrix(_y\_true_, _y\_pred_, _\*_, _labels\=None_, _sample\_weight\=None_, _normalize\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L418)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "Link to this definition")

Compute confusion matrix to evaluate the accuracy of a classification.

By definition a confusion matrix C is such that Ci,j is equal to the number of observations known to be in group i and predicted to be in group j.

Thus in binary classification, the count of true negatives is C0,0, false negatives is C1,0, true positives is C1,1 and false positives is C0,1.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,)

Estimated targets as returned by a classifier.

**labels**array-like of shape (n\_classes,), default=None

List of labels to index the matrix. This may be used to reorder or select a subset of labels. If `None` is given, those that appear at least once in `y_true` or `y_pred` are used in sorted order.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Added in version 0.18.

**normalize**{‘true’, ‘pred’, ‘all’}, default=None

Normalizes confusion matrix over the true (rows), predicted (columns) conditions or all the population. If None, confusion matrix will not be normalized.

Returns:

**C**ndarray of shape (n\_classes, n\_classes)

Confusion matrix whose i-th row and j-th column entry indicates the number of samples with true label being i-th class and predicted label being j-th class.

See also

[`ConfusionMatrixDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")

Plot the confusion matrix given an estimator, the data, and the label.

[`ConfusionMatrixDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")

Plot the confusion matrix given the true and predicted labels.

[`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")

Confusion Matrix visualization.

[`confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")

For binary classification, compute true negative, false positive, false negative and true positive counts per threshold.

References

\[1\]

[Wikipedia entry for the Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
 (Wikipedia and other references may use a different convention for axes).

Examples

\>>> from sklearn.metrics import confusion\_matrix
\>>> y\_true \= \[2, 0, 2, 2, 0, 1\]
\>>> y\_pred \= \[0, 0, 2, 2, 0, 2\]
\>>> confusion\_matrix(y\_true, y\_pred)
array(\[\[2, 0, 0\],\
       \[0, 0, 1\],\
       \[1, 0, 2\]\])

Copy to clipboard

\>>> y\_true \= \["cat", "ant", "cat", "cat", "ant", "bird"\]
\>>> y\_pred \= \["ant", "ant", "cat", "cat", "ant", "cat"\]
\>>> confusion\_matrix(y\_true, y\_pred, labels\=\["ant", "bird", "cat"\])
array(\[\[2, 0, 0\],\
       \[0, 0, 1\],\
       \[1, 0, 2\]\])

Copy to clipboard

In the binary case, we can extract true positives, etc. as follows:

\>>> tn, fp, fn, tp \= confusion\_matrix(\[0, 1, 0, 1\], \[1, 1, 1, 0\]).ravel().tolist()
\>>> (tn, fp, fn, tp)
(0, 2, 1, 1)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_active_learning_thumb.png)

[Label Propagation digits: Active learning](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)

Label Propagation digits: Active learning

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)