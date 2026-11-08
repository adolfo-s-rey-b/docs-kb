[Skip to main content](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#sphx-glr-download-auto-examples-inspection-plot-permutation-importance-multicollinear-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Permutation Importance with Multicollinear or Correlated Features[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#permutation-importance-with-multicollinear-or-correlated-features "Link to this heading")

========================================================================================================================================================================================================================================================================

In this example, we compute the [`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
 of the features to a trained [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 using the [Breast cancer Wisconsin (diagnostic) dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset)
. The model can easily get about 97% accuracy on a test dataset. Because this dataset contains multicollinear features, the permutation importance shows that none of the features are important, in contradiction with the high test accuracy.

We demo a possible approach to handling multicollinearity, which consists of hierarchical clustering on the features’ Spearman rank-order correlations, picking a threshold, and keeping a single feature from each cluster.

Note

See also [Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Random Forest Feature Importance on Breast Cancer Data[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#random-forest-feature-importance-on-breast-cancer-data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we define a function to ease the plotting:

import matplotlib

from sklearn.inspection import [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
from sklearn.utils.fixes import parse\_version

def plot\_permutation\_importance(clf, X, y, ax):
    result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
(clf, X, y, n\_repeats\=10, random\_state\=42, n\_jobs\=2)
    perm\_sorted\_idx \= result.importances\_mean.argsort()

    \# \`labels\` argument in boxplot is deprecated in matplotlib 3.9 and has been
    \# renamed to \`tick\_labels\`. The following code handles this, but as a
    \# scikit-learn user you probably can write simpler code by using \`labels=...\`
    \# (matplotlib < 3.9) or \`tick\_labels=...\` (matplotlib >= 3.9).
    tick\_labels\_parameter\_name \= (
        "tick\_labels"
        if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.9")
        else "labels"
    )
    tick\_labels\_dict \= {tick\_labels\_parameter\_name: X.columns\[perm\_sorted\_idx\]}
    \# \`vert\` was deprecated in matplotlib 3.11 and is replaced by \`orientation\`,
    \# which is available since matplotlib 3.10. The following code handles this,
    \# but as a scikit-learn user you probably can write simpler code by using
    \# \`vert=False\` (matplotlib < 3.11) or \`orientation="horizontal"\`
    \# (matplotlib >= 3.10).
    orientation\_dict \= (
        {"orientation": "horizontal"}
        if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.10")
        else {"vert": False}
    )
    ax.boxplot(
        result.importances\[perm\_sorted\_idx\].T, \*\*orientation\_dict, \*\*tick\_labels\_dict
    )
    ax.axvline(x\=0, color\="k", linestyle\="--")
    return ax

Copy to clipboard

We then train a [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 on the [Breast cancer Wisconsin (diagnostic) dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset)
 and evaluate its accuracy on a test set:

from sklearn.datasets import [load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
(return\_X\_y\=True, as\_frame\=True)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=42)

clf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(n\_estimators\=100, random\_state\=42)
clf.fit(X\_train, y\_train)
print(f"Baseline accuracy on test data: {clf.score(X\_test, y\_test):.2}")

Copy to clipboard

Baseline accuracy on test data: 0.97

Copy to clipboard

Next, we plot the tree based feature importance and the permutation importance. The permutation importance is calculated on the training set to show how much the model relies on each feature during training.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mdi\_importances \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
(clf.feature\_importances\_, index\=X\_train.columns)
tree\_importance\_sorted\_idx \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(clf.feature\_importances\_)

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(12, 8))
mdi\_importances.sort\_values().plot.barh(ax\=ax1)
ax1.set\_xlabel("Gini importance")
plot\_permutation\_importance(clf, X\_train, y\_train, ax2)
ax2.set\_xlabel("Decrease in accuracy score")
fig.suptitle(
    "Impurity-based vs. permutation importances on multicollinear features (train set)"
)
\_ \= fig.tight\_layout()

Copy to clipboard

![Impurity-based vs. permutation importances on multicollinear features (train set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_001.png)

The plot on the left shows the Gini importance of the model. As the scikit-learn implementation of [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 uses a random subsets of nfeatures features at each split, it is able to dilute the dominance of any single correlated feature. As a result, the individual feature importance may be distributed more evenly among the correlated features. Since the features have large cardinality and the classifier is non-overfitted, we can relatively trust those values.

The permutation importance on the right plot shows that permuting a feature drops the accuracy by at most `0.012`, which would suggest that none of the features are important. This is in contradiction with the high test accuracy computed as baseline: some feature must be important.

Similarly, the change in accuracy score computed on the test set appears to be driven by chance:

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(7, 6))
plot\_permutation\_importance(clf, X\_test, y\_test, ax)
ax.set\_title("Permutation Importances on multicollinear features\\n(test set)")
ax.set\_xlabel("Decrease in accuracy score")
\_ \= ax.figure.tight\_layout()

Copy to clipboard

![Permutation Importances on multicollinear features (test set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_002.png)

Nevertheless, one can still compute a meaningful permutation importance in the presence of correlated features, as demonstrated in the following section.

Handling Multicollinear Features[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#handling-multicollinear-features "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When features are collinear, permuting one feature has little effect on the models performance because it can get the same information from a correlated feature. Note that this is not the case for all predictive models and depends on their underlying implementation.

One way to handle multicollinear features is by performing hierarchical clustering on the Spearman rank-order correlations, picking a threshold, and keeping a single feature from each cluster. First, we plot a heatmap of the correlated features:

from scipy.cluster import hierarchy
from scipy.spatial.distance import [squareform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform "scipy.spatial.distance.squareform")
from scipy.stats import [spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr "scipy.stats.spearmanr")

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(12, 8))
corr \= [spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr "scipy.stats.spearmanr")
(X).correlation

\# Ensure the correlation matrix is symmetric
corr \= (corr + corr.T) / 2
[np.fill\_diagonal](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#numpy.fill_diagonal "numpy.fill_diagonal")
(corr, 1)

\# We convert the correlation matrix to a distance matrix before performing
\# hierarchical clustering using Ward's linkage.
distance\_matrix \= 1 \- np.abs(corr)
dist\_linkage \= [hierarchy.ward](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.ward.html#scipy.cluster.hierarchy.ward "scipy.cluster.hierarchy.ward")
([squareform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform "scipy.spatial.distance.squareform")
(distance\_matrix))
dendro \= [hierarchy.dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram "scipy.cluster.hierarchy.dendrogram")
(
    dist\_linkage, labels\=X.columns.to\_list(), ax\=ax1, leaf\_rotation\=90
)
dendro\_idx \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, len(dendro\["ivl"\]))

ax2.imshow(corr\[dendro\["leaves"\], :\]\[:, dendro\["leaves"\]\])
ax2.set\_xticks(dendro\_idx)
ax2.set\_yticks(dendro\_idx)
ax2.set\_xticklabels(dendro\["ivl"\], rotation\="vertical")
ax2.set\_yticklabels(dendro\["ivl"\])
\_ \= fig.tight\_layout()

Copy to clipboard

![plot permutation importance multicollinear](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_003.png)

Next, we manually pick a threshold by visual inspection of the dendrogram to group our features into clusters and choose a feature from each cluster to keep, select those features from our dataset, and train a new random forest. The test accuracy of the new random forest did not change much compared to the random forest trained on the complete dataset.

from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")

cluster\_ids \= [hierarchy.fcluster](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html#scipy.cluster.hierarchy.fcluster "scipy.cluster.hierarchy.fcluster")
(dist\_linkage, 1, criterion\="distance")
cluster\_id\_to\_feature\_ids \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
for idx, cluster\_id in enumerate(cluster\_ids):
    cluster\_id\_to\_feature\_ids\[cluster\_id\].append(idx)
selected\_features \= \[v\[0\] for v in cluster\_id\_to\_feature\_ids.values()\]
selected\_features\_names \= X.columns\[selected\_features\]

X\_train\_sel \= X\_train\[selected\_features\_names\]
X\_test\_sel \= X\_test\[selected\_features\_names\]

clf\_sel \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(n\_estimators\=100, random\_state\=42)
clf\_sel.fit(X\_train\_sel, y\_train)
print(
    "Baseline accuracy on test data with features removed:"
    f" {clf\_sel.score(X\_test\_sel, y\_test):.2}"
)

Copy to clipboard

Baseline accuracy on test data with features removed: 0.97

Copy to clipboard

We can finally explore the permutation importance of the selected subset of features:

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(7, 6))
plot\_permutation\_importance(clf\_sel, X\_test\_sel, y\_test, ax)
ax.set\_title("Permutation Importances on selected subset of features\\n(test set)")
ax.set\_xlabel("Decrease in accuracy score")
ax.figure.tight\_layout()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Permutation Importances on selected subset of features (test set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_004.png)

**Total running time of the script:** (0 minutes 8.331 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_permutation_importance_multicollinear.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_permutation_importance_multicollinear.ipynb)

[`Download Jupyter notebook: plot_permutation_importance_multicollinear.ipynb`](https://scikit-learn.org/stable/_downloads/4941b506cc56c9cec00d40992e2a4207/plot_permutation_importance_multicollinear.ipynb)

[`Download Python source code: plot_permutation_importance_multicollinear.py`](https://scikit-learn.org/stable/_downloads/756be88c4ccd4c7bba02ab13f0d3258a/plot_permutation_importance_multicollinear.py)

[`Download zipped: plot_permutation_importance_multicollinear.zip`](https://scikit-learn.org/stable/_downloads/2f90cc6b2b011c5fa616a3a47c2ed8d1/plot_permutation_importance_multicollinear.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_thumb.png)

[Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

Feature importances with a forest of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/756be88c4ccd4c7bba02ab13f0d3258a/plot_permutation_importance_multicollinear.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/4941b506cc56c9cec00d40992e2a4207/plot_permutation_importance_multicollinear.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2f90cc6b2b011c5fa616a3a47c2ed8d1/plot_permutation_importance_multicollinear.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_permutation_importance_multicollinear.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_permutation_importance_multicollinear.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)