[Skip to main content](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/covariance/plot_lw_vs_oas.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/covariance/plot_lw_vs_oas.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/covariance/plot_lw_vs_oas.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/covariance/plot_lw_vs_oas.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/covariance/plot_lw_vs_oas.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/covariance/plot_lw_vs_oas.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html#sphx-glr-download-auto-examples-covariance-plot-lw-vs-oas-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Ledoit-Wolf vs OAS estimation[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html#ledoit-wolf-vs-oas-estimation "Link to this heading")

====================================================================================================================================================================

The usual covariance maximum likelihood estimate can be regularized using shrinkage. Ledoit and Wolf proposed a close formula to compute the asymptotically optimal shrinkage parameter (minimizing an MSE criterion), yielding the Ledoit-Wolf covariance estimate.

Chen et al. [\[1\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html#id3)
 proposed an improvement of the Ledoit-Wolf shrinkage parameter, the OAS coefficient, whose convergence is significantly better under the assumption that the data are Gaussian.

This example, inspired from Chen’s publication [\[1\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html#id3)
, shows a comparison of the estimated MSE of the LW and OAS methods, using Gaussian distributed data.

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import [cholesky](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky.html#scipy.linalg.cholesky "scipy.linalg.cholesky")
, [toeplitz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.toeplitz.html#scipy.linalg.toeplitz "scipy.linalg.toeplitz")

from sklearn.covariance import [OAS](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
, [LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

Copy to clipboard

n\_features \= 100
\# simulation covariance matrix (AR(1) process)
r \= 0.1
real\_cov \= [toeplitz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.toeplitz.html#scipy.linalg.toeplitz "scipy.linalg.toeplitz")
(r \*\* [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_features))
coloring\_matrix \= [cholesky](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky.html#scipy.linalg.cholesky "scipy.linalg.cholesky")
(real\_cov)

n\_samples\_range \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(6, 31, 1)
repeat \= 100
lw\_mse \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_samples\_range.size, repeat))
oa\_mse \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_samples\_range.size, repeat))
lw\_shrinkage \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_samples\_range.size, repeat))
oa\_shrinkage \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_samples\_range.size, repeat))
for i, n\_samples in enumerate(n\_samples\_range):
    for j in range(repeat):
        X \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(n\_samples, n\_features)), coloring\_matrix.T)

        lw \= [LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
(store\_precision\=False, assume\_centered\=True)
        lw.fit(X)
        lw\_mse\[i, j\] \= lw.error\_norm(real\_cov, scaling\=False)
        lw\_shrinkage\[i, j\] \= lw.shrinkage\_

        oa \= [OAS](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
(store\_precision\=False, assume\_centered\=True)
        oa.fit(X)
        oa\_mse\[i, j\] \= oa.error\_norm(real\_cov, scaling\=False)
        oa\_shrinkage\[i, j\] \= oa.shrinkage\_

\# plot MSE
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 1)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    n\_samples\_range,
    lw\_mse.mean(1),
    yerr\=lw\_mse.std(1),
    label\="Ledoit-Wolf",
    color\="navy",
    lw\=2,
)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    n\_samples\_range,
    oa\_mse.mean(1),
    yerr\=oa\_mse.std(1),
    label\="OAS",
    color\="darkorange",
    lw\=2,
)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Squared error")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Comparison of covariance estimators")
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(5, 31)

\# plot shrinkage coefficient
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 2)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    n\_samples\_range,
    lw\_shrinkage.mean(1),
    yerr\=lw\_shrinkage.std(1),
    label\="Ledoit-Wolf",
    color\="navy",
    lw\=2,
)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    n\_samples\_range,
    oa\_shrinkage.mean(1),
    yerr\=oa\_shrinkage.std(1),
    label\="OAS",
    color\="darkorange",
    lw\=2,
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("n\_samples")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Shrinkage")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
([plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[0\], 1.0 + ([plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[1\] \- [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[0\]) / 10.0)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(5, 31)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Comparison of covariance estimators](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_001.png)

**Total running time of the script:** (0 minutes 3.190 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_lw_vs_oas.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_lw_vs_oas.ipynb)

[`Download Jupyter notebook: plot_lw_vs_oas.ipynb`](https://scikit-learn.org/stable/_downloads/6d7313d090e7392c48a23c84b6fdec0c/plot_lw_vs_oas.ipynb)

[`Download Python source code: plot_lw_vs_oas.py`](https://scikit-learn.org/stable/_downloads/7b17afb06830fd0b89d4d902646dc86e/plot_lw_vs_oas.py)

[`Download zipped: plot_lw_vs_oas.zip`](https://scikit-learn.org/stable/_downloads/f9d87a4251e5f99e531dd4a41c01b46c/plot_lw_vs_oas.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_vs_empirical_covariance_thumb.png)

[Robust vs Empirical covariance estimate](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)

Robust vs Empirical covariance estimate

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_thumb.png)

[Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)

Sparse inverse covariance estimation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/7b17afb06830fd0b89d4d902646dc86e/plot_lw_vs_oas.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6d7313d090e7392c48a23c84b6fdec0c/plot_lw_vs_oas.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f9d87a4251e5f99e531dd4a41c01b46c/plot_lw_vs_oas.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_lw_vs_oas.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_lw_vs_oas.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)