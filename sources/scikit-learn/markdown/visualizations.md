[Skip to main content](https://scikit-learn.org/stable/visualizations.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/visualizations.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/visualizations.html)
[1.8.0](https://scikit-learn.org/1.8/visualizations.html)
[1.7.2](https://scikit-learn.org/1.7/visualizations.html)
[1.6.1](https://scikit-learn.org/1.6/visualizations.html)
[1.5.2](https://scikit-learn.org/1.5/visualizations.html)
[1.4.2](https://scikit-learn.org/1.4/visualizations.html)

Collapse Sidebar Expand Sidebar

6\. Visualizations[#](https://scikit-learn.org/stable/visualizations.html#visualizations "Link to this heading")

=================================================================================================================

Scikit-learn defines a simple API for creating visualizations for machine learning. The key feature of this API is to allow for quick plotting and visual adjustments without recalculation. We provide `Display` classes that expose two methods for creating plots: `from_estimator` and `from_predictions`.

The `from_estimator` method generates a `Display` object from a fitted estimator, input data (`X`, `y`), and a plot. The `from_predictions` method creates a `Display` object from true and predicted values (`y_test`, `y_pred`), and a plot.

Using `from_predictions` avoids having to recompute predictions, but the user needs to take care that the prediction values passed correspond to the `pos_label`. For [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
, select the column corresponding to the `pos_label` class while for [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
, revert the score (i.e. multiply by -1) if `pos_label` is not the last class in the `classes_` attribute of your estimator.

The `Display` object stores the computed values (e.g., metric values or feature importance) required for plotting with Matplotlib. These values are the results derived from the raw predictions passed to `from_predictions`, or an estimator and `X` passed to `from_estimator`.

Display objects have a plot method that creates a matplotlib plot once the display object has been initialized (note that we recommend that display objects are created via `from_estimator` or `from_predictions` instead of initialized directly). The plot method allows adding to an existing plot by passing the existing plots [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.1)")
 to the `ax` parameter.

In the following example, we plot a ROC curve for a fitted Logistic Regression model `from_estimator`:

from sklearn.model\_selection import train\_test\_split
from sklearn.linear\_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load\_iris

X, y \= load\_iris(return\_X\_y\=True)
y \= y \== 2  \# make binary
X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
   X, y, test\_size\=.8, random\_state\=42
)
clf \= LogisticRegression(random\_state\=42, C\=.01)
clf.fit(X\_train, y\_train)

clf\_disp \= RocCurveDisplay.from\_estimator(clf, X\_test, y\_test)

Copy to clipboard

![_images/visualizations-1.png](https://scikit-learn.org/stable/_images/visualizations-1.png)

If you already have the prediction values, you could instead use `from_predictions` to do the same thing (and save on compute):

from sklearn.model\_selection import train\_test\_split
from sklearn.linear\_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load\_iris

X, y \= load\_iris(return\_X\_y\=True)
y \= y \== 2  \# make binary
X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
   X, y, test\_size\=.8, random\_state\=42
)
clf \= LogisticRegression(random\_state\=42, C\=.01)
clf.fit(X\_train, y\_train)

\# select the probability of the class that we considered to be the positive label
y\_pred \= clf.predict\_proba(X\_test)\[:, 1\]

clf\_disp \= RocCurveDisplay.from\_predictions(y\_test, y\_pred)

Copy to clipboard

![_images/visualizations-2.png](https://scikit-learn.org/stable/_images/visualizations-2.png)

The returned `clf_disp` object allows us to add another curve to the already computed ROC curve. In this case, the `clf_disp` is a [`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
 that stores the computed values as attributes called `roc_auc`, `fpr`, and `tpr`.

Next, we train a random forest classifier and plot the previously computed ROC curve again by using the `plot` method of the `Display` object.

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

rfc \= RandomForestClassifier(n\_estimators\=10, random\_state\=42)
rfc.fit(X\_train, y\_train)

ax \= plt.gca()
rfc\_disp \= RocCurveDisplay.from\_estimator(
  rfc, X\_test, y\_test, ax\=ax, curve\_kwargs\={"alpha": 0.8}
)
clf\_disp.plot(ax\=ax, curve\_kwargs\={"alpha": 0.8})

Copy to clipboard

![_images/visualizations-3.png](https://scikit-learn.org/stable/_images/visualizations-3.png)

Notice that we pass `alpha=0.8` to the plot functions to adjust the alpha values of the curves.

Examples

*   [Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#sphx-glr-auto-examples-inspection-plot-partial-dependence-visualization-api-py)
    
*   [ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#sphx-glr-auto-examples-miscellaneous-plot-roc-curve-visualization-api-py)
    
*   [Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html#sphx-glr-auto-examples-miscellaneous-plot-display-object-visualization-py)
    
*   [Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#sphx-glr-auto-examples-calibration-plot-compare-calibration-py)
    

6.1. Available Plotting Utilities[#](https://scikit-learn.org/stable/visualizations.html#available-plotting-utilities "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

### 6.1.1. Display Objects[#](https://scikit-learn.org/stable/visualizations.html#display-objects "Link to this heading")

|     |     |
| --- | --- |
| [`calibration.CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")<br>(prob\_true, ...) | Calibration curve (also known as reliability diagram) visualization. |
| [`inspection.PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")<br>(...\[, ...\]) | Partial Dependence Plot (PDP) and Individual Conditional Expectation (ICE). |
| [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")<br>(\*, xx0, ...) | Decisions boundary visualization. |
| [`metrics.ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")<br>(...\[, ...\]) | Confusion Matrix visualization. |
| [`metrics.DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")<br>(\*, fpr, fnr\[, ...\]) | Detection Error Tradeoff (DET) curve visualization. |
| [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")<br>(precision, ...) | Precision Recall visualization. |
| [`metrics.PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")<br>(\*, y\_true, y\_pred) | Visualization of the prediction error of a regression model. |
| [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")<br>(\*, fpr, tpr\[, ...\]) | ROC Curve visualization. |
| [`model_selection.LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")<br>(\*, ...) | Learning Curve visualization. |
| [`model_selection.ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")<br>(\*, ...) | Validation Curve visualization. |

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)