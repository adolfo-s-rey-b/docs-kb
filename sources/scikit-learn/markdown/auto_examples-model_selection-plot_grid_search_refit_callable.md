[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_grid_search_refit_callable.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_grid_search_refit_callable.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_grid_search_refit_callable.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_grid_search_refit_callable.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_grid_search_refit_callable.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#sphx-glr-download-auto-examples-model-selection-plot-grid-search-refit-callable-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Balance model complexity and cross-validated score[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#balance-model-complexity-and-cross-validated-score "Link to this heading")

====================================================================================================================================================================================================================================

This example demonstrates how to balance model complexity and cross-validated score by finding a decent accuracy within 1 standard deviation of the best accuracy score while minimising the number of [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 components [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#id2)
. It uses [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 with a custom refit callable to select the optimal model.

The figure shows the trade-off between cross-validated score and the number of PCA components. The balanced case is when `n_components=10` and `accuracy=0.88`, which falls into the range within 1 standard deviation of the best accuracy score.

References[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#references "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
import polars as pl

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")

Copy to clipboard

Introduction[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#introduction "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

When tuning hyperparameters, we often want to balance model complexity and performance. The “one-standard-error” rule is a common approach: select the simplest model whose performance is within one standard error of the best model’s performance. This helps to avoid overfitting by preferring simpler models when their performance is statistically comparable to more complex ones.

Helper functions[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#helper-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

We define two helper functions:

1.  `lower_bound`: Calculates the threshold for acceptable performance (best score - 1 std)
    
2.  `best_low_complexity`: Selects the model with the fewest PCA components that exceeds this threshold
    

def lower\_bound(cv\_results):
    """
    Calculate the lower bound within 1 standard deviation
    of the best \`mean\_test\_scores\`.

    Parameters
    ----------
    cv\_results : dict of numpy(masked) ndarrays
        See attribute cv\_results\_ of \`GridSearchCV\`

    Returns
    -------
    float
        Lower bound within 1 standard deviation of the
        best \`mean\_test\_score\`.
    """
    best\_score\_idx \= [np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")
(cv\_results\["mean\_test\_score"\])

    return (
        cv\_results\["mean\_test\_score"\]\[best\_score\_idx\]
        \- cv\_results\["std\_test\_score"\]\[best\_score\_idx\]
    )

def best\_low\_complexity(cv\_results):
    """
    Balance model complexity with cross-validated score.

    Parameters
    ----------
    cv\_results : dict of numpy(masked) ndarrays
        See attribute cv\_results\_ of \`GridSearchCV\`.

    Return
    ------
    int
        Index of a model that has the fewest PCA components
        while has its test score within 1 standard deviation of the best
        \`mean\_test\_score\`.
    """
    threshold \= lower\_bound(cv\_results)
    candidate\_idx \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(cv\_results\["mean\_test\_score"\] \>= threshold)
    best\_idx \= candidate\_idx\[\
        cv\_results\["param\_reduce\_dim\_\_n\_components"\]\[candidate\_idx\].argmin()\
    \]
    return best\_idx

Copy to clipboard

Set up the pipeline and parameter grid[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#set-up-the-pipeline-and-parameter-grid "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We create a pipeline with two steps:

1.  Dimensionality reduction using PCA
    
2.  Classification using LogisticRegression
    

We’ll search over different numbers of PCA components to find the optimal complexity.

pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("reduce\_dim", [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(random\_state\=42)),\
        ("classify", [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(random\_state\=42, C\=0.01, max\_iter\=1000)),\
    \]
)

param\_grid \= {"reduce\_dim\_\_n\_components": \[6, 8, 10, 15, 20, 25, 35, 45, 55\]}

Copy to clipboard

Perform the search with GridSearchCV[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#perform-the-search-with-gridsearchcv "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We use `GridSearchCV` with our custom `best_low_complexity` function as the refit parameter. This function will select the model with the fewest PCA components that still performs within one standard deviation of the best model.

grid \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    pipe,
    \# Use a non-stratified CV strategy to make sure that the inter-fold
    \# standard deviation of the test scores is informative.
    cv\=[ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
(n\_splits\=30, random\_state\=0),
    n\_jobs\=1,  \# increase this on your machine to use more physical cores
    param\_grid\=param\_grid,
    scoring\="accuracy",
    refit\=best\_low\_complexity,
    return\_train\_score\=True,
)

Copy to clipboard

Load the digits dataset and fit the model[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#load-the-digits-dataset-and-fit-the-model "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

X, y \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
grid.fit(X, y)

Copy to clipboard

GridSearchCV(cv=ShuffleSplit(n\_splits=30, random\_state=0, test\_size=None, train\_size=None),
             estimator=Pipeline(steps=\[('reduce\_dim', PCA(random\_state=42)),\
                                       ('classify',\
                                        LogisticRegression(C=0.01,\
                                                           max\_iter=1000,\
                                                           random\_state=42))\]),
             n\_jobs=1,
             param\_grid={'reduce\_dim\_\_n\_components': \[6, 8, 10, 15, 20, 25, 35,\
                                                      45, 55\]},
             refit=<function best\_low\_complexity at 0x7e1d3b4c52d0>,
             return\_train\_score=True, scoring='accuracy')

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...m\_state=42))\]) |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | {'reduce\_dim\_\_n\_components': \[6, 8, ...\]} |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | 'accuracy' |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | 1   |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | <function bes...x7e1d3b4c52d0> |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | ShuffleSplit(...ain\_size=None) |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | True |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | Pipeline | Pipeline(step...m\_state=42))\]) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(5) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'re...ts': 25} |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](10,) | \[0,1,2,...,7,8,9\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.1106..., 0.06497336\]), 'me...me': array(\[0.0016..., 0.00172111\]), 'me...re': array(\[0.8631..., 0.97166667\]), 'me...re': array(\[0.8696..., 0.99297052\]), ...} |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 64  |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 30  |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 0.06181 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | \_Scorer | make\_scorer(a...hod='predict') |

