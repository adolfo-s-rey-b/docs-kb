[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)

Collapse Sidebar Expand Sidebar

ConfusionMatrixDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#confusionmatrixdisplay "Link to this heading")

=======================================================================================================================================================================

class sklearn.metrics.ConfusionMatrixDisplay(_confusion\_matrix_, _\*_, _display\_labels\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/confusion_matrix.py#L15)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "Link to this definition")

Confusion Matrix visualization.

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
 to create a [`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")
. All parameters are stored as attributes.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
.

Parameters:

**confusion\_matrix**ndarray of shape (n\_classes, n\_classes)

Confusion matrix.

**display\_labels**ndarray of shape (n\_classes,), default=None

Display labels for plot. If None, display labels are set from 0 to `n_classes - 1`.

Attributes:

**im\_**matplotlib AxesImage

Image representing the confusion matrix.

**text\_**ndarray of shape (n\_classes, n\_classes), dtype=matplotlib Text, or None

Array of matplotlib axes. `None` if `include_values` is false.

**ax\_**matplotlib Axes

Axes with confusion matrix.

**figure\_**matplotlib Figure

Figure containing the confusion matrix.

See also

[`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")

Compute Confusion Matrix to evaluate the accuracy of a classification.

[`ConfusionMatrixDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")

Plot the confusion matrix given an estimator, the data, and the label.

[`ConfusionMatrixDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")

Plot the confusion matrix given the true and predicted labels.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import confusion\_matrix, ConfusionMatrixDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y,
...                                                     random\_state\=0)
\>>> clf \= SVC(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
SVC(random\_state=0)
\>>> predictions \= clf.predict(X\_test)
\>>> cm \= confusion\_matrix(y\_test, predictions, labels\=clf.classes\_)
\>>> disp \= ConfusionMatrixDisplay(confusion\_matrix\=cm,
...                               display\_labels\=clf.classes\_)
\>>> disp.plot()
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-ConfusionMatrixDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-metrics-ConfusionMatrixDisplay-1.png)

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _labels\=None_, _sample\_weight\=None_, _normalize\=None_, _display\_labels\=None_, _include\_values\=True_, _xticks\_rotation\='horizontal'_, _values\_format\=None_, _cmap\='viridis'_, _ax\=None_, _colorbar\=True_, _im\_kw\=None_, _text\_kw\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/confusion_matrix.py#L204)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "Link to this definition")

Plot Confusion Matrix given an estimator and some data.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
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

**labels**array-like of shape (n\_classes,), default=None

List of labels to index the confusion matrix. This may be used to reorder or select a subset of labels. If `None` is given, those that appear at least once in `y_true` or `y_pred` are used in sorted order.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**normalize**{‘true’, ‘pred’, ‘all’}, default=None

Either to normalize the counts display in the matrix:

*   if `'true'`, the confusion matrix is normalized over the true conditions (e.g. rows);
    
*   if `'pred'`, the confusion matrix is normalized over the predicted conditions (e.g. columns);
    
*   if `'all'`, the confusion matrix is normalized by the total number of samples;
    
*   if `None` (default), the confusion matrix will not be normalized.
    

**display\_labels**array-like of shape (n\_classes,), default=None

Target names used for plotting. By default, `labels` will be used if it is defined, otherwise the unique labels of `y_true` and `y_pred` will be used.

**include\_values**bool, default=True

Includes values in confusion matrix.

**xticks\_rotation**{‘vertical’, ‘horizontal’} or float, default=’horizontal’

Rotation of xtick labels.

**values\_format**str, default=None

Format specification for values in confusion matrix. If `None`, the format specification is ‘d’ or ‘.2g’ whichever is shorter.

**cmap**str or matplotlib Colormap, default=’viridis’

Colormap recognized by matplotlib.

**ax**matplotlib Axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**colorbar**bool, default=True

Whether or not to add a colorbar to the plot.

**im\_kw**dict, default=None

Dict with keywords passed to `matplotlib.pyplot.imshow` call.

**text\_kw**dict, default=None

Dict with keywords passed to `matplotlib.pyplot.text` call.

Added in version 1.2.

Returns:

**display**[`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")

See also

[`ConfusionMatrixDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")

Plot the confusion matrix given the true and predicted labels.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import ConfusionMatrixDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...         X, y, random\_state\=0)
\>>> clf \= SVC(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
SVC(random\_state=0)
\>>> ConfusionMatrixDisplay.from\_estimator(
...     clf, X\_test, y\_test)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-ConfusionMatrixDisplay-2_00_00.png](https://scikit-learn.org/stable/_images/sklearn-metrics-ConfusionMatrixDisplay-2_00_00.png)

For a detailed example of using a confusion matrix to evaluate a Support Vector Classifier, please see [Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py)

classmethod from\_predictions(_y\_true_, _y\_pred_, _\*_, _labels\=None_, _sample\_weight\=None_, _normalize\=None_, _display\_labels\=None_, _include\_values\=True_, _xticks\_rotation\='horizontal'_, _values\_format\=None_, _cmap\='viridis'_, _ax\=None_, _colorbar\=True_, _im\_kw\=None_, _text\_kw\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/confusion_matrix.py#L353)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "Link to this definition")

Plot Confusion Matrix given true and predicted labels.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
.

Added in version 1.0.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True labels.

**y\_pred**array-like of shape (n\_samples,)

The predicted labels given by the method `predict` of an classifier.

**labels**array-like of shape (n\_classes,), default=None

List of labels to index the confusion matrix. This may be used to reorder or select a subset of labels. If `None` is given, those that appear at least once in `y_true` or `y_pred` are used in sorted order.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**normalize**{‘true’, ‘pred’, ‘all’}, default=None

Either to normalize the counts display in the matrix:

*   if `'true'`, the confusion matrix is normalized over the true conditions (e.g. rows);
    
*   if `'pred'`, the confusion matrix is normalized over the predicted conditions (e.g. columns);
    
*   if `'all'`, the confusion matrix is normalized by the total number of samples;
    
*   if `None` (default), the confusion matrix will not be normalized.
    

**display\_labels**array-like of shape (n\_classes,), default=None

Target names used for plotting. By default, `labels` will be used if it is defined, otherwise the unique labels of `y_true` and `y_pred` will be used.

**include\_values**bool, default=True

Includes values in confusion matrix.

**xticks\_rotation**{‘vertical’, ‘horizontal’} or float, default=’horizontal’

Rotation of xtick labels.

**values\_format**str, default=None

Format specification for values in confusion matrix. If `None`, the format specification is ‘d’ or ‘.2g’ whichever is shorter.

**cmap**str or matplotlib Colormap, default=’viridis’

Colormap recognized by matplotlib.

**ax**matplotlib Axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**colorbar**bool, default=True

Whether or not to add a colorbar to the plot.

**im\_kw**dict, default=None

Dict with keywords passed to `matplotlib.pyplot.imshow` call.

**text\_kw**dict, default=None

Dict with keywords passed to `matplotlib.pyplot.text` call.

Added in version 1.2.

Returns:

**display**[`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")

See also

[`ConfusionMatrixDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")

Plot the confusion matrix given an estimator, the data, and the label.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.metrics import ConfusionMatrixDisplay
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.svm import SVC
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...         X, y, random\_state\=0)
\>>> clf \= SVC(random\_state\=0)
\>>> clf.fit(X\_train, y\_train)
SVC(random\_state=0)
\>>> y\_pred \= clf.predict(X\_test)
\>>> ConfusionMatrixDisplay.from\_predictions(
...    y\_test, y\_pred)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-ConfusionMatrixDisplay-3.png](https://scikit-learn.org/stable/_images/sklearn-metrics-ConfusionMatrixDisplay-3.png)

plot(_\*_, _include\_values\=True_, _cmap\='viridis'_, _xticks\_rotation\='horizontal'_, _values\_format\=None_, _ax\=None_, _colorbar\=True_, _im\_kw\=None_, _text\_kw\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/confusion_matrix.py#L88)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.plot "Link to this definition")

Plot visualization.

Parameters:

**include\_values**bool, default=True

Includes values in confusion matrix.

**cmap**str or matplotlib Colormap, default=’viridis’

Colormap recognized by matplotlib.

**xticks\_rotation**{‘vertical’, ‘horizontal’} or float, default=’horizontal’

Rotation of xtick labels.

**values\_format**str, default=None

Format specification for values in confusion matrix. If `None`, the format specification is ‘d’ or ‘.2g’ whichever is shorter.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**colorbar**bool, default=True

Whether or not to add a colorbar to the plot.

**im\_kw**dict, default=None

Dict with keywords passed to `matplotlib.pyplot.imshow` call.

**text\_kw**dict, default=None

Dict with keywords passed to `matplotlib.pyplot.text` call.

Added in version 1.2.

Returns:

**display**[`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")

Returns a [`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")
 instance that contains all the information to plot the confusion matrix.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)