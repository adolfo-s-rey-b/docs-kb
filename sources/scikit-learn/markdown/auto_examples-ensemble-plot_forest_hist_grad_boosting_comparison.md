[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#sphx-glr-download-auto-examples-ensemble-plot-forest-hist-grad-boosting-comparison-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing Random Forests and Histogram Gradient Boosting models[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#comparing-random-forests-and-histogram-gradient-boosting-models "Link to this heading")

=================================================================================================================================================================================================================================================================

In this example we compare the performance of Random Forest (RF) and Histogram Gradient Boosting (HGBT) models in terms of score and computation time for a regression dataset, though **all the concepts here presented apply to classification as well**.

The comparison is made by varying the parameters that control the number of trees according to each estimator:

*   `n_estimators` controls the number of trees in the forest. It’s a fixed number.
    
*   `max_iter` is the maximum number of iterations in a gradient boosting based model. The number of iterations corresponds to the number of trees for regression and binary classification problems. Furthermore, the actual number of trees required by the model depends on the stopping criteria.
    

HGBT uses gradient boosting to iteratively improve the model’s performance by fitting each tree to the negative gradient of the loss function with respect to the predicted value. RFs, on the other hand, are based on bagging and use a majority vote to predict the outcome.

See the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#ensemble)
 for more information on ensemble models or see [Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-auto-examples-ensemble-plot-hgbt-regression-py)
 for an example showcasing some other features of HGBT models.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load dataset[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#load-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.datasets import [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")

X, y \= [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
(return\_X\_y\=True, as\_frame\=True)
n\_samples, n\_features \= X.shape

Copy to clipboard

HGBT uses a histogram-based algorithm on binned feature values that can efficiently handle large datasets (tens of thousands of samples or more) with a high number of features (see [Why it’s faster](https://scikit-learn.org/stable/modules/ensemble.html#why-it-s-faster)
). The scikit-learn implementation of RF does not use binning and relies on exact splitting, which can be computationally expensive.

print(f"The dataset consists of {n\_samples} samples and {n\_features} features")

Copy to clipboard

The dataset consists of 20640 samples and 8 features

Copy to clipboard

Compute score and computation times[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#compute-score-and-computation-times "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Notice that many parts of the implementation of [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 are parallelized by default.

The implementation of [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
 and [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 can also be run on multiple cores by using the `n_jobs` parameter, here set to match the number of physical cores on the host machine. See [Parallelism](https://scikit-learn.org/stable/computing/parallelism.html#parallelism)
 for more information.

import joblib

N\_CORES \= [joblib.cpu\_count](https://joblib.readthedocs.io/en/latest/generated/joblib.cpu_count.html#joblib.cpu_count "joblib.cpu_count")
(only\_physical\_cores\=True)
print(f"Number of physical cores: {N\_CORES}")

Copy to clipboard

Number of physical cores: 3

Copy to clipboard

Unlike RF, HGBT models offer an early-stopping option (see [Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-early-stopping-py)
) to avoid adding new unnecessary trees. Internally, the algorithm uses an out-of-sample set to compute the generalization performance of the model at each addition of a tree. Thus, if the generalization performance is not improving for more than `n_iter_no_change` iterations, it stops adding trees.

The other parameters of both models were tuned but the procedure is not shown here to keep the example simple.

import pandas as pd

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
, [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")

models \= {
    "Random Forest": [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
(
        min\_samples\_leaf\=5, random\_state\=0, n\_jobs\=N\_CORES
    ),
    "Hist Gradient Boosting": [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
        max\_leaf\_nodes\=15, random\_state\=0, early\_stopping\=False
    ),
}
param\_grids \= {
    "Random Forest": {"n\_estimators": \[10, 20, 50, 100\]},
    "Hist Gradient Boosting": {"max\_iter": \[10, 20, 50, 100, 300, 500\]},
}
cv \= [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
(n\_splits\=4, shuffle\=True, random\_state\=0)

results \= \[\]
for name, model in models.items():
    grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
        estimator\=model,
        param\_grid\=param\_grids\[name\],
        return\_train\_score\=True,
        cv\=cv,
    ).fit(X, y)
    result \= {"model": name, "cv\_results": [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(grid\_search.cv\_results\_)}
    results.append(result)

Copy to clipboard

Note

Tuning the `n_estimators` for RF generally results in a waste of computer power. In practice one just needs to ensure that it is large enough so that doubling its value does not lead to a significant improvement of the testing score.

Plot results[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#plot-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

We can use a [plotly.express.scatter](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html)
 to visualize the trade-off between elapsed computing time and mean test score. Passing the cursor over a given point displays the corresponding parameters. Error bars correspond to one standard deviation as computed in the different folds of the cross-validation.

import plotly.colors as colors
import plotly.express as px
from plotly.subplots import make\_subplots

fig \= make\_subplots(
    rows\=1,
    cols\=2,
    shared\_yaxes\=True,
    subplot\_titles\=\["Train time vs score", "Predict time vs score"\],
)
model\_names \= \[result\["model"\] for result in results\]
colors\_list \= colors.qualitative.Plotly \* (
    len(model\_names) // len(colors.qualitative.Plotly) + 1
)

for idx, result in enumerate(results):
    cv\_results \= result\["cv\_results"\].round(3)
    model\_name \= result\["model"\]
    param\_name \= next(iter(param\_grids\[model\_name\].keys()))
    cv\_results\[param\_name\] \= cv\_results\["param\_" + param\_name\]
    cv\_results\["model"\] \= model\_name

    scatter\_fig \= px.scatter(
        cv\_results,
        x\="mean\_fit\_time",
        y\="mean\_test\_score",
        error\_x\="std\_fit\_time",
        error\_y\="std\_test\_score",
        hover\_data\=param\_name,
        color\="model",
    )
    line\_fig \= px.line(
        cv\_results,
        x\="mean\_fit\_time",
        y\="mean\_test\_score",
    )

    scatter\_trace \= scatter\_fig\["data"\]\[0\]
    line\_trace \= line\_fig\["data"\]\[0\]
    scatter\_trace.update(marker\=dict(color\=colors\_list\[idx\]))
    line\_trace.update(line\=dict(color\=colors\_list\[idx\]))
    fig.add\_trace(scatter\_trace, row\=1, col\=1)
    fig.add\_trace(line\_trace, row\=1, col\=1)

    scatter\_fig \= px.scatter(
        cv\_results,
        x\="mean\_score\_time",
        y\="mean\_test\_score",
        error\_x\="std\_score\_time",
        error\_y\="std\_test\_score",
        hover\_data\=param\_name,
    )
    line\_fig \= px.line(
        cv\_results,
        x\="mean\_score\_time",
        y\="mean\_test\_score",
    )

    scatter\_trace \= scatter\_fig\["data"\]\[0\]
    line\_trace \= line\_fig\["data"\]\[0\]
    scatter\_trace.update(marker\=dict(color\=colors\_list\[idx\]))
    line\_trace.update(line\=dict(color\=colors\_list\[idx\]))
    fig.add\_trace(scatter\_trace, row\=1, col\=2)
    fig.add\_trace(line\_trace, row\=1, col\=2)

fig.update\_layout(
    xaxis\=dict(title\="Train time (s) - lower is better"),
    yaxis\=dict(title\="Test R2 score - higher is better"),
    xaxis2\=dict(title\="Predict time (s) - lower is better"),
    legend\=dict(x\=0.72, y\=0.05, traceorder\="normal", borderwidth\=1),
    title\=dict(x\=0.5, text\="Speed-score trade-off of tree-based ensembles"),
)

Copy to clipboard

00.511.520.60.650.70.750.80.8500.020.040.060.08

Random ForestHist Gradient BoostingSpeed-score trade-off of tree-based ensemblesTrain time (s) - lower is betterPredict time (s) - lower is betterTest R2 score - higher is betterTrain time vs scorePredict time vs score

[plotly-logomark](https://plotly.com/)

  
  

Both HGBT and RF models improve when increasing the number of trees in the ensemble. However, the scores reach a plateau where adding new trees just makes fitting and scoring slower. The RF model reaches such plateau earlier and can never reach the test score of the largest HGBDT model.

Note that the results shown on the above plot can change slightly across runs and even more significantly when running on other machines: try to run this example on your own local machine.

Overall, one should often observe that the Histogram-based gradient boosting models uniformly dominate the Random Forest models in the “test score vs training speed trade-off” (the HGBDT curve should be on the top left of the RF curve, without ever crossing). The “test score vs prediction speed” trade-off can also be more disputed, but it’s most often favorable to HGBDT. It’s always a good idea to check both kinds of model (with hyper-parameter tuning) and compare their performance on your specific problem to determine which model is the best fit but **HGBT almost always offers a more favorable speed-accuracy trade-off than RF**, either with the default hyper-parameters or including the hyper-parameter tuning cost.

There is one exception to this rule of thumb though: when training a multiclass classification model with a large number of possible classes, HGBDT fits internally one-tree per class at each boosting iteration while the trees used by the RF models are naturally multiclass which should improve the speed accuracy trade-off of the RF models in this case.

**Total running time of the script:** (0 minutes 29.210 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.ipynb)

[`Download Jupyter notebook: plot_forest_hist_grad_boosting_comparison.ipynb`](https://scikit-learn.org/stable/_downloads/7c8070aa163e648367101a22133c5711/plot_forest_hist_grad_boosting_comparison.ipynb)

[`Download Python source code: plot_forest_hist_grad_boosting_comparison.py`](https://scikit-learn.org/stable/_downloads/96b1c8376e660407547a7226ce8b3bab/plot_forest_hist_grad_boosting_comparison.py)

[`Download zipped: plot_forest_hist_grad_boosting_comparison.zip`](https://scikit-learn.org/stable/_downloads/35620548aa1dcefbc9e36e7330feafdc/plot_forest_hist_grad_boosting_comparison.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png)

[Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Sample pipeline for text feature extraction and evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/96b1c8376e660407547a7226ce8b3bab/plot_forest_hist_grad_boosting_comparison.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7c8070aa163e648367101a22133c5711/plot_forest_hist_grad_boosting_comparison.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/35620548aa1dcefbc9e36e7330feafdc/plot_forest_hist_grad_boosting_comparison.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)