[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_ols_ridge.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_ols_ridge.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_ols_ridge.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_ols_ridge.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ols_ridge.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_ols_ridge.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#sphx-glr-download-auto-examples-linear-model-plot-ols-ridge-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Ordinary Least Squares and Ridge Regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#ordinary-least-squares-and-ridge-regression "Link to this heading")

==================================================================================================================================================================================================

1.  Ordinary Least Squares: We illustrate how to use the ordinary least squares (OLS) model, [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    , on a single feature of the diabetes dataset. We train on a subset of the data, evaluate on a test set, and visualize the predictions.
    
2.  Ordinary Least Squares and Ridge Regression Variance: We then show how OLS can have high variance when the data is sparse or noisy, by fitting on a very small synthetic sample repeatedly. Ridge regression, [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , reduces this variance by penalizing (shrinking) the coefficients, leading to more stable predictions.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data Loading and Preparation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#data-loading-and-preparation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Load the diabetes dataset. For simplicity, we only keep a single feature in the data. Then, we split the data and target into training and test sets.

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True)
X \= X\[:, \[2\]\]  \# Use only one feature
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=20, shuffle\=False)

Copy to clipboard

Linear regression model[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#linear-regression-model "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

We create a linear regression model and fit it on the training data. Note that by default, an intercept is added to the model. We can control this behavior by setting the `fit_intercept` parameter.

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")

regressor \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
().fit(X\_train, y\_train)

Copy to clipboard

Model evaluation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#model-evaluation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

We evaluate the model’s performance on the test set using the mean squared error and the coefficient of determination.

from sklearn.metrics import [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
, [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")

y\_pred \= regressor.predict(X\_test)

print(f"Mean squared error: {[mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_test, y\_pred):.2f}")
print(f"Coefficient of determination: {[r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred):.2f}")

Copy to clipboard

Mean squared error: 2548.07
Coefficient of determination: 0.47

Copy to clipboard

Plotting the results[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#plotting-the-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

Finally, we visualize the results on the train and test data.

import matplotlib.pyplot as plt

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(10, 5), sharex\=True, sharey\=True)

ax\[0\].scatter(X\_train, y\_train, label\="Train data points")
ax\[0\].plot(
    X\_train,
    regressor.predict(X\_train),
    linewidth\=3,
    color\="tab:orange",
    label\="Model predictions",
)
ax\[0\].set(xlabel\="Feature", ylabel\="Target", title\="Train set")
ax\[0\].legend()

ax\[1\].scatter(X\_test, y\_test, label\="Test data points")
ax\[1\].plot(X\_test, y\_pred, linewidth\=3, color\="tab:orange", label\="Model predictions")
ax\[1\].set(xlabel\="Feature", ylabel\="Target", title\="Test set")
ax\[1\].legend()

fig.suptitle("Linear Regression")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Linear Regression, Train set, Test set](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_001.png)

OLS on this single-feature subset learns a linear function that minimizes the mean squared error on the training data. We can see how well (or poorly) it generalizes by looking at the R^2 score and mean squared error on the test set. In higher dimensions, pure OLS often overfits, especially if the data is noisy. Regularization techniques (like Ridge or Lasso) can help reduce that.

Ordinary Least Squares and Ridge Regression Variance[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#ordinary-least-squares-and-ridge-regression-variance "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, we illustrate the problem of high variance more clearly by using a tiny synthetic dataset. We sample only two data points, then repeatedly add small Gaussian noise to them and refit both OLS and Ridge. We plot each new line to see how much OLS can jump around, whereas Ridge remains more stable thanks to its penalty term.

import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear\_model

X\_train \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[0.5, 1\].T
y\_train \= \[0.5, 1\]
X\_test \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[0, 2\].T

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

classifiers \= dict(
    ols\=[linear\_model.LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
(), ridge\=[linear\_model.Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=0.1)
)

for name, clf in classifiers.items():
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 3))

    for \_ in range(6):
        this\_X \= 0.1 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(2, 1)) + X\_train
        clf.fit(this\_X, y\_train)

        ax.plot(X\_test, clf.predict(X\_test), color\="gray")
        ax.scatter(this\_X, y\_train, s\=3, c\="gray", marker\="o", zorder\=10)

    clf.fit(X\_train, y\_train)
    ax.plot(X\_test, clf.predict(X\_test), linewidth\=2, color\="blue")
    ax.scatter(X\_train, y\_train, s\=30, c\="red", marker\="+", zorder\=10)

    ax.set\_title(name)
    ax.set\_xlim(0, 2)
    ax.set\_ylim((0, 1.6))
    ax.set\_xlabel("X")
    ax.set\_ylabel("y")

    fig.tight\_layout()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![ols](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_002.png)
*   ![ridge](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_003.png)

Conclusion[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#conclusion "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

*   In the first example, we applied OLS to a real dataset, showing how a plain linear model can fit the data by minimizing the squared error on the training set.
    
*   In the second example, OLS lines varied drastically each time noise was added, reflecting its high variance when data is sparse or noisy. By contrast, **Ridge** regression introduces a regularization term that shrinks the coefficients, stabilizing predictions.
    

Techniques like [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 or [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 (which applies an L1 penalty) are both common ways to improve generalization and reduce overfitting. A well-tuned Ridge or Lasso often outperforms pure OLS when features are correlated, data is noisy, or sample size is small.

**Total running time of the script:** (0 minutes 0.418 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ols_ridge.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ols_ridge.ipynb)

[`Download Jupyter notebook: plot_ols_ridge.ipynb`](https://scikit-learn.org/stable/_downloads/fef48f5bfe3b15126ce6aefe6c0149fc/plot_ols_ridge.ipynb)

[`Download Python source code: plot_ols_ridge.py`](https://scikit-learn.org/stable/_downloads/f0074aca289f62d3b8d12fcab4911dd3/plot_ols_ridge.py)

[`Download zipped: plot_ols_ridge.zip`](https://scikit-learn.org/stable/_downloads/02192f99342d6d1323161978b6c80bfc/plot_ols_ridge.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nnls_thumb.png)

[Non-negative least squares](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html)

Non-negative least squares

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)

[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)

Plot Ridge coefficients as a function of the regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_thumb.png)

[HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)

HuberRegressor vs Ridge on dataset with strong outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_thumb.png)

[Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Comparison of kernel ridge and Gaussian process regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f0074aca289f62d3b8d12fcab4911dd3/plot_ols_ridge.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/fef48f5bfe3b15126ce6aefe6c0149fc/plot_ols_ridge.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/02192f99342d6d1323161978b6c80bfc/plot_ols_ridge.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ols_ridge.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ols_ridge.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)