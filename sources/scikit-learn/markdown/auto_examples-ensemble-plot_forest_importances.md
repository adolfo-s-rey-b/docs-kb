[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_forest_importances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_forest_importances.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_forest_importances.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_forest_importances.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_forest_importances.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_forest_importances.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#sphx-glr-download-auto-examples-ensemble-plot-forest-importances-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Feature importances with a forest of trees[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importances-with-a-forest-of-trees "Link to this heading")

=====================================================================================================================================================================================================

This example shows the use of a forest of trees to evaluate the importance of features on an artificial classification task. The blue bars are the feature importances of the forest, along with their inter-trees variability represented by the error bars.

As expected, the plot suggests that 3 features are informative, while the remaining are not.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

Copy to clipboard

Data generation and model fitting[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#data-generation-and-model-fitting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We generate a synthetic dataset with only 3 informative features. We will explicitly not shuffle the dataset to ensure that the informative features will correspond to the three first columns of X. In addition, we will split our dataset into training and testing subsets.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=1000,
    n\_features\=10,
    n\_informative\=3,
    n\_redundant\=0,
    n\_repeated\=0,
    n\_classes\=2,
    random\_state\=0,
    shuffle\=False,
)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=42)

Copy to clipboard

A random forest classifier will be fitted to compute the feature importances.

from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

feature\_names \= \[f"feature {i}" for i in range(X.shape\[1\])\]
forest \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=0)
forest.fit(X\_train, y\_train)

Copy to clipboard

RandomForestClassifier(random\_state=0)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

RandomForestClassifier

