[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#sphx-glr-download-auto-examples-linear-model-plot-bayesian-ridge-curvefit-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Curve Fitting with Bayesian Ridge Regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#curve-fitting-with-bayesian-ridge-regression "Link to this heading")

==================================================================================================================================================================================================================

Computes a Bayesian Ridge Regression of Sinusoids.

See [Bayesian Ridge Regression](https://scikit-learn.org/stable/modules/linear_model.html#bayesian-ridge-regression)
 for more information on the regressor.

In general, when fitting a curve with a polynomial by Bayesian ridge regression, the selection of initial values of the regularization parameters (alpha, lambda) may be important. This is because the regularization parameters are determined by an iterative procedure that depends on initial values.

In this example, the sinusoid is approximated by a polynomial using different pairs of initial values.

When starting from the default values (alpha\_init = 1.90, lambda\_init = 1.), the bias of the resulting curve is large, and the variance is small. So, lambda\_init should be relatively small (1.e-3) so as to reduce the bias.

Also, by evaluating log marginal likelihood (L) of these models, we can determine which one is better. It can be concluded that the model with larger L is more likely.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sinusoidal data with noise[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#generate-sinusoidal-data-with-noise "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

def func(x):
    return [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* x)

size \= 25
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1234)
x\_train \= rng.uniform(0.0, 1.0, size)
y\_train \= func(x\_train) + rng.normal(scale\=0.1, size\=size)
x\_test \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, 100)

Copy to clipboard

Fit by cubic polynomial[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#fit-by-cubic-polynomial "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.linear\_model import [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")

n\_order \= 3
X\_train \= [np.vander](https://numpy.org/doc/stable/reference/generated/numpy.vander.html#numpy.vander "numpy.vander")
(x\_train, n\_order + 1, increasing\=True)
X\_test \= [np.vander](https://numpy.org/doc/stable/reference/generated/numpy.vander.html#numpy.vander "numpy.vander")
(x\_test, n\_order + 1, increasing\=True)
reg \= [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
(tol\=1e-6, fit\_intercept\=False, compute\_score\=True)

Copy to clipboard

Plot the true and predicted curves with log marginal likelihood (L)[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#plot-the-true-and-predicted-curves-with-log-marginal-likelihood-l "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(8, 4))
for i, ax in enumerate(axes):
    \# Bayesian ridge regression with different initial value pairs
    if i \== 0:
        init \= \[1 / [np.var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")\
(y\_train), 1.0\]  \# Default values
    elif i \== 1:
        init \= \[1.0, 1e-3\]
        reg.set\_params(alpha\_init\=init\[0\], lambda\_init\=init\[1\])
    reg.fit(X\_train, y\_train)
    ymean, ystd \= reg.predict(X\_test, return\_std\=True)

    ax.plot(x\_test, func(x\_test), color\="blue", label\="sin($2\\\\pi x$)")
    ax.scatter(x\_train, y\_train, s\=50, alpha\=0.5, label\="observation")
    ax.plot(x\_test, ymean, color\="red", label\="predict mean")
    ax.fill\_between(
        x\_test, ymean \- ystd, ymean + ystd, color\="pink", alpha\=0.5, label\="predict std"
    )
    ax.set\_ylim(\-1.3, 1.3)
    ax.legend()
    title \= "$\\\\alpha$\_init$={:.2f},\\\\ \\\\lambda$\_init$={}$".format(init\[0\], init\[1\])
    if i \== 0:
        title += " (Default)"
    ax.set\_title(title, fontsize\=12)
    text \= "$\\\\alpha={:.1f}$\\n$\\\\lambda={:.3f}$\\n$L={:.1f}$".format(
        reg.alpha\_, reg.lambda\_, reg.scores\_\[\-1\]
    )
    ax.text(0.05, \-1.0, text, fontsize\=12)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![$\alpha$_init$=1.90,\ \lambda$_init$=1.0$ (Default), $\alpha$_init$=1.00,\ \lambda$_init$=0.001$](https://scikit-learn.org/stable/_images/sphx_glr_plot_bayesian_ridge_curvefit_001.png)

**Total running time of the script:** (0 minutes 0.277 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_bayesian_ridge_curvefit.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_bayesian_ridge_curvefit.ipynb)

[`Download Jupyter notebook: plot_bayesian_ridge_curvefit.ipynb`](https://scikit-learn.org/stable/_downloads/255cd67462a63d35efce903bdc60d75d/plot_bayesian_ridge_curvefit.ipynb)

[`Download Python source code: plot_bayesian_ridge_curvefit.py`](https://scikit-learn.org/stable/_downloads/3e3e33acc340cbabe46e148ccc4c89cb/plot_bayesian_ridge_curvefit.py)

[`Download zipped: plot_bayesian_ridge_curvefit.zip`](https://scikit-learn.org/stable/_downloads/70d94cdb64ace13b2b2bcb80c1b9986a/plot_bayesian_ridge_curvefit.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_thumb.png)

[Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)

Using KBinsDiscretizer to discretize continuous features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/3e3e33acc340cbabe46e148ccc4c89cb/plot_bayesian_ridge_curvefit.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/255cd67462a63d35efce903bdc60d75d/plot_bayesian_ridge_curvefit.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/70d94cdb64ace13b2b2bcb80c1b9986a/plot_bayesian_ridge_curvefit.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_bayesian_ridge_curvefit.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_bayesian_ridge_curvefit.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)