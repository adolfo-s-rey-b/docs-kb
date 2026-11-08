[Skip to main content](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#sphx-glr-download-auto-examples-covariance-plot-robust-vs-empirical-covariance-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Robust vs Empirical covariance estimate[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#robust-vs-empirical-covariance-estimate "Link to this heading")

=============================================================================================================================================================================================================

The usual covariance maximum likelihood estimate is very sensitive to the presence of outliers in the data set. In such a case, it would be better to use a robust estimator of covariance to guarantee that the estimation is resistant to “erroneous” observations in the data set. [\[1\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#id4)
, [\[2\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#id5)

Minimum Covariance Determinant Estimator[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#minimum-covariance-determinant-estimator "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Minimum Covariance Determinant estimator is a robust, high-breakdown point (i.e. it can be used to estimate the covariance matrix of highly contaminated datasets, up to nsamples−nfeatures−12 outliers) estimator of covariance. The idea is to find nsamples+nfeatures+12 observations whose empirical covariance has the smallest determinant, yielding a “pure” subset of observations from which to compute standards estimates of location and covariance. After a correction step aiming at compensating the fact that the estimates were learned from only a portion of the initial data, we end up with robust estimates of the data set location and covariance.

The Minimum Covariance Determinant estimator (MCD) has been introduced by P.J.Rousseuw in [\[3\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#id6)
.

Evaluation[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#evaluation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

In this example, we compare the estimation errors that are made when using various types of location and covariance estimates on contaminated Gaussian distributed data sets:

*   The mean and the empirical covariance of the full dataset, which break down as soon as there are outliers in the data set
    
*   The robust MCD, that has a low error provided nsamples\>5nfeatures
    
*   The mean and the empirical covariance of the observations that are known to be good ones. This can be considered as a “perfect” MCD estimation, so one can trust our implementation by comparing to this case.
    

References[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#references "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![Influence of outliers on the location estimation, Influence of outliers on the covariance estimation](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_vs_empirical_covariance_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.font\_manager
import matplotlib.pyplot as plt
import numpy as np

from sklearn.covariance import [EmpiricalCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")
, [MinCovDet](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")

\# example settings
n\_samples \= 80
n\_features \= 5
repeat \= 10

range\_n\_outliers \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(
    (
        [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, n\_samples / 8, 5),
        [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(n\_samples / 8, n\_samples / 2, 5)\[1:\-1\],
    )
).astype(int)

\# definition of arrays to store results
err\_loc\_mcd \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((range\_n\_outliers.size, repeat))
err\_cov\_mcd \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((range\_n\_outliers.size, repeat))
err\_loc\_emp\_full \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((range\_n\_outliers.size, repeat))
err\_cov\_emp\_full \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((range\_n\_outliers.size, repeat))
err\_loc\_emp\_pure \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((range\_n\_outliers.size, repeat))
err\_cov\_emp\_pure \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((range\_n\_outliers.size, repeat))

\# computation
for i, n\_outliers in enumerate(range\_n\_outliers):
    for j in range(repeat):
        rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(i \* j)

        \# generate data
        X \= rng.randn(n\_samples, n\_features)
        \# add some outliers
        outliers\_index \= rng.permutation(n\_samples)\[:n\_outliers\]
        outliers\_offset \= 10.0 \* (
            [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(2, size\=(n\_outliers, n\_features)) \- 0.5
        )
        X\[outliers\_index\] += outliers\_offset
        inliers\_mask \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(n\_samples).astype(bool)
        inliers\_mask\[outliers\_index\] \= False

        \# fit a Minimum Covariance Determinant (MCD) robust estimator to data
        mcd \= [MinCovDet](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")
().fit(X)
        \# compare raw robust estimates with the true location and covariance
        err\_loc\_mcd\[i, j\] \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(mcd.location\_\*\*2)
        err\_cov\_mcd\[i, j\] \= mcd.error\_norm([np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
(n\_features))

        \# compare estimators learned from the full data set with true
        \# parameters
        err\_loc\_emp\_full\[i, j\] \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(X.mean(0) \*\* 2)
        err\_cov\_emp\_full\[i, j\] \= (
            [EmpiricalCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")
().fit(X).error\_norm([np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
(n\_features))
        )

        \# compare with an empirical covariance learned from a pure data set
        \# (i.e. "perfect" mcd)
        pure\_X \= X\[inliers\_mask\]
        pure\_location \= pure\_X.mean(0)
        pure\_emp\_cov \= [EmpiricalCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")
().fit(pure\_X)
        err\_loc\_emp\_pure\[i, j\] \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(pure\_location\*\*2)
        err\_cov\_emp\_pure\[i, j\] \= pure\_emp\_cov.error\_norm([np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
(n\_features))

\# Display results
font\_prop \= [matplotlib.font\_manager.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(size\=11)
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 1)
lw \= 2
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    range\_n\_outliers,
    err\_loc\_mcd.mean(1),
    yerr\=err\_loc\_mcd.std(1) / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(repeat),
    label\="Robust location",
    lw\=lw,
    color\="m",
)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    range\_n\_outliers,
    err\_loc\_emp\_full.mean(1),
    yerr\=err\_loc\_emp\_full.std(1) / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(repeat),
    label\="Full data set mean",
    lw\=lw,
    color\="green",
)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    range\_n\_outliers,
    err\_loc\_emp\_pure.mean(1),
    yerr\=err\_loc\_emp\_pure.std(1) / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(repeat),
    label\="Pure data set mean",
    lw\=lw,
    color\="black",
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Influence of outliers on the location estimation")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
(r"Error ($||\\mu - \\hat{\\mu}||\_2^2$)")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left", prop\=font\_prop)

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 2)
x\_size \= range\_n\_outliers.size
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    range\_n\_outliers,
    err\_cov\_mcd.mean(1),
    yerr\=err\_cov\_mcd.std(1),
    label\="Robust covariance (mcd)",
    color\="m",
)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    range\_n\_outliers\[: (x\_size // 5 + 1)\],
    err\_cov\_emp\_full.mean(1)\[: (x\_size // 5 + 1)\],
    yerr\=err\_cov\_emp\_full.std(1)\[: (x\_size // 5 + 1)\],
    label\="Full data set empirical covariance",
    color\="green",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    range\_n\_outliers\[(x\_size // 5) : (x\_size // 2 \- 1)\],
    err\_cov\_emp\_full.mean(1)\[(x\_size // 5) : (x\_size // 2 \- 1)\],
    color\="green",
    ls\="--",
)
[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
    range\_n\_outliers,
    err\_cov\_emp\_pure.mean(1),
    yerr\=err\_cov\_emp\_pure.std(1),
    label\="Pure data set empirical covariance",
    color\="black",
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Influence of outliers on the covariance estimation")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Amount of contamination (%)")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("RMSE")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="center", prop\=font\_prop)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.602 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_robust_vs_empirical_covariance.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_robust_vs_empirical_covariance.ipynb)

[`Download Jupyter notebook: plot_robust_vs_empirical_covariance.ipynb`](https://scikit-learn.org/stable/_downloads/c0510ef77613771032b63870b7baaa31/plot_robust_vs_empirical_covariance.ipynb)

[`Download Python source code: plot_robust_vs_empirical_covariance.py`](https://scikit-learn.org/stable/_downloads/55189006cedb95a2fc6bf8c216dab8f0/plot_robust_vs_empirical_covariance.py)

[`Download zipped: plot_robust_vs_empirical_covariance.zip`](https://scikit-learn.org/stable/_downloads/dcbef7d65782fe41603cd93588b9b909/plot_robust_vs_empirical_covariance.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mahalanobis_distances_thumb.png)

[Robust covariance estimation and Mahalanobis distances relevance](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html)

Robust covariance estimation and Mahalanobis distances relevance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_thumb.png)

[Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)

Ledoit-Wolf vs OAS estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_thumb.png)

[Linear and Quadratic Discriminant Analysis with covariance ellipsoid](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)

Linear and Quadratic Discriminant Analysis with covariance ellipsoid

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/55189006cedb95a2fc6bf8c216dab8f0/plot_robust_vs_empirical_covariance.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c0510ef77613771032b63870b7baaa31/plot_robust_vs_empirical_covariance.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/dcbef7d65782fe41603cd93588b9b909/plot_robust_vs_empirical_covariance.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_robust_vs_empirical_covariance.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_robust_vs_empirical_covariance.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)