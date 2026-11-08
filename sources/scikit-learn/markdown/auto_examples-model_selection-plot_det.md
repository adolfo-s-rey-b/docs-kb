[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_det.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_det.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_det.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_det.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_det.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_det.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#sphx-glr-download-auto-examples-model-selection-plot-det-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Detection error tradeoff (DET) curve[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#detection-error-tradeoff-det-curve "Link to this heading")

===============================================================================================================================================================================

In this example, we compare two binary classification multi-threshold metrics: the Receiver Operating Characteristic (ROC) and the Detection Error Tradeoff (DET). For such purpose, we evaluate two different classifiers for the same classification task.

ROC curves feature true positive rate (TPR) on the Y axis, and false positive rate (FPR) on the X axis. This means that the top left corner of the plot is the “ideal” point - a FPR of zero, and a TPR of one.

DET curves are a variation of ROC curves where False Negative Rate (FNR) is plotted on the y-axis instead of the TPR. In this case the origin (bottom left corner) is the “ideal” point.

Note

*   See [`sklearn.metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     for further information about ROC curves.
    
*   See [`sklearn.metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
     for further information about DET curves.
    
*   This example is loosely based on [Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py)
     example.
    
*   See [Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html#sphx-glr-auto-examples-model-selection-plot-roc-crossval-py)
     for an example estimating the variance of the ROC curves and ROC-AUC.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate synthetic data[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#generate-synthetic-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=1\_000,
    n\_features\=2,
    n\_redundant\=0,
    n\_informative\=2,
    random\_state\=1,
    n\_clusters\_per\_class\=1,
)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.4, random\_state\=0)

Copy to clipboard

Define the classifiers[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#define-the-classifiers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Here we define two different classifiers. The goal is to visually compare their statistical performance across thresholds using the ROC and DET curves.

from sklearn.dummy import [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

classifiers \= {
    "Linear SVM": [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(C\=0.025)),
    "Random Forest": [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(
        max\_depth\=5, n\_estimators\=10, max\_features\=1, random\_state\=0
    ),
    "Non-informative baseline": [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
(),
}

Copy to clipboard

Compare ROC and DET curves[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#compare-roc-and-det-curves "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

DET curves are commonly plotted in normal deviate scale. To achieve this the DET display transforms the error rates as returned by the [`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
 and the axis scale using `scipy.stats.norm`.

import matplotlib.pyplot as plt

from sklearn.dummy import [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay

fig, \[ax\_roc, ax\_det\] \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(11, 5))

ax\_roc.set\_title("Receiver Operating Characteristic (ROC) curves")
ax\_det.set\_title("Detection Error Tradeoff (DET) curves")

ax\_roc.grid(linestyle\="--")
ax\_det.grid(linestyle\="--")

for name, clf in classifiers.items():
    (color, linestyle) \= (
        ("black", "--") if name \== "Non-informative baseline" else (None, None)
    )
    clf.fit(X\_train, y\_train)
    [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(
        clf,
        X\_test,
        y\_test,
        ax\=ax\_roc,
        name\=name,
        curve\_kwargs\=dict(color\=color, linestyle\=linestyle),
    )
    [DetCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")
(
        clf, X\_test, y\_test, ax\=ax\_det, name\=name, color\=color, linestyle\=linestyle
    )

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Receiver Operating Characteristic (ROC) curves, Detection Error Tradeoff (DET) curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_001.png)

Notice that it is easier to visually assess the overall performance of different classification algorithms using DET curves than using ROC curves. As ROC curves are plot in a linear scale, different classifiers usually appear similar for a large part of the plot and differ the most in the top left corner of the graph. On the other hand, because DET curves represent straight lines in normal deviate scale, they tend to be distinguishable as a whole and the area of interest spans a large part of the plot.

DET curves give direct feedback of the detection error tradeoff to aid in operating point analysis. The user can then decide the FNR they are willing to accept at the expense of the FPR (or vice-versa).

Non-informative classifier baseline for the ROC and DET curves[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html#non-informative-classifier-baseline-for-the-roc-and-det-curves "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The diagonal black-dotted lines in the plots above correspond to a [`DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
 using the default “prior” strategy, to serve as baseline for comparison with other classifiers. This classifier makes constant predictions, independent of the input features in `X`, making it a non-informative classifier.

To further understand the non-informative baseline of the ROC and DET curves, we recall the following mathematical definitions:

FPR\=FPFP+TN

FNR\=FNTP+FN

TPR\=TPTP+FN

A classifier that always predict the positive class would have no true negatives nor false negatives, giving FPR\=TPR\=1 and FNR\=0, i.e.:

*   a single point in the upper right corner of the ROC plane,
    
*   a single point in the lower right corner of the DET plane.
    

Similarly, a classifier that always predict the negative class would have no true positives nor false positives, thus FPR\=TPR\=0 and FNR\=1, i.e.:

*   a single point in the lower left corner of the ROC plane,
    
*   a single point in the upper left corner of the DET plane.
    

**Total running time of the script:** (0 minutes 0.235 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_det.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_det.ipynb)

[`Download Jupyter notebook: plot_det.ipynb`](https://scikit-learn.org/stable/_downloads/10bb40e21b74618cdeed618ff1eae595/plot_det.ipynb)

[`Download Python source code: plot_det.py`](https://scikit-learn.org/stable/_downloads/67703ae8c65716668dd87c31a24a069b/plot_det.py)

[`Download zipped: plot_det.zip`](https://scikit-learn.org/stable/_downloads/2393eac1ae8c3b57f87d3a992f256469/plot_det.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_thumb.png)

[ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

ROC Curve with Visualization API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/67703ae8c65716668dd87c31a24a069b/plot_det.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/10bb40e21b74618cdeed618ff1eae595/plot_det.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2393eac1ae8c3b57f87d3a992f256469/plot_det.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_det.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_det.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)