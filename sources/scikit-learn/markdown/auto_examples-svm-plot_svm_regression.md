[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_svm_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_svm_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_svm_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_svm_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_svm_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#sphx-glr-download-auto-examples-svm-plot-svm-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Support Vector Regression (SVR) using linear and non-linear kernels[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#support-vector-regression-svr-using-linear-and-non-linear-kernels "Link to this heading")

============================================================================================================================================================================================================================================

Toy example of 1D regression using linear, polynomial and RBF kernels.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#generate-sample-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(5 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(40, 1), axis\=0)
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X).ravel()

\# add noise to targets
y\[::5\] += 3 \* (0.5 \- [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(8))

Copy to clipboard

Fit regression model[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#fit-regression-model "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

svr\_rbf \= [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
(kernel\="rbf", C\=100, gamma\=0.1, epsilon\=0.1)
svr\_lin \= [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
(kernel\="linear", C\=100, gamma\="auto")
svr\_poly \= [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
(kernel\="poly", C\=100, gamma\="auto", degree\=3, epsilon\=0.1, coef0\=1)

Copy to clipboard

Look at the results[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#look-at-the-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

lw \= 2

svrs \= \[svr\_rbf, svr\_lin, svr\_poly\]
kernel\_label \= \["RBF", "Linear", "Polynomial"\]
model\_color \= \["m", "c", "g"\]

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=3, figsize\=(15, 10), sharey\=True)
for ix, svr in enumerate(svrs):
    axes\[ix\].plot(
        X,
        svr.fit(X, y).predict(X),
        color\=model\_color\[ix\],
        lw\=lw,
        label\="{} model".format(kernel\_label\[ix\]),
    )
    axes\[ix\].scatter(
        X\[svr.support\_\],
        y\[svr.support\_\],
        facecolor\="none",
        edgecolor\=model\_color\[ix\],
        s\=50,
        label\="{} support vectors".format(kernel\_label\[ix\]),
    )
    axes\[ix\].scatter(
        X\[[np.setdiff1d](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html#numpy.setdiff1d "numpy.setdiff1d")\
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(len(X)), svr.support\_)\],
        y\[[np.setdiff1d](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html#numpy.setdiff1d "numpy.setdiff1d")\
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(len(X)), svr.support\_)\],
        facecolor\="none",
        edgecolor\="k",
        s\=50,
        label\="other training data",
    )
    axes\[ix\].legend(
        loc\="upper center",
        bbox\_to\_anchor\=(0.5, 1.1),
        ncol\=1,
        fancybox\=True,
        shadow\=True,
    )

fig.text(0.5, 0.04, "data", ha\="center", va\="center")
fig.text(0.06, 0.5, "target", ha\="center", va\="center", rotation\="vertical")
fig.suptitle("Support Vector Regression", fontsize\=14)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Support Vector Regression](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_regression_001.png)

**Total running time of the script:** (0 minutes 5.690 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_regression.ipynb)

[`Download Jupyter notebook: plot_svm_regression.ipynb`](https://scikit-learn.org/stable/_downloads/85b2b4f3ecdf3d37834c318b4889b4c0/plot_svm_regression.ipynb)

[`Download Python source code: plot_svm_regression.py`](https://scikit-learn.org/stable/_downloads/92eee1e3e3d824360fee295386f12216/plot_svm_regression.py)

[`Download zipped: plot_svm_regression.zip`](https://scikit-learn.org/stable/_downloads/461290890e86d787be8ca355c3c65e4a/plot_svm_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_thumb.png)

[Comparison of kernel ridge regression and SVR](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)

Comparison of kernel ridge regression and SVR

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)

[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Comparison between grid search and successive halving

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/92eee1e3e3d824360fee295386f12216/plot_svm_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/85b2b4f3ecdf3d37834c318b4889b4c0/plot_svm_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/461290890e86d787be8ca355c3c65e4a/plot_svm_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)