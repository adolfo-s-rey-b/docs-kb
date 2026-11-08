[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_discretization_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_discretization_classification.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_discretization_classification.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_discretization_classification.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_discretization_classification.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_discretization_classification.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html#sphx-glr-download-auto-examples-preprocessing-plot-discretization-classification-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Feature discretization[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html#feature-discretization "Link to this heading")

=============================================================================================================================================================================

A demonstration of feature discretization on synthetic classification datasets. Feature discretization decomposes each feature into a set of bins, here equally distributed in width. The discrete values are then one-hot encoded, and given to a linear classifier. This preprocessing enables a non-linear behavior even though the classifier is linear.

On this example, the first two rows represent linearly non-separable datasets (moons and concentric circles) while the third is approximately linearly separable. On the two linearly non-separable datasets, feature discretization largely increases the performance of linear classifiers. On the linearly separable dataset, feature discretization decreases the performance of linear classifiers. Two non-linear classifiers are also shown for comparison.

This example should be taken with a grain of salt, as the intuition conveyed does not necessarily carry over to real datasets. Particularly in high-dimensional spaces, data can more easily be separated linearly. Moreover, using feature discretization and one-hot encoding increases the number of features, which easily lead to overfitting when the number of samples is small.

The plots show training points in solid colors and testing points semi-transparent. The lower right shows the classification accuracy on the test set.

![Input data, LogisticRegression, LinearSVC, KBinsDiscretizer LogisticRegression, KBinsDiscretizer LinearSVC, GradientBoostingClassifier, SVC](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_001.png)

dataset 0
---------
LogisticRegression: 0.86
LinearSVC: 0.86
KBinsDiscretizer + LogisticRegression: 0.86
KBinsDiscretizer + LinearSVC: 0.86
GradientBoostingClassifier: 0.90
SVC: 0.94

dataset 1
---------
LogisticRegression: 0.40
LinearSVC: 0.40
KBinsDiscretizer + LogisticRegression: 0.82
KBinsDiscretizer + LinearSVC: 0.82
GradientBoostingClassifier: 0.84
SVC: 0.84

dataset 2
---------
LogisticRegression: 0.98
LinearSVC: 0.96
KBinsDiscretizer + LogisticRegression: 0.94
KBinsDiscretizer + LinearSVC: 0.94
GradientBoostingClassifier: 0.94
SVC: 0.98

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn.datasets import [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
, [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
, [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
from sklearn.ensemble import [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
from sklearn.exceptions import [ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
, [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
from sklearn.utils.\_testing import ignore\_warnings

h \= 0.02  \# step size in the mesh

def get\_name(estimator):
    name \= estimator.\_\_class\_\_.\_\_name\_\_
    if name \== "Pipeline":
        name \= \[get\_name(est\[1\]) for est in estimator.steps\]
        name \= " + ".join(name)
    return name

\# list of (estimator, param\_grid), where param\_grid is used in GridSearchCV
\# The parameter spaces in this example are limited to a narrow band to reduce
\# its runtime. In a real use case, a broader search space for the algorithms
\# should be used.
classifiers \= \[\
    (\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(random\_state\=0)),\
        {"logisticregression\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-1, 1, 3)},\
    ),\
    (\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(random\_state\=0)),\
        {"linearsvc\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-1, 1, 3)},\
    ),\
    (\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(),\
            [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")\
(\
                encode\="onehot", quantile\_method\="averaged\_inverted\_cdf", random\_state\=0\
            ),\
            [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(random\_state\=0),\
        ),\
        {\
            "kbinsdiscretizer\_\_n\_bins": [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(5, 8),\
            "logisticregression\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-1, 1, 3),\
        },\
    ),\
    (\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(),\
            [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")\
(\
                encode\="onehot", quantile\_method\="averaged\_inverted\_cdf", random\_state\=0\
            ),\
            [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(random\_state\=0),\
        ),\
        {\
            "kbinsdiscretizer\_\_n\_bins": [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(5, 8),\
            "linearsvc\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-1, 1, 3),\
        },\
    ),\
    (\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), [GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")\
(n\_estimators\=5, random\_state\=0)\
        ),\
        {"gradientboostingclassifier\_\_learning\_rate": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-2, 0, 5)},\
    ),\
    (\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")\
(random\_state\=0)),\
        {"svc\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-1, 1, 3)},\
    ),\
\]

names \= \[get\_name(e).replace("StandardScaler + ", "") for e, \_ in classifiers\]

n\_samples \= 100
datasets \= \[\
    [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")\
(n\_samples\=n\_samples, noise\=0.2, random\_state\=0),\
    [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")\
(n\_samples\=n\_samples, noise\=0.2, factor\=0.5, random\_state\=1),\
    [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")\
(\
        n\_samples\=n\_samples,\
        n\_features\=2,\
        n\_redundant\=0,\
        n\_informative\=2,\
        random\_state\=2,\
        n\_clusters\_per\_class\=1,\
    ),\
\]

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    nrows\=len(datasets), ncols\=len(classifiers) + 1, figsize\=(21, 9)
)

cm\_piyg \= plt.cm.PiYG
cm\_bright \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["#b30065", "#178000"\])

\# iterate over datasets
for ds\_cnt, (X, y) in enumerate(datasets):
    print(f"\\ndataset {ds\_cnt}\\n\---------")

    \# split into training and test part
    X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
        X, y, test\_size\=0.5, random\_state\=42
    )

    \# create the grid for background colors
    x\_min, x\_max \= X\[:, 0\].min() \- 0.5, X\[:, 0\].max() + 0.5
    y\_min, y\_max \= X\[:, 1\].min() \- 0.5, X\[:, 1\].max() + 0.5
    xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(x\_min, x\_max, h), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_min, y\_max, h))

    \# plot the dataset first
    ax \= axes\[ds\_cnt, 0\]
    if ds\_cnt \== 0:
        ax.set\_title("Input data")
    \# plot the training points
    ax.scatter(X\_train\[:, 0\], X\_train\[:, 1\], c\=y\_train, cmap\=cm\_bright, edgecolors\="k")
    \# and testing points
    ax.scatter(
        X\_test\[:, 0\], X\_test\[:, 1\], c\=y\_test, cmap\=cm\_bright, alpha\=0.6, edgecolors\="k"
    )
    ax.set\_xlim(xx.min(), xx.max())
    ax.set\_ylim(yy.min(), yy.max())
    ax.set\_xticks(())
    ax.set\_yticks(())

    \# iterate over classifiers
    for est\_idx, (name, (estimator, param\_grid)) in enumerate(zip(names, classifiers)):
        ax \= axes\[ds\_cnt, est\_idx + 1\]

        clf \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(estimator\=estimator, param\_grid\=param\_grid)
        with ignore\_warnings(category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
):
            clf.fit(X\_train, y\_train)
        score \= clf.score(X\_test, y\_test)
        print(f"{name}: {score:.2f}")

        \# plot the decision boundary. For that, we will assign a color to each
        \# point in the mesh \[x\_min, x\_max\]\*\[y\_min, y\_max\].
        if hasattr(clf, "decision\_function"):
            Z \= clf.decision\_function([np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[xx.ravel(), yy.ravel()\]))
        else:
            Z \= clf.predict\_proba([np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[xx.ravel(), yy.ravel()\]))\[:, 1\]

        \# put the result into a color plot
        Z \= Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap\=cm\_piyg, alpha\=0.8)

        \# plot the training points
        ax.scatter(
            X\_train\[:, 0\], X\_train\[:, 1\], c\=y\_train, cmap\=cm\_bright, edgecolors\="k"
        )
        \# and testing points
        ax.scatter(
            X\_test\[:, 0\],
            X\_test\[:, 1\],
            c\=y\_test,
            cmap\=cm\_bright,
            edgecolors\="k",
            alpha\=0.6,
        )
        ax.set\_xlim(xx.min(), xx.max())
        ax.set\_ylim(yy.min(), yy.max())
        ax.set\_xticks(())
        ax.set\_yticks(())

        if ds\_cnt \== 0:
            ax.set\_title(name.replace(" + ", "\\n"))
        ax.text(
            0.95,
            0.06,
            (f"{score:.2f}").lstrip("0"),
            size\=15,
            bbox\=dict(boxstyle\="round", alpha\=0.8, facecolor\="white"),
            transform\=ax.transAxes,
            horizontalalignment\="right",
        )

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

