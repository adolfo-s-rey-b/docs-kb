[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_randomized_search.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_randomized_search.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_randomized_search.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_randomized_search.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_randomized_search.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_randomized_search.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#sphx-glr-download-auto-examples-model-selection-plot-randomized-search-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing randomized search and grid search for hyperparameter estimation[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#comparing-randomized-search-and-grid-search-for-hyperparameter-estimation "Link to this heading")

=========================================================================================================================================================================================================================================================================

Compare several strategies to optimize the hyperparameters of a linear SVM trained with stochastic gradient descent. We score the candidates with the one-vs-rest ROC AUC (`roc_auc_ovr`), which evaluates the ranking quality of the predicted class probabilities rather than the raw accuracy of the hard labels.

We start with an exhaustive grid search ([`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
) that evaluates every combination of a discretized parameter grid. Because the grid is fixed, we are forced to fit every configuration and we may even miss a good combination that falls between two grid points.

We then run a randomized search ([`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
) that samples the parameter space instead of discretizing it. With a smaller budget it explores the space more efficiently and reaches an equivalent solution with fewer iterations.

Finally, we run a successive halving search ([`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
) that samples even more candidates but keeps the cost low by evaluating them on a small number of training samples first and discarding the unpromising ones early. It combines a large number of candidates with a reduced fit and predict time in the early iterations.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading the dataset[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#loading-the-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

We use the digits dataset and restrict ourselves to the first three classes to keep the problem small and the search fast.

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")

X, y \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True, n\_class\=3)

Copy to clipboard

Defining the estimator[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#defining-the-estimator "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

We optimize a linear SVM trained with stochastic gradient descent ([`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
). We use the `"modified_huber"` loss, a smoothed variant of the hinge loss: it keeps the large-margin behavior of a linear SVM while also exposing [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
. The probability estimates are required to score the candidates with the one-vs-rest ROC AUC, which the plain hinge loss could not provide.

from sklearn.linear\_model import [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")

linear\_svm \= [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(
    loss\="modified\_huber",
    penalty\="elasticnet",
    fit\_intercept\=True,
    max\_iter\=5\_000,
)

Copy to clipboard

The `report` helper below prints the best parameter settings found by a given search so that we can compare the different strategies.

Successive halving stores in `cv_results_` the candidates evaluated at every iteration, on increasing amounts of resources. The early iterations are scored on a small subset of the data, where perfect but unreliable scores are common. To keep the comparison fair, when an `"iter"` column is present we only keep the last iteration, i.e. the surviving candidates trained on the full set of resources, and we rank candidates by their mean validation score.

import pandas as pd

def report(results, n\_top\=3):
    """Report the top parameters for each search strategy."""
    results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results)
    if "iter" in results:
        results \= results\[results\["iter"\] \== results\["iter"\].max()\]

    for rank, (\_, candidate) in enumerate(
        results.nlargest(n\_top, "mean\_test\_score").iterrows(), start\=1
    ):
        print(
            f"Model with rank: {rank}\\n"
            f"Mean validation score: "
            f"{candidate\['mean\_test\_score'\]:.3f} "
            f"(std: {candidate\['std\_test\_score'\]:.3f})\\n"
            f"Parameters: {candidate\['params'\]}\\n"
        )

Copy to clipboard

Grid search[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#grid-search "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

[`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 explores the entire parameter space defined as a grid. Continuous parameters therefore have to be discretized beforehand and every combination of the grid is evaluated. Two limitations follow from this design: we are forced to fit and score each configuration, even the unpromising ones, and the best hyperparameters may lie between two grid points and thus be missed entirely.

Some configurations do not let [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 converge and raise a [`ConvergenceWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
. These correspond to the poorly performing configurations that the search is meant to explore and discard, so it is fine to silence the warning with a `warnings.catch_warnings` context manager to keep the output readable.

import warnings
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import numpy as np

from sklearn.exceptions import [ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")

param\_grid \= {
    "average": \[True, False\],
    "l1\_ratio": [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, num\=10),
    "alpha": [np.power](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")
(10, [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-2, 1, dtype\=float)),
}

grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(linear\_svm, param\_grid\=param\_grid, scoring\="roc\_auc\_ovr")
start \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
():
    [warnings.simplefilter](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter")
("ignore", category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
)
    grid\_search.fit(X, y)

print(
    f"GridSearchCV took {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start:.2f} seconds for "
    f"{len(grid\_search.cv\_results\_\['params'\])} candidate parameter settings."
)
report(grid\_search.cv\_results\_)

Copy to clipboard

GridSearchCV took 130.63 seconds for 60 candidate parameter settings.
Model with rank: 1
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(0.01), 'average': False, 'l1\_ratio': np.float64(0.5555555555555556)}

Model with rank: 2
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(0.1), 'average': False, 'l1\_ratio': np.float64(0.0)}

Model with rank: 3
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(1.0), 'average': False, 'l1\_ratio': np.float64(0.0)}

Copy to clipboard

Randomized search[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#randomized-search "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

[`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
 samples a fixed number of candidates from the parameter distributions instead of evaluating a predefined grid. Sampling lets us explore the continuous distributions directly and spend our budget where it matters. Here we use only half as many candidates as the grid above, yet the randomized search reaches results equivalent to the grid search while fitting far fewer configurations.

import scipy.stats as stats

from sklearn.model\_selection import [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")

param\_dist \= {
    "average": \[True, False\],
    "l1\_ratio": [stats.uniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html#scipy.stats.uniform "scipy.stats.uniform")
(0, 1),
    "alpha": [stats.loguniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform")
(1e-2, 1e0),
}

n\_iter\_search \= 30
random\_search \= [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
(
    linear\_svm,
    param\_distributions\=param\_dist,
    n\_iter\=n\_iter\_search,
    scoring\="roc\_auc\_ovr",
    random\_state\=42,
)

start \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
():
    [warnings.simplefilter](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter")
("ignore", category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
)
    random\_search.fit(X, y)
print(
    f"RandomizedSearchCV took {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start:.2f} seconds for {n\_iter\_search} "
    f"candidates parameter settings."
)
report(random\_search.cv\_results\_)

Copy to clipboard

RandomizedSearchCV took 52.56 seconds for 30 candidates parameter settings.
Model with rank: 1
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(0.1673808578875213), 'average': False, 'l1\_ratio': np.float64(0.04666566321361543)}

Model with rank: 2
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(0.04649617447336333), 'average': False, 'l1\_ratio': np.float64(0.7080725777960455)}

Model with rank: 3
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(0.3503398491158687), 'average': False, 'l1\_ratio': np.float64(0.2934881747180381)}

Copy to clipboard

Successive halving search[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#successive-halving-search "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
 samples candidates like the randomized search, but evaluates them on increasing amounts of resources (here the number of training samples). It starts with many candidates trained on a small subset of the data and, at each iteration, keeps only the most promising ones and grants them more samples. We therefore get the best of both worlds: a large number of candidates – which makes it more likely to find a good configuration – while keeping the fit and predict cost low in the early iterations where most candidates are discarded.

from sklearn.experimental import enable\_halving\_search\_cv  \# noqa: F401
from sklearn.model\_selection import [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")

n\_candidates \= 60
halving\_search \= [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
(
    linear\_svm,
    param\_distributions\=param\_dist,
    n\_candidates\=n\_candidates,
    scoring\="roc\_auc\_ovr",
    random\_state\=42,
    min\_resources\=100,
)
start \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
():
    [warnings.simplefilter](https://docs.python.org/3/library/warnings.html#warnings.simplefilter "warnings.simplefilter")
("ignore", category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
)
    halving\_search.fit(X, y)

print(
    f"HalvingRandomSearchCV took {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start:.2f} seconds for "
    f"{halving\_search.n\_candidates\_\[0\]} initial candidate parameter settings."
)
report(halving\_search.cv\_results\_)

Copy to clipboard

HalvingRandomSearchCV took 55.17 seconds for 60 initial candidate parameter settings.
Model with rank: 1
Mean validation score: 1.000 (std: 0.000)
Parameters: {'alpha': np.float64(0.7121996518301618), 'average': False, 'l1\_ratio': np.float64(0.11586905952512971)}

Model with rank: 2
Mean validation score: 1.000 (std: 0.001)
Parameters: {'alpha': np.float64(0.21137059440645725), 'average': False, 'l1\_ratio': np.float64(0.4251558744912447)}

Model with rank: 3
Mean validation score: 0.999 (std: 0.001)
Parameters: {'alpha': np.float64(0.697828126512603), 'average': False, 'l1\_ratio': np.float64(0.5704439744053994)}

Copy to clipboard

Conclusion[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html#conclusion "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Running the three searches on the same problem highlights their trade-offs:

*   **Grid search** evaluates all 60 combinations of the grid and reaches a best mean validation ROC AUC of essentially 1.0. It is exhaustive, but its cost grows with the resolution of the grid and a finer grid would be needed to refine the continuous parameters, making it the slowest of the three.
    
*   **Randomized search** reaches an essentially equivalent score while sampling only 30 candidates, i.e. half the budget, and is therefore markedly faster. Drawing the continuous parameters from distributions is usually a better use of a limited budget than refining a grid.
    
*   **Successive halving** screens the 60 candidates for a run time comparable to the randomized search by spending most of its resources only on the most promising candidates. It explores more candidates than the randomized search without paying the full cost of the grid search.
    

A word of caution when reading the halving output: the `cv_results_` of [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
 aggregates every iteration, including the first ones evaluated on very few samples where perfect but unreliable scores are common. This is why the `report` helper above keeps only the last iteration for the halving search, so that the reported scores are computed on the full set of resources and remain comparable to the grid and randomized searches. More generally, rely on `best_params_` – which the halving search selects among the last-iteration candidates – and confirm the chosen model on a held-out test set.

**Total running time of the script:** (3 minutes 58.371 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_randomized_search.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_randomized_search.ipynb)

[`Download Jupyter notebook: plot_randomized_search.ipynb`](https://scikit-learn.org/stable/_downloads/733ff7845fe2f197ecd0c72afcf23651/plot_randomized_search.ipynb)

[`Download Python source code: plot_randomized_search.py`](https://scikit-learn.org/stable/_downloads/f6e7c2e766100e8bcbb85bbb947d2893/plot_randomized_search.py)

[`Download zipped: plot_randomized_search.zip`](https://scikit-learn.org/stable/_downloads/98b05156f2b58b0d71d37e809c834124/plot_randomized_search.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_iterations_thumb.png)

[Successive Halving Iterations](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html)

Successive Halving Iterations

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)

[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Comparison between grid search and successive halving

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f6e7c2e766100e8bcbb85bbb947d2893/plot_randomized_search.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/733ff7845fe2f197ecd0c72afcf23651/plot_randomized_search.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/98b05156f2b58b0d71d37e809c834124/plot_randomized_search.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_randomized_search.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_randomized_search.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)