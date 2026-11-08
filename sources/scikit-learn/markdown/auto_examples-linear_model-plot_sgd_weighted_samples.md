[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgd_weighted_samples.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgd_weighted_samples.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgd_weighted_samples.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgd_weighted_samples.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgd_weighted_samples.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgd_weighted_samples.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html#sphx-glr-download-auto-examples-linear-model-plot-sgd-weighted-samples-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SGD: Weighted samples[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html#sgd-weighted-samples "Link to this heading")

================================================================================================================================================================

Plot decision function of a weighted dataset, where the size of points is proportional to its weight.

![plot sgd weighted samples](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear\_model

\# we create 20 points
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
X \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[[np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(10, 2) + \[1, 1\], [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(10, 2)\]
y \= \[1\] \* 10 + \[\-1\] \* 10
sample\_weight \= 100 \* np.abs([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(20))
\# and assign a bigger weight to the last 10 samples
sample\_weight\[:10\] \*= 10

\# plot the weighted data points
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4, 5, 500), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4, 5, 500))
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.scatter(
    X\[:, 0\],
    X\[:, 1\],
    c\=y,
    s\=sample\_weight,
    alpha\=0.9,
    cmap\=plt.cm.bone,
    edgecolor\="black",
)

\# fit the unweighted model
clf \= [linear\_model.SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(alpha\=0.01, max\_iter\=100)
clf.fit(X, y)
Z \= clf.decision\_function([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
Z \= Z.reshape(xx.shape)
no\_weights \= ax.contour(xx, yy, Z, levels\=\[0\], linestyles\=\["solid"\])

\# fit the weighted model
clf \= [linear\_model.SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(alpha\=0.01, max\_iter\=100)
clf.fit(X, y, sample\_weight\=sample\_weight)
Z \= clf.decision\_function([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
Z \= Z.reshape(xx.shape)
samples\_weights \= ax.contour(xx, yy, Z, levels\=\[0\], linestyles\=\["dashed"\])

no\_weights\_handles, \_ \= no\_weights.legend\_elements()
weights\_handles, \_ \= samples\_weights.legend\_elements()
ax.legend(
    \[no\_weights\_handles\[0\], weights\_handles\[0\]\],
    \["no weights", "with weights"\],
    loc\="lower left",
)

ax.set(xticks\=(), yticks\=())
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.068 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_weighted_samples.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_weighted_samples.ipynb)

[`Download Jupyter notebook: plot_sgd_weighted_samples.ipynb`](https://scikit-learn.org/stable/_downloads/6142de78d839661549389d7029cf98b0/plot_sgd_weighted_samples.ipynb)

[`Download Python source code: plot_sgd_weighted_samples.py`](https://scikit-learn.org/stable/_downloads/1fbe96ffa301da6ec5d1c4be786df135/plot_sgd_weighted_samples.py)

[`Download zipped: plot_sgd_weighted_samples.zip`](https://scikit-learn.org/stable/_downloads/da2a64f1701e08e61149af1143e91f0b/plot_sgd_weighted_samples.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_loss_functions_thumb.png)

[SGD: convex loss functions](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html)

SGD: convex loss functions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/1fbe96ffa301da6ec5d1c4be786df135/plot_sgd_weighted_samples.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6142de78d839661549389d7029cf98b0/plot_sgd_weighted_samples.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/da2a64f1701e08e61149af1143e91f0b/plot_sgd_weighted_samples.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_weighted_samples.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_weighted_samples.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)