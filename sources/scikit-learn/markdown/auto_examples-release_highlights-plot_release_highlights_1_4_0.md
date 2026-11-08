[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-4-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.4[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#release-highlights-for-scikit-learn-1-4 "Link to this heading")

===============================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 1.4! Many bug fixes and improvements were added, as well as some new key features. We detail below a few of the major features of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.4.html#release-notes-1-4)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

HistGradientBoosting Natively Supports Categorical DTypes in DataFrames[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#histgradientboosting-natively-supports-categorical-dtypes-in-dataframes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 now directly supports dataframes with categorical features. Here we have a dataset with a mixture of categorical and numerical features:

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

X\_adult, y\_adult \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("adult", version\=2, return\_X\_y\=True)

\# Remove redundant and non-feature columns
X\_adult \= X\_adult.drop(\["education-num", "fnlwgt"\], axis\="columns")
X\_adult.dtypes

Copy to clipboard

age                  int64
workclass         category
education         category
marital-status    category
occupation        category
relationship      category
race              category
sex               category
capital-gain         int64
capital-loss         int64
hours-per-week       int64
native-country    category
dtype: object

Copy to clipboard

By setting `categorical_features="from_dtype"`, the gradient boosting classifier treats the columns with categorical dtypes as categorical features in the algorithm:

from sklearn.ensemble import [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
from sklearn.metrics import [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X\_adult, y\_adult, random\_state\=0)
hist \= [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
(categorical\_features\="from\_dtype")

hist.fit(X\_train, y\_train)
y\_decision \= hist.decision\_function(X\_test)
print(f"ROC AUC score is {[roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(y\_test, y\_decision)}")

Copy to clipboard

ROC AUC score is 0.9283274410427749

Copy to clipboard

Polars output in `set_output`[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#polars-output-in-set-output "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

scikit-learn’s transformers now support polars output with the `set_output` API.

import polars as pl

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

df \= pl.DataFrame(
    {"height": \[120, 140, 150, 110, 100\], "pet": \["dog", "cat", "dog", "cat", "cat"\]}
)
preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        ("numerical", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), \["height"\]),\
        ("categorical", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(sparse\_output\=False), \["pet"\]),\
    \],
    verbose\_feature\_names\_out\=False,
)
preprocessor.set\_output(transform\="polars")

df\_out \= preprocessor.fit\_transform(df)
df\_out

Copy to clipboard

shape: (5, 3)

| height | pet\_cat | pet\_dog |
| --- | --- | --- |
| f64 | f64 | f64 |
| --- | --- | --- |
| \-0.215666 | 0.0 | 1.0 |
| 0.862662 | 1.0 | 0.0 |
| 1.401826 | 0.0 | 1.0 |
| \-0.754829 | 1.0 | 0.0 |
| \-1.293993 | 1.0 | 0.0 |

  
  

print(f"Output type: {type(df\_out)}")

Copy to clipboard

Output type: <class 'polars.dataframe.frame.DataFrame'>

Copy to clipboard

Missing value support for Random Forest[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#missing-value-support-for-random-forest "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The classes [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 and [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
 now support missing values. When training every individual tree, the splitter evaluates each potential threshold with the missing values going to the left and right nodes. More details in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#tree-missing-value-support)
.

import numpy as np

from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1, 6, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\]).reshape(\-1, 1)
y \= \[0, 0, 1, 1\]

forest \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=0).fit(X, y)
forest.predict(X)

Copy to clipboard

array(\[0, 0, 1, 1\])

Copy to clipboard

Add support for monotonic constraints in tree-based models[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#add-support-for-monotonic-constraints-in-tree-based-models "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While we added support for monotonic constraints in histogram-based gradient boosting in scikit-learn 0.23, we now support this feature for all other tree-based models as trees, random forests, extra-trees, and exact gradient boosting. Here, we show this feature for random forest on a regression problem.

import matplotlib.pyplot as plt

from sklearn.ensemble import [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
from sklearn.inspection import PartialDependenceDisplay

n\_samples \= 500
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X \= rng.randn(n\_samples, 2)
noise \= rng.normal(loc\=0.0, scale\=0.01, size\=n\_samples)
y \= 5 \* X\[:, 0\] + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(10 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* X\[:, 0\]) \- noise

rf\_no\_cst \= [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
().fit(X, y)
rf\_cst \= [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
(monotonic\_cst\=\[1, 0\]).fit(X, y)

disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    rf\_no\_cst,
    X,
    features\=\[0\],
    feature\_names\=\["feature 0"\],
    line\_kw\={"linewidth": 4, "label": "unconstrained", "color": "tab:blue"},
)
[PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    rf\_cst,
    X,
    features\=\[0\],
    line\_kw\={"linewidth": 4, "label": "constrained", "color": "tab:orange"},
    ax\=disp.axes\_,
)
disp.axes\_\[0, 0\].plot(
    X\[:, 0\], y, "o", alpha\=0.5, zorder\=-1, label\="samples", color\="tab:green"
)
disp.axes\_\[0, 0\].set\_ylim(\-3, 3)
disp.axes\_\[0, 0\].set\_xlim(\-1, 1)
disp.axes\_\[0, 0\].legend()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot release highlights 1 4 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_001.png)

Enriched estimator displays[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#enriched-estimator-displays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Estimators displays have been enriched: if we look at `forest`, defined above:

forest

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
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[0, 3, ..., dtype=int32), array(\[3, 1, ..., dtype=int32), array(\[1, 3, ..., dtype=int32), array(\[0, 1, ..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](1,) | \[1.\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 2   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
One can access the documentation of the estimator by clicking on the icon “?” on the top right corner of the diagram.\
\
In addition, the display changes color, from orange to blue, when the estimator is fitted. You can also get this information by hovering on the icon “i”.\
\
from sklearn.base import clone\
\
clone(forest)  \# the clone is not fitted\
\
Copy to clipboard\
\
RandomForestClassifier(random\_state=0)\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
RandomForestClassifier\
\
[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)\
iNot fitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |\
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |\
|     | [criterion criterion: {"gini", "entropy", "log\_loss"}, default="gini"  <br>  <br>The function to measure the quality of a split. Supported criteria are  <br>"gini" for the Gini impurity and "log\_loss" and "entropy" both for the  <br>Shannon information gain, see :ref:\`tree\_mathematical\_formulation\`.  <br>Note: This parameter is tree-specific.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'gini' |\
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |\
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |\
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |\
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_features max\_features: {"sqrt", "log2", None}, int or float, default="sqrt"  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>.. versionchanged:: 1.1  <br>The default of \`max\_features\` changed from \`"auto"\` to \`"sqrt"\`.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D%22sqrt%22) | 'sqrt' |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |\
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |\
|     | [bootstrap bootstrap: bool, default=True  <br>  <br>Whether bootstrap samples are used when building trees. If False, the  <br>whole dataset is used to build each tree.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | True |\
|     | [oob\_score oob\_score: bool or callable, default=False  <br>  <br>Whether to use out-of-bag samples to estimate the generalization score.  <br>By default, :func:\`~sklearn.metrics.accuracy\_score\` is used.  <br>Provide a callable with signature \`metric(y\_true, y\_pred)\` to use a  <br>custom metric. Only available if \`bootstrap=True\`.  <br>  <br>For an illustration of out-of-bag (OOB) error estimation, see the example  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_ensemble\_oob.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`predict\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |\
\
  \
  \
\
Metadata Routing Support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#metadata-routing-support "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Many meta-estimators and cross-validation routines now support metadata routing, which are listed in the [user guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing-models)\
. For instance, this is how you can do a nested cross-validation with sample weights and [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")\
:\
\
import sklearn\
from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")\
from sklearn.linear\_model import [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")\
from sklearn.metrics import [get\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")\
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
, [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")\
, [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
\
\# For now by default metadata routing is disabled, and need to be explicitly\
\# enabled.\
[sklearn.set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
(enable\_metadata\_routing\=True)\
\
n\_samples \= 100\
X, y \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")\
(n\_samples\=n\_samples, n\_features\=5, noise\=0.5)\
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
(7)\
groups \= rng.randint(0, 10, size\=n\_samples)\
sample\_weights \= rng.rand(n\_samples)\
estimator \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")\
().set\_fit\_request(sample\_weight\=True)\
hyperparameter\_grid \= {"alpha": \[0.1, 0.5, 1.0, 2.0\]}\
scoring\_inner\_cv \= [get\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")\
("neg\_mean\_squared\_error").set\_score\_request(\
    sample\_weight\=True\
)\
inner\_cv \= [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")\
(n\_splits\=5)\
\
grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
(\
    estimator\=estimator,\
    param\_grid\=hyperparameter\_grid,\
    cv\=inner\_cv,\
    scoring\=scoring\_inner\_cv,\
)\
\
outer\_cv \= [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")\
(n\_splits\=5)\
scorers \= {\
    "mse": [get\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")\
("neg\_mean\_squared\_error").set\_score\_request(sample\_weight\=True)\
}\
results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
(\
    grid\_search,\
    X,\
    y,\
    cv\=outer\_cv,\
    scoring\=scorers,\
    return\_estimator\=True,\
    params\={"sample\_weight": sample\_weights, "groups": groups},\
)\
print("cv error on test sets:", results\["test\_mse"\])\
\
\# Setting the flag to the default \`False\` to avoid interference with other\
\# scripts.\
[sklearn.set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
(enable\_metadata\_routing\=False)\
\
Copy to clipboard\
\
cv error on test sets: \[-0.52177476 -0.27491256 -0.41796353 -0.50465614 -0.35808885\]\
\
Copy to clipboard\
\
Improved memory and runtime efficiency for PCA on sparse data[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#improved-memory-and-runtime-efficiency-for-pca-on-sparse-data "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
PCA is now able to handle sparse matrices natively for the `arpack` solver by levaraging `scipy.sparse.linalg.LinearOperator` to avoid materializing large sparse matrices when performing the eigenvalue decomposition of the data set covariance matrix.\
\
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
\
import scipy.sparse as sp\
\
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
\
X\_sparse \= [sp.random](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.random.html#scipy.sparse.random "scipy.sparse.random")\
(m\=1000, n\=1000, random\_state\=0)\
X\_dense \= X\_sparse.toarray()\
\
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
()\
[PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(n\_components\=10, svd\_solver\="arpack").fit(X\_sparse)\
time\_sparse \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
() \- t0\
\
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
()\
[PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(n\_components\=10, svd\_solver\="arpack").fit(X\_dense)\
time\_dense \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")\
() \- t0\
\
print(f"Speedup: {time\_dense / time\_sparse:.1f}x")\
\
Copy to clipboard\
\
Speedup: 3.7x\
\
Copy to clipboard\
\
**Total running time of the script:** (0 minutes 2.006 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_4_0.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_4_0.ipynb)\
\
[`Download Jupyter notebook: plot_release_highlights_1_4_0.ipynb`](https://scikit-learn.org/stable/_downloads/53490cdb42c3c07ba8cccd1c4ed4dca4/plot_release_highlights_1_4_0.ipynb)\
\
[`Download Python source code: plot_release_highlights_1_4_0.py`](https://scikit-learn.org/stable/_downloads/c15cce0dbcd8722cb5638987eff985c0/plot_release_highlights_1_4_0.py)\
\
[`Download zipped: plot_release_highlights_1_4_0.zip`](https://scikit-learn.org/stable/_downloads/f170f118a3121751597248ab2244e237/plot_release_highlights_1_4_0.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)\
\
Release Highlights for scikit-learn 0.23\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)\
\
Release Highlights for scikit-learn 1.2\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)\
\
Release Highlights for scikit-learn 1.7\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)\
\
Release Highlights for scikit-learn 1.3\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/c15cce0dbcd8722cb5638987eff985c0/plot_release_highlights_1_4_0.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/53490cdb42c3c07ba8cccd1c4ed4dca4/plot_release_highlights_1_4_0.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/f170f118a3121751597248ab2244e237/plot_release_highlights_1_4_0.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_4_0.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_4_0.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)