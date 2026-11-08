[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_linearsvc_support_vectors.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_linearsvc_support_vectors.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_linearsvc_support_vectors.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_linearsvc_support_vectors.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_linearsvc_support_vectors.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_linearsvc_support_vectors.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html#sphx-glr-download-auto-examples-svm-plot-linearsvc-support-vectors-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot the support vectors in LinearSVC[#](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html#plot-the-support-vectors-in-linearsvc "Link to this heading")

=============================================================================================================================================================================================

Unlike SVC (based on LIBSVM), LinearSVC (based on LIBLINEAR) does not provide the support vectors. This example demonstrates how to obtain the support vectors in LinearSVC.

![C=1, C=100](https://scikit-learn.org/stable/_images/sphx_glr_plot_linearsvc_support_vectors_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=40, centers\=2, random\_state\=0)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 5))
for i, C in enumerate(\[1, 100\]):
    \# "hinge" is the standard SVM loss
    clf \= [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(C\=C, loss\="hinge", random\_state\=42).fit(X, y)
    \# obtain the support vectors through the decision function
    decision\_function \= clf.decision\_function(X)
    \# we can also calculate the decision function manually
    \# decision\_function = np.dot(X, clf.coef\_\[0\]) + clf.intercept\_\[0\]
    \# The support vectors are the samples that lie within the margin
    \# boundaries, whose size is conventionally constrained to 1
    support\_vector\_indices \= (np.abs(decision\_function) <= 1 + 1e-15).nonzero()\[0\]
    support\_vectors \= X\[support\_vector\_indices\]

    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, i + 1)
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y, s\=30, cmap\=plt.cm.Paired)
    ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        ax\=ax,
        grid\_resolution\=50,
        plot\_method\="contour",
        colors\="k",
        levels\=\[\-1, 0, 1\],
        alpha\=0.5,
        linestyles\=\["--", "-", "--"\],
    )
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        support\_vectors\[:, 0\],
        support\_vectors\[:, 1\],
        s\=100,
        linewidth\=1,
        facecolors\="none",
        edgecolors\="k",
    )
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("C=" + str(C))
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.156 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_linearsvc_support_vectors.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_linearsvc_support_vectors.ipynb)

[`Download Jupyter notebook: plot_linearsvc_support_vectors.ipynb`](https://scikit-learn.org/stable/_downloads/12a392e818ac5fa47dd91461855f3f77/plot_linearsvc_support_vectors.ipynb)

[`Download Python source code: plot_linearsvc_support_vectors.py`](https://scikit-learn.org/stable/_downloads/036b9372e2e7802453cbb994da7a6786/plot_linearsvc_support_vectors.py)

[`Download zipped: plot_linearsvc_support_vectors.zip`](https://scikit-learn.org/stable/_downloads/aba5d73e169336038beb51608b748211/plot_linearsvc_support_vectors.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_thumb.png)

[SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

SVM: Separating hyperplane for unbalanced classes

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/036b9372e2e7802453cbb994da7a6786/plot_linearsvc_support_vectors.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/12a392e818ac5fa47dd91461855f3f77/plot_linearsvc_support_vectors.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/aba5d73e169336038beb51608b748211/plot_linearsvc_support_vectors.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_linearsvc_support_vectors.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_linearsvc_support_vectors.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)