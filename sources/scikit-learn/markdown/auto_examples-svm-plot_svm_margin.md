[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_margin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_svm_margin.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_svm_margin.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_svm_margin.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_svm_margin.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_svm_margin.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html#sphx-glr-download-auto-examples-svm-plot-svm-margin-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM Margins Example[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html#svm-margins-example "Link to this heading")

==========================================================================================================================================

The plots below illustrate the effect the parameter `C` has on the separation line. A large value of `C` basically tells our model that we do not have that much faith in our data’s distribution, and will only consider points close to line of separation.

A small value of `C` includes more/all the observations, allowing the margins to be calculated using all the data in the area.

*   ![plot svm margin](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_001.png)
*   ![plot svm margin](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_002.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay

\# we create 40 separable points
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
X \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[[np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(20, 2) \- \[2, 2\], [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(20, 2) + \[2, 2\]\]
Y \= \[0\] \* 20 + \[1\] \* 20

\# figure number
fignum \= 1

\# fit the model
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear", C\=penalty)
    clf.fit(X, Y)

    \# get the separating hyperplane
    w \= clf.coef\_\[0\]
    a \= \-w\[0\] / w\[1\]
    xx \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5)
    yy \= a \* xx \- (clf.intercept\_\[0\]) / w\[1\]

    \# plot the parallels to the separating hyperplane that pass through the
    \# support vectors (margin away from hyperplane in direction
    \# perpendicular to hyperplane). This is sqrt(1+a^2) away vertically in
    \# 2-d.
    margin \= 1 / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
([np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(clf.coef\_\*\*2))
    yy\_down \= yy \- [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(1 + a\*\*2) \* margin
    yy\_up \= yy + [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(1 + a\*\*2) \* margin

    \# plot the line, the points, and the nearest vectors to the plane
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(fignum, figsize\=(4, 3))
    [plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf")
()
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, yy, "k-")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, yy\_down, "k--")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, yy\_up, "k--")

    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        clf.support\_vectors\_\[:, 0\],
        clf.support\_vectors\_\[:, 1\],
        s\=80,
        facecolors\="none",
        zorder\=10,
        edgecolors\="k",
    )
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[:, 0\], X\[:, 1\], c\=Y, zorder\=10, cmap\=[plt.get\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
("RdBu"), edgecolors\="k"
    )

    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
    x\_min \= \-4.8
    x\_max \= 4.1
    y\_min \= \-5
    y\_max \= 5

    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        ax\=[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
(),
        cmap\="RdBu",
        alpha\=0.5,
        response\_method\="decision\_function",
    )

    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(x\_min, x\_max)
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(y\_min, y\_max)

    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    fignum \= fignum + 1

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.059 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_margin.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_margin.ipynb)

[`Download Jupyter notebook: plot_svm_margin.ipynb`](https://scikit-learn.org/stable/_downloads/e5984993ae4c01e36276dcfed2bf0838/plot_svm_margin.ipynb)

[`Download Python source code: plot_svm_margin.py`](https://scikit-learn.org/stable/_downloads/a6621d4718b448229cd4e8e18fdbe4c6/plot_svm_margin.py)

[`Download zipped: plot_svm_margin.zip`](https://scikit-learn.org/stable/_downloads/03c018a16384c69f3a89e473650d57ee/plot_svm_margin.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_thumb.png)

[SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

SVM: Separating hyperplane for unbalanced classes

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/a6621d4718b448229cd4e8e18fdbe4c6/plot_svm_margin.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e5984993ae4c01e36276dcfed2bf0838/plot_svm_margin.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/03c018a16384c69f3a89e473650d57ee/plot_svm_margin.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_margin.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_margin.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)