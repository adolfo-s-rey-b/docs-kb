[Skip to main content](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/callbacks/plot_scoring_monitor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/callbacks/plot_scoring_monitor.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/callbacks/plot_scoring_monitor.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/callbacks/plot_scoring_monitor.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/callbacks/plot_scoring_monitor.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/callbacks/plot_scoring_monitor.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#sphx-glr-download-auto-examples-callbacks-plot-scoring-monitor-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Analysis of the convergence of penalized logistic regression models[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#analysis-of-the-convergence-of-penalized-logistic-regression-models "Link to this heading")

=====================================================================================================================================================================================================================================================

The purpose of this example is three-fold:

1.  Demonstrate registering a [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
     on the logistic regression step of a pipeline nested inside [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    .
    
2.  Show how to plot the metric values collected at each iteration of each fit of the logistic regression model during the grid search and analyze the convergence of the model for each hyperparameter combination.
    
3.  Show how the monitoring of diverse scoring metrics can inform us about the quality of the model and the trade-off between refinement and calibration.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Setup[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#setup "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Let’s first define the pipeline and the grid search. Here we register a [`ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
 callback on the logistic regression model to monitor the scores at each iteration of the L-BFGS solver.

We reuse the same scoring metrics for the grid search itself and use the D² log-loss as the primary metric to select the best hyperparameter combination.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.callback import [ProgressBar](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
, [ScoringMonitor](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=1000, n\_features\=100, n\_classes\=10, n\_informative\=30, random\_state\=42
)

scoring\_metrics \= \["d2\_log\_loss\_score", "accuracy", "average\_precision"\]
scoring\_monitor \= [ScoringMonitor](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
(scoring\=scoring\_metrics)
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(solver\="lbfgs", max\_iter\=1000).set\_callbacks(scoring\_monitor),
)

param\_grid \= {
    "standardscaler\_\_with\_std": \[True, False\],
    "logisticregression\_\_C": [np.geomspace](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")
(0.01, 100, 3),
}

grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    model,
    param\_grid,
    cv\=5,
    scoring\=scoring\_metrics,
    n\_jobs\=2,
    error\_score\="raise",
    refit\=scoring\_metrics\[0\],
)

Copy to clipboard

Let’s fit the grid search with the auto-propagating progress bar callback. Feel free to set max\_propagation\_depth=3 in the ProgressBar constructor to get a more detailed output by displaying the progress bars for the pipeline, the standard scaler and the logistic regression.

grid\_search.set\_callbacks([ProgressBar](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
()).fit(X, y)

Copy to clipboard

GridSearchCV - fit                                                 ━━━ 100% 0:0…
  GridSearchCV - search #0                                         ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #0  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #1  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #2  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #3  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #4  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #5  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #6  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #7  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #8  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #9  ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #10 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #11 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #12 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #13 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #14 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #15 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #16 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #17 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #18 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #19 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #20 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #21 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #22 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #23 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #24 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #25 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #26 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #27 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #28 ━━━ 100% 0:0…
    GridSearchCV - candidate-split-evaluation | Pipeline - fit #29 ━━━ 100% 0:0…
  GridSearchCV - refit-with-best-params | Pipeline - fit #1        ━━━ 100% 0:0…

Copy to clipboard

GridSearchCV(cv=5, error\_score='raise',
             estimator=Pipeline(steps=\[('standardscaler', StandardScaler()),\
                                       ('logisticregression',\
                                        LogisticRegression(max\_iter=1000))\]),
             n\_jobs=2,
             param\_grid={'logisticregression\_\_C': array(\[1.e-02, 1.e+00, 1.e+02\]),
                         'standardscaler\_\_with\_std': \[True, False\]},
             refit='d2\_log\_loss\_score',
             scoring=\['d2\_log\_loss\_score', 'accuracy', 'average\_precision'\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...\_iter=1000))\]) |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | {'logisticregression\_\_C': array(\[1.e-02...e+00, 1.e+02\]), 'standardscaler\_\_with\_std': \[True, False\]} |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | \['d2\_log\_loss\_score', 'accuracy', ...\] |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | 2   |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | 'd2\_log\_loss\_score' |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | 5   |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | 'raise' |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | Pipeline | Pipeline(step...\_iter=1000))\]) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(1) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'lo...\_C': np.float64(0.01), 'st...td': False} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the best\_estimator  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.  <br>  <br>This attribute is not available if \`\`refit\`\` is a function.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_score_,-float) | float64 | 0.1706 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](10,) | \[0,1,2,...,7,8,9\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.2121... 3.88371768\]), 'me...me': array(\[0.0190... 0.01351433\]), 'me...cy': array(\[0.296,...0.26 , 0.258\]), 'me...on': array(\[0.2980... 0.26786657\]), ...} |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | True |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 100 |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 1.074 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | dict | {'ac...cy': make\_scorer(a...hod='predict'), 'av...on': make\_scorer(a...edict\_proba')), 'd2...re': make\_scorer(d...redict\_proba')} |

best\_estimator\_: Pipeline

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | False |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](100,) | \[-0.1 , 0.05, 0. ,..., 0.06,-0. , 0.3 \] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 100 |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1000 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | NoneType | None |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | NoneType | None |

100 features

|     |
| --- |
| x0  |
| x1  |
| x2  |
| x3  |
| x4  |
| x5  |
| x6  |
| x7  |
| x8  |
| x9  |
| x10 |
| x11 |
| x12 |
| x13 |
| x14 |
| x15 |
| x16 |
| x17 |
| x18 |
| x19 |
| x20 |
| x21 |
| x22 |
| x23 |
| x24 |
| x25 |
| x26 |
| x27 |
| x28 |
| x29 |
| x30 |
| x31 |
| x32 |
| x33 |
| x34 |
| x35 |
| x36 |
| x37 |
| x38 |
| x39 |
| x40 |
| x41 |
| x42 |
| x43 |
| x44 |
| x45 |
| x46 |
| x47 |
| x48 |
| x49 |
| x50 |
| x51 |
| x52 |
| x53 |
| x54 |
| x55 |
| x56 |
| x57 |
| x58 |
| x59 |
| x60 |
| x61 |
| x62 |
| x63 |
| x64 |
| x65 |
| x66 |
| x67 |
| x68 |
| x69 |
| x70 |
| x71 |
| x72 |
| x73 |
| x74 |
| x75 |
| x76 |
| x77 |
| x78 |
| x79 |
| x80 |
| x81 |
| x82 |
| x83 |
| x84 |
| x85 |
| x86 |
| x87 |
| x88 |
| x89 |
| x90 |
| x91 |
| x92 |
| x93 |
| x94 |
| x95 |
| x96 |
| x97 |
| x98 |
| x99 |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | np.float64(0.01) |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 1000 |
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](10,) | \[0,1,2,...,7,8,9\] |
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](10, 100) | \[\[ 0.14,-0. , 0.06,..., 0.01, 0. ,-0. \], \[ 0.01, 0.04, 0.01,..., 0.02,-0.03, 0.01\], \[-0.11,-0.04, 0.06,...,-0.06, 0.06, 0. \], ..., \[-0.06, 0.05, 0.04,...,-0.07, 0.03, 0.02\], \[-0.03, 0. ,-0.05,..., 0.04,-0.06,-0.14\], \[-0.04,-0.05, 0. ,..., 0.03,-0. , 0.05\]\] |
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](10,) | \[-0. , 0.23,-0.15,..., 0.13,-0.07,-0.18\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 100 |
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[77\] |

  
  

We use a grid search with 3 values for the regularization parameter `C` and 2 values for the standardization of the features resulting in 6 parameter combinations.

Since we use 5-fold cross-validation (`cv=5`), we will have 5 fits of the logistic regression model for each parameter combination resulting in 30 fits as subtasks of the “search” [fit task](https://scikit-learn.org/stable/glossary.html#term-fit-task)
.

In addition, the grid search performs a final refit on the full dataset with the best hyperparameter combination found during the grid search. This is visible as the “refit-with-best-params” task in the output above.

Consolidation of the grid search results[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#consolidation-of-the-grid-search-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s look at the results of the grid search.

cv\_results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(grid\_search.cv\_results\_)
cv\_results.sort\_values(by\="rank\_test\_d2\_log\_loss\_score", ascending\=True)

Copy to clipboard

|     | mean\_fit\_time | std\_fit\_time | mean\_score\_time | std\_score\_time | param\_logisticregression\_\_C | param\_standardscaler\_\_with\_std | params | split0\_test\_d2\_log\_loss\_score | split1\_test\_d2\_log\_loss\_score | split2\_test\_d2\_log\_loss\_score | split3\_test\_d2\_log\_loss\_score | split4\_test\_d2\_log\_loss\_score | mean\_test\_d2\_log\_loss\_score | std\_test\_d2\_log\_loss\_score | rank\_test\_d2\_log\_loss\_score | split0\_test\_accuracy | split1\_test\_accuracy | split2\_test\_accuracy | split3\_test\_accuracy | split4\_test\_accuracy | mean\_test\_accuracy | std\_test\_accuracy | rank\_test\_accuracy | split0\_test\_average\_precision | split1\_test\_average\_precision | split2\_test\_average\_precision | split3\_test\_average\_precision | split4\_test\_average\_precision | mean\_test\_average\_precision | std\_test\_average\_precision | rank\_test\_average\_precision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1.477605 | 0.081582 | 0.014521 | 0.004147 | 0.01 | False | {'logisticregression\_\_C': 0.01, 'standardscale... | 0.135960 | 0.167780 | 0.189062 | 0.173567 | 0.186634 | 0.170601 | 0.019051 | 1   | 0.285 | 0.330 | 0.330 | 0.355 | 0.305 | 0.321 | 0.023958 | 1   | 0.319819 | 0.309708 | 0.360697 | 0.323126 | 0.340503 | 0.330771 | 0.017957 | 1   |
| 0   | 0.212196 | 0.032597 | 0.019046 | 0.012373 | 0.01 | True | {'logisticregression\_\_C': 0.01, 'standardscale... | 0.125785 | 0.112817 | 0.129538 | 0.127723 | 0.140616 | 0.127296 | 0.008883 | 2   | 0.290 | 0.275 | 0.315 | 0.320 | 0.280 | 0.296 | 0.018276 | 2   | 0.293645 | 0.258271 | 0.320959 | 0.290856 | 0.326432 | 0.298033 | 0.024429 | 2   |
| 2   | 0.505105 | 0.047843 | 0.012597 | 0.000717 | 1.00 | True | {'logisticregression\_\_C': 1.0, 'standardscaler... | \-0.262989 | \-0.348023 | \-0.293989 | \-0.300126 | \-0.229700 | \-0.286965 | 0.039509 | 3   | 0.270 | 0.245 | 0.260 | 0.230 | 0.290 | 0.259 | 0.020591 | 5   | 0.299362 | 0.258130 | 0.268917 | 0.268336 | 0.276840 | 0.274317 | 0.013860 | 3   |
| 3   | 3.822518 | 0.123444 | 0.024284 | 0.011158 | 1.00 | False | {'logisticregression\_\_C': 1.0, 'standardscaler... | \-0.344269 | \-0.424780 | \-0.381219 | \-0.380261 | \-0.299665 | \-0.366039 | 0.041863 | 4   | 0.280 | 0.250 | 0.260 | 0.230 | 0.280 | 0.260 | 0.018974 | 3   | 0.296932 | 0.259109 | 0.266720 | 0.268014 | 0.275371 | 0.273229 | 0.012926 | 4   |
| 4   | 0.539036 | 0.035050 | 0.023094 | 0.013744 | 100.00 | True | {'logisticregression\_\_C': 100.0, 'standardscal... | \-0.455882 | \-0.566974 | \-0.524439 | \-0.507518 | \-0.417598 | \-0.494482 | 0.052390 | 5   | 0.285 | 0.235 | 0.265 | 0.230 | 0.285 | 0.260 | 0.023664 | 3   | 0.293392 | 0.253425 | 0.258071 | 0.263983 | 0.271392 | 0.268052 | 0.014024 | 5   |
| 5   | 3.883718 | 0.593627 | 0.013514 | 0.003835 | 100.00 | False | {'logisticregression\_\_C': 100.0, 'standardscal... | \-0.458082 | \-0.571424 | \-0.526726 | \-0.510858 | \-0.419702 | \-0.497358 | 0.053110 | 6   | 0.285 | 0.235 | 0.255 | 0.230 | 0.285 | 0.258 | 0.023580 | 6   | 0.293282 | 0.253446 | 0.257693 | 0.263782 | 0.271130 | 0.267867 | 0.014034 | 6   |

  
  

We observe that the best models use regularization (small `C`). Feature standardization does not seem to matter much but helps reduce the fit times. We notice that many models have similar accuracy scores but different D² log-loss scores and average precision scores. D² log-loss and average precision are more sensitive to the quality of the model than accuracy because they evaluate the entire probability distribution of the predictions rather than just the match of the top predicted class with the true class.

Let’s now refine this analysis by looking at the same metrics computed on the training set at each iteration of the L-BFGS solver and for each parameter combination. Note that these are training-set scores recorded during L-BFGS iterations, not the held-out CV scores from `cv_results_`.

These values are stored in the `scoring_monitor` callback object:

all\_tasks\_log \= scoring\_monitor.get\_logs().data\_as\_pandas
all\_tasks\_log

Copy to clipboard

|     | task\_id\_path | parent\_task\_id\_path | estimator\_name | task\_name | task\_id | sequential\_subtasks | d2\_log\_loss\_score | accuracy | average\_precision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | (0, 1, 1) | (0, 1) | LogisticRegression | fit | 1   | True | 0.399415 | 0.53100 | 0.506463 |
| 1   | (0, 0, 0, 1) | (0, 0, 0) | LogisticRegression | fit | 1   | True | 0.306252 | 0.56000 | 0.565995 |
| 2   | (0, 0, 1, 1) | (0, 0, 1) | LogisticRegression | fit | 1   | True | 0.311447 | 0.57875 | 0.587007 |
| 3   | (0, 0, 2, 1) | (0, 0, 2) | LogisticRegression | fit | 1   | True | 0.305960 | 0.56250 | 0.564362 |
| 4   | (0, 0, 3, 1) | (0, 0, 3) | LogisticRegression | fit | 1   | True | 0.309061 | 0.58875 | 0.574045 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 2765 | (0, 0, 29, 1, 192) | (0, 0, 29, 1) | LogisticRegression | lbfgs-iter | 192 | True | 0.552078 | 0.66750 | 0.557115 |
| 2766 | (0, 0, 29, 1, 193) | (0, 0, 29, 1) | LogisticRegression | lbfgs-iter | 193 | True | 0.552078 | 0.66750 | 0.557045 |
| 2767 | (0, 0, 29, 1, 194) | (0, 0, 29, 1) | LogisticRegression | lbfgs-iter | 194 | True | 0.552078 | 0.66750 | 0.557063 |
| 2768 | (0, 0, 29, 1, 195) | (0, 0, 29, 1) | LogisticRegression | lbfgs-iter | 195 | True | 0.552078 | 0.66750 | 0.556962 |
| 2769 | (0, 0, 29, 1, 196) | (0, 0, 29, 1) | LogisticRegression | lbfgs-iter | 196 | True | 0.552078 | 0.66750 | 0.556983 |

2770 rows × 9 columns

  
  

Let’s enrich this log with the candidate parameters and the split index so we can plot the scores for each parameter combination for a particular CV split of interest.

candidate\_params \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(grid\_search.cv\_results\_\["params"\]).add\_prefix("param\_")

n\_splits \= grid\_search.n\_splits\_
lbfgs\_log \= all\_tasks\_log.query(
    "estimator\_name == 'LogisticRegression' and task\_name == 'lbfgs-iter'"
).copy()
\# Index 2 in \`\`task\_id\_path\`\` is the \`\`candidate-split-evaluation\`\` task id.
\# Future versions of scikit-learn will provide a more convenient way to
\# retrieve this task id.
lbfgs\_log\["eval\_task\_id"\] \= lbfgs\_log\["task\_id\_path"\].map(lambda path: path\[2\])
lbfgs\_log\["candidate\_idx"\] \= lbfgs\_log\["eval\_task\_id"\] // n\_splits
lbfgs\_log\["split\_idx"\] \= lbfgs\_log\["eval\_task\_id"\] % n\_splits
lbfgs\_log \= lbfgs\_log.query("split\_idx == 0").join(candidate\_params, on\="candidate\_idx")

Copy to clipboard

Exclude the final refit on the full dataset (`parent_task_id_path` starts with `(0, 1)` instead of `(0, 0)` for cross-validation fits). Note that it is possible to call `scoring_monitor.get_logs(include_lineage=True)` to retrieve the task name of the ancestor tasks if needed.

cv\_lbfgs\_log \= lbfgs\_log\[\
    lbfgs\_log\["parent\_task\_id\_path"\].map(lambda path: path\[1\]) \== 0\
\]

Copy to clipboard

We define labels for plotting purposes and plot each metric separately.

cv\_lbfgs\_log\["param\_label"\] \= cv\_lbfgs\_log.apply(
    lambda row: (
        f"with\_std={row\['param\_standardscaler\_\_with\_std'\]}, "
        f"C={row\['param\_logisticregression\_\_C'\]:.2g}"
    ),
    axis\=1,
)

metrics \= {
    "d2\_log\_loss\_score": "D² log-loss (train)",
    "accuracy": "Accuracy (train)",
    "average\_precision": "Average precision (train)",
}
\_, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    len(metrics),
    1,
    figsize\=(8, 2.5 \* len(metrics)),
    sharex\=True,
    constrained\_layout\=True,
)
for idx, (metric, ylabel) in enumerate(metrics.items()):
    ax \= axes\[idx\]
    for param\_label, group in cv\_lbfgs\_log.groupby("param\_label", sort\=False):
        ax.plot(group\["task\_id"\], group\[metric\], label\=param\_label)
    ax.set\_ylabel(ylabel)
    if idx \== 0:
        ax.set\_title("CV split 0")
        ax.legend(title\="Hyperparameters", fontsize\="small")

\_ \= axes\[\-1\].set\_xlabel("L-BFGS iteration")

Copy to clipboard

![CV split 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_001.png)

Analysis of the convergence of the logistic regression models[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#analysis-of-the-convergence-of-the-logistic-regression-models "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### D² log-loss convergence[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#d2-log-loss-convergence "Link to this heading")

The D² log-loss scores generally improve monotonically for all models. This is expected because the logistic regression model is fitted by minimizing the (regularized) log-loss computed on the training set.

### Accuracy fluctuations[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#accuracy-fluctuations "Link to this heading")

The accuracy score improves with the number of iterations, albeit with some local fluctuations. This is expected because accuracy is discontinuous and not directly optimized by the model. Instead the model minimizes the log-loss which is a smooth surrogate for the zero-one loss (and thus related to, but not directly optimized by, accuracy).

### Regularization and scaling[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#regularization-and-scaling "Link to this heading")

We also observe that the least regularized models (larger `C` values) tend to reach higher D² log-loss scores, and models trained on scaled features converge in much fewer iterations.

Furthermore, models trained with high regularization (lower `C` values) converge to a final D² log-loss value that depends on the regularization strength while this is not the case for models trained with low regularization: there is a strong coupling between the optimal regularization strength and the feature scaling.

### Average precision vs log-loss, refinement vs calibration[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#average-precision-vs-log-loss-refinement-vs-calibration "Link to this heading")

Finally, we observe that the average precision value measured on the training set can improve quickly in the first iterations and then worsen even though the D² log-loss value continues to improve on the same training data. This is especially noticeable for models trained with low regularization and feature standardization. This counter-intuitive behavior can be explained as follows. First recall that average precision is a pure ranking metric that measures the ability of the model to output predicted probabilities that rank the samples of a given class higher than the samples of the other classes, but does not take into account the calibration of the predicted probabilities. In other words, average precision only evaluates if the predicted probabilities are well ordered relatively to one another but is insensitive to a rank preserving transformation of their absolute values. The log-loss, on the other hand, is a strictly proper scoring rule that accounts for both the refinement (ranking power) of the model and the calibration of the predicted probabilities.

Therefore, the average precision curves of the low-regularized models trained on scaled features suggest that the first iterations mostly improve refinement of the models temporarily leaving calibration behind. In later iterations, the log-loss score continues to improve but average precision values worsen, which suggests that the logistic regression model progressively trades off refinement for calibration over the course of the final iterations. This phenomenon has been studied in [\[1\]](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#id2)
.

It would be interesting to see if this also happens when evaluating the model on a validation set so we could implement early stopping on average precision to explicitly select a model with high refinement on a validation set. This is not yet possible at the time of writing. Giving callbacks access to the validation set is planned for a future version of scikit-learn. Note that the callbacks API is still experimental and may change without the usual deprecation cycle.

References[#](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html#references "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

**Total running time of the script:** (0 minutes 29.194 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo3.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/callbacks/plot_scoring_monitor.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo3.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/callbacks/plot_scoring_monitor.ipynb)

[`Download Jupyter notebook: plot_scoring_monitor.ipynb`](https://scikit-learn.org/stable/_downloads/ce886caeea0a1431c0e5ed4ef01bf2b9/plot_scoring_monitor.ipynb)

[`Download Python source code: plot_scoring_monitor.py`](https://scikit-learn.org/stable/_downloads/4fe2b2aa32a37e8f0bb8f4d7954425d1/plot_scoring_monitor.py)

[`Download zipped: plot_scoring_monitor.zip`](https://scikit-learn.org/stable/_downloads/feb6f3b68aa660e6deb4aa408c613d09/plot_scoring_monitor.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_randomized_search_thumb.png)

[Comparing randomized search and grid search for hyperparameter estimation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html)

Comparing randomized search and grid search for hyperparameter estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4fe2b2aa32a37e8f0bb8f4d7954425d1/plot_scoring_monitor.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ce886caeea0a1431c0e5ed4ef01bf2b9/plot_scoring_monitor.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/feb6f3b68aa660e6deb4aa408c613d09/plot_scoring_monitor.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo3.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/callbacks/plot_scoring_monitor.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo3.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/callbacks/plot_scoring_monitor.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)