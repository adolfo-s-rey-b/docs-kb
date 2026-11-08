[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_voting_regressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_voting_regressor.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_voting_regressor.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_voting_regressor.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_voting_regressor.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_voting_regressor.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html#sphx-glr-download-auto-examples-ensemble-plot-voting-regressor-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot individual and voting regression predictions[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html#plot-individual-and-voting-regression-predictions "Link to this heading")

=================================================================================================================================================================================================================

A voting regressor is an ensemble meta-estimator that fits several base regressors, each on the whole dataset. Then it averages the individual predictions to form a final prediction. We will use three different regressors to predict the data: [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
, [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
, and [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
). Then the above 3 regressors will be used for the [`VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
.

Finally, we will plot the predictions made by all models for comparison.

We will work with the diabetes dataset which consists of 10 features collected from a cohort of diabetes patients. The target is a quantitative measure of disease progression one year after baseline.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
from sklearn.ensemble import (
    [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
,
    [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
,
    [VotingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
,
)
from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")

Copy to clipboard

Training classifiers[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html#training-classifiers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

First, we will load the diabetes dataset and initiate a gradient boosting regressor, a random forest regressor and a linear regression. Next, we will use the 3 regressors to build the voting regressor:

X, y \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True)

\# Train classifiers
reg1 \= [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(random\_state\=1)
reg2 \= [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
(random\_state\=1)
reg3 \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg \= [VotingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
(\[("gb", reg1), ("rf", reg2), ("lr", reg3)\])
ereg.fit(X, y)

Copy to clipboard

VotingRegressor(estimators=\[('gb', GradientBoostingRegressor(random\_state=1)),\
                            ('rf', RandomForestRegressor(random\_state=1)),\
                            ('lr', LinearRegression())\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

VotingRegressor

[?Documentation for VotingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimators estimators: list of (str, estimator) tuples  <br>  <br>Invoking the \`\`fit\`\` method on the \`\`VotingRegressor\`\` will fit clones  <br>of those original estimators that will be stored in the class attribute  <br>\`\`self.estimators\_\`\`. An estimator can be set to \`\`'drop'\`\` using  <br>:meth:\`set\_params\`.  <br>  <br>.. versionchanged:: 0.21  <br>\`\`'drop'\`\` is accepted. Using None was deprecated in 0.22 and  <br>support was removed in 0.24.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=estimators,-list%20of%20%28str%2C%20estimator%29%20tuples) | \[('gb', ...), ('rf', ...), ...\] |
|     | [weights weights: array-like of shape (n\_regressors,), default=None  <br>  <br>Sequence of weights (\`float\` or \`int\`) to weight the occurrences of  <br>predicted values before averaging. Uses uniform weights if \`None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=weights,-array-like%20of%20shape%20%28n_regressors%2C%29%2C%20default%3DNone) | None |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel for \`\`fit\`\`.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting will be printed as it  <br>is completed.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [estimators\_ estimators\_: list of regressors  <br>  <br>The collection of fitted sub-estimators as defined in \`\`estimators\`\`  <br>that are not 'drop'.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=estimators_,-list%20of%20regressors) | list | \[GradientBoost...andom\_state=1), RandomForestR...andom\_state=1), LinearRegression()\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying regressor exposes such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=n_features_in_,-int) | int | 10  |
| [named\_estimators\_ named\_estimators\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Attribute to access any fitted sub-estimators by name.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingRegressor.html#:~:text=named_estimators_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'gb': Gradie...rRegression()} |

gb

GradientBoostingRegressor

[?Documentation for GradientBoostingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the random seed given to each Tree estimator at each  <br>boosting iteration.  <br>In addition, it controls the random permutation of the features at  <br>each split (see Notes for more details).  <br>It also controls the random splitting of the training data to obtain a  <br>validation set if \`n\_iter\_no\_change\` is not None.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 1   |
|     | [loss loss: {'squared\_error', 'absolute\_error', 'huber', 'quantile'}, default='squared\_error'  <br>  <br>Loss function to be optimized. 'squared\_error' refers to the squared  <br>error for regression. 'absolute\_error' refers to the absolute error of  <br>regression and is a robust loss function. 'huber' is a  <br>combination of the two. 'quantile' allows quantile regression (use  <br>\`alpha\` to specify the quantile).  <br>See  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_quantile.py\`  <br>for an example that demonstrates quantile regression for creating  <br>prediction intervals with \`loss='quantile'\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27absolute_error%27%2C%20%27huber%27%2C%20%27quantile%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27squared_error%27) | 'squared\_error' |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>Learning rate shrinks the contribution of each tree by \`learning\_rate\`.  <br>There is a trade-off between learning\_rate and n\_estimators.  <br>Values must be in the range \`\[0.0, inf)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |\
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of boosting stages to perform. Gradient boosting  <br>is fairly robust to over-fitting so a large number usually  <br>results in better performance.  <br>Values must be in the range \`\[1, inf)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |\
|     | [subsample subsample: float, default=1.0  <br>  <br>The fraction of samples to be used for fitting the individual base  <br>learners. If smaller than 1.0 this results in Stochastic Gradient  <br>Boosting. \`subsample\` interacts with the parameter \`n\_estimators\`.  <br>Choosing \`subsample < 1.0\` leads to a reduction of variance  <br>and an increase in bias.  <br>Values must be in the range \`(0.0, 1.0\]\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=subsample,-float%2C%20default%3D1.0) | 1.0 |\
|     | [criterion criterion: {'friedman\_mse', 'squared\_error'}, default='friedman\_mse'  <br>  <br>This parameter has no effect.  <br>  <br>.. versionadded:: 0.18  <br>  <br>.. deprecated:: 1.9  <br>\`criterion\` is deprecated and will be removed in 1.11.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=criterion,-%7B%27friedman_mse%27%2C%20%27squared_error%27%7D%2C%20default%3D%27friedman_mse%27) | 'deprecated' |\
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, values must be in the range \`\[2, inf)\`.  <br>\- If float, values must be in the range \`(0.0, 1.0\]\` and \`min\_samples\_split\`  <br>will be \`ceil(min\_samples\_split \* n\_samples)\`.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |\
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, values must be in the range \`\[1, inf)\`.  <br>\- If float, values must be in the range \`(0.0, 1.0)\` and \`min\_samples\_leaf\`  <br>will be \`ceil(min\_samples\_leaf \* n\_samples)\`.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |\
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.  <br>Values must be in the range \`\[0.0, 0.5\]\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_depth max\_depth: int or None, default=3  <br>  <br>Maximum depth of the individual regression estimators. The maximum  <br>depth limits the number of nodes in the tree. Tune this parameter  <br>for best performance; the best value depends on the interaction  <br>of the input variables. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.  <br>If int, values must be in the range \`\[1, inf)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=max_depth,-int%20or%20None%2C%20default%3D3) | 3   |\
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>Values must be in the range \`\[0.0, inf)\`.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |\
|     | [init init: estimator or 'zero', default=None  <br>  <br>An estimator object that is used to compute the initial predictions.  <br>\`\`init\`\` has to provide :term:\`fit\` and :term:\`predict\`. If 'zero', the  <br>initial raw predictions are set to zero. By default a  <br>\`\`DummyEstimator\`\` is used, predicting either the average target value  <br>(for loss='squared\_error'), or a quantile for the other losses.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=init,-estimator%20or%20%27zero%27%2C%20default%3DNone) | None |\
|     | [max\_features max\_features: {'sqrt', 'log2'}, int or float, default=None  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, values must be in the range \`\[1, inf)\`.  <br>\- If float, values must be in the range \`(0.0, 1.0\]\` and the features  <br>considered at each split will be \`max(1, int(max\_features \* n\_features\_in\_))\`.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>Choosing \`max\_features < n\_features\` leads to a reduction of variance  <br>and an increase in bias.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=max_features,-%7B%27sqrt%27%2C%20%27log2%27%7D%2C%20int%20or%20float%2C%20default%3DNone) | None |\
|     | [alpha alpha: float, default=0.9  <br>  <br>The alpha-quantile of the huber loss function and the quantile  <br>loss function. Only if \`\`loss='huber'\`\` or \`\`loss='quantile'\`\`.  <br>Values must be in the range \`(0.0, 1.0)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=alpha,-float%2C%20default%3D0.9) | 0.9 |\
|     | [verbose verbose: int, default=0  <br>  <br>Enable verbose output. If 1 then it prints progress and performance  <br>once in a while (the more trees the lower the frequency). If greater  <br>than 1 then it prints progress and performance for every tree.  <br>Values must be in the range \`\[0, inf)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>Values must be in the range \`\[2, inf)\`.  <br>If None, then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just erase the  <br>previous solution. See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [validation\_fraction validation\_fraction: float, default=0.1  <br>  <br>The proportion of training data to set aside as validation set for  <br>early stopping. Values must be in the range \`(0.0, 1.0)\`.  <br>Only used if \`\`n\_iter\_no\_change\`\` is set to an integer.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=validation_fraction,-float%2C%20default%3D0.1) | 0.1 |\
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=None  <br>  <br>\`\`n\_iter\_no\_change\`\` is used to decide if early stopping will be used  <br>to terminate training when validation score is not improving. By  <br>default it is set to None to disable early stopping. If set to a  <br>number, it will set aside \`\`validation\_fraction\`\` size of the training  <br>data as validation and terminate training when validation score is not  <br>improving in all of the previous \`\`n\_iter\_no\_change\`\` numbers of  <br>iterations.  <br>Values must be in the range \`\[1, inf)\`.  <br>See  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_early\_stopping.py\`.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3DNone) | None |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for the early stopping. When the loss is not improving  <br>by at least tol for \`\`n\_iter\_no\_change\`\` iterations (if set to a  <br>number), the training stops.  <br>Values must be in the range \`\[0.0, inf)\`.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed.  <br>Values must be in the range \`\[0.0, inf)\`.  <br>See :ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [estimators\_ estimators\_: ndarray of DecisionTreeRegressor of shape (n\_estimators, 1)  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=estimators_,-int) | ndarray\[object\](100, 1) | \[\[DecisionTreeRegressor(max\_depth=3, random\_state=RandomState(MT19937) at 0x7E1D96200440)\], \[DecisionTreeRegressor(max\_depth=3, random\_state=RandomState(MT19937) at 0x7E1D96200440)\], \[DecisionTreeRegressor(max\_depth=3, random\_state=RandomState(MT19937) at 0x7E1D96200440)\], ..., \[DecisionTreeRegressor(max\_depth=3, random\_state=RandomState(MT19937) at 0x7E1D96200440)\], \[DecisionTreeRegressor(max\_depth=3, random\_state=RandomState(MT19937) at 0x7E1D96200440)\], \[DecisionTreeRegressor(max\_depth=3, random\_state=RandomState(MT19937) at 0x7E1D96200440)\]\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the MSE brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](10,) | \[0.05,0.01,0.26,...,0.02,0.4 ,0.04\] |\
| [init\_ init\_: estimator  <br>  <br>The estimator that provides the initial predictions. Set via the \`\`init\`\`  <br>argument.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=init_,-estimator) | DummyRegressor | DummyRegressor() |\
| [max\_features\_ max\_features\_: int  <br>  <br>The inferred value of max\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=max_features_,-int) | int | 10  |\
| [n\_estimators\_ n\_estimators\_: int  <br>  <br>The number of estimators as selected by early stopping (if  <br>\`\`n\_iter\_no\_change\`\` is specified). Otherwise it is set to  <br>\`\`n\_estimators\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=n_estimators_,-int) | int | 100 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=n_features_in_,-int) | int | 10  |\
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of trees that are built at each iteration. For regressors, this is  <br>always 1.  <br>  <br>.. versionadded:: 1.4.0](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |\
| [train\_score\_ train\_score\_: ndarray of shape (n\_estimators,)  <br>  <br>The i-th score \`\`train\_score\_\[i\]\`\` is the loss of the  <br>model at iteration \`\`i\`\` on the in-bag sample.  <br>If \`\`subsample == 1\`\` this is the loss on the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#:~:text=train_score_,-ndarray%20of%20shape%20%28n_estimators%2C%29) | ndarray\[float64\](100,) | \[5365.79,4906.74,4503.84,...,1199.28,1195.02,1191.67\] |\
\
rf\
\
RandomForestRegressor\
\
[?Documentation for RandomForestRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 1   |\
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |\
|     | [criterion criterion: {"squared\_error", "absolute\_error", "poisson"}, default="squared\_error"  <br>  <br>The function to measure the quality of a split. Supported criteria  <br>are "squared\_error" for the mean squared error, which is equal to  <br>variance reduction as feature selection criterion and minimizes the L2  <br>loss using the mean of each terminal node, "absolute\_error" for the mean  <br>absolute error, which minimizes the L1 loss using the median of each terminal  <br>node, and "poisson" which uses reduction in Poisson deviance to find splits,  <br>also using the mean of each terminal node.  <br>  <br>.. versionadded:: 0.18  <br>Mean Absolute Error (MAE) criterion.  <br>  <br>.. versionadded:: 1.0  <br>Poisson criterion.  <br>  <br>.. versionchanged:: 1.9  <br>Criterion \`"friedman\_mse"\` was deprecated.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=criterion,-%7B%22squared_error%22%2C%20%22absolute_error%22%2C%20%22poisson%22%7D%2C%20default%3D%22squared_error%22) | 'squared\_error' |\
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |\
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |\
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |\
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_features max\_features: {"sqrt", "log2", None}, int or float, default=1.0  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None or 1.0, then \`max\_features=n\_features\`.  <br>  <br>.. note::  <br>The default of 1.0 is equivalent to bagged trees and more  <br>randomness can be achieved by setting smaller values, e.g. 0.3.  <br>  <br>.. versionchanged:: 1.1  <br>The default of \`max\_features\` changed from \`"auto"\` to 1.0.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D1.0) | 1.0 |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |\
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |\
|     | [bootstrap bootstrap: bool, default=True  <br>  <br>Whether bootstrap samples are used when building trees. If False, the  <br>whole dataset is used to build each tree.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | True |\
|     | [oob\_score oob\_score: bool or callable, default=False  <br>  <br>Whether to use out-of-bag samples to estimate the generalization score.  <br>By default, :func:\`~sklearn.metrics.r2\_score\` is used.  <br>Provide a callable with signature \`metric(y\_true, y\_pred)\` to use a  <br>custom metric. Only available if \`bootstrap=True\`.  <br>  <br>For an illustration of out-of-bag (OOB) error estimation, see the example  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_ensemble\_oob.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`predict\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multioutput regressions (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeRegressor\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeRegressor) | DecisionTreeRegressor | DecisionTreeRegressor() |\
| [estimators\_ estimators\_: list of DecisionTreeRegressor  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=estimators_,-list%20of%20DecisionTreeRegressor) | list | \[DecisionTreeR...te=1791095845), DecisionTreeR...te=2135392491), DecisionTreeR...ate=946286476), DecisionTreeR...te=1857819720), ...\] |\
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[132, 2... dtype=int32), array(\[223, 1... dtype=int32), array(\[222, 1... dtype=int32), array(\[386, ... dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](10,) | \[0.06,0.01,0.28,...,0.02,0.3 ,0.07\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=n_features_in_,-int) | int | 10  |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=n_outputs_,-int) | int | 1   |\
\
lr\
\
LinearRegression\
\
[?Documentation for LinearRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to False, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [copy\_X copy\_X: bool, default=True  <br>  <br>If True, X will be copied; else, it may be overwritten.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=copy_X,-bool%2C%20default%3DTrue) | True |\
|     | [tol tol: float, default=1e-6  <br>  <br>The precision of the solution (\`coef\_\`) is determined by \`tol\` which  <br>specifies the convergence criterion of the underlying solver. \`tol\` is  <br>set as \`atol\` and \`btol\` of :func:\`scipy.sparse.linalg.lsqr\` when  <br>fitting on sparse training data. \`tol\` is set as \`cond\` of  <br>:func:\`scipy.linalg.lstsq\` when fitting on dense training data.  <br>  <br>.. versionadded:: 1.7  <br>.. versionchanged:: 1.9  <br>Now supported on dense data, interpreted as the \`cond\` parameter.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=tol,-float%2C%20default%3D1e-6) | 1e-06 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This will only provide  <br>speedup in case of sufficiently large problems, that is if firstly  <br>\`n\_targets > 1\` and secondly \`X\` is sparse or if \`positive\` is set  <br>to \`True\`. \`\`None\`\` means 1 unless in a  <br>:obj:\`joblib.parallel\_backend\` context. \`\`-1\`\` means using all  <br>processors. See :term:\`Glossary <n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [positive positive: bool, default=False  <br>  <br>When set to \`\`True\`\`, forces the coefficients to be positive. This  <br>option is only supported for dense arrays.  <br>  <br>For a comparison between a linear regression model with positive constraints  <br>on the regression coefficients and a linear regression without such constraints,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_nnls.py\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=positive,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [coef\_ coef\_: array of shape (n\_features, ) or (n\_targets, n\_features)  <br>  <br>Estimated coefficients for the linear regression problem.  <br>If multiple targets are passed during the fit (y 2D), this  <br>is a 2D array of shape (n\_targets, n\_features), while if only  <br>one target is passed, this is a 1D array of length n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=coef_,-array%20of%20shape%20%28n_features%2C%20%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](10,) | \[ -10.01,-239.82, 519.85,..., 177.06, 751.27, 67.63\] |\
| [intercept\_ intercept\_: float or array of shape (n\_targets,)  <br>  <br>Independent term in the linear model. Set to 0.0 if  <br>\`fit\_intercept = False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=intercept_,-float%20or%20array%20of%20shape%20%28n_targets%2C%29) | float64 | 152.1 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=n_features_in_,-int) | int | 10  |\
| [rank\_ rank\_: int  <br>  <br>Rank of matrix \`X\`. Only available when \`X\` is dense.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=rank_,-int) | int64 | np.int64(10) |\
| [singular\_ singular\_: array of shape (min(X, y),)  <br>  <br>Singular values of \`X\`. Only available when \`X\` is dense.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=singular_,-array%20of%20shape%20%28min%28X%2C%20y%29%2C%29) | ndarray\[float64\](10,) | \[2.01,1.22,1.1 ,...,0.66,0.28,0.09\] |\
\
3 features\
\
|     |\
| --- |\
| votingregressor\_gb |\
| votingregressor\_rf |\
| votingregressor\_lr |\
\
  \
  \
\
Making predictions[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html#making-predictions "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------\
\
Now we will use each of the regressors to make the 20 first predictions.\
\
xt \= X\[:20\]\
\
pred1 \= reg1.predict(xt)\
pred2 \= reg2.predict(xt)\
pred3 \= reg3.predict(xt)\
pred4 \= ereg.predict(xt)\
\
Copy to clipboard\
\
Plot the results[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html#plot-the-results "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------\
\
Finally, we will visualize the 20 predictions. The red stars show the average prediction made by [`VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")\
.\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
()\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(pred1, "gd", label\="GradientBoostingRegressor")\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(pred2, "b^", label\="RandomForestRegressor")\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(pred3, "ys", label\="LinearRegression")\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(pred4, "r\*", ms\=10, label\="VotingRegressor")\
\
[plt.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params")\
(axis\="x", which\="both", bottom\=False, top\=False, labelbottom\=False)\
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")\
("predicted")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("training samples")\
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")\
(loc\="best")\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Regressor predictions and their average")\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![Regressor predictions and their average](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_001.png)\
\
**Total running time of the script:** (0 minutes 0.913 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_voting_regressor.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_voting_regressor.ipynb)\
\
[`Download Jupyter notebook: plot_voting_regressor.ipynb`](https://scikit-learn.org/stable/_downloads/5bb69fbfba6a6762ece8fe57d5044636/plot_voting_regressor.ipynb)\
\
[`Download Python source code: plot_voting_regressor.py`](https://scikit-learn.org/stable/_downloads/41218639b706e8575551bfabbe93c69f/plot_voting_regressor.py)\
\
[`Download zipped: plot_voting_regressor.zip`](https://scikit-learn.org/stable/_downloads/639968ec6cece5483e8b9df39f02a7c4/plot_voting_regressor.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)\
\
[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)\
\
Combine predictors using stacking\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)\
\
[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)\
\
Decision Tree Regression with AdaBoost\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_regression_multioutput_thumb.png)\
\
[Comparing random forests and the multi-output meta estimator](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)\
\
Comparing random forests and the multi-output meta estimator\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)\
\
[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)\
\
Gradient Boosting regression\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/41218639b706e8575551bfabbe93c69f/plot_voting_regressor.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/5bb69fbfba6a6762ece8fe57d5044636/plot_voting_regressor.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/639968ec6cece5483e8b9df39f02a7c4/plot_voting_regressor.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_voting_regressor.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_voting_regressor.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)