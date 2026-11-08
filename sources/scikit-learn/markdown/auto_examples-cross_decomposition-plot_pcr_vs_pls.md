[Skip to main content](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#sphx-glr-download-auto-examples-cross-decomposition-plot-pcr-vs-pls-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Principal Component Regression vs Partial Least Squares Regression[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#principal-component-regression-vs-partial-least-squares-regression "Link to this heading")

========================================================================================================================================================================================================================================================

This example compares [Principal Component Regression](https://en.wikipedia.org/wiki/Principal_component_regression)
 (PCR) and [Partial Least Squares Regression](https://en.wikipedia.org/wiki/Partial_least_squares_regression)
 (PLS) on a toy dataset. Our goal is to illustrate how PLS can outperform PCR when the target is strongly correlated with some directions in the data that have a low variance.

PCR is a regressor composed of two steps: first, [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 is applied to the training data, possibly performing dimensionality reduction; then, a regressor (e.g. a linear regressor) is trained on the transformed samples. In [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, the transformation is purely unsupervised, meaning that no information about the targets is used. As a result, PCR may perform poorly in some datasets where the target is strongly correlated with _directions_ that have low variance. Indeed, the dimensionality reduction of PCA projects the data into a lower dimensional space where the variance of the projected data is greedily maximized along each axis. Despite them having the most predictive power on the target, the directions with a lower variance will be dropped, and the final regressor will not be able to leverage them.

PLS is both a transformer and a regressor, and it is quite similar to PCR: it also applies a dimensionality reduction to the samples before applying a linear regressor to the transformed data. The main difference with PCR is that the PLS transformation is supervised. Therefore, as we will see in this example, it does not suffer from the issue we just mentioned.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

The data[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#the-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

We start by creating a simple dataset with two features. Before we even dive into PCR and PLS, we fit a PCA estimator to display the two principal components of this dataset, i.e. the two directions that explain the most variance in the data.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
n\_samples \= 500
cov \= \[\[3, 3\], \[3, 4\]\]
X \= rng.multivariate\_normal(mean\=\[0, 0\], cov\=cov, size\=n\_samples)
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2).fit(X)

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], alpha\=0.3, label\="samples")
for i, (comp, var) in enumerate(zip(pca.components\_, pca.explained\_variance\_)):
    comp \= comp \* var  \# scale component by its variance explanation power
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        \[0, comp\[0\]\],
        \[0, comp\[1\]\],
        label\=f"Component {i}",
        linewidth\=5,
        color\=f"C{i + 2}",
    )
[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
().set(
    aspect\="equal",
    title\="2-dimensional dataset with principal components",
    xlabel\="first feature",
    ylabel\="second feature",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![2-dimensional dataset with principal components](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_001.png)

For the purpose of this example, we now define the target `y` such that it is strongly correlated with a direction that has a small variance. To this end, we will project `X` onto the second component, and add some noise to it.

y \= X.dot(pca.components\_\[1\]) + rng.normal(size\=n\_samples) / 2

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(10, 3))

axes\[0\].scatter(X.dot(pca.components\_\[0\]), y, alpha\=0.3)
axes\[0\].set(xlabel\="Projected data onto first PCA component", ylabel\="y")
axes\[1\].scatter(X.dot(pca.components\_\[1\]), y, alpha\=0.3)
axes\[1\].set(xlabel\="Projected data onto second PCA component", ylabel\="y")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot pcr vs pls](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_002.png)

Projection on one component and predictive power[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#projection-on-one-component-and-predictive-power "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We now create two regressors: PCR and PLS, and for our illustration purposes we set the number of components to 1. Before feeding the data to the PCA step of PCR, we first standardize it, as recommended by good practice. The PLS estimator has built-in scaling capabilities.

For both models, we plot the projected data onto the first component against the target. In both cases, this projected data is what the regressors will use as training data.

from sklearn.cross\_decomposition import [PLSRegression](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=rng)

pcr \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=1), [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
())
pcr.fit(X\_train, y\_train)
pca \= pcr.named\_steps\["pca"\]  \# retrieve the PCA step of the pipeline

pls \= [PLSRegression](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
(n\_components\=1)
pls.fit(X\_train, y\_train)

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(10, 3))
axes\[0\].scatter(pca.transform(X\_test), y\_test, alpha\=0.3, label\="ground truth")
axes\[0\].scatter(
    pca.transform(X\_test), pcr.predict(X\_test), alpha\=0.3, label\="predictions"
)
axes\[0\].set(
    xlabel\="Projected data onto first PCA component", ylabel\="y", title\="PCR / PCA"
)
axes\[0\].legend()
axes\[1\].scatter(pls.transform(X\_test), y\_test, alpha\=0.3, label\="ground truth")
axes\[1\].scatter(
    pls.transform(X\_test), pls.predict(X\_test), alpha\=0.3, label\="predictions"
)
axes\[1\].set(xlabel\="Projected data onto first PLS component", ylabel\="y", title\="PLS")
axes\[1\].legend()
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![PCR / PCA, PLS](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_003.png)

As expected, the unsupervised PCA transformation of PCR has dropped the second component, i.e. the direction with the lowest variance, despite it being the most predictive direction. This is because PCA is a completely unsupervised transformation, and results in the projected data having a low predictive power on the target.

On the other hand, the PLS regressor manages to capture the effect of the direction with the lowest variance, thanks to its use of target information during the transformation: it can recognize that this direction is actually the most predictive. We note that the first PLS component is negatively correlated with the target, which comes from the fact that the signs of eigenvectors are arbitrary.

We also print the R-squared scores of both estimators, which further confirms that PLS is a better alternative than PCR in this case. A negative R-squared indicates that PCR performs worse than a regressor that would simply predict the mean of the target.

print(f"PCR r-squared {pcr.score(X\_test, y\_test):.3f}")
print(f"PLS r-squared {pls.score(X\_test, y\_test):.3f}")

Copy to clipboard

PCR r-squared -0.026
PLS r-squared 0.658

Copy to clipboard

As a final remark, we note that PCR with 2 components performs as well as PLS: this is because in this case, PCR was able to leverage the second component which has the most preditive power on the target.

pca\_2 \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2), [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
())
pca\_2.fit(X\_train, y\_train)
print(f"PCR r-squared with 2 components {pca\_2.score(X\_test, y\_test):.3f}")

Copy to clipboard

PCR r-squared with 2 components 0.673

Copy to clipboard

**Total running time of the script:** (0 minutes 0.571 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo8.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cross_decomposition/plot_pcr_vs_pls.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo8.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cross_decomposition/plot_pcr_vs_pls.ipynb)

[`Download Jupyter notebook: plot_pcr_vs_pls.ipynb`](https://scikit-learn.org/stable/_downloads/0486bf9e537e44cedd2a236d034bcd90/plot_pcr_vs_pls.ipynb)

[`Download Python source code: plot_pcr_vs_pls.py`](https://scikit-learn.org/stable/_downloads/767218d296758dab2ab1c6e1ab1a07bd/plot_pcr_vs_pls.py)

[`Download zipped: plot_pcr_vs_pls.zip`](https://scikit-learn.org/stable/_downloads/1e308ad8f0f51110ea07c8d3b552c5bf/plot_pcr_vs_pls.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_cross_decomposition_thumb.png)

[Compare cross decomposition methods](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)

Compare cross decomposition methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_map_data_to_normal_thumb.png)

[Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html)

Map data to a normal distribution

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/767218d296758dab2ab1c6e1ab1a07bd/plot_pcr_vs_pls.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0486bf9e537e44cedd2a236d034bcd90/plot_pcr_vs_pls.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1e308ad8f0f51110ea07c8d3b552c5bf/plot_pcr_vs_pls.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo8.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cross_decomposition/plot_pcr_vs_pls.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo8.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cross_decomposition/plot_pcr_vs_pls.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)