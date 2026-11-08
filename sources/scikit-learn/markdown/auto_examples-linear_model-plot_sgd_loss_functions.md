[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgd_loss_functions.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgd_loss_functions.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgd_loss_functions.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgd_loss_functions.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgd_loss_functions.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgd_loss_functions.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html#sphx-glr-download-auto-examples-linear-model-plot-sgd-loss-functions-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SGD: convex loss functions[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html#sgd-convex-loss-functions "Link to this heading")

========================================================================================================================================================================

A plot that compares the various convex loss functions supported by [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 .

![plot sgd loss functions](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_loss_functions_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

def modified\_huber\_loss(y\_true, y\_pred):
    z \= y\_pred \* y\_true
    loss \= \-4 \* z
    loss\[z \>= \-1\] \= (1 \- z\[z \>= \-1\]) \*\* 2
    loss\[z \>= 1.0\] \= 0
    return loss

xmin, xmax \= \-4, 4
xx \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(xmin, xmax, 100)
lw \= 2
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[xmin, 0, 0, xmax\], \[1, 1, 0, 0\], color\="gold", lw\=lw, label\="Zero-one loss")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
(xx < 1, 1 \- xx, 0), color\="teal", lw\=lw, label\="Hinge loss")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, \-[np.minimum](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum")
(xx, 0), color\="yellowgreen", lw\=lw, label\="Perceptron loss")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, [np.log2](https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2 "numpy.log2")
(1 + [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-xx)), color\="cornflowerblue", lw\=lw, label\="Log loss")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    xx,
    [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
(xx < 1, 1 \- xx, 0) \*\* 2,
    color\="orange",
    lw\=lw,
    label\="Squared hinge loss",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    xx,
    modified\_huber\_loss(xx, 1),
    color\="darkorchid",
    lw\=lw,
    linestyle\="--",
    label\="Modified Huber loss",
)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
((0, 8))
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(r"Decision function $f(x)$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$L(y=1, f(x))$")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.118 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_loss_functions.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_loss_functions.ipynb)

[`Download Jupyter notebook: plot_sgd_loss_functions.ipynb`](https://scikit-learn.org/stable/_downloads/bad2c14c5cfbd2a6e2c7d563be123e11/plot_sgd_loss_functions.ipynb)

[`Download Python source code: plot_sgd_loss_functions.py`](https://scikit-learn.org/stable/_downloads/53882b11cf2430d2dadc527ba6c587d7/plot_sgd_loss_functions.py)

[`Download zipped: plot_sgd_loss_functions.zip`](https://scikit-learn.org/stable/_downloads/ee702db469ee8b432e74db09a687ae1d/plot_sgd_loss_functions.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/53882b11cf2430d2dadc527ba6c587d7/plot_sgd_loss_functions.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/bad2c14c5cfbd2a6e2c7d563be123e11/plot_sgd_loss_functions.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/ee702db469ee8b432e74db09a687ae1d/plot_sgd_loss_functions.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_loss_functions.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_loss_functions.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)