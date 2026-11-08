[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_oneclass.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_oneclass.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_oneclass.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_oneclass.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_oneclass.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_oneclass.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html#sphx-glr-download-auto-examples-svm-plot-oneclass-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

One-class SVM with non-linear kernel (RBF)[#](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html#one-class-svm-with-non-linear-kernel-rbf "Link to this heading")

====================================================================================================================================================================================

An example using a one-class SVM for novelty detection.

[One-class SVM](https://scikit-learn.org/stable/modules/svm.html#svm-outlier-detection)
 is an unsupervised algorithm that learns a decision function for novelty detection: classifying new data as similar or different to the training set.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import numpy as np

from sklearn import svm

\# Generate train data
X \= 0.3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(100, 2)
X\_train \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X + 2, X \- 2\]
\# Generate some regular novel observations
X \= 0.3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(20, 2)
X\_test \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X + 2, X \- 2\]
\# Generate some abnormal novel observations
X\_outliers \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(low\=-4, high\=4, size\=(20, 2))

\# fit the model
clf \= [svm.OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
(nu\=0.1, kernel\="rbf", gamma\=0.1)
clf.fit(X\_train)
y\_pred\_train \= clf.predict(X\_train)
y\_pred\_test \= clf.predict(X\_test)
y\_pred\_outliers \= clf.predict(X\_outliers)
n\_error\_train \= y\_pred\_train\[y\_pred\_train \== \-1\].size
n\_error\_test \= y\_pred\_test\[y\_pred\_test \== \-1\].size
n\_error\_outliers \= y\_pred\_outliers\[y\_pred\_outliers \== 1\].size

Copy to clipboard

import matplotlib.font\_manager
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from sklearn.inspection import DecisionBoundaryDisplay

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# generate grid for the boundary display
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, 10), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, 10))
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[xx.reshape(\-1, 1), yy.reshape(\-1, 1)\], axis\=1)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    response\_method\="decision\_function",
    plot\_method\="contourf",
    ax\=ax,
    cmap\="PuBu",
)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    response\_method\="decision\_function",
    plot\_method\="contourf",
    ax\=ax,
    levels\=\[0, 10000\],
    colors\="palevioletred",
)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    response\_method\="decision\_function",
    plot\_method\="contour",
    ax\=ax,
    levels\=\[0\],
    colors\="darkred",
    linewidths\=2,
)

s \= 40
b1 \= ax.scatter(X\_train\[:, 0\], X\_train\[:, 1\], c\="white", s\=s, edgecolors\="k")
b2 \= ax.scatter(X\_test\[:, 0\], X\_test\[:, 1\], c\="blueviolet", s\=s, edgecolors\="k")
c \= ax.scatter(X\_outliers\[:, 0\], X\_outliers\[:, 1\], c\="gold", s\=s, edgecolors\="k")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    \[[mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="darkred"), b1, b2, c\],
    \[\
        "learned frontier",\
        "training observations",\
        "new regular observations",\
        "new abnormal observations",\
    \],
    loc\="upper left",
    prop\=[matplotlib.font\_manager.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(size\=11),
)
ax.set(
    xlabel\=(
        f"error train: {n\_error\_train}/200 ; errors novel regular: {n\_error\_test}/40 ;"
        f" errors novel abnormal: {n\_error\_outliers}/40"
    ),
    title\="Novelty Detection",
    xlim\=(\-5, 5),
    ylim\=(\-5, 5),
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Novelty Detection](https://scikit-learn.org/stable/_images/sphx_glr_plot_oneclass_001.png)

**Total running time of the script:** (0 minutes 0.152 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_oneclass.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_oneclass.ipynb)

[`Download Jupyter notebook: plot_oneclass.ipynb`](https://scikit-learn.org/stable/_downloads/179a84f8da8ce09af733c9a82135ca4d/plot_oneclass.ipynb)

[`Download Python source code: plot_oneclass.py`](https://scikit-learn.org/stable/_downloads/616e8a231ab03301473c9183f6cf03e8/plot_oneclass.py)

[`Download zipped: plot_oneclass.zip`](https://scikit-learn.org/stable/_downloads/20d4c73f80be097989f7cb73d3588767/plot_oneclass.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_thumb.png)

[One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)

One-Class SVM versus One-Class SVM using Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/616e8a231ab03301473c9183f6cf03e8/plot_oneclass.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/179a84f8da8ce09af733c9a82135ca4d/plot_oneclass.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/20d4c73f80be097989f7cb73d3588767/plot_oneclass.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_oneclass.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_oneclass.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)