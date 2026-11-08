[Skip to main content](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/calibration/plot_calibration_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/calibration/plot_calibration_curve.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/calibration/plot_calibration_curve.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/calibration/plot_calibration_curve.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/calibration/plot_calibration_curve.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/calibration/plot_calibration_curve.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#sphx-glr-download-auto-examples-calibration-plot-calibration-curve-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Probability Calibration curves[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#probability-calibration-curves "Link to this heading")

===============================================================================================================================================================================

When performing classification one often wants to predict not only the class label, but also the associated probability. This probability gives some kind of confidence on the prediction. This example demonstrates how to visualize how well calibrated the predicted probabilities are using calibration curves, also known as reliability diagrams. Calibration of an uncalibrated classifier will also be demonstrated.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#dataset "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

We will use a synthetic binary classification dataset with 100,000 samples and 20 features. Of the 20 features, only 2 are informative, 10 are redundant (random combinations of the informative features) and the remaining 8 are uninformative (random numbers). Of the 100,000 samples, 1,000 will be used for model fitting and the rest for testing.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=100\_000, n\_features\=20, n\_informative\=2, n\_redundant\=10, random\_state\=42
)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.99, random\_state\=42
)

Copy to clipboard

Calibration curves[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#calibration-curves "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

### Gaussian Naive Bayes[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#gaussian-naive-bayes "Link to this heading")

First, we will compare:

*   [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     (used as baseline since very often, properly regularized logistic regression is well calibrated by default thanks to the use of the log-loss)
    
*   Uncalibrated [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
    
*   [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     with isotonic and sigmoid calibration (see [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
    )
    

Calibration curves for all 4 conditions are plotted below, with the average predicted probability for each bin on the x-axis and the fraction of positive classes in each bin on the y-axis.

import matplotlib.pyplot as plt
from matplotlib.gridspec import [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
, CalibrationDisplay
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.naive\_bayes import [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")

lr \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=1.0)
gnb \= [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
()
gnb\_isotonic \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(gnb, cv\=2, method\="isotonic")
gnb\_sigmoid \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(gnb, cv\=2, method\="sigmoid")

clf\_list \= \[\
    (lr, "Logistic"),\
    (gnb, "Naive Bayes"),\
    (gnb\_isotonic, "Naive Bayes + Isotonic"),\
    (gnb\_sigmoid, "Naive Bayes + Sigmoid"),\
\]

Copy to clipboard

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
gs \= [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(4, 2)
colors \= [plt.get\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
("Dark2")

ax\_calibration\_curve \= fig.add\_subplot(gs\[:2, :2\])
calibration\_displays \= {}
for i, (clf, name) in enumerate(clf\_list):
    clf.fit(X\_train, y\_train)
    display \= [CalibrationDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")
(
        clf,
        X\_test,
        y\_test,
        n\_bins\=10,
        name\=name,
        ax\=ax\_calibration\_curve,
        color\=colors(i),
    )
    calibration\_displays\[name\] \= display

ax\_calibration\_curve.grid()
ax\_calibration\_curve.set\_title("Calibration plots (Naive Bayes)")

\# Add histogram
grid\_positions \= \[(2, 0), (2, 1), (3, 0), (3, 1)\]
for i, (\_, name) in enumerate(clf\_list):
    row, col \= grid\_positions\[i\]
    ax \= fig.add\_subplot(gs\[row, col\])

    ax.hist(
        calibration\_displays\[name\].y\_prob,
        range\=(0, 1),
        bins\=10,
        label\=name,
        color\=colors(i),
    )
    ax.set(title\=name, xlabel\="Mean predicted probability", ylabel\="Count")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Calibration plots (Naive Bayes), Logistic, Naive Bayes, Naive Bayes + Isotonic, Naive Bayes + Sigmoid](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_001.png)

Uncalibrated [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
 is poorly calibrated because of the redundant features which violate the assumption of feature-independence and result in an overly confident classifier, which is indicated by the typical transposed-sigmoid curve. Calibration of the probabilities of [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
 with [Isotonic regression](https://scikit-learn.org/stable/modules/isotonic.html#isotonic)
 can fix this issue as can be seen from the nearly diagonal calibration curve. [Sigmoid regression](https://scikit-learn.org/stable/modules/calibration.html#sigmoid-regressor)
 also improves calibration slightly, albeit not as strongly as the non-parametric isotonic regression. This can be attributed to the fact that we have plenty of calibration data such that the greater flexibility of the non-parametric model can be exploited.

Below we will make a quantitative analysis considering several classification metrics: [Brier score loss](https://scikit-learn.org/stable/modules/model_evaluation.html#brier-score-loss)
, [Log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)
, [precision, recall, F1 score](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
 and [ROC AUC](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")

import pandas as pd

from sklearn.metrics import (
    [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
,
    [f1\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
,
    [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
,
    [precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
,
    [recall\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
,
    [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
,
)

scores \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
for i, (clf, name) in enumerate(clf\_list):
    clf.fit(X\_train, y\_train)
    y\_prob \= clf.predict\_proba(X\_test)
    y\_pred \= clf.predict(X\_test)
    scores\["Classifier"\].append(name)

    for metric in \[[brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")\
, [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")\
, [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")\
\]:
        score\_name \= metric.\_\_name\_\_.replace("\_", " ").replace("score", "").capitalize()
        scores\[score\_name\].append(metric(y\_test, y\_prob\[:, 1\]))

    for metric in \[[precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")\
, [recall\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")\
, [f1\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")\
\]:
        score\_name \= metric.\_\_name\_\_.replace("\_", " ").replace("score", "").capitalize()
        scores\[score\_name\].append(metric(y\_test, y\_pred))

    score\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(scores).set\_index("Classifier")
    score\_df.round(decimals\=3)

score\_df

Copy to clipboard

|     | Brier  loss | Log loss | Roc auc | Precision | Recall | F1  |
| --- | --- | --- | --- | --- | --- | --- |
| Classifier |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| Logistic | 0.098932 | 0.323200 | 0.937443 | 0.871965 | 0.851348 | 0.861533 |
| Naive Bayes | 0.117608 | 0.782755 | 0.940373 | 0.857400 | 0.875941 | 0.866571 |
| Naive Bayes + Isotonic | 0.098332 | 0.370738 | 0.938613 | 0.883065 | 0.836224 | 0.859007 |
| Naive Bayes + Sigmoid | 0.108880 | 0.368896 | 0.940201 | 0.861106 | 0.871277 | 0.866161 |

  
  

Notice that although calibration improves the [Brier score loss](https://scikit-learn.org/stable/modules/model_evaluation.html#brier-score-loss)
 (a metric composed of calibration term and refinement term) and [Log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)
, it does not significantly alter the prediction accuracy measures (precision, recall and F1 score). This is because calibration should not significantly change prediction probabilities at the location of the decision threshold (at x = 0.5 on the graph). Calibration should however, make the predicted probabilities more accurate and thus more useful for making allocation decisions under uncertainty. Further, ROC AUC, should not change at all because calibration is a monotonic transformation. Indeed, no rank metrics are affected by calibration.

### Linear support vector classifier[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#linear-support-vector-classifier "Link to this heading")

Next, we will compare:

*   [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     (baseline)
    
*   Uncalibrated [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    . Since SVC does not output probabilities by default, we naively scale the output of the [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
     into \[0, 1\] by applying min-max scaling.
    
*   [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     with isotonic and sigmoid calibration (see [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
    )
    

import numpy as np

from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

class NaivelyCalibratedLinearSVC([LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
):
    """LinearSVC with \`predict\_proba\` method that naively scales
    \`decision\_function\` output for binary classification."""

    def fit(self, X, y):
        super().fit(X, y)
        df \= self.decision\_function(X)
        self.df\_min\_ \= df.min()
        self.df\_max\_ \= df.max()

    def predict\_proba(self, X):
        """Min-max scale output of \`decision\_function\` to \[0, 1\]."""
        df \= self.decision\_function(X)
        calibrated\_df \= (df \- self.df\_min\_) / (self.df\_max\_ \- self.df\_min\_)
        proba\_pos\_class \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(calibrated\_df, 0, 1)
        proba\_neg\_class \= 1 \- proba\_pos\_class
        proba \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[proba\_neg\_class, proba\_pos\_class\]
        return proba

Copy to clipboard

lr \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=1.0)
svc \= NaivelyCalibratedLinearSVC(max\_iter\=10\_000)
svc\_isotonic \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(svc, cv\=2, method\="isotonic")
svc\_sigmoid \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
(svc, cv\=2, method\="sigmoid")

clf\_list \= \[\
    (lr, "Logistic"),\
    (svc, "SVC"),\
    (svc\_isotonic, "SVC + Isotonic"),\
    (svc\_sigmoid, "SVC + Sigmoid"),\
\]

Copy to clipboard

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
gs \= [GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(4, 2)

ax\_calibration\_curve \= fig.add\_subplot(gs\[:2, :2\])
calibration\_displays \= {}
for i, (clf, name) in enumerate(clf\_list):
    clf.fit(X\_train, y\_train)
    display \= [CalibrationDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")
(
        clf,
        X\_test,
        y\_test,
        n\_bins\=10,
        name\=name,
        ax\=ax\_calibration\_curve,
        color\=colors(i),
    )
    calibration\_displays\[name\] \= display

ax\_calibration\_curve.grid()
ax\_calibration\_curve.set\_title("Calibration plots (SVC)")

\# Add histogram
grid\_positions \= \[(2, 0), (2, 1), (3, 0), (3, 1)\]
for i, (\_, name) in enumerate(clf\_list):
    row, col \= grid\_positions\[i\]
    ax \= fig.add\_subplot(gs\[row, col\])

    ax.hist(
        calibration\_displays\[name\].y\_prob,
        range\=(0, 1),
        bins\=10,
        label\=name,
        color\=colors(i),
    )
    ax.set(title\=name, xlabel\="Mean predicted probability", ylabel\="Count")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Calibration plots (SVC), Logistic, SVC, SVC + Isotonic, SVC + Sigmoid](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_002.png)

[`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 shows the opposite behavior to [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
; the calibration curve has a sigmoid shape, which is typical for an under-confident classifier. In the case of [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
, this is caused by the margin property of the hinge loss, which focuses on samples that are close to the decision boundary (support vectors). Samples that are far away from the decision boundary do not impact the hinge loss. It thus makes sense that [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 does not try to separate samples in the high confidence region regions. This leads to flatter calibration curves near 0 and 1 and is empirically shown with a variety of datasets in Niculescu-Mizil & Caruana [\[1\]](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#id2)
.

Both kinds of calibration (sigmoid and isotonic) can fix this issue and yield similar results.

As before, we show the [Brier score loss](https://scikit-learn.org/stable/modules/model_evaluation.html#brier-score-loss)
, [Log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)
, [precision, recall, F1 score](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
 and [ROC AUC](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

scores \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
for i, (clf, name) in enumerate(clf\_list):
    clf.fit(X\_train, y\_train)
    y\_prob \= clf.predict\_proba(X\_test)
    y\_pred \= clf.predict(X\_test)
    scores\["Classifier"\].append(name)

    for metric in \[[brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")\
, [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")\
, [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")\
\]:
        score\_name \= metric.\_\_name\_\_.replace("\_", " ").replace("score", "").capitalize()
        scores\[score\_name\].append(metric(y\_test, y\_prob\[:, 1\]))

    for metric in \[[precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")\
, [recall\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")\
, [f1\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")\
\]:
        score\_name \= metric.\_\_name\_\_.replace("\_", " ").replace("score", "").capitalize()
        scores\[score\_name\].append(metric(y\_test, y\_pred))

    score\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(scores).set\_index("Classifier")
    score\_df.round(decimals\=3)

score\_df

Copy to clipboard

|     | Brier  loss | Log loss | Roc auc | Precision | Recall | F1  |
| --- | --- | --- | --- | --- | --- | --- |
| Classifier |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| Logistic | 0.098932 | 0.323200 | 0.937443 | 0.871965 | 0.851348 | 0.861533 |
| SVC | 0.144943 | 0.465660 | 0.937597 | 0.872186 | 0.851792 | 0.861868 |
| SVC + Isotonic | 0.099820 | 0.376999 | 0.936480 | 0.853174 | 0.877981 | 0.865400 |
| SVC + Sigmoid | 0.098758 | 0.321301 | 0.937532 | 0.873724 | 0.848743 | 0.861053 |

  
  

As with [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
 above, calibration improves both [Brier score loss](https://scikit-learn.org/stable/modules/model_evaluation.html#brier-score-loss)
 and [Log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)
 but does not alter the prediction accuracy measures (precision, recall and F1 score) much.

Summary[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#summary "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Parametric sigmoid calibration can deal with situations where the calibration curve of the base classifier is sigmoid (e.g., for [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
) but not where it is transposed-sigmoid (e.g., [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
). Non-parametric isotonic calibration can deal with both situations but may require more data to produce good results.

References[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#references "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

**Total running time of the script:** (0 minutes 3.060 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_calibration_curve.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_calibration_curve.ipynb)

[`Download Jupyter notebook: plot_calibration_curve.ipynb`](https://scikit-learn.org/stable/_downloads/6d4f620ec6653356eb970c2a6ed62081/plot_calibration_curve.ipynb)

[`Download Python source code: plot_calibration_curve.py`](https://scikit-learn.org/stable/_downloads/85db957603c93bd3e0a4265ea6565b13/plot_calibration_curve.py)

[`Download zipped: plot_calibration_curve.zip`](https://scikit-learn.org/stable/_downloads/5411a737a70dedec6dd709c217d0ce3f/plot_calibration_curve.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/85db957603c93bd3e0a4265ea6565b13/plot_calibration_curve.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6d4f620ec6653356eb970c2a6ed62081/plot_calibration_curve.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5411a737a70dedec6dd709c217d0ce3f/plot_calibration_curve.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_calibration_curve.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_calibration_curve.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)