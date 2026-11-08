[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_ica_vs_pca.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_ica_vs_pca.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_ica_vs_pca.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_ica_vs_pca.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_ica_vs_pca.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_ica_vs_pca.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html#sphx-glr-download-auto-examples-decomposition-plot-ica-vs-pca-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

FastICA on 2D point clouds[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html#fastica-on-2d-point-clouds "Link to this heading")

==================================================================================================================================================================

This example illustrates visually in the feature space a comparison by results using two different component analysis techniques.

[Independent component analysis (ICA)](https://scikit-learn.org/stable/modules/decomposition.html#ica)
 vs [Principal component analysis (PCA)](https://scikit-learn.org/stable/modules/decomposition.html#pca)
.

Representing ICA in the feature space gives the view of ‘geometric ICA’: ICA is an algorithm that finds directions in the feature space corresponding to projections with high non-Gaussianity. These directions need not be orthogonal in the original feature space, but they are orthogonal in the whitened feature space, in which all directions correspond to the same variance.

PCA, on the other hand, finds orthogonal directions in the raw feature space that correspond to directions accounting for maximum variance.

Here we simulate independent sources using a highly non-Gaussian process, 2 student T with a low number of degrees of freedom (top left figure). We mix them to create observations (top right figure). In this raw observation space, directions identified by PCA are represented by orange vectors. We represent the signal in the PCA space, after whitening by the variance corresponding to the PCA vectors (lower left). Running ICA corresponds to finding a rotation in this space to identify the directions of largest non-Gaussianity (lower right).

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html#generate-sample-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
S \= rng.standard\_t(1.5, size\=(20000, 2))
S\[:, 0\] \*= 2.0

\# Mix data
A \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[1, 1\], \[0, 2\]\])  \# Mixing matrix

X \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(S, A.T)  \# Generate observations

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
()
S\_pca\_ \= pca.fit(X).transform(X)

ica \= [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
(random\_state\=rng, whiten\="arbitrary-variance")
S\_ica\_ \= ica.fit(X).transform(X)  \# Estimate the sources

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html#plot-results "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

def plot\_samples(S, axis\_list\=None):
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        S\[:, 0\], S\[:, 1\], s\=2, marker\="o", zorder\=10, color\="steelblue", alpha\=0.5
    )
    if axis\_list is not None:
        for axis, color, label in axis\_list:
            x\_axis, y\_axis \= axis / axis.std()
            [plt.quiver](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver")
(
                (0, 0),
                (0, 0),
                x\_axis,
                y\_axis,
                zorder\=11,
                width\=0.01,
                scale\=6,
                color\=color,
                label\=label,
            )

    [plt.hlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html#matplotlib.pyplot.hlines "matplotlib.pyplot.hlines")
(0, \-5, 5, color\="black", linewidth\=0.5)
    [plt.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
(0, \-3, 3, color\="black", linewidth\=0.5)
    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\-5, 5)
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-3, 3)
    [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
().set\_aspect("equal")
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("x")
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 1)
plot\_samples(S / S.std())
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("True Independent Sources")

axis\_list \= \[(pca.components\_.T, "orange", "PCA"), (ica.mixing\_, "red", "ICA")\]
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 2)
plot\_samples(X / [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(X), axis\_list\=axis\_list)
legend \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left")
legend.set\_zorder(100)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Observations")

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 3)
plot\_samples(S\_pca\_ / [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(S\_pca\_))
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("PCA recovered signals")

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 4)
plot\_samples(S\_ica\_ / [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(S\_ica\_))
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("ICA recovered signals")

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.09, 0.04, 0.94, 0.94, 0.26, 0.36)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![True Independent Sources, Observations, PCA recovered signals, ICA recovered signals](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_vs_pca_001.png)

**Total running time of the script:** (0 minutes 0.331 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_ica_vs_pca.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_ica_vs_pca.ipynb)

[`Download Jupyter notebook: plot_ica_vs_pca.ipynb`](https://scikit-learn.org/stable/_downloads/4ee88a807e060ca374ab95e0d8d819ed/plot_ica_vs_pca.ipynb)

[`Download Python source code: plot_ica_vs_pca.py`](https://scikit-learn.org/stable/_downloads/dc313f6a0617a04ceea6108f4cde71b6/plot_ica_vs_pca.py)

[`Download zipped: plot_ica_vs_pca.zip`](https://scikit-learn.org/stable/_downloads/f7f600b44fff5cb66c5bb505ac77ef2a/plot_ica_vs_pca.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_blind_source_separation_thumb.png)

[Blind source separation using FastICA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html)

Blind source separation using FastICA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bias_variance_thumb.png)

[Single estimator versus bagging: bias-variance decomposition](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html)

Single estimator versus bagging: bias-variance decomposition

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_thumb.png)

[Principal Component Regression vs Partial Least Squares Regression](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)

Principal Component Regression vs Partial Least Squares Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/dc313f6a0617a04ceea6108f4cde71b6/plot_ica_vs_pca.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/4ee88a807e060ca374ab95e0d8d819ed/plot_ica_vs_pca.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f7f600b44fff5cb66c5bb505ac77ef2a/plot_ica_vs_pca.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_ica_vs_pca.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_ica_vs_pca.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)