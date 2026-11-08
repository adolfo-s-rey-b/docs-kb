[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_separating_hyperplane.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_separating_hyperplane.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_separating_hyperplane.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_separating_hyperplane.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_separating_hyperplane.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_separating_hyperplane.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html#sphx-glr-download-auto-examples-svm-plot-separating-hyperplane-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM: Maximum margin separating hyperplane[#](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html#svm-maximum-margin-separating-hyperplane "Link to this heading")

================================================================================================================================================================================================

Plot the maximum margin separating hyperplane within a two-class separable dataset using a Support Vector Machine classifier with linear kernel.

![plot separating hyperplane](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.inspection import DecisionBoundaryDisplay

\# we create 40 separable points
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=40, centers\=2, random\_state\=6)

\# fit the model, don't regularize for illustration purposes
clf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear", C\=1000)
clf.fit(X, y)

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y, s\=30, cmap\=plt.cm.Paired)

\# plot the decision function
ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    plot\_method\="contour",
    colors\="k",
    levels\=\[\-1, 0, 1\],
    alpha\=0.5,
    linestyles\=\["--", "-", "--"\],
    ax\=ax,
)
\# plot support vectors
ax.scatter(
    clf.support\_vectors\_\[:, 0\],
    clf.support\_vectors\_\[:, 1\],
    s\=100,
    linewidth\=1,
    facecolors\="none",
    edgecolors\="k",
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.061 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_separating_hyperplane.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_separating_hyperplane.ipynb)

[`Download Jupyter notebook: plot_separating_hyperplane.ipynb`](https://scikit-learn.org/stable/_downloads/e6a6423db5b5d652b6a6deafc8ca7ee0/plot_separating_hyperplane.ipynb)

[`Download Python source code: plot_separating_hyperplane.py`](https://scikit-learn.org/stable/_downloads/438bb54b7ea4cc4c565d0dbe5647119f/plot_separating_hyperplane.py)

[`Download zipped: plot_separating_hyperplane.zip`](https://scikit-learn.org/stable/_downloads/0afbdae4d5c21dfbf1e7f98e95e973c5/plot_separating_hyperplane.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_thumb.png)

[SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

SVM: Separating hyperplane for unbalanced classes

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_thumb.png)

[SVM Margins Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)

SVM Margins Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linearsvc_support_vectors_thumb.png)

[Plot the support vectors in LinearSVC](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html)

Plot the support vectors in LinearSVC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_thumb.png)

[SGD: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

SGD: Maximum margin separating hyperplane

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/438bb54b7ea4cc4c565d0dbe5647119f/plot_separating_hyperplane.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e6a6423db5b5d652b6a6deafc8ca7ee0/plot_separating_hyperplane.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0afbdae4d5c21dfbf1e7f98e95e973c5/plot_separating_hyperplane.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_separating_hyperplane.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_separating_hyperplane.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)