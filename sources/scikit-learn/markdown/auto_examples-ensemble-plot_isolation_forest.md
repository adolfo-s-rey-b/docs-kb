[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_isolation_forest.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_isolation_forest.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_isolation_forest.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_isolation_forest.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_isolation_forest.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_isolation_forest.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#sphx-glr-download-auto-examples-ensemble-plot-isolation-forest-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

IsolationForest example[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#isolationforest-example "Link to this heading")

=============================================================================================================================================================

An example using [`IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
 for anomaly detection.

The [Isolation Forest](https://scikit-learn.org/stable/modules/outlier_detection.html#isolation-forest)
 is an ensemble of “Isolation Trees” that “isolate” observations by recursive random partitioning, which can be represented by a tree structure. The number of splittings required to isolate a sample is lower for outliers and higher for inliers.

In the present example we demo two ways to visualize the decision boundary of an Isolation Forest trained on a toy dataset.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#data-generation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

We generate two clusters (each one containing `n_samples`) by randomly sampling the standard normal distribution as returned by [`numpy.random.randn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "(in NumPy v2.5)")
. One of them is spherical and the other one is slightly deformed.

For consistency with the [`IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
 notation, the inliers (i.e. the gaussian clusters) are assigned a ground truth label `1` whereas the outliers (created with [`numpy.random.uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "(in NumPy v2.5)")
) are assigned the label `-1`.

import numpy as np

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

n\_samples, n\_outliers \= 120, 40
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
covariance \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.5, \-0.1\], \[0.7, 0.4\]\])
cluster\_1 \= 0.4 \* rng.randn(n\_samples, 2) @ covariance + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[2, 2\])  \# general
cluster\_2 \= 0.3 \* rng.randn(n\_samples, 2) + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\-2, \-2\])  \# spherical
outliers \= rng.uniform(low\=-4, high\=4, size\=(n\_outliers, 2))

X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[cluster\_1, cluster\_2, outliers\])
y \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(
    \[[np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")\
((2 \* n\_samples), dtype\=int), \-[np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")\
((n\_outliers), dtype\=int)\]
)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=42)

Copy to clipboard

We can visualize the resulting clusters:

import matplotlib.pyplot as plt

scatter \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y, s\=20, edgecolor\="k")
handles, labels \= scatter.legend\_elements()
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("square")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(handles\=handles, labels\=\["outliers", "inliers"\], title\="true class")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Gaussian inliers with \\nuniformly distributed outliers")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Gaussian inliers with  uniformly distributed outliers](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_001.png)

