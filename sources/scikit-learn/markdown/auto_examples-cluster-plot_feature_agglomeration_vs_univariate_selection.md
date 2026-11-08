[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html#sphx-glr-download-auto-examples-cluster-plot-feature-agglomeration-vs-univariate-selection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Feature agglomeration vs. univariate selection[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html#feature-agglomeration-vs-univariate-selection "Link to this heading")

======================================================================================================================================================================================================================================

This example compares 2 dimensionality reduction strategies:

*   univariate feature selection with Anova
    
*   feature agglomeration with Ward hierarchical clustering
    

Both methods are compared in a regression problem using a BayesianRidge as supervised estimator.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import shutil
import tempfile

import matplotlib.pyplot as plt
import numpy as np
from joblib import [Memory](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory "joblib.Memory")
from scipy import linalg, ndimage

from sklearn import feature\_selection
from sklearn.cluster import [FeatureAgglomeration](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
from sklearn.feature\_extraction.image import grid\_to\_graph
from sklearn.linear\_model import [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")

Copy to clipboard

Set parameters

n\_samples \= 200
size \= 40  \# image size
roi\_size \= 15
snr \= 5.0
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

Copy to clipboard

Generate data

coef \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((size, size))
coef\[0:roi\_size, 0:roi\_size\] \= \-1.0
coef\[\-roi\_size:, \-roi\_size:\] \= 1.0

X \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, size\*\*2)
for x in X:  \# smooth data
    x\[:\] \= [ndimage.gaussian\_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")
(x.reshape(size, size), sigma\=1.0).ravel()
X \-= X.mean(axis\=0)
X /= X.std(axis\=0)

y \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, coef.ravel())

Copy to clipboard

add noise

noise \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(y.shape\[0\])
noise\_coef \= ([linalg.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html#scipy.linalg.norm "scipy.linalg.norm")
(y, 2) / [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(snr / 20.0)) / [linalg.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html#scipy.linalg.norm "scipy.linalg.norm")
(noise, 2)
y += noise\_coef \* noise

Copy to clipboard

Compute the coefs of a Bayesian Ridge with GridSearch

cv \= [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(2)  \# cross-validation generator for model selection
ridge \= [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
()
cachedir \= [tempfile.mkdtemp](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
()
mem \= [Memory](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory "joblib.Memory")
(location\=cachedir, verbose\=1)

Copy to clipboard

Ward agglomeration followed by BayesianRidge

connectivity \= grid\_to\_graph(n\_x\=size, n\_y\=size)
ward \= [FeatureAgglomeration](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
(n\_clusters\=10, connectivity\=connectivity, memory\=mem)
clf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(\[("ward", ward), ("ridge", ridge)\])
\# Select the optimal number of parcels with grid search
clf \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(clf, {"ward\_\_n\_clusters": \[10, 20, 30\]}, n\_jobs\=1, cv\=cv)
clf.fit(X, y)  \# set the best parameters
coef\_ \= clf.best\_estimator\_.steps\[\-1\]\[1\].coef\_
coef\_ \= clf.best\_estimator\_.steps\[0\]\[1\].inverse\_transform(coef\_)
coef\_agglomeration\_ \= coef\_.reshape(size, size)

Copy to clipboard

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[Memory\] Calling sklearn.cluster.\_agglomerative.ward\_tree...
ward\_tree(array(\[\[-0.451933, ..., -0.675318\],\
       ...,\
       \[ 0.275706, ..., -1.085711\]\], shape=(1600, 100)), connectivity=<COOrdinate sparse matrix of dtype 'int64'
        with 7840 stored elements and shape (1600, 1600)>, n\_clusters=None, return\_distance=False)
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ward\_tree - 0.0s, 0.0min
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[Memory\] Calling sklearn.cluster.\_agglomerative.ward\_tree...
ward\_tree(array(\[\[ 0.905206, ...,  0.161245\],\
       ...,\
       \[-0.849835, ..., -1.091621\]\], shape=(1600, 100)), connectivity=<COOrdinate sparse matrix of dtype 'int64'
        with 7840 stored elements and shape (1600, 1600)>, n\_clusters=None, return\_distance=False)
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ward\_tree - 0.0s, 0.0min
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[Memory\] Calling sklearn.cluster.\_agglomerative.ward\_tree...
ward\_tree(array(\[\[ 0.905206, ..., -0.675318\],\
       ...,\
       \[-0.849835, ..., -1.085711\]\], shape=(1600, 200)), connectivity=<COOrdinate sparse matrix of dtype 'int64'
        with 7840 stored elements and shape (1600, 1600)>, n\_clusters=None, return\_distance=False)
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ward\_tree - 0.0s, 0.0min

Copy to clipboard

Anova univariate feature selection followed by BayesianRidge

f\_regression \= mem.cache([feature\_selection.f\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
)  \# caching function
anova \= [feature\_selection.SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
(f\_regression)
clf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(\[("anova", anova), ("ridge", ridge)\])
\# Select the optimal percentage of features with grid search
clf \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(clf, {"anova\_\_percentile": \[5, 10, 20\]}, cv\=cv)
clf.fit(X, y)  \# set the best parameters
coef\_ \= clf.best\_estimator\_.steps\[\-1\]\[1\].coef\_
coef\_ \= clf.best\_estimator\_.steps\[0\]\[1\].inverse\_transform(coef\_.reshape(1, \-1))
coef\_selection\_ \= coef\_.reshape(size, size)

Copy to clipboard

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[Memory\] Calling sklearn.feature\_selection.\_univariate\_selection.f\_regression...
f\_regression(array(\[\[-0.451933, ...,  0.275706\],\
       ...,\
       \[-0.675318, ..., -1.085711\]\], shape=(100, 1600)),
array(\[ 25.267703, ..., -25.026711\], shape=(100,)))
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_f\_regression - 0.0s, 0.0min
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[Memory\] Calling sklearn.feature\_selection.\_univariate\_selection.f\_regression...
f\_regression(array(\[\[ 0.905206, ..., -0.849835\],\
       ...,\
       \[ 0.161245, ..., -1.091621\]\], shape=(100, 1600)),
array(\[ -27.447268, ..., -112.638768\], shape=(100,)))
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_f\_regression - 0.0s, 0.0min
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\[Memory\] Calling sklearn.feature\_selection.\_univariate\_selection.f\_regression...
f\_regression(array(\[\[ 0.905206, ..., -0.849835\],\
       ...,\
       \[-0.675318, ..., -1.085711\]\], shape=(200, 1600)),
array(\[-27.447268, ..., -25.026711\], shape=(200,)))
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_f\_regression - 0.0s, 0.0min

Copy to clipboard

Inverse the transformation to plot the results on an image

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
("all")
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7.3, 2.7))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 3, 1)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(coef, interpolation\="nearest", cmap\=plt.cm.RdBu\_r)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("True weights")
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 3, 2)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(coef\_selection\_, interpolation\="nearest", cmap\=plt.cm.RdBu\_r)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Feature Selection")
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 3, 3)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(coef\_agglomeration\_, interpolation\="nearest", cmap\=plt.cm.RdBu\_r)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Feature Agglomeration")
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.04, 0.0, 0.98, 0.94, 0.16, 0.26)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![True weights, Feature Selection, Feature Agglomeration](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_001.png)

Attempt to remove the temporary cachedir, but don’t worry if it fails

[shutil.rmtree](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")
(cachedir, ignore\_errors\=True)

Copy to clipboard

**Total running time of the script:** (0 minutes 0.439 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.ipynb)

[`Download Jupyter notebook: plot_feature_agglomeration_vs_univariate_selection.ipynb`](https://scikit-learn.org/stable/_downloads/fd3181da9f1988c60c583c95e97389f8/plot_feature_agglomeration_vs_univariate_selection.ipynb)

[`Download Python source code: plot_feature_agglomeration_vs_univariate_selection.py`](https://scikit-learn.org/stable/_downloads/6c7cb9f528114f658d5f562073332c24/plot_feature_agglomeration_vs_univariate_selection.py)

[`Download zipped: plot_feature_agglomeration_vs_univariate_selection.zip`](https://scikit-learn.org/stable/_downloads/9d4dd9a87478475252fc9d2e46a7c787/plot_feature_agglomeration_vs_univariate_selection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_thumb.png)

[HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)

HuberRegressor vs Ridge on dataset with strong outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_omp_thumb.png)

[Orthogonal Matching Pursuit](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html)

Orthogonal Matching Pursuit

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/6c7cb9f528114f658d5f562073332c24/plot_feature_agglomeration_vs_univariate_selection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/fd3181da9f1988c60c583c95e97389f8/plot_feature_agglomeration_vs_univariate_selection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/9d4dd9a87478475252fc9d2e46a7c787/plot_feature_agglomeration_vs_univariate_selection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)