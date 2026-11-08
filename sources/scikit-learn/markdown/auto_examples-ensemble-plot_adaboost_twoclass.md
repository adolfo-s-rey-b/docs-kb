[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_adaboost_twoclass.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_adaboost_twoclass.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_adaboost_twoclass.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_adaboost_twoclass.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_adaboost_twoclass.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_adaboost_twoclass.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html#sphx-glr-download-auto-examples-ensemble-plot-adaboost-twoclass-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Two-class AdaBoost[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html#two-class-adaboost "Link to this heading")

====================================================================================================================================================

This example fits an AdaBoosted decision stump on a non-linearly separable classification dataset composed of two “Gaussian quantiles” clusters (see [`sklearn.datasets.make_gaussian_quantiles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")
) and plots the decision boundary and decision scores. The distributions of decision scores are shown separately for samples of class A and B. The predicted class label for each sample is determined by the sign of the decision score. Samples with decision scores greater than zero are classified as B, and are otherwise classified as A. The magnitude of a decision score determines the degree of likeness with the predicted class label. Additionally, a new dataset could be constructed containing a desired purity of class B, for example, by only selecting samples with a decision score above some value.

![Decision Boundary, Decision Scores](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_gaussian\_quantiles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")
from sklearn.ensemble import [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

\# Construct dataset
X1, y1 \= [make\_gaussian\_quantiles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")
(
    cov\=2.0, n\_samples\=200, n\_features\=2, n\_classes\=2, random\_state\=1
)
X2, y2 \= [make\_gaussian\_quantiles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")
(
    mean\=(3, 3), cov\=1.5, n\_samples\=300, n\_features\=2, n\_classes\=2, random\_state\=1
)
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((X1, X2))
y \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((y1, \-y2 + 1))

\# Create and fit an AdaBoosted decision tree
bdt \= [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
([DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(max\_depth\=1), n\_estimators\=200)
bdt.fit(X, y)

plot\_colors \= "br"
plot\_step \= 0.02
class\_names \= "AB"

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 5))

\# Plot the decision boundaries
ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(121)
disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    bdt,
    X,
    cmap\=plt.cm.Paired,
    response\_method\="predict",
    ax\=ax,
    xlabel\="x",
    ylabel\="y",
)
x\_min, x\_max \= disp.xx0.min(), disp.xx0.max()
y\_min, y\_max \= disp.xx1.min(), disp.xx1.max()
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Plot the training points
for i, n, c in zip(range(2), class\_names, plot\_colors):
    idx \= (y \== i).nonzero()
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[idx, 0\],
        X\[idx, 1\],
        c\=c,
        s\=20,
        edgecolor\="k",
        label\="Class %s" % n,
    )
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(x\_min, x\_max)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(y\_min, y\_max)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Decision Boundary")

\# Plot the two-class decision scores
twoclass\_output \= bdt.decision\_function(X)
plot\_range \= (twoclass\_output.min(), twoclass\_output.max())
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(122)
for i, n, c in zip(range(2), class\_names, plot\_colors):
    [plt.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
(
        twoclass\_output\[y \== i\],
        bins\=10,
        range\=plot\_range,
        facecolor\=c,
        label\="Class %s" % n,
        alpha\=0.5,
        edgecolor\="k",
    )
x1, x2, y1, y2 \= [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
()
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
((x1, x2, y1, y2 \* 1.2))
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Samples")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Score")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Decision Scores")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(wspace\=0.35)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.672 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_adaboost_twoclass.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_adaboost_twoclass.ipynb)

[`Download Jupyter notebook: plot_adaboost_twoclass.ipynb`](https://scikit-learn.org/stable/_downloads/c3a0ceabf65f8c894895af414e685ee9/plot_adaboost_twoclass.ipynb)

[`Download Python source code: plot_adaboost_twoclass.py`](https://scikit-learn.org/stable/_downloads/f0440afe8f6b99019c4fd181a9f57c59/plot_adaboost_twoclass.py)

[`Download zipped: plot_adaboost_twoclass.zip`](https://scikit-learn.org/stable/_downloads/c6bab6fd031af67403ba45efde42d16c/plot_adaboost_twoclass.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_thumb.png)

[SGD: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

SGD: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_isoprobability_thumb.png)

[Iso-probability lines for Gaussian Processes classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html)

Iso-probability lines for Gaussian Processes classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)

[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Classifier comparison

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/f0440afe8f6b99019c4fd181a9f57c59/plot_adaboost_twoclass.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c3a0ceabf65f8c894895af414e685ee9/plot_adaboost_twoclass.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c6bab6fd031af67403ba45efde42d16c/plot_adaboost_twoclass.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_adaboost_twoclass.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_adaboost_twoclass.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)