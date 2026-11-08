[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html#sphx-glr-download-auto-examples-ensemble-plot-forest-iris-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot the decision surfaces of ensembles of trees on the iris dataset[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html#plot-the-decision-surfaces-of-ensembles-of-trees-on-the-iris-dataset "Link to this heading")

==================================================================================================================================================================================================================================================

Plot the decision surfaces of forests of randomized trees trained on pairs of features of the iris dataset.

This plot compares the decision surfaces learned by a decision tree classifier (first column), by a random forest classifier (second column), by an extra-trees classifier (third column) and by an AdaBoost classifier (fourth column).

In the first row, the classifiers are built using the sepal width and the sepal length features only, on the second row using the petal length and sepal length only, and on the third row using the petal width and the petal length only.

In descending order of quality, when trained (outside of this example) on all 4 features using 30 estimators and scored using 10 fold cross validation, we see:

[ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
()  \# 0.95 score
[RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
()  \# 0.94 score
AdaBoost(DecisionTree(max\_depth\=3))  \# 0.94 score
DecisionTree(max\_depth\=None)  \# 0.94 score

Copy to clipboard

Increasing `max_depth` for AdaBoost lowers the standard deviation of the scores (but the average score does not improve).

See the console’s output for further details about each model.

In this example you might try to:

1.  vary the `max_depth` for the `DecisionTreeClassifier` and `AdaBoostClassifier`, perhaps try `max_depth=3` for the `DecisionTreeClassifier` or `max_depth=None` for `AdaBoostClassifier`
    
2.  vary `n_estimators`
    

It is worth noting that RandomForests and ExtraTrees can be fitted in parallel on many cores as each tree is built independently of the others. AdaBoost’s samples are built sequentially and so do not use multiple cores.

![Classifiers on feature subsets of the Iris dataset, DecisionTree, RandomForest, ExtraTrees, AdaBoost](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_001.png)

DecisionTree with features \[0, 1\] has a score of 0.9266666666666666
RandomForest with 30 estimators with features \[0, 1\] has a score of 0.9266666666666666
ExtraTrees with 30 estimators with features \[0, 1\] has a score of 0.9266666666666666
AdaBoost with 30 estimators with features \[0, 1\] has a score of 0.82
DecisionTree with features \[0, 2\] has a score of 0.9933333333333333
RandomForest with 30 estimators with features \[0, 2\] has a score of 0.9933333333333333
ExtraTrees with 30 estimators with features \[0, 2\] has a score of 0.9933333333333333
AdaBoost with 30 estimators with features \[0, 2\] has a score of 0.9933333333333333
DecisionTree with features \[2, 3\] has a score of 0.9933333333333333
RandomForest with 30 estimators with features \[2, 3\] has a score of 0.9933333333333333
ExtraTrees with 30 estimators with features \[2, 3\] has a score of 0.9933333333333333
AdaBoost with 30 estimators with features \[2, 3\] has a score of 0.9866666666666667

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.ensemble import (
    [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
,
    [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
,
    [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
,
)
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

\# Parameters
n\_classes \= 3
n\_estimators \= 30
cmap \= plt.cm.RdYlBu
plot\_step \= 0.02  \# fine step width for decision surface contours
plot\_step\_coarser \= 0.5  \# step widths for coarse classifier guesses
RANDOM\_SEED \= 13  \# fix the seed on each iteration

\# Load data
iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()

plot\_idx \= 1

models \= \[\
    [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")\
(max\_depth\=None),\
    [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(n\_estimators\=n\_estimators),\
    [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")\
(n\_estimators\=n\_estimators),\
    [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")\
([DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")\
(max\_depth\=3), n\_estimators\=n\_estimators),\
\]

for pair in (\[0, 1\], \[0, 2\], \[2, 3\]):
    for model in models:
        \# We only take the two corresponding features
        X \= iris.data\[:, pair\]
        y \= iris.target

        \# Shuffle
        idx \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.shape\[0\])
        [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(RANDOM\_SEED)
        [np.random.shuffle](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html#numpy.random.shuffle "numpy.random.shuffle")
(idx)
        X \= X\[idx\]
        y \= y\[idx\]

        \# Standardize
        mean \= X.mean(axis\=0)
        std \= X.std(axis\=0)
        X \= (X \- mean) / std

        \# Train
        model.fit(X, y)

        scores \= model.score(X, y)
        \# Create a title for each column and the console by using str() and
        \# slicing away useless parts of the string
        model\_title \= str(type(model)).split(".")\[\-1\]\[:\-2\]\[: \-len("Classifier")\]

        model\_details \= model\_title
        if hasattr(model, "estimators\_"):
            model\_details += " with {} estimators".format(len(model.estimators\_))
        print(model\_details + " with features", pair, "has a score of", scores)

        [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(3, 4, plot\_idx)
        if plot\_idx <= len(models):
            \# Add a title at the top of each column
            [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(model\_title, fontsize\=9)

        \# Now plot the decision boundary using a fine mesh as input to a
        \# filled contour plot
        x\_min, x\_max \= X\[:, 0\].min() \- 1, X\[:, 0\].max() + 1
        y\_min, y\_max \= X\[:, 1\].min() \- 1, X\[:, 1\].max() + 1
        xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(
            [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(x\_min, x\_max, plot\_step), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_min, y\_max, plot\_step)
        )

        \# Plot either a single DecisionTreeClassifier or alpha blend the
        \# decision surfaces of the ensemble of classifiers
        if isinstance(model, [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
):
            Z \= model.predict([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
            Z \= Z.reshape(xx.shape)
            cs \= [plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(xx, yy, Z, cmap\=cmap)
        else:
            \# Choose alpha blend level with respect to the number
            \# of estimators
            \# that are in use (noting that AdaBoost can use fewer estimators
            \# than its maximum if it achieves a good enough fit early on)
            estimator\_alpha \= 1.0 / len(model.estimators\_)
            for tree in model.estimators\_:
                Z \= tree.predict([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
                Z \= Z.reshape(xx.shape)
                cs \= [plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(xx, yy, Z, alpha\=estimator\_alpha, cmap\=cmap)

        \# Build a coarser grid to plot a set of ensemble classifications
        \# to show how these are different to what we see in the decision
        \# surfaces. These points are regularly space and do not have a
        \# black outline
        xx\_coarser, yy\_coarser \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(
            [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(x\_min, x\_max, plot\_step\_coarser),
            [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_min, y\_max, plot\_step\_coarser),
        )
        Z\_points\_coarser \= model.predict(
            [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx\_coarser.ravel(), yy\_coarser.ravel()\]
        ).reshape(xx\_coarser.shape)
        cs\_points \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            xx\_coarser,
            yy\_coarser,
            s\=15,
            c\=Z\_points\_coarser,
            cmap\=cmap,
            edgecolors\="none",
        )

        \# Plot the training points, these are clustered together and have a
        \# black outline
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            X\[:, 0\],
            X\[:, 1\],
            c\=y,
            cmap\=[ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["r", "y", "b"\]),
            edgecolor\="k",
            s\=20,
        )
        plot\_idx += 1  \# move on to the next plot in sequence

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Classifiers on feature subsets of the Iris dataset", fontsize\=12)
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(h\_pad\=0.2, w\_pad\=0.2, pad\=2.5)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 6.792 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_forest_iris.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_iris.ipynb)

[`Download Jupyter notebook: plot_forest_iris.ipynb`](https://scikit-learn.org/stable/_downloads/985f759e90739932d90206b8295630d6/plot_forest_iris.ipynb)

[`Download Python source code: plot_forest_iris.py`](https://scikit-learn.org/stable/_downloads/7b2d436e94933f77577bba1962762f33/plot_forest_iris.py)

[`Download zipped: plot_forest_iris.zip`](https://scikit-learn.org/stable/_downloads/92ee804b84e076734477cbf10677d350/plot_forest_iris.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/7b2d436e94933f77577bba1962762f33/plot_forest_iris.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/985f759e90739932d90206b8295630d6/plot_forest_iris.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/92ee804b84e076734477cbf10677d350/plot_forest_iris.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_iris.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_forest_iris.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)