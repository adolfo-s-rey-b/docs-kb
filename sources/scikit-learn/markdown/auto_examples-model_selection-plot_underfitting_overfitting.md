[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_underfitting_overfitting.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_underfitting_overfitting.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_underfitting_overfitting.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_underfitting_overfitting.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_underfitting_overfitting.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_underfitting_overfitting.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html#sphx-glr-download-auto-examples-model-selection-plot-underfitting-overfitting-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Underfitting vs. Overfitting[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html#underfitting-vs-overfitting "Link to this heading")

=====================================================================================================================================================================================

This example demonstrates the problems of underfitting and overfitting and how we can use linear regression with polynomial features to approximate nonlinear functions. The plot shows the function that we want to approximate, which is a part of the cosine function. In addition, the samples from the real function and the approximations of different models are displayed. The models have polynomial features of different degrees. We can see that a linear function (polynomial with degree 1) is not sufficient to fit the training samples. This is called **underfitting**. A polynomial of degree 4 approximates the true function almost perfectly. However, for higher degrees the model will **overfit** the training data, i.e. it learns the noise of the training data. We evaluate quantitatively **overfitting** / **underfitting** by using cross-validation. We calculate the mean squared error (MSE) on the validation set, the higher, the less likely the model generalizes correctly from the training data.

![Degree 1 MSE = 4.08e-01(+/- 4.25e-01), Degree 4 MSE = 4.32e-02(+/- 7.08e-02), Degree 15 MSE = 1.83e+08(+/- 5.48e+08)](https://scikit-learn.org/stable/_images/sphx_glr_plot_underfitting_overfitting_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.model\_selection import [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")

def true\_fun(X):
    return [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(1.5 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* X)

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

n\_samples \= 30
degrees \= \[1, 4, 15\]

X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
([np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(n\_samples))
y \= true\_fun(X) + [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples) \* 0.1

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(14, 5))
for i in range(len(degrees)):
    ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, len(degrees), i + 1)
    [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(ax, xticks\=(), yticks\=())

    polynomial\_features \= [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(degree\=degrees\[i\], include\_bias\=False)
    \# Avoid truncating small singular values (tol is used as cond in lstsq since v1.9)
    linear\_regression \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
(tol\=[np.finfo](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy.finfo "numpy.finfo")
(float).eps)
    pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
        \[\
            ("polynomial\_features", polynomial\_features),\
            ("linear\_regression", linear\_regression),\
        \]
    )
    pipeline.fit(X\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\], y)

    \# Evaluate the models using crossvalidation
    scores \= [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(
        pipeline, X\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\], y, scoring\="neg\_mean\_squared\_error", cv\=10
    )

    X\_test \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 100)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, pipeline.predict(X\_test\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]), label\="Model")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, true\_fun(X\_test), label\="True function")
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X, y, edgecolor\="b", s\=20, label\="Samples")
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("x")
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
((0, 1))
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
((\-2, 2))
    [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        "Degree {}\\nMSE = {:.2e}(+/- {:.2e})".format(
            degrees\[i\], \-scores.mean(), scores.std()
        )
    )
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.199 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_underfitting_overfitting.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_underfitting_overfitting.ipynb)

[`Download Jupyter notebook: plot_underfitting_overfitting.ipynb`](https://scikit-learn.org/stable/_downloads/3b25b9158f1c0a1564eb0f4c9e531d46/plot_underfitting_overfitting.ipynb)

[`Download Python source code: plot_underfitting_overfitting.py`](https://scikit-learn.org/stable/_downloads/746a69b3fd67273959a3cd9bfc2a88e8/plot_underfitting_overfitting.py)

[`Download zipped: plot_underfitting_overfitting.zip`](https://scikit-learn.org/stable/_downloads/4a71403d3ce9170ab7db4afc50d661a7/plot_underfitting_overfitting.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_thumb.png)

[Polynomial and Spline interpolation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)

Polynomial and Spline interpolation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)

[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)

Robust linear estimator fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/746a69b3fd67273959a3cd9bfc2a88e8/plot_underfitting_overfitting.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3b25b9158f1c0a1564eb0f4c9e531d46/plot_underfitting_overfitting.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4a71403d3ce9170ab7db4afc50d661a7/plot_underfitting_overfitting.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_underfitting_overfitting.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_underfitting_overfitting.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)