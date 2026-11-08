[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpr-prior-posterior-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Illustration of prior and posterior Gaussian process for different kernels[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#illustration-of-prior-and-posterior-gaussian-process-for-different-kernels "Link to this heading")

==============================================================================================================================================================================================================================================================================

This example illustrates the prior and posterior of a [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
 with different kernels. Mean, standard deviation, and 5 samples are shown for both prior and posterior distributions.

Here, we only give some illustration. To know more about kernels’ formulation, refer to the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Helper function[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#helper-function "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Before presenting each individual kernel available for Gaussian processes, we will define a helper function allowing us plotting samples drawn from the Gaussian process.

This function will take a [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
 model and will drawn sample from the Gaussian process. If the model was not fit, the samples are drawn from the prior distribution while after model fitting, the samples are drawn from the posterior distribution.

import matplotlib.pyplot as plt
import numpy as np

def plot\_gpr\_samples(gpr\_model, n\_samples, ax):
    """Plot samples drawn from the Gaussian process model.

    If the Gaussian process model is not trained then the drawn samples are
    drawn from the prior distribution. Otherwise, the samples are drawn from
    the posterior distribution. Be aware that a sample here corresponds to a
    function.

    Parameters
    ----------
    gpr\_model : \`GaussianProcessRegressor\`
        A :class:\`~sklearn.gaussian\_process.GaussianProcessRegressor\` model.
    n\_samples : int
        The number of samples to draw from the Gaussian process distribution.
    ax : matplotlib axis
        The matplotlib axis where to plot the samples.
    """
    x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, 100)
    X \= x.reshape(\-1, 1)

    y\_mean, y\_std \= gpr\_model.predict(X, return\_std\=True)
    y\_samples \= gpr\_model.sample\_y(X, n\_samples)

    for idx, single\_prior in enumerate(y\_samples.T):
        ax.plot(
            x,
            single\_prior,
            linestyle\="--",
            alpha\=0.7,
            label\=f"Sampled function #{idx + 1}",
        )
    ax.plot(x, y\_mean, color\="black", label\="Mean")
    ax.fill\_between(
        x,
        y\_mean \- y\_std,
        y\_mean + y\_std,
        alpha\=0.1,
        color\="black",
        label\=r"$\\pm$ 1 std. dev.",
    )
    ax.set\_xlabel("x")
    ax.set\_ylabel("y")
    ax.set\_ylim(\[\-3, 3\])

Copy to clipboard

Dataset and Gaussian process generation[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#dataset-and-gaussian-process-generation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will create a training dataset that we will use in the different sections.

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(4)
X\_train \= rng.uniform(0, 5, 10).reshape(\-1, 1)
y\_train \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
((X\_train\[:, 0\] \- 2.5) \*\* 2)
n\_samples \= 5

Copy to clipboard

Kernel cookbook[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#kernel-cookbook "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we illustrate some samples drawn from the prior and posterior distributions of the Gaussian process with different kernels.

### Radial Basis Function kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#radial-basis-function-kernel "Link to this heading")

from sklearn.gaussian\_process import [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")

kernel \= 1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1.0, length\_scale\_bounds\=(1e-1, 10.0))
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, random\_state\=0)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True, sharey\=True, figsize\=(10, 8))

\# plot prior
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[0\])
axs\[0\].set\_title("Samples from prior distribution")

\# plot posterior
gpr.fit(X\_train, y\_train)
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[1\])
axs\[1\].scatter(X\_train\[:, 0\], y\_train, color\="red", zorder\=10, label\="Observations")
axs\[1\].legend(bbox\_to\_anchor\=(1.05, 1.5), loc\="upper left")
axs\[1\].set\_title("Samples from posterior distribution")

fig.suptitle("Radial Basis Function kernel", fontsize\=18)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Radial Basis Function kernel, Samples from prior distribution, Samples from posterior distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_001.png)

print(f"Kernel parameters before fit:\\n{kernel})")
print(
    f"Kernel parameters after fit: \\n{gpr.kernel\_} \\n"
    f"Log-likelihood: {gpr.log\_marginal\_likelihood(gpr.kernel\_.theta):.3f}"
)

Copy to clipboard

Kernel parameters before fit:
1\*\*2 \* RBF(length\_scale=1))
Kernel parameters after fit:
0.594\*\*2 \* RBF(length\_scale=0.279)
Log-likelihood: -0.067

Copy to clipboard

