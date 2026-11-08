[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_multi_metric_evaluation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_multi_metric_evaluation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_multi_metric_evaluation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_multi_metric_evaluation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_multi_metric_evaluation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_multi_metric_evaluation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#sphx-glr-download-auto-examples-model-selection-plot-multi-metric-evaluation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#demonstration-of-multi-metric-evaluation-on-cross-val-score-and-gridsearchcv "Link to this heading")

=======================================================================================================================================================================================================================================================================================

Multiple metric parameter search can be done by setting the `scoring` parameter to a list of metric scorer names or a dict mapping the scorer names to the scorer callables.

The scores of all the scorers are available in the `cv_results_` dict at keys ending in `'_<scorer_name>'` (`'mean_test_precision'`, `'rank_test_precision'`, etc…)

The `best_estimator_`, `best_index_`, `best_score_` and `best_params_` correspond to the scorer (key) that is set to the `refit` attribute.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import [make\_hastie\_10\_2](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "sklearn.datasets.make_hastie_10_2")
from sklearn.metrics import [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
, [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

Copy to clipboard

Running `GridSearchCV` using multiple evaluation metrics[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#running-gridsearchcv-using-multiple-evaluation-metrics "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

X, y \= [make\_hastie\_10\_2](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "sklearn.datasets.make_hastie_10_2")
(n\_samples\=8000, random\_state\=42)

\# The scorers can be either one of the predefined metric strings or a scorer
\# callable, like the one returned by make\_scorer
scoring \= {"AUC": "roc\_auc", "Accuracy": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
)}

\# Setting refit='AUC', refits an estimator on the whole dataset with the
\# parameter setting that has the best cross-validated AUC score.
\# That estimator is made available at \`\`gs.best\_estimator\_\`\` along with
\# parameters like \`\`gs.best\_score\_\`\`, \`\`gs.best\_params\_\`\` and
\# \`\`gs.best\_index\_\`\`
gs \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(random\_state\=42),
    param\_grid\={"min\_samples\_split": range(2, 403, 20)},
    scoring\=scoring,
    refit\="AUC",
    n\_jobs\=2,
    return\_train\_score\=True,
)
gs.fit(X, y)
results \= gs.cv\_results\_

Copy to clipboard

Plotting the result[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#plotting-the-result "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(13, 13))
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("GridSearchCV evaluating using multiple scorers simultaneously", fontsize\=16)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("min\_samples\_split")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Score")

ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
ax.set\_xlim(0, 402)
ax.set\_ylim(0.73, 1)

\# Get the regular numpy array from the MaskedArray
X\_axis \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(results\["param\_min\_samples\_split"\].data, dtype\=float)

for scorer, color in zip(sorted(scoring), \["g", "k"\]):
    for sample, style in (("train", "--"), ("test", "-")):
        sample\_score\_mean \= results\["mean\_%s\_%s" % (sample, scorer)\]
        sample\_score\_std \= results\["std\_%s\_%s" % (sample, scorer)\]
        ax.fill\_between(
            X\_axis,
            sample\_score\_mean \- sample\_score\_std,
            sample\_score\_mean + sample\_score\_std,
            alpha\=0.1 if sample \== "test" else 0,
            color\=color,
        )
        ax.plot(
            X\_axis,
            sample\_score\_mean,
            style,
            color\=color,
            alpha\=1 if sample \== "test" else 0.7,
            label\="%s (%s)" % (scorer, sample),
        )

    best\_index \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
(results\["rank\_test\_%s" % scorer\] \== 1)\[0\]\[0\]
    best\_score \= results\["mean\_test\_%s" % scorer\]\[best\_index\]

    \# Plot a dotted vertical line at the best score for that scorer marked by x
    ax.plot(
        \[\
            X\_axis\[best\_index\],\
        \]
        \* 2,
        \[0, best\_score\],
        linestyle\="-.",
        color\=color,
        marker\="x",
        markeredgewidth\=3,
        ms\=8,
    )

    \# Annotate the best score for that scorer
    ax.annotate("%0.2f" % best\_score, (X\_axis\[best\_index\], best\_score + 0.005))

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(False)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![GridSearchCV evaluating using multiple scorers simultaneously](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_metric_evaluation_001.png)

**Total running time of the script:** (0 minutes 7.753 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_multi_metric_evaluation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_multi_metric_evaluation.ipynb)

[`Download Jupyter notebook: plot_multi_metric_evaluation.ipynb`](https://scikit-learn.org/stable/_downloads/f57e1ee55d4c7a51949d5c26b3af07bb/plot_multi_metric_evaluation.ipynb)

[`Download Python source code: plot_multi_metric_evaluation.py`](https://scikit-learn.org/stable/_downloads/dedbcc9464f3269f4f012f4bfc7d16da/plot_multi_metric_evaluation.py)

[`Download zipped: plot_multi_metric_evaluation.zip`](https://scikit-learn.org/stable/_downloads/535778bfbc9b4881da3e662bc2ea8484/plot_multi_metric_evaluation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)

[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Comparison between grid search and successive halving

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/dedbcc9464f3269f4f012f4bfc7d16da/plot_multi_metric_evaluation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f57e1ee55d4c7a51949d5c26b3af07bb/plot_multi_metric_evaluation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/535778bfbc9b4881da3e662bc2ea8484/plot_multi_metric_evaluation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_multi_metric_evaluation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_multi_metric_evaluation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)