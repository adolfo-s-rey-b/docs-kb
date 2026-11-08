[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgd_penalties.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgd_penalties.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgd_penalties.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgd_penalties.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgd_penalties.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgd_penalties.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html#sphx-glr-download-auto-examples-linear-model-plot-sgd-penalties-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SGD: Penalties[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html#sgd-penalties "Link to this heading")

===========================================================================================================================================

Contours of where the penalty is equal to 1 for the three penalties L1, L2 and elastic-net.

All of the above are supported by [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 and [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
.

![plot sgd penalties](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_penalties_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

l1\_color \= "navy"
l2\_color \= "c"
elastic\_net\_color \= "darkorange"

line \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1.5, 1.5, 1001)
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(line, line)

l2 \= xx\*\*2 + yy\*\*2
l1 \= np.abs(xx) + np.abs(yy)
rho \= 0.5
elastic\_net \= rho \* l1 + (1 \- rho) \* l2

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10), dpi\=100)
ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()

elastic\_net\_contour \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(
    xx, yy, elastic\_net, levels\=\[1\], colors\=elastic\_net\_color
)
l2\_contour \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(xx, yy, l2, levels\=\[1\], colors\=l2\_color)
l1\_contour \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(xx, yy, l1, levels\=\[1\], colors\=l1\_color)
ax.set\_aspect("equal")
ax.spines\["left"\].set\_position("center")
ax.spines\["right"\].set\_color("none")
ax.spines\["bottom"\].set\_position("center")
ax.spines\["top"\].set\_color("none")

[plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(
    elastic\_net\_contour,
    inline\=1,
    fontsize\=18,
    fmt\={1.0: "elastic-net"},
    manual\=\[(\-1, \-1)\],
)
[plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(l2\_contour, inline\=1, fontsize\=18, fmt\={1.0: "L2"}, manual\=\[(\-1, \-1)\])
[plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(l1\_contour, inline\=1, fontsize\=18, fmt\={1.0: "L1"}, manual\=\[(\-1, \-1)\])

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.245 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_penalties.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_penalties.ipynb)

[`Download Jupyter notebook: plot_sgd_penalties.ipynb`](https://scikit-learn.org/stable/_downloads/061854726c268bcdae5cd1c330cf8c75/plot_sgd_penalties.ipynb)

[`Download Python source code: plot_sgd_penalties.py`](https://scikit-learn.org/stable/_downloads/8f25e8f3f3c619cc58b57d51b2029f29/plot_sgd_penalties.py)

[`Download zipped: plot_sgd_penalties.zip`](https://scikit-learn.org/stable/_downloads/eb2eb8ac4033d060dc6864d179f8a96e/plot_sgd_penalties.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/8f25e8f3f3c619cc58b57d51b2029f29/plot_sgd_penalties.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/061854726c268bcdae5cd1c330cf8c75/plot_sgd_penalties.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/eb2eb8ac4033d060dc6864d179f8a96e/plot_sgd_penalties.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_penalties.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_penalties.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)