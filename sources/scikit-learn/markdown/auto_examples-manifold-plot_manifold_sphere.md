[Skip to main content](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/manifold/plot_manifold_sphere.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/manifold/plot_manifold_sphere.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/manifold/plot_manifold_sphere.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/manifold/plot_manifold_sphere.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/manifold/plot_manifold_sphere.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/manifold/plot_manifold_sphere.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html#sphx-glr-download-auto-examples-manifold-plot-manifold-sphere-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Manifold Learning methods on a severed sphere[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html#manifold-learning-methods-on-a-severed-sphere "Link to this heading")

========================================================================================================================================================================================================

An application of the different [Manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold)
 techniques on a spherical data-set. Here one can see the use of dimensionality reduction in order to gain some intuition regarding the manifold learning methods. Regarding the dataset, the poles are cut from the sphere, as well as a thin slice down its side. This enables the manifold learning techniques to ‘spread it open’ whilst projecting it onto two dimensions.

For a similar example, where the methods are applied to the S-curve dataset, see [Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#sphx-glr-auto-examples-manifold-plot-compare-methods-py)
.

Note that the purpose of the [MDS](https://scikit-learn.org/stable/modules/manifold.html#multidimensional-scaling)
 is to find a low-dimensional representation of the data (here 2D) in which the distances respect well the distances in the original high-dimensional space, unlike other manifold-learning algorithms, it does not seeks an isotropic representation of the data in the low-dimensional space. Here the manifold problem matches fairly that of representing a flat map of the Earth, as with [map projection](https://en.wikipedia.org/wiki/Map_projection)
.

![Manifold Learning with 1000 points, 10 neighbors, LLE (0.064 sec), LTSA (0.65 sec), Hessian LLE (0.57 sec), Modified LLE (0.94 sec), Isomap (0.1 sec), MDS (0.88 sec), Non-metric MDS (11 sec), Classical MDS (0.035 sec), Spectral Embedding (0.015 sec), t-SNE (3.5 sec)](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_001.png)

standard: 0.064 sec
ltsa: 0.65 sec
hessian: 0.57 sec
modified: 0.94 sec
ISO: 0.1 sec
MDS: 0.88 sec
Non-metric MDS: 11 sec
Classical MDS: 0.035 sec
Spectral Embedding: 0.015 sec
t-SNE: 3.5 sec

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt

\# Unused but required import for doing 3d projections with matplotlib < 3.2
import mpl\_toolkits.mplot3d  \# noqa: F401
import numpy as np
from matplotlib.ticker import [NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")

from sklearn import manifold
from sklearn.utils import [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")

\# Variables for manifold learning.
n\_neighbors \= 10
n\_samples \= 1000

\# Create our sphere.
random\_state \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(0)
p \= random\_state.rand(n\_samples) \* (2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \- 0.55)
t \= random\_state.rand(n\_samples) \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")

\# Sever the poles from the sphere.
indices \= (t < ([np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \- ([np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 8))) & (t \> ([np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 8))
colors \= p\[indices\]
x, y, z \= (
    [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(t\[indices\]) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(p\[indices\]),
    [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(t\[indices\]) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(p\[indices\]),
    [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(t\[indices\]),
)

\# Plot our dataset.
fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(15, 12))
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
(
    "Manifold Learning with %i points, %i neighbors" % (1000, n\_neighbors), fontsize\=14
)

ax \= fig.add\_subplot(351, projection\="3d")
ax.scatter(x, y, z, c\=p\[indices\], cmap\=plt.cm.rainbow)
ax.view\_init(40, \-10)

sphere\_data \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[x, y, z\]).T

\# Perform Locally Linear Embedding Manifold learning
methods \= \["standard", "ltsa", "hessian", "modified"\]
labels \= \["LLE", "LTSA", "Hessian LLE", "Modified LLE"\]

for i, method in enumerate(methods):
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    trans\_data \= (
        [manifold.LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(
            n\_neighbors\=n\_neighbors, n\_components\=2, method\=method, random\_state\=42
        )
        .fit\_transform(sphere\_data)
        .T
    )
    t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    print("%s: %.2g sec" % (methods\[i\], t1 \- t0))

    ax \= fig.add\_subplot(352 + i)
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("%s (%.2g sec)" % (labels\[i\], t1 \- t0))
    ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Perform Isomap Manifold learning.
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
trans\_data \= (
    [manifold.Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
(n\_neighbors\=n\_neighbors, n\_components\=2)
    .fit\_transform(sphere\_data)
    .T
)
t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print("%s: %.2g sec" % ("ISO", t1 \- t0))

ax \= fig.add\_subplot(357)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("%s (%.2g sec)" % ("Isomap", t1 \- t0))
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Perform Multi-dimensional scaling.
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mds \= [manifold.MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(2, n\_init\=1, random\_state\=42, init\="classical\_mds")
trans\_data \= mds.fit\_transform(sphere\_data).T
t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print("MDS: %.2g sec" % (t1 \- t0))

ax \= fig.add\_subplot(358)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("MDS (%.2g sec)" % (t1 \- t0))
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mds \= [manifold.MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(2, n\_init\=1, random\_state\=42, metric\_mds\=False, init\="classical\_mds")
trans\_data \= mds.fit\_transform(sphere\_data).T
t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print("Non-metric MDS: %.2g sec" % (t1 \- t0))

ax \= fig.add\_subplot(359)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Non-metric MDS (%.2g sec)" % (t1 \- t0))
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mds \= [manifold.ClassicalMDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")
(2)
trans\_data \= mds.fit\_transform(sphere\_data).T
t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print("Classical MDS: %.2g sec" % (t1 \- t0))

ax \= fig.add\_subplot(3, 5, 10)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Classical MDS (%.2g sec)" % (t1 \- t0))
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Perform Spectral Embedding.
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
se \= [manifold.SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
(
    n\_components\=2, n\_neighbors\=n\_neighbors, random\_state\=42
)
trans\_data \= se.fit\_transform(sphere\_data).T
t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print("Spectral Embedding: %.2g sec" % (t1 \- t0))

ax \= fig.add\_subplot(3, 5, 12)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Spectral Embedding (%.2g sec)" % (t1 \- t0))
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Perform t-distributed stochastic neighbor embedding.
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
tsne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(n\_components\=2, random\_state\=0)
trans\_data \= tsne.fit\_transform(sphere\_data).T
t1 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print("t-SNE: %.2g sec" % (t1 \- t0))

ax \= fig.add\_subplot(3, 5, 13)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(trans\_data\[0\], trans\_data\[1\], c\=colors, cmap\=plt.cm.rainbow)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("t-SNE (%.2g sec)" % (t1 \- t0))
ax.xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
ax.yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 18.181 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_manifold_sphere.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_manifold_sphere.ipynb)

[`Download Jupyter notebook: plot_manifold_sphere.ipynb`](https://scikit-learn.org/stable/_downloads/604c0a9de0e1b80dae9e6754fdb27014/plot_manifold_sphere.ipynb)

[`Download Python source code: plot_manifold_sphere.py`](https://scikit-learn.org/stable/_downloads/9846b34238b553e03157c49723da2b04/plot_manifold_sphere.py)

[`Download zipped: plot_manifold_sphere.zip`](https://scikit-learn.org/stable/_downloads/26485aa00d25776ba2b4e87114e5ad56/plot_manifold_sphere.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_t_sne_perplexity_thumb.png)

[t-SNE: The effect of various perplexity values on the shape](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html)

t-SNE: The effect of various perplexity values on the shape

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/9846b34238b553e03157c49723da2b04/plot_manifold_sphere.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/604c0a9de0e1b80dae9e6754fdb27014/plot_manifold_sphere.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/26485aa00d25776ba2b4e87114e5ad56/plot_manifold_sphere.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_manifold_sphere.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_manifold_sphere.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)