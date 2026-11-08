[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#sphx-glr-download-auto-examples-miscellaneous-plot-roc-curve-visualization-api-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

ROC Curve with Visualization API[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#roc-curve-with-visualization-api "Link to this heading")

===============================================================================================================================================================================================

Scikit-learn defines a simple API for creating visualizations for machine learning. The key features of this API is to allow for quick plotting and visual adjustments without recalculation. In this example, we will demonstrate how to use the visualization API by comparing ROC curves.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load Data and Train an SVC[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#load-data-and-train-an-svc "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we load the wine dataset and convert it to a binary classification problem. Then, we train a support vector classifier on a training dataset.

import matplotlib.pyplot as plt

from sklearn.datasets import [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.metrics import RocCurveDisplay
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

X, y \= [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
(return\_X\_y\=True)
y \= y \== 2

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=42)
svc \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(random\_state\=42)
svc.fit(X\_train, y\_train)

Copy to clipboard

SVC(random\_state=42)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

SVC

[?Documentation for SVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>probability estimates. Ignored when \`probability\` is False.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive. The penalty  <br>is a squared l2 penalty. For an intuitive visualization of the effects  <br>of scaling the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |
|     | [kernel kernel: {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'} or callable, default='rbf'  <br>  <br>Specifies the kernel type to be used in the algorithm. If  <br>none is given, 'rbf' will be used. If a callable is given it is used to  <br>pre-compute the kernel matrix from data matrices; that matrix should be  <br>an array of shape \`\`(n\_samples, n\_samples)\`\`. For an intuitive  <br>visualization of different kernel types see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_kernels.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=kernel,-%7B%27linear%27%2C%20%27poly%27%2C%20%27rbf%27%2C%20%27sigmoid%27%2C%20%27precomputed%27%7D%20or%20callable%2C%20%20%20%20%20%20%20%20%20%20default%3D%27rbf%27) | 'rbf' |
|     | [degree degree: int, default=3  <br>  <br>Degree of the polynomial kernel function ('poly').  <br>Must be non-negative. Ignored by all other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=degree,-int%2C%20default%3D3) | 3   |
|     | [gamma gamma: {'scale', 'auto'} or float, default='scale'  <br>  <br>Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.  <br>  <br>\- if \`\`gamma='scale'\`\` (default) is passed then it uses  <br>1 / (n\_features \* X.var()) as value of gamma,  <br>\- if 'auto', uses 1 / n\_features  <br>\- if float, must be non-negative.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`gamma\`\` changed from 'auto' to 'scale'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=gamma,-%7B%27scale%27%2C%20%27auto%27%7D%20or%20float%2C%20default%3D%27scale%27) | 'scale' |
|     | [coef0 coef0: float, default=0.0  <br>  <br>Independent term in kernel function.  <br>It is only significant in 'poly' and 'sigmoid'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=coef0,-float%2C%20default%3D0.0) | 0.0 |
|     | [shrinking shrinking: bool, default=True  <br>  <br>Whether to use the shrinking heuristic.  <br>See the :ref:\`User Guide <shrinking\_svm>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=shrinking,-bool%2C%20default%3DTrue) | True |
|     | [probability probability: bool, default=False  <br>  <br>Whether to enable probability estimates. This must be enabled prior  <br>to calling \`fit\`, will slow down that method as it internally uses  <br>5-fold cross-validation, and \`predict\_proba\` may be inconsistent with  <br>\`predict\`. Read more in the :ref:\`User Guide <scores\_probabilities>\`.  <br>  <br>..deprecated:: 1.9  <br>The \`probability\` parameter is deprecated and will be removed in 1.11.  <br>Use \`CalibratedClassifierCV(SVC(), ensemble=False)\` instead of  <br>\`SVC(probability=True)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probability,-bool%2C%20default%3DFalse) | 'deprecated' |
|     | [tol tol: float, default=1e-3  <br>  <br>Tolerance for stopping criterion.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=tol,-float%2C%20default%3D1e-3) | 0.001 |
|     | [cache\_size cache\_size: float, default=200  <br>  <br>Specify the size of the kernel cache (in MB).](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=cache_size,-float%2C%20default%3D200) | 200 |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Set the parameter C of class i to class\_weight\[i\]\*C for  <br>SVC. If not given, all classes are supposed to have  <br>weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>Enable verbose output. Note that this setting takes advantage of a  <br>per-process runtime setting in libsvm that, if enabled, may not work  <br>properly in a multithreaded context.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |
|     | [max\_iter max\_iter: int, default=-1  <br>  <br>Hard limit on iterations within solver, or -1 for no limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=max_iter,-int%2C%20default%3D-1) | \-1 |
|     | [decision\_function\_shape decision\_function\_shape: {'ovo', 'ovr'}, default='ovr'  <br>  <br>Whether to return a one-vs-rest ('ovr') decision function of shape  <br>(n\_samples, n\_classes) as all other classifiers, or the original  <br>one-vs-one ('ovo') decision function of libsvm which has shape  <br>(n\_samples, n\_classes \* (n\_classes - 1) / 2). However, note that  <br>internally, one-vs-one ('ovo') is always used as a multi-class strategy  <br>to train models; an ovr matrix is only constructed from the ovo matrix.  <br>The parameter is ignored for binary classification.  <br>  <br>.. versionchanged:: 0.19  <br>decision\_function\_shape is 'ovr' by default.  <br>  <br>.. versionadded:: 0.17  <br>\*decision\_function\_shape='ovr'\* is recommended.  <br>  <br>.. versionchanged:: 0.17  <br>Deprecated \*decision\_function\_shape='ovo' and None\*.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=decision_function_shape,-%7B%27ovo%27%2C%20%27ovr%27%7D%2C%20default%3D%27ovr%27) | 'ovr' |
|     | [break\_ties break\_ties: bool, default=False  <br>  <br>If true, \`\`decision\_function\_shape='ovr'\`\`, and number of classes > 2,  <br>:term:\`predict\` will break ties according to the confidence values of  <br>:term:\`decision\_function\`; otherwise the first class among the tied  <br>classes is returned. Please note that breaking ties comes at a  <br>relatively high computational cost compared to a simple predict. See  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_tie\_breaking.py\` for an  <br>example of its usage with \`\`decision\_function\_shape='ovr'\`\`.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=break_ties,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [class\_weight\_ class\_weight\_: ndarray of shape (n\_classes,)  <br>  <br>Multipliers of parameter C for each class.  <br>Computed based on the \`\`class\_weight\`\` parameter.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=class_weight_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[float64\](2,) | \[1.,1.\] |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[bool\](2,) | \[False, True\] |
| [dual\_coef\_ dual\_coef\_: ndarray or sparse array/matrix of shape (n\_classes -1, n\_SV)  <br>  <br>Dual coefficients of the support vector in the decision  <br>function (see :ref:\`sgd\_mathematical\_formulation\`), multiplied by  <br>their targets.  <br>For multiclass, coefficient for all 1-vs-1 classifiers.  <br>The layout of the coefficients in the multiclass case is somewhat  <br>non-trivial. See the :ref:\`multi-class section of the User Guide  <br><svm\_multi\_class>\` for details.  <br>If \`X\` is sparse, these will also be sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=dual_coef_,-ndarray%20or%20sparse%20array/matrix%20of%20shape%20%28n_classes%20-1%2C%20n_SV%29) | ndarray\[float64\](1, 73) | \[\[-1.,-1.,-1.,..., 1., 1., 1.\]\] |
| [fit\_status\_ fit\_status\_: int  <br>  <br>0 if correctly fitted, 1 otherwise (will raise warning)](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=fit_status_,-int) | int | 0   |
| [intercept\_ intercept\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2,)  <br>  <br>Constants in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=intercept_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%2C%29) | ndarray\[float64\](1,) | \[-1.1\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_features_in_,-int) | int | 13  |
| [n\_iter\_ n\_iter\_: ndarray of shape (n\_classes \* (n\_classes - 1) // 2,)  <br>  <br>Number of iterations run by the optimization routine to fit the model.  <br>The shape of this attribute depends on the number of models optimized  <br>which in turn depends on the number of classes.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_iter_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20//%202%2C%29) | ndarray\[int32\](1,) | \[45\] |
| [n\_support\_ n\_support\_: ndarray of shape (n\_classes,), dtype=int32  <br>  <br>Number of support vectors for each class.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_support_,-ndarray%20of%20shape%20%28n_classes%2C%29%2C%20dtype%3Dint32) | ndarray\[int32\](2,) | \[37,36\] |
| [probA\_ probA\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2)  <br>  <br>If \`probability=True\`, it corresponds to the parameters learned in  <br>Platt scaling to produce probability estimates from decision values.  <br>If \`probability=False\`, it's an empty array. Platt scaling uses the  <br>logistic function](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probA_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%29) | ndarray\[float64\](0,) | \[\] |
| [probB\_ probB\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2)  <br>  <br>If \`probability=True\`, it corresponds to the parameters learned in  <br>Platt scaling. Platt scaling uses the logistic function  <br>\`\`1 / (1 + exp(decision\_value \* probA\_ + probB\_))\`\`  <br>where \`\`probA\_\`\` and \`\`probB\_\`\` are learned from the dataset \[2\]\_. For  <br>more information on the multiclass case and training procedure see  <br>section 8 of \[1\]\_.  <br>  <br>.. deprecated:: 1.9  <br>The attributes \`probA\_\` and \`probB\_\` are deprecated in version 1.9 and will  <br>be removed in 1.11.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probB_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%29) | ndarray\[float64\](0,) | \[\] |
| [shape\_fit\_ shape\_fit\_: tuple of int of shape (n\_dimensions\_of\_X,)  <br>  <br>Array dimensions of training vector \`\`X\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=shape_fit_,-tuple%20of%20int%20of%20shape%20%28n_dimensions_of_X%2C%29) | tuple | (133, 13) |
| [support\_ support\_: ndarray of shape (n\_SV)  <br>  <br>Indices of support vectors.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=support_,-ndarray%20of%20shape%20%28n_SV%29) | ndarray\[int32\](73,) | \[ 1, 10, 11,...,118,119,126\] |
| [support\_vectors\_ support\_vectors\_: ndarray or sparse array/matrix of shape (n\_SV, n\_features)  <br>  <br>Support vectors. An empty array if kernel is precomputed.  <br>If \`X\` is sparse, these will also be sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=support_vectors_,-ndarray%20or%20sparse%20array/matrix%20of%20shape%20%28n_SV%2C%20n_features%29) | ndarray\[float64\](73, 13) | \[\[ 12.08, 2.08, 1.7 ,..., 1.27, 2.96,710. \], \[ 12.51, 1.73, 1.98,..., 1.04, 3.57,672. \], \[ 12.33, 0.99, 1.95,..., 1.06, 2.31,750. \], ..., \[ 12.86, 1.35, 2.32,..., 0.76, 1.29,630. \], \[ 12.79, 2.67, 2.48,..., 0.48, 1.47,480. \], \[ 14.13, 4.1 , 2.74,..., 0.61, 1.6 ,560. \]\] |

  
  

Plotting the ROC Curve[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#plotting-the-roc-curve "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, we plot the ROC curve with a single call to [`sklearn.metrics.RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
. The returned `svc_disp` object allows us to continue using the already computed ROC curve for the SVC in future plots.

svc\_disp \= [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(svc, X\_test, y\_test)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot roc curve visualization api](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_001.png)

Training a Random Forest and Plotting the ROC Curve[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#training-a-random-forest-and-plotting-the-roc-curve "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We train a random forest classifier and create a plot comparing it to the SVC ROC curve. Notice how `svc_disp` uses [`plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.plot "sklearn.metrics.RocCurveDisplay.plot")
 to plot the SVC ROC curve without recomputing the values of the roc curve itself. Furthermore, we pass `alpha=0.8` to the plot functions to adjust the alpha values of the curves.

rfc \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(n\_estimators\=10, random\_state\=42)
rfc.fit(X\_train, y\_train)
ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
rfc\_disp \= [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(
    rfc, X\_test, y\_test, ax\=ax, curve\_kwargs\=dict(alpha\=0.8)
)
svc\_disp.plot(ax\=ax, curve\_kwargs\=dict(alpha\=0.8))
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot roc curve visualization api](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_002.png)

**Total running time of the script:** (0 minutes 0.186 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_roc_curve_visualization_api.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_roc_curve_visualization_api.ipynb)

[`Download Jupyter notebook: plot_roc_curve_visualization_api.ipynb`](https://scikit-learn.org/stable/_downloads/3577ee5e1121d4b5da38feb779aa44bb/plot_roc_curve_visualization_api.ipynb)

[`Download Python source code: plot_roc_curve_visualization_api.py`](https://scikit-learn.org/stable/_downloads/837ade0d39a9ca8d8a3cc25eb9433a58/plot_roc_curve_visualization_api.py)

[`Download zipped: plot_roc_curve_visualization_api.zip`](https://scikit-learn.org/stable/_downloads/1630d9144544d31ca40f70d5ce894b1c/plot_roc_curve_visualization_api.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/837ade0d39a9ca8d8a3cc25eb9433a58/plot_roc_curve_visualization_api.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3577ee5e1121d4b5da38feb779aa44bb/plot_roc_curve_visualization_api.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1630d9144544d31ca40f70d5ce894b1c/plot_roc_curve_visualization_api.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_roc_curve_visualization_api.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_roc_curve_visualization_api.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)