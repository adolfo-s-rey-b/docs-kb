[Skip to main content](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/tree/plot_tree_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/tree/plot_tree_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/tree/plot_tree_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/tree/plot_tree_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/tree/plot_tree_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/tree/plot_tree_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-download-auto-examples-tree-plot-tree-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Decision Tree Regression[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#decision-tree-regression "Link to this heading")

==========================================================================================================================================================

In this example, we demonstrate the effect of changing the maximum depth of a decision tree on how it fits to the data. We perform this once on a 1D regression task and once on a multi-output regression task.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Decision Tree on a 1D Regression Task[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#decision-tree-on-a-1d-regression-task "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we fit a tree on a 1D regression task.

The [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)
 is used to fit a sine curve with addition noisy observation. As a result, it learns local linear regressions approximating the sine curve.

We can see that if the maximum depth of the tree (controlled by the `max_depth` parameter) is set too high, the decision trees learn too fine details of the training data and learn from the noise, i.e. they overfit.

### Create a random 1D dataset[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#create-a-random-1d-dataset "Link to this heading")

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(5 \* rng.rand(80, 1), axis\=0)
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X).ravel()
y\[::5\] += 3 \* (0.5 \- rng.rand(16))

Copy to clipboard

### Fit regression model[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#fit-regression-model "Link to this heading")

Here we fit two models with different maximum depths

from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

regr\_1 \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=2)
regr\_2 \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=5)
regr\_1.fit(X, y)
regr\_2.fit(X, y)

Copy to clipboard

DecisionTreeRegressor(max\_depth=5)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

DecisionTreeRegressor

