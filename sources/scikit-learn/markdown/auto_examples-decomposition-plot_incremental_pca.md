[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_incremental_pca.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_incremental_pca.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_incremental_pca.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_incremental_pca.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_incremental_pca.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_incremental_pca.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html#sphx-glr-download-auto-examples-decomposition-plot-incremental-pca-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Incremental PCA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html#incremental-pca "Link to this heading")

=================================================================================================================================================

Incremental principal component analysis (IPCA) is typically used as a replacement for principal component analysis (PCA) when the dataset to be decomposed is too large to fit in memory. IPCA builds a low-rank approximation for the input data using an amount of memory which is independent of the number of input data samples. It is still dependent on the input data features, but changing the batch size allows for control of memory usage.

This example serves as a visual check that IPCA is able to find a similar projection of the data to PCA (to a sign flip), while only processing a few samples at a time. This can be considered a “toy example”, as IPCA is intended for large datasets which do not fit in main memory, requiring incremental approaches.

*   ![Incremental PCA of iris dataset Mean absolute unsigned error 0.002201](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_001.png)
*   ![PCA of iris dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_002.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [IncrementalPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data
y \= iris.target

n\_components \= 2
ipca \= [IncrementalPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
(n\_components\=n\_components, batch\_size\=10)
X\_ipca \= ipca.fit\_transform(X)

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=n\_components)
X\_pca \= pca.fit\_transform(X)

colors \= \["navy", "turquoise", "darkorange"\]

for X\_transformed, title in \[(X\_ipca, "Incremental PCA"), (X\_pca, "PCA")\]:
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 8))
    for color, i, target\_name in zip(colors, \[0, 1, 2\], iris.target\_names):
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            X\_transformed\[y \== i, 0\],
            X\_transformed\[y \== i, 1\],
            color\=color,
            lw\=2,
            label\=target\_name,
        )

    if "Incremental" in title:
        err \= np.abs(np.abs(X\_pca) \- np.abs(X\_ipca)).mean()
        [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title + " of iris dataset\\nMean absolute unsigned error %.6f" % err)
    else:
        [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title + " of iris dataset")
    [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best", shadow\=False, scatterpoints\=1)
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
(\[\-4, 4, \-1.5, 1.5\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.213 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_incremental_pca.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_incremental_pca.ipynb)

[`Download Jupyter notebook: plot_incremental_pca.ipynb`](https://scikit-learn.org/stable/_downloads/1e455640a8ffb0f44808048624f12d3d/plot_incremental_pca.ipynb)

[`Download Python source code: plot_incremental_pca.py`](https://scikit-learn.org/stable/_downloads/84013ce9dfea94b493c87cb1413fc3bf/plot_incremental_pca.py)

[`Download zipped: plot_incremental_pca.zip`](https://scikit-learn.org/stable/_downloads/c9e0ce7ab0d4145aa1e41ca5fc31178e/plot_incremental_pca.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/84013ce9dfea94b493c87cb1413fc3bf/plot_incremental_pca.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1e455640a8ffb0f44808048624f12d3d/plot_incremental_pca.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c9e0ce7ab0d4145aa1e41ca5fc31178e/plot_incremental_pca.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_incremental_pca.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_incremental_pca.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)