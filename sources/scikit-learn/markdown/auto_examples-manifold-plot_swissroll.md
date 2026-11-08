[Skip to main content](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/manifold/plot_swissroll.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/manifold/plot_swissroll.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/manifold/plot_swissroll.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/manifold/plot_swissroll.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/manifold/plot_swissroll.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/manifold/plot_swissroll.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html#sphx-glr-download-auto-examples-manifold-plot-swissroll-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Swiss Roll And Swiss-Hole Reduction[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html#swiss-roll-and-swiss-hole-reduction "Link to this heading")

==============================================================================================================================================================================

This notebook seeks to compare two popular non-linear dimensionality techniques, T-distributed Stochastic Neighbor Embedding (t-SNE) and Locally Linear Embedding (LLE), on the classic Swiss Roll dataset. Then, we will explore how they both deal with the addition of a hole in the data.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Swiss Roll[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html#swiss-roll "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

We start by generating the Swiss Roll dataset.

import matplotlib.pyplot as plt

from sklearn import datasets, manifold

sr\_points, sr\_color \= [datasets.make\_swiss\_roll](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")
(n\_samples\=1500, random\_state\=0)

Copy to clipboard

Now, let’s take a look at our data:

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 6))
ax \= fig.add\_subplot(111, projection\="3d")
fig.add\_axes(ax)
ax.scatter(
    sr\_points\[:, 0\], sr\_points\[:, 1\], sr\_points\[:, 2\], c\=sr\_color, s\=50, alpha\=0.8
)
ax.set\_title("Swiss Roll in Ambient Space")
ax.view\_init(azim\=-66, elev\=12)
\_ \= ax.text2D(0.8, 0.05, s\="n\_samples=1500", transform\=ax.transAxes)

Copy to clipboard

![Swiss Roll in Ambient Space](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_001.png)

Computing the LLE and t-SNE embeddings, we find that LLE seems to unroll the Swiss Roll pretty effectively. t-SNE on the other hand, is able to preserve the general structure of the data, but, poorly represents the continuous nature of our original data. Instead, it seems to unnecessarily clump sections of points together.

sr\_lle, sr\_err \= [manifold.locally\_linear\_embedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#sklearn.manifold.locally_linear_embedding "sklearn.manifold.locally_linear_embedding")
(
    sr\_points, n\_neighbors\=12, n\_components\=2
)

sr\_tsne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(n\_components\=2, perplexity\=40, random\_state\=0).fit\_transform(
    sr\_points
)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 8), nrows\=2)
axs\[0\].scatter(sr\_lle\[:, 0\], sr\_lle\[:, 1\], c\=sr\_color)
axs\[0\].set\_title("LLE Embedding of Swiss Roll")
axs\[1\].scatter(sr\_tsne\[:, 0\], sr\_tsne\[:, 1\], c\=sr\_color)
\_ \= axs\[1\].set\_title("t-SNE Embedding of Swiss Roll")

Copy to clipboard

![LLE Embedding of Swiss Roll, t-SNE Embedding of Swiss Roll](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_002.png)

Note

LLE seems to be stretching the points from the center (purple) of the swiss roll. However, we observe that this is simply a byproduct of how the data was generated. There is a higher density of points near the center of the roll, which ultimately affects how LLE reconstructs the data in a lower dimension.

Swiss-Hole[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html#swiss-hole "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Now let’s take a look at how both algorithms deal with us adding a hole to the data. First, we generate the Swiss-Hole dataset and plot it:

sh\_points, sh\_color \= [datasets.make\_swiss\_roll](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")
(
    n\_samples\=1500, hole\=True, random\_state\=0
)

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 6))
ax \= fig.add\_subplot(111, projection\="3d")
fig.add\_axes(ax)
ax.scatter(
    sh\_points\[:, 0\], sh\_points\[:, 1\], sh\_points\[:, 2\], c\=sh\_color, s\=50, alpha\=0.8
)
ax.set\_title("Swiss-Hole in Ambient Space")
ax.view\_init(azim\=-66, elev\=12)
\_ \= ax.text2D(0.8, 0.05, s\="n\_samples=1500", transform\=ax.transAxes)

Copy to clipboard

![Swiss-Hole in Ambient Space](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_003.png)

Computing the LLE and t-SNE embeddings, we obtain similar results to the Swiss Roll. LLE very capably unrolls the data and even preserves the hole. t-SNE, again seems to clump sections of points together, but, we note that it preserves the general topology of the original data.

sh\_lle, sh\_err \= [manifold.locally\_linear\_embedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#sklearn.manifold.locally_linear_embedding "sklearn.manifold.locally_linear_embedding")
(
    sh\_points, n\_neighbors\=12, n\_components\=2
)

sh\_tsne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(
    n\_components\=2, perplexity\=40, init\="random", random\_state\=0
).fit\_transform(sh\_points)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 8), nrows\=2)
axs\[0\].scatter(sh\_lle\[:, 0\], sh\_lle\[:, 1\], c\=sh\_color)
axs\[0\].set\_title("LLE Embedding of Swiss-Hole")
axs\[1\].scatter(sh\_tsne\[:, 0\], sh\_tsne\[:, 1\], c\=sh\_color)
\_ \= axs\[1\].set\_title("t-SNE Embedding of Swiss-Hole")

Copy to clipboard

![LLE Embedding of Swiss-Hole, t-SNE Embedding of Swiss-Hole](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_004.png)

Concluding remarks[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html#concluding-remarks "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

We note that t-SNE benefits from testing more combinations of parameters. Better results could probably have been obtained by better tuning these parameters.

We observe that, as seen in the “Manifold learning on handwritten digits” example, t-SNE generally performs better than LLE on real world data.

**Total running time of the script:** (0 minutes 16.855 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_swissroll.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_swissroll.ipynb)

[`Download Jupyter notebook: plot_swissroll.ipynb`](https://scikit-learn.org/stable/_downloads/4c773264381a88c3d3933952c6040058/plot_swissroll.ipynb)

[`Download Python source code: plot_swissroll.py`](https://scikit-learn.org/stable/_downloads/7f0a2318ad82288d649c688011f52618/plot_swissroll.py)

[`Download zipped: plot_swissroll.zip`](https://scikit-learn.org/stable/_downloads/3a435b85c0a6eebd325c2b99faad732b/plot_swissroll.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/7f0a2318ad82288d649c688011f52618/plot_swissroll.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/4c773264381a88c3d3933952c6040058/plot_swissroll.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3a435b85c0a6eebd325c2b99faad732b/plot_swissroll.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_swissroll.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_swissroll.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)