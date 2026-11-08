[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_lasso_model_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_lasso_model_selection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_lasso_model_selection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_lasso_model_selection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_lasso_model_selection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_lasso_model_selection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-download-auto-examples-linear-model-plot-lasso-model-selection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Lasso model selection: AIC-BIC / cross-validation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#lasso-model-selection-aic-bic-cross-validation "Link to this heading")

=======================================================================================================================================================================================================================

This example focuses on model selection for Lasso models that are linear models with an L1 penalty for regression problems.

Indeed, several strategies can be used to select the value of the regularization parameter: via cross-validation or using an information criterion, namely AIC or BIC.

In what follows, we will discuss in details the different strategies.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#dataset "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

In this example, we will use the diabetes dataset.

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")

X, y \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True, as\_frame\=True)
X.head()

Copy to clipboard

|     | age | sex | bmi | bp  | s1  | s2  | s3  | s4  | s5  | s6  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0.038076 | 0.050680 | 0.061696 | 0.021872 | \-0.044223 | \-0.034821 | \-0.043401 | \-0.002592 | 0.019907 | \-0.017646 |
| 1   | \-0.001882 | \-0.044642 | \-0.051474 | \-0.026328 | \-0.008449 | \-0.019163 | 0.074412 | \-0.039493 | \-0.068332 | \-0.092204 |
| 2   | 0.085299 | 0.050680 | 0.044451 | \-0.005670 | \-0.045599 | \-0.034194 | \-0.032356 | \-0.002592 | 0.002861 | \-0.025930 |
| 3   | \-0.089063 | \-0.044642 | \-0.011595 | \-0.036656 | 0.012191 | 0.024991 | \-0.036038 | 0.034309 | 0.022688 | \-0.009362 |
| 4   | 0.005383 | \-0.044642 | \-0.036385 | 0.021872 | 0.003935 | 0.015596 | 0.008142 | \-0.002592 | \-0.031988 | \-0.046641 |

  
  

In addition, we add some random features to the original data to better illustrate the feature selection performed by the Lasso model.

