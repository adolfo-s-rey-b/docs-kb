[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_omp.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_omp.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_omp.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_omp.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_omp.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_omp.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html#sphx-glr-download-auto-examples-linear-model-plot-omp-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Orthogonal Matching Pursuit[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html#orthogonal-matching-pursuit "Link to this heading")

============================================================================================================================================================

Using orthogonal matching pursuit for recovering a sparse signal from a noisy measurement encoded with a dictionary

![Sparse signal recovery with Orthogonal Matching Pursuit, Sparse signal, Recovered signal from noise-free measurements, Recovered signal from noisy measurements, Recovered signal from noisy measurements with CV](https://scikit-learn.org/stable/_images/sphx_glr_plot_omp_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_sparse\_coded\_signal](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal")
from sklearn.linear\_model import [OrthogonalMatchingPursuit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
, [OrthogonalMatchingPursuitCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV")

n\_components, n\_features \= 512, 100
n\_nonzero\_coefs \= 17

\# generate the data

\# y = Xw
\# |x|\_0 = n\_nonzero\_coefs

y, X, w \= [make\_sparse\_coded\_signal](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal")
(
    n\_samples\=1,
    n\_components\=n\_components,
    n\_features\=n\_features,
    n\_nonzero\_coefs\=n\_nonzero\_coefs,
    random\_state\=0,
)
X \= X.T

(idx,) \= w.nonzero()

\# distort the clean signal
y\_noisy \= y + 0.05 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(len(y))

\# plot the sparse signal
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 7))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(4, 1, 1)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(0, 512)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Sparse signal")
[plt.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
(idx, w\[idx\])

\# plot the noise-free reconstruction
omp \= [OrthogonalMatchingPursuit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
(n\_nonzero\_coefs\=n\_nonzero\_coefs)
omp.fit(X, y)
coef \= omp.coef\_
(idx\_r,) \= coef.nonzero()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(4, 1, 2)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(0, 512)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Recovered signal from noise-free measurements")
[plt.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
(idx\_r, coef\[idx\_r\])

\# plot the noisy reconstruction
omp.fit(X, y\_noisy)
coef \= omp.coef\_
(idx\_r,) \= coef.nonzero()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(4, 1, 3)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(0, 512)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Recovered signal from noisy measurements")
[plt.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
(idx\_r, coef\[idx\_r\])

\# plot the noisy reconstruction with number of non-zeros set by CV
omp\_cv \= [OrthogonalMatchingPursuitCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV")
()
omp\_cv.fit(X, y\_noisy)
coef \= omp\_cv.coef\_
(idx\_r,) \= coef.nonzero()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(4, 1, 4)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(0, 512)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Recovered signal from noisy measurements with CV")
[plt.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
(idx\_r, coef\[idx\_r\])

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Sparse signal recovery with Orthogonal Matching Pursuit", fontsize\=16)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.228 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_omp.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_omp.ipynb)

[`Download Jupyter notebook: plot_omp.ipynb`](https://scikit-learn.org/stable/_downloads/a79c521bd835e8739e06d7dafbfc4eb4/plot_omp.ipynb)

[`Download Python source code: plot_omp.py`](https://scikit-learn.org/stable/_downloads/9b5ca5a413df494778642d75caeb33d7/plot_omp.py)

[`Download zipped: plot_omp.zip`](https://scikit-learn.org/stable/_downloads/7ea565549e75a394bc13798f2a296900/plot_omp.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_blind_source_separation_thumb.png)

[Blind source separation using FastICA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html)

Blind source separation using FastICA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/9b5ca5a413df494778642d75caeb33d7/plot_omp.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a79c521bd835e8739e06d7dafbfc4eb4/plot_omp.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/7ea565549e75a394bc13798f2a296900/plot_omp.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_omp.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_omp.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)