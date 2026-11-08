[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_lasso_and_elasticnet.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#sphx-glr-download-auto-examples-linear-model-plot-lasso-and-elasticnet-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

L1-based models for Sparse Signals[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#l1-based-models-for-sparse-signals "Link to this heading")

===========================================================================================================================================================================================

The present example compares three l1-based regression models on a synthetic signal obtained from sparse and correlated features that are further corrupted with additive Gaussian noise:

*   a [Lasso](https://scikit-learn.org/stable/modules/linear_model.html#lasso)
    ;
    
*   an [Automatic Relevance Determination - ARD](https://scikit-learn.org/stable/modules/linear_model.html#automatic-relevance-determination)
    ;
    
*   an [Elastic-Net](https://scikit-learn.org/stable/modules/linear_model.html#elastic-net)
    .
    

It is known that the Lasso estimates turn to be close to the model selection estimates when the data dimensions grow, given that the irrelevant variables are not too correlated with the relevant ones. In the presence of correlated features, Lasso itself cannot select the correct sparsity pattern [\[1\]](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#id2)
.

Here we compare the performance of the three models in terms of the R2 score, the fitting time and the sparsity of the estimated coefficients when compared with the ground-truth.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate synthetic dataset[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#generate-synthetic-dataset "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We generate a dataset where the number of samples is lower than the total number of features. This leads to an underdetermined system, i.e. the solution is not unique, and thus we cannot apply an [Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)
 by itself. Regularization introduces a penalty term to the objective function, which modifies the optimization problem and can help alleviate the underdetermined nature of the system.

The target `y` is a linear combination with alternating signs of sinusoidal signals. Only the 10 lowest out of the 100 frequencies in `X` are used to generate `y`, while the rest of the features are not informative. This results in a high dimensional sparse feature space, where some degree of l1-penalization is necessary.

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
n\_samples, n\_features, n\_informative \= 50, 100, 10
time\_step \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-2, 2, n\_samples)
freqs \= 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(rng.rand(n\_features)) / 0.01
X \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_samples, n\_features))

for i in range(n\_features):
    X\[:, i\] \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(freqs\[i\] \* time\_step)

idx \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_features)
true\_coef \= (\-1) \*\* idx \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-idx / 10)
true\_coef\[n\_informative:\] \= 0  \# sparsify coef
y \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, true\_coef)

Copy to clipboard

Some of the informative features have close frequencies to induce (anti-)correlations.

freqs\[:n\_informative\]

Copy to clipboard

array(\[ 2.9502547 , 11.8059798 , 12.63394388, 12.70359377, 24.62241605,\
       37.84077985, 40.30506066, 44.63327171, 54.74495357, 59.02456369\])

Copy to clipboard

A random phase is introduced using [`numpy.random.random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "(in NumPy v2.5)")
 and some Gaussian noise (implemented by [`numpy.random.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "(in NumPy v2.5)")
) is added to both the features and the target.

for i in range(n\_features):
    X\[:, i\] \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(freqs\[i\] \* time\_step + 2 \* (rng.random\_sample() \- 0.5))
    X\[:, i\] += 0.2 \* rng.normal(0, 1, n\_samples)

y += 0.2 \* rng.normal(0, 1, n\_samples)

Copy to clipboard

Such sparse, noisy and correlated features can be obtained, for instance, from sensor nodes monitoring some environmental variables, as they typically register similar values depending on their positions (spatial correlations). We can visualize the target.

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(time\_step, y)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target signal")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("time")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Superposition of sinusoidal signals")

Copy to clipboard

![Superposition of sinusoidal signals](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_001.png)

We split the data into train and test sets for simplicity. In practice one should use a [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
 cross-validation to estimate the variance of the test score. Here we set `shuffle="False"` as we must not use training data that succeed the testing data when dealing with data that have a temporal relationship.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.5, shuffle\=False)

Copy to clipboard

In the following, we compute the performance of three l1-based models in terms of the goodness of fit R2 score and the fitting time. Then we make a plot to compare the sparsity of the estimated coefficients with respect to the ground-truth coefficients and finally we analyze the previous results.

