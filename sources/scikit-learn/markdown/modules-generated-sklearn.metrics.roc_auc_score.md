[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

roc\_auc\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#roc-auc-score "Link to this heading")

==============================================================================================================================================

sklearn.metrics.roc\_auc\_score(_y\_true_, _y\_score_, _\*_, _average\='macro'_, _sample\_weight\=None_, _max\_fpr\=None_, _multi\_class\='raise'_, _labels\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L499)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "Link to this definition")

Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores.

Note: this implementation can be used with [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
, [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 classification, but some restrictions apply (see Parameters).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

True labels or [label indicator matrix](https://scikit-learn.org/stable/glossary.html#term-label-indicator-matrix)
. The binary and multiclass cases expect labels with shape (n\_samples,) while the multilabel case expects a [multilabel indicator matrix](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrix)
 with shape (n\_samples, n\_classes).

**y\_score**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

Target scores.

*   In the [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
     case, it corresponds to an array of shape `(n_samples,)`. Both probability estimates and non-thresholded decision values can be provided. The probability estimates correspond to the **probability of the class with the greater label**, i.e. `estimator.classes_[1]` and thus `estimator.predict_proba(X, y)[:, 1]`. The decision values corresponds to the output of `estimator.decision_function(X, y)`. See more information in the [User guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-auc-binary)
    ;
    
*   In the [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
     case, it corresponds to an array of shape `(n_samples, n_classes)` of probability estimates provided by the `predict_proba` method. The probability estimates **must** sum to 1 across the possible classes. In addition, the order of the class scores must correspond to the order of `labels`, if provided, or else to the numerical or lexicographical order of the labels in `y_true`. See more information in the [User guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-auc-multiclass)
    ;
    
*   In the [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
     case, it corresponds to an array of shape `(n_samples, n_classes)`. Probability estimates are provided by the `predict_proba` method and the non-thresholded decision values by the `decision_function` method. The probability estimates correspond to the **probability of the class with the greater label for each output** of the classifier. See more information in the [User guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-auc-multilabel)
    .
    

**average**{‘micro’, ‘macro’, ‘samples’, ‘weighted’} or None, default=’macro’

If `None`, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data. Note: multiclass ROC AUC currently only handles the ‘macro’ and ‘weighted’ averages. For multiclass targets, `average=None` is only implemented for `multi_class='ovr'` and `average='micro'` is only implemented for `multi_class='ovr'`.

`'micro'`:

Calculate metrics globally by considering each element of the label indicator matrix as a label.

`'macro'`:

Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.

`'weighted'`:

Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label).

`'samples'`:

Calculate metrics for each instance, and find their average.

Will be ignored when `y_true` is binary.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**max\_fpr**float > 0 and <= 1, default=None

If not `None`, the standardized partial AUC [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#r4bb7c4558997-2)
 over the range \[0, max\_fpr\] is returned. For the multiclass case, `max_fpr`, should be either equal to `None` or `1.0` as AUC ROC partial computation currently is not supported for multiclass.

**multi\_class**{‘raise’, ‘ovr’, ‘ovo’}, default=’raise’

Only used for multiclass targets. Determines the type of configuration to use. The default value raises an error, so either `'ovr'` or `'ovo'` must be passed explicitly.

`'ovr'`:

Stands for One-vs-rest. Computes the AUC of each class against the rest [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#r4bb7c4558997-3)
 [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#r4bb7c4558997-4)
. This treats the multiclass case in the same way as the multilabel case. Sensitive to class imbalance even when `average == 'macro'`, because class imbalance affects the composition of each of the ‘rest’ groupings.

`'ovo'`:

Stands for One-vs-one. Computes the average AUC of all possible pairwise combinations of classes [\[5\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#r4bb7c4558997-5)
. Insensitive to class imbalance when `average == 'macro'`.

**labels**array-like of shape (n\_classes,), default=None

Only used for multiclass targets. List of labels that index the classes in `y_score`. If `None`, the numerical or lexicographical order of the labels in `y_true` is used.

Returns:

**auc**float

Area Under the Curve score.

See also

[`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")

Area under the precision-recall curve.

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")

Plot Receiver Operating Characteristic (ROC) curve given an estimator and some data.

[`RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")

Plot Receiver Operating Characteristic (ROC) curve given the true and predicted values.

Notes

The Gini Coefficient is a summary measure of the ranking ability of binary classifiers. It is expressed using the area under of the ROC as follows:

G = 2 \* AUC - 1

Where G is the Gini coefficient and AUC is the ROC-AUC score. This normalisation will ensure that random guessing will yield a score of 0 in expectation, and it is upper bounded by 1.

References

\[1\]

[Wikipedia entry for the Receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#id1)\
\]

[Analyzing a portion of the ROC curve. McClish, 1989](https://www.ncbi.nlm.nih.gov/pubmed/2668680)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#id2)\
\]

Provost, F., Domingos, P. (2000). Well-trained PETs: Improving probability estimation trees (Section 6.2), CeDER Working Paper #IS-00-04, Stern School of Business, New York University.

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#id3)\
\]

[Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861-874.](https://www.sciencedirect.com/science/article/pii/S016786550500303X)

\[[5](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#id4)\
\]

[Hand, D.J., Till, R.J. (2001). A Simple Generalisation of the Area Under the ROC Curve for Multiple Class Classification Problems. Machine Learning, 45(2), 171-186.](http://link.springer.com/article/10.1023/A:1010920819831)

\[6\]

[Wikipedia entry for the Gini coefficient](https://en.wikipedia.org/wiki/Gini_coefficient)

Examples

Binary case:

\>>> from sklearn.datasets import load\_breast\_cancer
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.metrics import roc\_auc\_score
\>>> X, y \= load\_breast\_cancer(return\_X\_y\=True)
\>>> clf \= LogisticRegression(solver\="newton-cholesky", random\_state\=0).fit(X, y)
\>>> roc\_auc\_score(y, clf.predict\_proba(X)\[:, 1\])
0.99
\>>> roc\_auc\_score(y, clf.decision\_function(X))
0.99

Copy to clipboard

Multiclass case:

\>>> from sklearn.datasets import load\_iris
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> clf \= LogisticRegression(solver\="newton-cholesky").fit(X, y)
\>>> roc\_auc\_score(y, clf.predict\_proba(X), multi\_class\='ovr')
0.99

Copy to clipboard

Multilabel case:

\>>> import numpy as np
\>>> from sklearn.datasets import make\_multilabel\_classification
\>>> from sklearn.multioutput import MultiOutputClassifier
\>>> X, y \= make\_multilabel\_classification(random\_state\=0)
\>>> clf \= MultiOutputClassifier(clf).fit(X, y)
\>>> \# get a list of n\_output containing probability arrays of shape
\>>> \# (n\_samples, n\_classes)
\>>> y\_score \= clf.predict\_proba(X)
\>>> \# extract the positive columns for each output
\>>> y\_score \= np.transpose(\[score\[:, 1\] for score in y\_score\])
\>>> roc\_auc\_score(y, y\_score, average\=None)
array(\[0.828, 0.852, 0.94, 0.869, 0.95\])
\>>> from sklearn.linear\_model import RidgeClassifierCV
\>>> clf \= RidgeClassifierCV().fit(X, y)
\>>> roc\_auc\_score(y, clf.decision\_function(X), average\=None)
array(\[0.82, 0.847, 0.93, 0.872, 0.944\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_thumb.png)

[Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html)

Statistical comparison of models using grid search

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)