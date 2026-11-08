[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#sphx-glr-download-auto-examples-ensemble-plot-gradient-boosting-early-stopping-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Early stopping in Gradient Boosting[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#early-stopping-in-gradient-boosting "Link to this heading")

=====================================================================================================================================================================================================

Gradient Boosting is an ensemble technique that combines multiple weak learners, typically decision trees, to create a robust and powerful predictive model. It does so in an iterative fashion, where each new stage (tree) corrects the errors of the previous ones.

Early stopping is a technique in Gradient Boosting that allows us to find the optimal number of iterations required to build a model that generalizes well to unseen data and avoids overfitting. The concept is simple: we set aside a portion of our dataset as a validation set (specified using `validation_fraction`) to assess the model’s performance during training. As the model is iteratively built with additional stages (trees), its performance on the validation set is monitored as a function of the number of steps.

Early stopping becomes effective when the model’s performance on the validation set plateaus or worsens (within deviations specified by `tol`) over a certain number of consecutive stages (specified by `n_iter_no_change`). This signals that the model has reached a point where further iterations may lead to overfitting, and it’s time to stop training.

The number of estimators (trees) in the final model, when early stopping is applied, can be accessed using the `n_estimators_` attribute. Overall, early stopping is a valuable tool to strike a balance between model performance and efficiency in gradient boosting.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data Preparation[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#data-preparation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

First we load and prepares the California Housing Prices dataset for training and evaluation. It subsets the dataset, splits it into training and validation sets.

import time

import matplotlib.pyplot as plt

from sklearn.datasets import [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
from sklearn.ensemble import [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
from sklearn.metrics import [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

data \= [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
()
X, y \= data.data\[:600\], data.target\[:600\]

X\_train, X\_val, y\_train, y\_val \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.2, random\_state\=42)

Copy to clipboard

Model Training and Comparison[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#model-training-and-comparison "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Two [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
 models are trained: one with and another without early stopping. The purpose is to compare their performance. It also calculates the training time and the `n_estimators_` used by both models.

params \= dict(n\_estimators\=1000, max\_depth\=5, learning\_rate\=0.1, random\_state\=42)

gbm\_full \= [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(\*\*params)
gbm\_early\_stopping \= [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(
    \*\*params,
    validation\_fraction\=0.1,
    n\_iter\_no\_change\=10,
)

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
gbm\_full.fit(X\_train, y\_train)
training\_time\_full \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time
n\_estimators\_full \= gbm\_full.n\_estimators\_

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
gbm\_early\_stopping.fit(X\_train, y\_train)
training\_time\_early\_stopping \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time
estimators\_early\_stopping \= gbm\_early\_stopping.n\_estimators\_

Copy to clipboard

Error Calculation[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#error-calculation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The code calculates the [`mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
 for both training and validation datasets for the models trained in the previous section. It computes the errors for each boosting iteration. The purpose is to assess the performance and convergence of the models.

train\_errors\_without \= \[\]
val\_errors\_without \= \[\]

train\_errors\_with \= \[\]
val\_errors\_with \= \[\]

for i, (train\_pred, val\_pred) in enumerate(
    zip(
        gbm\_full.staged\_predict(X\_train),
        gbm\_full.staged\_predict(X\_val),
    )
):
    train\_errors\_without.append([mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_train, train\_pred))
    val\_errors\_without.append([mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_val, val\_pred))

for i, (train\_pred, val\_pred) in enumerate(
    zip(
        gbm\_early\_stopping.staged\_predict(X\_train),
        gbm\_early\_stopping.staged\_predict(X\_val),
    )
):
    train\_errors\_with.append([mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_train, train\_pred))
    val\_errors\_with.append([mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_val, val\_pred))

Copy to clipboard

Visualize Comparison[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#visualize-comparison "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

It includes three subplots:

1.  Plotting training errors of both models over boosting iterations.
    
2.  Plotting validation errors of both models over boosting iterations.
    
3.  Creating a bar chart to compare the training times and the estimator used of the models with and without early stopping.
    

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(12, 4))

axes\[0\].plot(train\_errors\_without, label\="gbm\_full")
axes\[0\].plot(train\_errors\_with, label\="gbm\_early\_stopping")
axes\[0\].set\_xlabel("Boosting Iterations")
axes\[0\].set\_ylabel("MSE (Training)")
axes\[0\].set\_yscale("log")
axes\[0\].legend()
axes\[0\].set\_title("Training Error")

axes\[1\].plot(val\_errors\_without, label\="gbm\_full")
axes\[1\].plot(val\_errors\_with, label\="gbm\_early\_stopping")
axes\[1\].set\_xlabel("Boosting Iterations")
axes\[1\].set\_ylabel("MSE (Validation)")
axes\[1\].set\_yscale("log")
axes\[1\].legend()
axes\[1\].set\_title("Validation Error")

training\_times \= \[training\_time\_full, training\_time\_early\_stopping\]
labels \= \["gbm\_full", "gbm\_early\_stopping"\]
bars \= axes\[2\].bar(labels, training\_times)
axes\[2\].set\_ylabel("Training Time (s)")

for bar, n\_estimators in zip(bars, \[n\_estimators\_full, estimators\_early\_stopping\]):
    height \= bar.get\_height()
    axes\[2\].text(
        bar.get\_x() + bar.get\_width() / 2,
        height + 0.001,
        f"Estimators: {n\_estimators}",
        ha\="center",
        va\="bottom",
    )

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Training Error, Validation Error](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_001.png)

The difference in training error between the `gbm_full` and the `gbm_early_stopping` stems from the fact that `gbm_early_stopping` sets aside `validation_fraction` of the training data as internal validation set. Early stopping is decided based on this internal validation score.

Summary[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#summary "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

In our example with the [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
 model on the California Housing Prices dataset, we have demonstrated the practical benefits of early stopping:

*   **Preventing Overfitting:** We showed how the validation error stabilizes or starts to increase after a certain point, indicating that the model generalizes better to unseen data. This is achieved by stopping the training process before overfitting occurs.
    
*   **Improving Training Efficiency:** We compared training times between models with and without early stopping. The model with early stopping achieved comparable accuracy while requiring significantly fewer estimators, resulting in faster training.
    

**Total running time of the script:** (0 minutes 2.720 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_early_stopping.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_early_stopping.ipynb)

[`Download Jupyter notebook: plot_gradient_boosting_early_stopping.ipynb`](https://scikit-learn.org/stable/_downloads/8452fc8dfe9850cfdaa1b758e5a2748b/plot_gradient_boosting_early_stopping.ipynb)

[`Download Python source code: plot_gradient_boosting_early_stopping.py`](https://scikit-learn.org/stable/_downloads/be911e971b87fe80b6899069dbcfb737/plot_gradient_boosting_early_stopping.py)

[`Download zipped: plot_gradient_boosting_early_stopping.zip`](https://scikit-learn.org/stable/_downloads/bc627aa67e9e5146b84d53d996f25245/plot_gradient_boosting_early_stopping.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_thumb.png)

[Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html)

Early stopping of Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/be911e971b87fe80b6899069dbcfb737/plot_gradient_boosting_early_stopping.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/8452fc8dfe9850cfdaa1b758e5a2748b/plot_gradient_boosting_early_stopping.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/bc627aa67e9e5146b84d53d996f25245/plot_gradient_boosting_early_stopping.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_early_stopping.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_early_stopping.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)