[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-3-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.3[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#release-highlights-for-scikit-learn-1-3 "Link to this heading")

===============================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 1.3! Many bug fixes and improvements were added, as well as some new key features. We detail below a few of the major features of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.3.html#release-notes-1-3)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

Metadata Routing[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#metadata-routing "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

We are in the process of introducing a new way to route metadata such as `sample_weight` throughout the codebase, which would affect how meta-estimators such as [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 and [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 route metadata. While the infrastructure for this feature is already included in this release, the work is ongoing and not all meta-estimators support this new feature. You can read more about this feature in the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
. Note that this feature is still under development and not implemented for most meta-estimators.

Third party developers can already start incorporating this into their meta-estimators. For more details, see [metadata routing developer guide](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-auto-examples-miscellaneous-plot-metadata-routing-py)
.

HDBSCAN: hierarchical density-based clustering[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#hdbscan-hierarchical-density-based-clustering "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Originally hosted in the scikit-learn-contrib repository, [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
 has been adpoted into scikit-learn. It’s missing a few features from the original implementation which will be added in future releases. By performing a modified version of [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
 over multiple epsilon values simultaneously, [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
 finds clusters of varying densities making it more robust to parameter selection than [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
. More details in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#hdbscan)
.

import numpy as np

from sklearn.cluster import [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.metrics import [v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")

X, true\_labels \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
print(f"number of digits: {len([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(true\_labels))}")

hdbscan \= [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(min\_cluster\_size\=15, copy\=True).fit(X)
non\_noisy\_labels \= hdbscan.labels\_\[hdbscan.labels\_ != \-1\]
print(f"number of clusters found: {len([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(non\_noisy\_labels))}")

print([v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
(true\_labels\[hdbscan.labels\_ != \-1\], non\_noisy\_labels))

Copy to clipboard

number of digits: 10
number of clusters found: 11
0.9694898472080092

Copy to clipboard

TargetEncoder: a new category encoding strategy[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#targetencoder-a-new-category-encoding-strategy "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Well suited for categorical features with high cardinality, [`preprocessing.TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
 encodes the categories based on a shrunk estimate of the average target values for observations belonging to that category. More details in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
.

import numpy as np

from sklearn.model\_selection import [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
from sklearn.preprocessing import [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\["cat"\] \* 30 + \["dog"\] \* 20 + \["snake"\] \* 38\], dtype\=object).T
y \= \[90.3\] \* 30 + \[20.4\] \* 20 + \[21.2\] \* 38

enc \= [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
(cv\=[KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(shuffle\=True, random\_state\=0))
X\_trans \= enc.fit\_transform(X, y)

enc.encodings\_

Copy to clipboard

\[array(\[90.3, 20.4, 21.2\])\]

Copy to clipboard

Missing values support in decision trees[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#missing-values-support-in-decision-trees "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The classes [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
 now support missing values. For each potential threshold on the non-missing data, the splitter will evaluate the split with all the missing values going to the left node or the right node. See more details in the [User Guide](https://scikit-learn.org/stable/modules/tree.html#tree-missing-value-support)
 or see [Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-auto-examples-ensemble-plot-hgbt-regression-py)
 for a usecase example of this feature in [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
.

import numpy as np

from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1, 6, [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\]).reshape(\-1, 1)
y \= \[0, 0, 1, 1\]

tree \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(random\_state\=0).fit(X, y)
tree.predict(X)

Copy to clipboard

array(\[0, 0, 1, 1\])

Copy to clipboard

New display [`ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")
[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#new-display-validationcurvedisplay "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`model_selection.ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")
 is now available to plot results from [`model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import ValidationCurveDisplay

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(1000, 10, random\_state\=0)

\_ \= [ValidationCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay.from_estimator "sklearn.model_selection.ValidationCurveDisplay.from_estimator")
(
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(),
    X,
    y,
    param\_name\="C",
    param\_range\=[np.geomspace](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")
(1e-5, 1e3, num\=9),
    score\_type\="both",
    score\_name\="Accuracy",
)

Copy to clipboard

![plot release highlights 1 3 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_001.png)

Gamma loss for gradient boosting[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#gamma-loss-for-gradient-boosting "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The class [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 supports the Gamma deviance loss function via `loss="gamma"`. This loss function is useful for modeling strictly positive targets with a right-skewed distribution.

import numpy as np

from sklearn.datasets import [make\_low\_rank\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix")
from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.model\_selection import [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")

n\_samples, n\_features \= 500, 10
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X \= [make\_low\_rank\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix")
(n\_samples, n\_features, random\_state\=rng)
coef \= rng.uniform(low\=-10, high\=20, size\=n\_features)
y \= rng.gamma(shape\=2, scale\=[np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(X @ coef) / 2)
gbdt \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(loss\="gamma")
[cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(gbdt, X, y).mean()

Copy to clipboard

np.float64(0.44587161562873445)

Copy to clipboard

Grouping infrequent categories in [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#grouping-infrequent-categories-in-ordinalencoder "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Similarly to [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, the class [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
 now supports aggregating infrequent categories into a single output for each feature. The parameters to enable the gathering of infrequent categories are `min_frequency` and `max_categories`. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)
 for more details.

import numpy as np

from sklearn.preprocessing import [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[\["dog"\] \* 5 + \["cat"\] \* 20 + \["rabbit"\] \* 10 + \["snake"\] \* 3\], dtype\=object
).T
enc \= [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
(min\_frequency\=6).fit(X)
enc.infrequent\_categories\_

Copy to clipboard

\[array(\['dog', 'snake'\], dtype=object)\]

Copy to clipboard

**Total running time of the script:** (0 minutes 1.284 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_3_0.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_3_0.ipynb)

[`Download Jupyter notebook: plot_release_highlights_1_3_0.ipynb`](https://scikit-learn.org/stable/_downloads/0785ea6d45bde062e5beedda88131215/plot_release_highlights_1_3_0.ipynb)

[`Download Python source code: plot_release_highlights_1_3_0.py`](https://scikit-learn.org/stable/_downloads/3316f301d7c7651c033565a5ae51c295/plot_release_highlights_1_3_0.py)

[`Download zipped: plot_release_highlights_1_3_0.zip`](https://scikit-learn.org/stable/_downloads/27381e4bd5a9b2476f7ed4a8c0d7c8a2/plot_release_highlights_1_3_0.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/3316f301d7c7651c033565a5ae51c295/plot_release_highlights_1_3_0.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0785ea6d45bde062e5beedda88131215/plot_release_highlights_1_3_0.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/27381e4bd5a9b2476f7ed4a8c0d7c8a2/plot_release_highlights_1_3_0.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_3_0.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_3_0.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)