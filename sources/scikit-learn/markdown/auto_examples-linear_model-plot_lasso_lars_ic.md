[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_lasso_lars_ic.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_lasso_lars_ic.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_lasso_lars_ic.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_lasso_lars_ic.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_lasso_lars_ic.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_lasso_lars_ic.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#sphx-glr-download-auto-examples-linear-model-plot-lasso-lars-ic-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Lasso model selection via information criteria[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#lasso-model-selection-via-information-criteria "Link to this heading")

============================================================================================================================================================================================================

This example reproduces the example of Fig. 2 of [\[ZHT2007\]](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#zht2007)
. A [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
 estimator is fit on a diabetes dataset and the AIC and the BIC criteria are used to select the best model.

Note

It is important to note that the optimization to find `alpha` with [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
 relies on the AIC or BIC criteria that are computed in-sample, thus on the training set directly. This approach differs from the cross-validation procedure. For a comparison of the two approaches, you can refer to the following example: [Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-auto-examples-linear-model-plot-lasso-model-selection-py)
.

References

\[ZHT2007\] ([1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#id1)
,[2](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#id2)
)

[Zou, Hui, Trevor Hastie, and Robert Tibshirani. “On the degrees of freedom of the lasso.” The Annals of Statistics 35.5 (2007): 2173-2192.](https://arxiv.org/abs/0712.0881)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

We will use the diabetes dataset.

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")

X, y \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True, as\_frame\=True)
n\_samples \= X.shape\[0\]
X.head()

Copy to clipboard

|     | age | sex | bmi | bp  | s1  | s2  | s3  | s4  | s5  | s6  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0.038076 | 0.050680 | 0.061696 | 0.021872 | \-0.044223 | \-0.034821 | \-0.043401 | \-0.002592 | 0.019907 | \-0.017646 |
| 1   | \-0.001882 | \-0.044642 | \-0.051474 | \-0.026328 | \-0.008449 | \-0.019163 | 0.074412 | \-0.039493 | \-0.068332 | \-0.092204 |
| 2   | 0.085299 | 0.050680 | 0.044451 | \-0.005670 | \-0.045599 | \-0.034194 | \-0.032356 | \-0.002592 | 0.002861 | \-0.025930 |
| 3   | \-0.089063 | \-0.044642 | \-0.011595 | \-0.036656 | 0.012191 | 0.024991 | \-0.036038 | 0.034309 | 0.022688 | \-0.009362 |
| 4   | 0.005383 | \-0.044642 | \-0.036385 | 0.021872 | 0.003935 | 0.015596 | 0.008142 | \-0.002592 | \-0.031988 | \-0.046641 |

  
  

Scikit-learn provides an estimator called [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
 that uses either Akaike’s information criterion (AIC) or the Bayesian information criterion (BIC) to select the best model. Before fitting this model, we will scale the dataset.

In the following, we are going to fit two models to compare the values reported by AIC and BIC.

from sklearn.linear\_model import [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

lasso\_lars\_ic \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LassoLarsIC](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
(criterion\="aic")).fit(X, y)

Copy to clipboard

To be in line with the definition in [\[ZHT2007\]](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html#zht2007)
, we need to rescale the AIC and the BIC. Indeed, Zou et al. are ignoring some constant terms compared to the original definition of AIC derived from the maximum log-likelihood of a linear model. You can refer to [mathematical detail section for the User Guide](https://scikit-learn.org/stable/modules/linear_model.html#lasso-lars-ic)
.

def zou\_et\_al\_criterion\_rescaling(criterion, n\_samples, noise\_variance):
    """Rescale the information criterion to follow the definition of Zou et al."""
    return criterion \- n\_samples \* [np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* noise\_variance) \- n\_samples

Copy to clipboard

import numpy as np

aic\_criterion \= zou\_et\_al\_criterion\_rescaling(
    lasso\_lars\_ic\[\-1\].criterion\_,
    n\_samples,
    lasso\_lars\_ic\[\-1\].noise\_variance\_,
)

index\_alpha\_path\_aic \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(
    lasso\_lars\_ic\[\-1\].alphas\_ \== lasso\_lars\_ic\[\-1\].alpha\_
)\[0\]

Copy to clipboard

lasso\_lars\_ic.set\_params(lassolarsic\_\_criterion\="bic").fit(X, y)

bic\_criterion \= zou\_et\_al\_criterion\_rescaling(
    lasso\_lars\_ic\[\-1\].criterion\_,
    n\_samples,
    lasso\_lars\_ic\[\-1\].noise\_variance\_,
)

index\_alpha\_path\_bic \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(
    lasso\_lars\_ic\[\-1\].alphas\_ \== lasso\_lars\_ic\[\-1\].alpha\_
)\[0\]

Copy to clipboard

Now that we collected the AIC and BIC, we can as well check that the minima of both criteria happen at the same alpha. Then, we can simplify the following plot.

index\_alpha\_path\_aic \== index\_alpha\_path\_bic

Copy to clipboard

np.True\_

Copy to clipboard

Finally, we can plot the AIC and BIC criterion and the subsequent selected regularization parameter.

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(aic\_criterion, color\="tab:blue", marker\="o", label\="AIC criterion")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(bic\_criterion, color\="tab:orange", marker\="o", label\="BIC criterion")
[plt.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
(
    index\_alpha\_path\_bic,
    aic\_criterion.min(),
    aic\_criterion.max(),
    color\="black",
    linestyle\="--",
    label\="Selected alpha",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Information criterion")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Lasso model sequence")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Lasso model selection via AIC and BIC")

Copy to clipboard

![Lasso model selection via AIC and BIC](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lars_ic_001.png)

**Total running time of the script:** (0 minutes 0.129 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_lars_ic.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_lars_ic.ipynb)

[`Download Jupyter notebook: plot_lasso_lars_ic.ipynb`](https://scikit-learn.org/stable/_downloads/51833337bfc73d152b44902e5baa50ff/plot_lasso_lars_ic.ipynb)

[`Download Python source code: plot_lasso_lars_ic.py`](https://scikit-learn.org/stable/_downloads/8c96d910ed5b614924f36c896b1934a6/plot_lasso_lars_ic.py)

[`Download zipped: plot_lasso_lars_ic.zip`](https://scikit-learn.org/stable/_downloads/30cf609ec45ebd9e95d54912b37002fa/plot_lasso_lars_ic.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_thumb.png)

[Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)

Lasso model selection: AIC-BIC / cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_thumb.png)

[Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html)

Early stopping of Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/8c96d910ed5b614924f36c896b1934a6/plot_lasso_lars_ic.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/51833337bfc73d152b44902e5baa50ff/plot_lasso_lars_ic.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/30cf609ec45ebd9e95d54912b37002fa/plot_lasso_lars_ic.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_lars_ic.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_lars_ic.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)