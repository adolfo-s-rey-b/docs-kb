[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_varimax_fa.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_varimax_fa.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_varimax_fa.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_varimax_fa.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_varimax_fa.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_varimax_fa.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html#sphx-glr-download-auto-examples-decomposition-plot-varimax-fa-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Factor Analysis (with rotation) to visualize patterns[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html#factor-analysis-with-rotation-to-visualize-patterns "Link to this heading")

======================================================================================================================================================================================================================

Investigating the Iris dataset, we see that sepal length, petal length and petal width are highly correlated. Sepal width is less redundant. Matrix decomposition techniques can uncover these latent patterns. Applying rotations to the resulting components does not inherently improve the predictive value of the derived latent space, but can help visualise their structure; here, for example, the varimax rotation, which is found by maximizing the squared variances of the weights, finds a structure where the second component only loads positively on sepal width.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

Copy to clipboard

Load Iris data

data \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
().fit\_transform(data\["data"\])
feature\_names \= data\["feature\_names"\]

Copy to clipboard

Plot covariance of Iris features

ax \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
()

im \= ax.imshow([np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X.T), cmap\="RdBu\_r", vmin\=-1, vmax\=1)

ax.set\_xticks(\[0, 1, 2, 3\])
ax.set\_xticklabels(list(feature\_names), rotation\=90)
ax.set\_yticks(\[0, 1, 2, 3\])
ax.set\_yticklabels(list(feature\_names))

[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(im).ax.set\_ylabel("$r$", rotation\=0)
ax.set\_title("Iris feature correlation matrix")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Iris feature correlation matrix](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_001.png)

Run factor analysis with Varimax rotation

n\_comps \= 2

methods \= \[\
    ("PCA", [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
()),\
    ("Unrotated FA", [FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")\
()),\
    ("Varimax FA", [FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")\
(rotation\="varimax")),\
\]
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=len(methods), figsize\=(10, 8), sharey\=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set\_params(n\_components\=n\_comps)
    fa.fit(X)

    components \= fa.components\_.T
    print("\\n\\n %s :\\n" % method)
    print(components)

    vmax \= np.abs(components).max()
    ax.imshow(components, cmap\="RdBu\_r", vmax\=vmax, vmin\=-vmax)
    ax.set\_yticks([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(feature\_names)))
    ax.set\_yticklabels(feature\_names)
    ax.set\_title(str(method))
    ax.set\_xticks(\[0, 1\])
    ax.set\_xticklabels(\["Comp. 1", "Comp. 2"\])
fig.suptitle("Factors")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Factors, PCA, Unrotated FA, Varimax FA](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_002.png)

 PCA :

\[\[ 0.52106591  0.37741762\]\
 \[-0.26934744  0.92329566\]\
 \[ 0.5804131   0.02449161\]\
 \[ 0.56485654  0.06694199\]\]


 Unrotated FA :

\[\[ 0.88096009 -0.4472869 \]\
 \[-0.41691605 -0.55390036\]\
 \[ 0.99918858  0.01915283\]\
 \[ 0.96228895  0.05840206\]\]


 Varimax FA :

\[\[ 0.98633022 -0.05752333\]\
 \[-0.16052385 -0.67443065\]\
 \[ 0.90809432  0.41726413\]\
 \[ 0.85857475  0.43847489\]\]

Copy to clipboard

**Total running time of the script:** (0 minutes 0.374 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_varimax_fa.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_varimax_fa.ipynb)

[`Download Jupyter notebook: plot_varimax_fa.ipynb`](https://scikit-learn.org/stable/_downloads/7716523ca12b85a020d7a525dff641cc/plot_varimax_fa.ipynb)

[`Download Python source code: plot_varimax_fa.py`](https://scikit-learn.org/stable/_downloads/e953392bd366ce4c91e2993b65d310dd/plot_varimax_fa.py)

[`Download zipped: plot_varimax_fa.zip`](https://scikit-learn.org/stable/_downloads/053b58bbfc8177072856c743b2c93424/plot_varimax_fa.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_thumb.png)

[Model selection with Probabilistic PCA and Factor Analysis (FA)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)

Model selection with Probabilistic PCA and Factor Analysis (FA)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/e953392bd366ce4c91e2993b65d310dd/plot_varimax_fa.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7716523ca12b85a020d7a525dff641cc/plot_varimax_fa.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/053b58bbfc8177072856c743b2c93424/plot_varimax_fa.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_varimax_fa.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_varimax_fa.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)