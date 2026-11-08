[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpr-noisy-targets-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gaussian Processes regression: basic introductory example[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#gaussian-processes-regression-basic-introductory-example "Link to this heading")

=========================================================================================================================================================================================================================================

A simple one-dimensional regression example computed in two different ways:

1.  A noise-free case
    
2.  A noisy case with known noise-level per datapoint
    

In both cases, the kernel’s parameters are estimated using the maximum likelihood principle.

The figures illustrate the interpolating property of the Gaussian Process model as well as its probabilistic nature in the form of a pointwise 95% confidence interval.

Note that `alpha` is a parameter to control the strength of the Tikhonov regularization on the assumed training points’ covariance matrix.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset generation[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#dataset-generation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

We will start by generating a synthetic dataset. The true generative process is defined as f(x)\=xsin⁡(x).

import numpy as np

X \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(start\=0, stop\=10, num\=1\_000).reshape(\-1, 1)
y \= [np.squeeze](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")
(X \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X))

Copy to clipboard

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\=r"$f(x) = x \\sin(x)$", linestyle\="dotted")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$f(x)$")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("True generative process")

Copy to clipboard

![True generative process](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_001.png)

We will use this dataset in the next experiment to illustrate how Gaussian Process regression is working.

Example with noise-free target[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#example-with-noise-free-target "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this first example, we will use the true generative process without adding any noise. For training the Gaussian Process regression, we will only select few samples.

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
training\_indices \= rng.choice([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y.size), size\=6, replace\=False)
X\_train, y\_train \= X\[training\_indices\], y\[training\_indices\]

Copy to clipboard

Now, we fit a Gaussian process on these few training data samples. We will use a radial basis function (RBF) kernel and a constant parameter to fit the amplitude.

from sklearn.gaussian\_process import [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")

kernel \= 1 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1.0, length\_scale\_bounds\=(1e-2, 1e2))
gaussian\_process \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, n\_restarts\_optimizer\=9)
gaussian\_process.fit(X\_train, y\_train)
gaussian\_process.kernel\_

Copy to clipboard

5.02\*\*2 \* RBF(length\_scale=1.43)

Copy to clipboard

After fitting our model, we see that the hyperparameters of the kernel have been optimized. Now, we will use our kernel to compute the mean prediction of the full dataset and plot the 95% confidence interval.

mean\_prediction, std\_prediction \= gaussian\_process.predict(X, return\_std\=True)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\=r"$f(x) = x \\sin(x)$", linestyle\="dotted")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train, y\_train, label\="Observations")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, mean\_prediction, label\="Mean prediction")
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    X.ravel(),
    mean\_prediction \- 1.96 \* std\_prediction,
    mean\_prediction + 1.96 \* std\_prediction,
    alpha\=0.5,
    label\=r"95% confidence interval",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$f(x)$")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Gaussian process regression on noise-free dataset")

Copy to clipboard

![Gaussian process regression on noise-free dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_002.png)

We see that for a prediction made on a data point close to the one from the training set, the 95% confidence has a small amplitude. Whenever a sample falls far from training data, our model’s prediction is less accurate and the model prediction is less precise (higher uncertainty).

Example with noisy targets[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#example-with-noisy-targets "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can repeat a similar experiment adding an additional noise to the target this time. It will allow seeing the effect of the noise on the fitted model.

We add some random Gaussian noise to the target with an arbitrary standard deviation.

noise\_std \= 0.75
y\_train\_noisy \= y\_train + rng.normal(loc\=0.0, scale\=noise\_std, size\=y\_train.shape)

Copy to clipboard

We create a similar Gaussian process model. In addition to the kernel, this time, we specify the parameter `alpha` which can be interpreted as the variance of a Gaussian noise.

gaussian\_process \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(
    kernel\=kernel, alpha\=noise\_std\*\*2, n\_restarts\_optimizer\=9
)
gaussian\_process.fit(X\_train, y\_train\_noisy)
mean\_prediction, std\_prediction \= gaussian\_process.predict(X, return\_std\=True)

Copy to clipboard

Let’s plot the mean prediction and the uncertainty region as before.

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\=r"$f(x) = x \\sin(x)$", linestyle\="dotted")
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    X\_train,
    y\_train\_noisy,
    noise\_std,
    linestyle\="None",
    color\="tab:blue",
    marker\=".",
    markersize\=10,
    label\="Observations",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, mean\_prediction, label\="Mean prediction")
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    X.ravel(),
    mean\_prediction \- 1.96 \* std\_prediction,
    mean\_prediction + 1.96 \* std\_prediction,
    color\="tab:orange",
    alpha\=0.5,
    label\=r"95% confidence interval",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$f(x)$")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Gaussian process regression on a noisy dataset")

Copy to clipboard

![Gaussian process regression on a noisy dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_003.png)

The noise affects the predictions close to the training samples: the predictive uncertainty near to the training samples is larger because we explicitly model a given level target noise independent of the input variable.

**Total running time of the script:** (0 minutes 0.475 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_noisy_targets.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_noisy_targets.ipynb)

[`Download Jupyter notebook: plot_gpr_noisy_targets.ipynb`](https://scikit-learn.org/stable/_downloads/517bdba67b49ba04ad16cff789c15fba/plot_gpr_noisy_targets.ipynb)

[`Download Python source code: plot_gpr_noisy_targets.py`](https://scikit-learn.org/stable/_downloads/ba8fe72a3ef4d20bcdd7f2c95e635271/plot_gpr_noisy_targets.py)

[`Download zipped: plot_gpr_noisy_targets.zip`](https://scikit-learn.org/stable/_downloads/82c79cb352203b04e0caab27b7e3f5e7/plot_gpr_noisy_targets.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_thumb.png)

[Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Comparison of kernel ridge and Gaussian process regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_thumb.png)

[Ability of Gaussian process regression (GPR) to estimate data noise-level](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)

Ability of Gaussian process regression (GPR) to estimate data noise-level

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_thumb.png)

[Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html)

Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ba8fe72a3ef4d20bcdd7f2c95e635271/plot_gpr_noisy_targets.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/517bdba67b49ba04ad16cff789c15fba/plot_gpr_noisy_targets.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/82c79cb352203b04e0caab27b7e3f5e7/plot_gpr_noisy_targets.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_noisy_targets.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_noisy_targets.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)