import numpy as np
import pandas as pd

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
n\_random\_features \= 14
X\_random \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    rng.randn(X.shape\[0\], n\_random\_features),
    columns\=\[f"random\_{i:02d}" for i in range(n\_random\_features)\],
)
X \= [pd.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
(\[X, X\_random\], axis\=1)
\# Show only a subset of the columns
X\[X.columns\[::3\]\].head()

Copy to clipboard

|     | age | bp  | s3  | s6  | random\_02 | random\_05 | random\_08 | random\_11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0.038076 | 0.021872 | \-0.043401 | \-0.017646 | 0.647689 | \-0.234137 | \-0.469474 | \-0.465730 |
| 1   | \-0.001882 | \-0.026328 | 0.074412 | \-0.092204 | \-1.012831 | \-1.412304 | 0.067528 | 0.110923 |
| 2   | 0.085299 | \-0.005670 | \-0.032356 | \-0.025930 | \-0.601707 | \-1.057711 | 0.208864 | 0.196861 |
| 3   | \-0.089063 | \-0.036656 | \-0.036038 | \-0.009362 | \-1.478522 | 1.057122 | 0.324084 | 0.611676 |
| 4   | 0.005383 | 0.021872 | 0.008142 | \-0.046641 | 0.331263 | \-0.185659 | 0.812526 | 1.003533 |

  
  

Selecting Lasso via an information criterion[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#selecting-lasso-via-an-information-criterion "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
 provides a Lasso estimator that uses the Akaike information criterion (AIC) or the Bayes information criterion (BIC) to select the optimal value of the regularization parameter alpha.

Before fitting the model, we will standardize the data with a [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
. In addition, we will measure the time to fit and tune the hyperparameter alpha in order to compare with the cross-validation strategy.

We will first fit a Lasso model with the AIC criterion.

import time

from sklearn.linear\_model import [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
lasso\_lars\_ic \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
(criterion\="aic")).fit(X, y)
fit\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time

Copy to clipboard

We store the AIC metric for each value of alpha used during `fit`.

results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "alphas": lasso\_lars\_ic\[\-1\].alphas\_,
        "AIC criterion": lasso\_lars\_ic\[\-1\].criterion\_,
    }
).set\_index("alphas")
alpha\_aic \= lasso\_lars\_ic\[\-1\].alpha\_

Copy to clipboard

Now, we perform the same analysis using the BIC criterion.

lasso\_lars\_ic.set\_params(lassolarsic\_\_criterion\="bic").fit(X, y)
results\["BIC criterion"\] \= lasso\_lars\_ic\[\-1\].criterion\_
alpha\_bic \= lasso\_lars\_ic\[\-1\].alpha\_

Copy to clipboard

We can check which value of `alpha` leads to the minimum AIC and BIC.

def highlight\_min(x):
    x\_min \= x.min()
    return \["font-weight: bold" if v \== x\_min else "" for v in x\]

results.style.apply(highlight\_min)

Copy to clipboard

|     | AIC criterion | BIC criterion |
| --- | --- | --- |
| alphas |     |     |
| --- | --- | --- |
| 45.160030 | 5244.764779 | 5244.764779 |
| 42.300343 | 5208.250639 | 5212.341949 |
| 21.542052 | 4928.018900 | 4936.201520 |
| 15.034077 | 4869.678359 | 4881.952289 |
| 6.189631 | 4815.437362 | 4831.802601 |
| 5.329616 | 4810.423641 | 4830.880191 |
| 4.306012 | 4803.573491 | 4828.121351 |
| 4.124225 | 4804.126502 | 4832.765671 |
| 3.820705 | 4803.621645 | 4836.352124 |
| 3.750389 | 4805.012521 | 4841.834310 |
| 3.570655 | 4805.290075 | 4846.203174 |
| 3.550213 | 4807.075887 | 4852.080295 |
| 3.358295 | 4806.878051 | 4855.973770 |
| 3.259297 | 4807.706026 | 4860.893055 |
| 3.237703 | 4809.440409 | 4866.718747 |
| 2.850031 | 4805.989341 | 4867.358990 |
| 2.384338 | 4801.702266 | 4867.163224 |
| 2.296575 | 4802.594754 | 4872.147022 |
| 2.031555 | 4801.236720 | 4874.880298 |
| 1.618263 | 4798.484109 | 4876.218997 |
| 1.526599 | 4799.543841 | 4881.370039 |
| 0.586798 | 4794.238744 | 4880.156252 |
| 0.445978 | 4795.589715 | 4885.598533 |
| 0.259031 | 4796.966981 | 4891.067109 |
| 0.032179 | 4794.662409 | 4888.762537 |
| 0.019069 | 4794.652739 | 4888.752867 |
| 0.000000 | 4796.626286 | 4894.817724 |

  
  

Finally, we can plot the AIC and BIC values for the different alpha values. The vertical lines in the plot correspond to the alpha chosen for each criterion. The selected alpha corresponds to the minimum of the AIC or BIC criterion.

ax \= results.plot()
ax.vlines(
    alpha\_aic,
    results\["AIC criterion"\].min(),
    results\["AIC criterion"\].max(),
    label\="alpha: AIC estimate",
    linestyles\="--",
    color\="tab:blue",
)
ax.vlines(
    alpha\_bic,
    results\["BIC criterion"\].min(),
    results\["BIC criterion"\].max(),
    label\="alpha: BIC estimate",
    linestyle\="--",
    color\="tab:orange",
)
ax.set\_xlabel(r"$\\alpha$")
ax.set\_ylabel("criterion")
ax.set\_xscale("log")
ax.legend()
\_ \= ax.set\_title(
    f"Information-criterion for model selection (training time {fit\_time:.2f}s)"
)

Copy to clipboard

![Information-criterion for model selection (training time 0.01s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_001.png)

Model selection with an information-criterion is very fast. It relies on computing the criterion on the in-sample set provided to `fit`. Both criteria estimate the model generalization error based on the training set error and penalize this overly optimistic error. However, this penalty relies on a proper estimation of the degrees of freedom and the noise variance. Both are derived for large samples (asymptotic results) and assume the model is correct, i.e. that the data are actually generated by this model.

These models also tend to break when the problem is badly conditioned (more features than samples). It is then required to provide an estimate of the noise variance.

Selecting Lasso via cross-validation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#selecting-lasso-via-cross-validation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Lasso estimator can be implemented with different solvers: coordinate descent and least angle regression. They differ with regards to their execution speed and sources of numerical errors.

In scikit-learn, two different estimators are available with integrated cross-validation: [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
 and [`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
 that respectively solve the problem with coordinate descent and least angle regression.

In the remainder of this section, we will present both approaches. For both algorithms, we will use a 20-fold cross-validation strategy.

### Lasso via coordinate descent[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#lasso-via-coordinate-descent "Link to this heading")

Let’s start by making the hyperparameter tuning using [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
.

from sklearn.linear\_model import [LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
(cv\=20)).fit(X, y)
fit\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time

Copy to clipboard

import matplotlib.pyplot as plt

ymin, ymax \= 2300, 3800
lasso \= model\[\-1\]
[plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(lasso.alphas\_, lasso.mse\_path\_, linestyle\=":")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    lasso.alphas\_,
    lasso.mse\_path\_.mean(axis\=-1),
    color\="black",
    label\="Average across the folds",
    linewidth\=2,
)
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(lasso.alpha\_, linestyle\="--", color\="black", label\="alpha: CV estimate")

[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(ymin, ymax)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(r"$\\alpha$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Mean square error")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    f"Mean square error on each fold: coordinate descent (train time: {fit\_time:.2f}s)"
)

Copy to clipboard

![Mean square error on each fold: coordinate descent (train time: 0.34s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_002.png)

### Lasso via least angle regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#lasso-via-least-angle-regression "Link to this heading")

Let’s start by making the hyperparameter tuning using [`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
.

from sklearn.linear\_model import [LassoLarsCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")

start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LassoLarsCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
(cv\=20)).fit(X, y)
fit\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time

Copy to clipboard

lasso \= model\[\-1\]
[plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(lasso.cv\_alphas\_, lasso.mse\_path\_, ":")
[plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(
    lasso.cv\_alphas\_,
    lasso.mse\_path\_.mean(axis\=-1),
    color\="black",
    label\="Average across the folds",
    linewidth\=2,
)
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(lasso.alpha\_, linestyle\="--", color\="black", label\="alpha CV")

[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(ymin, ymax)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(r"$\\alpha$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Mean square error")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(f"Mean square error on each fold: Lars (train time: {fit\_time:.2f}s)")

Copy to clipboard

![Mean square error on each fold: Lars (train time: 0.09s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_003.png)

### Summary of cross-validation approach[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#summary-of-cross-validation-approach "Link to this heading")

Both algorithms give roughly the same results.

Lars computes a solution path only for each kink in the path. As a result, it is very efficient when there are only of few kinks, which is the case if there are few features or samples. Also, it is able to compute the full path without setting any hyperparameter. On the opposite, coordinate descent computes the path points on a pre-specified grid (here we use the default). Thus it is more efficient if the number of grid points is smaller than the number of kinks in the path. Such a strategy can be interesting if the number of features is really large and there are enough samples to be selected in each of the cross-validation fold. In terms of numerical errors, for heavily correlated variables, Lars will accumulate more errors, while the coordinate descent algorithm will only sample the path on a grid.

Note how the optimal value of alpha varies for each fold. This illustrates why nested-cross validation is a good strategy when trying to evaluate the performance of a method for which a parameter is chosen by cross-validation: this choice of parameter may not be optimal for a final evaluation on unseen test set only.

Conclusion[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#conclusion "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

In this tutorial, we presented two approaches for selecting the best hyperparameter `alpha`: one strategy finds the optimal value of `alpha` by only using the training set and some information criterion, and another strategy is based on cross-validation.

In this example, both approaches are working similarly. The in-sample hyperparameter selection even shows its efficacy in terms of computational performance. However, it can only be used when the number of samples is large enough compared to the number of features.

That’s why hyperparameter optimization via cross-validation is a safe strategy: it works in different settings.

**Total running time of the script:** (0 minutes 0.984 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_model_selection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_model_selection.ipynb)

[`Download Jupyter notebook: plot_lasso_model_selection.ipynb`](https://scikit-learn.org/stable/_downloads/901ad159d788e1122a5616f537985e74/plot_lasso_model_selection.ipynb)

[`Download Python source code: plot_lasso_model_selection.py`](https://scikit-learn.org/stable/_downloads/58580795dd881384f33e7e6492e154e2/plot_lasso_model_selection.py)

[`Download zipped: plot_lasso_model_selection.zip`](https://scikit-learn.org/stable/_downloads/f2f93218efc289130afe6ccd4aae9a02/plot_lasso_model_selection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lars_ic_thumb.png)

[Lasso model selection via information criteria](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html)

Lasso model selection via information criteria

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/58580795dd881384f33e7e6492e154e2/plot_lasso_model_selection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/901ad159d788e1122a5616f537985e74/plot_lasso_model_selection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f2f93218efc289130afe6ccd4aae9a02/plot_lasso_model_selection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_model_selection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_model_selection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)