Lasso[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#lasso "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

In this example, we demo a [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 with a fixed value of the regularization parameter `alpha`. In practice, the optimal parameter `alpha` should be selected by passing a [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
 cross-validation strategy to a [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
. To keep the example simple and fast to execute, we directly set the optimal value for alpha here.

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn.linear\_model import [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
from sklearn.metrics import [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
lasso \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
(alpha\=0.14).fit(X\_train, y\_train)
print(f"Lasso fit done in {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

y\_pred\_lasso \= lasso.predict(X\_test)
r2\_score\_lasso \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_lasso)
print(f"Lasso r^2 on test data : {r2\_score\_lasso:.3f}")

Copy to clipboard

Lasso fit done in 0.001s
Lasso r^2 on test data : 0.480

Copy to clipboard

Automatic Relevance Determination (ARD)[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#automatic-relevance-determination-ard "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An ARD regression is the Bayesian version of the Lasso. It can produce interval estimates for all of the parameters, including the error variance, if required. It is a suitable option when the signals have Gaussian noise. See the example [Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#sphx-glr-auto-examples-linear-model-plot-ard-py)
 for a comparison of [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
 and [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
 regressors.

from sklearn.linear\_model import [ARDRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
ard \= [ARDRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
().fit(X\_train, y\_train)
print(f"ARD fit done in {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

y\_pred\_ard \= ard.predict(X\_test)
r2\_score\_ard \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_ard)
print(f"ARD r^2 on test data : {r2\_score\_ard:.3f}")

Copy to clipboard

ARD fit done in 0.039s
ARD r^2 on test data : 0.543

Copy to clipboard

ElasticNet[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#elasticnet "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

[`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
 is a middle ground between [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 and [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
, as it combines an L1 and an L2-penalty. The amount of regularization is controlled by the two hyperparameters `l1_ratio` and `alpha`. For `l1_ratio = 0` the penalty is pure L2 and the model is equivalent to a [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
. Similarly, `l1_ratio = 1` is a pure L1 penalty and the model is equivalent to a [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
. For `0 < l1_ratio < 1`, the penalty is a combination of L1 and L2.

As done before, we train the model with fix values for `alpha` and `l1_ratio`. To select their optimal value we used an [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
, not shown here to keep the example simple.

from sklearn.linear\_model import [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
enet \= [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
(alpha\=0.08, l1\_ratio\=0.5).fit(X\_train, y\_train)
print(f"ElasticNet fit done in {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

y\_pred\_enet \= enet.predict(X\_test)
r2\_score\_enet \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_enet)
print(f"ElasticNet r^2 on test data : {r2\_score\_enet:.3f}")

Copy to clipboard

ElasticNet fit done in 0.001s
ElasticNet r^2 on test data : 0.636

Copy to clipboard

Plot and analysis of the results[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#plot-and-analysis-of-the-results "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we use a heatmap to visualize the sparsity of the true and estimated coefficients of the respective linear models.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import [SymLogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")

df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "True coefficients": true\_coef,
        "Lasso": lasso.coef\_,
        "ARDRegression": ard.coef\_,
        "ElasticNet": enet.coef\_,
    }
)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 6))
ax \= [sns.heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")
(
    df.T,
    norm\=[SymLogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
(linthresh\=10e-4, vmin\=-1, vmax\=1),
    cbar\_kws\={"label": "coefficients' values"},
    cmap\="seismic\_r",
)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("linear model")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    f"Models' coefficients\\nLasso $R^2$: {r2\_score\_lasso:.3f}, "
    f"ARD $R^2$: {r2\_score\_ard:.3f}, "
    f"ElasticNet $R^2$: {r2\_score\_enet:.3f}"
)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Models' coefficients Lasso $R^2$: 0.480, ARD $R^2$: 0.543, ElasticNet $R^2$: 0.636](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_002.png)

In the present example [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
 yields the best score and captures the most of the predictive features, yet still fails at finding all the true components. Notice that both [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
 and [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
 result in a less sparse model than a [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
.

Conclusions[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#conclusions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 is known to recover sparse data effectively but does not perform well with highly correlated features. Indeed, if several correlated features contribute to the target, [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 would end up selecting a single one of them. In the case of sparse yet non-correlated features, a [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 model would be more suitable.

[`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
 introduces some sparsity on the coefficients and shrinks their values to zero. Thus, in the presence of correlated features that contribute to the target, the model is still able to reduce their weights without setting them exactly to zero. This results in a less sparse model than a pure [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
 and may capture non-predictive features as well.

[`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
 is better when handling Gaussian noise, but is still unable to handle correlated features and requires a larger amount of time due to fitting a prior.

References[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#references "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

**Total running time of the script:** (0 minutes 0.558 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_and_elasticnet.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_and_elasticnet.ipynb)

[`Download Jupyter notebook: plot_lasso_and_elasticnet.ipynb`](https://scikit-learn.org/stable/_downloads/6cd2f23417e24a8a2a445c34f1b57930/plot_lasso_and_elasticnet.ipynb)

[`Download Python source code: plot_lasso_and_elasticnet.py`](https://scikit-learn.org/stable/_downloads/3d58721191491072eecc520f0a45cdb3/plot_lasso_and_elasticnet.py)

[`Download zipped: plot_lasso_and_elasticnet.zip`](https://scikit-learn.org/stable/_downloads/90cf257940769245392cef28e5ab05b4/plot_lasso_and_elasticnet.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_dense_vs_sparse_data_thumb.png)

[Lasso on dense and sparse data](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)

Lasso on dense and sparse data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/3d58721191491072eecc520f0a45cdb3/plot_lasso_and_elasticnet.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6cd2f23417e24a8a2a445c34f1b57930/plot_lasso_and_elasticnet.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/90cf257940769245392cef28e5ab05b4/plot_lasso_and_elasticnet.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_and_elasticnet.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_and_elasticnet.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)