[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html#sphx-glr-download-auto-examples-linear-model-plot-sgdocsvm-vs-ocsvm-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

One-Class SVM versus One-Class SVM using Stochastic Gradient Descent[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html#one-class-svm-versus-one-class-svm-using-stochastic-gradient-descent "Link to this heading")

============================================================================================================================================================================================================================================================

This example shows how to approximate the solution of [`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 in the case of an RBF kernel with [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
, a Stochastic Gradient Descent (SGD) version of the One-Class SVM. A kernel approximation is first used in order to apply [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 which implements a linear One-Class SVM using SGD.

Note that [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 scales linearly with the number of samples whereas the complexity of a kernelized [`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 is at best quadratic with respect to the number of samples. It is not the purpose of this example to illustrate the benefits of such an approximation in terms of computation time but rather to show that we obtain similar results on a toy dataset.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
from sklearn.linear\_model import [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.svm import [OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")

font \= {"weight": "normal", "size": 15}

[matplotlib.rc](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc "matplotlib.rc")
("font", \*\*font)

random\_state \= 42
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(random\_state)

\# Generate train data
X \= 0.3 \* rng.randn(500, 2)
X\_train \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X + 2, X \- 2\]
\# Generate some regular novel observations
X \= 0.3 \* rng.randn(20, 2)
X\_test \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X + 2, X \- 2\]
\# Generate some abnormal novel observations
X\_outliers \= rng.uniform(low\=-4, high\=4, size\=(20, 2))

\# OCSVM hyperparameters
nu \= 0.05
gamma \= 2.0

\# Fit the One-Class SVM
clf \= [OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
(gamma\=gamma, kernel\="rbf", nu\=nu)
clf.fit(X\_train)
y\_pred\_train \= clf.predict(X\_train)
y\_pred\_test \= clf.predict(X\_test)
y\_pred\_outliers \= clf.predict(X\_outliers)
n\_error\_train \= y\_pred\_train\[y\_pred\_train \== \-1\].size
n\_error\_test \= y\_pred\_test\[y\_pred\_test \== \-1\].size
n\_error\_outliers \= y\_pred\_outliers\[y\_pred\_outliers \== 1\].size

\# Fit the One-Class SVM using a kernel approximation and SGD
transform \= [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
(gamma\=gamma, random\_state\=random\_state)
clf\_sgd \= [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
(
    nu\=nu, shuffle\=True, fit\_intercept\=True, random\_state\=random\_state, tol\=1e-4
)
pipe\_sgd \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(transform, clf\_sgd)
pipe\_sgd.fit(X\_train)
y\_pred\_train\_sgd \= pipe\_sgd.predict(X\_train)
y\_pred\_test\_sgd \= pipe\_sgd.predict(X\_test)
y\_pred\_outliers\_sgd \= pipe\_sgd.predict(X\_outliers)
n\_error\_train\_sgd \= y\_pred\_train\_sgd\[y\_pred\_train\_sgd \== \-1\].size
n\_error\_test\_sgd \= y\_pred\_test\_sgd\[y\_pred\_test\_sgd \== \-1\].size
n\_error\_outliers\_sgd \= y\_pred\_outliers\_sgd\[y\_pred\_outliers\_sgd \== 1\].size

Copy to clipboard

from sklearn.inspection import DecisionBoundaryDisplay

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(9, 6))

xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4.5, 4.5, 50), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4.5, 4.5, 50))
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[xx.ravel().reshape(\-1, 1), yy.ravel().reshape(\-1, 1)\], axis\=1)
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
    plot\_method\="contour",
    ax\=ax,
    linewidths\=2,
    colors\="darkred",
    levels\=\[0\],
)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    response\_method\="decision\_function",
    plot\_method\="contourf",
    ax\=ax,
    colors\="palevioletred",
    levels\=\[0, clf.decision\_function(X).max()\],
)

s \= 20
b1 \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\[:, 0\], X\_train\[:, 1\], c\="white", s\=s, edgecolors\="k")
b2 \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_test\[:, 0\], X\_test\[:, 1\], c\="blueviolet", s\=s, edgecolors\="k")
c \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_outliers\[:, 0\], X\_outliers\[:, 1\], c\="gold", s\=s, edgecolors\="k")

