[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_digits_kde_sampling.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_digits_kde_sampling.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_digits_kde_sampling.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_digits_kde_sampling.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_digits_kde_sampling.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_digits_kde_sampling.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html#sphx-glr-download-auto-examples-neighbors-plot-digits-kde-sampling-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Kernel Density Estimation[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html#kernel-density-estimation "Link to this heading")

=====================================================================================================================================================================

This example shows how kernel density estimation (KDE), a powerful non-parametric density estimation technique, can be used to learn a generative model for a dataset. With this generative model in place, new samples can be drawn. These new samples reflect the underlying model of the data.

![Selection from the input data, ](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_001.png)

best bandwidth: 3.79269019073225

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.neighbors import [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")

\# load the data
digits \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()

\# project the 64-dimensional data to a lower dimension
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=15, whiten\=False)
data \= pca.fit\_transform(digits.data)

\# use grid search cross-validation to optimize the bandwidth
params \= {"bandwidth": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-1, 1, 20)}
grid \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
([KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
(), params)
grid.fit(data)

print("best bandwidth: {0}".format(grid.best\_estimator\_.bandwidth))

\# use the best estimator to compute the kernel density estimate
kde \= grid.best\_estimator\_

\# sample 44 new points from the data
new\_data \= kde.sample(44, random\_state\=0)
new\_data \= pca.inverse\_transform(new\_data)

\# turn data into a 4x11 grid
new\_data \= new\_data.reshape((4, 11, \-1))
real\_data \= digits.data\[:44\].reshape((4, 11, \-1))

\# plot real digits and resampled digits
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(9, 11, subplot\_kw\=dict(xticks\=\[\], yticks\=\[\]))
for j in range(11):
    ax\[4, j\].set\_visible(False)
    for i in range(4):
        im \= ax\[i, j\].imshow(
            real\_data\[i, j\].reshape((8, 8)), cmap\=plt.cm.binary, interpolation\="nearest"
        )
        im.set\_clim(0, 16)
        im \= ax\[i + 5, j\].imshow(
            new\_data\[i, j\].reshape((8, 8)), cmap\=plt.cm.binary, interpolation\="nearest"
        )
        im.set\_clim(0, 16)

ax\[0, 5\].set\_title("Selection from the input data")
ax\[5, 5\].set\_title('"New" digits drawn from the kernel density model')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.659 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_digits_kde_sampling.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_digits_kde_sampling.ipynb)

[`Download Jupyter notebook: plot_digits_kde_sampling.ipynb`](https://scikit-learn.org/stable/_downloads/c82bd3e95b1fad595c0ed8d47e58d845/plot_digits_kde_sampling.ipynb)

[`Download Python source code: plot_digits_kde_sampling.py`](https://scikit-learn.org/stable/_downloads/02a7bbce3c39c70d62d80e875968e5c6/plot_digits_kde_sampling.py)

[`Download zipped: plot_digits_kde_sampling.zip`](https://scikit-learn.org/stable/_downloads/207f6ccc40c29c40986fcdad2dcf463f/plot_digits_kde_sampling.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_digits_thumb.png)

[Recursive feature elimination](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html)

Recursive feature elimination

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_thumb.png)

[Simple 1D Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)

Simple 1D Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/02a7bbce3c39c70d62d80e875968e5c6/plot_digits_kde_sampling.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c82bd3e95b1fad595c0ed8d47e58d845/plot_digits_kde_sampling.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/207f6ccc40c29c40986fcdad2dcf463f/plot_digits_kde_sampling.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_digits_kde_sampling.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_digits_kde_sampling.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)