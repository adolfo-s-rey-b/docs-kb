[Skip to main content](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/manifold/plot_t_sne_perplexity.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/manifold/plot_t_sne_perplexity.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/manifold/plot_t_sne_perplexity.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/manifold/plot_t_sne_perplexity.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/manifold/plot_t_sne_perplexity.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/manifold/plot_t_sne_perplexity.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html#sphx-glr-download-auto-examples-manifold-plot-t-sne-perplexity-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

t-SNE: The effect of various perplexity values on the shape[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html#t-sne-the-effect-of-various-perplexity-values-on-the-shape "Link to this heading")

====================================================================================================================================================================================================================================

An illustration of t-SNE on the two concentric circles and the S-curve datasets for different perplexity values.

We observe a tendency towards clearer shapes as the perplexity value increases.

The size, the distance and the shape of clusters may vary upon initialization, perplexity values and does not always convey a meaning.

As shown below, t-SNE for higher perplexities finds meaningful topology of two concentric circles, however the size and the distance of the circles varies slightly from the original. Contrary to the two circles dataset, the shapes visually diverge from S-curve topology on the S-curve dataset even for larger perplexity values.

For further details, “How to Use t-SNE Effectively” [https://distill.pub/2016/misread-tsne/](https://distill.pub/2016/misread-tsne/)
 provides a good discussion of the effects of various parameters, as well as interactive plots to explore those effects.

![Perplexity=5, Perplexity=30, Perplexity=50, Perplexity=100, Perplexity=5, Perplexity=30, Perplexity=50, Perplexity=100, Perplexity=5, Perplexity=30, Perplexity=50, Perplexity=100](https://scikit-learn.org/stable/_images/sphx_glr_plot_t_sne_perplexity_001.png)

circles, perplexity=5 in 0.13 sec
circles, perplexity=30 in 0.2 sec
circles, perplexity=50 in 0.24 sec
circles, perplexity=100 in 0.24 sec
S-curve, perplexity=5 in 0.14 sec
S-curve, perplexity=30 in 0.2 sec
S-curve, perplexity=50 in 0.24 sec
S-curve, perplexity=100 in 0.23 sec
uniform grid, perplexity=5 in 0.16 sec
uniform grid, perplexity=30 in 0.24 sec
uniform grid, perplexity=50 in 0.27 sec
uniform grid, perplexity=100 in 0.27 sec

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import [NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")

from sklearn import datasets, manifold

n\_samples \= 150
n\_components \= 2
(fig, subplots) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 5, figsize\=(15, 8))
perplexities \= \[5, 30, 50, 100\]

X, y \= [datasets.make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
(
    n\_samples\=n\_samples, factor\=0.5, noise\=0.05, random\_state\=0
)

red \= y \== 0
green \= y \== 1

ax \= subplots\[0\]\[0\]
ax.scatter(X\[red, 0\], X\[red, 1\], c\="r")
ax.scatter(X\[green, 0\], X\[green, 1\], c\="g")
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

for i, perplexity in enumerate(perplexities):
    ax \= subplots\[0\]\[i + 1\]

    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    tsne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(
        n\_components\=n\_components,
        init\="random",
        random\_state\=0,
        perplexity\=perplexity,
        max\_iter\=300,
    )
    Y \= tsne.fit\_transform(X)
    t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    print("circles, perplexity=%d in %.2g sec" % (perplexity, t1 \- t0))
    ax.set\_title("Perplexity=%d" % perplexity)
    ax.scatter(Y\[red, 0\], Y\[red, 1\], c\="r")
    ax.scatter(Y\[green, 0\], Y\[green, 1\], c\="g")
    ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.axis("tight")

\# Another example using s-curve
X, color \= [datasets.make\_s\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "sklearn.datasets.make_s_curve")
(n\_samples, random\_state\=0)

ax \= subplots\[1\]\[0\]
ax.scatter(X\[:, 0\], X\[:, 2\], c\=color)
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())

for i, perplexity in enumerate(perplexities):
    ax \= subplots\[1\]\[i + 1\]

    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    tsne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(
        n\_components\=n\_components,
        init\="random",
        random\_state\=0,
        perplexity\=perplexity,
        learning\_rate\="auto",
        max\_iter\=300,
    )
    Y \= tsne.fit\_transform(X)
    t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    print("S-curve, perplexity=%d in %.2g sec" % (perplexity, t1 \- t0))

    ax.set\_title("Perplexity=%d" % perplexity)
    ax.scatter(Y\[:, 0\], Y\[:, 1\], c\=color)
    ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.axis("tight")

\# Another example using a 2D uniform grid
x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, int([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(n\_samples)))
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(x, x)
X \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(
    \[\
        xx.ravel().reshape(\-1, 1),\
        yy.ravel().reshape(\-1, 1),\
    \]
)
color \= xx.ravel()
ax \= subplots\[2\]\[0\]
ax.scatter(X\[:, 0\], X\[:, 1\], c\=color)
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())

for i, perplexity in enumerate(perplexities):
    ax \= subplots\[2\]\[i + 1\]

    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    tsne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(
        n\_components\=n\_components,
        init\="random",
        random\_state\=0,
        perplexity\=perplexity,
        max\_iter\=400,
    )
    Y \= tsne.fit\_transform(X)
    t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    print("uniform grid, perplexity=%d in %.2g sec" % (perplexity, t1 \- t0))

    ax.set\_title("Perplexity=%d" % perplexity)
    ax.scatter(Y\[:, 0\], Y\[:, 1\], c\=color)
    ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.axis("tight")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.054 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_t_sne_perplexity.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_t_sne_perplexity.ipynb)

[`Download Jupyter notebook: plot_t_sne_perplexity.ipynb`](https://scikit-learn.org/stable/_downloads/8b98cea0e0ec1ca3cc503c13ddac0537/plot_t_sne_perplexity.ipynb)

[`Download Python source code: plot_t_sne_perplexity.py`](https://scikit-learn.org/stable/_downloads/dec20a8d5f622301132b632f5e0bd532/plot_t_sne_perplexity.py)

[`Download zipped: plot_t_sne_perplexity.zip`](https://scikit-learn.org/stable/_downloads/87939fa0b9f88b9ec889e5fc62f83214/plot_t_sne_perplexity.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_thumb.png)

[Swiss Roll And Swiss-Hole Reduction](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html)

Swiss Roll And Swiss-Hole Reduction

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/dec20a8d5f622301132b632f5e0bd532/plot_t_sne_perplexity.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/8b98cea0e0ec1ca3cc503c13ddac0537/plot_t_sne_perplexity.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/87939fa0b9f88b9ec889e5fc62f83214/plot_t_sne_perplexity.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_t_sne_perplexity.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_t_sne_perplexity.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)