[Skip to main content](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/multiclass/plot_multiclass_overview.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/multiclass/plot_multiclass_overview.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/multiclass/plot_multiclass_overview.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/multiclass/plot_multiclass_overview.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/multiclass/plot_multiclass_overview.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/multiclass/plot_multiclass_overview.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#sphx-glr-download-auto-examples-multiclass-plot-multiclass-overview-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Overview of multiclass training meta-estimators[#](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#overview-of-multiclass-training-meta-estimators "Link to this heading")

==================================================================================================================================================================================================================

In this example, we discuss the problem of classification when the target variable is composed of more than two classes. This is called multiclass classification.

In scikit-learn, all estimators support multiclass classification out of the box: the most sensible strategy was implemented for the end-user. The [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
 module implements various strategies that one can use for experimenting or developing third-party estimators that only support binary classification.

[`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
 includes OvO/OvR strategies used to train a multiclass classifier by fitting a set of binary classifiers (the [`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
 and [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 meta-estimators). This example will review them.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

The Yeast UCI dataset[#](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#the-yeast-uci-dataset "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

In this example, we use a UCI dataset [\[1\]](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#id5)
, generally referred as the Yeast dataset. We use the [`sklearn.datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
 function to load the dataset from OpenML.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=181, as\_frame\=True, return\_X\_y\=True)

Copy to clipboard

To know the type of data science problem we are dealing with, we can check the target for which we want to build a predictive model.

y.value\_counts().sort\_index()

Copy to clipboard

class\_protein\_localization
CYT    463
ERL      5
EXC     35
ME1     44
ME2     51
ME3    163
MIT    244
NUC    429
POX     20
VAC     30
Name: count, dtype: int64

Copy to clipboard

We see that the target is discrete and composed of 10 classes. We therefore deal with a multiclass classification problem.

Strategies comparison[#](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#strategies-comparison "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

In the following experiment, we use a [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 and a [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
 cross-validation with 3 splits and 5 repetitions.

We compare the following strategies:

*   [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     can handle multiclass classification without needing any special adjustments. It works by breaking down the training data into smaller subsets and focusing on the most common class in each subset. By repeating this process, the model can accurately classify input data into multiple different classes.
    
*   [`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     trains a set of binary classifiers where each classifier is trained to distinguish between two classes.
    
*   [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
    : trains a set of binary classifiers where each classifier is trained to distinguish between one class and the rest of the classes.
    
*   [`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
    : trains a set of binary classifiers where each classifier is trained to distinguish between a set of classes from the rest of the classes. The set of classes is defined by a codebook, which is randomly generated in scikit-learn. This method exposes a parameter `code_size` to control the size of the codebook. We set it above one since we are not interested in compressing the class representation.
    

import pandas as pd

from sklearn.model\_selection import [RepeatedStratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
, [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
from sklearn.multiclass import (
    [OneVsOneClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
,
    [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
,
    [OutputCodeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
,
)
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

cv \= [RepeatedStratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
(n\_splits\=3, n\_repeats\=5, random\_state\=0)

tree \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(random\_state\=0)
ovo\_tree \= [OneVsOneClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
(tree)
ovr\_tree \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
(tree)
ecoc \= [OutputCodeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
(tree, code\_size\=2)

cv\_results\_tree \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(tree, X, y, cv\=cv, n\_jobs\=2)
cv\_results\_ovo \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(ovo\_tree, X, y, cv\=cv, n\_jobs\=2)
cv\_results\_ovr \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(ovr\_tree, X, y, cv\=cv, n\_jobs\=2)
cv\_results\_ecoc \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(ecoc, X, y, cv\=cv, n\_jobs\=2)

Copy to clipboard

We can now compare the statistical performance of the different strategies. We plot the score distribution of the different strategies.

from matplotlib import pyplot as plt

scores \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "DecisionTreeClassifier": cv\_results\_tree\["test\_score"\],
        "OneVsOneClassifier": cv\_results\_ovo\["test\_score"\],
        "OneVsRestClassifier": cv\_results\_ovr\["test\_score"\],
        "OutputCodeClassifier": cv\_results\_ecoc\["test\_score"\],
    }
)
ax \= scores.plot.kde(legend\=True)
ax.set\_xlabel("Accuracy score")
ax.set\_xlim(\[0, 0.7\])
\_ \= ax.set\_title(
    "Density of the accuracy scores for the different multiclass strategies"
)

Copy to clipboard

![Density of the accuracy scores for the different multiclass strategies](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_001.png)

At a first glance, we can see that the built-in strategy of the decision tree classifier is working quite well. One-vs-one and the error-correcting output code strategies are working even better. However, the one-vs-rest strategy is not working as well as the other strategies.

Indeed, these results reproduce something reported in the literature as in [\[2\]](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#id6)
. However, the story is not as simple as it seems.

The importance of hyperparameters search[#](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#the-importance-of-hyperparameters-search "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It was later shown in [\[3\]](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#id7)
 that the multiclass strategies would show similar scores if the hyperparameters of the base classifiers are first optimized.

Here we try to reproduce such result by at least optimizing the depth of the base decision tree.

from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")

param\_grid \= {"max\_depth": \[3, 5, 8\]}
tree\_optimized \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(tree, param\_grid\=param\_grid, cv\=3)
ovo\_tree \= [OneVsOneClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
(tree\_optimized)
ovr\_tree \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
(tree\_optimized)
ecoc \= [OutputCodeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
(tree\_optimized, code\_size\=2)

cv\_results\_tree \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(tree\_optimized, X, y, cv\=cv, n\_jobs\=2)
cv\_results\_ovo \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(ovo\_tree, X, y, cv\=cv, n\_jobs\=2)
cv\_results\_ovr \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(ovr\_tree, X, y, cv\=cv, n\_jobs\=2)
cv\_results\_ecoc \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(ecoc, X, y, cv\=cv, n\_jobs\=2)

scores \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "DecisionTreeClassifier": cv\_results\_tree\["test\_score"\],
        "OneVsOneClassifier": cv\_results\_ovo\["test\_score"\],
        "OneVsRestClassifier": cv\_results\_ovr\["test\_score"\],
        "OutputCodeClassifier": cv\_results\_ecoc\["test\_score"\],
    }
)
ax \= scores.plot.kde(legend\=True)
ax.set\_xlabel("Accuracy score")
ax.set\_xlim(\[0, 0.7\])
\_ \= ax.set\_title(
    "Density of the accuracy scores for the different multiclass strategies"
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Density of the accuracy scores for the different multiclass strategies](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_002.png)

We can see that once the hyperparameters are optimized, all multiclass strategies have similar performance as discussed in [\[3\]](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#id7)
.

Conclusion[#](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#conclusion "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

We can get some intuition behind those results.

First, the reason for which one-vs-one and error-correcting output code are outperforming the tree when the hyperparameters are not optimized relies on fact that they ensemble a larger number of classifiers. The ensembling improves the generalization performance. This is a bit similar why a bagging classifier generally performs better than a single decision tree if no care is taken to optimize the hyperparameters.

Then, we see the importance of optimizing the hyperparameters. Indeed, it should be regularly explored when developing predictive models even if techniques such as ensembling help at reducing this impact.

Finally, it is important to recall that the estimators in scikit-learn are developed with a specific strategy to handle multiclass classification out of the box. So for these estimators, it means that there is no need to use different strategies. These strategies are mainly useful for third-party estimators supporting only binary classification. In all cases, we also show that the hyperparameters should be optimized.

References[#](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html#references "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

**Total running time of the script:** (0 minutes 21.050 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo24.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/multiclass/plot_multiclass_overview.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo24.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/multiclass/plot_multiclass_overview.ipynb)

[`Download Jupyter notebook: plot_multiclass_overview.ipynb`](https://scikit-learn.org/stable/_downloads/917c94a6c4500bbf4185faeba5504398/plot_multiclass_overview.ipynb)

[`Download Python source code: plot_multiclass_overview.py`](https://scikit-learn.org/stable/_downloads/6ab77a144e3d99c2ecfc30e7fb84ed8e/plot_multiclass_overview.py)

[`Download zipped: plot_multiclass_overview.zip`](https://scikit-learn.org/stable/_downloads/3e3ff82825c1590c99d9a44b3a517f55/plot_multiclass_overview.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_thumb.png)

[Nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Nested versus non-nested cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_thumb.png)

[Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_thumb.png)

[Multilabel classification using a classifier chain](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Multilabel classification using a classifier chain

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/6ab77a144e3d99c2ecfc30e7fb84ed8e/plot_multiclass_overview.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/917c94a6c4500bbf4185faeba5504398/plot_multiclass_overview.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3e3ff82825c1590c99d9a44b3a517f55/plot_multiclass_overview.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo24.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/multiclass/plot_multiclass_overview.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo24.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/multiclass/plot_multiclass_overview.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)