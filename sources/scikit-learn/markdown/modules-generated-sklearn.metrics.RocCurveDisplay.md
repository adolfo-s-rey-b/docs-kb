[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.RocCurveDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.RocCurveDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.RocCurveDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.RocCurveDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.RocCurveDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.RocCurveDisplay.html)

Collapse Sidebar Expand Sidebar

RocCurveDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#roccurvedisplay "Link to this heading")

==================================================================================================================================================

class sklearn.metrics.RocCurveDisplay(_\*_, _fpr_, _tpr_, _roc\_auc\=None_, _name\=None_, _pos\_label\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/roc_curve.py#L17)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "Link to this definition")

ROC Curve visualization.

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
 or [`from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")
 to create a [`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
. All parameters are stored as attributes.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

Parameters:

**fpr**ndarray or list of ndarrays

False positive rates. Each ndarray should contain values for a single curve. If plotting multiple curves, list should be of same length as `tpr`.

Changed in version 1.7: Now accepts a list for plotting multiple curves.

**tpr**ndarray or list of ndarrays

True positive rates. Each ndarray should contain values for a single curve. If plotting multiple curves, list should be of same length as `fpr`.

Changed in version 1.7: Now accepts a list for plotting multiple curves.

**roc\_auc**float or list of floats, default=None

Area under ROC curve, used for labeling each curve in the legend. If plotting multiple curves, should be a list of the same length as `fpr` and `tpr`. If `None`, ROC AUC scores are not shown in the legend.

Changed in version 1.7: Now accepts a list for plotting multiple curves.

**name**str or list of str, default=None

Name for labeling legend entries. The number of legend entries is determined by the `curve_kwargs` passed to `plot`, and is not affected by `name`.

If a string is provided, it will be used to either label the single legend entry or if there are multiple legend entries, label each individual curve with the same name.

If a list is provided, it will be used to label each curve individually. Passing a list will raise an error if `curve_kwargs` is not a list to avoid labeling individual curves that have the same appearance.

If `None`, no name is shown in the legend.

Changed in version 1.7: `estimator_name` was deprecated in favor of `name` and now accepts a list for plotting multiple curves.

**pos\_label**int, float, bool or str, default=None

The class considered the positive class when ROC AUC metrics computed. If not `None`, this value is displayed in the x- and y-axes labels.

Added in version 0.24.

Attributes:

**line\_**matplotlib Artist or list of matplotlib Artists

ROC Curves.

Changed in version 1.7: This attribute can now be a list of Artists, for when multiple curves are plotted.

**chance\_level\_**matplotlib Artist or None

The chance level line. It is `None` if the chance level is not plotted.

Added in version 1.3.

**ax\_**matplotlib Axes

Axes with ROC Curve.

**figure\_**matplotlib Figure

Figure containing the curve.

See also

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")

Plot Receiver Operating Characteristic (ROC) curve given an estimator and some data.

[`RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")

Plot Receiver Operating Characteristic (ROC) curve given the true and predicted values.

[`RocCurveDisplay.from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")

Plot multi-fold ROC curves given cross-validation results.

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

Examples

\>>> import matplotlib.pyplot as plt
\>>> import numpy as np
\>>> from sklearn import metrics
\>>> y\_true \= np.array(\[0, 0, 1, 1\])
\>>> y\_score \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> fpr, tpr, thresholds \= metrics.roc\_curve(y\_true, y\_score)
\>>> roc\_auc \= metrics.auc(fpr, tpr)
\>>> display \= metrics.RocCurveDisplay(fpr\=fpr, tpr\=tpr, roc\_auc\=roc\_auc,
...                                   name\='example estimator')
\>>> display.plot()
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-RocCurveDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-metrics-RocCurveDisplay-1.png)

classmethod from\_cv\_results(_cv\_results_, _X_, _y_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=True_, _response\_method\='auto'_, _pos\_label\=None_, _ax\=None_, _name\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kwargs\=None_, _despine\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/roc_curve.py#L575)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "Link to this definition")

Create a multi-fold ROC curve display given cross-validation results.

Added in version 1.7.

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

Whether to drop some suboptimal thresholds which would not appear on a plotted ROC curve. This is useful in order to create lighter ROC curves.

**response\_method**{‘predict\_proba’, ‘decision\_function’, ‘auto’} default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the target response. If set to ‘auto’, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and if it does not exist [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 is tried next.

**pos\_label**int, float, bool or str, default=None

The class considered as the positive class when computing the ROC AUC metrics. By default, `estimator.classes_[1]` (using `estimator` from `cv_results`) is considered as the positive class.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**name**str or list of str, default=None

Name for labeling legend entries. The number of legend entries is determined by the `curve_kwargs` passed to `plot`, and is not affected by `name`.

If a string is provided, it will be used to either label the single legend entry or if there are multiple legend entries, label each individual curve with the same name.

If a list is provided, it will be used to label each curve individually. Passing a list will raise an error if `curve_kwargs` is not a list to avoid labeling individual curves that have the same appearance.

If `None`, no name is shown in the legend.

**curve\_kwargs**dict or list of dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function to draw individual ROC curves. If a list is provided the parameters are applied to the ROC curves of each CV fold sequentially and a legend entry is added for each curve. If a single dictionary is provided, the same parameters are applied to all ROC curves and a single legend entry for all curves is added, labeled with the mean ROC AUC score.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level.

**chance\_level\_kwargs**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Returns:

**display**[`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")

The multi-fold ROC curve display.

See also

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")

Plot Receiver Operating Characteristic (ROC) curve given an estimator and some data.

[`RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")

ROC Curve visualization given the probabilities of scores of a classifier.

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import RocCurveDisplay
\>>> from sklearn.model\_selection import cross\_validate
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> clf \= SVC(random\_state\=0)
\>>> cv\_results \= cross\_validate(
...     clf, X, y, cv\=3, return\_estimator\=True, return\_indices\=True)
\>>> RocCurveDisplay.from\_cv\_results(cv\_results, X, y)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-RocCurveDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-metrics-RocCurveDisplay-2.png)

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=True_, _response\_method\='auto'_, _pos\_label\=None_, _name\=None_, _ax\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kw\=None_, _despine\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/roc_curve.py#L296)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "Link to this definition")

Create a ROC Curve display from an estimator.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
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

**drop\_intermediate**bool, default=True

Whether to drop thresholds where the resulting point is collinear with its neighbors in ROC space. This has no effect on the ROC AUC or visual shape of the curve, but reduces the number of plotted points.

**response\_method**{‘predict\_proba’, ‘decision\_function’, ‘auto’} default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the target response. If set to ‘auto’, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and if it does not exist [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 is tried next.

**pos\_label**int, float, bool or str, default=None

The class considered as the positive class when computing the ROC AUC. By default, `estimators.classes_[1]` is considered as the positive class.

**name**str, default=None

Name of ROC Curve for labeling. If `None`, use the name of the estimator.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**curve\_kwargs**dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function.

Added in version 1.7.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level.

Added in version 1.3.

**chance\_level\_kw**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

Added in version 1.3.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Added in version 1.6.

Returns:

**display**[`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")

The ROC Curve display.

See also

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")

ROC Curve visualization given the probabilities of scores of a classifier.

[`RocCurveDisplay.from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")

Plot multi-fold ROC curves given cross-validation results.

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import RocCurveDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=0)
\>>> clf \= SVC(random\_state\=0).fit(X\_train, y\_train)
\>>> RocCurveDisplay.from\_estimator(
...    clf, X\_test, y\_test)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-RocCurveDisplay-3.png](https://scikit-learn.org/stable/_images/sklearn-metrics-RocCurveDisplay-3.png)

classmethod from\_predictions(_y\_true_, _y\_score\=None_, _\*_, _sample\_weight\=None_, _drop\_intermediate\=True_, _pos\_label\=None_, _name\=None_, _ax\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kw\=None_, _despine\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/roc_curve.py#L435)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "Link to this definition")

Plot ROC curve given the true and predicted values.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

Added in version 1.0.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True labels.

**y\_score**array-like of shape (n\_samples,)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers).

Added in version 1.7: `y_pred` has been renamed to `y_score`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=True

Whether to drop thresholds where the resulting point is collinear with its neighbors in ROC space. This has no effect on the ROC AUC or visual shape of the curve, but reduces the number of plotted points.

**pos\_label**int, float, bool or str, default=None

The label of the positive class when computing the ROC AUC. When `pos_label=None`, if `y_true` is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

**name**str, default=None

Name of ROC curve for legend labeling. If `None`, name will be set to `"Classifier"`.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**curve\_kwargs**dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function.

Added in version 1.7.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level.

Added in version 1.3.

**chance\_level\_kw**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

Added in version 1.3.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Added in version 1.6.

Returns:

**display**[`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")

Object that stores computed values.

See also

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")

ROC Curve visualization given an estimator and some data.

[`RocCurveDisplay.from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")

Plot multi-fold ROC curves given cross-validation results.

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import RocCurveDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, random\_state\=0)
\>>> clf \= SVC(random\_state\=0).fit(X\_train, y\_train)
\>>> y\_score \= clf.decision\_function(X\_test)
\>>> RocCurveDisplay.from\_predictions(y\_test, y\_score)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-RocCurveDisplay-4.png](https://scikit-learn.org/stable/_images/sklearn-metrics-RocCurveDisplay-4.png)

plot(_ax\=None_, _\*_, _name\=None_, _curve\_kwargs\=None_, _plot\_chance\_level\=False_, _chance\_level\_kw\=None_, _despine\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/roc_curve.py#L160)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.plot "Link to this definition")

Plot visualization.

Parameters:

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**name**str or list of str, default=None

Name for labeling legend entries. The number of legend entries is determined by the `curve_kwargs` passed to `plot`, and is not affected by `name`.

If a string is provided, it will be used to either label the single legend entry or if there are multiple legend entries, label each individual curve with the same name.

If a list is provided, it will be used to label each curve individually. Passing a list will raise an error if `curve_kwargs` is not a list to avoid labeling individual curves that have the same appearance.

If `None`, set to `name` provided at `RocCurveDisplay` initialization. If still `None`, no name is shown in the legend.

Added in version 1.7.

**curve\_kwargs**dict or list of dict, default=None

Keywords arguments to be passed to matplotlib’s `plot` function to draw individual ROC curves. For single curve plotting, should be a dictionary. For multi-curve plotting, if a list is provided the parameters are applied to the ROC curves of each CV fold sequentially and a legend entry is added for each curve. If a single dictionary is provided, the same parameters are applied to all ROC curves and a single legend entry for all curves is added, labeled with the mean ROC AUC score.

Added in version 1.7.

**plot\_chance\_level**bool, default=False

Whether to plot the chance level.

Added in version 1.3.

**chance\_level\_kw**dict, default=None

Keyword arguments to be passed to matplotlib’s `plot` for rendering the chance level line.

Added in version 1.3.

**despine**bool, default=False

Whether to remove the top and right spines from the plot.

Added in version 1.6.

Returns:

**display**[`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")

Object that stores computed values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_thumb.png)

[ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

ROC Curve with Visualization API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)