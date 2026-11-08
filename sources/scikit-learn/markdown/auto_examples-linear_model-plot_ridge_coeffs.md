[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_ridge_coeffs.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_ridge_coeffs.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_ridge_coeffs.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_ridge_coeffs.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ridge_coeffs.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_ridge_coeffs.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#sphx-glr-download-auto-examples-linear-model-plot-ridge-coeffs-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Ridge coefficients as a function of the L2 Regularization[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#ridge-coefficients-as-a-function-of-the-l2-regularization "Link to this heading")

=================================================================================================================================================================================================================================

A model that overfits learns the training data too well, capturing both the underlying patterns and the noise in the data. However, when applied to unseen data, the learned associations may not hold. We normally detect this when we apply our trained predictions to the test data and see the statistical performance drop significantly compared to the training data.

One way to overcome overfitting is through regularization, which can be done by penalizing large weights (coefficients) in linear models, forcing the model to shrink all coefficients. Regularization reduces a model’s reliance on specific information obtained from the training samples.

This example illustrates how L2 regularization in a [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 regression affects a model’s performance by adding a penalty term to the loss that increases with the coefficients β.

The regularized loss function is given by: L(X,y,β)\=‖y−Xβ‖22+α‖β‖22

where X is the input data, y is the target variable, β is the vector of coefficients associated with the features, and α is the regularization strength.

The regularized loss function aims to balance the trade-off between accurately predicting the training set and to prevent overfitting.

In this regularized loss, the left-hand side (e.g. ‖y−Xβ‖22) measures the squared difference between the actual target variable, y, and the predicted values. Minimizing this term alone could lead to overfitting, as the model may become too complex and sensitive to noise in the training data.

To address overfitting, Ridge regularization adds a constraint, called a penalty term, (α‖β‖22) to the loss function. This penalty term is the sum of the squares of the model’s coefficients, multiplied by the regularization strength α. By introducing this constraint, Ridge regularization discourages any single coefficient βi from taking an excessively large value and encourages smaller and more evenly distributed coefficients. Higher values of α force the coefficients towards zero. However, an excessively high α can result in an underfit model that fails to capture important patterns in the data.

Therefore, the regularized loss function combines the prediction accuracy term and the penalty term. By adjusting the regularization strength, practitioners can fine-tune the degree of constraint imposed on the weights, training a model capable of generalizing well to unseen data while avoiding overfitting.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Purpose of this example[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#purpose-of-this-example "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

For the purpose of showing how Ridge regularization works, we will create a non-noisy data set. Then we will train a regularized model on a range of regularization strengths (α) and plot how the trained coefficients and the mean squared error between those and the original values behave as functions of the regularization strength.

### Creating a non-noisy data set[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#creating-a-non-noisy-data-set "Link to this heading")

We make a toy data set with 100 samples and 10 features, that’s suitable to detect regression. Out of the 10 features, 8 are informative and contribute to the regression, while the remaining 2 features do not have any effect on the target variable (their true coefficients are 0). Please note that in this example the data is non-noisy, hence we can expect our regression model to recover exactly the true coefficients w.

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")

X, y, w \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(
    n\_samples\=100, n\_features\=10, n\_informative\=8, coef\=True, random\_state\=1
)

\# Obtain the true coefficients
print(f"The true coefficient of this regression problem are:\\n{w}")

Copy to clipboard

The true coefficient of this regression problem are:
\[38.32634568 88.49665188  0.         29.75747153  0.         19.08699432\
 25.44381023 38.69892343 49.28808734 71.75949622\]

Copy to clipboard

### Training the Ridge Regressor[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#training-the-ridge-regressor "Link to this heading")

We use [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
, a linear model with L2 regularization. We train several models, each with a different value for the model parameter `alpha`, which is a positive constant that multiplies the penalty term, controlling the regularization strength. For each trained model we then compute the error between the true coefficients `w` and the coefficients found by the model `clf`. We store the identified coefficients and the calculated errors for the corresponding coefficients in lists, which makes it convenient for us to plot them.

import numpy as np

from sklearn.linear\_model import [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
from sklearn.metrics import [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")

clf \= [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
()

\# Generate values for \`alpha\` that are evenly distributed on a logarithmic scale
alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-3, 4, 200)
coefs \= \[\]
errors\_coefs \= \[\]

\# Train the model with different regularisation strengths
for a in alphas:
    clf.set\_params(alpha\=a).fit(X, y)
    coefs.append(clf.coef\_)
    errors\_coefs.append([mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(clf.coef\_, w))

Copy to clipboard

### Plotting trained Coefficients and Mean Squared Errors[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#plotting-trained-coefficients-and-mean-squared-errors "Link to this heading")

We now plot the 10 different regularized coefficients as a function of the regularization parameter `alpha` where each color represents a different coefficient.

On the right-hand-side, we plot how the errors of the coefficients from the estimator change as a function of regularization.

import matplotlib.pyplot as plt
import pandas as pd

alphas \= [pd.Index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
(alphas, name\="alpha")
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(coefs, index\=alphas, columns\=\[f"Feature {i}" for i in range(10)\])
errors \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
(errors\_coefs, index\=alphas, name\="Mean squared error")

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(20, 6))

coefs.plot(
    ax\=axs\[0\],
    logx\=True,
    title\="Ridge coefficients as a function of the regularization strength",
)
axs\[0\].set\_ylabel("Ridge coefficient values")
errors.plot(
    ax\=axs\[1\],
    logx\=True,
    title\="Coefficient error as a function of the regularization strength",
)
\_ \= axs\[1\].set\_ylabel("Mean squared error")

Copy to clipboard

![Ridge coefficients as a function of the regularization strength, Coefficient error as a function of the regularization strength](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_001.png)

### Interpreting the plots[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#interpreting-the-plots "Link to this heading")

The plot on the left-hand side shows how the regularization strength (`alpha`) affects the Ridge regression coefficients. Smaller values of `alpha` (weak regularization), allow the coefficients to closely resemble the true coefficients (`w`) used to generate the data set. This is because no additional noise was added to our artificial data set. As `alpha` increases, the coefficients shrink towards zero, gradually reducing the impact of the features that were formerly more significant.

The right-hand side plot shows the mean squared error (MSE) between the coefficients found by the model and the true coefficients (`w`). It provides a measure that relates to how exact our ridge model is in comparison to the true generative model. A low error means that it found coefficients closer to the ones of the true generative model. In this case, since our toy data set was non-noisy, we can see that the least regularized model retrieves coefficients closest to the true coefficients (`w`) (error is close to 0).

When `alpha` is small, the model captures the intricate details of the training data, whether those were caused by noise or by actual information. As `alpha` increases, the highest coefficients shrink more rapidly, rendering their corresponding features less influential in the training process. This can enhance a model’s ability to generalize to unseen data (if there was a lot of noise to capture), but it also poses the risk of losing performance if the regularization becomes too strong compared to the amount of noise the data contained (as in this example).

In real-world scenarios where data typically includes noise, selecting an appropriate `alpha` value becomes crucial in striking a balance between an overfitting and an underfitting model.

Here, we saw that [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 adds a penalty to the coefficients to fight overfitting. Another problem that occurs is linked to the presence of outliers in the training dataset. An outlier is a data point that differs significantly from other observations. Concretely, these outliers impact the left-hand side term of the loss function that we showed earlier. Some other linear models are formulated to be robust to outliers such as the [`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
. You can learn more about it in the [HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html#sphx-glr-auto-examples-linear-model-plot-huber-vs-ridge-py)
 example.

**Total running time of the script:** (0 minutes 0.647 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ridge_coeffs.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ridge_coeffs.ipynb)

[`Download Jupyter notebook: plot_ridge_coeffs.ipynb`](https://scikit-learn.org/stable/_downloads/44775ca43ce935c840a877c3d2ebed6c/plot_ridge_coeffs.ipynb)

[`Download Python source code: plot_ridge_coeffs.py`](https://scikit-learn.org/stable/_downloads/b075b4610b24c70d5757248abef3fb61/plot_ridge_coeffs.py)

[`Download zipped: plot_ridge_coeffs.zip`](https://scikit-learn.org/stable/_downloads/f57e626755a909b821ad476093ada898/plot_ridge_coeffs.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)

[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)

Plot Ridge coefficients as a function of the regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/b075b4610b24c70d5757248abef3fb61/plot_ridge_coeffs.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/44775ca43ce935c840a877c3d2ebed6c/plot_ridge_coeffs.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f57e626755a909b821ad476093ada898/plot_ridge_coeffs.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ridge_coeffs.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ridge_coeffs.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)