ax.set(
    title\="One-Class SVM",
    xlim\=(\-4.5, 4.5),
    ylim\=(\-4.5, 4.5),
    xlabel\=(
        f"error train: {n\_error\_train}/{X\_train.shape\[0\]}; "
        f"errors novel regular: {n\_error\_test}/{X\_test.shape\[0\]}; "
        f"errors novel abnormal: {n\_error\_outliers}/{X\_outliers.shape\[0\]}"
    ),
)
\_ \= ax.legend(
    \[[mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="darkred", label\="learned frontier"), b1, b2, c\],
    \[\
        "learned frontier",\
        "training observations",\
        "new regular observations",\
        "new abnormal observations",\
    \],
    loc\="upper left",
)

Copy to clipboard

![One-Class SVM](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_001.png)

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(9, 6))

xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4.5, 4.5, 50), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4.5, 4.5, 50))
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[xx.ravel().reshape(\-1, 1), yy.ravel().reshape(\-1, 1)\], axis\=1)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    pipe\_sgd,
    X,
    response\_method\="decision\_function",
    plot\_method\="contourf",
    ax\=ax,
    cmap\="PuBu",
)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    pipe\_sgd,
    X,
    response\_method\="decision\_function",
    plot\_method\="contour",
    ax\=ax,
    linewidths\=2,
    colors\="darkred",
    levels\=\[0\],
)
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    pipe\_sgd,
    X,
    response\_method\="decision\_function",
    plot\_method\="contourf",
    ax\=ax,
    colors\="palevioletred",
    levels\=\[0, pipe\_sgd.decision\_function(X).max()\],
)

s \= 20
b1 \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\[:, 0\], X\_train\[:, 1\], c\="white", s\=s, edgecolors\="k")
b2 \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_test\[:, 0\], X\_test\[:, 1\], c\="blueviolet", s\=s, edgecolors\="k")
c \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_outliers\[:, 0\], X\_outliers\[:, 1\], c\="gold", s\=s, edgecolors\="k")

ax.set(
    title\="Online One-Class SVM",
    xlim\=(\-4.5, 4.5),
    ylim\=(\-4.5, 4.5),
    xlabel\=(
        f"error train: {n\_error\_train\_sgd}/{X\_train.shape\[0\]}; "
        f"errors novel regular: {n\_error\_test\_sgd}/{X\_test.shape\[0\]}; "
        f"errors novel abnormal: {n\_error\_outliers\_sgd}/{X\_outliers.shape\[0\]}"
    ),
)
ax.legend(
    \[[mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="darkred", label\="learned frontier"), b1, b2, c\],
    \[\
        "learned frontier",\
        "training observations",\
        "new regular observations",\
        "new abnormal observations",\
    \],
    loc\="upper left",
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Online One-Class SVM](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_002.png)

**Total running time of the script:** (0 minutes 0.484 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.ipynb)

[`Download Jupyter notebook: plot_sgdocsvm_vs_ocsvm.ipynb`](https://scikit-learn.org/stable/_downloads/69531acbb2cc9d87ef86f75c8eaba68d/plot_sgdocsvm_vs_ocsvm.ipynb)

[`Download Python source code: plot_sgdocsvm_vs_ocsvm.py`](https://scikit-learn.org/stable/_downloads/3692f2475b52d40c3632818c00ff5b52/plot_sgdocsvm_vs_ocsvm.py)

[`Download zipped: plot_sgdocsvm_vs_ocsvm.zip`](https://scikit-learn.org/stable/_downloads/c8d6400be1e93975c77a6f188d6c9cd0/plot_sgdocsvm_vs_ocsvm.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_oneclass_thumb.png)

[One-class SVM with non-linear kernel (RBF)](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html)

One-class SVM with non-linear kernel (RBF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_thumb.png)

[SVM Margins Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)

SVM Margins Example

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/3692f2475b52d40c3632818c00ff5b52/plot_sgdocsvm_vs_ocsvm.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/69531acbb2cc9d87ef86f75c8eaba68d/plot_sgdocsvm_vs_ocsvm.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c8d6400be1e93975c77a6f188d6c9cd0/plot_sgdocsvm_vs_ocsvm.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)