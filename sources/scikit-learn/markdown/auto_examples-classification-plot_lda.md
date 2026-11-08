[Skip to main content](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/classification/plot_lda.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/classification/plot_lda.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/classification/plot_lda.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/classification/plot_lda.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/classification/plot_lda.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/classification/plot_lda.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html#sphx-glr-download-auto-examples-classification-plot-lda-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification[#](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html#normal-ledoit-wolf-and-oas-linear-discriminant-analysis-for-classification "Link to this heading")

=============================================================================================================================================================================================================================================================

This example illustrates how the Ledoit-Wolf and Oracle Approximating Shrinkage (OAS) estimators of covariance can improve classification.

![LDA (Linear Discriminant Analysis) vs. LDA with Ledoit Wolf vs. LDA with OAS (1 discriminative feature)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.covariance import [OAS](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.discriminant\_analysis import [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")

n\_train \= 20  \# samples for training
n\_test \= 200  \# samples for testing
n\_averages \= 50  \# how often to repeat classification
n\_features\_max \= 75  \# maximum number of features
step \= 4  \# step size for the calculation

def generate\_data(n\_samples, n\_features):
    """Generate random blob-ish data with noisy features.

    This returns an array of input data with shape \`(n\_samples, n\_features)\`
    and an array of \`n\_samples\` target labels.

    Only one feature contains discriminative information, the other features
    contain only noise.
    """
    X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, n\_features\=1, centers\=\[\[\-2\], \[2\]\])

    \# add non-discriminative features
    if n\_features \> 1:
        X \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(\[X, [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(n\_samples, n\_features \- 1)\])
    return X, y

acc\_clf1, acc\_clf2, acc\_clf3 \= \[\], \[\], \[\]
n\_features\_range \= range(1, n\_features\_max + 1, step)
for n\_features in n\_features\_range:
    score\_clf1, score\_clf2, score\_clf3 \= 0, 0, 0
    for \_ in range(n\_averages):
        X, y \= generate\_data(n\_train, n\_features)

        clf1 \= [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(solver\="lsqr", shrinkage\=None).fit(X, y)
        clf2 \= [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(solver\="lsqr", shrinkage\="auto").fit(X, y)
        oa \= [OAS](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")
(store\_precision\=False, assume\_centered\=False)
        clf3 \= [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(solver\="lsqr", covariance\_estimator\=oa).fit(
            X, y
        )

        X, y \= generate\_data(n\_test, n\_features)
        score\_clf1 += clf1.score(X, y)
        score\_clf2 += clf2.score(X, y)
        score\_clf3 += clf3.score(X, y)

    acc\_clf1.append(score\_clf1 / n\_averages)
    acc\_clf2.append(score\_clf2 / n\_averages)
    acc\_clf3.append(score\_clf3 / n\_averages)

features\_samples\_ratio \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(n\_features\_range) / n\_train

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    features\_samples\_ratio,
    acc\_clf1,
    linewidth\=2,
    label\="LDA",
    color\="gold",
    linestyle\="solid",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    features\_samples\_ratio,
    acc\_clf2,
    linewidth\=2,
    label\="LDA with Ledoit Wolf",
    color\="navy",
    linestyle\="dashed",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    features\_samples\_ratio,
    acc\_clf3,
    linewidth\=2,
    label\="LDA with OAS",
    color\="red",
    linestyle\="dotted",
)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("n\_features / n\_samples")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Classification accuracy")

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower left")
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
((0.65, 1.0))
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
(
    "LDA (Linear Discriminant Analysis) vs."
    "\\n"
    "LDA with Ledoit Wolf vs."
    "\\n"
    "LDA with OAS (1 discriminative feature)"
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 9.988 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_lda.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_lda.ipynb)

[`Download Jupyter notebook: plot_lda.ipynb`](https://scikit-learn.org/stable/_downloads/acc912c1f80e1cb0e32675b5f7686075/plot_lda.ipynb)

[`Download Python source code: plot_lda.py`](https://scikit-learn.org/stable/_downloads/14f620cd922ca2c9a39ae5784034dd0d/plot_lda.py)

[`Download zipped: plot_lda.zip`](https://scikit-learn.org/stable/_downloads/250bd742eab59d3e4df845fe6c5fbaf4/plot_lda.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_thumb.png)

[Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)

Ledoit-Wolf vs OAS estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_thumb.png)

[Linear and Quadratic Discriminant Analysis with covariance ellipsoid](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)

Linear and Quadratic Discriminant Analysis with covariance ellipsoid

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/14f620cd922ca2c9a39ae5784034dd0d/plot_lda.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/acc912c1f80e1cb0e32675b5f7686075/plot_lda.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/250bd742eab59d3e4df845fe6c5fbaf4/plot_lda.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_lda.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_lda.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)