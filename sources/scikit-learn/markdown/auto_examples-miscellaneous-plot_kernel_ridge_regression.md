[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#sphx-glr-download-auto-examples-miscellaneous-plot-kernel-ridge-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of kernel ridge regression and SVR[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#comparison-of-kernel-ridge-regression-and-svr "Link to this heading")

=====================================================================================================================================================================================================================

Both kernel ridge regression (KRR) and SVR learn a non-linear function by employing the kernel trick, i.e., they learn a linear function in the space induced by the respective kernel which corresponds to a non-linear function in the original space. They differ in the loss functions (ridge versus epsilon-insensitive loss). In contrast to SVR, fitting a KRR can be done in closed-form and is typically faster for medium-sized datasets. On the other hand, the learned model is non-sparse and thus slower than SVR at prediction-time.

This example illustrates both methods on an artificial dataset, which consists of a sinusoidal target function and strong noise added to every fifth datapoint.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#generate-sample-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)

X \= 5 \* rng.rand(10000, 1)
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X).ravel()

\# Add noise to targets
y\[::5\] += 3 \* (0.5 \- rng.rand(X.shape\[0\] // 5))

X\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, 100000)\[:, None\]

Copy to clipboard

Construct the kernel-based regression models[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#construct-the-kernel-based-regression-models "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.kernel\_ridge import [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.svm import [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")

train\_size \= 100

svr \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
(kernel\="rbf", gamma\=0.1),
    param\_grid\={"C": \[1e0, 1e1, 1e2, 1e3\], "gamma": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 2, 5)},
)

kr \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
(kernel\="rbf", gamma\=0.1),
    param\_grid\={"alpha": \[1e0, 0.1, 1e-2, 1e-3\], "gamma": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 2, 5)},
)

Copy to clipboard

Compare times of SVR and Kernel Ridge Regression[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#compare-times-of-svr-and-kernel-ridge-regression "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time

t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
svr.fit(X\[:train\_size\], y\[:train\_size\])
svr\_fit \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print(f"Best SVR with params: {svr.best\_params\_} and R2 score: {svr.best\_score\_:.3f}")
print("SVR complexity and bandwidth selected and model fitted in %.3f s" % svr\_fit)

t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
kr.fit(X\[:train\_size\], y\[:train\_size\])
kr\_fit \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print(f"Best KRR with params: {kr.best\_params\_} and R2 score: {kr.best\_score\_:.3f}")
print("KRR complexity and bandwidth selected and model fitted in %.3f s" % kr\_fit)

sv\_ratio \= svr.best\_estimator\_.support\_.shape\[0\] / train\_size
print("Support vector ratio: %.3f" % sv\_ratio)

t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
y\_svr \= svr.predict(X\_plot)
svr\_predict \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print("SVR prediction for %d inputs in %.3f s" % (X\_plot.shape\[0\], svr\_predict))

t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
y\_kr \= kr.predict(X\_plot)
kr\_predict \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print("KRR prediction for %d inputs in %.3f s" % (X\_plot.shape\[0\], kr\_predict))

Copy to clipboard

Best SVR with params: {'C': 1.0, 'gamma': np.float64(0.1)} and R2 score: 0.737
SVR complexity and bandwidth selected and model fitted in 0.589 s
Best KRR with params: {'alpha': 0.1, 'gamma': np.float64(0.1)} and R2 score: 0.723
KRR complexity and bandwidth selected and model fitted in 0.246 s
Support vector ratio: 0.340
SVR prediction for 100000 inputs in 0.151 s
KRR prediction for 100000 inputs in 0.095 s

Copy to clipboard

Look at the results[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#look-at-the-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

sv\_ind \= svr.best\_estimator\_.support\_
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[sv\_ind\],
    y\[sv\_ind\],
    c\="r",
    s\=50,
    label\="SVR support vectors",
    zorder\=2,
    edgecolors\=(0, 0, 0),
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:100\], y\[:100\], c\="k", label\="data", zorder\=1, edgecolors\=(0, 0, 0))
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    X\_plot,
    y\_svr,
    c\="r",
    label\="SVR (fit: %.3fs, predict: %.3fs)" % (svr\_fit, svr\_predict),
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    X\_plot, y\_kr, c\="g", label\="KRR (fit: %.3fs, predict: %.3fs)" % (kr\_fit, kr\_predict)
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("SVR versus Kernel Ridge")
\_ \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()

Copy to clipboard

![SVR versus Kernel Ridge](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_001.png)

