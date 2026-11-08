[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_outlier_detection_wine.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_outlier_detection_wine.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_outlier_detection_wine.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_outlier_detection_wine.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_outlier_detection_wine.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_outlier_detection_wine.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html#sphx-glr-download-auto-examples-applications-plot-outlier-detection-wine-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Outlier detection on a real data set[#](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html#outlier-detection-on-a-real-data-set "Link to this heading")

=================================================================================================================================================================================================

This example illustrates the need for robust covariance estimation on a real data set. It is useful both for outlier detection and for a better understanding of the data structure.

We selected two sets of two variables from the Wine data set as an illustration of what kind of analysis can be done with several outlier detection tools. For the purpose of visualization, we are working with two-dimensional examples, but one should be aware that things are not so trivial in high-dimension, as it will be pointed out.

In both examples below, the main result is that the empirical covariance estimate, as a non-robust one, is highly influenced by the heterogeneous structure of the observations. Although the robust covariance estimate is able to focus on the main mode of the data distribution, it sticks to the assumption that the data should be Gaussian distributed, yielding some biased estimation of the data structure, but yet accurate to some extent. The One-Class SVM does not assume any parametric form of the data distribution and can therefore model the complex shape of the data much better.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

First example[#](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html#first-example "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The first example illustrates how the Minimum Covariance Determinant robust estimator can help concentrate on a relevant cluster when outlying points exist. Here the empirical covariance estimation is skewed by points outside of the main cluster. Of course, some screening tools would have pointed out the presence of two clusters (Support Vector Machines, Gaussian Mixture Models, univariate outlier detection, …). But had it been a high-dimensional example, none of these could be applied that easily.

from sklearn.covariance import [EllipticEnvelope](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import [OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")

estimators \= {
    "Empirical Covariance": [EllipticEnvelope](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
(support\_fraction\=1.0, contamination\=0.25),
    "Robust Covariance (Minimum Covariance Determinant)": [EllipticEnvelope](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
(
        contamination\=0.25
    ),
    "OCSVM": [OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
(nu\=0.25, gamma\=0.35),
}

Copy to clipboard

import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from sklearn.datasets import [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")

X \= [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
()\["data"\]\[:, \[1, 2\]\]  \# two clusters

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
colors \= \["tab:blue", "tab:orange", "tab:red"\]
\# Learn a frontier for outlier detection with several classifiers
legend\_lines \= \[\]
for color, (name, estimator) in zip(colors, estimators.items()):
    estimator.fit(X)
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        estimator,
        X,
        response\_method\="decision\_function",
        plot\_method\="contour",
        levels\=\[0\],
        colors\=color,
        ax\=ax,
    )
    legend\_lines.append([mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
(\[\], \[\], color\=color, label\=name))

ax.scatter(X\[:, 0\], X\[:, 1\], color\="black")
bbox\_args \= dict(boxstyle\="round", fc\="0.8")
arrow\_args \= dict(arrowstyle\="->")
ax.annotate(
    "outlying points",
    xy\=(4, 2),
    xycoords\="data",
    textcoords\="data",
    xytext\=(3, 1.25),
    bbox\=bbox\_args,
    arrowprops\=arrow\_args,
)
ax.legend(handles\=legend\_lines, loc\="upper center")
\_ \= ax.set(
    xlabel\="ash",
    ylabel\="malic\_acid",
    title\="Outlier detection on a real data set (wine recognition)",
)

Copy to clipboard

![Outlier detection on a real data set (wine recognition)](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_001.png)

Second example[#](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html#second-example "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

The second example shows the ability of the Minimum Covariance Determinant robust estimator of covariance to concentrate on the main mode of the data distribution: the location seems to be well estimated, although the covariance is hard to estimate due to the banana-shaped distribution. Anyway, we can get rid of some outlying observations. The One-Class SVM is able to capture the real data structure, but the difficulty is to adjust its kernel bandwidth parameter so as to obtain a good compromise between the shape of the data scatter matrix and the risk of over-fitting the data.

X \= [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
()\["data"\]\[:, \[6, 9\]\]  \# "banana"-shaped

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
colors \= \["tab:blue", "tab:orange", "tab:red"\]
\# Learn a frontier for outlier detection with several classifiers
legend\_lines \= \[\]
for color, (name, estimator) in zip(colors, estimators.items()):
    estimator.fit(X)
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        estimator,
        X,
        response\_method\="decision\_function",
        plot\_method\="contour",
        levels\=\[0\],
        colors\=color,
        ax\=ax,
    )
    legend\_lines.append([mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
(\[\], \[\], color\=color, label\=name))

ax.scatter(X\[:, 0\], X\[:, 1\], color\="black")
ax.legend(handles\=legend\_lines, loc\="upper center")
ax.set(
    xlabel\="flavanoids",
    ylabel\="color\_intensity",
    title\="Outlier detection on a real data set (wine recognition)",
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Outlier detection on a real data set (wine recognition)](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_002.png)

**Total running time of the script:** (0 minutes 0.452 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_outlier_detection_wine.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_outlier_detection_wine.ipynb)

[`Download Jupyter notebook: plot_outlier_detection_wine.ipynb`](https://scikit-learn.org/stable/_downloads/dd28338257df6d2a7e6b9ff5f2743272/plot_outlier_detection_wine.ipynb)

[`Download Python source code: plot_outlier_detection_wine.py`](https://scikit-learn.org/stable/_downloads/609eccf9ab7d476daf68967ce1fce0b7/plot_outlier_detection_wine.py)

[`Download zipped: plot_outlier_detection_wine.zip`](https://scikit-learn.org/stable/_downloads/d24b370bfcf725dbb3feedb9cb874c73/plot_outlier_detection_wine.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_outlier_detection_thumb.png)

[Outlier detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html)

Outlier detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_vs_empirical_covariance_thumb.png)

[Robust vs Empirical covariance estimate](https://scikit-learn.org/stable/auto_examples/covariance/plot_robust_vs_empirical_covariance.html)

Robust vs Empirical covariance estimate

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_thumb.png)

[Linear and Quadratic Discriminant Analysis with covariance ellipsoid](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)

Linear and Quadratic Discriminant Analysis with covariance ellipsoid

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/609eccf9ab7d476daf68967ce1fce0b7/plot_outlier_detection_wine.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/dd28338257df6d2a7e6b9ff5f2743272/plot_outlier_detection_wine.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d24b370bfcf725dbb3feedb9cb874c73/plot_outlier_detection_wine.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_outlier_detection_wine.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_outlier_detection_wine.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)