[?Documentation for DecisionTreeRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.  <br>  <br>For an example of how \`\`max\_depth\`\` influences the model, see  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_tree\_regression.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_depth,-int%2C%20default%3DNone) | 5   |
|     | [criterion criterion: {"squared\_error", "absolute\_error", "poisson"}, default="squared\_error"  <br>  <br>The function to measure the quality of a split. Supported criteria  <br>are "squared\_error" for the mean squared error, which is equal to  <br>variance reduction as feature selection criterion and minimizes the L2  <br>loss using the mean of each terminal node, "absolute\_error" for the mean  <br>absolute error, which minimizes the L1 loss using the median of each terminal  <br>node, and "poisson" which uses reduction in Poisson deviance to find splits,  <br>also using the mean of each terminal node.  <br>  <br>.. versionadded:: 0.18  <br>Mean Absolute Error (MAE) criterion.  <br>  <br>.. versionadded:: 0.24  <br>Poisson deviance criterion.  <br>  <br>.. versionchanged:: 1.9  <br>Criterion \`"friedman\_mse"\` was deprecated.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=criterion,-%7B%22squared_error%22%2C%20%22absolute_error%22%2C%20%22poisson%22%7D%2C%20default%3D%22squared_error%22) | 'squared\_error' |
|     | [splitter splitter: {"best", "random"}, default="best"  <br>  <br>The strategy used to choose the split at each node. Supported  <br>strategies are "best" to choose the best split and "random" to choose  <br>the best random split among considered features for this split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=splitter,-%7B%22best%22%2C%20%22random%22%7D%2C%20default%3D%22best%22) | 'best' |
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |
|     | [max\_features max\_features: int, float or {"sqrt", "log2"}, default=None  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>Note: splitting may inspect more than \`\`max\_features\`\` features if  <br>needed to find a valid split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_features,-int%2C%20float%20or%20%7B%22sqrt%22%2C%20%22log2%22%7D%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the randomness of the estimator. The features are always  <br>randomly permuted at each split, even if \`\`splitter\`\` is set to  <br>\`\`"best"\`\`. When \`\`max\_features < n\_features\`\`, the algorithm will  <br>select \`\`max\_features\`\` at random at each split before finding the best  <br>split among them. But the best found split may vary across different  <br>runs, even if \`\`max\_features=n\_features\`\`. That is the case, if the  <br>improvement of the criterion is identical for several splits and one  <br>split has to be selected at random. To obtain a deterministic behaviour  <br>during fitting, \`\`random\_state\`\` has to be fixed to an integer.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow a tree with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multioutput regressions (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the  <br>(normalized) total reduction of the criterion brought  <br>by that feature. It is also known as the Gini importance \[4\]\_.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](1,) | \[1.\] |
| [max\_features\_ max\_features\_: int  <br>  <br>The inferred value of max\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_features_,-int) | int | 1   |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=n_features_in_,-int) | int | 1   |
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=n_outputs_,-int) | int | 1   |
| [tree\_ tree\_: Tree instance  <br>  <br>The underlying Tree object. Please refer to  <br>\`\`help(sklearn.tree.\_tree.Tree)\`\` for attributes of Tree object and  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_unveil\_tree\_structure.py\`  <br>for basic usage of these attributes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=tree_,-Tree%20instance) | Tree | <sklearn.tree...x7e1dbd643600> |

  
  

### Predict[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#predict "Link to this heading")

Get predictions on the test set

X\_test \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 5.0, 0.01)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
y\_1 \= regr\_1.predict(X\_test)
y\_2 \= regr\_2.predict(X\_test)

Copy to clipboard

### Plot the results[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#plot-the-results "Link to this heading")

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X, y, s\=20, edgecolor\="black", c\="darkorange", label\="data")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_1, color\="cornflowerblue", label\="max\_depth=2", linewidth\=2)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_2, color\="yellowgreen", label\="max\_depth=5", linewidth\=2)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Decision Tree Regression")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Decision Tree Regression](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png)

As you can see, the model with a depth of 5 (yellow) learns the details of the training data to the point that it overfits to the noise. On the other hand, the model with a depth of 2 (blue) learns the major tendencies in the data well and does not overfit. In real use cases, you need to make sure that the tree is not overfitting the training data, which can be done using cross-validation.

Decision Tree Regression with Multi-Output Targets[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#decision-tree-regression-with-multi-output-targets "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here the [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)
 is used to predict simultaneously the noisy `x` and `y` observations of a circle given a single underlying feature. As a result, it learns local linear regressions approximating the circle.

We can see that if the maximum depth of the tree (controlled by the `max_depth` parameter) is set too high, the decision trees learn too fine details of the training data and learn from the noise, i.e. they overfit.

### Create a random dataset[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#create-a-random-dataset "Link to this heading")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(200 \* rng.rand(100, 1) \- 100, axis\=0)
y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")\
(X).ravel(), [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")\
(X).ravel()\]).T
y\[::5, :\] += 0.5 \- rng.rand(20, 2)

Copy to clipboard

### Fit regression model[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#id1 "Link to this heading")

regr\_1 \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=2)
regr\_2 \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=5)
regr\_3 \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=8)
regr\_1.fit(X, y)
regr\_2.fit(X, y)
regr\_3.fit(X, y)

Copy to clipboard

DecisionTreeRegressor(max\_depth=8)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

DecisionTreeRegressor

[?Documentation for DecisionTreeRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.  <br>  <br>For an example of how \`\`max\_depth\`\` influences the model, see  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_tree\_regression.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_depth,-int%2C%20default%3DNone) | 8   |
|     | [criterion criterion: {"squared\_error", "absolute\_error", "poisson"}, default="squared\_error"  <br>  <br>The function to measure the quality of a split. Supported criteria  <br>are "squared\_error" for the mean squared error, which is equal to  <br>variance reduction as feature selection criterion and minimizes the L2  <br>loss using the mean of each terminal node, "absolute\_error" for the mean  <br>absolute error, which minimizes the L1 loss using the median of each terminal  <br>node, and "poisson" which uses reduction in Poisson deviance to find splits,  <br>also using the mean of each terminal node.  <br>  <br>.. versionadded:: 0.18  <br>Mean Absolute Error (MAE) criterion.  <br>  <br>.. versionadded:: 0.24  <br>Poisson deviance criterion.  <br>  <br>.. versionchanged:: 1.9  <br>Criterion \`"friedman\_mse"\` was deprecated.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=criterion,-%7B%22squared_error%22%2C%20%22absolute_error%22%2C%20%22poisson%22%7D%2C%20default%3D%22squared_error%22) | 'squared\_error' |
|     | [splitter splitter: {"best", "random"}, default="best"  <br>  <br>The strategy used to choose the split at each node. Supported  <br>strategies are "best" to choose the best split and "random" to choose  <br>the best random split among considered features for this split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=splitter,-%7B%22best%22%2C%20%22random%22%7D%2C%20default%3D%22best%22) | 'best' |
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |
|     | [max\_features max\_features: int, float or {"sqrt", "log2"}, default=None  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>Note: splitting may inspect more than \`\`max\_features\`\` features if  <br>needed to find a valid split.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_features,-int%2C%20float%20or%20%7B%22sqrt%22%2C%20%22log2%22%7D%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the randomness of the estimator. The features are always  <br>randomly permuted at each split, even if \`\`splitter\`\` is set to  <br>\`\`"best"\`\`. When \`\`max\_features < n\_features\`\`, the algorithm will  <br>select \`\`max\_features\`\` at random at each split before finding the best  <br>split among them. But the best found split may vary across different  <br>runs, even if \`\`max\_features=n\_features\`\`. That is the case, if the  <br>improvement of the criterion is identical for several splits and one  <br>split has to be selected at random. To obtain a deterministic behaviour  <br>during fitting, \`\`random\_state\`\` has to be fixed to an integer.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow a tree with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multioutput regressions (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the  <br>(normalized) total reduction of the criterion brought  <br>by that feature. It is also known as the Gini importance \[4\]\_.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](1,) | \[1.\] |
| [max\_features\_ max\_features\_: int  <br>  <br>The inferred value of max\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=max_features_,-int) | int | 1   |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=n_features_in_,-int) | int | 1   |
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=n_outputs_,-int) | int | 2   |
| [tree\_ tree\_: Tree instance  <br>  <br>The underlying Tree object. Please refer to  <br>\`\`help(sklearn.tree.\_tree.Tree)\`\` for attributes of Tree object and  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_unveil\_tree\_structure.py\`  <br>for basic usage of these attributes.](https://scikit-learn.org/1.9/modules/generated/sklearn.tree.DecisionTreeRegressor.html#:~:text=tree_,-Tree%20instance) | Tree | <sklearn.tree...x7e1dbd641530> |

  
  

### Predict[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#id2 "Link to this heading")

Get predictions on the test set

X\_test \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-100.0, 100.0, 0.01)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
y\_1 \= regr\_1.predict(X\_test)
y\_2 \= regr\_2.predict(X\_test)
y\_3 \= regr\_3.predict(X\_test)

Copy to clipboard

### Plot the results[#](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#id3 "Link to this heading")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
s \= 25
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(y\[:, 0\], y\[:, 1\], c\="yellow", s\=s, edgecolor\="black", label\="data")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    y\_1\[:, 0\],
    y\_1\[:, 1\],
    c\="cornflowerblue",
    s\=s,
    edgecolor\="black",
    label\="max\_depth=2",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(y\_2\[:, 0\], y\_2\[:, 1\], c\="red", s\=s, edgecolor\="black", label\="max\_depth=5")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(y\_3\[:, 0\], y\_3\[:, 1\], c\="blue", s\=s, edgecolor\="black", label\="max\_depth=8")
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\[\-6, 6\])
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\[\-6, 6\])
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("target 1")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target 2")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Multi-output Decision Tree Regression")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Multi-output Decision Tree Regression](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_002.png)

As you can see, the higher the value of `max_depth`, the more details of the data are caught by the model. However, the model also overfits to the data and is influenced by the noise.

**Total running time of the script:** (0 minutes 0.322 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_tree_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_tree_regression.ipynb)

[`Download Jupyter notebook: plot_tree_regression.ipynb`](https://scikit-learn.org/stable/_downloads/ad1c1da0830674700828e658b74f6cf6/plot_tree_regression.ipynb)

[`Download Python source code: plot_tree_regression.py`](https://scikit-learn.org/stable/_downloads/1fda803e152cdabd5ad21330d93e1258/plot_tree_regression.py)

[`Download zipped: plot_tree_regression.zip`](https://scikit-learn.org/stable/_downloads/82643d7dc9e517c462b1325c8c1c93a5/plot_tree_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)

[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)

Decision Tree Regression with AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_regression_multioutput_thumb.png)

[Comparing random forests and the multi-output meta estimator](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)

Comparing random forests and the multi-output meta estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/1fda803e152cdabd5ad21330d93e1258/plot_tree_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ad1c1da0830674700828e658b74f6cf6/plot_tree_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/82643d7dc9e517c462b1325c8c1c93a5/plot_tree_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_tree_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_tree_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)