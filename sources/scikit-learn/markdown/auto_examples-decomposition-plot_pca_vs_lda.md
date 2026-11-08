[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_pca_vs_lda.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_pca_vs_lda.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_pca_vs_lda.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_pca_vs_lda.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_pca_vs_lda.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_pca_vs_lda.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#sphx-glr-download-auto-examples-decomposition-plot-pca-vs-lda-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of LDA and PCA 2D projection of Iris dataset[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#comparison-of-lda-and-pca-2d-projection-of-iris-dataset "Link to this heading")

============================================================================================================================================================================================================================

The Iris dataset represents 3 kind of Iris flowers (Setosa, Versicolour and Virginica) with 4 attributes: sepal length, sepal width, petal length and petal width.

Principal Component Analysis (PCA) applied to this data identifies the combination of attributes (principal components, or directions in the feature space) that account for the most variance in the data. Here we plot the different samples on the 2 first principal components.

Linear Discriminant Analysis (LDA) tries to identify attributes that account for the most variance _between classes_. In particular, LDA, in contrast to PCA, is a supervised method, using known class labels.

*   ![PCA of IRIS dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_001.png)
*   ![LDA of IRIS dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_002.png)

explained variance ratio (first two components): \[0.92461872 0.05306648\]

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.discriminant\_analysis import [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")

iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()

X \= iris.data
y \= iris.target
target\_names \= iris.target\_names

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2)
X\_r \= pca.fit(X).transform(X)

lda \= [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(n\_components\=2)
X\_r2 \= lda.fit(X, y).transform(X)

\# Percentage of variance explained for each components
print(
    "explained variance ratio (first two components): %s"
    % str(pca.explained\_variance\_ratio\_)
)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
colors \= \["navy", "turquoise", "darkorange"\]
lw \= 2

for color, i, target\_name in zip(colors, \[0, 1, 2\], target\_names):
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\_r\[y \== i, 0\], X\_r\[y \== i, 1\], color\=color, alpha\=0.8, lw\=lw, label\=target\_name
    )
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best", shadow\=False, scatterpoints\=1)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("PCA of IRIS dataset")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for color, i, target\_name in zip(colors, \[0, 1, 2\], target\_names):
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\_r2\[y \== i, 0\], X\_r2\[y \== i, 1\], alpha\=0.8, color\=color, label\=target\_name
    )
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best", shadow\=False, scatterpoints\=1)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("LDA of IRIS dataset")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.193 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_pca_vs_lda.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_pca_vs_lda.ipynb)

[`Download Jupyter notebook: plot_pca_vs_lda.ipynb`](https://scikit-learn.org/stable/_downloads/24a2d942938af474165a1cab2179d64d/plot_pca_vs_lda.ipynb)

[`Download Python source code: plot_pca_vs_lda.py`](https://scikit-learn.org/stable/_downloads/1c72371dcc2add3178503d130a25cd74/plot_pca_vs_lda.py)

[`Download zipped: plot_pca_vs_lda.zip`](https://scikit-learn.org/stable/_downloads/c2fa5e42f146df31090b4867fccadd4a/plot_pca_vs_lda.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_thumb.png)

[Dimensionality Reduction with Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)

Dimensionality Reduction with Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/1c72371dcc2add3178503d130a25cd74/plot_pca_vs_lda.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/24a2d942938af474165a1cab2179d64d/plot_pca_vs_lda.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c2fa5e42f146df31090b4867fccadd4a/plot_pca_vs_lda.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_pca_vs_lda.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_pca_vs_lda.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)