Training of the model[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#training-of-the-model "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.ensemble import [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")

clf \= [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
(max\_samples\=100, random\_state\=0)
clf.fit(X\_train)

Copy to clipboard

IsolationForest(max\_samples=100, random\_state=0)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

IsolationForest

[?Documentation for IsolationForest](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [max\_samples max\_samples: "auto", int or float, default="auto"  <br>  <br>The number of samples to draw from X to train each base estimator.  <br>  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` samples.  <br>\- If "auto", then \`max\_samples=min(256, n\_samples)\`.  <br>  <br>If max\_samples is larger than the number of samples provided,  <br>all samples will be used for all trees (no sampling).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=max_samples,-%22auto%22%2C%20int%20or%20float%2C%20default%3D%22auto%22) | 100 |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo-randomness of the selection of the feature  <br>and split values for each branching step and each tree in the forest.  <br>  <br>Pass an int for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of base estimators in the ensemble.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |
|     | [contamination contamination: 'auto' or float, default='auto'  <br>  <br>The amount of contamination of the data set, i.e. the proportion  <br>of outliers in the data set. Used when fitting to define the threshold  <br>on the scores of the samples.  <br>  <br>\- If 'auto', the threshold is determined as in the  <br>original paper.  <br>\- If float, the contamination should be in the range (0, 0.5\].  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`contamination\`\` changed from 0.1  <br>to \`\`'auto'\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=contamination,-%27auto%27%20or%20float%2C%20default%3D%27auto%27) | 'auto' |
|     | [max\_features max\_features: int or float, default=1.0  <br>  <br>The number of features to draw from X to train each base estimator.  <br>  <br>\- If int, then draw \`max\_features\` features.  <br>\- If float, then draw \`max(1, int(max\_features \* n\_features\_in\_))\` features.  <br>  <br>Note: using a float number less than 1.0 or integer less than number of  <br>features will enable feature subsampling and leads to a longer runtime.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=max_features,-int%20or%20float%2C%20default%3D1.0) | 1.0 |
|     | [bootstrap bootstrap: bool, default=False  <br>  <br>If True, individual trees are fit on random subsets of the training  <br>data sampled with replacement. If False, sampling without replacement  <br>is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=bootstrap,-bool%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel for :meth:\`fit\`. \`\`None\`\` means 1  <br>unless in a :obj:\`joblib.parallel\_backend\` context. \`\`-1\`\` means using  <br>all processors. See :term:\`Glossary <n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of the tree building process.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.21](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [estimator\_ estimator\_: :class:\`~sklearn.tree.ExtraTreeRegressor\` instance  <br>  <br>The child estimator template used to create the collection of  <br>fitted sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.ExtraTreeRegressor%20instance) | ExtraTreeRegressor | ExtraTreeRegr...andom\_state=0) |
| [estimators\_ estimators\_: list of ExtraTreeRegressor instances  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=estimators_,-list%20of%20ExtraTreeRegressor%20instances) | list | \[ExtraTreeRegr...te=2087557356), ExtraTreeRegr...ate=132990059), ExtraTreeRegr...te=1109697837), ExtraTreeRegr...ate=123230084), ...\] |
| [estimators\_features\_ estimators\_features\_: list of ndarray  <br>  <br>The subset of drawn features for each base estimator.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=estimators_features_,-list%20of%20ndarray) | list | \[array(\[0, 1\]), array(\[0, 1\]), array(\[0, 1\]), array(\[0, 1\]), ...\] |
| [estimators\_samples\_ estimators\_samples\_: list of ndarray  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=estimators_samples_,-list%20of%20ndarray) | list | \[array(\[131, ...57, 12, 61\]), array(\[ 3, 1...36, 124, 16\]), array(\[146, ...16, 124, 78\]), array(\[183, 1...99, 61, 78\]), ...\] |
| [max\_samples\_ max\_samples\_: int  <br>  <br>The actual number of samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=max_samples_,-int) | int | 100 |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=n_features_in_,-int) | int | 2   |
| [offset\_ offset\_: float  <br>  <br>Offset used to define the decision function from the raw scores. We  <br>have the relation: \`\`decision\_function = score\_samples - offset\_\`\`.  <br>\`\`offset\_\`\` is defined as follows. When the contamination parameter is  <br>set to "auto", the offset is equal to -0.5 as the scores of inliers are  <br>close to 0 and the scores of outliers are close to -1. When a  <br>contamination parameter different than "auto" is provided, the offset  <br>is defined in such a way we obtain the expected number of outliers  <br>(samples with decision function < 0) in training.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.IsolationForest.html#:~:text=offset_,-float) | float | \-0.5 |

  
  

Plot discrete decision boundary[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#plot-discrete-decision-boundary "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We use the class [`DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
 to visualize a discrete decision boundary. The background color represents whether a sample in that given area is predicted to be an outlier or not. The scatter plot displays the true labels.

import matplotlib.pyplot as plt

from sklearn.inspection import DecisionBoundaryDisplay

disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    response\_method\="predict",
    alpha\=0.5,
)
disp.ax\_.scatter(X\[:, 0\], X\[:, 1\], c\=y, s\=20, edgecolor\="k")
disp.ax\_.set\_title("Binary decision boundary \\nof IsolationForest")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("square")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(handles\=handles, labels\=\["outliers", "inliers"\], title\="true class")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Binary decision boundary  of IsolationForest](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_002.png)

Plot path length decision boundary[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html#plot-path-length-decision-boundary "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By setting the `response_method="decision_function"`, the background of the [`DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
 represents the measure of normality of an observation. Such score is given by the path length averaged over a forest of random trees, which itself is given by the depth of the leaf (or equivalently the number of splits) required to isolate a given sample.

When a forest of random trees collectively produce short path lengths for isolating some particular samples, they are highly likely to be anomalies and the measure of normality is close to `0`. Similarly, large paths correspond to values close to `1` and are more likely to be inliers.

disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    response\_method\="decision\_function",
    alpha\=0.5,
)
disp.ax\_.scatter(X\[:, 0\], X\[:, 1\], c\=y, s\=20, edgecolor\="k")
disp.ax\_.set\_title("Path length decision boundary \\nof IsolationForest")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("square")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(handles\=handles, labels\=\["outliers", "inliers"\], title\="true class")
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(disp.ax\_.collections\[1\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Path length decision boundary  of IsolationForest](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_003.png)

**Total running time of the script:** (0 minutes 0.577 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_isolation_forest.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_isolation_forest.ipynb)

[`Download Jupyter notebook: plot_isolation_forest.ipynb`](https://scikit-learn.org/stable/_downloads/f39c19ddd9f1c49a604c054eff707568/plot_isolation_forest.ipynb)

[`Download Python source code: plot_isolation_forest.py`](https://scikit-learn.org/stable/_downloads/2108844cb1b17bae9a6b4c0b0fb3b211/plot_isolation_forest.py)

[`Download zipped: plot_isolation_forest.zip`](https://scikit-learn.org/stable/_downloads/452ef11734eef7e89e9b6f7bb4bcb108/plot_isolation_forest.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_thumb.png)

[Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)

Two-class AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_thumb.png)

[Theil-Sen Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)

Theil-Sen Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/2108844cb1b17bae9a6b4c0b0fb3b211/plot_isolation_forest.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f39c19ddd9f1c49a604c054eff707568/plot_isolation_forest.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/452ef11734eef7e89e9b6f7bb4bcb108/plot_isolation_forest.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_isolation_forest.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_isolation_forest.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)