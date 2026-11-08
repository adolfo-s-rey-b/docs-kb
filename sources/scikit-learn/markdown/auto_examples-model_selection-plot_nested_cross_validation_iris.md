[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_nested_cross_validation_iris.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_nested_cross_validation_iris.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_nested_cross_validation_iris.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_nested_cross_validation_iris.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_nested_cross_validation_iris.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html#sphx-glr-download-auto-examples-model-selection-plot-nested-cross-validation-iris-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Nested versus non-nested cross-validation[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html#nested-versus-non-nested-cross-validation "Link to this heading")

====================================================================================================================================================================================================================

This example compares non-nested and nested cross-validation strategies on a classifier of the iris data set. Nested cross-validation (CV) is often used to train a model in which hyperparameters also need to be optimized. Nested CV estimates the generalization error of the underlying model and its (hyper)parameter search. Choosing the parameters that maximize non-nested CV biases the model to the dataset, yielding an overly-optimistic score.

Model selection without nested CV uses the same data to tune model parameters and evaluate model performance. Information may thus “leak” into the model and overfit the data. The magnitude of this effect is primarily dependent on the size of the dataset and the stability of the model. See Cawley and Talbot [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html#id2)
 for an analysis of these issues.

To avoid this problem, nested CV effectively uses a series of train/validation/test set splits. In the inner loop (here executed by [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
), the score is approximately maximized by fitting a model to each training set, and then directly maximized in selecting (hyper)parameters over the validation set. In the outer loop (here in [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
), generalization error is estimated by averaging test set scores over several dataset splits.

The example below uses a support vector classifier with a non-linear kernel to build a model with optimized hyperparameters by grid search. We compare the performance of non-nested and nested CV strategies by taking the difference between their scores.

See also

*   [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
    
*   [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
    

References

![Non-Nested and Nested Cross Validation on Iris Dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_001.png)

Average difference of 0.007581 with std. dev. of 0.007833.

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
, [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

\# Number of random trials
NUM\_TRIALS \= 30

\# Load the dataset
iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X\_iris \= iris.data
y\_iris \= iris.target

\# Set up possible values of parameters to optimize over
p\_grid \= {"C": \[1, 10, 100\], "gamma": \[0.01, 0.1\]}

\# We will use a Support Vector Classifier with "rbf" kernel
svm \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="rbf")

\# Arrays to store scores
non\_nested\_scores \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(NUM\_TRIALS)
nested\_scores \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(NUM\_TRIALS)

\# Loop for each trial
for i in range(NUM\_TRIALS):
    \# Choose cross-validation techniques for the inner and outer loops,
    \# independently of the dataset.
    \# E.g "GroupKFold", "LeaveOneOut", "LeaveOneGroupOut", etc.
    inner\_cv \= [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(n\_splits\=4, shuffle\=True, random\_state\=i)
    outer\_cv \= [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(n\_splits\=4, shuffle\=True, random\_state\=i)

    \# Non\_nested parameter search and scoring
    clf \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(estimator\=svm, param\_grid\=p\_grid, cv\=outer\_cv)
    clf.fit(X\_iris, y\_iris)
    non\_nested\_scores\[i\] \= clf.best\_score\_

    \# Nested CV with parameter optimization
    clf \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(estimator\=svm, param\_grid\=p\_grid, cv\=inner\_cv)
    nested\_score \= [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(clf, X\=X\_iris, y\=y\_iris, cv\=outer\_cv)
    nested\_scores\[i\] \= nested\_score.mean()

score\_difference \= non\_nested\_scores \- nested\_scores

print(
    "Average difference of {:6f} with std. dev. of {:6f}.".format(
        score\_difference.mean(), score\_difference.std()
    )
)

\# Plot scores on each trial for nested and non-nested CV
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(211)
(non\_nested\_scores\_line,) \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(non\_nested\_scores, color\="r")
(nested\_line,) \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(nested\_scores, color\="b")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("score", fontsize\="14")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    \[non\_nested\_scores\_line, nested\_line\],
    \["Non-Nested CV", "Nested CV"\],
    bbox\_to\_anchor\=(0, 0.4, 0.5, 0),
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Non-Nested and Nested Cross Validation on Iris Dataset",
    x\=0.5,
    y\=1.1,
    fontsize\="15",
)

\# Plot bar chart of the difference.
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(212)
difference\_plot \= [plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(range(NUM\_TRIALS), score\_difference)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Individual Trial #")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    \[difference\_plot\],
    \["Non-Nested CV - Nested CV Score"\],
    bbox\_to\_anchor\=(0, 1, 0.8, 0),
)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("score difference", fontsize\="14")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 9.014 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_nested_cross_validation_iris.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_nested_cross_validation_iris.ipynb)

[`Download Jupyter notebook: plot_nested_cross_validation_iris.ipynb`](https://scikit-learn.org/stable/_downloads/45916745bb89ca49be3a50aa80e65e3f/plot_nested_cross_validation_iris.ipynb)

[`Download Python source code: plot_nested_cross_validation_iris.py`](https://scikit-learn.org/stable/_downloads/23614d75e8327ef369659da7d2ed62db/plot_nested_cross_validation_iris.py)

[`Download zipped: plot_nested_cross_validation_iris.zip`](https://scikit-learn.org/stable/_downloads/e4e5f5cf3f2329fa034f4cc5287020f8/plot_nested_cross_validation_iris.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_thumb.png)

[Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)

Visualizing cross-validation behavior in scikit-learn

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/23614d75e8327ef369659da7d2ed62db/plot_nested_cross_validation_iris.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/45916745bb89ca49be3a50aa80e65e3f/plot_nested_cross_validation_iris.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e4e5f5cf3f2329fa034f4cc5287020f8/plot_nested_cross_validation_iris.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_nested_cross_validation_iris.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_nested_cross_validation_iris.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)