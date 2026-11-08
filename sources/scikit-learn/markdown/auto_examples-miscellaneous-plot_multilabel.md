[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_multilabel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_multilabel.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_multilabel.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_multilabel.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_multilabel.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_multilabel.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html#sphx-glr-download-auto-examples-miscellaneous-plot-multilabel-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Multilabel classification[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html#multilabel-classification "Link to this heading")

================================================================================================================================================================

This example simulates a multi-label document classification problem. The dataset is generated randomly based on the following process:

*   pick the number of labels: n ~ Poisson(n\_labels)
    
*   n times, choose a class c: c ~ Multinomial(theta)
    
*   pick the document length: k ~ Poisson(length)
    
*   k times, choose a word: w ~ Multinomial(theta\_c)
    

In the above process, rejection sampling is used to make sure that n is more than 2, and that the document length is never zero. Likewise, we reject classes which have already been chosen. The documents that are assigned to both classes are plotted surrounded by two colored circles.

The classification is performed by projecting to the first two principal components found by PCA and CCA for visualisation purposes, followed by using the [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 metaclassifier using two SVCs with linear kernels to learn a discriminative model for each class. Note that PCA is used to perform an unsupervised dimensionality reduction, while CCA is used to perform a supervised one.

Note: in the plot, “unlabeled samples” does not mean that we don’t know the labels (as in semi-supervised learning) but that the samples simply do _not_ have a label.

![With unlabeled samples + CCA, With unlabeled samples + PCA, Without unlabeled samples + CCA, Without unlabeled samples + PCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cross\_decomposition import [CCA](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
from sklearn.datasets import [make\_multilabel\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.multiclass import [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

def plot\_hyperplane(clf, min\_x, max\_x, linestyle, label):
    \# get the separating hyperplane
    w \= clf.coef\_\[0\]
    a \= \-w\[0\] / w\[1\]
    xx \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(min\_x \- 5, max\_x + 5)  \# make sure the line is long enough
    yy \= a \* xx \- (clf.intercept\_\[0\]) / w\[1\]
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xx, yy, linestyle, label\=label)

def plot\_subfigure(X, Y, subplot, title, transform):
    if transform \== "pca":
        X \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2).fit\_transform(X)
    elif transform \== "cca":
        X \= [CCA](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
(n\_components\=2).fit(X, Y).transform(X)
    else:
        raise ValueError

    min\_x \= [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(X\[:, 0\])
    max\_x \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(X\[:, 0\])

    min\_y \= [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(X\[:, 1\])
    max\_y \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(X\[:, 1\])

    classif \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
([SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear"))
    classif.fit(X, Y)

    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, subplot)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title)

    zero\_class \= (Y\[:, 0\]).nonzero()
    one\_class \= (Y\[:, 1\]).nonzero()
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], s\=40, c\="gray", edgecolors\=(0, 0, 0))
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[zero\_class, 0\],
        X\[zero\_class, 1\],
        s\=160,
        edgecolors\="b",
        facecolors\="none",
        linewidths\=2,
        label\="Class 1",
    )
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[one\_class, 0\],
        X\[one\_class, 1\],
        s\=80,
        edgecolors\="orange",
        facecolors\="none",
        linewidths\=2,
        label\="Class 2",
    )

    plot\_hyperplane(
        classif.estimators\_\[0\], min\_x, max\_x, "k--", "Boundary\\nfor class 1"
    )
    plot\_hyperplane(
        classif.estimators\_\[1\], min\_x, max\_x, "k-.", "Boundary\\nfor class 2"
    )
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())

    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(min\_x \- 0.5 \* max\_x, max\_x + 0.5 \* max\_x)
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(min\_y \- 0.5 \* max\_y, max\_y + 0.5 \* max\_y)
    if subplot \== 2:
        [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("First principal component")
        [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Second principal component")
        [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 6))

X, Y \= [make\_multilabel\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
(
    n\_classes\=2, n\_labels\=1, allow\_unlabeled\=True, random\_state\=1
)

plot\_subfigure(X, Y, 1, "With unlabeled samples + CCA", "cca")
plot\_subfigure(X, Y, 2, "With unlabeled samples + PCA", "pca")

X, Y \= [make\_multilabel\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
(
    n\_classes\=2, n\_labels\=1, allow\_unlabeled\=False, random\_state\=1
)

plot\_subfigure(X, Y, 3, "Without unlabeled samples + CCA", "cca")
plot\_subfigure(X, Y, 4, "Without unlabeled samples + PCA", "pca")

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.182 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_multilabel.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_multilabel.ipynb)

[`Download Jupyter notebook: plot_multilabel.ipynb`](https://scikit-learn.org/stable/_downloads/65b807da1fd0f3cbb60c1425fddba026/plot_multilabel.ipynb)

[`Download Python source code: plot_multilabel.py`](https://scikit-learn.org/stable/_downloads/d9b8062b664fa0515a7849d4a28e98ed/plot_multilabel.py)

[`Download zipped: plot_multilabel.zip`](https://scikit-learn.org/stable/_downloads/02fe21a1f5d14bd1ebbe34aa905d9bf6/plot_multilabel.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_cross_decomposition_thumb.png)

[Compare cross decomposition methods](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)

Compare cross decomposition methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_multilabel_dataset_thumb.png)

[Plot randomly generated multilabel dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html)

Plot randomly generated multilabel dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_thumb.png)

[SVM Margins Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)

SVM Margins Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)

[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Semi-supervised Classification on a Text Dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/d9b8062b664fa0515a7849d4a28e98ed/plot_multilabel.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/65b807da1fd0f3cbb60c1425fddba026/plot_multilabel.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/02fe21a1f5d14bd1ebbe34aa905d9bf6/plot_multilabel.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_multilabel.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_multilabel.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)