[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_precision_recall.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_precision_recall.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_precision_recall.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_precision_recall.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_precision_recall.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_precision_recall.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#sphx-glr-download-auto-examples-model-selection-plot-precision-recall-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Precision-Recall[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#precision-recall "Link to this heading")

======================================================================================================================================================

Example of Precision-Recall metric to evaluate classifier output quality.

Precision-Recall is a useful measure of success of prediction when the classes are very imbalanced. In information retrieval, precision is a measure of the fraction of relevant items among actually returned items while recall is a measure of the fraction of items that were returned among all items that should have been returned. ‘Relevancy’ here refers to items that are positively labeled, i.e., true positives and false negatives.

Precision (P) is defined as the number of true positives (Tp) over the number of true positives plus the number of false positives (Fp).

P\=TpTp+Fp

Recall (R) is defined as the number of true positives (Tp) over the number of true positives plus the number of false negatives (Fn).

R\=TpTp+Fn

The precision-recall curve shows the tradeoff between precision and recall for different thresholds. A high area under the curve represents both high recall and high precision. High precision is achieved by having few false positives in the returned results, and high recall is achieved by having few false negatives in the relevant results. High scores for both show that the classifier is returning accurate results (high precision), as well as returning a majority of all relevant results (high recall).

A system with high recall but low precision returns most of the relevant items, but the proportion of returned results that are incorrectly labeled is high. A system with high precision but low recall is just the opposite, returning very few of the relevant items, but most of its predicted labels are correct when compared to the actual labels. An ideal system with high precision and high recall will return most of the relevant items, with most results labeled correctly.

The definition of precision (TpTp+Fp) shows that lowering the threshold of a classifier may increase the denominator, by increasing the number of results returned. If the threshold was previously set too high, the new results may all be true positives, which will increase precision. If the previous threshold was about right or too low, further lowering the threshold will introduce false positives, decreasing precision.

Recall is defined as TpTp+Fn, where Tp+Fn does not depend on the classifier threshold. Changing the classifier threshold can only change the numerator, Tp. Lowering the classifier threshold may increase recall, by increasing the number of true positive results. It is also possible that lowering the threshold may leave recall unchanged, while the precision fluctuates. Thus, precision does not necessarily decrease with recall.

The relationship between recall and precision can be observed in the stairstep area of the plot - at the edges of these steps a small change in the threshold considerably reduces precision, with only a minor gain in recall.

**Average precision** (AP) summarizes such a plot as the weighted mean of precisions achieved at each threshold, with the increase in recall from the previous threshold used as the weight:

AP\=∑n(Rn−Rn−1)Pn

where Pn and Rn are the precision and recall at the nth threshold. A pair (Rk,Pk) is referred to as an _operating point_.

AP and the trapezoidal area under the operating points ([`sklearn.metrics.auc`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
) are common ways to summarize a precision-recall curve that lead to different results. Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Precision-recall curves are typically used in binary classification to study the output of a classifier. In order to extend the precision-recall curve and average precision to multi-class or multi-label classification, it is necessary to binarize the output. One curve can be drawn per label, but one can also draw a precision-recall curve by considering each element of the label indicator matrix as a binary prediction ([micro-averaging](https://scikit-learn.org/stable/modules/model_evaluation.html#average)
).

Note

See also [`sklearn.metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
,

[`sklearn.metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
, [`sklearn.metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
, [`sklearn.metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

In binary classification settings[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#in-binary-classification-settings "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Dataset and model[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#dataset-and-model "Link to this heading")

We will use a Linear SVC classifier to differentiate two types of irises.

import numpy as np

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
(return\_X\_y\=True)

\# Add noisy features
random\_state \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
n\_samples, n\_features \= X.shape
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[X, random\_state.randn(n\_samples, 200 \* n\_features)\], axis\=1)

\# Limit to the two first classes, and split into training and test
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X\[y < 2\], y\[y < 2\], test\_size\=0.5, random\_state\=random\_state
)

Copy to clipboard

Linear SVC will expect each feature to have a similar range of values. Thus, we will first scale the data using a [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
.

from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

classifier \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(random\_state\=random\_state))
classifier.fit(X\_train, y\_train)

Copy to clipboard

Pipeline(steps=\[('standardscaler', StandardScaler()),\
                ('linearsvc',\
                 LinearSVC(random\_state=RandomState(MT19937) at 0x7E1DF5B93940))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('standardscaler', ...), ('linearsvc', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 804 |

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](804,) | \[ 5.44, 3.13, 2.76,..., 0.08,-0.09, 0.07\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 804 |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 50  |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](804,) | \[0.59,0.51,1.41,...,0.9 ,0.82,0.98\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](804,) | \[0.35,0.26,2. ,...,0.81,0.68,0.97\] |

100 of 804 features

|     |
| --- |
| x0  |
| x1  |
| x2  |
| x3  |
| x4  |
| x5  |
| x6  |
| x7  |
| x8  |
| x9  |
| x10 |
| x11 |
| x12 |
| x13 |
| x14 |
| x15 |
| x16 |
| x17 |
| x18 |
| x19 |
| x20 |
| x21 |
| x22 |
| x23 |
| x24 |
| x25 |
| x26 |
| x27 |
| x28 |
| x29 |
| x30 |
| x31 |
| x32 |
| x33 |
| x34 |
| x35 |
| x36 |
| x37 |
| x38 |
| x39 |
| x40 |
| x41 |
| x42 |
| x43 |
| x44 |
| x45 |
| x46 |
| x47 |
| x48 |
| x49 |
| x50 |
| x51 |
| x52 |
| x53 |
| x54 |
| x55 |
| x56 |
| x57 |
| x58 |
| x59 |
| x60 |
| x61 |
| x62 |
| x63 |
| x64 |
| x65 |
| x66 |
| x67 |
| x68 |
| x69 |
| x70 |
| x71 |
| x72 |
| x73 |
| x74 |
| x75 |
| x76 |
| x77 |
| x78 |
| x79 |
| x80 |
| x81 |
| x82 |
| x83 |
| x84 |
| x85 |
| x86 |
| x87 |
| x88 |
| x89 |
| x90 |
| x91 |
| x92 |
| x93 |
| x94 |
| x95 |
| x96 |
| x97 |
| x98 |
| x99 |

LinearSVC

[?Documentation for LinearSVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>the dual coordinate descent (if \`\`dual=True\`\`). When \`\`dual=False\`\` the  <br>underlying implementation of :class:\`LinearSVC\` is not random and  <br>\`\`random\_state\`\` has no effect on the results.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | RandomState(M...0x7E1DF5B93940 |
|     | [penalty penalty: {'l1', 'l2'}, default='l2'  <br>  <br>Specifies the norm used in the penalization. The 'l2'  <br>penalty is the standard used in SVC. The 'l1' leads to \`\`coef\_\`\`  <br>vectors that are sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%7D%2C%20default%3D%27l2%27) | 'l2' |
|     | [loss loss: {'hinge', 'squared\_hinge'}, default='squared\_hinge'  <br>  <br>Specifies the loss function. 'hinge' is the standard SVM loss  <br>(used e.g. by the SVC class) while 'squared\_hinge' is the  <br>square of the hinge loss. The combination of \`\`penalty='l1'\`\`  <br>and \`\`loss='hinge'\`\` is not supported.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=loss,-%7B%27hinge%27%2C%20%27squared_hinge%27%7D%2C%20default%3D%27squared_hinge%27) | 'squared\_hinge' |
|     | [dual dual: "auto" or bool, default="auto"  <br>  <br>Select the algorithm to either solve the dual or primal  <br>optimization problem. Prefer dual=False when n\_samples > n\_features.  <br>\`dual="auto"\` will choose the value of the parameter automatically,  <br>based on the values of \`n\_samples\`, \`n\_features\`, \`loss\`, \`multi\_class\`  <br>and \`penalty\`. If \`n\_samples\` < \`n\_features\` and optimizer supports  <br>chosen \`loss\`, \`multi\_class\` and \`penalty\`, then dual will be set to True,  <br>otherwise it will be set to False.  <br>  <br>.. versionchanged:: 1.3  <br>The \`"auto"\` option is added in version 1.3 and will be the default  <br>in version 1.5.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=dual,-%22auto%22%20or%20bool%2C%20default%3D%22auto%22) | 'auto' |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive.  <br>For an intuitive visualization of the effects of scaling  <br>the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |
|     | [multi\_class multi\_class: {'ovr', 'crammer\_singer'}, default='ovr'  <br>  <br>Determines the multi-class strategy if \`y\` contains more than  <br>two classes.  <br>\`\`"ovr"\`\` trains n\_classes one-vs-rest classifiers, while  <br>\`\`"crammer\_singer"\`\` optimizes a joint objective over all classes.  <br>While \`crammer\_singer\` is interesting from a theoretical perspective  <br>as it is consistent, it is seldom used in practice as it rarely leads  <br>to better accuracy and is more expensive to compute.  <br>If \`\`"crammer\_singer"\`\` is chosen, the options loss, penalty and dual  <br>will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=multi_class,-%7B%27ovr%27%2C%20%27crammer_singer%27%7D%2C%20default%3D%27ovr%27) | 'ovr' |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether or not to fit an intercept. If set to True, the feature vector  <br>is extended to include an intercept term: \`\[x\_1, ..., x\_n, 1\]\`, where  <br>1 corresponds to the intercept. If set to False, no intercept will be  <br>used in calculations (i.e. data is expected to be already centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1.0  <br>  <br>When \`fit\_intercept\` is True, the instance vector x becomes \`\`\[x\_1,  <br>..., x\_n, intercept\_scaling\]\`\`, i.e. a "synthetic" feature with a  <br>constant value equal to \`intercept\_scaling\` is appended to the instance  <br>vector. The intercept becomes intercept\_scaling \* synthetic feature  <br>weight. Note that liblinear internally penalizes the intercept,  <br>treating it like any other term in the feature vector. To reduce the  <br>impact of the regularization on the intercept, the \`intercept\_scaling\`  <br>parameter can be set to a value greater than 1; the higher the value of  <br>\`intercept\_scaling\`, the lower the impact of regularization on it.  <br>Then, the weights become \`\[w\_x\_1, ..., w\_x\_n,  <br>w\_intercept\*intercept\_scaling\]\`, where \`w\_x\_1, ..., w\_x\_n\` represent  <br>the feature weights and the intercept weight is scaled by  <br>\`intercept\_scaling\`. This scaling allows the intercept term to have a  <br>different regularization behavior compared to the other features.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=intercept_scaling,-float%2C%20default%3D1.0) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Set the parameter C of class i to \`\`class\_weight\[i\]\*C\`\` for  <br>SVC. If not given, all classes are supposed to have  <br>weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Enable verbose output. Note that this setting takes advantage of a  <br>per-process runtime setting in liblinear that, if enabled, may not work  <br>properly in a multithreaded context.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [max\_iter max\_iter: int, default=1000  <br>  <br>The maximum number of iterations to be run.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=max_iter,-int%2C%20default%3D1000) | 1000 |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The unique classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray of shape (1, n\_features) if n\_classes == 2 else (n\_classes, n\_features)  <br>  <br>Weights assigned to the features (coefficients in the primal  <br>problem).  <br>  <br>\`\`coef\_\`\` is a readonly property derived from \`\`raw\_coef\_\`\` that  <br>follows the internal memory layout of liblinear.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=coef_,-ndarray%20of%20shape%20%281%2C%20n_features%29%20if%20n_classes%20%3D%3D%202%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 804) | \[\[ 0.03,-0.04, 0.05,..., 0. ,-0. , 0. \]\] |
| [intercept\_ intercept\_: ndarray of shape (1,) if n\_classes == 2 else (n\_classes,)  <br>  <br>Constants in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20if%20n_classes%20%3D%3D%202%20else%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.04\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=n_features_in_,-int) | int | 804 |
| [n\_iter\_ n\_iter\_: int  <br>  <br>Maximum number of iterations run across all classes.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=n_iter_,-int) | int | 53  |

  
  

### Plot the Precision-Recall curve[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#plot-the-precision-recall-curve "Link to this heading")

To plot the precision-recall curve, you should use [`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
. There are three methods available:

*   for plotting a single curve:
    
    *   [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
         for when you have not computed the predictions
        
    *   [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
         for when you already have the predictions
        
*   for plotting multiple curves using cross-validation results: [`from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_cv_results "sklearn.metrics.PrecisionRecallDisplay.from_cv_results")
    

Let’s first plot the precision-recall curve without the classifier predictions. We use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
 that computes the predictions for us before plotting the curve.

from sklearn.metrics import [PrecisionRecallDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")

display \= [PrecisionRecallDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
(
    classifier, X\_test, y\_test, name\="LinearSVC", plot\_chance\_level\=True, despine\=True
)
\_ \= display.ax\_.set\_title("2-class Precision-Recall curve")

Copy to clipboard

![2-class Precision-Recall curve](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_001.png)

If we already got the estimated probabilities or scores for our model, then we can use [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
.

y\_score \= classifier.decision\_function(X\_test)

display \= [PrecisionRecallDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
(
    y\_test, y\_score, name\="LinearSVC", plot\_chance\_level\=True, despine\=True
)
\_ \= display.ax\_.set\_title("2-class Precision-Recall curve")

Copy to clipboard

![2-class Precision-Recall curve](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_002.png)

The [`from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_cv_results "sklearn.metrics.PrecisionRecallDisplay.from_cv_results")
 takes the cross-validation results from [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 and plots a precision-recall curve for each fold.

from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

classifier \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(random\_state\=random\_state))
cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
    classifier, X\_train, y\_train, return\_estimator\=True, return\_indices\=True
)
display \= [PrecisionRecallDisplay.from\_cv\_results](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_cv_results "sklearn.metrics.PrecisionRecallDisplay.from_cv_results")
(cv\_results, X\_train, y\_train)
\_ \= display.ax\_.set\_title("Cross-validation Precision-Recall curves")

Copy to clipboard

![Cross-validation Precision-Recall curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_003.png)

In multi-label settings[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#in-multi-label-settings "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The precision-recall curve does not support the multilabel setting. However, one can decide how to handle this case. We show such an example below.

### Create multi-label data, fit, and predict[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#create-multi-label-data-fit-and-predict "Link to this heading")

We create a multi-label dataset, to illustrate the precision-recall in multi-label settings.

from sklearn.preprocessing import [label\_binarize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")

\# Use label\_binarize to be multi-label like settings
Y \= [label\_binarize](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")
(y, classes\=\[0, 1, 2\])
n\_classes \= Y.shape\[1\]

\# Split into training and test
X\_train, X\_test, Y\_train, Y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, Y, test\_size\=0.5, random\_state\=random\_state
)

Copy to clipboard

We use [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 for multi-label prediction.

from sklearn.multiclass import [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")

classifier \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
(
    [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(random\_state\=random\_state))
)
classifier.fit(X\_train, Y\_train)
y\_score \= classifier.decision\_function(X\_test)

Copy to clipboard

### The average precision score in multi-label settings[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#the-average-precision-score-in-multi-label-settings "Link to this heading")

from sklearn.metrics import [average\_precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
, [precision\_recall\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

\# For each class
precision \= dict()
recall \= dict()
average\_precision \= dict()
for i in range(n\_classes):
    precision\[i\], recall\[i\], \_ \= [precision\_recall\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
(Y\_test\[:, i\], y\_score\[:, i\])
    average\_precision\[i\] \= [average\_precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
(Y\_test\[:, i\], y\_score\[:, i\])

\# A "micro-average": quantifying score on all classes jointly
precision\["micro"\], recall\["micro"\], \_ \= [precision\_recall\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
(
    Y\_test.ravel(), y\_score.ravel()
)
average\_precision\["micro"\] \= [average\_precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
(Y\_test, y\_score, average\="micro")

Copy to clipboard

### Plot the micro-averaged Precision-Recall curve[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#plot-the-micro-averaged-precision-recall-curve "Link to this heading")

from collections import [Counter](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")

display \= [PrecisionRecallDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
(
    recall\=recall\["micro"\],
    precision\=precision\["micro"\],
    average\_precision\=average\_precision\["micro"\],
    prevalence\_pos\_label\=[Counter](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")
(Y\_test.ravel())\[1\] / Y\_test.size,
)
display.plot(plot\_chance\_level\=True, despine\=True)
\_ \= display.ax\_.set\_title("Micro-averaged over all classes")

Copy to clipboard

![Micro-averaged over all classes](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_004.png)

### Plot Precision-Recall curve for each class and iso-f1 curves[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html#plot-precision-recall-curve-for-each-class-and-iso-f1-curves "Link to this heading")

from itertools import [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")

import matplotlib.pyplot as plt

\# setup plot details
colors \= [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(\["navy", "turquoise", "darkorange", "cornflowerblue", "teal"\])

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(7, 8))

f\_scores \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.2, 0.8, num\=4)
lines, labels \= \[\], \[\]
for f\_score in f\_scores:
    x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.01, 1)
    y \= f\_score \* x / (2 \* x \- f\_score)
    (l,) \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x\[y \>= 0\], y\[y \>= 0\], color\="gray", alpha\=0.2)
    [plt.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")
("f1={0:0.1f}".format(f\_score), xy\=(0.9, y\[45\] + 0.02))

display \= [PrecisionRecallDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
(
    recall\=recall\["micro"\],
    precision\=precision\["micro"\],
    average\_precision\=average\_precision\["micro"\],
)
display.plot(
    ax\=ax, name\="Micro-average precision-recall", curve\_kwargs\={"color": "gold"}
)

for i, color in zip(range(n\_classes), colors):
    display \= [PrecisionRecallDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
(
        recall\=recall\[i\],
        precision\=precision\[i\],
        average\_precision\=average\_precision\[i\],
    )
    display.plot(
        ax\=ax,
        name\=f"Precision-recall for class {i}",
        curve\_kwargs\={"color": color},
        despine\=True,
    )

\# add the legend for the iso-f1 curves
handles, labels \= display.ax\_.get\_legend\_handles\_labels()
handles.extend(\[l\])
labels.extend(\["iso-f1 curves"\])
\# set the legend and the axes
ax.legend(handles\=handles, labels\=labels, loc\="best")
ax.set\_title("Extension of Precision-Recall curve to multi-class")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Extension of Precision-Recall curve to multi-class](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_005.png)

**Total running time of the script:** (0 minutes 0.548 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_precision_recall.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_precision_recall.ipynb)

[`Download Jupyter notebook: plot_precision_recall.ipynb`](https://scikit-learn.org/stable/_downloads/764d061a261a2e06ad21ec9133361b2d/plot_precision_recall.ipynb)

[`Download Python source code: plot_precision_recall.py`](https://scikit-learn.org/stable/_downloads/98161c8b335acb98de356229c1005819/plot_precision_recall.py)

[`Download zipped: plot_precision_recall.zip`](https://scikit-learn.org/stable/_downloads/ecdf1fb2540fbc3ff9b429164cb880c2/plot_precision_recall.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_thumb.png)

[Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)

Sparse inverse covariance estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/98161c8b335acb98de356229c1005819/plot_precision_recall.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/764d061a261a2e06ad21ec9133361b2d/plot_precision_recall.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/ecdf1fb2540fbc3ff9b429164cb880c2/plot_precision_recall.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_precision_recall.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_precision_recall.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)