[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html#sphx-glr-download-auto-examples-linear-model-plot-sparse-logistic-regression-20newsgroups-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Multiclass sparse logistic regression on 20newgroups[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html#multiclass-sparse-logistic-regression-on-20newgroups "Link to this heading")

==================================================================================================================================================================================================================================================

Comparison of multinomial logistic L1 vs one-versus-rest L1 logistic regression to classify documents from the newgroups20 dataset. Multinomial logistic regression yields more accurate results and is faster to train on the larger scale dataset.

Here we use the l1 sparsity that trims the weights of not informative features to zero. This is good if the goal is to extract the strongly discriminative vocabulary of each class. If the goal is to get the best predictive accuracy, it is better to use the non sparsity-inducing l2 penalty instead.

A more traditional (and possibly better) way to predict on a sparse subset of input features would be to use univariate feature selection followed by a traditional (l2-penalised) logistic regression model.

![Multinomial vs One-vs-Rest Logistic L1 Dataset 20newsgroups](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_001.png)

Dataset 20newsgroup, train\_samples=4500, n\_features=130107, n\_classes=20
\[model=One versus Rest, solver=saga\] Number of epochs: 1
\[model=One versus Rest, solver=saga\] Number of epochs: 2
\[model=One versus Rest, solver=saga\] Number of epochs: 3
Test accuracy for model ovr: 0.5960
% non-zero coefficients for model ovr, per class:
 \[0.26593496 0.43348936 0.26362917 0.31973683 0.37815029 0.2928359\
 0.27054655 0.62717609 0.19522393 0.30897646 0.34586917 0.28207552\
 0.34125758 0.29898468 0.34279478 0.59489497 0.38353048 0.35278655\
 0.19829832 0.14603365\]
Run time (3 epochs) for model ovr:1.14
\[model=Multinomial, solver=saga\] Number of epochs: 1
\[model=Multinomial, solver=saga\] Number of epochs: 2
\[model=Multinomial, solver=saga\] Number of epochs: 5
Test accuracy for model multinomial: 0.6440
% non-zero coefficients for model multinomial, per class:
 \[0.36047253 0.1268187  0.10606655 0.17985197 0.5395559  0.07993421\
 0.06686804 0.21443888 0.11528972 0.2075215  0.10914094 0.11144673\
 0.13988486 0.09684337 0.26286057 0.11682692 0.55800226 0.17370318\
 0.11452112 0.14603365\]
Run time (5 epochs) for model multinomial:0.90
Example run in 5.128 s

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import timeit
import warnings

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [fetch\_20newsgroups\_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
from sklearn.exceptions import [ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.multiclass import [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")

[warnings.filterwarnings](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings")
("ignore", category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
, module\="sklearn")
t0 \= [timeit.default\_timer](https://docs.python.org/3/library/timeit.html#timeit.default_timer "timeit.default_timer")
()

\# We use SAGA solver
solver \= "saga"

\# Turn down for faster run time
n\_samples \= 5000

X, y \= [fetch\_20newsgroups\_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
(subset\="all", return\_X\_y\=True)
X \= X\[:n\_samples\]
y \= y\[:n\_samples\]

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, random\_state\=42, stratify\=y, test\_size\=0.1
)
train\_samples, n\_features \= X\_train.shape
n\_classes \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y).shape\[0\]

print(
    "Dataset 20newsgroup, train\_samples=%i, n\_features=%i, n\_classes=%i"
    % (train\_samples, n\_features, n\_classes)
)

models \= {
    "ovr": {"name": "One versus Rest", "iters": \[1, 2, 3\]},
    "multinomial": {"name": "Multinomial", "iters": \[1, 2, 5\]},
}

for model in models:
    \# Add initial chance-level values for plotting purpose
    accuracies \= \[1 / n\_classes\]
    times \= \[0\]
    densities \= \[1\]

    model\_params \= models\[model\]

    \# Small number of epochs for fast runtime
    for this\_max\_iter in model\_params\["iters"\]:
        print(
            "\[model=%s, solver=%s\] Number of epochs: %s"
            % (model\_params\["name"\], solver, this\_max\_iter)
        )
        clf \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(
            l1\_ratio\=1,
            solver\=solver,
            max\_iter\=this\_max\_iter,
            random\_state\=42,
        )
        if model \== "ovr":
            clf \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
(clf)
        t1 \= [timeit.default\_timer](https://docs.python.org/3/library/timeit.html#timeit.default_timer "timeit.default_timer")
()
        clf.fit(X\_train, y\_train)
        train\_time \= [timeit.default\_timer](https://docs.python.org/3/library/timeit.html#timeit.default_timer "timeit.default_timer")
() \- t1

        y\_pred \= clf.predict(X\_test)
        accuracy \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(y\_pred \== y\_test) / y\_test.shape\[0\]
        if model \== "ovr":
            coef \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[est.coef\_ for est in clf.estimators\_\])
        else:
            coef \= clf.coef\_
        density \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(coef != 0, axis\=1) \* 100
        accuracies.append(accuracy)
        densities.append(density)
        times.append(train\_time)
    models\[model\]\["times"\] \= times
    models\[model\]\["densities"\] \= densities
    models\[model\]\["accuracies"\] \= accuracies
    print("Test accuracy for model %s: %.4f" % (model, accuracies\[\-1\]))
    print(
        "%% non-zero coefficients for model %s, per class:\\n %s"
        % (model, densities\[\-1\])
    )
    print(
        "Run time (%i epochs) for model %s:%.2f"
        % (model\_params\["iters"\]\[\-1\], model, times\[\-1\])
    )

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
ax \= fig.add\_subplot(111)

for model in models:
    name \= models\[model\]\["name"\]
    times \= models\[model\]\["times"\]
    accuracies \= models\[model\]\["accuracies"\]
    ax.plot(times, accuracies, marker\="o", label\="Model: %s" % name)
    ax.set\_xlabel("Train time (s)")
    ax.set\_ylabel("Test accuracy")
ax.legend()
fig.suptitle("Multinomial vs One-vs-Rest Logistic L1\\nDataset %s" % "20newsgroups")
fig.tight\_layout()
fig.subplots\_adjust(top\=0.85)
run\_time \= [timeit.default\_timer](https://docs.python.org/3/library/timeit.html#timeit.default_timer "timeit.default_timer")
() \- t0
print("Example run in %.3f s" % run\_time)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 5.213 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.ipynb)

[`Download Jupyter notebook: plot_sparse_logistic_regression_20newsgroups.ipynb`](https://scikit-learn.org/stable/_downloads/583de4ea98c6544c52ea4c57e62b1813/plot_sparse_logistic_regression_20newsgroups.ipynb)

[`Download Python source code: plot_sparse_logistic_regression_20newsgroups.py`](https://scikit-learn.org/stable/_downloads/7e30d5b899fc588cbc75553c65cb76ed/plot_sparse_logistic_regression_20newsgroups.py)

[`Download zipped: plot_sparse_logistic_regression_20newsgroups.zip`](https://scikit-learn.org/stable/_downloads/e9634f730904cc10c4d965d5e91bf2a1/plot_sparse_logistic_regression_20newsgroups.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_thumb.png)

[Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/7e30d5b899fc588cbc75553c65cb76ed/plot_sparse_logistic_regression_20newsgroups.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/583de4ea98c6544c52ea4c57e62b1813/plot_sparse_logistic_regression_20newsgroups.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e9634f730904cc10c4d965d5e91bf2a1/plot_sparse_logistic_regression_20newsgroups.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)