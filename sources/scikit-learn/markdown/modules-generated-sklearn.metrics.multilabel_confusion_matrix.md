[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html)

Collapse Sidebar Expand Sidebar

multilabel\_confusion\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#multilabel-confusion-matrix "Link to this heading")

========================================================================================================================================================================================

sklearn.metrics.multilabel\_confusion\_matrix(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _labels\=None_, _samplewise\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L626)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "Link to this definition")

Compute a confusion matrix for each class or sample.

Added in version 0.21.

Compute class-wise (default) or sample-wise (samplewise=True) multilabel confusion matrix to evaluate the accuracy of a classification, and output confusion matrices for each class or sample.

In multilabel confusion matrix MCM, the count of true negatives is MCM:,0,0, false negatives is MCM:,1,0, true positives is MCM:,1,1 and false positives is MCM:,0,1.

Multiclass data will be treated as if binarized under a one-vs-rest transformation. Returned confusion matrices will be in the order of sorted unique labels in the union of (y\_true, y\_pred).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#multilabel-confusion-matrix)
.

Parameters:

**y\_true**{array-like, sparse matrix} of shape (n\_samples, n\_outputs) or (n\_samples,)

Ground truth (correct) target values. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**{array-like, sparse matrix} of shape (n\_samples, n\_outputs) or (n\_samples,)

Estimated targets as returned by a classifier. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**labels**array-like of shape (n\_classes,), default=None

A list of classes or column indices to select some (or to force inclusion of classes absent from the data).

**samplewise**bool, default=False

In the multilabel case, this calculates a confusion matrix per sample.

Returns:

**multi\_confusion**ndarray of shape (n\_outputs, 2, 2)

A 2x2 confusion matrix corresponding to each output in the input. When calculating class-wise multi\_confusion (default), then n\_outputs = n\_labels; when calculating sample-wise multi\_confusion (samplewise=True), n\_outputs = n\_samples. If `labels` is defined, the results will be returned in the order specified in `labels`, otherwise the results will be returned in sorted order by default.

See also

[`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")

Compute confusion matrix to evaluate the accuracy of a classifier.

Notes

The `multilabel_confusion_matrix` calculates class-wise or sample-wise multilabel confusion matrices, and in multiclass tasks, labels are binarized under a one-vs-rest way; while [`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
 calculates one confusion matrix for confusion between every two classes.

Examples

Multilabel-indicator case:

\>>> import numpy as np
\>>> from sklearn.metrics import multilabel\_confusion\_matrix
\>>> y\_true \= np.array(\[\[1, 0, 1\],\
...                    \[0, 1, 0\]\])
\>>> y\_pred \= np.array(\[\[1, 0, 0\],\
...                    \[0, 1, 1\]\])
\>>> multilabel\_confusion\_matrix(y\_true, y\_pred)
array(\[\[\[1, 0\],\
        \[0, 1\]\],\
\
       \[\[1, 0\],\
        \[0, 1\]\],\
\
       \[\[0, 1\],\
        \[1, 0\]\]\])

Copy to clipboard

Multiclass case:

\>>> y\_true \= \["cat", "ant", "cat", "cat", "ant", "bird"\]
\>>> y\_pred \= \["ant", "ant", "cat", "cat", "ant", "cat"\]
\>>> multilabel\_confusion\_matrix(y\_true, y\_pred,
...                             labels\=\["ant", "bird", "cat"\])
array(\[\[\[3, 1\],\
        \[0, 2\]\],\
\
       \[\[5, 0\],\
        \[1, 0\]\],\
\
       \[\[2, 1\],\
        \[1, 2\]\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)