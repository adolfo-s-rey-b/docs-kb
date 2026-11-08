[Skip to main content](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/compose/plot_digits_pipe.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/compose/plot_digits_pipe.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/compose/plot_digits_pipe.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/compose/plot_digits_pipe.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/compose/plot_digits_pipe.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/compose/plot_digits_pipe.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html#sphx-glr-download-auto-examples-compose-plot-digits-pipe-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Pipelining: chaining a PCA and a logistic regression[#](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html#pipelining-chaining-a-pca-and-a-logistic-regression "Link to this heading")

================================================================================================================================================================================================================

The PCA does an unsupervised dimensionality reduction, while the logistic regression does the prediction.

We use a GridSearchCV to set the dimensionality of the PCA

![plot digits pipe](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_001.png)

Best parameter (CV score=0.874):
{'logistic\_\_C': np.float64(21.54434690031882), 'pca\_\_n\_components': 60}

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
import polars as pl

from sklearn import datasets
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

\# Define a pipeline to search for the best combination of PCA truncation
\# and classifier regularization.
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
()
\# Define a Standard Scaler to normalize inputs
scaler \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()

\# set the tolerance to a large value to make the example faster
logistic \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(max\_iter\=10000, tol\=0.1)
pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(steps\=\[("scaler", scaler), ("pca", pca), ("logistic", logistic)\])

X\_digits, y\_digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
\# Parameters of pipelines can be set using '\_\_' separated parameter names:
param\_grid \= {
    "pca\_\_n\_components": \[5, 15, 30, 45, 60\],
    "logistic\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-4, 4, 4),
}
search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(pipe, param\_grid, n\_jobs\=2)
search.fit(X\_digits, y\_digits)
print("Best parameter (CV score=%0.3f):" % search.best\_score\_)
print(search.best\_params\_)

\# Plot the PCA spectrum
pca.fit(X\_digits)

fig, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True, figsize\=(6, 6))
ax0.plot(
    [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, pca.n\_components\_ + 1), pca.explained\_variance\_ratio\_, "+", linewidth\=2
)
ax0.set\_ylabel("PCA explained variance ratio")

ax0.axvline(
    search.best\_estimator\_.named\_steps\["pca"\].n\_components,
    linestyle\=":",
    label\="n\_components chosen",
)
ax0.legend(prop\=dict(size\=12))

\# For each number of components, find the best classifier results
components\_col \= "param\_pca\_\_n\_components"
is\_max\_test\_score \= pl.col("mean\_test\_score") \== pl.col("mean\_test\_score").max()
best\_clfs \= (
    pl.LazyFrame(search.cv\_results\_)
    .filter(is\_max\_test\_score.over(components\_col))
    .unique(components\_col)
    .sort(components\_col)
    .collect()
)
ax1.errorbar(
    best\_clfs\[components\_col\],
    best\_clfs\["mean\_test\_score"\],
    yerr\=best\_clfs\["std\_test\_score"\],
)
ax1.set\_ylabel("Classification accuracy (val)")
ax1.set\_xlabel("n\_components")

[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\-1, 70)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.880 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_digits_pipe.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_digits_pipe.ipynb)

[`Download Jupyter notebook: plot_digits_pipe.ipynb`](https://scikit-learn.org/stable/_downloads/898b30acf62919d918478efbe526195f/plot_digits_pipe.ipynb)

[`Download Python source code: plot_digits_pipe.py`](https://scikit-learn.org/stable/_downloads/ba89a400c6902f85c10199ff86947d23/plot_digits_pipe.py)

[`Download zipped: plot_digits_pipe.zip`](https://scikit-learn.org/stable/_downloads/25110f74d039a8886ab72ea3a1c2876d/plot_digits_pipe.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isotonic_regression_thumb.png)

[Isotonic Regression](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html)

Isotonic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/ba89a400c6902f85c10199ff86947d23/plot_digits_pipe.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/898b30acf62919d918478efbe526195f/plot_digits_pipe.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/25110f74d039a8886ab72ea3a1c2876d/plot_digits_pipe.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_digits_pipe.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_digits_pipe.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)