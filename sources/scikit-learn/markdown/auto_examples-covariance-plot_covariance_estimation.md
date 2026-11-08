[Skip to main content](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/covariance/plot_covariance_estimation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/covariance/plot_covariance_estimation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/covariance/plot_covariance_estimation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/covariance/plot_covariance_estimation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/covariance/plot_covariance_estimation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/covariance/plot_covariance_estimation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#sphx-glr-download-auto-examples-covariance-plot-covariance-estimation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#shrinkage-covariance-estimation-ledoitwolf-vs-oas-and-max-likelihood "Link to this heading")

===============================================================================================================================================================================================================================================================

When working with covariance estimation, the usual approach is to use a maximum likelihood estimator, such as the [`EmpiricalCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")
. It is unbiased, i.e. it converges to the true (population) covariance when given many observations. However, it can also be beneficial to regularize it, in order to reduce its variance; this, in turn, introduces some bias. This example illustrates the simple regularization used in [Shrunk Covariance](https://scikit-learn.org/stable/modules/covariance.html#shrunk-covariance)
 estimators. In particular, it focuses on how to set the amount of regularization, i.e. how to choose the bias-variance trade-off.

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#generate-sample-data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

n\_features, n\_samples \= 40, 20
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(42)
base\_X\_train \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(n\_samples, n\_features))
base\_X\_test \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(n\_samples, n\_features))

\# Color samples
coloring\_matrix \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(n\_features, n\_features))
X\_train \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(base\_X\_train, coloring\_matrix)
X\_test \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(base\_X\_test, coloring\_matrix)

Copy to clipboard

Compute the likelihood on test data[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#compute-the-likelihood-on-test-data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from scipy import linalg

from sklearn.covariance import [ShrunkCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")
, [empirical\_covariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#sklearn.covariance.empirical_covariance "sklearn.covariance.empirical_covariance")
, log\_likelihood

\# spanning a range of possible shrinkage coefficient values
shrinkages \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 0, 30)
negative\_logliks \= \[\
    \-[ShrunkCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")\
(shrinkage\=s).fit(X\_train).score(X\_test) for s in shrinkages\
\]

\# under the ground-truth model, which we would not have access to in real
\# settings
real\_cov \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(coloring\_matrix.T, coloring\_matrix)
emp\_cov \= [empirical\_covariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#sklearn.covariance.empirical_covariance "sklearn.covariance.empirical_covariance")
(X\_train)
loglik\_real \= \-log\_likelihood(emp\_cov, [linalg.inv](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html#scipy.linalg.inv "scipy.linalg.inv")
(real\_cov))

Copy to clipboard

Compare different approaches to setting the regularization parameter[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#compare-different-approaches-to-setting-the-regularization-parameter "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we compare 3 approaches:

*   Setting the parameter by cross-validating the likelihood on three folds according to a grid of potential shrinkage parameters.
    
*   A close formula proposed by Ledoit and Wolf to compute the asymptotically optimal regularization parameter (minimizing an MSE criterion), yielding the [`LedoitWolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
     covariance estimate.
    
*   An improvement of the Ledoit-Wolf shrinkage, the [`OAS`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
    , proposed by Chen et al. [\[1\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#id1)
    . Its convergence is significantly better under the assumption that the data are Gaussian, in particular for small samples.
    

from sklearn.covariance import [OAS](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
, [LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")

\# GridSearch for an optimal shrinkage coefficient
tuned\_parameters \= \[{"shrinkage": shrinkages}\]
cv \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
([ShrunkCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")
(), tuned\_parameters)
cv.fit(X\_train)

\# Ledoit-Wolf optimal shrinkage coefficient estimate
lw \= [LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
()
loglik\_lw \= lw.fit(X\_train).score(X\_test)

\# OAS coefficient estimate
oa \= [OAS](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
()
loglik\_oa \= oa.fit(X\_train).score(X\_test)

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#plot-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

To quantify estimation error, we plot the likelihood of unseen data for different values of the shrinkage parameter. We also show the choices by cross-validation, or with the LedoitWolf and OAS estimates.

import matplotlib.pyplot as plt

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Regularized covariance: likelihood and shrinkage coefficient")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Regularization parameter: shrinkage coefficient")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Error: negative log-likelihood on test data")
\# range shrinkage curve
[plt.loglog](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog "matplotlib.pyplot.loglog")
(shrinkages, negative\_logliks, label\="Negative log-likelihood")

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(), 2 \* \[loglik\_real\], "--r", label\="Real covariance likelihood")

\# adjust view
lik\_max \= [np.amax](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")
(negative\_logliks)
lik\_min \= [np.amin](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")
(negative\_logliks)
ymin \= lik\_min \- 6.0 \* [np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
(([plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[1\] \- [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[0\]))
ymax \= lik\_max + 10.0 \* [np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
(lik\_max \- lik\_min)
xmin \= shrinkages\[0\]
xmax \= shrinkages\[\-1\]
\# LW likelihood
[plt.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
(
    lw.shrinkage\_,
    ymin,
    \-loglik\_lw,
    color\="magenta",
    linewidth\=3,
    label\="Ledoit-Wolf estimate",
)
\# OAS likelihood
[plt.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
(
    oa.shrinkage\_, ymin, \-loglik\_oa, color\="purple", linewidth\=3, label\="OAS estimate"
)
\# best CV estimator likelihood
[plt.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
(
    cv.best\_estimator\_.shrinkage,
    ymin,
    \-cv.best\_estimator\_.score(X\_test),
    color\="cyan",
    linewidth\=3,
    label\="Cross-validation best estimate",
)

[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(ymin, ymax)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(xmin, xmax)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Regularized covariance: likelihood and shrinkage coefficient](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_001.png)

Note

The maximum likelihood estimate corresponds to no shrinkage, and thus performs poorly. The Ledoit-Wolf estimate performs really well, as it is close to the optimal and is not computationally costly. In this example, the OAS estimate is a bit further away. Interestingly, both approaches outperform cross-validation, which is significantly most computationally costly.

**Total running time of the script:** (0 minutes 0.468 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_covariance_estimation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_covariance_estimation.ipynb)

[`Download Jupyter notebook: plot_covariance_estimation.ipynb`](https://scikit-learn.org/stable/_downloads/503dcbe9fdb65a8f83bd6e34b3adc769/plot_covariance_estimation.ipynb)

[`Download Python source code: plot_covariance_estimation.py`](https://scikit-learn.org/stable/_downloads/29c38fef6831de20867ac61e068f2461/plot_covariance_estimation.py)

[`Download zipped: plot_covariance_estimation.zip`](https://scikit-learn.org/stable/_downloads/bbe339f46fa25869444a824be9486f14/plot_covariance_estimation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_thumb.png)

[Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)

Ledoit-Wolf vs OAS estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_thumb.png)

[Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)

Sparse inverse covariance estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/29c38fef6831de20867ac61e068f2461/plot_covariance_estimation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/503dcbe9fdb65a8f83bd6e34b3adc769/plot_covariance_estimation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/bbe339f46fa25869444a824be9486f14/plot_covariance_estimation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_covariance_estimation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_covariance_estimation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)