### Rational Quadratic kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#rational-quadratic-kernel "Link to this heading")

from sklearn.gaussian\_process.kernels import [RationalQuadratic](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "sklearn.gaussian_process.kernels.RationalQuadratic")

kernel \= 1.0 \* [RationalQuadratic](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "sklearn.gaussian_process.kernels.RationalQuadratic")
(length\_scale\=1.0, alpha\=0.1, alpha\_bounds\=(1e-5, 1e15))
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, random\_state\=0)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True, sharey\=True, figsize\=(10, 8))

\# plot prior
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[0\])
axs\[0\].set\_title("Samples from prior distribution")

\# plot posterior
gpr.fit(X\_train, y\_train)
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[1\])
axs\[1\].scatter(X\_train\[:, 0\], y\_train, color\="red", zorder\=10, label\="Observations")
axs\[1\].legend(bbox\_to\_anchor\=(1.05, 1.5), loc\="upper left")
axs\[1\].set\_title("Samples from posterior distribution")

fig.suptitle("Rational Quadratic kernel", fontsize\=18)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Rational Quadratic kernel, Samples from prior distribution, Samples from posterior distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_002.png)

/home/circleci/project/sklearn/gaussian\_process/\_gpr.py:530: RuntimeWarning: covariance is not symmetric positive-semidefinite.
  y\_samples = rng.multivariate\_normal(y\_mean, y\_cov, n\_samples).T

Copy to clipboard

print(f"Kernel parameters before fit:\\n{kernel})")
print(
    f"Kernel parameters after fit: \\n{gpr.kernel\_} \\n"
    f"Log-likelihood: {gpr.log\_marginal\_likelihood(gpr.kernel\_.theta):.3f}"
)

Copy to clipboard

Kernel parameters before fit:
1\*\*2 \* RationalQuadratic(alpha=0.1, length\_scale=1))
Kernel parameters after fit:
0.594\*\*2 \* RationalQuadratic(alpha=1.1e+07, length\_scale=0.279)
Log-likelihood: -0.067

Copy to clipboard

### Exp-Sine-Squared kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#exp-sine-squared-kernel "Link to this heading")

from sklearn.gaussian\_process.kernels import [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")

kernel \= 1.0 \* [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
(
    length\_scale\=1.0,
    periodicity\=3.0,
    length\_scale\_bounds\=(0.1, 10.0),
    periodicity\_bounds\=(1.0, 10.0),
)
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, random\_state\=0)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True, sharey\=True, figsize\=(10, 8))

\# plot prior
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[0\])
axs\[0\].set\_title("Samples from prior distribution")

\# plot posterior
gpr.fit(X\_train, y\_train)
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[1\])
axs\[1\].scatter(X\_train\[:, 0\], y\_train, color\="red", zorder\=10, label\="Observations")
axs\[1\].legend(bbox\_to\_anchor\=(1.05, 1.5), loc\="upper left")
axs\[1\].set\_title("Samples from posterior distribution")

fig.suptitle("Exp-Sine-Squared kernel", fontsize\=18)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Exp-Sine-Squared kernel, Samples from prior distribution, Samples from posterior distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_003.png)

print(f"Kernel parameters before fit:\\n{kernel})")
print(
    f"Kernel parameters after fit: \\n{gpr.kernel\_} \\n"
    f"Log-likelihood: {gpr.log\_marginal\_likelihood(gpr.kernel\_.theta):.3f}"
)

Copy to clipboard

Kernel parameters before fit:
1\*\*2 \* ExpSineSquared(length\_scale=1, periodicity=3))
Kernel parameters after fit:
0.799\*\*2 \* ExpSineSquared(length\_scale=0.791, periodicity=2.87)
Log-likelihood: 3.394

Copy to clipboard

### Dot-product kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#dot-product-kernel "Link to this heading")

from sklearn.gaussian\_process.kernels import [ConstantKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ConstantKernel.html#sklearn.gaussian_process.kernels.ConstantKernel "sklearn.gaussian_process.kernels.ConstantKernel")
, [DotProduct](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")

kernel \= [ConstantKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ConstantKernel.html#sklearn.gaussian_process.kernels.ConstantKernel "sklearn.gaussian_process.kernels.ConstantKernel")
(0.1, (0.01, 10.0)) \* (
    [DotProduct](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")
(sigma\_0\=1.0, sigma\_0\_bounds\=(0.1, 10.0)) \*\* 2
)
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, random\_state\=0, normalize\_y\=True)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True, sharey\=True, figsize\=(10, 8))

\# plot prior
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[0\])
axs\[0\].set\_title("Samples from prior distribution")

\# plot posterior
gpr.fit(X\_train, y\_train)
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[1\])
axs\[1\].scatter(X\_train\[:, 0\], y\_train, color\="red", zorder\=10, label\="Observations")
axs\[1\].legend(bbox\_to\_anchor\=(1.05, 1.5), loc\="upper left")
axs\[1\].set\_title("Samples from posterior distribution")