\# Add suptitles above the figure
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(top\=0.90)
suptitles \= \[\
    "Linear classifiers",\
    "Feature discretization and linear classifiers",\
    "Non-linear classifiers",\
\]
for i, suptitle in zip(\[1, 3, 5\], suptitles):
    ax \= axes\[0, i\]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform\=ax.transAxes,
        horizontalalignment\="center",
        size\="x-large",
    )
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 4.085 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_discretization_classification.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_discretization_classification.ipynb)

[`Download Jupyter notebook: plot_discretization_classification.ipynb`](https://scikit-learn.org/stable/_downloads/aa8e07ce1b796a15ada1d9f0edce48b5/plot_discretization_classification.ipynb)

[`Download Python source code: plot_discretization_classification.py`](https://scikit-learn.org/stable/_downloads/74caedf3eb449b80f3f00e66c1c576bd/plot_discretization_classification.py)

[`Download zipped: plot_discretization_classification.zip`](https://scikit-learn.org/stable/_downloads/1c8e15dadd5530db0ffab60f34a29a64/plot_discretization_classification.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)

[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Classifier comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/74caedf3eb449b80f3f00e66c1c576bd/plot_discretization_classification.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/aa8e07ce1b796a15ada1d9f0edce48b5/plot_discretization_classification.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1c8e15dadd5530db0ffab60f34a29a64/plot_discretization_classification.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_discretization_classification.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_discretization_classification.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)