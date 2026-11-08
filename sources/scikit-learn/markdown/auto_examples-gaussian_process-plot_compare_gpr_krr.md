[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_compare_gpr_krr.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_compare_gpr_krr.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_compare_gpr_krr.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_compare_gpr_krr.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_compare_gpr_krr.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#sphx-glr-download-auto-examples-gaussian-process-plot-compare-gpr-krr-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of kernel ridge and Gaussian process regression[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#comparison-of-kernel-ridge-and-gaussian-process-regression "Link to this heading")

==========================================================================================================================================================================================================================================

This example illustrates differences between a kernel ridge regression and a Gaussian process regression.

Both kernel ridge regression and Gaussian process regression are using a so-called “kernel trick” to make their models expressive enough to fit the training data. However, the machine learning problems solved by the two methods are drastically different.

Kernel ridge regression will find the target function that minimizes a loss function (the mean squared error).

Instead of finding a single target function, the Gaussian process regression employs a probabilistic approach : a Gaussian posterior distribution over target functions is defined based on the Bayes’ theorem, Thus prior probabilities on target functions are being combined with a likelihood function defined by the observed training data to provide estimates of the posterior distributions.

We will illustrate these differences with an example and we will also focus on tuning the kernel hyperparameters.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generating a dataset[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#generating-a-dataset "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

We create a synthetic dataset. The true generative process will take a 1-D vector and compute its sine. Note that the period of this sine is thus 2π. We will reuse this information later in this example.

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
data \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 30, num\=1\_000).reshape(\-1, 1)
target \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(data).ravel()

Copy to clipboard

Now, we can imagine a scenario where we get observations from this true process. However, we will add some challenges:

*   the measurements will be noisy;
    
*   only samples from the beginning of the signal will be available.
    

training\_sample\_indices \= rng.choice([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 400), size\=40, replace\=False)
training\_data \= data\[training\_sample\_indices\]
training\_noisy\_target \= target\[training\_sample\_indices\] + 0.5 \* rng.randn(
    len(training\_sample\_indices)
)

Copy to clipboard

Let’s plot the true signal and the noisy measurements available for training.

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, target, label\="True signal", linewidth\=2)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    training\_data,
    training\_noisy\_target,
    color\="black",
    label\="Noisy measurements",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Illustration of the true generative process and \\n"
    "noisy measurements available during training"
)

Copy to clipboard

![Illustration of the true generative process and  noisy measurements available during training](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_001.png)

