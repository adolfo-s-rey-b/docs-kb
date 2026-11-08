[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.PredictionErrorDisplay.html)

Collapse Sidebar Expand Sidebar

PredictionErrorDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#predictionerrordisplay "Link to this heading")

=======================================================================================================================================================================

class sklearn.metrics.PredictionErrorDisplay(_\*_, _y\_true_, _y\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/regression.py#L13)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "Link to this definition")

Visualization of the prediction error of a regression model.

This tool can display “residuals vs predicted” or “actual vs predicted” using scatter plots to qualitatively assess the behavior of a regressor, preferably on held-out data points.

See the details in the docstrings of [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_estimator "sklearn.metrics.PredictionErrorDisplay.from_estimator")
 or [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
 to create a visualizer. All parameters are stored as attributes.

For general information regarding `scikit-learn` visualization tools, read more in the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For details regarding interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#visualization-regression-evaluation)
.

Added in version 1.2.

Parameters:

**y\_true**ndarray of shape (n\_samples,)

True values.

**y\_pred**ndarray of shape (n\_samples,)

Prediction values.

Attributes:

**line\_**matplotlib Artist

Optimal line representing `y_true == y_pred`. Therefore, it is a diagonal line for `kind="predictions"` and a horizontal line for `kind="residuals"`.

**errors\_lines\_**matplotlib Artist or None

Residual lines. If `with_errors=False`, then it is set to `None`.

**scatter\_**matplotlib Artist

Scatter data points.

**ax\_**matplotlib Axes

Axes with the different matplotlib axis.

**figure\_**matplotlib Figure

Figure containing the scatter and lines.

See also

[`PredictionErrorDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_estimator "sklearn.metrics.PredictionErrorDisplay.from_estimator")

Prediction error visualization given an estimator and some data.

[`PredictionErrorDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")

Prediction error visualization given the true and predicted targets.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import load\_diabetes
\>>> from sklearn.linear\_model import Ridge
\>>> from sklearn.metrics import PredictionErrorDisplay
\>>> X, y \= load\_diabetes(return\_X\_y\=True)
\>>> ridge \= Ridge().fit(X, y)
\>>> y\_pred \= ridge.predict(X)
\>>> display \= PredictionErrorDisplay(y\_true\=y, y\_pred\=y\_pred)
\>>> display.plot()
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PredictionErrorDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PredictionErrorDisplay-1.png)

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _kind\='residual\_vs\_predicted'_, _subsample\=1000_, _random\_state\=None_, _ax\=None_, _scatter\_kwargs\=None_, _line\_kwargs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/regression.py#L189)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_estimator "Link to this definition")

Plot the prediction error given a regressor and some data.

For general information regarding `scikit-learn` visualization tools, read more in the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For details regarding interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#visualization-regression-evaluation)
.

Added in version 1.2.

Parameters:

**estimator**estimator instance

Fitted regressor or a fitted [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 in which the last estimator is a regressor.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input values.

**y**array-like of shape (n\_samples,)

Target values.

**kind**{“actual\_vs\_predicted”, “residual\_vs\_predicted”}, default=”residual\_vs\_predicted”

The type of plot to draw:

*   “actual\_vs\_predicted” draws the observed values (y-axis) vs. the predicted values (x-axis).
    
*   “residual\_vs\_predicted” draws the residuals, i.e. difference between observed and predicted values, (y-axis) vs. the predicted values (x-axis).
    

**subsample**float, int or None, default=1\_000

Sampling the samples to be shown on the scatter plot. If `float`, it should be between 0 and 1 and represents the proportion of the original dataset. If `int`, it represents the number of samples display on the scatter plot. If `None`, no subsampling will be applied. by default, 1000 samples or less will be displayed.

**random\_state**int or RandomState, default=None

Controls the randomness when `subsample` is not `None`. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**scatter\_kwargs**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.scatter` call.

**line\_kwargs**dict, default=None

Dictionary with keyword passed to the `matplotlib.pyplot.plot` call to draw the optimal line.

Returns:

**display**[`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")

Object that stores the computed values.

See also

[`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")

Prediction error visualization for regression.

[`PredictionErrorDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")

Prediction error visualization given the true and predicted targets.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import load\_diabetes
\>>> from sklearn.linear\_model import Ridge
\>>> from sklearn.metrics import PredictionErrorDisplay
\>>> X, y \= load\_diabetes(return\_X\_y\=True)
\>>> ridge \= Ridge().fit(X, y)
\>>> disp \= PredictionErrorDisplay.from\_estimator(ridge, X, y)
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PredictionErrorDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PredictionErrorDisplay-2.png)

classmethod from\_predictions(_y\_true_, _y\_pred_, _\*_, _kind\='residual\_vs\_predicted'_, _subsample\=1000_, _random\_state\=None_, _ax\=None_, _scatter\_kwargs\=None_, _line\_kwargs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/regression.py#L294)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "Link to this definition")

Plot the prediction error given the true and predicted targets.

For general information regarding `scikit-learn` visualization tools, read more in the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For details regarding interpreting these plots, refer to the [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#visualization-regression-evaluation)
.

Added in version 1.2.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True target values.

**y\_pred**array-like of shape (n\_samples,)

Predicted target values.

**kind**{“actual\_vs\_predicted”, “residual\_vs\_predicted”}, default=”residual\_vs\_predicted”

The type of plot to draw:

*   “actual\_vs\_predicted” draws the observed values (y-axis) vs. the predicted values (x-axis).
    
*   “residual\_vs\_predicted” draws the residuals, i.e. difference between observed and predicted values, (y-axis) vs. the predicted values (x-axis).
    

**subsample**float, int or None, default=1\_000

Sampling the samples to be shown on the scatter plot. If `float`, it should be between 0 and 1 and represents the proportion of the original dataset. If `int`, it represents the number of samples display on the scatter plot. If `None`, no subsampling will be applied. by default, 1000 samples or less will be displayed.

**random\_state**int or RandomState, default=None

Controls the randomness when `subsample` is not `None`. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**scatter\_kwargs**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.scatter` call.

**line\_kwargs**dict, default=None

Dictionary with keyword passed to the `matplotlib.pyplot.plot` call to draw the optimal line.

Returns:

**display**[`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")

Object that stores the computed values.

See also

[`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")

Prediction error visualization for regression.

[`PredictionErrorDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_estimator "sklearn.metrics.PredictionErrorDisplay.from_estimator")

Prediction error visualization given an estimator and some data.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import load\_diabetes
\>>> from sklearn.linear\_model import Ridge
\>>> from sklearn.metrics import PredictionErrorDisplay
\>>> X, y \= load\_diabetes(return\_X\_y\=True)
\>>> ridge \= Ridge().fit(X, y)
\>>> y\_pred \= ridge.predict(X)
\>>> disp \= PredictionErrorDisplay.from\_predictions(y\_true\=y, y\_pred\=y\_pred)
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-metrics-PredictionErrorDisplay-3.png](https://scikit-learn.org/stable/_images/sklearn-metrics-PredictionErrorDisplay-3.png)

plot(_ax\=None_, _\*_, _kind\='residual\_vs\_predicted'_, _scatter\_kwargs\=None_, _line\_kwargs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_plot/regression.py#L85)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.plot "Link to this definition")

Plot visualization.

Extra keyword arguments will be passed to matplotlib’s `plot`.

Parameters:

**ax**matplotlib axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**kind**{“actual\_vs\_predicted”, “residual\_vs\_predicted”}, default=”residual\_vs\_predicted”

The type of plot to draw:

*   “actual\_vs\_predicted” draws the observed values (y-axis) vs. the predicted values (x-axis).
    
*   “residual\_vs\_predicted” draws the residuals, i.e. difference between observed and predicted values, (y-axis) vs. the predicted values (x-axis).
    

**scatter\_kwargs**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.scatter` call.

**line\_kwargs**dict, default=None

Dictionary with keyword passed to the `matplotlib.pyplot.plot` call to draw the optimal line.

Returns:

**display**[`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")

Object that stores computed values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)