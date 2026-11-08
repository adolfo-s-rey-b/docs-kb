[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_weighted_samples.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_weighted_samples.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_weighted_samples.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_weighted_samples.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_weighted_samples.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_weighted_samples.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html#sphx-glr-download-auto-examples-svm-plot-weighted-samples-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM: Weighted samples[#](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html#svm-weighted-samples "Link to this heading")

===================================================================================================================================================

Plot decision function of a weighted dataset, where the size of points is proportional to its weight.

The sample weighting rescales the C parameter, which means that the classifier puts more emphasis on getting these points right. The effect might often be subtle. To emphasize the effect here, we particularly increase the weight of the positive class, making the deformation of the decision boundary more visible.

![Constant weights, Modified weights](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=1\_000,
    n\_features\=2,
    n\_informative\=2,
    n\_redundant\=0,
    n\_clusters\_per\_class\=1,
    class\_sep\=1.1,
    weights\=\[0.9, 0.1\],
    random\_state\=0,
)
\# down-sample for plotting
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
plot\_indices \= rng.choice([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.shape\[0\]), size\=100, replace\=True)
X\_plot, y\_plot \= X\[plot\_indices\], y\[plot\_indices\]

def plot\_decision\_function(classifier, sample\_weight, axis, title):
    """Plot the synthetic data and the classifier decision function. Points with
    larger sample\_weight are mapped to larger circles in the scatter plot."""
    axis.scatter(
        X\_plot\[:, 0\],
        X\_plot\[:, 1\],
        c\=y\_plot,
        s\=100 \* sample\_weight\[plot\_indices\],
        alpha\=0.9,
        cmap\=plt.cm.bone,
        edgecolors\="black",
    )
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        classifier,
        X\_plot,
        response\_method\="decision\_function",
        alpha\=0.75,
        ax\=axis,
        cmap\=plt.cm.bone,
    )
    axis.axis("off")
    axis.set\_title(title)

\# we define constant weights as expected by the plotting function
sample\_weight\_constant \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len(X))
\# assign random weights to all points
sample\_weight\_modified \= abs(rng.randn(len(X)))
\# assign bigger weights to the positive class
positive\_class\_indices \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(y \== 1).nonzero()\[0\]
sample\_weight\_modified\[positive\_class\_indices\] \*= 15

\# This model does not include sample weights.
clf\_no\_weights \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(gamma\=1)
clf\_no\_weights.fit(X, y)

\# This other model includes sample weights.
clf\_weights \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(gamma\=1)
clf\_weights.fit(X, y, sample\_weight\=sample\_weight\_modified)

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(14, 6))
plot\_decision\_function(
    clf\_no\_weights, sample\_weight\_constant, axes\[0\], "Constant weights"
)
plot\_decision\_function(clf\_weights, sample\_weight\_modified, axes\[1\], "Modified weights")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.317 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_weighted_samples.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_weighted_samples.ipynb)

[`Download Jupyter notebook: plot_weighted_samples.ipynb`](https://scikit-learn.org/stable/_downloads/cea3fc06a4f342c635cadafa63b33319/plot_weighted_samples.ipynb)

[`Download Python source code: plot_weighted_samples.py`](https://scikit-learn.org/stable/_downloads/d03d4aeab237925427bfe3c81433b953/plot_weighted_samples.py)

[`Download zipped: plot_weighted_samples.zip`](https://scikit-learn.org/stable/_downloads/f4caac5f151abedf4fe41507b2ef12a6/plot_weighted_samples.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_elastic_net_precomputed_gram_matrix_with_weighted_samples_thumb.png)

[Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)

Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_regression_thumb.png)

[Nearest Neighbors regression](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html)

Nearest Neighbors regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/d03d4aeab237925427bfe3c81433b953/plot_weighted_samples.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/cea3fc06a4f342c635cadafa63b33319/plot_weighted_samples.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f4caac5f151abedf4fe41507b2ef12a6/plot_weighted_samples.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_weighted_samples.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_weighted_samples.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)