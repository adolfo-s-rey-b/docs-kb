[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.calibration.CalibrationDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.calibration.CalibrationDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.calibration.CalibrationDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.calibration.CalibrationDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.calibration.CalibrationDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.calibration.CalibrationDisplay.html)

Collapse Sidebar Expand Sidebar

CalibrationDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#calibrationdisplay "Link to this heading")

===============================================================================================================================================================

class sklearn.calibration.CalibrationDisplay(_prob\_true_, _prob\_pred_, _y\_prob_, _\*_, _estimator\_name\=None_, _pos\_label\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L1345)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "Link to this definition")

Calibration curve (also known as reliability diagram) visualization.

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")
 to create a `CalibrationDisplay`. All parameters are stored as attributes.

Read more about calibration in the [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
 and more about the scikit-learn visualization API in [Visualizations](https://scikit-learn.org/stable/visualizations.html#visualizations)
.

For an example on how to use the visualization, see [Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#sphx-glr-auto-examples-calibration-plot-calibration-curve-py)
.

Added in version 1.0.

Parameters:

**prob\_true**ndarray of shape (n\_bins,)

The proportion of samples whose class is the positive class (fraction of positives), in each bin.

**prob\_pred**ndarray of shape (n\_bins,)

The mean predicted probability in each bin.

**y\_prob**ndarray of shape (n\_samples,)

Probability estimates for the positive class, for each sample.

**estimator\_name**str, default=None

Name of estimator. If None, the estimator name is not shown.

**pos\_label**int, float, bool or str, default=None

The positive class when calibration curve computed. If not `None`, this value is displayed in the x- and y-axes labels.

Added in version 1.1.

Attributes:

**line\_**matplotlib Artist

Calibration curve.

**ax\_**matplotlib Axes

Axes with calibration curve.

**figure\_**matplotlib Figure

Figure containing the curve.

See also

[`calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")

Compute true and predicted probabilities for a calibration curve.

[`CalibrationDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")

Plot calibration curve using true and predicted labels.

[`CalibrationDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")

Plot calibration curve using an estimator and data.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.calibration import calibration\_curve, CalibrationDisplay
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=0)
\>>> clf \= LogisticRegression(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
LogisticRegression(random\_state=0)
\>>> y\_prob \= clf.predict\_proba(X\_test)\[:, 1\]
\>>> prob\_true, prob\_pred \= calibration\_curve(y\_test, y\_prob, n\_bins\=10)
\>>> disp \= CalibrationDisplay(prob\_true, prob\_pred, y\_prob)
\>>> disp.plot()
<...>

Copy to clipboard

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _n\_bins\=5_, _strategy\='uniform'_, _pos\_label\=None_, _name\=None_, _ax\=None_, _ref\_line\=True_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L1484)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "Link to this definition")

Plot calibration curve using a binary classifier and data.

A calibration curve, also known as a reliability diagram, uses inputs from a binary classifier and plots the average predicted probability for each bin against the fraction of positive classes, on the y-axis.

Extra keyword arguments will be passed to [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.1)")
.

Read more about calibration in the [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
 and more about the scikit-learn visualization API in [Visualizations](https://scikit-learn.org/stable/visualizations.html#visualizations)
.

Added in version 1.0.

Parameters:

**estimator**estimator instance

Fitted classifier or a fitted [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 in which the last estimator is a classifier. The classifier must have a [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 method.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input values.

**y**array-like of shape (n\_samples,)

Binary target values.

**n\_bins**int, default=5

Number of bins to discretize the \[0, 1\] interval into when calculating the calibration curve. A bigger number requires more data.

**strategy**{‘uniform’, ‘quantile’}, default=’uniform’

Strategy used to define the widths of the bins.

*   `'uniform'`: The bins have identical widths.
    
*   `'quantile'`: The bins have the same number of samples and depend on predicted probabilities.
    

**pos\_label**int, float, bool or str, default=None

The positive class when computing the calibration curve. By default, `estimators.classes_[1]` is considered as the positive class.

Added in version 1.1.

**name**str, default=None

Name for labeling curve. If `None`, the name of the estimator is used.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**ref\_line**bool, default=True

If `True`, plots a reference line representing a perfectly calibrated classifier.

**\*\*kwargs**dict

Keyword arguments to be passed to [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.1)")
.

Returns:

**display**[`CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
.

Object that stores computed values.

See also

[`CalibrationDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")

Plot calibration curve using true and predicted labels.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.calibration import CalibrationDisplay
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=0)
\>>> clf \= LogisticRegression(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
LogisticRegression(random\_state=0)
\>>> disp \= CalibrationDisplay.from\_estimator(clf, X\_test, y\_test)
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-calibration-CalibrationDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-calibration-CalibrationDisplay-1.png)

classmethod from\_predictions(_y\_true_, _y\_prob_, _\*_, _n\_bins\=5_, _strategy\='uniform'_, _pos\_label\=None_, _name\=None_, _ax\=None_, _ref\_line\=True_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L1608)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "Link to this definition")

Plot calibration curve using true labels and predicted probabilities.

Calibration curve, also known as reliability diagram, uses inputs from a binary classifier and plots the average predicted probability for each bin against the fraction of positive classes, on the y-axis.

Extra keyword arguments will be passed to [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.1)")
.

Read more about calibration in the [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
 and more about the scikit-learn visualization API in [Visualizations](https://scikit-learn.org/stable/visualizations.html#visualizations)
.

Added in version 1.0.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True labels.

**y\_prob**array-like of shape (n\_samples,)

The predicted probabilities of the positive class.

**n\_bins**int, default=5

Number of bins to discretize the \[0, 1\] interval into when calculating the calibration curve. A bigger number requires more data.

**strategy**{‘uniform’, ‘quantile’}, default=’uniform’

Strategy used to define the widths of the bins.

*   `'uniform'`: The bins have identical widths.
    
*   `'quantile'`: The bins have the same number of samples and depend on predicted probabilities.
    

**pos\_label**int, float, bool or str, default=None

The positive class when computing the calibration curve. When `pos_label=None`, if `y_true` is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

Added in version 1.1.

**name**str, default=None

Name for labeling curve.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**ref\_line**bool, default=True

If `True`, plots a reference line representing a perfectly calibrated classifier.

**\*\*kwargs**dict

Keyword arguments to be passed to [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.1)")
.

Returns:

**display**[`CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
.

Object that stores computed values.

See also

[`CalibrationDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")

Plot calibration curve using an estimator and data.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.calibration import CalibrationDisplay
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=0)
\>>> clf \= LogisticRegression(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
LogisticRegression(random\_state=0)
\>>> y\_prob \= clf.predict\_proba(X\_test)\[:, 1\]
\>>> disp \= CalibrationDisplay.from\_predictions(y\_test, y\_prob)
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-calibration-CalibrationDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-calibration-CalibrationDisplay-2.png)

plot(_\*_, _ax\=None_, _name\=None_, _ref\_line\=True_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L1430)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.plot "Link to this definition")

Plot visualization.

Extra keyword arguments will be passed to [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.1)")
.

Parameters:

**ax**Matplotlib Axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**name**str, default=None

Name for labeling curve. If `None`, use `estimator_name` if not `None`, otherwise no labeling is shown.

**ref\_line**bool, default=True

If `True`, plots a reference line representing a perfectly calibrated classifier.

**\*\*kwargs**dict

Keyword arguments to be passed to [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.1)")
.

Returns:

**display**[`CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")

Object that stores computed values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_thumb.png)

[Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html)

Release Highlights for scikit-learn 1.8

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)