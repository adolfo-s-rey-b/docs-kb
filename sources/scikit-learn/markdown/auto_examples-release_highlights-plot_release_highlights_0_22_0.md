[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-0-22-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 0.22[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#release-highlights-for-scikit-learn-0-22 "Link to this heading")

==================================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 0.22, which comes with many bug fixes and new features! We detail below a few of the major features of this release. For an exhaustive list of all the changes, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v0.22.html#release-notes-0-22)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

New plotting API[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#new-plotting-api "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

A new plotting API is available for creating visualizations. This new API allows for quickly adjusting the visuals of a plot without involving any recomputation. It is also possible to add different plots to the same figure. The following example illustrates `plot_roc_curve`, but other plots utilities are supported like `plot_partial_dependence`, `plot_precision_recall_curve`, and `plot_confusion_matrix`. Read more about this new API in the [User Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
.

import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

\# from sklearn.metrics import plot\_roc\_curve
from sklearn.metrics import RocCurveDisplay
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
from sklearn.utils.fixes import parse\_version

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(random\_state\=0)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=42)

svc \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(random\_state\=42)
svc.fit(X\_train, y\_train)
rfc \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=42)
rfc.fit(X\_train, y\_train)

\# plot\_roc\_curve has been removed in version 1.2. From 1.2, use RocCurveDisplay instead.
\# svc\_disp = plot\_roc\_curve(svc, X\_test, y\_test)
\# rfc\_disp = plot\_roc\_curve(rfc, X\_test, y\_test, ax=svc\_disp.ax\_)
svc\_disp \= [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(svc, X\_test, y\_test)
rfc\_disp \= [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(rfc, X\_test, y\_test, ax\=svc\_disp.ax\_)
rfc\_disp.figure\_.suptitle("ROC curve comparison")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![ROC curve comparison](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_001.png)

Stacking Classifier and Regressor[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#stacking-classifier-and-regressor "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
 and [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
 allow you to have a stack of estimators with a final classifier or a regressor. Stacked generalization consists in stacking the output of individual estimators and use a classifier to compute the final prediction. Stacking allows to use the strength of each individual estimator by using their output as input of a final estimator. Base estimators are fitted on the full `X` while the final estimator is trained using cross-validated predictions of the base estimators using `cross_val_predict`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#stacking)
.

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.ensemble import [StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

X, y \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
(return\_X\_y\=True)
estimators \= \[\
    ("rf", [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(n\_estimators\=10, random\_state\=42)),\
    ("svr", [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(dual\="auto", random\_state\=42))),\
\]
clf \= [StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
(estimators\=estimators, final\_estimator\=[LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
())
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=42)
clf.fit(X\_train, y\_train).score(X\_test, y\_test)

Copy to clipboard

0.9473684210526315

Copy to clipboard

Permutation-based feature importance[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#permutation-based-feature-importance "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
 can be used to get an estimate of the importance of each feature, for any fitted estimator:

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.inspection import [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(random\_state\=0, n\_features\=5, n\_informative\=3)
feature\_names \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[f"x\_{i}" for i in range(X.shape\[1\])\])

rf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=0).fit(X, y)
result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
(rf, X, y, n\_repeats\=10, random\_state\=0, n\_jobs\=2)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
sorted\_idx \= result.importances\_mean.argsort()

\# \`labels\` argument in boxplot is deprecated in matplotlib 3.9 and has been
\# renamed to \`tick\_labels\`. The following code handles this, but as a
\# scikit-learn user you probably can write simpler code by using \`labels=...\`
\# (matplotlib < 3.9) or \`tick\_labels=...\` (matplotlib >= 3.9).
tick\_labels\_parameter\_name \= (
    "tick\_labels"
    if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.9")
    else "labels"
)
tick\_labels\_dict \= {tick\_labels\_parameter\_name: feature\_names\[sorted\_idx\]}
\# \`vert\` was deprecated in matplotlib 3.11 and is replaced by \`orientation\`,
\# which is available since matplotlib 3.10. The following code handles this, but
\# as a scikit-learn user you probably can write simpler code by using
\# \`vert=False\` (matplotlib < 3.11) or \`orientation="horizontal"\`
\# (matplotlib >= 3.10).
orientation\_dict \= (
    {"orientation": "horizontal"}
    if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.10")
    else {"vert": False}
)
ax.boxplot(result.importances\[sorted\_idx\].T, \*\*orientation\_dict, \*\*tick\_labels\_dict)
ax.set\_title("Permutation Importance of each feature")
ax.set\_ylabel("Features")
fig.tight\_layout()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Permutation Importance of each feature](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_002.png)

Native support for missing values for gradient boosting[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#native-support-for-missing-values-for-gradient-boosting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 now have native support for missing values (NaNs). This means that there is no need for imputing data when training or predicting.

from sklearn.ensemble import [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1, 2, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\]).reshape(\-1, 1)
y \= \[0, 0, 1, 1\]

gbdt \= [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
(min\_samples\_leaf\=1).fit(X, y)
print(gbdt.predict(X))

Copy to clipboard

\[0 0 1 1\]

Copy to clipboard

Precomputed sparse nearest neighbors graph[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#precomputed-sparse-nearest-neighbors-graph "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most estimators based on nearest neighbors graphs now accept precomputed sparse graphs as input, to reuse the same graph for multiple estimator fits. To use this feature in a pipeline, one can use the `memory` parameter, along with one of the two new transformers, [`neighbors.KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
 and [`neighbors.RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")
. The precomputation can also be performed by custom estimators to use alternative implementations, such as approximate nearest neighbors methods. See more details in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#neighbors-transformer)
.

from tempfile import [TemporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory "tempfile.TemporaryDirectory")

from sklearn.manifold import [Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
from sklearn.neighbors import [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(random\_state\=0)

with [TemporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory "tempfile.TemporaryDirectory")
(prefix\="sklearn\_cache\_") as tmpdir:
    estimator \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
        [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
(n\_neighbors\=10, mode\="distance"),
        [Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
(n\_neighbors\=10, metric\="precomputed"),
        memory\=tmpdir,
    )
    estimator.fit(X)

    \# We can decrease the number of neighbors and the graph will not be
    \# recomputed.
    estimator.set\_params(isomap\_\_n\_neighbors\=5)
    estimator.fit(X)

Copy to clipboard

KNN Based Imputation[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#knn-based-imputation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We now support imputation for completing missing values using k-Nearest Neighbors.

Each sample’s missing values are imputed using the mean value from `n_neighbors` nearest neighbors found in the training set. Two samples are close if the features that neither is missing are close. By default, a euclidean distance metric that supports missing values, [`nan_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#sklearn.metrics.pairwise.nan_euclidean_distances "sklearn.metrics.pairwise.nan_euclidean_distances")
, is used to find the nearest neighbors.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/impute.html#knnimpute)
.

from sklearn.impute import [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")

X \= \[\[1, 2, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\], \[3, 4, 3\], \[[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
, 6, 5\], \[8, 8, 7\]\]
imputer \= [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
(n\_neighbors\=2)
print(imputer.fit\_transform(X))

Copy to clipboard

\[\[1.  2.  4. \]\
 \[3.  4.  3. \]\
 \[5.5 6.  5. \]\
 \[8.  8.  7. \]\]

Copy to clipboard

Tree pruning[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#tree-pruning "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

It is now possible to prune most tree-based estimators once the trees are built. The pruning is based on minimal cost-complexity. Read more in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)
 for details.

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(random\_state\=0)

rf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=0, ccp\_alpha\=0).fit(X, y)
print(
    "Average number of nodes without pruning {:.1f}".format(
        [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(\[e.tree\_.node\_count for e in rf.estimators\_\])
    )
)

rf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=0, ccp\_alpha\=0.05).fit(X, y)
print(
    "Average number of nodes with pruning {:.1f}".format(
        [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(\[e.tree\_.node\_count for e in rf.estimators\_\])
    )
)

Copy to clipboard

Average number of nodes without pruning 22.3
Average number of nodes with pruning 6.4

Copy to clipboard

Retrieve dataframes from OpenML[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#retrieve-dataframes-from-openml "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
 can now return pandas dataframe and thus properly handle datasets with heterogeneous data:

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

titanic \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("titanic", version\=1, as\_frame\=True, parser\="pandas")
print(titanic.data.head()\[\["pclass", "embarked"\]\])

Copy to clipboard

   pclass embarked
0       1        S
1       1        S
2       1        S
3       1        S
4       1        S

Copy to clipboard

Checking scikit-learn compatibility of an estimator[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#checking-scikit-learn-compatibility-of-an-estimator "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Developers can check the compatibility of their scikit-learn compatible estimators using [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
. For instance, the `check_estimator(LinearSVC())` passes.

We now provide a `pytest` specific decorator which allows `pytest` to run all checks independently and report the checks that are failing.

..note::

This entry was slightly updated in version 0.24, where passing classes isn’t supported anymore: pass instances instead.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
from sklearn.utils.estimator\_checks import [parametrize\_with\_checks](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")

@parametrize\_with\_checks(\[[LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(), [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
()\])
def test\_sklearn\_compatible\_estimator(estimator, check):
    check(estimator)

Copy to clipboard

ROC AUC now supports multiclass classification[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#roc-auc-now-supports-multiclass-classification "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
 function can also be used in multi-class classification. Two averaging strategies are currently supported: the one-vs-one algorithm computes the average of the pairwise ROC AUC scores, and the one-vs-rest algorithm computes the average of the ROC AUC scores for each class against all other classes. In both cases, the multiclass ROC AUC scores are computed from the probability estimates that a sample belongs to a particular class according to the model. The OvO and OvR algorithms support weighting uniformly (`average='macro'`) and weighting by the prevalence (`average='weighted'`).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_classes\=4, n\_informative\=16)
clf \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
().fit(X, y)
print([roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(y, clf.predict\_proba(X), multi\_class\="ovr"))

Copy to clipboard

0.9546666666666667

Copy to clipboard

**Total running time of the script:** (0 minutes 1.737 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_0_22_0.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_0_22_0.ipynb)

[`Download Jupyter notebook: plot_release_highlights_0_22_0.ipynb`](https://scikit-learn.org/stable/_downloads/df790541d4c6bdebcc75018a2459467a/plot_release_highlights_0_22_0.ipynb)

[`Download Python source code: plot_release_highlights_0_22_0.py`](https://scikit-learn.org/stable/_downloads/50040ae12dd16e7d2e79135d7793c17e/plot_release_highlights_0_22_0.py)

[`Download zipped: plot_release_highlights_0_22_0.zip`](https://scikit-learn.org/stable/_downloads/d731b5f8ec6b42fcb1e93a30584080e8/plot_release_highlights_0_22_0.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/50040ae12dd16e7d2e79135d7793c17e/plot_release_highlights_0_22_0.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/df790541d4c6bdebcc75018a2459467a/plot_release_highlights_0_22_0.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d731b5f8ec6b42fcb1e93a30584080e8/plot_release_highlights_0_22_0.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_0_22_0.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_0_22_0.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)