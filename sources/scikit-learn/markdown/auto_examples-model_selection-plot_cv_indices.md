[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_cv_indices.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_cv_indices.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_cv_indices.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_cv_indices.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_cv_indices.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_cv_indices.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-download-auto-examples-model-selection-plot-cv-indices-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Visualizing cross-validation behavior in scikit-learn[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualizing-cross-validation-behavior-in-scikit-learn "Link to this heading")

==========================================================================================================================================================================================================================

Choosing the right cross-validation object is a crucial part of fitting a model properly. There are many ways to split data into training and test sets in order to avoid model overfitting, to standardize the number of groups in test sets, etc.

This example visualizes the behavior of several common scikit-learn objects for comparison.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import [Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")

from sklearn.model\_selection import (
    [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
,
    [GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")
,
    [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
,
    [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
,
    [StratifiedGroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")
,
    [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
,
    [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
,
    [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
,
)

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1338)
cmap\_data \= plt.cm.Paired
cmap\_cv \= plt.cm.coolwarm
n\_splits \= 4

Copy to clipboard

Visualize our data[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualize-our-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

First, we must understand the structure of our data. It has 100 randomly generated input datapoints, 3 classes split unevenly across datapoints, and 10 “groups” split evenly across datapoints.

As we’ll see, some cross-validation objects do specific things with labeled data, others behave differently with grouped data, and others do not use this information.

To begin, we’ll visualize our data.

\# Generate the class/group data
n\_points \= 100
X \= rng.randn(100, 10)

percentiles\_classes \= \[0.1, 0.3, 0.6\]
y \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(\[\[ii\] \* int(100 \* perc) for ii, perc in enumerate(percentiles\_classes)\])

\# Generate uneven groups
group\_prior \= rng.dirichlet(\[2\] \* 10)
groups \= [np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10), rng.multinomial(100, group\_prior))

def visualize\_groups(classes, groups, name):
    \# Visualize dataset groups
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    ax.scatter(
        range(len(groups)),
        \[0.5\] \* len(groups),
        c\=groups,
        marker\="\_",
        lw\=50,
        cmap\=cmap\_data,
    )
    ax.scatter(
        range(len(groups)),
        \[3.5\] \* len(groups),
        c\=classes,
        marker\="\_",
        lw\=50,
        cmap\=cmap\_data,
    )
    ax.set(
        ylim\=\[\-1, 5\],
        yticks\=\[0.5, 3.5\],
        yticklabels\=\["Data\\ngroup", "Data\\nclass"\],
        xlabel\="Sample index",
    )

visualize\_groups(y, groups, "no groups")

Copy to clipboard

![plot cv indices](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_001.png)

Define a function to visualize cross-validation behavior[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#define-a-function-to-visualize-cross-validation-behavior "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We’ll define a function that lets us visualize the behavior of each cross-validation object. We’ll perform 4 splits of the data. On each split, we’ll visualize the indices chosen for the training set (in blue) and the test set (in red).

def plot\_cv\_indices(cv, X, y, group, ax, n\_splits, lw\=10):
    """Create a sample plot for indices of a cross-validation object."""
    use\_groups \= "Group" in type(cv).\_\_name\_\_
    groups \= group if use\_groups else None
    \# Generate the training/testing visualizations for each CV split
    for ii, (tr, tt) in enumerate(cv.split(X\=X, y\=y, groups\=groups)):
        \# Fill in indices with the training/test groups
        indices \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
\] \* len(X))
        indices\[tt\] \= 1
        indices\[tr\] \= 0

        \# Visualize the results
        ax.scatter(
            range(len(indices)),
            \[ii + 0.5\] \* len(indices),
            c\=indices,
            marker\="\_",
            lw\=lw,
            cmap\=cmap\_cv,
            vmin\=-0.2,
            vmax\=1.2,
        )

    \# Plot the data classes and groups at the end
    ax.scatter(
        range(len(X)), \[ii + 1.5\] \* len(X), c\=y, marker\="\_", lw\=lw, cmap\=cmap\_data
    )

    ax.scatter(
        range(len(X)), \[ii + 2.5\] \* len(X), c\=group, marker\="\_", lw\=lw, cmap\=cmap\_data
    )

    \# Formatting
    yticklabels \= list(range(n\_splits)) + \["class", "group"\]
    ax.set(
        yticks\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_splits + 2) + 0.5,
        yticklabels\=yticklabels,
        xlabel\="Sample index",
        ylabel\="CV iteration",
        ylim\=\[n\_splits + 2.2, \-0.2\],
        xlim\=\[0, 100\],
    )
    ax.set\_title("{}".format(type(cv).\_\_name\_\_), fontsize\=15)
    return ax

Copy to clipboard

Let’s see how it looks for the [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 cross-validation object:

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
cv \= [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(n\_splits)
plot\_cv\_indices(cv, X, y, groups, ax, n\_splits)

Copy to clipboard

![KFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_002.png)

<Axes: title={'center': 'KFold'}, xlabel='Sample index', ylabel='CV iteration'>

Copy to clipboard

As you can see, by default the KFold cross-validation iterator does not take either datapoint class or group into consideration. We can change this by using either:

*   `StratifiedKFold` to preserve the percentage of samples for each class.
    
*   `GroupKFold` to ensure that the same group will not appear in two different folds.
    
*   `StratifiedGroupKFold` to keep the constraint of `GroupKFold` while attempting to return stratified folds.
    

cvs \= \[[StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")\
, [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")\
, [StratifiedGroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")\
\]

for cv in cvs:
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 3))
    plot\_cv\_indices(cv(n\_splits), X, y, groups, ax, n\_splits)
    ax.legend(
        \[[Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
(color\=cmap\_cv(0.8)), [Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
(color\=cmap\_cv(0.02))\],
        \["Testing set", "Training set"\],
        loc\=(1.02, 0.8),
    )
    \# Make the legend fit
    [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
    fig.subplots\_adjust(right\=0.7)

Copy to clipboard

*   ![StratifiedKFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_003.png)
*   ![GroupKFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_004.png)
*   ![StratifiedGroupKFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_005.png)

Next we’ll visualize this behavior for a number of CV iterators.

Visualize cross-validation indices for many CV objects[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualize-cross-validation-indices-for-many-cv-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s visually compare the cross validation behavior for many scikit-learn cross-validation objects. Below we will loop through several common cross-validation objects, visualizing the behavior of each.

Note how some use the group/class information while others do not.

cvs \= \[\
    [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")\
,\
    [GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")\
,\
    [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")\
,\
    [StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")\
,\
    [StratifiedGroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")\
,\
    [GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")\
,\
    [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")\
,\
    [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")\
,\
\]

for cv in cvs:
    this\_cv \= cv(n\_splits\=n\_splits)
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 3))
    plot\_cv\_indices(this\_cv, X, y, groups, ax, n\_splits)

    ax.legend(
        \[[Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
(color\=cmap\_cv(0.8)), [Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
(color\=cmap\_cv(0.02))\],
        \["Testing set", "Training set"\],
        loc\=(1.02, 0.8),
    )
    \# Make the legend fit
    [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
    fig.subplots\_adjust(right\=0.7)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![KFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_006.png)
*   ![GroupKFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_007.png)
*   ![ShuffleSplit](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_008.png)
*   ![StratifiedKFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_009.png)
*   ![StratifiedGroupKFold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_010.png)
*   ![GroupShuffleSplit](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_011.png)
*   ![StratifiedShuffleSplit](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_012.png)
*   ![TimeSeriesSplit](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_013.png)

**Total running time of the script:** (0 minutes 1.193 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_cv_indices.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_cv_indices.ipynb)

[`Download Jupyter notebook: plot_cv_indices.ipynb`](https://scikit-learn.org/stable/_downloads/49cd91d05440a1c88b074430761aeb76/plot_cv_indices.ipynb)

[`Download Python source code: plot_cv_indices.py`](https://scikit-learn.org/stable/_downloads/f1caa332331b42f32518c03ec8a71341/plot_cv_indices.py)

[`Download zipped: plot_cv_indices.zip`](https://scikit-learn.org/stable/_downloads/4bdf97c300a97c8d6b10374db210d15c/plot_cv_indices.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_thumb.png)

[Nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Nested versus non-nested cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)

[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Recursive feature elimination with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f1caa332331b42f32518c03ec8a71341/plot_cv_indices.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/49cd91d05440a1c88b074430761aeb76/plot_cv_indices.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4bdf97c300a97c8d6b10374db210d15c/plot_cv_indices.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_cv_indices.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_cv_indices.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)