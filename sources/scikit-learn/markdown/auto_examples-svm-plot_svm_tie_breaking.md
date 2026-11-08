[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_tie_breaking.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_svm_tie_breaking.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_svm_tie_breaking.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_svm_tie_breaking.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_svm_tie_breaking.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_svm_tie_breaking.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html#sphx-glr-download-auto-examples-svm-plot-svm-tie-breaking-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM Tie Breaking Example[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html#svm-tie-breaking-example "Link to this heading")

==========================================================================================================================================================

Tie breaking is costly if `decision_function_shape='ovr'`, and therefore it is not enabled by default. This example illustrates the effect of the `break_ties` parameter for a multiclass classification problem and `decision_function_shape='ovr'`.

The two plots differ only in the area in the middle where the classes are tied. If `break_ties=False`, all input in that area would be classified as one class, whereas if `break_ties=True`, the tie-breaking mechanism will create a non-convex decision boundary in that area.

![break_ties = False, break_ties = True](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_tie_breaking_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(random\_state\=27)

fig, sub \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(5, 8))
titles \= ("break\_ties = False", "break\_ties = True")

for break\_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(
        kernel\="linear", C\=1, break\_ties\=break\_ties, decision\_function\_shape\="ovr"
    ).fit(X, y)

    xlim \= \[X\[:, 0\].min(), X\[:, 0\].max()\]
    ylim \= \[X\[:, 1\].min(), X\[:, 1\].max()\]

    xs \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(xlim\[0\], xlim\[1\], 1000)
    ys \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(ylim\[0\], ylim\[1\], 1000)
    xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(xs, ys)

    pred \= svm.predict([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])

    colors \= \[plt.cm.Accent(i) for i in \[0, 4, 7\]\]

    points \= ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, cmap\="Accent")
    classes \= \[(0, 1), (0, 2), (1, 2)\]
    line \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(X\[:, 1\].min() \- 5, X\[:, 1\].max() + 5)
    ax.imshow(
        pred.reshape(xx.shape),
        cmap\="Accent",
        alpha\=0.2,
        extent\=(xlim\[0\], xlim\[1\], ylim\[1\], ylim\[0\]),
    )

    for coef, intercept, col in zip(svm.coef\_, svm.intercept\_, classes):
        line2 \= \-(line \* coef\[1\] + intercept) / coef\[0\]
        ax.plot(line2, line, "-", c\=colors\[col\[0\]\])
        ax.plot(line2, line, "--", c\=colors\[col\[1\]\])
    ax.set\_xlim(xlim)
    ax.set\_ylim(ylim)
    ax.set\_title(title)
    ax.set\_aspect("equal")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.095 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_tie_breaking.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_tie_breaking.ipynb)

[`Download Jupyter notebook: plot_svm_tie_breaking.ipynb`](https://scikit-learn.org/stable/_downloads/358cfc6f7881b63fd4067f3b13ced9ab/plot_svm_tie_breaking.ipynb)

[`Download Python source code: plot_svm_tie_breaking.py`](https://scikit-learn.org/stable/_downloads/87c535e0896b225a19d2142c6f7c6744/plot_svm_tie_breaking.py)

[`Download zipped: plot_svm_tie_breaking.zip`](https://scikit-learn.org/stable/_downloads/c1445b023cf96a45dff2bda6de47c0ef/plot_svm_tie_breaking.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_thumb.png)

[SVM Margins Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)

SVM Margins Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/87c535e0896b225a19d2142c6f7c6744/plot_svm_tie_breaking.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/358cfc6f7881b63fd4067f3b13ced9ab/plot_svm_tie_breaking.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c1445b023cf96a45dff2bda6de47c0ef/plot_svm_tie_breaking.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_tie_breaking.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_tie_breaking.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)