The previous figure compares the learned model of KRR and SVR when both complexity/regularization and bandwidth of the RBF kernel are optimized using grid-search. The learned functions are very similar; however, fitting KRR is approximately 3-4 times faster than fitting SVR (both with grid-search).

Prediction of 100000 target values could be in theory approximately three times faster with SVR since it has learned a sparse model using only approximately 1/3 of the training datapoints as support vectors. However, in practice, this is not necessarily the case because of implementation details in the way the kernel function is computed for each model that can make the KRR model as fast or even faster despite computing more arithmetic operations.

Visualize training and prediction times[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#visualize-training-and-prediction-times "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

sizes \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(1, 3.8, 7).astype(int)
for name, estimator in {
    "KRR": [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
(kernel\="rbf", alpha\=0.01, gamma\=10),
    "SVR": [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
(kernel\="rbf", C\=1e2, gamma\=10),
}.items():
    train\_time \= \[\]
    test\_time \= \[\]
    for train\_test\_size in sizes:
        t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        estimator.fit(X\[:train\_test\_size\], y\[:train\_test\_size\])
        train\_time.append([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0)

        t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        estimator.predict(X\_plot\[:1000\])
        test\_time.append([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0)

    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        sizes,
        train\_time,
        "o-",
        color\="r" if name \== "SVR" else "g",
        label\="%s (train)" % name,
    )
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        sizes,
        test\_time,
        "o--",
        color\="r" if name \== "SVR" else "g",
        label\="%s (test)" % name,
    )

[plt.xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html#matplotlib.pyplot.xscale "matplotlib.pyplot.xscale")
("log")
[plt.yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")
("log")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Train size")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Time (seconds)")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Execution Time")
\_ \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")

Copy to clipboard

![Execution Time](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_002.png)

This figure compares the time for fitting and prediction of KRR and SVR for different sizes of the training set. Fitting KRR is faster than SVR for medium-sized training sets (less than a few thousand samples); however, for larger training sets SVR scales better. With regard to prediction time, SVR should be faster than KRR for all sizes of the training set because of the learned sparse solution, however this is not necessarily the case in practice because of implementation details. Note that the degree of sparsity and thus the prediction time depends on the parameters epsilon and C of the SVR.

Visualize the learning curves[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#visualize-the-learning-curves "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.model\_selection import LearningCurveDisplay

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

svr \= [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
(kernel\="rbf", C\=1e1, gamma\=0.1)
kr \= [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
(kernel\="rbf", alpha\=0.1, gamma\=0.1)

common\_params \= {
    "X": X\[:100\],
    "y": y\[:100\],
    "train\_sizes": [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.1, 1, 10),
    "scoring": "neg\_mean\_squared\_error",
    "negate\_score": True,
    "score\_name": "Mean Squared Error",
    "score\_type": "test",
    "std\_display\_style": None,
    "ax": ax,
}

[LearningCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "sklearn.model_selection.LearningCurveDisplay.from_estimator")
(svr, \*\*common\_params)
[LearningCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "sklearn.model_selection.LearningCurveDisplay.from_estimator")
(kr, \*\*common\_params)
ax.set\_title("Learning curves")
ax.legend(handles\=ax.get\_legend\_handles\_labels()\[0\], labels\=\["SVR", "KRR"\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Learning curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_003.png)

**Total running time of the script:** (0 minutes 8.864 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_kernel_ridge_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_kernel_ridge_regression.ipynb)

[`Download Jupyter notebook: plot_kernel_ridge_regression.ipynb`](https://scikit-learn.org/stable/_downloads/9d2f119ab4a1b6f1454c43b796f2c6a6/plot_kernel_ridge_regression.ipynb)

[`Download Python source code: plot_kernel_ridge_regression.py`](https://scikit-learn.org/stable/_downloads/1dcd684ce26b8c407ec2c2d2101c5c73/plot_kernel_ridge_regression.py)

[`Download zipped: plot_kernel_ridge_regression.zip`](https://scikit-learn.org/stable/_downloads/aff4193b21ef6ea0af509058be609d18/plot_kernel_ridge_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_regression_thumb.png)

[Support Vector Regression (SVR) using linear and non-linear kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html)

Support Vector Regression (SVR) using linear and non-linear kernels

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_thumb.png)

[Probabilistic predictions with Gaussian process classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html)

Probabilistic predictions with Gaussian process classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/1dcd684ce26b8c407ec2c2d2101c5c73/plot_kernel_ridge_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/9d2f119ab4a1b6f1454c43b796f2c6a6/plot_kernel_ridge_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/aff4193b21ef6ea0af509058be609d18/plot_kernel_ridge_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_kernel_ridge_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_kernel_ridge_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)