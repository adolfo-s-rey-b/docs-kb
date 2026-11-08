[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_successive_halving_heatmap.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_successive_halving_heatmap.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_successive_halving_heatmap.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_successive_halving_heatmap.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_successive_halving_heatmap.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html#sphx-glr-download-auto-examples-model-selection-plot-successive-halving-heatmap-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison between grid search and successive halving[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html#comparison-between-grid-search-and-successive-halving "Link to this heading")

==========================================================================================================================================================================================================================================

This example compares the parameter search performed by [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 and [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.experimental import enable\_halving\_search\_cv  \# noqa: F401
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [HalvingGridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

Copy to clipboard

We first define the parameter space for an [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 estimator, and compute the time required to train a [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 instance, as well as a [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 instance.

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X, y \= [datasets.make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=1000, random\_state\=rng)

gammas \= \[1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7\]
Cs \= \[1, 10, 100, 1e3, 1e4, 1e5\]
param\_grid \= {"gamma": gammas, "C": Cs}

clf \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(random\_state\=rng)

tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
gsh \= [HalvingGridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
(
    estimator\=clf, param\_grid\=param\_grid, factor\=2, random\_state\=rng
)
gsh.fit(X, y)
gsh\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic

tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
gs \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(estimator\=clf, param\_grid\=param\_grid)
gs.fit(X, y)
gs\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic

Copy to clipboard

We now plot heatmaps for both search estimators.

def make\_heatmap(ax, gs, is\_sh\=False, make\_cbar\=False):
    """Helper to make a heatmap."""
    results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(gs.cv\_results\_)
    results\[\["param\_C", "param\_gamma"\]\] \= results\[\["param\_C", "param\_gamma"\]\].astype(
        [np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
    )
    if is\_sh:
        \# SH dataframe: get mean\_test\_score values for the highest iter
        scores\_matrix \= results.sort\_values("iter").pivot\_table(
            index\="param\_gamma",
            columns\="param\_C",
            values\="mean\_test\_score",
            aggfunc\="last",
        )
    else:
        scores\_matrix \= results.pivot(
            index\="param\_gamma", columns\="param\_C", values\="mean\_test\_score"
        )

    im \= ax.imshow(scores\_matrix)

    ax.set\_xticks([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(Cs)))
    ax.set\_xticklabels(\["{:.0E}".format(x) for x in Cs\])
    ax.set\_xlabel("C", fontsize\=15)

    ax.set\_yticks([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(gammas)))
    ax.set\_yticklabels(\["{:.0E}".format(x) for x in gammas\])
    ax.set\_ylabel("gamma", fontsize\=15)

    \# Rotate the tick labels and set their alignment.
    [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
(ax.get\_xticklabels(), rotation\=45, ha\="right", rotation\_mode\="anchor")

    if is\_sh:
        iterations \= results.pivot\_table(
            index\="param\_gamma", columns\="param\_C", values\="iter", aggfunc\="max"
        ).values
        for i in range(len(gammas)):
            for j in range(len(Cs)):
                ax.text(
                    j,
                    i,
                    iterations\[i, j\],
                    ha\="center",
                    va\="center",
                    color\="w",
                    fontsize\=20,
                )

    if make\_cbar:
        fig.subplots\_adjust(right\=0.8)
        cbar\_ax \= fig.add\_axes(\[0.85, 0.15, 0.05, 0.7\])
        fig.colorbar(im, cax\=cbar\_ax)
        cbar\_ax.set\_ylabel("mean\_test\_score", rotation\=-90, va\="bottom", fontsize\=15)

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, sharey\=True)
ax1, ax2 \= axes

make\_heatmap(ax1, gsh, is\_sh\=True)
make\_heatmap(ax2, gs, make\_cbar\=True)

ax1.set\_title("Successive Halving\\ntime = {:.3f}s".format(gsh\_time), fontsize\=15)
ax2.set\_title("GridSearch\\ntime = {:.3f}s".format(gs\_time), fontsize\=15)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Successive Halving time = 1.802s, GridSearch time = 6.462s](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_001.png)

The heatmaps show the mean test score of the parameter combinations for an [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 instance. The [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 also shows the iteration at which the combinations where last used. The combinations marked as `0` were only evaluated at the first iteration, while the ones with `5` are the parameter combinations that are considered the best ones.

We can see that the [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 class is able to find parameter combinations that are just as accurate as [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, in much less time.

**Total running time of the script:** (0 minutes 8.442 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_successive_halving_heatmap.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_successive_halving_heatmap.ipynb)

[`Download Jupyter notebook: plot_successive_halving_heatmap.ipynb`](https://scikit-learn.org/stable/_downloads/69f1bc3bab6ea5d622c5dd4cbd78227f/plot_successive_halving_heatmap.ipynb)

[`Download Python source code: plot_successive_halving_heatmap.py`](https://scikit-learn.org/stable/_downloads/6383d955c013c730f9d211f15e261f38/plot_successive_halving_heatmap.py)

[`Download zipped: plot_successive_halving_heatmap.zip`](https://scikit-learn.org/stable/_downloads/ce1d170a6b8e6097fd3c01ab24b276f5/plot_successive_halving_heatmap.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_iterations_thumb.png)

[Successive Halving Iterations](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html)

Successive Halving Iterations

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_randomized_search_thumb.png)

[Comparing randomized search and grid search for hyperparameter estimation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html)

Comparing randomized search and grid search for hyperparameter estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)

[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)

Pipelining: chaining a PCA and a logistic regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/6383d955c013c730f9d211f15e261f38/plot_successive_halving_heatmap.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/69f1bc3bab6ea5d622c5dd4cbd78227f/plot_successive_halving_heatmap.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/ce1d170a6b8e6097fd3c01ab24b276f5/plot_successive_halving_heatmap.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_successive_halving_heatmap.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_successive_halving_heatmap.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)