fig.suptitle("Dot-product kernel", fontsize\=18)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Dot-product kernel, Samples from prior distribution, Samples from posterior distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_004.png)

print(f"Kernel parameters before fit:\\n{kernel})")
print(
    f"Kernel parameters after fit: \\n{gpr.kernel\_} \\n"
    f"Log-likelihood: {gpr.log\_marginal\_likelihood(gpr.kernel\_.theta):.3f}"
)

Copy to clipboard

Kernel parameters before fit:
0.316\*\*2 \* DotProduct(sigma\_0=1) \*\* 2)
Kernel parameters after fit:
0.316\*\*2 \* DotProduct(sigma\_0=1) \*\* 2
Log-likelihood: -18108740473.516

Copy to clipboard

### Matérn kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html#matern-kernel "Link to this heading")

from sklearn.gaussian\_process.kernels import [Matern](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "sklearn.gaussian_process.kernels.Matern")

kernel \= 1.0 \* [Matern](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "sklearn.gaussian_process.kernels.Matern")
(length\_scale\=1.0, length\_scale\_bounds\=(1e-1, 10.0), nu\=1.5)
gpr \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel, random\_state\=0)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True, sharey\=True, figsize\=(10, 8))

\# plot prior
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[0\])
axs\[0\].set\_title("Samples from prior distribution")

\# plot posterior
gpr.fit(X\_train, y\_train)
plot\_gpr\_samples(gpr, n\_samples\=n\_samples, ax\=axs\[1\])
axs\[1\].scatter(X\_train\[:, 0\], y\_train, color\="red", zorder\=10, label\="Observations")
axs\[1\].legend(bbox\_to\_anchor\=(1.05, 1.5), loc\="upper left")
axs\[1\].set\_title("Samples from posterior distribution")

fig.suptitle("Matérn kernel", fontsize\=18)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Matérn kernel, Samples from prior distribution, Samples from posterior distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_005.png)

print(f"Kernel parameters before fit:\\n{kernel})")
print(
    f"Kernel parameters after fit: \\n{gpr.kernel\_} \\n"
    f"Log-likelihood: {gpr.log\_marginal\_likelihood(gpr.kernel\_.theta):.3f}"
)

Copy to clipboard

Kernel parameters before fit:
1\*\*2 \* Matern(length\_scale=1, nu=1.5))
Kernel parameters after fit:
0.609\*\*2 \* Matern(length\_scale=0.484, nu=1.5)
Log-likelihood: -1.185

Copy to clipboard

**Total running time of the script:** (0 minutes 1.403 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_prior_posterior.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_prior_posterior.ipynb)

[`Download Jupyter notebook: plot_gpr_prior_posterior.ipynb`](https://scikit-learn.org/stable/_downloads/75a08bb798ae7156529a808a0e08e7b4/plot_gpr_prior_posterior.ipynb)

[`Download Python source code: plot_gpr_prior_posterior.py`](https://scikit-learn.org/stable/_downloads/1bcb2039afa126da41f1cea42b4a5866/plot_gpr_prior_posterior.py)

[`Download zipped: plot_gpr_prior_posterior.zip`](https://scikit-learn.org/stable/_downloads/21a52befdcfce43d65a7b00dc6414056/plot_gpr_prior_posterior.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_thumb.png)

[Ability of Gaussian process regression (GPR) to estimate data noise-level](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)

Ability of Gaussian process regression (GPR) to estimate data noise-level

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_thumb.png)

[Demonstration of k-means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html)

Demonstration of k-means assumptions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/1bcb2039afa126da41f1cea42b4a5866/plot_gpr_prior_posterior.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/75a08bb798ae7156529a808a0e08e7b4/plot_gpr_prior_posterior.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/21a52befdcfce43d65a7b00dc6414056/plot_gpr_prior_posterior.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_prior_posterior.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_prior_posterior.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)