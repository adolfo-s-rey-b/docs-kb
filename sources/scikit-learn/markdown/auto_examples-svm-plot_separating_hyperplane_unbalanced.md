[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#sphx-glr-download-auto-examples-svm-plot-separating-hyperplane-unbalanced-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM: Separating hyperplane for unbalanced classes[#](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#svm-separating-hyperplane-for-unbalanced-classes "Link to this heading")

===========================================================================================================================================================================================================================

Find the optimal separating hyperplane using an SVC for classes that are unbalanced.

We first find the separating plane with a plain SVC and then plot (dashed) the separating hyperplane with automatically correction for unbalanced classes.

Note

This example will also work by replacing `SVC(kernel="linear")` with `SGDClassifier(loss="hinge")`. Setting the `loss` parameter of the [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 equal to `hinge` will yield behaviour such as that of an SVC with a linear kernel.

For example try instead of the `SVC`:

clf \= SGDClassifier(n\_iter\=100, alpha\=0.01)

Copy to clipboard

![plot separating hyperplane unbalanced](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.lines as mlines
import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.inspection import DecisionBoundaryDisplay

\# we create two clusters of random points
n\_samples\_1 \= 1000
n\_samples\_2 \= 100
centers \= \[\[0.0, 0.0\], \[2.0, 2.0\]\]
clusters\_std \= \[1.5, 0.5\]
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=\[n\_samples\_1, n\_samples\_2\],
    centers\=centers,
    cluster\_std\=clusters\_std,
    random\_state\=0,
    shuffle\=False,
)

\# fit the model and get the separating hyperplane
clf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear", C\=1.0)
clf.fit(X, y)

\# fit the model and get the separating hyperplane using weighted classes
wclf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear", class\_weight\={1: 10})
wclf.fit(X, y)

\# plot the samples
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y, cmap\=plt.cm.Paired, edgecolors\="k")

\# plot the decision functions for both classifiers
ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    plot\_method\="contour",
    colors\="k",
    levels\=\[0\],
    alpha\=0.5,
    linestyles\=\["-"\],
    ax\=ax,
)

\# plot decision boundary and margins for weighted classes
wdisp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    wclf,
    X,
    plot\_method\="contour",
    colors\="r",
    levels\=\[0\],
    alpha\=0.5,
    linestyles\=\["-"\],
    ax\=ax,
)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    \[\
        [mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="k", label\="non weighted"),\
        [mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="r", label\="weighted"),\
    \],
    \["non weighted", "weighted"\],
    loc\="upper right",
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.182 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_separating_hyperplane_unbalanced.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_separating_hyperplane_unbalanced.ipynb)

[`Download Jupyter notebook: plot_separating_hyperplane_unbalanced.ipynb`](https://scikit-learn.org/stable/_downloads/d22cc4079af5678a112fa5aa77700680/plot_separating_hyperplane_unbalanced.ipynb)

[`Download Python source code: plot_separating_hyperplane_unbalanced.py`](https://scikit-learn.org/stable/_downloads/ff58cea6f60833cdaaaa13c98576eac5/plot_separating_hyperplane_unbalanced.py)

[`Download zipped: plot_separating_hyperplane_unbalanced.zip`](https://scikit-learn.org/stable/_downloads/d3bae9b99abb4dfdba5f7c8588be8746/plot_separating_hyperplane_unbalanced.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_thumb.png)

[SGD: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

SGD: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_thumb.png)

[SVM Margins Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)

SVM Margins Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/ff58cea6f60833cdaaaa13c98576eac5/plot_separating_hyperplane_unbalanced.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/d22cc4079af5678a112fa5aa77700680/plot_separating_hyperplane_unbalanced.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d3bae9b99abb4dfdba5f7c8588be8746/plot_separating_hyperplane_unbalanced.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_separating_hyperplane_unbalanced.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_separating_hyperplane_unbalanced.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)