[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_confusion_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_confusion_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_confusion_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_confusion_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_confusion_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_confusion_matrix.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-download-auto-examples-model-selection-plot-confusion-matrix-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Evaluate the performance of a classifier with Confusion Matrix[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#evaluate-the-performance-of-a-classifier-with-confusion-matrix "Link to this heading")

==================================================================================================================================================================================================================================================

Example of confusion matrix usage to evaluate the quality of the output of a classifier on the iris data set. The diagonal elements represent the number of points for which the predicted label is equal to the true label, while off-diagonal elements are those that are mislabeled by the classifier. The higher the diagonal values of the confusion matrix the better, indicating many correct predictions.

The figures show the confusion matrix with and without normalization by class support size (number of elements in each class). This kind of normalization can be interesting in case of class imbalance to have a more visual interpretation of which class is being misclassified.

Here the results are not as good as they could be as our choice for the regularization parameter C was not the best. In real life applications this parameter is usually chosen using [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

\# import some data to play with
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data
y \= iris.target
class\_names \= iris.target\_names

\# Split the data into a training set and a test set
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

\# Run classifier, using a model that is too regularized (C too low) to see
\# the impact on the results
classifier \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=0.01).fit(X\_train, y\_train)

[np.set\_printoptions](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
(precision\=2)

\# Plot non-normalized confusion matrix
titles\_options \= \[\
    ("Confusion matrix, without normalization", None),\
    ("Normalized confusion matrix", "true"),\
\]
for title, normalize in titles\_options:
    disp \= [ConfusionMatrixDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
(
        classifier,
        X\_test,
        y\_test,
        display\_labels\=class\_names,
        cmap\=plt.cm.Blues,
        normalize\=normalize,
    )
    disp.ax\_.set\_title(title)

    print(title)
    print(disp.confusion\_matrix)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Confusion matrix, without normalization](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_001.png)
*   ![Normalized confusion matrix](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_002.png)

Confusion matrix, without normalization
\[\[13  0  0\]\
 \[ 0  3 13\]\
 \[ 0  0  9\]\]
Normalized confusion matrix
\[\[1.   0.   0.  \]\
 \[0.   0.19 0.81\]\
 \[0.   0.   1.  \]\]

Copy to clipboard

Binary Classification[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#binary-classification "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

For binary classification, use [`sklearn.metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
 with the `ravel` method to get counts of true negatives, false positives, false negatives, and true positives.

To obtain counts of true negatives, false positives, false negatives, and true positives at different thresholds, one can use [`sklearn.metrics.confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")
. This is fundamental for binary classification metrics like [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
 and [`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.metrics import [confusion\_matrix\_at\_thresholds](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=100,
    n\_features\=20,
    n\_informative\=20,
    n\_redundant\=0,
    n\_classes\=2,
    random\_state\=42,
)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.3, random\_state\=42
)

classifier \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=0.01)
classifier.fit(X\_train, y\_train)

y\_score \= classifier.predict\_proba(X\_test)\[:, 1\]

tns, fps, fns, tps, thresholds \= [confusion\_matrix\_at\_thresholds](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")
(y\_test, y\_score)

\# Plot TNs, FPs, FNs and TPs vs Thresholds
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 6))

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(thresholds, tns, label\="True Negatives (TNs)")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(thresholds, fps, label\="False Positives (FPs)")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(thresholds, fns, label\="False Negatives (FNs)")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(thresholds, tps, label\="True Positives (TPs)")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Thresholds")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Count")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("TNs, FPs, FNs and TPs vs Thresholds")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![TNs, FPs, FNs and TPs vs Thresholds](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_003.png)

**Total running time of the script:** (0 minutes 0.307 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_confusion_matrix.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_confusion_matrix.ipynb)

[`Download Jupyter notebook: plot_confusion_matrix.ipynb`](https://scikit-learn.org/stable/_downloads/9ad55bf68758018c9961815802c65e18/plot_confusion_matrix.ipynb)

[`Download Python source code: plot_confusion_matrix.py`](https://scikit-learn.org/stable/_downloads/d6fdb17f9d063111bf8547f1af312fc5/plot_confusion_matrix.py)

[`Download zipped: plot_confusion_matrix.zip`](https://scikit-learn.org/stable/_downloads/bb136fd1099bc957fc4cc8e783dd9b2e/plot_confusion_matrix.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/d6fdb17f9d063111bf8547f1af312fc5/plot_confusion_matrix.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/9ad55bf68758018c9961815802c65e18/plot_confusion_matrix.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/bb136fd1099bc957fc4cc8e783dd9b2e/plot_confusion_matrix.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_confusion_matrix.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_confusion_matrix.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)