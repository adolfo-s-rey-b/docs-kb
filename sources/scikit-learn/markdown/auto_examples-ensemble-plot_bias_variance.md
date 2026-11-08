[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_bias_variance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_bias_variance.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_bias_variance.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_bias_variance.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_bias_variance.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_bias_variance.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html#sphx-glr-download-auto-examples-ensemble-plot-bias-variance-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Single estimator versus bagging: bias-variance decomposition[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html#single-estimator-versus-bagging-bias-variance-decomposition "Link to this heading")

===================================================================================================================================================================================================================================

This example illustrates and compares the bias-variance decomposition of the expected mean squared error of a single estimator against a bagging ensemble.

In regression, the expected mean squared error of an estimator can be decomposed in terms of bias, variance and noise. On average over datasets of the regression problem, the bias term measures the average amount by which the predictions of the estimator differ from the predictions of the best possible estimator for the problem (i.e., the Bayes model). The variance term measures the variability of the predictions of the estimator when fit over different random instances of the same problem. Each problem instance is noted “LS”, for “Learning Sample”, in the following. Finally, the noise measures the irreducible part of the error which is due the variability in the data.

The upper left figure illustrates the predictions (in dark red) of a single decision tree trained over a random dataset LS (the blue dots) of a toy 1d regression problem. It also illustrates the predictions (in light red) of other single decision trees trained over other (and different) randomly drawn instances LS of the problem. Intuitively, the variance term here corresponds to the width of the beam of predictions (in light red) of the individual estimators. The larger the variance, the more sensitive are the predictions for `x` to small changes in the training set. The bias term corresponds to the difference between the average prediction of the estimator (in cyan) and the best possible model (in dark blue). On this problem, we can thus observe that the bias is quite low (both the cyan and the blue curves are close to each other) while the variance is large (the red beam is rather wide).

The lower left figure plots the pointwise decomposition of the expected mean squared error of a single decision tree. It confirms that the bias term (in blue) is low while the variance is large (in green). It also illustrates the noise part of the error which, as expected, appears to be constant and around `0.01`.

The right figures correspond to the same plots but using instead a bagging ensemble of decision trees. In both figures, we can observe that the bias term is larger than in the previous case. In the upper right figure, the difference between the average prediction (in cyan) and the best possible model is larger (e.g., notice the offset around `x=2`). In the lower right figure, the bias curve is also slightly higher than in the lower left figure. In terms of variance however, the beam of predictions is narrower, which suggests that the variance is lower. Indeed, as the lower right figure confirms, the variance term (in green) is lower than for single decision trees. Overall, the bias-variance decomposition is therefore no longer the same. The tradeoff is better for bagging: averaging several decision trees fit on bootstrap copies of the dataset slightly increases the bias term but allows for a larger reduction of the variance, which results in a lower overall mean squared error (compare the red curves int the lower figures). The script output also confirms this intuition. The total error of the bagging ensemble is lower than the total error of a single decision tree, and this difference indeed mainly stems from a reduced variance.

For further details on bias-variance decomposition, see section 7.3 of [\[1\]](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html#id2)
.

References[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html#references "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

![Tree, Bagging(Tree)](https://scikit-learn.org/stable/_images/sphx_glr_plot_bias_variance_001.png)

Tree: 0.0255 (error) = 0.0003 (bias^2)  + 0.0152 (var) + 0.0098 (noise)
Bagging(Tree): 0.0196 (error) = 0.0004 (bias^2)  + 0.0092 (var) + 0.0098 (noise)

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

\# Settings
n\_repeat \= 50  \# Number of iterations for computing expectations
n\_train \= 50  \# Size of the training set
n\_test \= 1000  \# Size of the test set
noise \= 0.1  \# Standard deviation of the noise
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

\# Change this for exploring the bias-variance decomposition of other
\# estimators. This should work well for estimators with high variance (e.g.,
\# decision trees or KNN), but poorly for estimators with low variance (e.g.,
\# linear models).
estimators \= \[\
    ("Tree", [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
()),\
    ("Bagging(Tree)", [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")\
([DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
())),\
\]

n\_estimators \= len(estimators)

\# Generate data
def f(x):
    x \= x.ravel()

    return [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-(x\*\*2)) + 1.5 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-((x \- 2) \*\* 2))

def generate(n\_samples, noise, n\_repeat\=1):
    X \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(n\_samples) \* 10 \- 5
    X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(X)

    if n\_repeat \== 1:
        y \= f(X) + [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0.0, noise, n\_samples)
    else:
        y \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_samples, n\_repeat))

        for i in range(n\_repeat):
            y\[:, i\] \= f(X) + [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0.0, noise, n\_samples)

    X \= X.reshape((n\_samples, 1))

    return X, y

X\_train \= \[\]
y\_train \= \[\]

for i in range(n\_repeat):
    X, y \= generate(n\_samples\=n\_train, noise\=noise)
    X\_train.append(X)
    y\_train.append(y)

X\_test, y\_test \= generate(n\_samples\=n\_test, noise\=noise, n\_repeat\=n\_repeat)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 8))

