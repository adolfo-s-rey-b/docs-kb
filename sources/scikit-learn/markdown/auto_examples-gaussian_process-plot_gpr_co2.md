[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpr_co2.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpr_co2.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpr_co2.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpr_co2.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpr_co2.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpr_co2.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpr-co2-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#forecasting-of-co2-level-on-mona-loa-dataset-using-gaussian-process-regression-gpr "Link to this heading")

====================================================================================================================================================================================================================================================================================

This example is based on Section 5.4.3 of “Gaussian Processes for Machine Learning” [\[1\]](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#id2)
. It illustrates an example of complex kernel engineering and hyperparameter optimization using gradient ascent on the log-marginal-likelihood. The data consists of the monthly average atmospheric CO2 concentrations (in parts per million by volume (ppm)) collected at the Mauna Loa Observatory in Hawaii, between 1958 and 2001. The objective is to model the CO2 concentration as a function of the time t and extrapolate for years after 2001.

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Build the dataset[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#build-the-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

We will derive a dataset from the Mauna Loa Observatory that collected air samples. We are interested in estimating the concentration of CO2 and extrapolate it for further years. First, we load the original dataset available in OpenML as a pandas dataframe. This will be replaced with Polars once `fetch_openml` adds a native support for it.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

co2 \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=41187, as\_frame\=True)
co2.frame.head()

Copy to clipboard

|     | year | month | day | weight | flag | station | co2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1958 | 3   | 29  | 4   | 0   | MLO | 316.1 |
| 1   | 1958 | 4   | 5   | 6   | 0   | MLO | 317.3 |
| 2   | 1958 | 4   | 12  | 4   | 0   | MLO | 317.6 |
| 3   | 1958 | 4   | 19  | 6   | 0   | MLO | 317.5 |
| 4   | 1958 | 4   | 26  | 2   | 0   | MLO | 316.4 |

  
  

First, we process the original dataframe to create a date column and select it along with the CO2 column.

import polars as pl

co2\_data \= pl.DataFrame(co2.frame\[\["year", "month", "day", "co2"\]\]).select(
    pl.date("year", "month", "day"), "co2"
)
co2\_data.head()

Copy to clipboard

shape: (5, 2)

| date | co2 |
| --- | --- |
| date | f64 |
| --- | --- |
| 1958-03-29 | 316.1 |
| 1958-04-05 | 317.3 |
| 1958-04-12 | 317.6 |
| 1958-04-19 | 317.5 |
| 1958-04-26 | 316.4 |

  
  

co2\_data\["date"\].min(), co2\_data\["date"\].max()

Copy to clipboard

(datetime.date(1958, 3, 29), datetime.date(2001, 12, 29))

Copy to clipboard

We see that we get CO2 concentration for some days from March, 1958 to December, 2001. We can plot the raw information to have a better understanding.

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(co2\_data\["date"\], co2\_data\["co2"\])
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("date")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("CO$\_2$ concentration (ppm)")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Raw air samples measurements from the Mauna Loa Observatory")

Copy to clipboard

![Raw air samples measurements from the Mauna Loa Observatory](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_001.png)

We will preprocess the dataset by taking a monthly average and drop months for which no measurements were collected. Such a processing will have a smoothing effect on the data.

co2\_data \= (
    co2\_data.sort(by\="date")
    .group\_by\_dynamic("date", every\="1mo")
    .agg(pl.col("co2").mean())
    .drop\_nulls()
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(co2\_data\["date"\], co2\_data\["co2"\])
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("date")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Monthly average of CO$\_2$ concentration (ppm)")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Monthly average of air samples measurements\\nfrom the Mauna Loa Observatory"
)

Copy to clipboard

![Monthly average of air samples measurements from the Mauna Loa Observatory](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_002.png)

The idea in this example will be to predict the CO2 concentration in function of the date. We are as well interested in extrapolating for upcoming year after 2001.

As a first step, we will divide the data and the target to estimate. The data being a date, we will convert it into a numeric.

X \= co2\_data.select(
    pl.col("date").dt.year() + pl.col("date").dt.month() / 12
).to\_numpy()
y \= co2\_data\["co2"\].to\_numpy()

Copy to clipboard

Design the proper kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#design-the-proper-kernel "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

To design the kernel to use with our Gaussian process, we can make some assumption regarding the data at hand. We observe that they have several characteristics: we see a long term rising trend, a pronounced seasonal variation and some smaller irregularities. We can use different appropriate kernel that would capture these features.

First, the long term rising trend could be fitted using a radial basis function (RBF) kernel with a large length-scale parameter. The RBF kernel with a large length-scale enforces this component to be smooth. A trending increase is not enforced as to give a degree of freedom to our model. The specific length-scale and the amplitude are free hyperparameters.

from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")

long\_term\_trend\_kernel \= 50.0\*\*2 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=50.0)

Copy to clipboard

The seasonal variation is explained by the periodic exponential sine squared kernel with a fixed periodicity of 1 year. The length-scale of this periodic component, controlling its smoothness, is a free parameter. In order to allow decaying away from exact periodicity, the product with an RBF kernel is taken. The length-scale of this RBF component controls the decay time and is a further free parameter. This type of kernel is also known as locally periodic kernel.

from sklearn.gaussian\_process.kernels import [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")

seasonal\_kernel \= (
    2.0\*\*2
    \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=100.0)
    \* [ExpSineSquared](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")
(length\_scale\=1.0, periodicity\=1.0, periodicity\_bounds\="fixed")
)

Copy to clipboard

The small irregularities are to be explained by a rational quadratic kernel component, whose length-scale and alpha parameter, which quantifies the diffuseness of the length-scales, are to be determined. A rational quadratic kernel is equivalent to an RBF kernel with several length-scale and will better accommodate the different irregularities.

from sklearn.gaussian\_process.kernels import [RationalQuadratic](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "sklearn.gaussian_process.kernels.RationalQuadratic")

irregularities\_kernel \= 0.5\*\*2 \* [RationalQuadratic](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "sklearn.gaussian_process.kernels.RationalQuadratic")
(length\_scale\=1.0, alpha\=1.0)

Copy to clipboard

Finally, the noise in the dataset can be accounted with a kernel consisting of an RBF kernel contribution, which shall explain the correlated noise components such as local weather phenomena, and a white kernel contribution for the white noise. The relative amplitudes and the RBF’s length scale are further free parameters.

from sklearn.gaussian\_process.kernels import [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")

noise\_kernel \= 0.1\*\*2 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=0.1) + [WhiteKernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")
(
    noise\_level\=0.1\*\*2, noise\_level\_bounds\=(1e-5, 1e5)
)

Copy to clipboard

Thus, our final kernel is an addition of all previous kernel.

co2\_kernel \= (
    long\_term\_trend\_kernel + seasonal\_kernel + irregularities\_kernel + noise\_kernel
)
co2\_kernel

Copy to clipboard

50\*\*2 \* RBF(length\_scale=50) + 2\*\*2 \* RBF(length\_scale=100) \* ExpSineSquared(length\_scale=1, periodicity=1) + 0.5\*\*2 \* RationalQuadratic(alpha=1, length\_scale=1) + 0.1\*\*2 \* RBF(length\_scale=0.1) + WhiteKernel(noise\_level=0.01)

Copy to clipboard

Model fitting and extrapolation[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#model-fitting-and-extrapolation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we are ready to use a Gaussian process regressor and fit the available data. To follow the example from the literature, we will subtract the mean from the target. We could have used `normalize_y=True`. However, doing so would have also scaled the target (dividing `y` by its standard deviation). Thus, the hyperparameters of the different kernel would have had different meaning since they would not have been expressed in ppm.

from sklearn.gaussian\_process import [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")

y\_mean \= y.mean()
gaussian\_process \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=co2\_kernel, normalize\_y\=False)
gaussian\_process.fit(X, y \- y\_mean)

Copy to clipboard

GaussianProcessRegressor(kernel=50\*\*2 \* RBF(length\_scale=50) + 2\*\*2 \* RBF(length\_scale=100) \* ExpSineSquared(length\_scale=1, periodicity=1) + 0.5\*\*2 \* RationalQuadratic(alpha=1, length\_scale=1) + 0.1\*\*2 \* RBF(length\_scale=0.1) + WhiteKernel(noise\_level=0.01))

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GaussianProcessRegressor

[?Documentation for GaussianProcessRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [kernel kernel: kernel instance, default=None  <br>  <br>The kernel specifying the covariance function of the GP.  <br>If \`None\` is passed,  <br>the kernel \`ConstantKernel() \* RBF()\` is used as default.  <br>Note that  <br>the kernel hyperparameters are optimized during fitting  <br>unless the bounds are marked as \`"fixed"\`  <br>or the argument \`optimizer\` is set to \`None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=kernel,-kernel%20instance%2C%20default%3DNone) | 50\*\*2 \* RBF(l...se\_level=0.01) |
|     | kernel\_\_k1 | 50\*\*2 \* RBF(l...ength\_scale=1) |
|     | kernel\_\_k2 | 0.1\*\*2 \* RBF(...se\_level=0.01) |
|     | kernel\_\_k1\_\_k1 | 50\*\*2 \* RBF(l...periodicity=1) |
|     | kernel\_\_k1\_\_k2 | 0.5\*\*2 \* Rati...ength\_scale=1) |
|     | kernel\_\_k1\_\_k1\_\_k1 | 50\*\*2 \* RBF(length\_scale=50) |
|     | kernel\_\_k1\_\_k1\_\_k2 | 2\*\*2 \* RBF(le...periodicity=1) |
|     | kernel\_\_k1\_\_k1\_\_k1\_\_k1 | 50\*\*2 |
|     | kernel\_\_k1\_\_k1\_\_k1\_\_k2 | RBF(length\_scale=50) |
|     | kernel\_\_k1\_\_k1\_\_k1\_\_k1\_\_constant\_value | 2500.0 |
|     | kernel\_\_k1\_\_k1\_\_k1\_\_k1\_\_constant\_value\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k1\_\_k1\_\_k2\_\_length\_scale | 50.0 |
|     | kernel\_\_k1\_\_k1\_\_k1\_\_k2\_\_length\_scale\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1 | 2\*\*2 \* RBF(length\_scale=100) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k2 | ExpSineSquare...periodicity=1) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1\_\_k1 | 2\*\*2 |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1\_\_k2 | RBF(length\_scale=100) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1\_\_k1\_\_constant\_value | 4.0 |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1\_\_k1\_\_constant\_value\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1\_\_k2\_\_length\_scale | 100.0 |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k1\_\_k2\_\_length\_scale\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k2\_\_length\_scale | 1.0 |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k2\_\_periodicity | 1.0 |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k2\_\_length\_scale\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k1\_\_k2\_\_k2\_\_periodicity\_bounds | 'fixed' |
|     | kernel\_\_k1\_\_k2\_\_k1 | 0.5\*\*2 |
|     | kernel\_\_k1\_\_k2\_\_k2 | RationalQuadr...ength\_scale=1) |
|     | kernel\_\_k1\_\_k2\_\_k1\_\_constant\_value | 0.25 |
|     | kernel\_\_k1\_\_k2\_\_k1\_\_constant\_value\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k2\_\_k2\_\_length\_scale | 1.0 |
|     | kernel\_\_k1\_\_k2\_\_k2\_\_alpha | 1.0 |
|     | kernel\_\_k1\_\_k2\_\_k2\_\_length\_scale\_bounds | (1e-05, ...) |
|     | kernel\_\_k1\_\_k2\_\_k2\_\_alpha\_bounds | (1e-05, ...) |
|     | kernel\_\_k2\_\_k1 | 0.1\*\*2 \* RBF(length\_scale=0.1) |
|     | kernel\_\_k2\_\_k2 | WhiteKernel(noise\_level=0.01) |
|     | kernel\_\_k2\_\_k1\_\_k1 | 0.1\*\*2 |
|     | kernel\_\_k2\_\_k1\_\_k2 | RBF(length\_scale=0.1) |
|     | kernel\_\_k2\_\_k1\_\_k1\_\_constant\_value | 0.010000000000000002 |
|     | kernel\_\_k2\_\_k1\_\_k1\_\_constant\_value\_bounds | (1e-05, ...) |
|     | kernel\_\_k2\_\_k1\_\_k2\_\_length\_scale | 0.1 |
|     | kernel\_\_k2\_\_k1\_\_k2\_\_length\_scale\_bounds | (1e-05, ...) |
|     | kernel\_\_k2\_\_k2\_\_noise\_level | 0.010000000000000002 |
|     | kernel\_\_k2\_\_k2\_\_noise\_level\_bounds | (1e-05, ...) |
|     | [alpha alpha: float or ndarray of shape (n\_samples,), default=1e-10  <br>  <br>Value added to the diagonal of the kernel matrix during fitting.  <br>This can prevent a potential numerical issue during fitting, by  <br>ensuring that the calculated values form a positive definite matrix.  <br>It can also be interpreted as the variance of additional Gaussian  <br>measurement noise on the training observations. Note that this is  <br>different from using a \`WhiteKernel\`. If an array is passed, it must  <br>have the same number of entries as the data used for fitting and is  <br>used as datapoint-dependent noise level. Allowing to specify the  <br>noise level directly as a parameter is mainly for convenience and  <br>for consistency with :class:\`~sklearn.linear\_model.Ridge\`.  <br>For an example illustrating how the alpha parameter controls  <br>the noise variance in Gaussian Process Regression, see  <br>:ref:\`sphx\_glr\_auto\_examples\_gaussian\_process\_plot\_gpr\_noisy\_targets.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=alpha,-float%20or%20ndarray%20of%20shape%20%28n_samples%2C%29%2C%20default%3D1e-10) | 1e-10 |
|     | [optimizer optimizer: "fmin\_l\_bfgs\_b", callable or None, default="fmin\_l\_bfgs\_b"  <br>  <br>Can either be one of the internally supported optimizers for optimizing  <br>the kernel's parameters, specified by a string, or an externally  <br>defined optimizer passed as a callable. If a callable is passed, it  <br>must have the signature::  <br>  <br>def optimizer(obj\_func, initial\_theta, bounds):  <br>\# \* 'obj\_func': the objective function to be minimized, which  <br>\# takes the hyperparameters theta as a parameter and an  <br>\# optional flag eval\_gradient, which determines if the  <br>\# gradient is returned additionally to the function value  <br>\# \* 'initial\_theta': the initial value for theta, which can be  <br>\# used by local optimizers  <br>\# \* 'bounds': the bounds on the values of theta  <br>....  <br>\# Returned are the best found hyperparameters theta and  <br>\# the corresponding value of the target function.  <br>return theta\_opt, func\_min  <br>  <br>Per default, the L-BFGS-B algorithm from \`scipy.optimize.minimize\`  <br>is used. If None is passed, the kernel's parameters are kept fixed.  <br>Available internal optimizers are: \`{'fmin\_l\_bfgs\_b'}\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=optimizer,-%22fmin_l_bfgs_b%22%2C%20callable%20or%20None%2C%20default%3D%22fmin_l_bfgs_b%22) | 'fmin\_l\_bfgs\_b' |
|     | [n\_restarts\_optimizer n\_restarts\_optimizer: int, default=0  <br>  <br>The number of restarts of the optimizer for finding the kernel's  <br>parameters which maximize the log-marginal likelihood. The first run  <br>of the optimizer is performed from the kernel's initial parameters,  <br>the remaining ones (if any) from thetas sampled log-uniform randomly  <br>from the space of allowed theta-values. If greater than 0, all bounds  <br>must be finite. Note that \`n\_restarts\_optimizer == 0\` implies that one  <br>run is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=n_restarts_optimizer,-int%2C%20default%3D0) | 0   |
|     | [normalize\_y normalize\_y: bool, default=False  <br>  <br>Whether or not to normalize the target values \`y\` by removing the mean  <br>and scaling to unit-variance. This is recommended for cases where  <br>zero-mean, unit-variance priors are used. Note that, in this  <br>implementation, the normalisation is reversed before the GP predictions  <br>are reported.  <br>  <br>.. versionchanged:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=normalize_y,-bool%2C%20default%3DFalse) | False |
|     | [copy\_X\_train copy\_X\_train: bool, default=True  <br>  <br>If True, a persistent copy of the training data is stored in the  <br>object. Otherwise, just a reference to the training data is stored,  <br>which might cause predictions to change if the data is modified  <br>externally.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=copy_X_train,-bool%2C%20default%3DTrue) | True |
|     | [n\_targets n\_targets: int, default=None  <br>  <br>The number of dimensions of the target values. Used to decide the number  <br>of outputs when sampling from the prior distributions (i.e. calling  <br>:meth:\`sample\_y\` before :meth:\`fit\`). This parameter is ignored once  <br>:meth:\`fit\` has been called.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=n_targets,-int%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Determines random number generation used to initialize the centers.  <br>Pass an int for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [L\_ L\_: array-like of shape (n\_samples, n\_samples)  <br>  <br>Lower-triangular Cholesky decomposition of the kernel in \`\`X\_train\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=L_,-array-like%20of%20shape%20%28n_samples%2C%20n_samples%29) | ndarray\[float64\](521, 521) | \[\[44.86, 0. , 0. ,..., 0. , 0. , 0. \], \[44.85, 0.96, 0. ,..., 0. , 0. , 0. \], \[44.83, 1.55, 0.75,..., 0. , 0. , 0. \], ..., \[31.35, 2.17, 2. ,..., 0.29, 0. , 0. \], \[31.31, 1.83, 1.85,..., 0.19, 0.29, 0. \], \[31.29, 1.5 , 1.68,..., 0.16, 0.19, 0.29\]\] |
| [X\_train\_ X\_train\_: array-like of shape (n\_samples, n\_features) or list of object  <br>  <br>Feature vectors or other representations of training data (also  <br>required for prediction).](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=X_train_,-array-like%20of%20shape%20%28n_samples%2C%20n_features%29%20or%20list%20of%20object) | ndarray\[float64\](521, 1) | \[\[1958.25\], \[1958.33\], \[1958.42\], ..., \[2001.83\], \[2001.92\], \[2002. \]\] |
| [alpha\_ alpha\_: array-like of shape (n\_samples,)  <br>  <br>Dual coefficients of training data points in kernel space.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=alpha_,-array-like%20of%20shape%20%28n_samples%2C%29) | ndarray\[float64\](521,) | \[-0.86, 2.37,-3.4 ,..., 1.17,-2.45, 2.96\] |
| [kernel\_ kernel\_: kernel instance  <br>  <br>The kernel used for prediction. The structure of the kernel is the  <br>same as the one passed as parameter but with optimized hyperparameters.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=kernel_,-kernel%20instance) | Sum | 44.8\*\*2 \* RBF...\_level=0.0367) |
| [log\_marginal\_likelihood\_value\_ log\_marginal\_likelihood\_value\_: float  <br>  <br>The log-marginal-likelihood of \`\`self.kernel\_.theta\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=log_marginal_likelihood_value_,-float) | float64 | \-115.1 |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=n_features_in_,-int) | int | 1   |
| [y\_train\_ y\_train\_: array-like of shape (n\_samples,) or (n\_samples, n\_targets)  <br>  <br>Target values in training data (also required for prediction).](https://scikit-learn.org/1.9/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#:~:text=y_train_,-array-like%20of%20shape%20%28n_samples%2C%29%20or%20%28n_samples%2C%20n_targets%29) | ndarray\[float64\](521,) | \[-23.72,-22.62,-22.39,..., 28.23, 29.55, 31.2 \] |

  
  

Now, we will use the Gaussian process to predict on:

*   training data to inspect the goodness of fit;
    
*   future data to see the extrapolation done by the model.
    

Thus, we create synthetic data from 1958 to the current month. In addition, we need to add the subtracted mean computed during training.

import datetime

import numpy as np

today \= [datetime.datetime.now](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now")
()
current\_month \= today.year + today.month / 12
X\_test \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(start\=1958, stop\=current\_month, num\=1\_000).reshape(\-1, 1)
mean\_y\_pred, std\_y\_pred \= gaussian\_process.predict(X\_test, return\_std\=True)
mean\_y\_pred += y\_mean

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, color\="black", linestyle\="dashed", label\="Measurements")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, mean\_y\_pred, color\="tab:blue", alpha\=0.4, label\="Gaussian process")
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    X\_test.ravel(),
    mean\_y\_pred \- std\_y\_pred,
    mean\_y\_pred + std\_y\_pred,
    color\="tab:blue",
    alpha\=0.2,
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Year")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Monthly average of CO$\_2$ concentration (ppm)")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Monthly average of air samples measurements\\nfrom the Mauna Loa Observatory"
)

Copy to clipboard

![Monthly average of air samples measurements from the Mauna Loa Observatory](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_003.png)

Our fitted model is capable to fit previous data properly and extrapolate to future year with confidence.

Interpretation of kernel hyperparameters[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html#interpretation-of-kernel-hyperparameters "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we can have a look at the hyperparameters of the kernel.

gaussian\_process.kernel\_

Copy to clipboard

44.8\*\*2 \* RBF(length\_scale=51.6) + 2.64\*\*2 \* RBF(length\_scale=91.5) \* ExpSineSquared(length\_scale=1.48, periodicity=1) + 0.536\*\*2 \* RationalQuadratic(alpha=2.89, length\_scale=0.968) + 0.188\*\*2 \* RBF(length\_scale=0.122) + WhiteKernel(noise\_level=0.0367)

Copy to clipboard

Thus, most of the target signal, with the mean subtracted, is explained by a long-term rising trend for ~45 ppm and a length-scale of ~52 years. The periodic component has an amplitude of ~2.6ppm, a decay time of ~90 years and a length-scale of ~1.5. The long decay time indicates that we have a component very close to a seasonal periodicity. The correlated noise has an amplitude of ~0.2 ppm with a length scale of ~0.12 years and a white-noise contribution of ~0.04 ppm. Thus, the overall noise level is very small, indicating that the data can be very well explained by the model.

**Total running time of the script:** (0 minutes 4.079 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_co2.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_co2.ipynb)

[`Download Jupyter notebook: plot_gpr_co2.ipynb`](https://scikit-learn.org/stable/_downloads/91a0c94f9f7c19d59a0ad06e77512326/plot_gpr_co2.ipynb)

[`Download Python source code: plot_gpr_co2.py`](https://scikit-learn.org/stable/_downloads/1b8827af01c9a70017a4739bcf2e21a8/plot_gpr_co2.py)

[`Download zipped: plot_gpr_co2.zip`](https://scikit-learn.org/stable/_downloads/c2cfe11afa629e514b58e6b27dbf5ae7/plot_gpr_co2.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_thumb.png)

[Ability of Gaussian process regression (GPR) to estimate data noise-level](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)

Ability of Gaussian process regression (GPR) to estimate data noise-level

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_thumb.png)

[Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Comparison of kernel ridge and Gaussian process regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/1b8827af01c9a70017a4739bcf2e21a8/plot_gpr_co2.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/91a0c94f9f7c19d59a0ad06e77512326/plot_gpr_co2.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c2cfe11afa629e514b58e6b27dbf5ae7/plot_gpr_co2.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_co2.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_co2.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)