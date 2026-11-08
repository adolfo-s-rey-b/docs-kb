[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.classification_report.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.classification_report.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.classification_report.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.classification_report.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.classification_report.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.classification_report.html)

Collapse Sidebar Expand Sidebar

classification\_report[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#classification-report "Link to this heading")

=====================================================================================================================================================================

sklearn.metrics.classification\_report(_y\_true_, _y\_pred_, _\*_, _labels\=None_, _target\_names\=None_, _sample\_weight\=None_, _digits\=2_, _output\_dict\=False_, _zero\_division\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L2950)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "Link to this definition")

Build a text report showing the main classification metrics.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-report)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) target values. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Estimated targets as returned by a classifier. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**labels**array-like of shape (n\_labels,), default=None

Optional list of label indices to include in the report.

**target\_names**array-like of shape (n\_labels,), default=None

Optional display names matching the labels (same order).

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**digits**int, default=2

Number of digits for formatting output floating point values. When `output_dict` is `True`, this will be ignored and the returned values will not be rounded.

**output\_dict**bool, default=False

If True, return output as dict.

Added in version 0.20.

**zero\_division**{“warn”, 0.0, 1.0, np.nan}, default=”warn”

Sets the value to return when there is a zero division. If set to “warn”, this acts as 0, but warnings are also raised.

Added in version 1.3: `np.nan` option was added.

Returns:

**report**str or dict

Text summary of the precision, recall, F1 score for each class. Dictionary returned if output\_dict is True. Dictionary has the following structure:

{'label 1': {'precision':0.5,
             'recall':1.0,
             'f1-score':0.67,
             'support':1},
 'label 2': { ... },
  ...
}

Copy to clipboard

The reported averages include macro average (averaging the unweighted mean per label), weighted average (averaging the support-weighted mean per label), and sample average (only for multilabel classification). Micro average (averaging the total true positives, false negatives and false positives) is only shown for multi-label or multi-class with a subset of classes, because it corresponds to accuracy otherwise and would be the same for all metrics. See also [`precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")
 for more details on averages.

Note that in binary classification, recall of the positive class is also known as “sensitivity”; recall of the negative class is “specificity”.

See also

[`precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")

Compute precision, recall, F-measure and support for each class.

[`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")

Compute confusion matrix to evaluate the accuracy of a classification.

[`multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")

Compute a confusion matrix for each class or sample.

Examples

\>>> from sklearn.metrics import classification\_report
\>>> y\_true \= \[0, 1, 2, 2, 2\]
\>>> y\_pred \= \[0, 0, 2, 2, 1\]
\>>> target\_names \= \['class 0', 'class 1', 'class 2'\]
\>>> print(classification\_report(y\_true, y\_pred, target\_names\=target\_names))
              precision    recall  f1-score   support

     class 0       0.50      1.00      0.67         1
     class 1       0.00      0.00      0.00         1
     class 2       1.00      0.67      0.80         3

    accuracy                           0.60         5
   macro avg       0.50      0.56      0.49         5
weighted avg       0.70      0.60      0.61         5

\>>> y\_pred \= \[1, 1, 0\]
\>>> y\_true \= \[1, 1, 1\]
\>>> print(classification\_report(y\_true, y\_pred, labels\=\[1, 2, 3\]))
              precision    recall  f1-score   support

           1       1.00      0.67      0.80         3
           2       0.00      0.00      0.00         0
           3       0.00      0.00      0.00         0

   micro avg       1.00      0.67      0.80         3
   macro avg       0.33      0.22      0.27         3
weighted avg       1.00      0.67      0.80         3

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

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