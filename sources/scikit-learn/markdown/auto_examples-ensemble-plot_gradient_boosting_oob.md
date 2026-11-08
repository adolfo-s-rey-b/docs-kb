[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_gradient_boosting_oob.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_gradient_boosting_oob.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_gradient_boosting_oob.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_gradient_boosting_oob.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_gradient_boosting_oob.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_gradient_boosting_oob.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html#sphx-glr-download-auto-examples-ensemble-plot-gradient-boosting-oob-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gradient Boosting Out-of-Bag estimates[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html#gradient-boosting-out-of-bag-estimates "Link to this heading")

================================================================================================================================================================================================

Out-of-bag (OOB) estimates can be a useful heuristic to estimate the “optimal” number of boosting iterations. OOB estimates are almost identical to cross-validation estimates but they can be computed on-the-fly without the need for repeated model fitting. OOB estimates are only available for Stochastic Gradient Boosting (i.e. `subsample < 1.0`), the estimates are derived from the improvement in loss based on the examples not included in the bootstrap sample (the so-called out-of-bag examples). The OOB estimator is a pessimistic estimator of the true test loss, but remains a fairly good approximation for a small number of trees. The figure shows the cumulative sum of the negative OOB improvements as a function of the boosting iteration. As you can see, it tracks the test loss for the first hundred iterations but then diverges in a pessimistic way. The figure also shows the performance of 3-fold cross validation which usually gives a better estimate of the test loss but is computationally more demanding.

![plot gradient boosting oob](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_oob_001.png)

Accuracy: 0.6800

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import [expit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expit.html#scipy.special.expit "scipy.special.expit")

from sklearn import ensemble
from sklearn.metrics import [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
from sklearn.model\_selection import [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
, [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

\# Generate data (adapted from G. Ridgeway's gbm example)
n\_samples \= 1000
random\_state \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(13)
x1 \= random\_state.uniform(size\=n\_samples)
x2 \= random\_state.uniform(size\=n\_samples)
x3 \= random\_state.randint(0, 4, size\=n\_samples)

p \= [expit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expit.html#scipy.special.expit "scipy.special.expit")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(3 \* x1) \- 4 \* x2 + x3)
y \= random\_state.binomial(1, p, size\=n\_samples)

X \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[x1, x2, x3\]

X \= X.astype([np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.5, random\_state\=9)

\# Fit classifier with out-of-bag estimates
params \= {
    "n\_estimators": 1200,
    "max\_depth": 3,
    "subsample": 0.5,
    "learning\_rate": 0.01,
    "min\_samples\_leaf": 1,
    "random\_state": 3,
}
clf \= [ensemble.GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
(\*\*params)

clf.fit(X\_train, y\_train)
acc \= clf.score(X\_test, y\_test)
print("Accuracy: {:.4f}".format(acc))

n\_estimators \= params\["n\_estimators"\]
x \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_estimators) + 1

def heldout\_score(clf, X\_test, y\_test):
    """compute deviance scores on \`\`X\_test\`\` and \`\`y\_test\`\`."""
    score \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_estimators,), dtype\=[np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
    for i, y\_proba in enumerate(clf.staged\_predict\_proba(X\_test)):
        score\[i\] \= 2 \* [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\_test, y\_proba\[:, 1\])
    return score

def cv\_estimate(n\_splits\=None):
    cv \= [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(n\_splits\=n\_splits)
    cv\_clf \= [ensemble.GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
(\*\*params)
    val\_scores \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_estimators,), dtype\=[np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
    for train, test in cv.split(X\_train, y\_train):
        cv\_clf.fit(X\_train\[train\], y\_train\[train\])
        val\_scores += heldout\_score(cv\_clf, X\_train\[test\], y\_train\[test\])
    val\_scores /= n\_splits
    return val\_scores

\# Estimate best n\_estimator using cross-validation
cv\_score \= cv\_estimate(3)

\# Compute best n\_estimator for test data
test\_score \= heldout\_score(clf, X\_test, y\_test)

\# negative cumulative sum of oob improvements
cumsum \= \-[np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
(clf.oob\_improvement\_)

\# min loss according to OOB
oob\_best\_iter \= x\[[np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")\
(cumsum)\]

\# min loss according to test (normalize such that first loss is 0)
test\_score \-= test\_score\[0\]
test\_best\_iter \= x\[[np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")\
(test\_score)\]

\# min loss according to cv (normalize such that first loss is 0)
cv\_score \-= cv\_score\[0\]
cv\_best\_iter \= x\[[np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")\
(cv\_score)\]

\# color brew for the three curves
oob\_color \= list(map(lambda x: x / 256.0, (190, 174, 212)))
test\_color \= list(map(lambda x: x / 256.0, (127, 201, 127)))
cv\_color \= list(map(lambda x: x / 256.0, (253, 192, 134)))

\# line type for the three curves
oob\_line \= "dashed"
test\_line \= "solid"
cv\_line \= "dashdot"

\# plot curves and vertical lines for best iterations
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 4.8))
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, cumsum, label\="OOB loss", color\=oob\_color, linestyle\=oob\_line)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, test\_score, label\="Test loss", color\=test\_color, linestyle\=test\_line)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, cv\_score, label\="CV loss", color\=cv\_color, linestyle\=cv\_line)
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(x\=oob\_best\_iter, color\=oob\_color, linestyle\=oob\_line)
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(x\=test\_best\_iter, color\=test\_color, linestyle\=test\_line)
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(x\=cv\_best\_iter, color\=cv\_color, linestyle\=cv\_line)

\# add three vertical lines to xticks
xticks \= [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
()
xticks\_pos \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    xticks\[0\].tolist() + \[oob\_best\_iter, cv\_best\_iter, test\_best\_iter\]
)
xticks\_label \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(list(map(lambda t: int(t), xticks\[0\])) + \["OOB", "CV", "Test"\])
ind \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(xticks\_pos)
xticks\_pos \= xticks\_pos\[ind\]
xticks\_label \= xticks\_label\[ind\]
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(xticks\_pos, xticks\_label, rotation\=90)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper center")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("normalized loss")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("number of iterations")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 12.099 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_oob.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_oob.ipynb)

[`Download Jupyter notebook: plot_gradient_boosting_oob.ipynb`](https://scikit-learn.org/stable/_downloads/d45483409febd18772e1fe41233d258e/plot_gradient_boosting_oob.ipynb)

[`Download Python source code: plot_gradient_boosting_oob.py`](https://scikit-learn.org/stable/_downloads/a0f093cdc82e6c383a734fc9beaf8e24/plot_gradient_boosting_oob.py)

[`Download zipped: plot_gradient_boosting_oob.zip`](https://scikit-learn.org/stable/_downloads/2fce81c38823a4c8e6cf7beebb010f00/plot_gradient_boosting_oob.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ensemble_oob_thumb.png)

[OOB Errors for Random Forests](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html)

OOB Errors for Random Forests

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)

[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Gradient Boosting regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/a0f093cdc82e6c383a734fc9beaf8e24/plot_gradient_boosting_oob.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/d45483409febd18772e1fe41233d258e/plot_gradient_boosting_oob.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2fce81c38823a4c8e6cf7beebb010f00/plot_gradient_boosting_oob.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_oob.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_oob.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)