[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |
|     | [criterion criterion: {"gini", "entropy", "log\_loss"}, default="gini"  <br>  <br>The function to measure the quality of a split. Supported criteria are  <br>"gini" for the Gini impurity and "log\_loss" and "entropy" both for the  <br>Shannon information gain, see :ref:\`tree\_mathematical\_formulation\`.  <br>Note: This parameter is tree-specific.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'gini' |
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |
|     | [max\_features max\_features: {"sqrt", "log2", None}, int or float, default="sqrt"  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>.. versionchanged:: 1.1  <br>The default of \`max\_features\` changed from \`"auto"\` to \`"sqrt"\`.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D%22sqrt%22) | 'sqrt' |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |
|     | [bootstrap bootstrap: bool, default=True  <br>  <br>Whether bootstrap samples are used when building trees. If False, the  <br>whole dataset is used to build each tree.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | True |
|     | [oob\_score oob\_score: bool or callable, default=False  <br>  <br>Whether to use out-of-bag samples to estimate the generalization score.  <br>By default, :func:\`~sklearn.metrics.accuracy\_score\` is used.  <br>Provide a callable with signature \`metric(y\_true, y\_pred)\` to use a  <br>custom metric. Only available if \`bootstrap=True\`.  <br>  <br>For an illustration of out-of-bag (OOB) error estimation, see the example  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_ensemble\_oob.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`predict\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,) or a list of such arrays  <br>  <br>The classes labels (single output problem), or a list of arrays of  <br>class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20a%20list%20of%20such%20arrays) | ndarray\[int64\](2,) | \[0,1\] |
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeClassifier\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeClassifier) | DecisionTreeClassifier | DecisionTreeClassifier() |
| [estimators\_ estimators\_: list of DecisionTreeClassifier  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_,-list%20of%20DecisionTreeClassifier) | list | \[DecisionTreeC...ate=209652396), DecisionTreeC...ate=398764591), DecisionTreeC...ate=924231285), DecisionTreeC...te=1478610112), ...\] |
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[236, 2..., dtype=int32), array(\[107, 1..., dtype=int32), array(\[301, 5..., dtype=int32), array(\[357, 1..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](10,) | \[0.21,0.32,0.2 ,...,0.04,0.04,0.04\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 2   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 10  |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
Feature importance based on mean decrease in impurity[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importance-based-on-mean-decrease-in-impurity "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Feature importances are provided by the fitted attribute `feature_importances_` and they are computed as the mean and standard deviation of accumulation of the impurity decrease within each tree.\
\
Warning\
\
Impurity-based feature importances can be misleading for **high cardinality** features (many unique values). See [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance)\
 as an alternative below.\
\
import time\
\
import numpy as np\
\
start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")\
()\
importances \= forest.feature\_importances\_\
std \= [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")\
(\[tree.feature\_importances\_ for tree in forest.estimators\_\], axis\=0)\
elapsed\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")\
() \- start\_time\
\
print(f"Elapsed time to compute the importances: {elapsed\_time:.3f} seconds")\
\
Copy to clipboard\
\
Elapsed time to compute the importances: 0.015 seconds\
\
Copy to clipboard\
\
Let’s plot the impurity-based importance.\
\
import pandas as pd\
\
forest\_importances \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")\
(importances, index\=feature\_names)\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
forest\_importances.plot.bar(yerr\=std, ax\=ax)\
ax.set\_title("Feature importances using MDI")\
ax.set\_ylabel("Mean decrease in impurity")\
fig.tight\_layout()\
\
Copy to clipboard\
\
![Feature importances using MDI](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_001.png)\
\
We observe that, as expected, the three first features are found important.\
\
Feature importance based on feature permutation[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importance-based-on-feature-permutation "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Permutation feature importance overcomes limitations of the impurity-based feature importance: they do not have a bias toward high-cardinality features and can be computed on a left-out test set.\
\
from sklearn.inspection import [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
\
start\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")\
()\
result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
(\
    forest, X\_test, y\_test, n\_repeats\=10, random\_state\=42, n\_jobs\=2\
)\
elapsed\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")\
() \- start\_time\
print(f"Elapsed time to compute the importances: {elapsed\_time:.3f} seconds")\
\
forest\_importances \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")\
(result.importances\_mean, index\=feature\_names)\
\
Copy to clipboard\
\
Elapsed time to compute the importances: 1.258 seconds\
\
Copy to clipboard\
\
The computation for full permutation importance is more costly. Each feature is shuffled n times and the model is used to make predictions on the permuted data to see the drop in performance. Please see [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance)\
 for more details. We can now plot the importance ranking.\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
forest\_importances.plot.bar(yerr\=result.importances\_std, ax\=ax)\
ax.set\_title("Feature importances using permutation on full model")\
ax.set\_ylabel("Mean accuracy decrease")\
fig.tight\_layout()\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![Feature importances using permutation on full model](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_002.png)\
\
The same features are detected as most important using both methods. Although the relative importances vary. As seen on the plots, MDI is less likely than permutation importance to fully omit a feature.\
\
**Total running time of the script:** (0 minutes 1.838 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_forest_importances.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_importances.ipynb)\
\
[`Download Jupyter notebook: plot_forest_importances.ipynb`](https://scikit-learn.org/stable/_downloads/5e3b69cd18b43dd31a46a35ccba413e7/plot_forest_importances.ipynb)\
\
[`Download Python source code: plot_forest_importances.py`](https://scikit-learn.org/stable/_downloads/74c6ab6570af7f9379b15af6a1323943/plot_forest_importances.py)\
\
[`Download zipped: plot_forest_importances.zip`](https://scikit-learn.org/stable/_downloads/175dc7cd79fedbe3d38829513430275a/plot_forest_importances.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)\
\
[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)\
\
Permutation Importance vs Random Forest Feature Importance (MDI)\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)\
\
[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)\
\
Permutation Importance with Multicollinear or Correlated Features\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)\
\
[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)\
\
Gradient Boosting regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)\
\
Release Highlights for scikit-learn 0.22\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/74c6ab6570af7f9379b15af6a1323943/plot_forest_importances.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/5e3b69cd18b43dd31a46a35ccba413e7/plot_forest_importances.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/175dc7cd79fedbe3d38829513430275a/plot_forest_importances.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_importances.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_forest_importances.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)