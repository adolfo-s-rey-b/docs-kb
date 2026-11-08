[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_monotonic_constraints.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_monotonic_constraints.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_monotonic_constraints.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_monotonic_constraints.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_monotonic_constraints.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_monotonic_constraints.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html#sphx-glr-download-auto-examples-ensemble-plot-monotonic-constraints-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Monotonic Constraints[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html#monotonic-constraints "Link to this heading")

==============================================================================================================================================================

This example illustrates the effect of monotonic constraints on a gradient boosting estimator.

We build an artificial dataset where the target value is in general positively correlated with the first feature (with some random and non-random variations), and in general negatively correlated with the second feature.

By imposing a monotonic increase or a monotonic decrease constraint, respectively, on the features during the learning process, the estimator is able to properly follow the general trend instead of being subject to the variations.

This example was inspired by the [XGBoost documentation](https://xgboost.readthedocs.io/en/latest/tutorials/monotonic.html)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.inspection import PartialDependenceDisplay

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

n\_samples \= 1000
f\_0 \= rng.rand(n\_samples)
f\_1 \= rng.rand(n\_samples)
X \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[f\_0, f\_1\]
noise \= rng.normal(loc\=0.0, scale\=0.01, size\=n\_samples)

\# y is positively correlated with f\_0, and negatively correlated with f\_1
y \= 5 \* f\_0 + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(10 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* f\_0) \- 5 \* f\_1 \- [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(10 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* f\_1) + noise

Copy to clipboard

Fit a first model on this dataset without any constraints.

gbdt\_no\_cst \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
()
gbdt\_no\_cst.fit(X, y)

Copy to clipboard

HistGradientBoostingRegressor()

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

HistGradientBoostingRegressor

[?Documentation for HistGradientBoostingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [loss loss: {'squared\_error', 'absolute\_error', 'gamma', 'poisson', 'quantile'}, default='squared\_error'  <br>  <br>The loss function to use in the boosting process. Note that the  <br>"squared error", "gamma" and "poisson" losses actually implement  <br>"half least squares loss", "half gamma deviance" and "half poisson  <br>deviance" to simplify the computation of the gradient. Furthermore,  <br>"gamma" and "poisson" losses internally use a log-link, "gamma"  <br>requires \`\`y > 0\`\` and "poisson" requires \`\`y >= 0\`\`.  <br>"quantile" uses the pinball loss.  <br>  <br>.. versionchanged:: 0.23  <br>Added option 'poisson'.  <br>  <br>.. versionchanged:: 1.1  <br>Added option 'quantile'.  <br>  <br>.. versionchanged:: 1.3  <br>Added option 'gamma'.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27absolute_error%27%2C%20%27gamma%27%2C%20%27poisson%27%2C%20%27quantile%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27squared_error%27) | 'squared\_error' |
|     | [quantile quantile: float, default=None  <br>  <br>If loss is "quantile", this parameter specifies which quantile to be estimated  <br>and must be between 0 and 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=quantile,-float%2C%20default%3DNone) | None |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\` and  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_categorical.py\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: the :ref:\`coefficient of determination <r2\_score>\`  <br>(:math:\`R^2\`) is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores during early  <br>stopping. The higher the tolerance, the more likely we are to early  <br>stop: higher tolerance means that it will be harder for subsequent  <br>iterations to be considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [do\_early\_stopping\_ do\_early\_stopping\_: bool  <br>  <br>Indicates whether early stopping is used during training.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=do_early_stopping_,-bool) | bool | False |
| [is\_categorical\_ is\_categorical\_: ndarray, shape (n\_features, ) or None  <br>  <br>Boolean mask for the categorical features. \`\`None\`\` if there are no  <br>categorical features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=is_categorical_,-ndarray%2C%20shape%20%28n_features%2C%20%29%20or%20None) | NoneType | None |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations as selected by early stopping, depending on  <br>the \`early\_stopping\` parameter. Otherwise it corresponds to max\_iter.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_,-int) | int | 100 |
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of tree that are built at each iteration. For regressors,  <br>this is always 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |
| [train\_score\_ train\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the training data. The first entry  <br>is the score of the ensemble before the first iteration. Scores are  <br>computed according to the \`\`scoring\`\` parameter. If \`\`scoring\`\` is  <br>not 'loss', scores are computed on a subset of at most 10 000  <br>samples. Empty if no early stopping.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=train_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |
| [validation\_score\_ validation\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the held-out validation data. The  <br>first entry is the score of the ensemble before the first iteration.  <br>Scores are computed according to the \`\`scoring\`\` parameter. Empty if  <br>no early stopping or if \`\`validation\_fraction\`\` is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |

  
  

Fit a second model on this dataset with monotonic increase (1) and a monotonic decrease (-1) constraints, respectively.

gbdt\_with\_monotonic\_cst \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(monotonic\_cst\=\[1, \-1\])
gbdt\_with\_monotonic\_cst.fit(X, y)

Copy to clipboard

HistGradientBoostingRegressor(monotonic\_cst=\[1, -1\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

HistGradientBoostingRegressor

[?Documentation for HistGradientBoostingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | \[1, -1\] |
|     | [loss loss: {'squared\_error', 'absolute\_error', 'gamma', 'poisson', 'quantile'}, default='squared\_error'  <br>  <br>The loss function to use in the boosting process. Note that the  <br>"squared error", "gamma" and "poisson" losses actually implement  <br>"half least squares loss", "half gamma deviance" and "half poisson  <br>deviance" to simplify the computation of the gradient. Furthermore,  <br>"gamma" and "poisson" losses internally use a log-link, "gamma"  <br>requires \`\`y > 0\`\` and "poisson" requires \`\`y >= 0\`\`.  <br>"quantile" uses the pinball loss.  <br>  <br>.. versionchanged:: 0.23  <br>Added option 'poisson'.  <br>  <br>.. versionchanged:: 1.1  <br>Added option 'quantile'.  <br>  <br>.. versionchanged:: 1.3  <br>Added option 'gamma'.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27absolute_error%27%2C%20%27gamma%27%2C%20%27poisson%27%2C%20%27quantile%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27squared_error%27) | 'squared\_error' |
|     | [quantile quantile: float, default=None  <br>  <br>If loss is "quantile", this parameter specifies which quantile to be estimated  <br>and must be between 0 and 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=quantile,-float%2C%20default%3DNone) | None |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\` and  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_categorical.py\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: the :ref:\`coefficient of determination <r2\_score>\`  <br>(:math:\`R^2\`) is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores during early  <br>stopping. The higher the tolerance, the more likely we are to early  <br>stop: higher tolerance means that it will be harder for subsequent  <br>iterations to be considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [do\_early\_stopping\_ do\_early\_stopping\_: bool  <br>  <br>Indicates whether early stopping is used during training.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=do_early_stopping_,-bool) | bool | False |
| [is\_categorical\_ is\_categorical\_: ndarray, shape (n\_features, ) or None  <br>  <br>Boolean mask for the categorical features. \`\`None\`\` if there are no  <br>categorical features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=is_categorical_,-ndarray%2C%20shape%20%28n_features%2C%20%29%20or%20None) | NoneType | None |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations as selected by early stopping, depending on  <br>the \`early\_stopping\` parameter. Otherwise it corresponds to max\_iter.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_,-int) | int | 100 |
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of tree that are built at each iteration. For regressors,  <br>this is always 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |
| [train\_score\_ train\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the training data. The first entry  <br>is the score of the ensemble before the first iteration. Scores are  <br>computed according to the \`\`scoring\`\` parameter. If \`\`scoring\`\` is  <br>not 'loss', scores are computed on a subset of at most 10 000  <br>samples. Empty if no early stopping.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=train_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |
| [validation\_score\_ validation\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the held-out validation data. The  <br>first entry is the score of the ensemble before the first iteration.  <br>Scores are computed according to the \`\`scoring\`\` parameter. Empty if  <br>no early stopping or if \`\`validation\_fraction\`\` is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |

  
  

Let’s display the partial dependence of the predictions on the two features.

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    gbdt\_no\_cst,
    X,
    features\=\[0, 1\],
    feature\_names\=(
        "First feature",
        "Second feature",
    ),
    line\_kw\={"linewidth": 4, "label": "unconstrained", "color": "tab:blue"},
    ax\=ax,
)
[PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    gbdt\_with\_monotonic\_cst,
    X,
    features\=\[0, 1\],
    line\_kw\={"linewidth": 4, "label": "constrained", "color": "tab:orange"},
    ax\=disp.axes\_,
)

for f\_idx in (0, 1):
    disp.axes\_\[0, f\_idx\].plot(
        X\[:, f\_idx\], y, "o", alpha\=0.3, zorder\=-1, color\="tab:green"
    )
    disp.axes\_\[0, f\_idx\].set\_ylim(\-6, 6)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
fig.suptitle("Monotonic constraints effect on partial dependences")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Monotonic constraints effect on partial dependences](https://scikit-learn.org/stable/_images/sphx_glr_plot_monotonic_constraints_001.png)

We can see that the predictions of the unconstrained model capture the oscillations of the data while the constrained model follows the general trend and ignores the local variations.

Using feature names to specify monotonic constraints[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html#using-feature-names-to-specify-monotonic-constraints "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note that if the training data has feature names, it’s possible to specify the monotonic constraints by passing a dictionary:

import pandas as pd

X\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(X, columns\=\["f\_0", "f\_1"\])

gbdt\_with\_monotonic\_cst\_df \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
    monotonic\_cst\={"f\_0": 1, "f\_1": \-1}
).fit(X\_df, y)

[np.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")
(
    gbdt\_with\_monotonic\_cst\_df.predict(X\_df), gbdt\_with\_monotonic\_cst.predict(X)
)

Copy to clipboard

True

Copy to clipboard

**Total running time of the script:** (0 minutes 0.568 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_monotonic_constraints.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_monotonic_constraints.ipynb)

[`Download Jupyter notebook: plot_monotonic_constraints.ipynb`](https://scikit-learn.org/stable/_downloads/215c560d29193ab9b0a495609bc74802/plot_monotonic_constraints.ipynb)

[`Download Python source code: plot_monotonic_constraints.py`](https://scikit-learn.org/stable/_downloads/9e22207e9bd6485b95f32783b59d9a80/plot_monotonic_constraints.py)

[`Download zipped: plot_monotonic_constraints.zip`](https://scikit-learn.org/stable/_downloads/235d8129d59e30e986be1e36b5badcc5/plot_monotonic_constraints.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_thumb.png)

[Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html)

Advanced Plotting With Partial Dependence

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/9e22207e9bd6485b95f32783b59d9a80/plot_monotonic_constraints.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/215c560d29193ab9b0a495609bc74802/plot_monotonic_constraints.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/235d8129d59e30e986be1e36b5badcc5/plot_monotonic_constraints.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_monotonic_constraints.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_monotonic_constraints.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)