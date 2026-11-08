[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpr_noisy.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpr_noisy.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpr_noisy.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpr_noisy.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpr_noisy.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpr_noisy.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpr-noisy-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Ability of Gaussian process regression (GPR) to estimate data noise-level[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html#ability-of-gaussian-process-regression-gpr-to-estimate-data-noise-level "Link to this heading")

================================================================================================================================================================================================================================================================

This example shows the ability of the [`WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
 to estimate the noise level in the data. Moreover, we show the importance of kernel hyperparameters initialization.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html#data-generation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

We will work in a setting where `X` will contain a single feature. We create a function that will generate the target to be predicted. We will add an option to add some noise to the generated target.

import numpy as np

def target\_generator(X, add\_noise\=False):
    target \= 0.5 + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(3 \* X)
    if add\_noise:
        rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
        target += rng.normal(0, 0.3, size\=target.shape)
    return target.squeeze()

Copy to clipboard

Let’s have a look to the target generator where we will not add any noise to observe the signal that we would like to predict.

X \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, num\=80).reshape(\-1, 1)
y \= target\_generator(X, add\_noise\=False)

Copy to clipboard

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\="Expected signal")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X")
\_ \= [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")

Copy to clipboard

![plot gpr noisy](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_001.png)

The target is transforming the input `X` using a sine function. Now, we will generate few noisy training samples. To illustrate the noise level, we will plot the true signal together with the noisy training samples.

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X\_train \= rng.uniform(0, 5, size\=20).reshape(\-1, 1)
y\_train \= target\_generator(X\_train, add\_noise\=True)

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\="Expected signal")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    x\=X\_train\[:, 0\],
    y\=y\_train,
    color\="black",
    alpha\=0.4,
    label\="Observations",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X")
\_ \= [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")

Copy to clipboard

![plot gpr noisy](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_002.png)

Optimisation of kernel hyperparameters in GPR[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html#optimisation-of-kernel-hyperparameters-in-gpr "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we will create a [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
 using an additive kernel adding a [`RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
 and [`WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
 kernels. The [`WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
 is a kernel that will able to estimate the amount of noise present in the data while the [`RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
 will serve at fitting the non-linearity between the data and the target.

However, we will show that the hyperparameter space contains several local minima. It will highlights the importance of initial hyperparameter values.

We will create a model using a kernel with a high noise level and a large length scale, which will explain all variations in the data by noise.

from sklearn.gaussian\_process import [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
, [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")

kernel \= 1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1e1, length\_scale\_bounds\=(1e-2, 1e3)) + [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
(
    noise\_level\=1, noise\_level\_bounds\=(1e-10, 1e1)
)
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, alpha\=0.0)
gpr.fit(X\_train, y\_train)
y\_mean, y\_std \= gpr.predict(X, return\_std\=True)

Copy to clipboard

/home/circleci/project/sklearn/gaussian\_process/kernels.py:455: ConvergenceWarning: The optimal value found for dimension 0 of parameter k1\_\_k2\_\_length\_scale is close to the specified upper bound 1000.0. Increasing the bound and calling fit again may find a better value.
  warnings.warn(

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\="Expected signal")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(x\=X\_train\[:, 0\], y\=y\_train, color\="black", alpha\=0.4, label\="Observations")
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(X, y\_mean, y\_std, label\="Posterior mean ± std")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    (
        f"Initial: {kernel}\\nOptimum: {gpr.kernel\_}\\nLog-Marginal-Likelihood: "
        f"{gpr.log\_marginal\_likelihood(gpr.kernel\_.theta)}"
    ),
    fontsize\=8,
)

Copy to clipboard

![Initial: 1**2 * RBF(length_scale=10) + WhiteKernel(noise_level=1) Optimum: 0.763**2 * RBF(length_scale=1e+03) + WhiteKernel(noise_level=0.525) Log-Marginal-Likelihood: -23.49926645542419](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_003.png)

We see that the optimum kernel found still has a high noise level and an even larger length scale. The length scale reaches the maximum bound that we allowed for this parameter and we got a warning as a result.

More importantly, we observe that the model does not provide useful predictions: the mean prediction seems to be constant: it does not follow the expected noise-free signal.

Now, we will initialize the [`RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
 with a larger `length_scale` initial value and the [`WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
 with a smaller initial noise level lower while keeping the parameter bounds unchanged.

kernel \= 1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1e-1, length\_scale\_bounds\=(1e-2, 1e3)) + [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
(
    noise\_level\=1e-2, noise\_level\_bounds\=(1e-10, 1e1)
)
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, alpha\=0.0)
gpr.fit(X\_train, y\_train)
y\_mean, y\_std \= gpr.predict(X, return\_std\=True)

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\="Expected signal")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(x\=X\_train\[:, 0\], y\=y\_train, color\="black", alpha\=0.4, label\="Observations")
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(X, y\_mean, y\_std, label\="Posterior mean ± std")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    (
        f"Initial: {kernel}\\nOptimum: {gpr.kernel\_}\\nLog-Marginal-Likelihood: "
        f"{gpr.log\_marginal\_likelihood(gpr.kernel\_.theta)}"
    ),
    fontsize\=8,
)

Copy to clipboard

![Initial: 1**2 * RBF(length_scale=0.1) + WhiteKernel(noise_level=0.01) Optimum: 1.05**2 * RBF(length_scale=0.569) + WhiteKernel(noise_level=0.134) Log-Marginal-Likelihood: -18.429732528984058](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_004.png)

First, we see that the model’s predictions are more precise than the previous model’s: this new model is able to estimate the noise-free functional relationship.

Looking at the kernel hyperparameters, we see that the best combination found has a smaller noise level and shorter length scale than the first model.

We can inspect the negative Log-Marginal-Likelihood (LML) of [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
 for different hyperparameters to get a sense of the local minima.

from matplotlib.colors import [LogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")

length\_scale \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 4, num\=80)
noise\_level \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 1, num\=80)
length\_scale\_grid, noise\_level\_grid \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(length\_scale, noise\_level)

log\_marginal\_likelihood \= \[\
    gpr.log\_marginal\_likelihood(theta\=[np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")\
(\[0.36, scale, noise\]))\
    for scale, noise in zip(length\_scale\_grid.ravel(), noise\_level\_grid.ravel())\
\]
log\_marginal\_likelihood \= [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(log\_marginal\_likelihood, noise\_level\_grid.shape)

Copy to clipboard

vmin, vmax \= (\-log\_marginal\_likelihood).min(), 50
level \= [np.around](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")
([np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
([np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
(vmin), [np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
(vmax), num\=20), decimals\=1)
[plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(
    length\_scale\_grid,
    noise\_level\_grid,
    \-log\_marginal\_likelihood,
    levels\=level,
    norm\=[LogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
(vmin\=vmin, vmax\=vmax),
)
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()
[plt.xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html#matplotlib.pyplot.xscale "matplotlib.pyplot.xscale")
("log")
[plt.yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")
("log")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Length-scale")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Noise-level")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Negative log-marginal-likelihood")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Negative log-marginal-likelihood](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_005.png)

We see that there are two local minima that correspond to the combination of hyperparameters previously found. Depending on the initial values for the hyperparameters, the gradient-based optimization might or might not converge to the best model. It is thus important to repeat the optimization several times for different initializations. This can be done by setting the `n_restarts_optimizer` parameter of the [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
 class.

Let’s try again to fit our model with the bad initial values but this time with 10 random restarts.

kernel \= 1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1e1, length\_scale\_bounds\=(1e-2, 1e3)) + [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
(
    noise\_level\=1, noise\_level\_bounds\=(1e-10, 1e1)
)
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(
    kernel\=kernel, alpha\=0.0, n\_restarts\_optimizer\=10, random\_state\=0
)
gpr.fit(X\_train, y\_train)
y\_mean, y\_std \= gpr.predict(X, return\_std\=True)

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, label\="Expected signal")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(x\=X\_train\[:, 0\], y\=y\_train, color\="black", alpha\=0.4, label\="Observations")
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(X, y\_mean, y\_std, label\="Posterior mean ± std")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    (
        f"Initial: {kernel}\\nOptimum: {gpr.kernel\_}\\nLog-Marginal-Likelihood: "
        f"{gpr.log\_marginal\_likelihood(gpr.kernel\_.theta)}"
    ),
    fontsize\=8,
)

Copy to clipboard

![Initial: 1**2 * RBF(length_scale=10) + WhiteKernel(noise_level=1) Optimum: 1.05**2 * RBF(length_scale=0.569) + WhiteKernel(noise_level=0.134) Log-Marginal-Likelihood: -18.42973252897085](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_006.png)

As we hoped, random restarts allow the optimization to find the best set of hyperparameters despite the bad initial values.

**Total running time of the script:** (0 minutes 4.126 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_noisy.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_noisy.ipynb)

[`Download Jupyter notebook: plot_gpr_noisy.ipynb`](https://scikit-learn.org/stable/_downloads/9235188b9f885ba3542bf0529565fdfe/plot_gpr_noisy.ipynb)

[`Download Python source code: plot_gpr_noisy.py`](https://scikit-learn.org/stable/_downloads/aaca2576b757b51627adfee40c458ed4/plot_gpr_noisy.py)

[`Download zipped: plot_gpr_noisy.zip`](https://scikit-learn.org/stable/_downloads/12fb3a51f4f60a9be2386b10ccc076cf/plot_gpr_noisy.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_thumb.png)

[Illustration of prior and posterior Gaussian process for different kernels](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)

Illustration of prior and posterior Gaussian process for different kernels

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_thumb.png)

[Probabilistic predictions with Gaussian process classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html)

Probabilistic predictions with Gaussian process classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_thumb.png)

[Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html)

Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/aaca2576b757b51627adfee40c458ed4/plot_gpr_noisy.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/9235188b9f885ba3542bf0529565fdfe/plot_gpr_noisy.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/12fb3a51f4f60a9be2386b10ccc076cf/plot_gpr_noisy.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_noisy.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_noisy.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)