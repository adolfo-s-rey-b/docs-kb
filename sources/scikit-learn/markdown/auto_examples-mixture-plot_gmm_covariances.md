[Skip to main content](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/mixture/plot_gmm_covariances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/mixture/plot_gmm_covariances.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/mixture/plot_gmm_covariances.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/mixture/plot_gmm_covariances.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/mixture/plot_gmm_covariances.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/mixture/plot_gmm_covariances.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html#sphx-glr-download-auto-examples-mixture-plot-gmm-covariances-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

GMM covariances[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html#gmm-covariances "Link to this heading")

===========================================================================================================================================

Demonstration of several covariances types for Gaussian mixture models.

See [Gaussian mixture models](https://scikit-learn.org/stable/modules/mixture.html#gmm)
 for more information on the estimator.

Although GMM are often used for clustering, we can compare the obtained clusters with the actual classes from the dataset. We initialize the means of the Gaussians with the means of the classes from the training set to make this comparison valid.

We plot predicted labels on both training and held out test data using a variety of GMM covariance types on the iris dataset. We compare GMMs with spherical, diagonal, full, and tied covariance matrices in increasing order of performance. Although one would expect full covariance to perform best in general, it is prone to overfitting on small datasets and does not generalize well to held out test data.

On the plots, train data is shown as dots, while test data is shown as crosses. The iris dataset is four-dimensional. Only the first two dimensions are shown here, and thus some points are separated in other dimensions.

![spherical, diag, tied, full](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.mixture import [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
from sklearn.model\_selection import [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")

colors \= \["navy", "turquoise", "darkorange"\]

def make\_ellipses(gmm, ax):
    for n, color in enumerate(colors):
        if gmm.covariance\_type \== "full":
            covariances \= gmm.covariances\_\[n\]\[:2, :2\]
        elif gmm.covariance\_type \== "tied":
            covariances \= gmm.covariances\_\[:2, :2\]
        elif gmm.covariance\_type \== "diag":
            covariances \= [np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
(gmm.covariances\_\[n\]\[:2\])
        elif gmm.covariance\_type \== "spherical":
            covariances \= [np.eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
(gmm.means\_.shape\[1\]) \* gmm.covariances\_\[n\]
        v, w \= [np.linalg.eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")
(covariances)
        u \= w\[0\] / [np.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")
(w\[0\])
        angle \= [np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
(u\[1\], u\[0\])
        angle \= 180 \* angle / [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
  \# convert to degrees
        v \= 2.0 \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(2.0) \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(v)
        ell \= [mpl.patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(
            gmm.means\_\[n, :2\], v\[0\], v\[1\], angle\=180 + angle, color\=color
        )
        ell.set\_clip\_box(ax.bbox)
        ell.set\_alpha(0.5)
        ax.add\_artist(ell)
        ax.set\_aspect("equal", "datalim")

iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()

\# Break up the dataset into non-overlapping training (75%) and testing
\# (25%) sets.
skf \= [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
(n\_splits\=4)
\# Only take the first fold.
train\_index, test\_index \= next(iter(skf.split(iris.data, iris.target)))

X\_train \= iris.data\[train\_index\]
y\_train \= iris.target\[train\_index\]
X\_test \= iris.data\[test\_index\]
y\_test \= iris.target\[test\_index\]

n\_classes \= len([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y\_train))

\# Try GMMs using different types of covariances.
estimators \= {
    cov\_type: [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(
        n\_components\=n\_classes, covariance\_type\=cov\_type, max\_iter\=20, random\_state\=0
    )
    for cov\_type in \["spherical", "diag", "tied", "full"\]
}

n\_estimators \= len(estimators)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(3 \* n\_estimators // 2, 6))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(
    bottom\=0.01, top\=0.95, hspace\=0.15, wspace\=0.05, left\=0.01, right\=0.99
)

for index, (name, estimator) in enumerate(estimators.items()):
    \# Since we have class labels for the training data, we can
    \# initialize the GMM parameters in a supervised manner.
    estimator.means\_init \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
        \[X\_train\[y\_train \== i\].mean(axis\=0) for i in range(n\_classes)\]
    )

    \# Train the other parameters using the EM algorithm.
    estimator.fit(X\_train)

    h \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, n\_estimators // 2, index + 1)
    make\_ellipses(estimator, h)

    for n, color in enumerate(colors):
        data \= iris.data\[iris.target \== n\]
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            data\[:, 0\], data\[:, 1\], s\=0.8, color\=color, label\=iris.target\_names\[n\]
        )
    \# Plot the test data with crosses
    for n, color in enumerate(colors):
        data \= X\_test\[y\_test \== n\]
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(data\[:, 0\], data\[:, 1\], marker\="x", color\=color)

    y\_train\_pred \= estimator.predict(X\_train)
    train\_accuracy \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_train\_pred.ravel() \== y\_train.ravel()) \* 100
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.05, 0.9, "Train accuracy: %.1f" % train\_accuracy, transform\=h.transAxes)

    y\_test\_pred \= estimator.predict(X\_test)
    test\_accuracy \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y\_test\_pred.ravel() \== y\_test.ravel()) \* 100
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.05, 0.8, "Test accuracy: %.1f" % test\_accuracy, transform\=h.transAxes)

    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(name)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(scatterpoints\=1, loc\="lower right", prop\=dict(size\=12))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.177 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm_covariances.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm_covariances.ipynb)

[`Download Jupyter notebook: plot_gmm_covariances.ipynb`](https://scikit-learn.org/stable/_downloads/471829dadf19abf3dd2b87b08c9ffc92/plot_gmm_covariances.ipynb)

[`Download Python source code: plot_gmm_covariances.py`](https://scikit-learn.org/stable/_downloads/22c1b876aa7bf8b912208cbfed5299c7/plot_gmm_covariances.py)

[`Download zipped: plot_gmm_covariances.zip`](https://scikit-learn.org/stable/_downloads/21c126a0a1b9942f3e59abf4750774bc/plot_gmm_covariances.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_thumb.png)

[Gaussian Mixture Model Ellipsoids](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)

Gaussian Mixture Model Ellipsoids

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_init_thumb.png)

[GMM Initialization Methods](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_init.html)

GMM Initialization Methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_sin_thumb.png)

[Gaussian Mixture Model Sine Curve](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html)

Gaussian Mixture Model Sine Curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/22c1b876aa7bf8b912208cbfed5299c7/plot_gmm_covariances.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/471829dadf19abf3dd2b87b08c9ffc92/plot_gmm_covariances.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/21c126a0a1b9942f3e59abf4750774bc/plot_gmm_covariances.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm_covariances.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm_covariances.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)