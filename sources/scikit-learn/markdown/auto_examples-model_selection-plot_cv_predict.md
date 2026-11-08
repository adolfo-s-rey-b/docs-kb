[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_cv_predict.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_cv_predict.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_cv_predict.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_cv_predict.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_cv_predict.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_cv_predict.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html#sphx-glr-download-auto-examples-model-selection-plot-cv-predict-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plotting Cross-Validated Predictions[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html#plotting-cross-validated-predictions "Link to this heading")

========================================================================================================================================================================================

This example shows how to use [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
 together with [`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")
 to visualize prediction errors.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

We will load the diabetes dataset and create an instance of a linear regression model.

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")

X, y \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True)
lr \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()

Copy to clipboard

[`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
 returns an array of the same size of `y` where each entry is a prediction obtained by cross validation.

from sklearn.model\_selection import [cross\_val\_predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")

y\_pred \= [cross\_val\_predict](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
(lr, X, y, cv\=10)

Copy to clipboard

Since `cv=10`, it means that we trained 10 models and each model was used to predict on one of the 10 folds. We can now use the [`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")
 to visualize the prediction errors.

On the left axis, we plot the observed values y vs. the predicted values y^ given by the models. On the right axis, we plot the residuals (i.e. the difference between the observed values and the predicted values) vs. the predicted values.

import matplotlib.pyplot as plt

from sklearn.metrics import PredictionErrorDisplay

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(8, 4))
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y,
    y\_pred\=y\_pred,
    kind\="actual\_vs\_predicted",
    subsample\=100,
    ax\=axs\[0\],
    random\_state\=0,
)
axs\[0\].set\_title("Actual vs. Predicted values")
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y,
    y\_pred\=y\_pred,
    kind\="residual\_vs\_predicted",
    subsample\=100,
    ax\=axs\[1\],
    random\_state\=0,
)
axs\[1\].set\_title("Residuals vs. Predicted Values")
fig.suptitle("Plotting cross-validated predictions")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Plotting cross-validated predictions, Actual vs. Predicted values, Residuals vs. Predicted Values](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_001.png)

It is important to note that we used [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
 for visualization purpose only in this example.

It would be problematic to quantitatively assess the model performance by computing a single performance metric from the concatenated predictions returned by [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
 when the different CV folds vary by size and distributions.

It is recommended to compute per-fold performance metrics using: [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
 or [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 instead.

**Total running time of the script:** (0 minutes 0.191 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_cv_predict.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_cv_predict.ipynb)

[`Download Jupyter notebook: plot_cv_predict.ipynb`](https://scikit-learn.org/stable/_downloads/93afb18fff95760fe854241141b4bdae/plot_cv_predict.ipynb)

[`Download Python source code: plot_cv_predict.py`](https://scikit-learn.org/stable/_downloads/ff75d3bf9db66ac1cfeb9d15a1400576/plot_cv_predict.py)

[`Download zipped: plot_cv_predict.zip`](https://scikit-learn.org/stable/_downloads/b5ad104e8ecfa33bea1e5b896063738a/plot_cv_predict.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_thumb.png)

[Demonstration of k-means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html)

Demonstration of k-means assumptions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/ff75d3bf9db66ac1cfeb9d15a1400576/plot_cv_predict.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/93afb18fff95760fe854241141b4bdae/plot_cv_predict.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/b5ad104e8ecfa33bea1e5b896063738a/plot_cv_predict.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_cv_predict.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_cv_predict.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)