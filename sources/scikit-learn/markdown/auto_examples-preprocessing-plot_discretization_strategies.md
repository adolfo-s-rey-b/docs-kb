[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_discretization_strategies.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_discretization_strategies.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_discretization_strategies.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_discretization_strategies.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_discretization_strategies.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_discretization_strategies.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html#sphx-glr-download-auto-examples-preprocessing-plot-discretization-strategies-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demonstrating the different strategies of KBinsDiscretizer[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html#demonstrating-the-different-strategies-of-kbinsdiscretizer "Link to this heading")

=================================================================================================================================================================================================================================================

This example presents the different strategies implemented in KBinsDiscretizer:

*   ‘uniform’: The discretization is uniform in each feature, which means that the bin widths are constant in each dimension.
    
*   ‘quantile’: The discretization is done on the quantiled values, which means that each bin has approximately the same number of samples.
    
*   ‘kmeans’: The discretization is based on the centroids of a KMeans clustering procedure.
    

The plot shows the regions where the discretized encoding is constant.

![Input data, strategy='uniform', strategy='quantile', strategy='kmeans'](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.preprocessing import [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")

strategies \= \["uniform", "quantile", "kmeans"\]

n\_samples \= 200
centers\_0 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0, 0\], \[0, 5\], \[2, 4\], \[8, 8\]\])
centers\_1 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0, 0\], \[3, 1\]\])

\# construct the datasets
random\_state \= 42
X\_list \= \[\
    [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
(random\_state).uniform(\-3, 3, size\=(n\_samples, 2)),\
    [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
(\
        n\_samples\=\[\
            n\_samples // 10,\
            n\_samples \* 4 // 10,\
            n\_samples // 10,\
            n\_samples \* 4 // 10,\
        \],\
        cluster\_std\=0.5,\
        centers\=centers\_0,\
        random\_state\=random\_state,\
    )\[0\],\
    [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
(\
        n\_samples\=\[n\_samples // 5, n\_samples \* 4 // 5\],\
        cluster\_std\=0.5,\
        centers\=centers\_1,\
        random\_state\=random\_state,\
    )\[0\],\
\]

figure \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(14, 9))
i \= 1
for ds\_cnt, X in enumerate(X\_list):
    ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len(X\_list), len(strategies) + 1, i)
    ax.scatter(X\[:, 0\], X\[:, 1\], edgecolors\="k")
    if ds\_cnt \== 0:
        ax.set\_title("Input data", size\=14)

    xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(
        [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(X\[:, 0\].min(), X\[:, 0\].max(), 300),
        [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(X\[:, 1\].min(), X\[:, 1\].max(), 300),
    )
    grid \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\]

    ax.set\_xlim(xx.min(), xx.max())
    ax.set\_ylim(yy.min(), yy.max())
    ax.set\_xticks(())
    ax.set\_yticks(())

    i += 1
    \# transform the dataset with KBinsDiscretizer
    for strategy in strategies:
        enc \= [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
(
            n\_bins\=4,
            encode\="ordinal",
            quantile\_method\="averaged\_inverted\_cdf",
            strategy\=strategy,
        )
        enc.fit(X)
        grid\_encoded \= enc.transform(grid)

        ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len(X\_list), len(strategies) + 1, i)

        \# horizontal stripes
        horizontal \= grid\_encoded\[:, 0\].reshape(xx.shape)
        ax.contourf(xx, yy, horizontal, alpha\=0.5)
        \# vertical stripes
        vertical \= grid\_encoded\[:, 1\].reshape(xx.shape)
        ax.contourf(xx, yy, vertical, alpha\=0.5)

        ax.scatter(X\[:, 0\], X\[:, 1\], edgecolors\="k")
        ax.set\_xlim(xx.min(), xx.max())
        ax.set\_ylim(yy.min(), yy.max())
        ax.set\_xticks(())
        ax.set\_yticks(())
        if ds\_cnt \== 0:
            ax.set\_title("strategy='%s'" % (strategy,), size\=14)

        i += 1

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.506 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_discretization_strategies.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_discretization_strategies.ipynb)

[`Download Jupyter notebook: plot_discretization_strategies.ipynb`](https://scikit-learn.org/stable/_downloads/adc9be3b7acc279025dad9ee4ce92038/plot_discretization_strategies.ipynb)

[`Download Python source code: plot_discretization_strategies.py`](https://scikit-learn.org/stable/_downloads/43e84df0b93ff974da370e8da900f2ee/plot_discretization_strategies.py)

[`Download zipped: plot_discretization_strategies.zip`](https://scikit-learn.org/stable/_downloads/7b16734166ab4280e940d7fb89dd6113/plot_discretization_strategies.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_embedding_thumb.png)

[Hashing feature transformation using Totally Random Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html)

Hashing feature transformation using Totally Random Trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/43e84df0b93ff974da370e8da900f2ee/plot_discretization_strategies.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/adc9be3b7acc279025dad9ee4ce92038/plot_discretization_strategies.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/7b16734166ab4280e940d7fb89dd6113/plot_discretization_strategies.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_discretization_strategies.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_discretization_strategies.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)