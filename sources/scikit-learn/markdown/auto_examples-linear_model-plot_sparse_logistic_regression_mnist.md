[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html#sphx-glr-download-auto-examples-linear-model-plot-sparse-logistic-regression-mnist-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

MNIST classification using multinomial logistic + L1[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html#mnist-classification-using-multinomial-logistic-l1 "Link to this heading")

=========================================================================================================================================================================================================================================

Here we fit a multinomial logistic regression with L1 penalty on a subset of the MNIST digits classification task. We use the SAGA algorithm for this purpose: this a solver that is fast when the number of samples is significantly larger than the number of features and is able to finely optimize non-smooth objective functions which is the case with the l1-penalty. Test accuracy reaches > 0.8, while weight vectors remains _sparse_ and therefore more easily _interpretable_.

Note that this accuracy of this l1-penalized linear model is significantly below what can be reached by an l2-penalized linear model or a non-linear multi-layer perceptron model on this dataset.

![Classification vector for...](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_001.png)

Sparsity with L1 penalty: 80.33%
Test score with L1 penalty: 0.8212
Example run in 6.601 s

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.utils import [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")

\# Turn down for faster convergence
t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
train\_samples \= 5000

\# Load data from https://www.openml.org/d/554
X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("mnist\_784", version\=1, return\_X\_y\=True, as\_frame\=False)

random\_state \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(0)
permutation \= random\_state.permutation(X.shape\[0\])
X \= X\[permutation\]
y \= y\[permutation\]
X \= X.reshape((X.shape\[0\], \-1))

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, train\_size\=train\_samples, test\_size\=10000
)

scaler \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()
X\_train \= scaler.fit\_transform(X\_train)
X\_test \= scaler.transform(X\_test)

\# Turn up tolerance for faster convergence
clf \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=50.0 / train\_samples, l1\_ratio\=1, solver\="saga", tol\=0.1)
clf.fit(X\_train, y\_train)
sparsity \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(clf.coef\_ \== 0) \* 100
score \= clf.score(X\_test, y\_test)
\# print('Best C % .4f' % clf.C\_)
print("Sparsity with L1 penalty: %.2f%%" % sparsity)
print("Test score with L1 penalty: %.4f" % score)

coef \= clf.coef\_.copy()
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 5))
scale \= np.abs(coef).max()
for i in range(10):
    l1\_plot \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 5, i + 1)
    l1\_plot.imshow(
        coef\[i\].reshape(28, 28),
        interpolation\="nearest",
        cmap\=plt.cm.RdBu,
        vmin\=-scale,
        vmax\=scale,
    )
    l1\_plot.set\_xticks(())
    l1\_plot.set\_yticks(())
    l1\_plot.set\_xlabel(f"Class {i}")
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Classification vector for...")

run\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print("Example run in %.3f s" % run\_time)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 6.674 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sparse_logistic_regression_mnist.ipynb)

[`Download Jupyter notebook: plot_sparse_logistic_regression_mnist.ipynb`](https://scikit-learn.org/stable/_downloads/2a5eb3b98b9fe593b9bfeb548a54175d/plot_sparse_logistic_regression_mnist.ipynb)

[`Download Python source code: plot_sparse_logistic_regression_mnist.py`](https://scikit-learn.org/stable/_downloads/5a847ed2e1c03e450c5f9dee339423ad/plot_sparse_logistic_regression_mnist.py)

[`Download zipped: plot_sparse_logistic_regression_mnist.zip`](https://scikit-learn.org/stable/_downloads/f8915489864d3c3a6162a9d08c2ddc8b/plot_sparse_logistic_regression_mnist.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/5a847ed2e1c03e450c5f9dee339423ad/plot_sparse_logistic_regression_mnist.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2a5eb3b98b9fe593b9bfeb548a54175d/plot_sparse_logistic_regression_mnist.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f8915489864d3c3a6162a9d08c2ddc8b/plot_sparse_logistic_regression_mnist.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sparse_logistic_regression_mnist.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)