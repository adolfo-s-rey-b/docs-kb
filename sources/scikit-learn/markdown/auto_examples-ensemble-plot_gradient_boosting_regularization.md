[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_gradient_boosting_regularization.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_gradient_boosting_regularization.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_gradient_boosting_regularization.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_gradient_boosting_regularization.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_gradient_boosting_regularization.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html#sphx-glr-download-auto-examples-ensemble-plot-gradient-boosting-regularization-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gradient Boosting regularization[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html#gradient-boosting-regularization "Link to this heading")

===============================================================================================================================================================================================

Illustration of the effect of different regularization strategies for Gradient Boosting. The example is taken from Hastie et al 2009 [\[1\]](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html#id2)
.

The loss function used is binomial deviance. Regularization via shrinkage (`learning_rate < 1.0`) improves performance considerably. In combination with shrinkage, stochastic gradient boosting (`subsample < 1.0`) can produce more accurate models by reducing the variance via bagging. Subsampling without shrinkage usually does poorly. Another strategy to reduce the variance is by subsampling the features analogous to the random splits in Random Forests (via the `max_features` parameter).

![plot gradient boosting regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, ensemble
from sklearn.metrics import [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [datasets.make\_hastie\_10\_2](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "sklearn.datasets.make_hastie_10_2")
(n\_samples\=4000, random\_state\=1)

\# map labels from {-1, 1} to {0, 1}
labels, y \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y, return\_inverse\=True)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.8, random\_state\=0)

original\_params \= {
    "n\_estimators": 400,
    "max\_leaf\_nodes": 4,
    "max\_depth": None,
    "random\_state": 2,
    "min\_samples\_split": 5,
}

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

for label, color, setting in \[\
    ("No shrinkage", "orange", {"learning\_rate": 1.0, "subsample": 1.0}),\
    ("learning\_rate=0.2", "turquoise", {"learning\_rate": 0.2, "subsample": 1.0}),\
    ("subsample=0.5", "blue", {"learning\_rate": 1.0, "subsample": 0.5}),\
    (\
        "learning\_rate=0.2, subsample=0.5",\
        "gray",\
        {"learning\_rate": 0.2, "subsample": 0.5},\
    ),\
    (\
        "learning\_rate=0.2, max\_features=2",\
        "magenta",\
        {"learning\_rate": 0.2, "max\_features": 2},\
    ),\
\]:
    params \= dict(original\_params)
    params.update(setting)

    clf \= [ensemble.GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
(\*\*params)
    clf.fit(X\_train, y\_train)

    \# compute test set deviance
    test\_deviance \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((params\["n\_estimators"\],), dtype\=[np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)

    for i, y\_proba in enumerate(clf.staged\_predict\_proba(X\_test)):
        test\_deviance\[i\] \= 2 \* [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\_test, y\_proba\[:, 1\])

    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        ([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(test\_deviance.shape\[0\]) + 1)\[::5\],
        test\_deviance\[::5\],
        "-",
        color\=color,
        label\=label,
    )

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Boosting Iterations")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Test Set Deviance")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 8.165 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_regularization.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_regularization.ipynb)

[`Download Jupyter notebook: plot_gradient_boosting_regularization.ipynb`](https://scikit-learn.org/stable/_downloads/0a90f2b8e2dadb7d37ca67b3f7adb656/plot_gradient_boosting_regularization.ipynb)

[`Download Python source code: plot_gradient_boosting_regularization.py`](https://scikit-learn.org/stable/_downloads/e641093af989b69bc2b89b130bcf320f/plot_gradient_boosting_regularization.py)

[`Download zipped: plot_gradient_boosting_regularization.zip`](https://scikit-learn.org/stable/_downloads/1acfe5256fc92dfaed2c1033304ed297/plot_gradient_boosting_regularization.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_oob_thumb.png)

[Gradient Boosting Out-of-Bag estimates](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html)

Gradient Boosting Out-of-Bag estimates

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_thumb.png)

[Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)

Compare Stochastic learning strategies for MLPClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/e641093af989b69bc2b89b130bcf320f/plot_gradient_boosting_regularization.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0a90f2b8e2dadb7d37ca67b3f7adb656/plot_gradient_boosting_regularization.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1acfe5256fc92dfaed2c1033304ed297/plot_gradient_boosting_regularization.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_regularization.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_regularization.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)