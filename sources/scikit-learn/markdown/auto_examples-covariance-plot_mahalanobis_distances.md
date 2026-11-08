[Skip to main content](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/covariance/plot_mahalanobis_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/covariance/plot_mahalanobis_distances.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/covariance/plot_mahalanobis_distances.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/covariance/plot_mahalanobis_distances.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/covariance/plot_mahalanobis_distances.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/covariance/plot_mahalanobis_distances.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#sphx-glr-download-auto-examples-covariance-plot-mahalanobis-distances-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Robust covariance estimation and Mahalanobis distances relevance[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#robust-covariance-estimation-and-mahalanobis-distances-relevance "Link to this heading")

======================================================================================================================================================================================================================================================

This example shows covariance estimation with Mahalanobis distances on Gaussian distributed data.

For Gaussian distributed data, the distance of an observation xi to the mode of the distribution can be computed using its Mahalanobis distance:

d(μ,Σ)(xi)2\=(xi−μ)TΣ−1(xi−μ)

where μ and Σ are the location and the covariance of the underlying Gaussian distributions.

In practice, μ and Σ are replaced by some estimates. The standard covariance maximum likelihood estimate (MLE) is very sensitive to the presence of outliers in the data set and therefore, the downstream Mahalanobis distances also are. It would be better to use a robust estimator of covariance to guarantee that the estimation is resistant to “erroneous” observations in the dataset and that the calculated Mahalanobis distances accurately reflect the true organization of the observations.

The Minimum Covariance Determinant estimator (MCD) is a robust, high-breakdown point (i.e. it can be used to estimate the covariance matrix of highly contaminated datasets, up to nsamples−nfeatures−12 outliers) estimator of covariance. The idea behind the MCD is to find nsamples+nfeatures+12 observations whose empirical covariance has the smallest determinant, yielding a “pure” subset of observations from which to compute standards estimates of location and covariance. The MCD was introduced by P.J.Rousseuw in [\[1\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#id2)
.

This example illustrates how the Mahalanobis distances are affected by outlying data. Observations drawn from a contaminating distribution are not distinguishable from the observations coming from the real, Gaussian distribution when using standard covariance MLE based Mahalanobis distances. Using MCD-based Mahalanobis distances, the two populations become distinguishable. Associated applications include outlier detection, observation ranking and clustering.

Note

See also [Robust vs Empirical covariance estimate](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html#sphx-glr-auto-examples-covariance-plot-robust-vs-empirical-covariance-py)

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate data[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#generate-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

First, we generate a dataset of 125 samples and 2 features. Both features are Gaussian distributed with mean of 0 but feature 1 has a standard deviation equal to 2 and feature 2 has a standard deviation equal to 1. Next, 25 samples are replaced with Gaussian outlier samples where feature 1 has a standard deviation equal to 1 and feature 2 has a standard deviation equal to 7.

import numpy as np

\# for consistent results
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(7)

n\_samples \= 125
n\_outliers \= 25
n\_features \= 2

\# generate Gaussian data of shape (125, 2)
gen\_cov \= [np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
(n\_features)
gen\_cov\[0, 0\] \= 2.0
X \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, n\_features), gen\_cov)
\# add some outliers
outliers\_cov \= [np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
(n\_features)
outliers\_cov\[[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(1, n\_features), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(1, n\_features)\] \= 7.0
X\[\-n\_outliers:\] \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_outliers, n\_features), outliers\_cov)

Copy to clipboard

Comparison of results[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#comparison-of-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Below, we fit MCD and MLE based covariance estimators to our data and print the estimated covariance matrices. Note that the estimated variance of feature 2 is much higher with the MLE based estimator (7.5) than that of the MCD robust estimator (1.2). This shows that the MCD based robust estimator is much more resistant to the outlier samples, which were designed to have a much larger variance in feature 2.

import matplotlib.pyplot as plt

from sklearn.covariance import [EmpiricalCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")
, [MinCovDet](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")

\# fit an MCD robust estimator to data
robust\_cov \= [MinCovDet](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")
().fit(X)
\# fit an MLE estimator to data
emp\_cov \= [EmpiricalCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")
().fit(X)
print(
    "Estimated covariance matrix:\\nMCD (Robust):\\n{}\\nMLE:\\n{}".format(
        robust\_cov.covariance\_, emp\_cov.covariance\_
    )
)

Copy to clipboard

Estimated covariance matrix:
MCD (Robust):
\[\[ 3.60075119 -0.07640781\]\
 \[-0.07640781  1.51855963\]\]
MLE:
\[\[ 3.23773583 -0.24640578\]\
 \[-0.24640578  7.51963999\]\]

Copy to clipboard

To better visualize the difference, we plot contours of the Mahalanobis distances calculated by both methods. Notice that the robust MCD based Mahalanobis distances fit the inlier black points much better, whereas the MLE based distances are more influenced by the outlier red points.

import matplotlib.lines as mlines

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 5))
\# Plot data set
inlier\_plot \= ax.scatter(X\[:, 0\], X\[:, 1\], color\="black", label\="inliers")
outlier\_plot \= ax.scatter(
    X\[:, 0\]\[\-n\_outliers:\], X\[:, 1\]\[\-n\_outliers:\], color\="red", label\="outliers"
)
ax.set\_xlim(ax.get\_xlim()\[0\], 10.0)
ax.set\_title("Mahalanobis distances of a contaminated data set")

\# Create meshgrid of feature 1 and feature 2 values
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(
    [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
()\[0\], [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
()\[1\], 100),
    [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[0\], [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()\[1\], 100),
)
zz \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\]
\# Calculate the MLE based Mahalanobis distances of the meshgrid
mahal\_emp\_cov \= emp\_cov.mahalanobis(zz)
mahal\_emp\_cov \= mahal\_emp\_cov.reshape(xx.shape)
emp\_cov\_contour \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(
    xx, yy, [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(mahal\_emp\_cov), cmap\=plt.cm.PuBu\_r, linestyles\="dashed"
)
\# Calculate the MCD based Mahalanobis distances
mahal\_robust\_cov \= robust\_cov.mahalanobis(zz)
mahal\_robust\_cov \= mahal\_robust\_cov.reshape(xx.shape)
robust\_contour \= ax.contour(
    xx, yy, [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(mahal\_robust\_cov), cmap\=plt.cm.YlOrBr\_r, linestyles\="dotted"
)

\# Add legend
ax.legend(
    \[\
        [mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="tab:blue", linestyle\="dashed"),\
        [mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="tab:orange", linestyle\="dotted"),\
        inlier\_plot,\
        outlier\_plot,\
    \],
    \["MLE dist", "MCD dist", "inliers", "outliers"\],
    loc\="upper right",
    borderaxespad\=0,
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Mahalanobis distances of a contaminated data set](https://scikit-learn.org/stable/_images/sphx_glr_plot_mahalanobis_distances_001.png)

Finally, we highlight the ability of MCD based Mahalanobis distances to distinguish outliers. We take the cubic root of the Mahalanobis distances, yielding approximately normal distributions (as suggested by Wilson and Hilferty [\[2\]](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#id3)
), then plot the values of inlier and outlier samples with boxplots. The distribution of outlier samples is more separated from the distribution of inlier samples for robust MCD based Mahalanobis distances.

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(wspace\=0.6)

\# Calculate cubic root of MLE Mahalanobis distances for samples
emp\_mahal \= emp\_cov.mahalanobis(X \- [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(X, 0)) \*\* (0.33)
\# Plot boxplots
ax1.boxplot(\[emp\_mahal\[:\-n\_outliers\], emp\_mahal\[\-n\_outliers:\]\], widths\=0.25)
\# Plot individual samples
ax1.plot(
    [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n\_samples \- n\_outliers, 1.26),
    emp\_mahal\[:\-n\_outliers\],
    "+k",
    markeredgewidth\=1,
)
ax1.plot([np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n\_outliers, 2.26), emp\_mahal\[\-n\_outliers:\], "+k", markeredgewidth\=1)
ax1.axes.set\_xticklabels(("inliers", "outliers"), size\=15)
ax1.set\_ylabel(r"$\\sqrt\[3\]{\\rm{(Mahal. dist.)}}$", size\=16)
ax1.set\_title("Using non-robust estimates\\n(Maximum Likelihood)")

\# Calculate cubic root of MCD Mahalanobis distances for samples
robust\_mahal \= robust\_cov.mahalanobis(X \- robust\_cov.location\_) \*\* (0.33)
\# Plot boxplots
ax2.boxplot(\[robust\_mahal\[:\-n\_outliers\], robust\_mahal\[\-n\_outliers:\]\], widths\=0.25)
\# Plot individual samples
ax2.plot(
    [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n\_samples \- n\_outliers, 1.26),
    robust\_mahal\[:\-n\_outliers\],
    "+k",
    markeredgewidth\=1,
)
ax2.plot([np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n\_outliers, 2.26), robust\_mahal\[\-n\_outliers:\], "+k", markeredgewidth\=1)
ax2.axes.set\_xticklabels(("inliers", "outliers"), size\=15)
ax2.set\_ylabel(r"$\\sqrt\[3\]{\\rm{(Mahal. dist.)}}$", size\=16)
ax2.set\_title("Using robust estimates\\n(Minimum Covariance Determinant)")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Using non-robust estimates (Maximum Likelihood), Using robust estimates (Minimum Covariance Determinant)](https://scikit-learn.org/stable/_images/sphx_glr_plot_mahalanobis_distances_002.png)

**Total running time of the script:** (0 minutes 0.300 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_mahalanobis_distances.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_mahalanobis_distances.ipynb)

[`Download Jupyter notebook: plot_mahalanobis_distances.ipynb`](https://scikit-learn.org/stable/_downloads/83d33d2afcbf708f386433bb1abb0785/plot_mahalanobis_distances.ipynb)

[`Download Python source code: plot_mahalanobis_distances.py`](https://scikit-learn.org/stable/_downloads/7aa7f72ae5f3350402429f7a9851b596/plot_mahalanobis_distances.py)

[`Download zipped: plot_mahalanobis_distances.zip`](https://scikit-learn.org/stable/_downloads/e9bea5fda5f2e724b4f11b783c9afee5/plot_mahalanobis_distances.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_vs_empirical_covariance_thumb.png)

[Robust vs Empirical covariance estimate](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)

Robust vs Empirical covariance estimate

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_thumb.png)

[Linear and Quadratic Discriminant Analysis with covariance ellipsoid](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)

Linear and Quadratic Discriminant Analysis with covariance ellipsoid

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/7aa7f72ae5f3350402429f7a9851b596/plot_mahalanobis_distances.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/83d33d2afcbf708f386433bb1abb0785/plot_mahalanobis_distances.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e9bea5fda5f2e724b4f11b783c9afee5/plot_mahalanobis_distances.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_mahalanobis_distances.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_mahalanobis_distances.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)