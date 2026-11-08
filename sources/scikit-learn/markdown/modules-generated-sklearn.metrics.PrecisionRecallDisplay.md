[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html)

Collapse Sidebar Expand Sidebar

PrecisionRecallDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#precisionrecalldisplay "Link to this heading")

=======================================================================================================================================================================

class sklearn.metrics.PrecisionRecallDisplay(_precision_, _recall_, _\*_, _average\_precision\=None_, _name\=None_, _pos\_label\=None_, _prevalence\_pos\_label\=None_, _estimator\_name\='deprecated'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/precision_recall_curve.py#L20)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "Link to this definition")

Precision Recall visualization.

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
 to create a [`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
. All parameters are stored as attributes.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**precision**ndarray or list of ndarrays

Precision values. Each ndarray should contain values for a single curve. If plotting multiple curves, list should be of same length as `recall`.

Changed in version 1.9: Now accepts a list for plotting multiple curves.

**recall**ndarray or list of ndarrays

Recall values. Each ndarray should contain values for a single curve. If plotting multiple curves, list should be of same length as `precision`.

Changed in version 1.9: Now accepts a list for plotting multiple curves.

**average\_precision**float or list of floats, default=None

Average precision, used for labeling each curve in the legend. If plotting multiple curves, should be a list of the same length as `precision` and `recall`. If `None`, average precision values are not shown in the legend.

Changed in version 1.9: Now accepts a list for plotting multiple curves.

**name**str or list of str, default=None

Name for labeling legend entries. The number of legend entries is determined by the `curve_kwargs` passed to `plot`, and is not affected by `name`.

If a string is provided, it will be used to either label the single legend entry or if there are multiple legend entries, label each individual curve with the same name.

If a list is provided, it will be used to label each curve individually. Passing a list will raise an error if `curve_kwargs` is not a list to avoid labeling individual curves that have the same appearance.

If `None`, no name is shown in the legend.

Changed in version 1.8: `estimator_name` was deprecated in favor of `name`.

Changed in version 1.9: `name` can now take a list of str for multiple curves.

**pos\_label**int, float, bool or str, default=None

The class considered the positive class when precision and recall metrics computed. If not `None`, this value is displayed in the x- and y-axes labels.

Added in version 0.24.

**prevalence\_pos\_label**float or list of floats, default=None

The prevalence of the positive label. It is used for plotting the chance level lines. If None, no chance level line will be plotted even if `plot_chance_level` is set to True when plotting.

Added in version 1.3.

Changed in version 1.9: May now be list of floats for when multiple curves plotted.

**estimator\_name**str, default=None

Name of estimator. If None, the estimator name is not shown.

Deprecated since version 1.8: `estimator_name` is deprecated and will be removed in 1.10. Use `name` instead.

Attributes:

**line\_**matplotlib Artist or list of Artists

Precision recall curve(s).

Changed in version 1.9: This attribute can now be a list of Artists, for when multiple curves are plotted.

**chance\_level\_**matplotlib Artist or list of Artists or None

Chance level line(s). It is `None` if the chance level is not plotted.

Added in version 1.3.

Changed in version 1.9: This attribute can now be a list of Artists, for when multiple curves are plotted.

**ax\_**matplotlib Axes

Axes with precision recall curve.

**figure\_**matplotlib Figure

Figure containing the curve.

See also

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall pairs for different probability thresholds.

[`PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")

Plot Precision Recall Curve given a binary classifier.

[`PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")

Plot Precision Recall Curve using predictions from a binary classifier.

Notes

The average precision (cf. [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
) in scikit-learn is computed without any interpolation. To be consistent with this metric, the precision-recall curve is plotted without any interpolation as well (step-wise style).

To enable interpolation, pass `curve_kwargs={"drawstyle": "default"}` to meth:`plot`, [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
, or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
. However, the curve will not be strictly consistent with the reported average precision.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import (precision\_recall\_curve,
...                              PrecisionRecallDisplay)
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y,
...                                                     random\_state\=0)
\>>> clf \= SVC(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
SVC(random\_state=0)
\>>> predictions \= clf.predict(X\_test)
\>>> precision, recall, \_ \= precision\_recall\_curve(y\_test, predictions)
\>>> disp \= PrecisionRecallDisplay(precision\=precision, recall\=recall)
\>>> disp.plot()
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PrecisionRecallDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PrecisionRecallDisplay-1.png)

classmethod from\_cv\_results(_cv\_results_, _X_, _y_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=True_, _response\_method\='auto'_, _pos\_label\=None_, _name\=None_, _ax\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kwargs\=None_, _despine\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/precision_recall_curve.py#L737)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_cv_results "Link to this definition")

Plot multi-fold precision-recall curves given cross-validation results.

Added in version 1.9.

Parameters:

**cv\_results**dict

Dictionary as returned by [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 using `return_estimator=True` and `return_indices=True` (i.e., dictionary should contain the keys “estimator” and “indices”).

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input values.

**y**array-like of shape (n\_samples,)

Target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=True

Whether to drop some suboptimal thresholds which would not appear on a plotted precision-recall curve. This is useful in order to create lighter precision-recall curves.

**response\_method**{‘predict\_proba’, ‘decision\_function’, ‘auto’} default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the target response. If set to ‘auto’, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and if it does not exist [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 is tried next.

**pos\_label**int, float, bool or str, default=None

The class considered as the positive class when computing the precision and recall metrics. By default, `estimators.classes_[1]` is considered as the positive class.

**name**str or list of str, default=None

Name for labeling legend entries. The number of legend entries is determined by `curve_kwargs`, and is not affected by `name`.

If a string is provided, it will be used to either label the single legend entry or if there are multiple legend entries, label each individual curve with the same name.

If a list is provided, it will be used to label each curve individually. Passing a list will raise an error if `curve_kwargs` is not a list to avoid labeling individual curves that have the same appearance.

If `None`, no name is shown in the legend.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**curve\_kwargs**dict or list of dict, default=None

Dictionary with keywords passed to the matplotlib’s `plot` function to draw the individual precision-recall curves. If a list is provided, the parameters are applied to the precision-recall curves of each CV fold sequentially. If a single dictionary is provided, the same parameters are applied to all precision-recall curves.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level lines.

**chance\_level\_kwargs**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level lines.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Returns:

**display**[`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")

See also

[`PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")

Plot precision-recall curve using estimated probabilities or output of decision function.

[`PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")

Plot precision-recall curve using an estimator.

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall pairs for different probability thresholds.

[`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")

Compute average precision (AP) from prediction scores.

Notes

The average precision (cf. [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
) in scikit-learn is computed without any interpolation. To be consistent with this metric, the precision-recall curve is plotted without any interpolation as well (step-wise style).

To enable interpolation, pass `curve_kwargs={"drawstyle": "default"}`. However, the curve will not be strictly consistent with the reported average precision.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import PrecisionRecallDisplay
\>>> from sklearn.model\_selection import cross\_validate
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> clf \= SVC(random\_state\=0)
\>>> cv\_results \= cross\_validate(
...     clf, X, y, cv\=3, return\_estimator\=True, return\_indices\=True)
\>>> PrecisionRecallDisplay.from\_cv\_results(cv\_results, X, y)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PrecisionRecallDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PrecisionRecallDisplay-2.png)

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=False_, _response\_method\='auto'_, _pos\_label\=None_, _name\=None_, _ax\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kw\=None_, _despine\=False_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/precision_recall_curve.py#L405)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "Link to this definition")

Plot precision-recall curve given an estimator and some data.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

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

**drop\_intermediate**bool, default=False

Whether to drop some suboptimal thresholds which would not appear on a plotted precision-recall curve. This is useful in order to create lighter precision-recall curves.

Added in version 1.3.

**response\_method**{‘predict\_proba’, ‘decision\_function’, ‘auto’}, default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the target response. If set to ‘auto’, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and if it does not exist [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 is tried next.

**pos\_label**int, float, bool or str, default=None

The class considered as the positive class when computing the precision and recall metrics. By default, `estimators.classes_[1]` is considered as the positive class.

**name**str, default=None

Name for labeling curve. If `None`, no name is used.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**curve\_kwargs**dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function.

Added in version 1.9.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level. The chance level is the prevalence of the positive label computed from the data passed during [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
 call.

Added in version 1.3.

**chance\_level\_kw**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

Added in version 1.3.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Added in version 1.6.

**\*\*kwargs**dict

Keyword arguments to be passed to matplotlib’s `plot`.

Deprecated since version 1.9: kwargs is deprecated and will be removed in 1.11. Pass matplotlib arguments to `curve_kwargs` as a dictionary instead.

Returns:

**display**[`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")

See also

[`PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")

Plot precision-recall curve using estimated probabilities or output of decision function.

Notes

The average precision (cf. [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
) in scikit-learn is computed without any interpolation. To be consistent with this metric, the precision-recall curve is plotted without any interpolation as well (step-wise style).

To enable interpolation, pass `curve_kwargs={"drawstyle": "default"}`. However, the curve will not be strictly consistent with the reported average precision.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import PrecisionRecallDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...         X, y, random\_state\=0)
\>>> clf \= LogisticRegression()
\>>> clf.fit(X\_train, y\_train)
LogisticRegression()
\>>> PrecisionRecallDisplay.from\_estimator(
...    clf, X\_test, y\_test)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PrecisionRecallDisplay-3.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PrecisionRecallDisplay-3.png)

classmethod from\_predictions(_y\_true_, _y\_score\=None_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=False_, _pos\_label\=None_, _name\=None_, _ax\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kw\=None_, _despine\=False_, _y\_pred\='deprecated'_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/precision_recall_curve.py#L563)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "Link to this definition")

Plot precision-recall curve given binary class predictions.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True binary labels.

**y\_score**array-like of shape (n\_samples,)

Estimated probabilities or output of decision function.

Added in version 1.8: `y_pred` has been renamed to `y_score`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=False

Whether to drop some suboptimal thresholds which would not appear on a plotted precision-recall curve. This is useful in order to create lighter precision-recall curves.

Added in version 1.3.

**pos\_label**int, float, bool or str, default=None

The class considered as the positive class when computing the precision and recall metrics. When `pos_label=None`, if `y_true` is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

**name**str, default=None

Name for labeling curve. If `None`, name will be set to `"Classifier"`.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**curve\_kwargs**dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function.

Added in version 1.9.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level. The chance level is the prevalence of the positive label computed from the data passed during [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
 call.

Added in version 1.3.

**chance\_level\_kw**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

Added in version 1.3.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Added in version 1.6.

**y\_pred**array-like of shape (n\_samples,)

Estimated probabilities or output of decision function.

Deprecated since version 1.8: `y_pred` is deprecated and will be removed in 1.10. Use `y_score` instead.

**\*\*kwargs**dict

Keyword arguments to be passed to matplotlib’s `plot`.

Deprecated since version 1.9: kwargs is deprecated and will be removed in 1.11. Pass matplotlib arguments to `curve_kwargs` as a dictionary instead.

Returns:

**display**[`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")

See also

[`PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")

Plot precision-recall curve using an estimator.

Notes

The average precision (cf. [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
) in scikit-learn is computed without any interpolation. To be consistent with this metric, the precision-recall curve is plotted without any interpolation as well (step-wise style).

To enable interpolation, pass `curve_kwargs={"drawstyle": "default"}`. However, the curve will not be strictly consistent with the reported average precision.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import PrecisionRecallDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...         X, y, random\_state\=0)
\>>> clf \= LogisticRegression()
\>>> clf.fit(X\_train, y\_train)
LogisticRegression()
\>>> y\_score \= clf.predict\_proba(X\_test)\[:, 1\]
\>>> PrecisionRecallDisplay.from\_predictions(
...    y\_test, y\_score)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PrecisionRecallDisplay-4.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PrecisionRecallDisplay-4.png)

plot(_ax\=None_, _\*_, _name\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kw\=None_, _despine\=False_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/precision_recall_curve.py#L208)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.plot "Link to this definition")

Plot visualization.

Parameters:

**ax**Matplotlib Axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**name**str or list of str, default=None

Name for labeling legend entries. The number of legend entries is determined by `curve_kwargs`, and is not affected by `name`.

If a string is provided, it will be used to either label the single legend entry or if there are multiple legend entries, label each individual curve with the same name.

If a list is provided, it will be used to label each curve individually. Passing a list will raise an error if `curve_kwargs` is not a list to avoid labeling individual curves that have the same appearance.

If `None`, set to `name` provided at `PrecisionRecallDisplay` initialization. If still `None`, no name is shown in the legend.

Changed in version 1.9: Now accepts a list for plotting multiple curves.

**curve\_kwargs**dict or list of dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function to draw individual precision-recall curves. For single curve plotting, this should be a dictionary. For multi-curve plotting, if a list is provided, the parameters are applied to each precision-recall curve sequentially and a legend entry is added for each curve. If a single dictionary is provided, the same parameters are applied to all curves and a single legend entry for all curves is added, labeled with the mean average precision.

Added in version 1.9.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level. The chance level is the prevalence of the positive label computed from the data passed during [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
 call.

Added in version 1.3.

**chance\_level\_kw**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

Added in version 1.3.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Added in version 1.6.

**\*\*kwargs**dict

Keyword arguments to be passed to matplotlib’s `plot`.

Deprecated since version 1.9: kwargs is deprecated and will be removed in 1.11. Pass matplotlib arguments to `curve_kwargs` as a dictionary instead.

Returns:

**display**[`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")

Object that stores computed values.

Notes

The average precision (cf. [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
) in scikit-learn is computed without any interpolation. To be consistent with this metric, the precision-recall curve is plotted without any interpolation as well (step-wise style).

To enable interpolation, pass `curve_kwargs={"drawstyle": "default"}`. However, the curve will not be strictly consistent with the reported average precision.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)