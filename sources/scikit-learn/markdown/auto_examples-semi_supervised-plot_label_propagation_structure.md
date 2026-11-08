[Skip to main content](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_structure.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/semi_supervised/plot_label_propagation_structure.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_structure.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/semi_supervised/plot_label_propagation_structure.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/semi_supervised/plot_label_propagation_structure.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/semi_supervised/plot_label_propagation_structure.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/semi_supervised/plot_label_propagation_structure.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/semi_supervised/plot_label_propagation_structure.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_structure.html#sphx-glr-download-auto-examples-semi-supervised-plot-label-propagation-structure-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Label Propagation circles: Learning a complex structure[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_structure.html#label-propagation-circles-learning-a-complex-structure "Link to this heading")

==============================================================================================================================================================================================================================================

Example of LabelPropagation learning a complex internal structure to demonstrate “manifold learning”. The outer circle should be labeled “red” and the inner circle “blue”. Because both label groups lie inside their own distinct shape, we can see that the labels propagate correctly around the circle.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

We generate a dataset with two concentric circles. In addition, a label is associated with each sample of the dataset that is: 0 (belonging to the outer circle), 1 (belonging to the inner circle), and -1 (unknown). Here, all labels but two are tagged as unknown.

import numpy as np

from sklearn.datasets import [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")

n\_samples \= 200
X, y \= [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
(n\_samples\=n\_samples, shuffle\=False)
outer, inner \= 0, 1
labels \= [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n\_samples, \-1.0)
labels\[0\] \= outer
labels\[\-1\] \= inner

Copy to clipboard

Plot raw data

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 4))
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[labels \== outer, 0\],
    X\[labels \== outer, 1\],
    color\="navy",
    marker\="s",
    lw\=0,
    label\="outer labeled",
    s\=10,
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[labels \== inner, 0\],
    X\[labels \== inner, 1\],
    color\="c",
    marker\="s",
    lw\=0,
    label\="inner labeled",
    s\=10,
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[labels \== \-1, 0\],
    X\[labels \== \-1, 1\],
    color\="darkorange",
    marker\=".",
    label\="unlabeled",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(scatterpoints\=1, shadow\=False, loc\="center")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Raw data (2 classes=outer and inner)")

Copy to clipboard

![Raw data (2 classes=outer and inner)](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_structure_001.png)

The aim of [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 is to associate a label to sample where the label is initially unknown.

from sklearn.semi\_supervised import [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")

label\_spread \= [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
(kernel\="knn", alpha\=0.8)
label\_spread.fit(X, labels)

Copy to clipboard

LabelSpreading(alpha=0.8, kernel='knn')

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

LabelSpreading

[?Documentation for LabelSpreading](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [kernel kernel: {'knn', 'rbf'} or callable, default='rbf'  <br>  <br>String identifier for kernel function to use or the kernel function  <br>itself. Only 'rbf' and 'knn' strings are valid inputs. The function  <br>passed should take two inputs, each of shape (n\_samples, n\_features),  <br>and return a (n\_samples, n\_samples) shaped weight matrix.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=kernel,-%7B%27knn%27%2C%20%27rbf%27%7D%20or%20callable%2C%20default%3D%27rbf%27) | 'knn' |
|     | [alpha alpha: float, default=0.2  <br>  <br>Clamping factor. A value in (0, 1) that specifies the relative amount  <br>that an instance should adopt the information from its neighbors as  <br>opposed to its initial label.  <br>alpha=0 means keeping the initial label information; alpha=1 means  <br>replacing all initial information.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=alpha,-float%2C%20default%3D0.2) | 0.8 |
|     | [gamma gamma: float, default=20  <br>  <br>Parameter for rbf kernel.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=gamma,-float%2C%20default%3D20) | 20  |
|     | [n\_neighbors n\_neighbors: int, default=7  <br>  <br>Parameter for knn kernel which is a strictly positive integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=n_neighbors,-int%2C%20default%3D7) | 7   |
|     | [max\_iter max\_iter: int, default=30  <br>  <br>Maximum number of iterations allowed.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=max_iter,-int%2C%20default%3D30) | 30  |
|     | [tol tol: float, default=1e-3  <br>  <br>Convergence tolerance: threshold to consider the system at steady  <br>state.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=tol,-float%2C%20default%3D1e-3) | 0.001 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of parallel jobs to run.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [X\_ X\_: ndarray of shape (n\_samples, n\_features)  <br>  <br>Input array.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=X_,-ndarray%20of%20shape%20%28n_samples%2C%20n_features%29) | ndarray\[float64\](200, 2) | \[\[ 1. , 0. \], \[ 1. , 0.06\], \[ 0.99, 0.13\], ..., \[ 0.79,-0.15\], \[ 0.79,-0.1 \], \[ 0.8 ,-0.05\]\] |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The distinct labels used in classifying instances.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[float64\](2,) | \[0.,1.\] |
| [label\_distributions\_ label\_distributions\_: ndarray of shape (n\_samples, n\_classes)  <br>  <br>Categorical distribution for each item.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=label_distributions_,-ndarray%20of%20shape%20%28n_samples%2C%20n_classes%29) | ndarray\[float64\](200, 2) | \[\[1.,0.\], \[1.,0.\], \[1.,0.\], ..., \[0.,1.\], \[0.,1.\], \[0.,1.\]\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_iter\_ n\_iter\_: int  <br>  <br>Number of iterations run.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=n_iter_,-int) | int | 18  |
| [transduction\_ transduction\_: ndarray of shape (n\_samples,)  <br>  <br>Label assigned to each item during :term:\`fit\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.semi_supervised.LabelSpreading.html#:~:text=transduction_,-ndarray%20of%20shape%20%28n_samples%2C%29) | ndarray\[float64\](200,) | \[0.,0.,0.,...,1.,1.,1.\] |

  
  

Now, we can check which labels have been associated with each sample when the label was unknown.

output\_labels \= label\_spread.transduction\_
output\_label\_array \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(output\_labels)
outer\_numbers \= (output\_label\_array \== outer).nonzero()\[0\]
inner\_numbers \= (output\_label\_array \== inner).nonzero()\[0\]

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 4))
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[outer\_numbers, 0\],
    X\[outer\_numbers, 1\],
    color\="navy",
    marker\="s",
    lw\=0,
    s\=10,
    label\="outer learned",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[inner\_numbers, 0\],
    X\[inner\_numbers, 1\],
    color\="c",
    marker\="s",
    lw\=0,
    s\=10,
    label\="inner learned",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(scatterpoints\=1, shadow\=False, loc\="center")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Labels learned with Label Spreading (KNN)")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Labels learned with Label Spreading (KNN)](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_structure_002.png)

**Total running time of the script:** (0 minutes 0.172 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_label_propagation_structure.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_label_propagation_structure.ipynb)

[`Download Jupyter notebook: plot_label_propagation_structure.ipynb`](https://scikit-learn.org/stable/_downloads/9c824e9beef1b72c9f1ad3f39de0bf57/plot_label_propagation_structure.ipynb)

[`Download Python source code: plot_label_propagation_structure.py`](https://scikit-learn.org/stable/_downloads/c6e2877780eeb2421a441896c8ec77b7/plot_label_propagation_structure.py)

[`Download zipped: plot_label_propagation_structure.zip`](https://scikit-learn.org/stable/_downloads/0919b8971cbb94ffb3b06c80621a3283/plot_label_propagation_structure.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_thumb.png)

[A demo of the Spectral Biclustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html)

A demo of the Spectral Biclustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)

[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Semi-supervised Classification on a Text Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/c6e2877780eeb2421a441896c8ec77b7/plot_label_propagation_structure.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/9c824e9beef1b72c9f1ad3f39de0bf57/plot_label_propagation_structure.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0919b8971cbb94ffb3b06c80621a3283/plot_label_propagation_structure.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_label_propagation_structure.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_label_propagation_structure.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)