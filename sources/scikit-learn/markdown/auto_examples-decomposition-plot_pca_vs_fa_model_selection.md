[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html#sphx-glr-download-auto-examples-decomposition-plot-pca-vs-fa-model-selection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Model selection with Probabilistic PCA and Factor Analysis (FA)[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html#model-selection-with-probabilistic-pca-and-factor-analysis-fa "Link to this heading")

=========================================================================================================================================================================================================================================================

Probabilistic PCA and Factor Analysis are probabilistic models. The consequence is that the likelihood of new data can be used for model selection and covariance estimation. Here we compare PCA and FA with cross-validation on low rank data corrupted with homoscedastic noise (noise variance is the same for each feature) or heteroscedastic noise (noise variance is the different for each feature). In a second step we compare the model likelihood to the likelihoods obtained from shrinkage covariance estimators.

One can observe that with homoscedastic noise both FA and PCA succeed in recovering the size of the low rank subspace. The likelihood with PCA is higher than FA in this case. However PCA fails and overestimates the rank when heteroscedastic noise is present. Under appropriate circumstances (choice of the number of components), the held-out data is more likely for low rank models than for shrinkage models.

The automatic estimation from Automatic Choice of Dimensionality for PCA. NIPS 2000: 598-604 by Thomas P. Minka is also compared.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Create the data[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html#create-the-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
from scipy import linalg

n\_samples, n\_features, rank \= 500, 25, 5
sigma \= 1.0
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
U, \_, \_ \= [linalg.svd](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html#scipy.linalg.svd "scipy.linalg.svd")
(rng.randn(n\_features, n\_features))
X \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(rng.randn(n\_samples, rank), U\[:, :rank\].T)

\# Adding homoscedastic noise
X\_homo \= X + sigma \* rng.randn(n\_samples, n\_features)

\# Adding heteroscedastic noise
sigmas \= sigma \* rng.rand(n\_features) + sigma / 2.0
X\_hetero \= X + rng.randn(n\_samples, n\_features) \* sigmas

Copy to clipboard

Fit the models[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html#fit-the-models "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

from sklearn.covariance import [LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
, [ShrunkCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")

n\_components \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, n\_features, 5)  \# options for n\_components

def compute\_scores(X):
    pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(svd\_solver\="full")
    fa \= [FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
()

    pca\_scores, fa\_scores \= \[\], \[\]
    for n in n\_components:
        pca.n\_components \= n
        fa.n\_components \= n
        pca\_scores.append([np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(pca, X)))
        fa\_scores.append([np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(fa, X)))

    return pca\_scores, fa\_scores

def shrunk\_cov\_score(X):
    shrinkages \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 0, 30)
    cv \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
([ShrunkCovariance](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")
(), {"shrinkage": shrinkages})
    return [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(cv.fit(X).best\_estimator\_, X))

def lw\_score(X):
    return [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
([LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
(), X))

for X, title in \[(X\_homo, "Homoscedastic Noise"), (X\_hetero, "Heteroscedastic Noise")\]:
    pca\_scores, fa\_scores \= compute\_scores(X)
    n\_components\_pca \= n\_components\[[np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")\
(pca\_scores)\]
    n\_components\_fa \= n\_components\[[np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")\
(fa\_scores)\]

    pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(svd\_solver\="full", n\_components\="mle")
    pca.fit(X)
    n\_components\_pca\_mle \= pca.n\_components\_

    print("best n\_components by PCA CV = %d" % n\_components\_pca)
    print("best n\_components by FactorAnalysis CV = %d" % n\_components\_fa)
    print("best n\_components by PCA MLE = %d" % n\_components\_pca\_mle)

    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(n\_components, pca\_scores, "b", label\="PCA scores")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(n\_components, fa\_scores, "r", label\="FA scores")
    [plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(rank, color\="g", label\="TRUTH: %d" % rank, linestyle\="-")
    [plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(
        n\_components\_pca,
        color\="b",
        label\="PCA CV: %d" % n\_components\_pca,
        linestyle\="--",
    )
    [plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(
        n\_components\_fa,
        color\="r",
        label\="FactorAnalysis CV: %d" % n\_components\_fa,
        linestyle\="--",
    )
    [plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(
        n\_components\_pca\_mle,
        color\="k",
        label\="PCA MLE: %d" % n\_components\_pca\_mle,
        linestyle\="--",
    )

    \# compare with other covariance estimators
    [plt.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline")
(
        shrunk\_cov\_score(X),
        color\="violet",
        label\="Shrunk Covariance MLE",
        linestyle\="-.",
    )
    [plt.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline")
(
        lw\_score(X),
        color\="orange",
        label\="LedoitWolf MLE" % n\_components\_pca\_mle,
        linestyle\="-.",
    )

    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("nb of components")
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("CV scores")
    [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Homoscedastic Noise](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_001.png)
*   ![Heteroscedastic Noise](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_002.png)

best n\_components by PCA CV = 5
best n\_components by FactorAnalysis CV = 5
best n\_components by PCA MLE = 5
best n\_components by PCA CV = 20
best n\_components by FactorAnalysis CV = 5
best n\_components by PCA MLE = 18

Copy to clipboard

**Total running time of the script:** (0 minutes 2.544 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_pca_vs_fa_model_selection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_pca_vs_fa_model_selection.ipynb)

[`Download Jupyter notebook: plot_pca_vs_fa_model_selection.ipynb`](https://scikit-learn.org/stable/_downloads/0c988b0c2bea0040fec13fe1055db95c/plot_pca_vs_fa_model_selection.ipynb)

[`Download Python source code: plot_pca_vs_fa_model_selection.py`](https://scikit-learn.org/stable/_downloads/79ed9713970355da938b86bf77fcefa5/plot_pca_vs_fa_model_selection.py)

[`Download zipped: plot_pca_vs_fa_model_selection.zip`](https://scikit-learn.org/stable/_downloads/4158158e379fe1c9e1700dd8a6125179/plot_pca_vs_fa_model_selection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_thumb.png)

[Factor Analysis (with rotation) to visualize patterns](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html)

Factor Analysis (with rotation) to visualize patterns

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mahalanobis_distances_thumb.png)

[Robust covariance estimation and Mahalanobis distances relevance](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html)

Robust covariance estimation and Mahalanobis distances relevance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/79ed9713970355da938b86bf77fcefa5/plot_pca_vs_fa_model_selection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0c988b0c2bea0040fec13fe1055db95c/plot_pca_vs_fa_model_selection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4158158e379fe1c9e1700dd8a6125179/plot_pca_vs_fa_model_selection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_pca_vs_fa_model_selection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_pca_vs_fa_model_selection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)