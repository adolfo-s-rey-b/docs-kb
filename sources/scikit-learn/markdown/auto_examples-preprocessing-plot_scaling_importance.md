[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_scaling_importance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_scaling_importance.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_scaling_importance.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_scaling_importance.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_scaling_importance.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_scaling_importance.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#sphx-glr-download-auto-examples-preprocessing-plot-scaling-importance-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Importance of Feature Scaling[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#importance-of-feature-scaling "Link to this heading")

================================================================================================================================================================================

Feature scaling through standardization, also called Z-score normalization, is an important preprocessing step for many machine learning algorithms. It involves rescaling each feature such that it has a standard deviation of 1 and a mean of 0.

Even if tree based models are (almost) not affected by scaling, many other algorithms require features to be normalized, often for different reasons: to ease the convergence (such as a non-penalized logistic regression), to create a completely different model fit compared to the fit with unscaled data (such as KNeighbors models). The latter is demonstrated on the first part of the present example.

On the second part of the example we show how Principal Component Analysis (PCA) is impacted by normalization of features. To illustrate this, we compare the principal components found using [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 on unscaled data with those obtained when using a [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 to scale data first.

In the last part of the example we show the effect of the normalization on the accuracy of a model trained on PCA-reduced data.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load and prepare data[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#load-and-prepare-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

The dataset used is the [Wine recognition dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-dataset)
 available at UCI. This dataset has continuous features that are heterogeneous in scale due to differing properties that they measure (e.g. alcohol content and malic acid).

from sklearn.datasets import [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X, y \= [load\_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
(return\_X\_y\=True, as\_frame\=True)
scaler \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
().set\_output(transform\="pandas")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.30, random\_state\=42
)
scaled\_X\_train \= scaler.fit\_transform(X\_train)

Copy to clipboard

Effect of rescaling on a k-neighbors models[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#effect-of-rescaling-on-a-k-neighbors-models "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For the sake of visualizing the decision boundary of a [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
, in this section we select a subset of 2 features that have values with different orders of magnitude.

Keep in mind that using a subset of the features to train the model may likely leave out feature with high predictive impact, resulting in a decision boundary that is much worse in comparison to a model trained on the full set of features.

import matplotlib.pyplot as plt
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")

X\_plot \= X\[\["proline", "hue"\]\]
X\_plot\_scaled \= scaler.fit\_transform(X\_plot)
clf \= [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
(n\_neighbors\=20)

def fit\_and\_plot\_model(X\_plot, y, clf, ax):
    clf.fit(X\_plot, y)
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X\_plot,
        response\_method\="predict",
        alpha\=0.5,
        ax\=ax,
    )
    cmap \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(disp.multiclass\_colors\_)
    disp.ax\_.scatter(
        X\_plot\["proline"\], X\_plot\["hue"\], c\=y, cmap\=cmap, s\=20, edgecolor\="k"
    )
    disp.ax\_.set\_xlim((X\_plot\["proline"\].min(), X\_plot\["proline"\].max()))
    disp.ax\_.set\_ylim((X\_plot\["hue"\].min(), X\_plot\["hue"\].max()))
    return disp.ax\_

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 6))

fit\_and\_plot\_model(X\_plot, y, clf, ax1)
ax1.set\_title("KNN without scaling")

fit\_and\_plot\_model(X\_plot\_scaled, y, clf, ax2)
ax2.set\_xlabel("scaled proline")
ax2.set\_ylabel("scaled hue")
\_ \= ax2.set\_title("KNN with scaling")

Copy to clipboard

![KNN without scaling, KNN with scaling](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_001.png)

Here the decision boundary shows that fitting scaled or non-scaled data lead to completely different models. The reason is that the variable “proline” has values which vary between 0 and 1,000; whereas the variable “hue” varies between 1 and 10. Because of this, distances between samples are mostly impacted by differences in values of “proline”, while values of the “hue” will be comparatively ignored. If one uses [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 to normalize this database, both scaled values lay approximately between -3 and 3 and the neighbors structure will be impacted more or less equivalently by both variables.

Effect of rescaling on a PCA dimensional reduction[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#effect-of-rescaling-on-a-pca-dimensional-reduction "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dimensional reduction using [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 consists of finding the features that maximize the variance. If one feature varies more than the others only because of their respective scales, [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 would determine that such feature dominates the direction of the principal components.

We can inspect the first principal components using all the original features:

import pandas as pd

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2).fit(X\_train)
scaled\_pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2).fit(scaled\_X\_train)
X\_train\_transformed \= pca.transform(X\_train)
X\_train\_std\_transformed \= scaled\_pca.transform(scaled\_X\_train)

first\_pca\_component \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    pca.components\_\[0\], index\=X.columns, columns\=\["without scaling"\]
)
first\_pca\_component\["with scaling"\] \= scaled\_pca.components\_\[0\]
first\_pca\_component.plot.bar(
    title\="Weights of the first principal component", figsize\=(6, 8)
)

\_ \= [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Weights of the first principal component](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_002.png)

Indeed we find that the “proline” feature dominates the direction of the first principal component without scaling, being about two orders of magnitude above the other features. This is contrasted when observing the first principal component for the scaled version of the data, where the orders of magnitude are roughly the same across all the features.

We can visualize the distribution of the principal components in both cases:

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(10, 5))

target\_classes \= range(0, 3)
colors \= ("blue", "red", "green")
markers \= ("^", "s", "o")

for target\_class, color, marker in zip(target\_classes, colors, markers):
    ax1.scatter(
        x\=X\_train\_transformed\[y\_train \== target\_class, 0\],
        y\=X\_train\_transformed\[y\_train \== target\_class, 1\],
        color\=color,
        label\=f"class {target\_class}",
        alpha\=0.5,
        marker\=marker,
    )

    ax2.scatter(
        x\=X\_train\_std\_transformed\[y\_train \== target\_class, 0\],
        y\=X\_train\_std\_transformed\[y\_train \== target\_class, 1\],
        color\=color,
        label\=f"class {target\_class}",
        alpha\=0.5,
        marker\=marker,
    )

ax1.set\_title("Unscaled training dataset after PCA")
ax2.set\_title("Standardized training dataset after PCA")

for ax in (ax1, ax2):
    ax.set\_xlabel("1st principal component")
    ax.set\_ylabel("2nd principal component")
    ax.legend(loc\="upper right")
    ax.grid()

\_ \= [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Unscaled training dataset after PCA, Standardized training dataset after PCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_003.png)

From the plot above we observe that scaling the features before reducing the dimensionality results in components with the same order of magnitude. In this case it also improves the separability of the classes. Indeed, in the next section we confirm that a better separability has a good repercussion on the overall model’s performance.

Effect of rescaling on model’s performance[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#effect-of-rescaling-on-model-s-performance "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First we show how the optimal regularization of a [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
 depends on the scaling or non-scaling of the data:

import numpy as np

from sklearn.linear\_model import [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

Cs \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-5, 5, 20)

unscaled\_clf \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    pca,
    [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
(
        Cs\=Cs,
        use\_legacy\_attributes\=False,
        l1\_ratios\=(0,),  \# TODO(1.10): remove because it is default now
        scoring\="neg\_log\_loss",  \# TODO(1.11): remove because it is default now
    ),
)
unscaled\_clf.fit(X\_train, y\_train)

scaled\_clf \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    scaler,
    pca,
    [LogisticRegressionCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
(
        Cs\=Cs,
        use\_legacy\_attributes\=False,
        l1\_ratios\=(0,),  \# TODO(1.10): remove because it is default now
        scoring\="neg\_log\_loss",  \# TODO(1.11): remove because it is default now,
    ),
)
scaled\_clf.fit(X\_train, y\_train)

print(f"Optimal C for the unscaled PCA: {unscaled\_clf\[\-1\].C\_:.4f}\\n")
print(f"Optimal C for the standardized data with PCA: {scaled\_clf\[\-1\].C\_:.2f}")

Copy to clipboard

Optimal C for the unscaled PCA: 0.0000

Optimal C for the standardized data with PCA: 6.16

Copy to clipboard

The need for regularization is higher (lower values of `C`) for the data that was not scaled before applying PCA. We now evaluate the effect of scaling on the accuracy and the mean log-loss of the optimal models:

from sklearn.metrics import [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
, [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")

y\_pred \= unscaled\_clf.predict(X\_test)
y\_pred\_scaled \= scaled\_clf.predict(X\_test)
y\_proba \= unscaled\_clf.predict\_proba(X\_test)
y\_proba\_scaled \= scaled\_clf.predict\_proba(X\_test)

print("Test accuracy for the unscaled PCA")
print(f"{[accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\_test, y\_pred):.2%}\\n")
print("Test accuracy for the standardized data with PCA")
print(f"{[accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\_test, y\_pred\_scaled):.2%}\\n")
print("Log-loss for the unscaled PCA")
print(f"{[log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\_test, y\_proba):.3}\\n")
print("Log-loss for the standardized data with PCA")
print(f"{[log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\_test, y\_proba\_scaled):.3}")

Copy to clipboard

Test accuracy for the unscaled PCA
35.19%

Test accuracy for the standardized data with PCA
96.30%

Log-loss for the unscaled PCA
1.18

Log-loss for the standardized data with PCA
0.0739

Copy to clipboard

A clear difference in prediction accuracies is observed when the data is scaled before [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, as it vastly outperforms the unscaled version. This corresponds to the intuition obtained from the plot in the previous section, where the components become linearly separable when scaling before using [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
.

Notice that in this case the models with scaled features perform better than the models with non-scaled features because all the variables are expected to be predictive and we rather avoid some of them being comparatively ignored.

If the variables in lower scales were not predictive, one may experience a decrease of the performance after scaling the features: noisy features would contribute more to the prediction after scaling and therefore scaling would increase overfitting.

Last but not least, we observe that one achieves a lower log-loss by means of the scaling step.

**Total running time of the script:** (0 minutes 1.631 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_scaling_importance.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_scaling_importance.ipynb)

[`Download Jupyter notebook: plot_scaling_importance.ipynb`](https://scikit-learn.org/stable/_downloads/c9688d36cfbf43a68f3613b58110ceaa/plot_scaling_importance.ipynb)

[`Download Python source code: plot_scaling_importance.py`](https://scikit-learn.org/stable/_downloads/4ef6a0e5e8f2fe6463d63928373e5f91/plot_scaling_importance.py)

[`Download zipped: plot_scaling_importance.zip`](https://scikit-learn.org/stable/_downloads/2b824c234439fb855e512d2465db9d8e/plot_scaling_importance.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_thumb.png)

[Kernel PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html)

Kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4ef6a0e5e8f2fe6463d63928373e5f91/plot_scaling_importance.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c9688d36cfbf43a68f3613b58110ceaa/plot_scaling_importance.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2b824c234439fb855e512d2465db9d8e/plot_scaling_importance.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_scaling_importance.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_scaling_importance.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)