\# Loop over estimators to compare
for n, (name, estimator) in enumerate(estimators):
    \# Compute predictions
    y\_predict \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_test, n\_repeat))

    for i in range(n\_repeat):
        estimator.fit(X\_train\[i\], y\_train\[i\])
        y\_predict\[:, i\] \= estimator.predict(X\_test)

    \# Bias^2 + Variance + Noise decomposition of the mean squared error
    y\_error \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_test)

    for i in range(n\_repeat):
        for j in range(n\_repeat):
            y\_error += (y\_test\[:, j\] \- y\_predict\[:, i\]) \*\* 2

    y\_error /= n\_repeat \* n\_repeat

    y\_noise \= [np.var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
(y\_test, axis\=1)
    y\_bias \= (f(X\_test) \- [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_predict, axis\=1)) \*\* 2
    y\_var \= [np.var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
(y\_predict, axis\=1)

    print(
        "{0}: {1:.4f} (error) = {2:.4f} (bias^2) "
        " + {3:.4f} (var) + {4:.4f} (noise)".format(
            name, [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_error), [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_bias), [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_var), [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_noise)
        )
    )

    \# Plot figures
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, n\_estimators, n + 1)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, f(X\_test), "b", label\="$f(x)$")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_train\[0\], y\_train\[0\], ".b", label\="LS ~ $y = f(x)+noise$")

    for i in range(n\_repeat):
        if i \== 0:
            [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_predict\[:, i\], "r", label\=r"$\\^y(x)$")
        else:
            [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_predict\[:, i\], "r", alpha\=0.05)

    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_predict, axis\=1), "c", label\=r"$\\mathbb{E}\_{LS} \\^y(x)$")

    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\[\-5, 5\])
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(name)

    if n \== n\_estimators \- 1:
        [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\=(1.1, 0.5))

    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, n\_estimators, n\_estimators + n + 1)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_error, "r", label\="$error(x)$")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_bias, "b", label\="$bias^2(x)$")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_var, "g", label\="$variance(x)$")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_noise, "c", label\="$noise(x)$")

    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\[\-5, 5\])
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\[0, 0.1\])

    if n \== n\_estimators \- 1:
        [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\=(1.1, 0.5))

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(right\=0.75)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.174 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_bias_variance.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_bias_variance.ipynb)

[`Download Jupyter notebook: plot_bias_variance.ipynb`](https://scikit-learn.org/stable/_downloads/8d09950dfaf03c48cddf217f4acf8b65/plot_bias_variance.ipynb)

[`Download Python source code: plot_bias_variance.py`](https://scikit-learn.org/stable/_downloads/4fe7ce5d502ee21f3c344f775829354a/plot_bias_variance.py)

[`Download zipped: plot_bias_variance.zip`](https://scikit-learn.org/stable/_downloads/feb442c34c5c9dab879c789adc5755fc/plot_bias_variance.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4fe7ce5d502ee21f3c344f775829354a/plot_bias_variance.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/8d09950dfaf03c48cddf217f4acf8b65/plot_bias_variance.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/feb442c34c5c9dab879c789adc5755fc/plot_bias_variance.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_bias_variance.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_bias_variance.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)