Limitations of a simple linear model[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#limitations-of-a-simple-linear-model "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we would like to highlight the limitations of a linear model given our dataset. We fit a [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 and check the predictions of this model on our dataset.

from sklearn.linear\_model import [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")

ridge \= [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
().fit(training\_data, training\_noisy\_target)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, target, label\="True signal", linewidth\=2)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    training\_data,
    training\_noisy\_target,
    color\="black",
    label\="Noisy measurements",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, ridge.predict(data), label\="Ridge regression")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Limitation of a linear model such as ridge")

Copy to clipboard

![Limitation of a linear model such as ridge](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_002.png)

Such a ridge regressor underfits data since it is not expressive enough.

Kernel methods: kernel ridge and Gaussian process[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#kernel-methods-kernel-ridge-and-gaussian-process "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Kernel ridge[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#kernel-ridge "Link to this heading")

We can make the previous linear model more expressive by using a so-called kernel. A kernel is an embedding from the original feature space to another one. Simply put, it is used to map our original data into a newer and more complex feature space. This new space is explicitly defined by the choice of kernel.

In our case, we know that the true generative process is a periodic function. We can use a [`ExpSineSquared`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
 kernel which allows recovering the periodicity. The class [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 will accept such a kernel.

Using this model together with a kernel is equivalent to embed the data using the mapping function of the kernel and then apply a ridge regression. In practice, the data are not mapped explicitly; instead the dot product between samples in the higher dimensional feature space is computed using the “kernel trick”.

Thus, let’s use such a [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
.

import time

from sklearn.gaussian\_process.kernels import [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
from sklearn.kernel\_ridge import [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")

kernel\_ridge \= [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
(kernel\=[ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
())

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
kernel\_ridge.fit(training\_data, training\_noisy\_target)
print(
    f"Fitting KernelRidge with default kernel: {[time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.3f} seconds"
)

Copy to clipboard

Fitting KernelRidge with default kernel: 0.001 seconds

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, target, label\="True signal", linewidth\=2, linestyle\="dashed")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    training\_data,
    training\_noisy\_target,
    color\="black",
    label\="Noisy measurements",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    data,
    kernel\_ridge.predict(data),
    label\="Kernel ridge",
    linewidth\=2,
    linestyle\="dashdot",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Kernel ridge regression with an exponential sine squared\\n "
    "kernel using default hyperparameters"
)

Copy to clipboard

![Kernel ridge regression with an exponential sine squared  kernel using default hyperparameters](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_003.png)

This fitted model is not accurate. Indeed, we did not set the parameters of the kernel and instead used the default ones. We can inspect them.

kernel\_ridge.kernel

Copy to clipboard

ExpSineSquared(length\_scale=1, periodicity=1)

Copy to clipboard

Our kernel has two parameters: the length-scale and the periodicity. For our dataset, we use `sin` as the generative process, implying a 2π\-periodicity for the signal. The default value of the parameter being 1, it explains the high frequency observed in the predictions of our model. Similar conclusions could be drawn with the length-scale parameter. Thus, it tells us that the kernel parameters need to be tuned. We will use a randomized search to tune the different parameters the kernel ridge model: the `alpha` parameter and the kernel parameters.

from scipy.stats import [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")

from sklearn.model\_selection import [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")

param\_distributions \= {
    "alpha": [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")
(1e0, 1e3),
    "kernel\_\_length\_scale": [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")
(1e-2, 1e2),
    "kernel\_\_periodicity": [loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")
(1e0, 1e1),
}
kernel\_ridge\_tuned \= [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
(
    kernel\_ridge,
    param\_distributions\=param\_distributions,
    n\_iter\=500,
    random\_state\=0,
)
start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
kernel\_ridge\_tuned.fit(training\_data, training\_noisy\_target)
print(f"Time for KernelRidge fitting: {[time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.3f} seconds")

Copy to clipboard

Time for KernelRidge fitting: 4.468 seconds

Copy to clipboard

Fitting the model is now more computationally expensive since we have to try several combinations of hyperparameters. We can have a look at the hyperparameters found to get some intuitions.

kernel\_ridge\_tuned.best\_params\_

Copy to clipboard

{'alpha': np.float64(1.991584977345022), 'kernel\_\_length\_scale': np.float64(0.7986499491396734), 'kernel\_\_periodicity': np.float64(6.6072758064261095)}

Copy to clipboard

Looking at the best parameters, we see that they are different from the defaults. We also see that the periodicity is closer to the expected value: 2π. We can now inspect the predictions of our tuned kernel ridge.

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
predictions\_kr \= kernel\_ridge\_tuned.predict(data)
print(f"Time for KernelRidge predict: {[time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.3f} seconds")

Copy to clipboard

Time for KernelRidge predict: 0.001 seconds

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, target, label\="True signal", linewidth\=2, linestyle\="dashed")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    training\_data,
    training\_noisy\_target,
    color\="black",
    label\="Noisy measurements",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    data,
    predictions\_kr,
    label\="Kernel ridge",
    linewidth\=2,
    linestyle\="dashdot",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Kernel ridge regression with an exponential sine squared\\n "
    "kernel using tuned hyperparameters"
)

Copy to clipboard

![Kernel ridge regression with an exponential sine squared  kernel using tuned hyperparameters](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_004.png)

We get a much more accurate model. We still observe some errors mainly due to the noise added to the dataset.

### Gaussian process regression[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#gaussian-process-regression "Link to this heading")

Now, we will use a [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
 to fit the same dataset. When training a Gaussian process, the hyperparameters of the kernel are optimized during the fitting process. There is no need for an external hyperparameter search. Here, we create a slightly more complex kernel than for the kernel ridge regressor: we add a [`WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
 that is used to estimate the noise in the dataset.

from sklearn.gaussian\_process import [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
from sklearn.gaussian\_process.kernels import [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")

kernel \= 1.0 \* [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
(1.0, 5.0, periodicity\_bounds\=(1e-2, 1e1)) + [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
(
    1e-1
)
gaussian\_process \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel)
start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
gaussian\_process.fit(training\_data, training\_noisy\_target)
print(
    f"Time for GaussianProcessRegressor fitting: {[time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.3f} seconds"
)

Copy to clipboard

Time for GaussianProcessRegressor fitting: 0.024 seconds

Copy to clipboard

The computation cost of training a Gaussian process is much less than the kernel ridge that uses a randomized search. We can check the parameters of the kernels that we computed.

gaussian\_process.kernel\_

Copy to clipboard

0.675\*\*2 \* ExpSineSquared(length\_scale=1.34, periodicity=6.57) + WhiteKernel(noise\_level=0.182)

Copy to clipboard

Indeed, we see that the parameters have been optimized. Looking at the `periodicity` parameter, we see that we found a period close to the theoretical value 2π. We can have a look now at the predictions of our model.

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mean\_predictions\_gpr, std\_predictions\_gpr \= gaussian\_process.predict(
    data,
    return\_std\=True,
)
print(
    f"Time for GaussianProcessRegressor predict: {[time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time:.3f} seconds"
)

Copy to clipboard

Time for GaussianProcessRegressor predict: 0.002 seconds

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, target, label\="True signal", linewidth\=2, linestyle\="dashed")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    training\_data,
    training\_noisy\_target,
    color\="black",
    label\="Noisy measurements",
)
\# Plot the predictions of the kernel ridge
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    data,
    predictions\_kr,
    label\="Kernel ridge",
    linewidth\=2,
    linestyle\="dashdot",
)
\# Plot the predictions of the gaussian process regressor
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    data,
    mean\_predictions\_gpr,
    label\="Gaussian process regressor",
    linewidth\=2,
    linestyle\="dotted",
)
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    data.ravel(),
    mean\_predictions\_gpr \- std\_predictions\_gpr,
    mean\_predictions\_gpr + std\_predictions\_gpr,
    color\="tab:green",
    alpha\=0.2,
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Comparison between kernel ridge and gaussian process regressor")

Copy to clipboard

![Comparison between kernel ridge and gaussian process regressor](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_005.png)

We observe that the results of the kernel ridge and the Gaussian process regressor are close. However, the Gaussian process regressor also provide an uncertainty information that is not available with a kernel ridge. Due to the probabilistic formulation of the target functions, the Gaussian process can output the standard deviation (or the covariance) together with the mean predictions of the target functions.

However, it comes at a cost: the time to compute the predictions is higher with a Gaussian process.

Final conclusion[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#final-conclusion "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

We can give a final word regarding the possibility of the two models to extrapolate. Indeed, we only provided the beginning of the signal as a training set. Using a periodic kernel forces our model to repeat the pattern found on the training set. Using this kernel information together with the capacity of the both models to extrapolate, we observe that the models will continue to predict the sine pattern.

Gaussian process allows to combine kernels together. Thus, we could associate the exponential sine squared kernel together with a radial basis function kernel.

from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")

kernel \= 1.0 \* [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
(1.0, 5.0, periodicity\_bounds\=(1e-2, 1e1)) \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(
    length\_scale\=15, length\_scale\_bounds\="fixed"
) + [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
(1e-1)
gaussian\_process \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel)
gaussian\_process.fit(training\_data, training\_noisy\_target)
mean\_predictions\_gpr, std\_predictions\_gpr \= gaussian\_process.predict(
    data,
    return\_std\=True,
)

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(data, target, label\="True signal", linewidth\=2, linestyle\="dashed")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    training\_data,
    training\_noisy\_target,
    color\="black",
    label\="Noisy measurements",
)
\# Plot the predictions of the kernel ridge
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    data,
    predictions\_kr,
    label\="Kernel ridge",
    linewidth\=2,
    linestyle\="dashdot",
)
\# Plot the predictions of the gaussian process regressor
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    data,
    mean\_predictions\_gpr,
    label\="Gaussian process regressor",
    linewidth\=2,
    linestyle\="dotted",
)
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    data.ravel(),
    mean\_predictions\_gpr \- std\_predictions\_gpr,
    mean\_predictions\_gpr + std\_predictions\_gpr,
    color\="tab:green",
    alpha\=0.2,
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Effect of using a radial basis function kernel")

Copy to clipboard

![Effect of using a radial basis function kernel](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_006.png)

The effect of using a radial basis function kernel will attenuate the periodicity effect once that no sample are available in the training. As testing samples get further away from the training ones, predictions are converging towards their mean and their standard deviation also increases.

**Total running time of the script:** (0 minutes 5.149 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_compare_gpr_krr.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_compare_gpr_krr.ipynb)

[`Download Jupyter notebook: plot_compare_gpr_krr.ipynb`](https://scikit-learn.org/stable/_downloads/c3bc3113489c0b7c9a698b430d691ddc/plot_compare_gpr_krr.ipynb)

[`Download Python source code: plot_compare_gpr_krr.py`](https://scikit-learn.org/stable/_downloads/c499f9c8abaa56c9b615349a539cb6ae/plot_compare_gpr_krr.py)

[`Download zipped: plot_compare_gpr_krr.zip`](https://scikit-learn.org/stable/_downloads/fbde8dfb8bd7af110ec5f186216b4186/plot_compare_gpr_krr.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_thumb.png)

[HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)

HuberRegressor vs Ridge on dataset with strong outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)

[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)

Plot Ridge coefficients as a function of the regularization

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/c499f9c8abaa56c9b615349a539cb6ae/plot_compare_gpr_krr.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c3bc3113489c0b7c9a698b430d691ddc/plot_compare_gpr_krr.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/fbde8dfb8bd7af110ec5f186216b4186/plot_compare_gpr_krr.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_compare_gpr_krr.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_compare_gpr_krr.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)