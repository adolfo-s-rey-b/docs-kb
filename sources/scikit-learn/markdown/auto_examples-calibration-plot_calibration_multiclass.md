[Skip to main content](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/calibration/plot_calibration_multiclass.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/calibration/plot_calibration_multiclass.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/calibration/plot_calibration_multiclass.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/calibration/plot_calibration_multiclass.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/calibration/plot_calibration_multiclass.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/calibration/plot_calibration_multiclass.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#sphx-glr-download-auto-examples-calibration-plot-calibration-multiclass-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Probability Calibration for 3-class classification[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#probability-calibration-for-3-class-classification "Link to this heading")

============================================================================================================================================================================================================================

This example illustrates how sigmoid [calibration](https://scikit-learn.org/stable/modules/calibration.html#calibration)
 changes predicted probabilities for a 3-class classification problem. Illustrated is the standard 2-simplex, where the three corners correspond to the three classes. Arrows point from the probability vectors predicted by an uncalibrated classifier to the probability vectors predicted by the same classifier after sigmoid calibration on a hold-out validation set. Colors indicate the true class of an instance (red: class 1, green: class 2, blue: class 3).

Data[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Below, we generate a classification dataset with 2000 samples, 2 features and 3 target classes. We then split the data as follows:

*   train: 600 samples (for training the classifier)
    
*   valid: 400 samples (for calibrating predicted probabilities)
    
*   test: 1000 samples
    

Note that we also create `X_train_valid` and `y_train_valid`, which consists of both the train and valid subsets. This is used when we only want to train the classifier but not calibrate the predicted probabilities.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=2000, n\_features\=2, centers\=3, random\_state\=42, cluster\_std\=5.0
)
X\_train, y\_train \= X\[:600\], y\[:600\]
X\_valid, y\_valid \= X\[600:1000\], y\[600:1000\]
X\_train\_valid, y\_train\_valid \= X\[:1000\], y\[:1000\]
X\_test, y\_test \= X\[1000:\], y\[1000:\]

Copy to clipboard

Fitting and calibration[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#fitting-and-calibration "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we will train a [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 with 25 base estimators (trees) on the concatenated train and validation data (1000 samples). This is the uncalibrated classifier.

from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

clf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(n\_estimators\=25)
clf.fit(X\_train\_valid, y\_train\_valid)

Copy to clipboard

RandomForestClassifier(n\_estimators=25)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

RandomForestClassifier

[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 25  |
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
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,) or a list of such arrays  <br>  <br>The classes labels (single output problem), or a list of arrays of  <br>class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20a%20list%20of%20such%20arrays) | ndarray\[int64\](3,) | \[0,1,2\] |
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeClassifier\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeClassifier) | DecisionTreeClassifier | DecisionTreeClassifier() |
| [estimators\_ estimators\_: list of DecisionTreeClassifier  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_,-list%20of%20DecisionTreeClassifier) | list | \[DecisionTreeC...ate=209652396), DecisionTreeC...ate=398764591), DecisionTreeC...ate=924231285), DecisionTreeC...te=1478610112), ...\] |
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[236, 2... dtype=int32), array(\[107, 1... dtype=int32), array(\[301, 5... dtype=int32), array(\[900, 3... dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](2,) | \[0.44,0.56\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 3   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 2   |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
To train the calibrated classifier, we start with the same [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
 but train it using only the train data subset (600 samples) then calibrate, with `method='sigmoid'`, using the valid data subset (400 samples) in a 2-stage process.\
\
from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")\
from sklearn.frozen import [FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")\
\
clf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(n\_estimators\=25)\
clf.fit(X\_train, y\_train)\
cal\_clf \= [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")\
([FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")\
(clf), method\="sigmoid")\
cal\_clf.fit(X\_valid, y\_valid)\
\
Copy to clipboard\
\
CalibratedClassifierCV(estimator=FrozenEstimator(estimator=RandomForestClassifier(n\_estimators=25)))\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
CalibratedClassifierCV\
\
[?Documentation for CalibratedClassifierCV](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [estimator estimator: estimator instance, default=None  <br>  <br>The classifier whose output need to be calibrated to provide more  <br>accurate \`predict\_proba\` outputs. The default classifier is  <br>a :class:\`~sklearn.svm.LinearSVC\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=estimator,-estimator%20instance%2C%20default%3DNone) | FrozenEstimat...stimators=25)) |\
|     | [method method: {'sigmoid', 'isotonic', 'temperature'}, default='sigmoid'  <br>  <br>The method to use for calibration. Can be:  <br>  <br>\- 'sigmoid', which corresponds to Platt's method (i.e. a binary logistic  <br>regression model).  <br>\- 'isotonic', which is a non-parametric approach.  <br>\- 'temperature', temperature scaling.  <br>  <br>Sigmoid and isotonic calibration methods natively support only binary  <br>classifiers and extend to multi-class classification using a One-vs-Rest (OvR)  <br>strategy with post-hoc renormalization, i.e., adjusting the probabilities after  <br>calibration to ensure they sum up to 1.  <br>  <br>In contrast, temperature scaling naturally supports multi-class calibration by  <br>applying \`softmax(classifier\_logits/T)\` with a value of \`T\` (temperature)  <br>that optimizes the log loss.  <br>  <br>For very uncalibrated classifiers on very imbalanced datasets, sigmoid  <br>calibration might be preferred because it fits an additional intercept  <br>parameter. This helps shift decision boundaries appropriately when the  <br>classifier being calibrated is biased towards the majority class.  <br>  <br>Isotonic calibration is not recommended when the number of calibration samples  <br>is too low \`\`(≪1000)\`\` since it then tends to overfit.  <br>  <br>.. versionchanged:: 1.8  <br>Added option 'temperature'.](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=method,-%7B%27sigmoid%27%2C%20%27isotonic%27%2C%20%27temperature%27%7D%2C%20default%3D%27sigmoid%27) | 'sigmoid' |\
|     | [cv cv: int, cross-validation generator, or iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross-validation,  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used. If \`\`y\`\` is  <br>neither binary nor multiclass, :class:\`~sklearn.model\_selection.KFold\`  <br>is used.  <br>  <br>Refer to the :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%2C%20or%20iterable%2C%20default%3DNone) | None |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors.  <br>  <br>Base estimator clones are fitted in parallel across cross-validation  <br>iterations.  <br>  <br>See :term:\`Glossary <n\_jobs>\` for more details.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [ensemble ensemble: bool, or "auto", default="auto"  <br>  <br>Determines how the calibrator is fitted.  <br>  <br>"auto" will use \`False\` if the \`estimator\` is a  <br>:class:\`~sklearn.frozen.FrozenEstimator\`, and \`True\` otherwise.  <br>  <br>If \`True\`, the \`estimator\` is fitted using training data, and  <br>calibrated using testing data, for each \`cv\` fold. The final estimator  <br>is an ensemble of \`n\_cv\` fitted classifier and calibrator pairs, where  <br>\`n\_cv\` is the number of cross-validation folds. The output is the  <br>average predicted probabilities of all pairs.  <br>  <br>If \`False\`, \`cv\` is used to compute unbiased predictions, via  <br>:func:\`~sklearn.model\_selection.cross\_val\_predict\`, which are then  <br>used for calibration. At prediction time, the classifier used is the  <br>\`estimator\` trained on all the data.  <br>Note that this method is also internally implemented in  <br>:mod:\`sklearn.svm\` estimators with the \`probabilities=True\` parameter.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.6  <br>\`"auto"\` option is added and is the default.](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=ensemble,-bool%2C%20or%20%22auto%22%2C%20default%3D%22auto%22) | 'auto' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [calibrated\_classifiers\_ calibrated\_classifiers\_: list (len() equal to cv or 1 if \`ensemble=False\`)  <br>  <br>The list of classifier and calibrator pairs.  <br>  <br>\- When \`ensemble=True\`, \`n\_cv\` fitted \`estimator\` and calibrator pairs.  <br>\`n\_cv\` is the number of cross-validation folds.  <br>\- When \`ensemble=False\`, the \`estimator\`, fitted on all the data, and fitted  <br>calibrator.  <br>  <br>.. versionchanged:: 0.24  <br>Single calibrated classifier case when \`ensemble=False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=calibrated_classifiers_,-list%20%28len%28%29%20equal%20to%20cv%20or%201%20if%20ensemble%3DFalse%29) | list | \[<sklearn.cali...x7e1dcbfc47e0>\] |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The class labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](3,) | \[0,1,2\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#:~:text=n_features_in_,-int) | int | 2   |\
\
estimator: FrozenEstimator\
\
FrozenEstimator(estimator=RandomForestClassifier(n\_estimators=25))\
\
estimator: RandomForestClassifier\
\
RandomForestClassifier(n\_estimators=25)\
\
RandomForestClassifier\
\
[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 25  |\
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
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,) or a list of such arrays  <br>  <br>The classes labels (single output problem), or a list of arrays of  <br>class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20a%20list%20of%20such%20arrays) | ndarray\[int64\](3,) | \[0,1,2\] |\
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeClassifier\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeClassifier) | DecisionTreeClassifier | DecisionTreeClassifier() |\
| [estimators\_ estimators\_: list of DecisionTreeClassifier  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_,-list%20of%20DecisionTreeClassifier) | list | \[DecisionTreeC...te=1686997841), DecisionTreeC...te=1827923621), DecisionTreeC...te=1443447321), DecisionTreeC...ate=305097549), ...\] |\
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[ 66, ..., dtype=int32), array(\[313, 4..., dtype=int32), array(\[237, 4..., dtype=int32), array(\[ 1, 2..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](2,) | \[0.45,0.55\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 3   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 2   |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
Compare probabilities[#](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html#compare-probabilities "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Below we plot a 2-simplex with arrows showing the change in predicted probabilities of the test samples.\
\
import matplotlib.pyplot as plt\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
(figsize\=(10, 10))\
colors \= \["r", "g", "b"\]\
\
clf\_probs \= clf.predict\_proba(X\_test)\
cal\_clf\_probs \= cal\_clf.predict\_proba(X\_test)\
\# Plot arrows\
for i in range(clf\_probs.shape\[0\]):\
    [plt.arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.arrow.html#matplotlib.pyplot.arrow "matplotlib.pyplot.arrow")\
(\
        clf\_probs\[i, 0\],\
        clf\_probs\[i, 1\],\
        cal\_clf\_probs\[i, 0\] \- clf\_probs\[i, 0\],\
        cal\_clf\_probs\[i, 1\] \- clf\_probs\[i, 1\],\
        color\=colors\[y\_test\[i\]\],\
        head\_width\=1e-2,\
    )\
\
\# Plot perfect predictions, at each vertex\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[1.0\], \[0.0\], "ro", ms\=20, label\="Class 1")\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0.0\], \[1.0\], "go", ms\=20, label\="Class 2")\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0.0\], \[0.0\], "bo", ms\=20, label\="Class 3")\
\
\# Plot boundaries of unit simplex\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0.0, 1.0, 0.0, 0.0\], \[0.0, 0.0, 1.0, 0.0\], "k", label\="Simplex")\
\
\# Annotate points 6 points around the simplex, and mid point inside simplex\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($\\frac{1}{3}$, $\\frac{1}{3}$, $\\frac{1}{3}$)",\
    xy\=(1.0 / 3, 1.0 / 3),\
    xytext\=(1.0 / 3, 0.23),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[1.0 / 3\], \[1.0 / 3\], "ko", ms\=5)\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($\\frac{1}{2}$, $0$, $\\frac{1}{2}$)",\
    xy\=(0.5, 0.0),\
    xytext\=(0.5, 0.1),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($0$, $\\frac{1}{2}$, $\\frac{1}{2}$)",\
    xy\=(0.0, 0.5),\
    xytext\=(0.1, 0.5),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($\\frac{1}{2}$, $\\frac{1}{2}$, $0$)",\
    xy\=(0.5, 0.5),\
    xytext\=(0.6, 0.6),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($0$, $0$, $1$)",\
    xy\=(0, 0),\
    xytext\=(0.1, 0.1),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($1$, $0$, $0$)",\
    xy\=(1, 0),\
    xytext\=(1, 0.1),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
[plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")\
(\
    r"($0$, $1$, $0$)",\
    xy\=(0, 1),\
    xytext\=(0.1, 1),\
    xycoords\="data",\
    arrowprops\=dict(facecolor\="black", shrink\=0.05),\
    horizontalalignment\="center",\
    verticalalignment\="center",\
)\
\# Add grid\
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")\
(False)\
for x in \[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0\]:\
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0, x\], \[x, 0\], "k", alpha\=0.2)\
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0, 0 + (1 \- x) / 2\], \[x, x + (1 \- x) / 2\], "k", alpha\=0.2)\
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[x, x + (1 \- x) / 2\], \[0, 0 + (1 \- x) / 2\], "k", alpha\=0.2)\
\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Change of predicted probabilities on test samples after sigmoid calibration")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Probability class 1")\
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")\
("Probability class 2")\
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")\
(\-0.05, 1.05)\
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")\
(\-0.05, 1.05)\
\_ \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")\
(loc\="best")\
\
Copy to clipboard\
\
![Change of predicted probabilities on test samples after sigmoid calibration](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_001.png)\
\
In the figure above, each vertex of the simplex represents a perfectly predicted class (e.g., 1, 0, 0). The mid point inside the simplex represents predicting the three classes with equal probability (i.e., 1/3, 1/3, 1/3). Each arrow starts at the uncalibrated probabilities and end with the arrow head at the calibrated probability. The color of the arrow represents the true class of that test sample.\
\
The uncalibrated classifier is overly confident in its predictions and incurs a large [log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)\
. The calibrated classifier incurs a lower [log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)\
 due to two factors. First, notice in the figure above that the arrows generally point away from the edges of the simplex, where the probability of one class is 0. Second, a large proportion of the arrows point towards the true class, e.g., green arrows (samples where the true class is ‘green’) generally point towards the green vertex. This results in fewer over-confident, 0 predicted probabilities and at the same time an increase in the predicted probabilities of the correct class. Thus, the calibrated classifier produces more accurate predicted probabilities that incur a lower [log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)\
\
We can show this objectively by comparing the [log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)\
 of the uncalibrated and calibrated classifiers on the predictions of the 1000 test samples. Note that an alternative would have been to increase the number of base estimators (trees) of the [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
 which would have resulted in a similar decrease in [log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)\
.\
\
from sklearn.metrics import [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")\
\
loss \= [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")\
(y\_test, clf\_probs)\
cal\_loss \= [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")\
(y\_test, cal\_clf\_probs)\
\
print("Log-loss of:")\
print(f" - uncalibrated classifier: {loss:.3f}")\
print(f" - calibrated classifier: {cal\_loss:.3f}")\
\
Copy to clipboard\
\
Log-loss of:\
 - uncalibrated classifier: 1.327\
 - calibrated classifier: 0.549\
\
Copy to clipboard\
\
We can also assess calibration with the Brier score for probabilistics predictions (lower is better, possible range is \[0, 2\]):\
\
from sklearn.metrics import [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")\
\
loss \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")\
(y\_test, clf\_probs)\
cal\_loss \= [brier\_score\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")\
(y\_test, cal\_clf\_probs)\
\
print("Brier score of")\
print(f" - uncalibrated classifier: {loss:.3f}")\
print(f" - calibrated classifier: {cal\_loss:.3f}")\
\
Copy to clipboard\
\
Brier score of\
 - uncalibrated classifier: 0.308\
 - calibrated classifier: 0.310\
\
Copy to clipboard\
\
According to the Brier score, the calibrated classifier is not better than the original model.\
\
Finally we generate a grid of possible uncalibrated probabilities over the 2-simplex, compute the corresponding calibrated probabilities and plot arrows for each. The arrows are colored according the highest uncalibrated probability. This illustrates the learned calibration map:\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
(figsize\=(10, 10))\
\# Generate grid of probability values\
p1d \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 1, 20)\
p0, p1 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")\
(p1d, p1d)\
p2 \= 1 \- p0 \- p1\
p \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")\
\[p0.ravel(), p1.ravel(), p2.ravel()\]\
p \= p\[p\[:, 2\] \>= 0\]\
\
\# Use the three class-wise calibrators to compute calibrated probabilities\
calibrated\_classifier \= cal\_clf.calibrated\_classifiers\_\[0\]\
prediction \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")\
(\
    \[\
        calibrator.predict(this\_p)\
        for calibrator, this\_p in zip(calibrated\_classifier.calibrators, p.T)\
    \]\
).T\
\
\# Re-normalize the calibrated predictions to make sure they stay inside the\
\# simplex. This same renormalization step is performed internally by the\
\# predict method of CalibratedClassifierCV on multiclass problems.\
prediction /= prediction.sum(axis\=1)\[:, None\]\
\
\# Plot changes in predicted probabilities induced by the calibrators\
for i in range(prediction.shape\[0\]):\
    [plt.arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.arrow.html#matplotlib.pyplot.arrow "matplotlib.pyplot.arrow")\
(\
        p\[i, 0\],\
        p\[i, 1\],\
        prediction\[i, 0\] \- p\[i, 0\],\
        prediction\[i, 1\] \- p\[i, 1\],\
        head\_width\=1e-2,\
        color\=colors\[[np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")\
(p\[i\])\],\
    )\
\
\# Plot the boundaries of the unit simplex\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0.0, 1.0, 0.0, 0.0\], \[0.0, 0.0, 1.0, 0.0\], "k", label\="Simplex")\
\
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")\
(False)\
for x in \[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0\]:\
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0, x\], \[x, 0\], "k", alpha\=0.2)\
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[0, 0 + (1 \- x) / 2\], \[x, x + (1 \- x) / 2\], "k", alpha\=0.2)\
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\[x, x + (1 \- x) / 2\], \[0, 0 + (1 \- x) / 2\], "k", alpha\=0.2)\
\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Learned sigmoid calibration map")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Probability class 1")\
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")\
("Probability class 2")\
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")\
(\-0.05, 1.05)\
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")\
(\-0.05, 1.05)\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![Learned sigmoid calibration map](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_002.png)\
\
One can observe that, on average, the calibrator is pushing highly confident predictions away from the boundaries of the simplex while simultaneously moving uncertain predictions towards one of three modes, one for each class. We can also observe that the mapping is not symmetric. Furthermore some arrows seem to cross class assignment boundaries which is not necessarily what one would expect from a calibration map as it means that some predicted classes will change after calibration.\
\
All in all, the One-vs-Rest multiclass-calibration strategy implemented in `CalibratedClassifierCV` should not be trusted blindly.\
\
**Total running time of the script:** (0 minutes 1.591 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_calibration_multiclass.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_calibration_multiclass.ipynb)\
\
[`Download Jupyter notebook: plot_calibration_multiclass.ipynb`](https://scikit-learn.org/stable/_downloads/b367e30cc681ed484e0148f4ce9eccb0/plot_calibration_multiclass.ipynb)\
\
[`Download Python source code: plot_calibration_multiclass.py`](https://scikit-learn.org/stable/_downloads/f4a2350e7cc794cdb19840052e96a1e7/plot_calibration_multiclass.py)\
\
[`Download zipped: plot_calibration_multiclass.zip`](https://scikit-learn.org/stable/_downloads/6ef4b0956dab0972b88de2f2a3bf20d7/plot_calibration_multiclass.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)\
\
[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)\
\
Probability calibration of classifiers\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)\
\
[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)\
\
Comparison of Calibration of Classifiers\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)\
\
[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)\
\
Probability Calibration curves\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)\
\
[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)\
\
Examples of Using FrozenEstimator\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/f4a2350e7cc794cdb19840052e96a1e7/plot_calibration_multiclass.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b367e30cc681ed484e0148f4ce9eccb0/plot_calibration_multiclass.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/6ef4b0956dab0972b88de2f2a3bf20d7/plot_calibration_multiclass.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo2.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/calibration/plot_calibration_multiclass.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo2.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/calibration/plot_calibration_multiclass.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)