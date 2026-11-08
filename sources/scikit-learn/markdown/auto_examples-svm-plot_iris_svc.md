[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_iris_svc.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_iris_svc.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_iris_svc.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_iris_svc.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_iris_svc.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_iris_svc.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html#sphx-glr-download-auto-examples-svm-plot-iris-svc-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot different SVM classifiers in the iris dataset[#](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html#plot-different-svm-classifiers-in-the-iris-dataset "Link to this heading")

======================================================================================================================================================================================================

Comparison of different linear SVM classifiers on a 2D projection of the iris dataset. We only consider the first 2 features of this dataset:

*   Sepal length
    
*   Sepal width
    

This example shows how to plot the decision surface and the support vectors for four SVM classifiers with different kernels.

The linear models `LinearSVC()` and `SVC(kernel='linear')` yield slightly different decision boundaries. This can be a consequence of the following differences:

*   `LinearSVC` minimizes the squared hinge loss while `SVC` minimizes the regular hinge loss.
    
*   `LinearSVC` uses the One-vs-All (also known as One-vs-Rest) multiclass reduction while `SVC` uses the One-vs-One multiclass reduction.
    

Both linear models have linear decision boundaries (intersecting hyperplanes) while the non-linear kernel models (polynomial or Gaussian RBF) have more flexible non-linear decision boundaries with shapes that depend on the kind of kernel and its parameters.

Note

While plotting the decision function of classifiers for toy 2D datasets can help get an intuitive understanding of their respective expressive power, be aware that those intuitions don’t always generalize to more realistic high-dimensional problems.

![SVC with linear kernel, LinearSVC (linear kernel), SVC with RBF kernel, SVC with polynomial (degree 3) kernel](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, svm
from sklearn.inspection import DecisionBoundaryDisplay

\# Import some data to play with.
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
\# Take the first two features. We could avoid this by using a two-dim dataset.
X \= iris.data\[:, :2\]
y \= iris.target

\# We create an instance of SVM and fit out data. We do not scale our
\# data since we want to plot the support vectors.
C \= 1.0  \# SVM regularization parameter
models \= (
    [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear", C\=C),
    [svm.LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(C\=C, max\_iter\=10000),
    [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="rbf", gamma\=0.7, C\=C),
    [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="poly", degree\=3, gamma\="auto", C\=C),
)
models \= (clf.fit(X, y) for clf in models)

\# Title for the plots
titles \= (
    "SVC with linear kernel",
    "LinearSVC (linear kernel)",
    "SVC with RBF kernel",
    "SVC with polynomial (degree 3) kernel",
)

\# Set-up 2x2 grid for plotting.
fig, sub \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(wspace\=0.4, hspace\=0.4)

for clf, title, ax in zip(models, titles, sub.flatten()):
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        response\_method\="predict",
        multiclass\_colors\="coolwarm",
        alpha\=0.8,
        ax\=ax,
        xlabel\=iris.feature\_names\[0\],
        ylabel\=iris.feature\_names\[1\],
    )

    \# Plot the support vectors.
    \# For LinearSVC we compute the support vectors from the decision function, see
    \# https://scikit-learn.org/dev/auto\_examples/svm/plot\_linearsvc\_support\_vectors.html
    if hasattr(clf, "support\_"):
        support\_vector\_indices \= clf.support\_
    else:
        decision\_function \= clf.decision\_function(X)
        support\_vector\_indices \= (np.abs(decision\_function) <= 1 + 1e-15).nonzero()\[0\]
    ax.scatter(
        X\[support\_vector\_indices, 0\],
        X\[support\_vector\_indices, 1\],
        c\=y\[support\_vector\_indices\],
        cmap\=plt.cm.coolwarm,
        edgecolors\="k",
    )

    ax.set\_xticks(())
    ax.set\_yticks(())
    ax.set\_title(title)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.225 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_iris_svc.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_iris_svc.ipynb)

[`Download Jupyter notebook: plot_iris_svc.ipynb`](https://scikit-learn.org/stable/_downloads/f84209ea397909becdc84b5de1a5b047/plot_iris_svc.ipynb)

[`Download Python source code: plot_iris_svc.py`](https://scikit-learn.org/stable/_downloads/4186bc506946013950b224b06f827118/plot_iris_svc.py)

[`Download zipped: plot_iris_svc.zip`](https://scikit-learn.org/stable/_downloads/8bafbf478bc8e9392d50f1e4c9ce3c4e/plot_iris_svc.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linearsvc_support_vectors_thumb.png)

[Plot the support vectors in LinearSVC](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html)

Plot the support vectors in LinearSVC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/4186bc506946013950b224b06f827118/plot_iris_svc.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f84209ea397909becdc84b5de1a5b047/plot_iris_svc.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/8bafbf478bc8e9392d50f1e4c9ce3c4e/plot_iris_svc.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_iris_svc.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_iris_svc.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)