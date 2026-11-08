[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.DetCurveDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.DetCurveDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.DetCurveDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.DetCurveDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.DetCurveDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.DetCurveDisplay.html)

Collapse Sidebar Expand Sidebar

DetCurveDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#detcurvedisplay "Link to this heading")

==================================================================================================================================================

class sklearn.metrics.DetCurveDisplay(_\*_, _fpr_, _fnr_, _estimator\_name\=None_, _pos\_label\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/det_curve.py#L14)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "Link to this definition")

Detection Error Tradeoff (DET) curve visualization.

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")
 to create a visualizer. All parameters are stored as attributes.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#det-curve)
.

Added in version 0.24.

Parameters:

**fpr**ndarray

False positive rate.

**fnr**ndarray

False negative rate.

**estimator\_name**str, default=None

Name of estimator. If None, the estimator name is not shown.

**pos\_label**int, float, bool or str, default=None

The label of the positive class. If not `None`, this value is displayed in the x- and y-axes labels.

Attributes:

**line\_**matplotlib Artist

DET Curve.

**ax\_**matplotlib Axes

Axes with DET Curve.

**figure\_**matplotlib Figure

Figure containing the curve.

See also

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute error rates for different probability thresholds.

[`DetCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")

Plot DET curve given an estimator and some data.

[`DetCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")

Plot DET curve given the true and predicted labels.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import det\_curve, DetCurveDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(n\_samples\=1000, random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, test\_size\=0.4, random\_state\=0)
\>>> clf \= SVC(random\_state\=0).fit(X\_train, y\_train)
\>>> y\_score \= clf.decision\_function(X\_test)
\>>> fpr, fnr, \_ \= det\_curve(y\_test, y\_score)
\>>> display \= DetCurveDisplay(
...     fpr\=fpr, fnr\=fnr, estimator\_name\="SVC"
... )
\>>> display.plot()
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-DetCurveDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-metrics-DetCurveDisplay-1.png)

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=True_, _response\_method\='auto'_, _pos\_label\=None_, _name\=None_, _ax\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/det_curve.py#L89)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "Link to this definition")

Plot DET curve given an estimator and data.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#det-curve)
.

Added in version 1.0.

Parameters:

**estimator**estimator instance

Fitted classifier or a fitted [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 in which the last estimator is a classifier.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input values.

**y**array-like of shape (n\_samples,)

Target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=True

Whether to drop thresholds where true positives (tp) do not change from the previous or subsequent threshold. All points with the same tp value have the same `fnr` and thus same y coordinate.

Added in version 1.7.

**response\_method**{‘predict\_proba’, ‘decision\_function’, ‘auto’} default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the predicted target response. If set to ‘auto’, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and if it does not exist [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 is tried next.

**pos\_label**int, float, bool or str, default=None

The label of the positive class. By default, `estimators.classes_[1]` is considered as the positive class.

**name**str, default=None

Name of DET curve for labeling. If `None`, use the name of the estimator.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**\*\*kwargs**dict

Additional keywords arguments passed to matplotlib `plot` function.

Returns:

**display**[`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")

Object that stores computed values.

See also

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute error rates for different probability thresholds.

[`DetCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")

Plot DET curve given the true and predicted labels.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import DetCurveDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(n\_samples\=1000, random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, test\_size\=0.4, random\_state\=0)
\>>> clf \= SVC(random\_state\=0).fit(X\_train, y\_train)
\>>> DetCurveDisplay.from\_estimator(
...    clf, X\_test, y\_test)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-DetCurveDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-metrics-DetCurveDisplay-2.png)

classmethod from\_predictions(_y\_true_, _y\_score\=None_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=True_, _pos\_label\=None_, _name\=None_, _ax\=None_, _y\_pred\='deprecated'_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/det_curve.py#L204)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "Link to this definition")

Plot the DET curve given the true and predicted labels.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#det-curve)
.

Added in version 1.0.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True labels.

**y\_score**array-like of shape (n\_samples,)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers).

Added in version 1.8: `y_pred` has been renamed to `y_score`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=True

Whether to drop thresholds where true positives (tp) do not change from the previous or subsequent threshold. All points with the same tp value have the same `fnr` and thus same y coordinate.

Added in version 1.7.

**pos\_label**int, float, bool or str, default=None

The label of the positive class. When `pos_label=None`, if `y_true` is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

**name**str, default=None

Name of DET curve for labeling. If `None`, name will be set to `"Classifier"`.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**y\_pred**array-like of shape (n\_samples,)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers).

Deprecated since version 1.8: `y_pred` is deprecated and will be removed in 1.10. Use `y_score` instead.

**\*\*kwargs**dict

Additional keywords arguments passed to matplotlib `plot` function.

Returns:

**display**[`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")

Object that stores computed values.

See also

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute error rates for different probability thresholds.

[`DetCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")

Plot DET curve given an estimator and some data.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import DetCurveDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(n\_samples\=1000, random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, test\_size\=0.4, random\_state\=0)
\>>> clf \= SVC(random\_state\=0).fit(X\_train, y\_train)
\>>> y\_score \= clf.decision\_function(X\_test)
\>>> DetCurveDisplay.from\_predictions(
...    y\_test, y\_score)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-DetCurveDisplay-3.png](https://scikit-learn.org/stable/_images/sklearn-metrics-DetCurveDisplay-3.png)

plot(_ax\=None_, _\*_, _name\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/det_curve.py#L325)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.plot "Link to this definition")

Plot visualization.

Parameters:

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**name**str, default=None

Name of DET curve for labeling. If `None`, use `estimator_name` if it is not `None`, otherwise no labeling is shown.

**\*\*kwargs**dict

Additional keywords arguments passed to matplotlib `plot` function.

Returns:

**display**[`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")

Object that stores computed values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)