[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_caching_nearest_neighbors.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_caching_nearest_neighbors.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_caching_nearest_neighbors.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_caching_nearest_neighbors.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_caching_nearest_neighbors.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html#sphx-glr-download-auto-examples-neighbors-plot-caching-nearest-neighbors-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Caching nearest neighbors[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html#caching-nearest-neighbors "Link to this heading")

===========================================================================================================================================================================

This example demonstrates how to precompute the k nearest neighbors before using them in KNeighborsClassifier. KNeighborsClassifier can compute the nearest neighbors internally, but precomputing them can have several benefits, such as finer parameter control, caching for multiple use, or custom implementations.

Here we use the caching property of pipelines to cache the nearest neighbors graph between multiple fits of KNeighborsClassifier. The first call is slow since it computes the neighbors graph, while subsequent calls are faster as they do not need to recompute the graph. Here the durations are small since the dataset is small, but the gain can be more substantial when the dataset grows larger, or when the grid of parameter to search is large.

![Classification accuracy, Fit time (with caching)](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from tempfile import [TemporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory "tempfile.TemporaryDirectory")

import matplotlib.pyplot as plt

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
, [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")

X, y \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
n\_neighbors\_list \= \[1, 2, 3, 4, 5, 6, 7, 8, 9\]

\# The transformer computes the nearest neighbors graph using the maximum number
\# of neighbors necessary in the grid search. The classifier model filters the
\# nearest neighbors graph as required by its own n\_neighbors parameter.
graph\_model \= [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
(n\_neighbors\=max(n\_neighbors\_list), mode\="distance")
classifier\_model \= [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
(metric\="precomputed")

\# Note that we give \`memory\` a directory to cache the graph computation
\# that will be used several times when tuning the hyperparameters of the
\# classifier.
with [TemporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory "tempfile.TemporaryDirectory")
(prefix\="sklearn\_graph\_cache\_") as tmpdir:
    full\_model \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
        steps\=\[("graph", graph\_model), ("classifier", classifier\_model)\], memory\=tmpdir
    )

    param\_grid \= {"classifier\_\_n\_neighbors": n\_neighbors\_list}
    grid\_model \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(full\_model, param\_grid)
    grid\_model.fit(X, y)

\# Plot the results of the grid search.
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(8, 4))
axes\[0\].errorbar(
    x\=n\_neighbors\_list,
    y\=grid\_model.cv\_results\_\["mean\_test\_score"\],
    yerr\=grid\_model.cv\_results\_\["std\_test\_score"\],
)
axes\[0\].set(xlabel\="n\_neighbors", title\="Classification accuracy")
axes\[1\].errorbar(
    x\=n\_neighbors\_list,
    y\=grid\_model.cv\_results\_\["mean\_fit\_time"\],
    yerr\=grid\_model.cv\_results\_\["std\_fit\_time"\],
    color\="r",
)
axes\[1\].set(xlabel\="n\_neighbors", title\="Fit time (with caching)")
fig.tight\_layout()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.707 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_caching_nearest_neighbors.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_caching_nearest_neighbors.ipynb)

[`Download Jupyter notebook: plot_caching_nearest_neighbors.ipynb`](https://scikit-learn.org/stable/_downloads/2eaa49c025f80c826512eda4a8add5c3/plot_caching_nearest_neighbors.ipynb)

[`Download Python source code: plot_caching_nearest_neighbors.py`](https://scikit-learn.org/stable/_downloads/7880ee063d9d3845a0ed85afa9948265/plot_caching_nearest_neighbors.py)

[`Download zipped: plot_caching_nearest_neighbors.zip`](https://scikit-learn.org/stable/_downloads/d46573f9713a1a8e4ec685dbe05d7696/plot_caching_nearest_neighbors.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/7880ee063d9d3845a0ed85afa9948265/plot_caching_nearest_neighbors.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2eaa49c025f80c826512eda4a8add5c3/plot_caching_nearest_neighbors.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d46573f9713a1a8e4ec685dbe05d7696/plot_caching_nearest_neighbors.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_caching_nearest_neighbors.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_caching_nearest_neighbors.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)