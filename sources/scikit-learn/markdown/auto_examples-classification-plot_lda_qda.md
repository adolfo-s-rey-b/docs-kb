[Skip to main content](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/classification/plot_lda_qda.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/classification/plot_lda_qda.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/classification/plot_lda_qda.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/classification/plot_lda_qda.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/classification/plot_lda_qda.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/classification/plot_lda_qda.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html#sphx-glr-download-auto-examples-classification-plot-lda-qda-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Linear and Quadratic Discriminant Analysis with covariance ellipsoid[#](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html#linear-and-quadratic-discriminant-analysis-with-covariance-ellipsoid "Link to this heading")

====================================================================================================================================================================================================================================================

This example plots the covariance ellipsoids of each class and the decision boundary learned by [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
 (LDA) and [`QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
 (QDA). The ellipsoids display the double standard deviation for each class. With LDA, the standard deviation is the same for all the classes, while each class has its own standard deviation with QDA.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html#data-generation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

First, we define a function to generate synthetic data. It creates two blobs centered at `(0, 0)` and `(1, 1)`. Each blob is assigned a specific class. The dispersion of the blob is controlled by the parameters `cov_class_1` and `cov_class_2`, that are the covariance matrices used when generating the samples from the Gaussian distributions.

import numpy as np

def make\_data(n\_samples, n\_features, cov\_class\_1, cov\_class\_2, seed\=0):
    rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(seed)
    X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(
        \[\
            rng.randn(n\_samples, n\_features) @ cov\_class\_1,\
            rng.randn(n\_samples, n\_features) @ cov\_class\_2 + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\[1, 1\]),\
        \]
    )
    y \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[[np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")\
(n\_samples), [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")\
(n\_samples)\])
    return X, y

Copy to clipboard

We generate three datasets. In the first dataset, the two classes share the same covariance matrix, and this covariance matrix has the specificity of being spherical (isotropic). The second dataset is similar to the first one but does not enforce the covariance to be spherical. Finally, the third dataset has a non-spherical covariance matrix for each class.

covariance \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[1, 0\], \[0, 1\]\])
X\_isotropic\_covariance, y\_isotropic\_covariance \= make\_data(
    n\_samples\=1\_000,
    n\_features\=2,
    cov\_class\_1\=covariance,
    cov\_class\_2\=covariance,
    seed\=0,
)
covariance \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.0, \-0.23\], \[0.83, 0.23\]\])
X\_shared\_covariance, y\_shared\_covariance \= make\_data(
    n\_samples\=300,
    n\_features\=2,
    cov\_class\_1\=covariance,
    cov\_class\_2\=covariance,
    seed\=0,
)
cov\_class\_1 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.0, \-1.0\], \[2.5, 0.7\]\]) \* 2.0
cov\_class\_2 \= cov\_class\_1.T
X\_different\_covariance, y\_different\_covariance \= make\_data(
    n\_samples\=300,
    n\_features\=2,
    cov\_class\_1\=cov\_class\_1,
    cov\_class\_2\=cov\_class\_2,
    seed\=0,
)

Copy to clipboard

Plotting Functions[#](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html#plotting-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

The code below is used to plot several pieces of information from the estimators used, i.e., [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
 (LDA) and [`QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
 (QDA). The displayed information includes:

*   the decision boundary based on the probability estimate of the estimator;
    
*   a scatter plot with circles representing the well-classified samples;
    
*   a scatter plot with crosses representing the misclassified samples;
    
*   the mean of each class, estimated by the estimator, marked with a star;
    
*   the estimated covariance represented by an ellipse at 2 standard deviations from the mean.
    

import matplotlib as mpl
from matplotlib import colors

from sklearn.inspection import DecisionBoundaryDisplay

def plot\_ellipse(mean, cov, color, ax):
    v, w \= [np.linalg.eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")
(cov)
    u \= w\[0\] / [np.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")
(w\[0\])
    angle \= [np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
(u\[1\] / u\[0\])
    angle \= 180 \* angle / [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
  \# convert to degrees
    \# filled Gaussian at 2 standard deviation
    ell \= [mpl.patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(
        mean,
        2 \* v\[0\] \*\* 0.5,
        2 \* v\[1\] \*\* 0.5,
        angle\=180 + angle,
        facecolor\=color,
        edgecolor\="black",
        linewidth\=2,
    )
    ell.set\_clip\_box(ax.bbox)
    ell.set\_alpha(0.4)
    ax.add\_artist(ell)

def plot\_result(estimator, X, y, ax):
    cmap \= [colors.ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["tab:red", "tab:blue"\])
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        estimator,
        X,
        response\_method\="predict\_proba",
        plot\_method\="pcolormesh",
        ax\=ax,
        cmap\="RdBu",
        alpha\=0.3,
    )
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        estimator,
        X,
        response\_method\="predict\_proba",
        plot\_method\="contour",
        ax\=ax,
        alpha\=1.0,
        levels\=\[0.5\],
    )
    y\_pred \= estimator.predict(X)
    X\_right, y\_right \= X\[y \== y\_pred\], y\[y \== y\_pred\]
    X\_wrong, y\_wrong \= X\[y != y\_pred\], y\[y != y\_pred\]
    ax.scatter(X\_right\[:, 0\], X\_right\[:, 1\], c\=y\_right, s\=20, cmap\=cmap, alpha\=0.5)
    ax.scatter(
        X\_wrong\[:, 0\],
        X\_wrong\[:, 1\],
        c\=y\_wrong,
        s\=30,
        cmap\=cmap,
        alpha\=0.9,
        marker\="x",
    )
    ax.scatter(
        estimator.means\_\[:, 0\],
        estimator.means\_\[:, 1\],
        c\="yellow",
        s\=200,
        marker\="\*",
        edgecolor\="black",
    )

    if isinstance(estimator, [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
):
        covariance \= \[estimator.covariance\_\] \* 2
    else:
        covariance \= estimator.covariance\_
    plot\_ellipse(estimator.means\_\[0\], covariance\[0\], "tab:red", ax)
    plot\_ellipse(estimator.means\_\[1\], covariance\[1\], "tab:blue", ax)

    ax.set\_box\_aspect(1)
    ax.spines\["top"\].set\_visible(False)
    ax.spines\["bottom"\].set\_visible(False)
    ax.spines\["left"\].set\_visible(False)
    ax.spines\["right"\].set\_visible(False)
    ax.set(xticks\=\[\], yticks\=\[\])

Copy to clipboard

Comparison of LDA and QDA[#](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html#comparison-of-lda-and-qda "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

We compare the two estimators LDA and QDA on all three datasets.

import matplotlib.pyplot as plt

from sklearn.discriminant\_analysis import (
    [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
,
    [QuadraticDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
,
)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3, ncols\=2, sharex\="row", sharey\="row", figsize\=(8, 12))

lda \= [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(solver\="svd", store\_covariance\=True)
qda \= [QuadraticDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
(solver\="svd", store\_covariance\=True)

for ax\_row, X, y in zip(
    axs,
    (X\_isotropic\_covariance, X\_shared\_covariance, X\_different\_covariance),
    (y\_isotropic\_covariance, y\_shared\_covariance, y\_different\_covariance),
):
    lda.fit(X, y)
    plot\_result(lda, X, y, ax\_row\[0\])
    qda.fit(X, y)
    plot\_result(qda, X, y, ax\_row\[1\])

axs\[0, 0\].set\_title("Linear Discriminant Analysis")
axs\[0, 0\].set\_ylabel("Data with fixed and spherical covariance")
axs\[1, 0\].set\_ylabel("Data with fixed covariance")
axs\[0, 1\].set\_title("Quadratic Discriminant Analysis")
axs\[2, 0\].set\_ylabel("Data with varying covariances")
fig.suptitle(
    "Linear Discriminant Analysis vs Quadratic Discriminant Analysis",
    y\=0.94,
    fontsize\=15,
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Linear Discriminant Analysis vs Quadratic Discriminant Analysis, Linear Discriminant Analysis, Quadratic Discriminant Analysis](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_001.png)

The first important thing to notice is that LDA and QDA are equivalent for the first and second datasets. Indeed, the major difference is that LDA assumes that the covariance matrix of each class is equal, while QDA estimates a covariance matrix per class. Since in these cases the data generative process has the same covariance matrix for both classes, QDA estimates two covariance matrices that are (almost) equal and therefore equivalent to the covariance matrix estimated by LDA.

In the first dataset the covariance matrix used to generate the dataset is spherical, which results in a discriminant boundary that aligns with the perpendicular bisector between the two means. This is no longer the case for the second dataset. The discriminant boundary only passes through the middle of the two means.

Finally, in the third dataset, we observe the real difference between LDA and QDA. QDA fits two covariance matrices and provides a non-linear discriminant boundary, whereas LDA underfits since it assumes that both classes share a single covariance matrix.

**Total running time of the script:** (0 minutes 0.376 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_lda_qda.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_lda_qda.ipynb)

[`Download Jupyter notebook: plot_lda_qda.ipynb`](https://scikit-learn.org/stable/_downloads/1a2ab00bbfd4eb80e0afca13d83e2a14/plot_lda_qda.ipynb)

[`Download Python source code: plot_lda_qda.py`](https://scikit-learn.org/stable/_downloads/d7c704916c145b9b383b87c04245efda/plot_lda_qda.py)

[`Download zipped: plot_lda_qda.zip`](https://scikit-learn.org/stable/_downloads/e4c20bdc523a6a0313bebc9cf95a9883/plot_lda_qda.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_thumb.png)

[Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)

Sparse inverse covariance estimation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/d7c704916c145b9b383b87c04245efda/plot_lda_qda.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1a2ab00bbfd4eb80e0afca13d83e2a14/plot_lda_qda.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e4c20bdc523a6a0313bebc9cf95a9883/plot_lda_qda.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_lda_qda.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_lda_qda.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)