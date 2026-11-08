[Skip to main content](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neural_networks/plot_mlp_alpha.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neural_networks/plot_mlp_alpha.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neural_networks/plot_mlp_alpha.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neural_networks/plot_mlp_alpha.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neural_networks/plot_mlp_alpha.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neural_networks/plot_mlp_alpha.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html#sphx-glr-download-auto-examples-neural-networks-plot-mlp-alpha-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Varying regularization in Multi-layer Perceptron[#](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html#varying-regularization-in-multi-layer-perceptron "Link to this heading")

===============================================================================================================================================================================================================

A comparison of different values for regularization parameter ‘alpha’ on synthetic datasets. The plot shows that different alphas yield different decision functions.

Alpha is a parameter for regularization term, aka penalty term, that combats overfitting by constraining the size of the weights. Increasing alpha may fix high variance (a sign of overfitting) by encouraging smaller weights, resulting in a decision boundary plot that appears with lesser curvatures. Similarly, decreasing alpha may fix high bias (a sign of underfitting) by encouraging larger weights, potentially resulting in a more complicated decision boundary.

![alpha 0.10, alpha 0.32, alpha 1.00, alpha 3.16, alpha 10.00, alpha 0.10, alpha 0.32, alpha 1.00, alpha 3.16, alpha 10.00, alpha 0.10, alpha 0.32, alpha 1.00, alpha 3.16, alpha 10.00](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn.datasets import [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
, [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
, [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.neural\_network import [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

h \= 0.02  \# step size in the mesh

alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-1, 1, 5)

classifiers \= \[\]
names \= \[\]
for alpha in alphas:
    classifiers.append(
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
            [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
            [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
(
                solver\="lbfgs",
                alpha\=alpha,
                random\_state\=1,
                max\_iter\=2000,
                early\_stopping\=True,
                hidden\_layer\_sizes\=\[10, 10\],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_features\=2, n\_redundant\=0, n\_informative\=2, random\_state\=0, n\_clusters\_per\_class\=1
)
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(2)
X += 2 \* rng.uniform(size\=X.shape)
linearly\_separable \= (X, y)

datasets \= \[\
    [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")\
(noise\=0.3, random\_state\=0),\
    [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")\
(noise\=0.2, factor\=0.5, random\_state\=1),\
    linearly\_separable,\
\]

figure \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(17, 9))
i \= 1
\# iterate over datasets
for X, y in datasets:
    \# split into training and test part
    X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
        X, y, test\_size\=0.4, random\_state\=42
    )

    x\_min, x\_max \= X\[:, 0\].min() \- 0.5, X\[:, 0\].max() + 0.5
    y\_min, y\_max \= X\[:, 1\].min() \- 0.5, X\[:, 1\].max() + 0.5
    xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(x\_min, x\_max, h), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_min, y\_max, h))

    \# just plot the dataset first
    cm \= plt.cm.RdBu
    cm\_bright \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["#FF0000", "#0000FF"\])
    ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len(datasets), len(classifiers) + 1, i)
    \# Plot the training points
    ax.scatter(X\_train\[:, 0\], X\_train\[:, 1\], c\=y\_train, cmap\=cm\_bright)
    \# and testing points
    ax.scatter(X\_test\[:, 0\], X\_test\[:, 1\], c\=y\_test, cmap\=cm\_bright, alpha\=0.6)
    ax.set\_xlim(xx.min(), xx.max())
    ax.set\_ylim(yy.min(), yy.max())
    ax.set\_xticks(())
    ax.set\_yticks(())
    i += 1

    \# iterate over classifiers
    for name, clf in zip(names, classifiers):
        ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len(datasets), len(classifiers) + 1, i)
        clf.fit(X\_train, y\_train)
        score \= clf.score(X\_test, y\_test)

        \# Plot the decision boundary. For that, we will assign a color to each
        \# point in the mesh \[x\_min, x\_max\] x \[y\_min, y\_max\].
        if hasattr(clf, "decision\_function"):
            Z \= clf.decision\_function([np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[xx.ravel(), yy.ravel()\]))
        else:
            Z \= clf.predict\_proba([np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[xx.ravel(), yy.ravel()\]))\[:, 1\]

        \# Put the result into a color plot
        Z \= Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap\=cm, alpha\=0.8)

        \# Plot also the training points
        ax.scatter(
            X\_train\[:, 0\],
            X\_train\[:, 1\],
            c\=y\_train,
            cmap\=cm\_bright,
            edgecolors\="black",
            s\=25,
        )
        \# and testing points
        ax.scatter(
            X\_test\[:, 0\],
            X\_test\[:, 1\],
            c\=y\_test,
            cmap\=cm\_bright,
            alpha\=0.6,
            edgecolors\="black",
            s\=25,
        )

        ax.set\_xlim(xx.min(), xx.max())
        ax.set\_ylim(yy.min(), yy.max())
        ax.set\_xticks(())
        ax.set\_yticks(())
        ax.set\_title(name)
        ax.text(
            xx.max() \- 0.3,
            yy.min() + 0.3,
            f"{score:.3f}".lstrip("0"),
            size\=15,
            horizontalalignment\="right",
        )
        i += 1

figure.subplots\_adjust(left\=0.02, right\=0.98)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.684 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo27.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neural_networks/plot_mlp_alpha.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo27.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neural_networks/plot_mlp_alpha.ipynb)

[`Download Jupyter notebook: plot_mlp_alpha.ipynb`](https://scikit-learn.org/stable/_downloads/7ce809adad0d67b96c1df3b7fcd74567/plot_mlp_alpha.ipynb)

[`Download Python source code: plot_mlp_alpha.py`](https://scikit-learn.org/stable/_downloads/8af613cc7180fed274715982abcd696d/plot_mlp_alpha.py)

[`Download zipped: plot_mlp_alpha.zip`](https://scikit-learn.org/stable/_downloads/e4310e2da2aadb3d26dad89e2830f503/plot_mlp_alpha.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)

[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Classifier comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_embedding_thumb.png)

[Hashing feature transformation using Totally Random Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html)

Hashing feature transformation using Totally Random Trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/8af613cc7180fed274715982abcd696d/plot_mlp_alpha.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7ce809adad0d67b96c1df3b7fcd74567/plot_mlp_alpha.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e4310e2da2aadb3d26dad89e2830f503/plot_mlp_alpha.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo27.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neural_networks/plot_mlp_alpha.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo27.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neural_networks/plot_mlp_alpha.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)