best\_estimator\_: Pipeline

PCA

[?Documentation for PCA](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_components n\_components: int, float or 'mle', default=None  <br>  <br>Number of components to keep.  <br>if n\_components is not set all components are kept::  <br>  <br>n\_components == min(n\_samples, n\_features)  <br>  <br>If \`\`n\_components == 'mle'\`\` and \`\`svd\_solver == 'full'\`\`, Minka's  <br>MLE is used to guess the dimension. Use of \`\`n\_components == 'mle'\`\`  <br>will interpret \`\`svd\_solver == 'auto'\`\` as \`\`svd\_solver == 'full'\`\`.  <br>  <br>If \`\`0 < n\_components < 1\`\` and \`\`svd\_solver == 'full'\`\`, select the  <br>number of components such that the amount of variance that needs to be  <br>explained is greater than the percentage specified by n\_components.  <br>  <br>If \`\`svd\_solver == 'arpack'\`\`, the number of components must be  <br>strictly less than the minimum of n\_features and n\_samples.  <br>  <br>Hence, the None case results in::  <br>  <br>n\_components == min(n\_samples, n\_features) - 1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components,-int%2C%20float%20or%20%27mle%27%2C%20default%3DNone) | 25  |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Used when the 'arpack' or 'randomized' solvers are used. Pass an int  <br>for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |
|     | [copy copy: bool, default=True  <br>  <br>If False, data passed to fit are overwritten and running  <br>fit(X).transform(X) will not yield the expected results,  <br>use fit\_transform(X) instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [whiten whiten: bool, default=False  <br>  <br>When True (False by default) the \`components\_\` vectors are multiplied  <br>by the square root of n\_samples and then divided by the singular values  <br>to ensure uncorrelated outputs with unit component-wise variances.  <br>  <br>Whitening will remove some information from the transformed signal  <br>(the relative variance scales of the components) but can sometime  <br>improve the predictive accuracy of the downstream estimators by  <br>making their data respect some hard-wired assumptions.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=whiten,-bool%2C%20default%3DFalse) | False |
|     | [svd\_solver svd\_solver: {'auto', 'full', 'covariance\_eigh', 'arpack', 'randomized'}, default='auto'  <br>  <br>"auto" :  <br>The solver is selected by a default 'auto' policy is based on \`X.shape\` and  <br>\`n\_components\`: if the input data has fewer than 1000 features and  <br>more than 10 times as many samples, then the "covariance\_eigh"  <br>solver is used. Otherwise, if the input data is larger than 500x500  <br>and the number of components to extract is lower than 80% of the  <br>smallest dimension of the data, then the more efficient  <br>"randomized" method is selected. Otherwise the exact "full" SVD is  <br>computed and optionally truncated afterwards.  <br>"full" :  <br>Run exact full SVD calling the standard LAPACK solver via  <br>\`scipy.linalg.svd\` and select the components by postprocessing  <br>"covariance\_eigh" :  <br>Precompute the covariance matrix (on centered data), run a  <br>classical eigenvalue decomposition on the covariance matrix  <br>typically using LAPACK and select the components by postprocessing.  <br>This solver is very efficient for n\_samples >> n\_features and small  <br>n\_features. It is, however, not tractable otherwise for large  <br>n\_features (large memory footprint required to materialize the  <br>covariance matrix). Also note that compared to the "full" solver,  <br>this solver effectively doubles the condition number and is  <br>therefore less numerical stable (e.g. on input data with a large  <br>range of singular values).  <br>"arpack" :  <br>Run SVD truncated to \`n\_components\` calling ARPACK solver via  <br>\`scipy.sparse.linalg.svds\`. It requires strictly  <br>\`0 < n\_components < min(X.shape)\`  <br>"randomized" :  <br>Run randomized SVD by the method of Halko et al.  <br>  <br>.. versionadded:: 0.18.0  <br>  <br>.. versionchanged:: 1.5  <br>Added the 'covariance\_eigh' solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=svd_solver,-%7B%27auto%27%2C%20%27full%27%2C%20%27covariance_eigh%27%2C%20%27arpack%27%2C%20%27randomized%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27auto%27) | 'auto' |
|     | [tol tol: float, default=0.0  <br>  <br>Tolerance for singular values computed by svd\_solver == 'arpack'.  <br>Must be of range \[0.0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=tol,-float%2C%20default%3D0.0) | 0.0 |\
|     | [iterated\_power iterated\_power: int or 'auto', default='auto'  <br>  <br>Number of iterations for the power method computed by  <br>svd\_solver == 'randomized'.  <br>Must be of range \[0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=iterated_power,-int%20or%20%27auto%27%2C%20default%3D%27auto%27) | 'auto' |\
|     | [n\_oversamples n\_oversamples: int, default=10  <br>  <br>This parameter is only relevant when \`svd\_solver="randomized"\`.  <br>It corresponds to the additional number of random vectors to sample the  <br>range of \`X\` so as to ensure proper conditioning. See  <br>:func:\`~sklearn.utils.extmath.randomized\_svd\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_oversamples,-int%2C%20default%3D10) | 10  |\
|     | [power\_iteration\_normalizer power\_iteration\_normalizer: {'auto', 'QR', 'LU', 'none'}, default='auto'  <br>  <br>Power iteration normalizer for randomized SVD solver.  <br>Not used by ARPACK. See :func:\`~sklearn.utils.extmath.randomized\_svd\`  <br>for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=power_iteration_normalizer,-%7B%27auto%27%2C%20%27QR%27%2C%20%27LU%27%2C%20%27none%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Principal axes in feature space, representing the directions of  <br>maximum variance in the data. Equivalently, the right singular  <br>vectors of the centered input data, parallel to its eigenvectors.  <br>The components are sorted by decreasing \`\`explained\_variance\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float64\](25, 64) | \[\[ 0. ,-0.02,-0.22,...,-0.09,-0.04,-0.01\], \[ 0. , 0.01, 0.05,...,-0.18,-0.02, 0.01\], \[ 0. ,-0.02,-0.13,...,-0.23,-0.17,-0.03\], ..., \[-0. , 0.03, 0.09,...,-0.02,-0.12,-0.05\], \[-0. ,-0.05,-0.07,..., 0.02, 0.01, 0.03\], \[-0. ,-0.02,-0.04,..., 0.12, 0.12, 0.09\]\] |\
| [explained\_variance\_ explained\_variance\_: ndarray of shape (n\_components,)  <br>  <br>The amount of variance explained by each of the selected components.  <br>The variance estimation uses \`n\_samples - 1\` degrees of freedom.  <br>  <br>Equal to n\_components largest eigenvalues  <br>of the covariance matrix of X.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=explained_variance_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](25,) | \[179.01,163.72,141.79,..., 9.23, 8.69, 8.37\] |\
| [explained\_variance\_ratio\_ explained\_variance\_ratio\_: ndarray of shape (n\_components,)  <br>  <br>Percentage of variance explained by each of the selected components.  <br>  <br>If \`\`n\_components\`\` is not set then all components are stored and the  <br>sum of the ratios is equal to 1.0.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=explained_variance_ratio_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](25,) | \[0.15,0.14,0.12,...,0.01,0.01,0.01\] |\
| [mean\_ mean\_: ndarray of shape (n\_features,)  <br>  <br>Per-feature empirical mean, estimated from the training set.  <br>  <br>Equal to \`X.mean(axis=0)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[0. ,0.3 ,5.2 ,...,6.76,2.07,0.36\] |\
| [n\_components\_ n\_components\_: int  <br>  <br>The estimated number of components. When n\_components is set  <br>to 'mle' or a number between 0 and 1 (with svd\_solver == 'full') this  <br>number is estimated from input data. Otherwise it equals the parameter  <br>n\_components, or the lesser value of n\_features and n\_samples  <br>if n\_components is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components_,-int) | int | 25  |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_features_in_,-int) | int | 64  |\
| [n\_samples\_ n\_samples\_: int  <br>  <br>Number of samples in the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_samples_,-int) | int | 1797 |\
| [noise\_variance\_ noise\_variance\_: float  <br>  <br>The estimated noise covariance following the Probabilistic PCA model  <br>from Tipping and Bishop 1999. See "Pattern Recognition and  <br>Machine Learning" by C. Bishop, 12.2.1 p. 574 or  <br>http://www.miketipping.com/papers/met-mppca.pdf. It is required to  <br>compute the estimated data covariance and score samples.  <br>  <br>Equal to the average of (min(n\_features, n\_samples) - n\_components)  <br>smallest eigenvalues of the covariance matrix of X.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=noise_variance_,-float) | float64 | 2.064 |\
| [singular\_values\_ singular\_values\_: ndarray of shape (n\_components,)  <br>  <br>The singular values corresponding to each of the selected components.  <br>The singular values are equal to the 2-norms of the \`\`n\_components\`\`  <br>variables in the lower-dimensional space.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=singular_values_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](25,) | \[567.01,542.25,504.63,...,128.73,124.93,122.58\] |\
\
25 features\
\
|     |\
| --- |\
| pca0 |\
| pca1 |\
| pca2 |\
| pca3 |\
| pca4 |\
| pca5 |\
| pca6 |\
| pca7 |\
| pca8 |\
| pca9 |\
| pca10 |\
| pca11 |\
| pca12 |\
| pca13 |\
| pca14 |\
| pca15 |\
| pca16 |\
| pca17 |\
| pca18 |\
| pca19 |\
| pca20 |\
| pca21 |\
| pca22 |\
| pca23 |\
| pca24 |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 0.01 |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | 42  |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 1000 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](10,) | \[0,1,2,...,7,8,9\] |\
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](10, 25) | \[\[ 0.08,-0.26, 0.06,...,-0.01,-0.03, 0.01\], \[ 0.09, 0.17,-0.05,...,-0.02,-0.08, 0.17\], \[-0.16, 0.08,-0.22,...,-0.01, 0.01, 0. \], ..., \[ 0.02, 0.15, 0.18,...,-0.03,-0.01,-0.06\], \[ 0.01, 0.02,-0.04,...,-0.01, 0.02,-0. \], \[-0.25,-0.03, 0.15,...,-0.01,-0.09, 0. \]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](10,) | \[-0.69,-0.07,-0.59,...,-0.14, 2.16,-0.35\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 25  |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[93\] |\
\
  \
  \
\
Visualize the results[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#visualize-the-results "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We’ll create a bar chart showing the test scores for different numbers of PCA components, along with horizontal lines indicating the best score and the one-standard-deviation threshold.\
\
n\_components \= grid.cv\_results\_\["param\_reduce\_dim\_\_n\_components"\]\
test\_scores \= grid.cv\_results\_\["mean\_test\_score"\]\
\
\# Create a polars DataFrame for better data manipulation and visualization\
results\_df \= pl.DataFrame(\
    {\
        "n\_components": n\_components,\
        "mean\_test\_score": test\_scores,\
        "std\_test\_score": grid.cv\_results\_\["std\_test\_score"\],\
        "mean\_train\_score": grid.cv\_results\_\["mean\_train\_score"\],\
        "std\_train\_score": grid.cv\_results\_\["std\_train\_score"\],\
        "mean\_fit\_time": grid.cv\_results\_\["mean\_fit\_time"\],\
        "rank\_test\_score": grid.cv\_results\_\["rank\_test\_score"\],\
    }\
)\
\
\# Sort by number of components\
results\_df \= results\_df.sort("n\_components")\
\
\# Calculate the lower bound threshold\
lower \= lower\_bound(grid.cv\_results\_)\
\
\# Get the best model information\
best\_index\_ \= grid.best\_index\_\
best\_components \= n\_components\[best\_index\_\]\
best\_score \= grid.cv\_results\_\["mean\_test\_score"\]\[best\_index\_\]\
\
\# Add a column to mark the selected model\
results\_df \= results\_df.with\_columns(\
    pl.when(pl.col("n\_components") \== best\_components)\
    .then(pl.lit("Selected"))\
    .otherwise(pl.lit("Regular"))\
    .alias("model\_type")\
)\
\
\# Get the number of CV splits from the results\
n\_splits \= sum(\
    1\
    for key in grid.cv\_results\_.keys()\
    if key.startswith("split") and key.endswith("test\_score")\
)\
\
\# Extract individual scores for each split\
test\_scores \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\
    \[\
        \[grid.cv\_results\_\[f"split{i}\_test\_score"\]\[j\] for i in range(n\_splits)\]\
        for j in range(len(n\_components))\
    \]\
)\
train\_scores \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\
    \[\
        \[grid.cv\_results\_\[f"split{i}\_train\_score"\]\[j\] for i in range(n\_splits)\]\
        for j in range(len(n\_components))\
    \]\
)\
\
\# Calculate mean and std of test scores\
mean\_test\_scores \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(test\_scores, axis\=1)\
std\_test\_scores \= [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")\
(test\_scores, axis\=1)\
\
\# Find best score and threshold\
best\_mean\_score \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")\
(mean\_test\_scores)\
threshold \= best\_mean\_score \- std\_test\_scores\[[np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")\
(mean\_test\_scores)\]\
\
\# Create a single figure for visualization\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(12, 8))\
\
\# Plot individual points\
for i, comp in enumerate(n\_components):\
    \# Plot individual test points\
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")\
(\
        \[comp\] \* n\_splits,\
        test\_scores\[i\],\
        alpha\=0.2,\
        color\="blue",\
        s\=20,\
        label\="Individual test scores" if i \== 0 else "",\
    )\
    \# Plot individual train points\
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")\
(\
        \[comp\] \* n\_splits,\
        train\_scores\[i\],\
        alpha\=0.2,\
        color\="green",\
        s\=20,\
        label\="Individual train scores" if i \== 0 else "",\
    )\
\
\# Plot mean lines with error bands\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\
    n\_components,\
    [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(test\_scores, axis\=1),\
    "-",\
    color\="blue",\
    linewidth\=2,\
    label\="Mean test score",\
)\
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")\
(\
    n\_components,\
    [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(test\_scores, axis\=1) \- [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")\
(test\_scores, axis\=1),\
    [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(test\_scores, axis\=1) + [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")\
(test\_scores, axis\=1),\
    alpha\=0.15,\
    color\="blue",\
)\
\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
(\
    n\_components,\
    [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(train\_scores, axis\=1),\
    "-",\
    color\="green",\
    linewidth\=2,\
    label\="Mean train score",\
)\
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")\
(\
    n\_components,\
    [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(train\_scores, axis\=1) \- [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")\
(train\_scores, axis\=1),\
    [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")\
(train\_scores, axis\=1) + [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")\
(train\_scores, axis\=1),\
    alpha\=0.15,\
    color\="green",\
)\
\
\# Add threshold lines\
[plt.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline")\
(\
    best\_mean\_score,\
    color\="#9b59b6",  \# Purple\
    linestyle\="--",\
    label\="Best score",\
    linewidth\=2,\
)\
[plt.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline")\
(\
    threshold,\
    color\="#e67e22",  \# Orange\
    linestyle\="--",\
    label\="Best score - 1 std",\
    linewidth\=2,\
)\
\
\# Highlight selected model\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(\
    best\_components,\
    color\="#9b59b6",  \# Purple\
    alpha\=0.2,\
    linewidth\=8,\
    label\="Selected model",\
)\
\
\# Set titles and labels\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Number of PCA components", fontsize\=12)\
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")\
("Score", fontsize\=12)\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Model Selection: Balancing Complexity and Performance", fontsize\=14)\
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")\
(True, linestyle\="--", alpha\=0.7)\
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")\
(\
    bbox\_to\_anchor\=(1.02, 1),\
    loc\="upper left",\
    borderaxespad\=0,\
)\
\
\# Set axis properties\
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")\
(n\_components)\
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")\
((0.85, 1.0))\
\
\# # Adjust layout\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![Model Selection: Balancing Complexity and Performance](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_001.png)\
\
Print the results[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#print-the-results "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We print information about the selected model, including its complexity and performance. We also show a summary table of all models using polars.\
\
print("Best model selected by the one-standard-error rule:")\
print(f"Number of PCA components: {best\_components}")\
print(f"Accuracy score: {best\_score:.4f}")\
print(f"Best possible accuracy: {[np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")\
(test\_scores):.4f}")\
print(f"Accuracy threshold (best - 1 std): {lower:.4f}")\
\
\# Create a summary table with polars\
summary\_df \= results\_df.select(\
    pl.col("n\_components"),\
    pl.col("mean\_test\_score").round(4).alias("test\_score"),\
    pl.col("std\_test\_score").round(4).alias("test\_std"),\
    pl.col("mean\_train\_score").round(4).alias("train\_score"),\
    pl.col("std\_train\_score").round(4).alias("train\_std"),\
    pl.col("mean\_fit\_time").round(3).alias("fit\_time"),\
    pl.col("rank\_test\_score").alias("rank"),\
)\
\
\# Add a column to mark the selected model\
summary\_df \= summary\_df.with\_columns(\
    pl.when(pl.col("n\_components") \== best\_components)\
    .then(pl.lit("\*"))\
    .otherwise(pl.lit(""))\
    .alias("selected")\
)\
\
print("\\nModel comparison table:")\
print(summary\_df)\
\
Copy to clipboard\
\
Best model selected by the one-standard-error rule:\
Number of PCA components: 25\
Accuracy score: 0.9643\
Best possible accuracy: 0.9944\
Accuracy threshold (best - 1 std): 0.9623\
\
Model comparison table:\
shape: (9, 8)\
┌──────────────┬────────────┬──────────┬─────────────┬───────────┬──────────┬──────┬──────────┐\
│ n\_components ┆ test\_score ┆ test\_std ┆ train\_score ┆ train\_std ┆ fit\_time ┆ rank ┆ selected │\
│ ---          ┆ ---        ┆ ---      ┆ ---         ┆ ---       ┆ ---      ┆ ---  ┆ ---      │\
│ i64          ┆ f64        ┆ f64      ┆ f64         ┆ f64       ┆ f64      ┆ i32  ┆ str      │\
╞══════════════╪════════════╪══════════╪═════════════╪═══════════╪══════════╪══════╪══════════╡\
│ 6            ┆ 0.8631     ┆ 0.0241   ┆ 0.8697      ┆ 0.0047    ┆ 0.111    ┆ 9    ┆          │\
│ 8            ┆ 0.9037     ┆ 0.0194   ┆ 0.9147      ┆ 0.0028    ┆ 0.104    ┆ 8    ┆          │\
│ 10           ┆ 0.9341     ┆ 0.0148   ┆ 0.9493      ┆ 0.0023    ┆ 0.071    ┆ 7    ┆          │\
│ 15           ┆ 0.95       ┆ 0.0162   ┆ 0.9662      ┆ 0.0022    ┆ 0.067    ┆ 6    ┆          │\
│ 20           ┆ 0.9563     ┆ 0.0144   ┆ 0.9759      ┆ 0.0019    ┆ 0.064    ┆ 5    ┆          │\
│ 25           ┆ 0.9643     ┆ 0.0126   ┆ 0.9836      ┆ 0.0014    ┆ 0.059    ┆ 4    ┆ \*        │\
│ 35           ┆ 0.9685     ┆ 0.0115   ┆ 0.9903      ┆ 0.0013    ┆ 0.061    ┆ 3    ┆          │\
│ 45           ┆ 0.9711     ┆ 0.0093   ┆ 0.9926      ┆ 0.001     ┆ 0.063    ┆ 2    ┆          │\
│ 55           ┆ 0.9717     ┆ 0.0093   ┆ 0.993       ┆ 0.001     ┆ 0.065    ┆ 1    ┆          │\
└──────────────┴────────────┴──────────┴─────────────┴───────────┴──────────┴──────┴──────────┘\
\
Copy to clipboard\
\
Conclusion[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#conclusion "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------\
\
The one-standard-error rule helps us select a simpler model (fewer PCA components) while maintaining performance statistically comparable to the best model. This approach can help prevent overfitting and improve model interpretability and efficiency.\
\
In this example, we’ve seen how to implement this rule using a custom refit callable with [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
.\
\
Key takeaways:\
\
1.  The one-standard-error rule provides a good rule of thumb to select simpler models\
    \
2.  Custom refit callables in [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
     allow for flexible model selection strategies\
    \
3.  Visualizing both train and test scores helps identify potential overfitting\
    \
\
This approach can be applied to other model selection scenarios where balancing complexity and performance is important, or in cases where a use-case specific selection of the “best” model is desired.\
\
\# Display the figure\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
**Total running time of the script:** (0 minutes 21.385 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_refit_callable.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_refit_callable.ipynb)\
\
[`Download Jupyter notebook: plot_grid_search_refit_callable.ipynb`](https://scikit-learn.org/stable/_downloads/af8345a01f32fc7a8b3c9693bb4aca30/plot_grid_search_refit_callable.ipynb)\
\
[`Download Python source code: plot_grid_search_refit_callable.py`](https://scikit-learn.org/stable/_downloads/02d88d76c60b7397c8c6e221b31568dd/plot_grid_search_refit_callable.py)\
\
[`Download zipped: plot_grid_search_refit_callable.zip`](https://scikit-learn.org/stable/_downloads/a88ca03d46b8289eaed2fc08e505bee2/plot_grid_search_refit_callable.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)\
\
[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)\
\
Pipelining: chaining a PCA and a logistic regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)\
\
[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)\
\
Custom refit strategy of a grid search with cross-validation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)\
\
[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)\
\
Lagged features for time series forecasting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)\
\
[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)\
\
Recursive feature elimination with cross-validation\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/02d88d76c60b7397c8c6e221b31568dd/plot_grid_search_refit_callable.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/af8345a01f32fc7a8b3c9693bb4aca30/plot_grid_search_refit_callable.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/a88ca03d46b8289eaed2fc08e505bee2/plot_grid_search_refit_callable.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_refit_callable.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_refit_callable.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)