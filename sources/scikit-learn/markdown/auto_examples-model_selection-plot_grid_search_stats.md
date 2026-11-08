[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_grid_search_stats.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_grid_search_stats.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_grid_search_stats.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_grid_search_stats.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_grid_search_stats.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_grid_search_stats.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#sphx-glr-download-auto-examples-model-selection-plot-grid-search-stats-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Statistical comparison of models using grid search[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#statistical-comparison-of-models-using-grid-search "Link to this heading")

===========================================================================================================================================================================================================================

This example illustrates how to statistically compare the performance of models trained and evaluated using [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

We will start by simulating moon shaped data (where the ideal separation between classes is non-linear), adding to it a moderate degree of noise. Datapoints will belong to one of two possible classes to be predicted by two features. We will simulate 50 samples for each class:

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")

X, y \= [make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
(noise\=0.352, random\_state\=1, n\_samples\=100)

[sns.scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
(
    x\=X\[:, 0\], y\=X\[:, 1\], hue\=y, marker\="o", s\=25, edgecolor\="k", legend\=False
).set\_title("Data")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Data](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_001.png)

We will compare the performance of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 estimators that vary on their `kernel` parameter, to decide which choice of this hyper-parameter predicts our simulated data best. We will evaluate the performance of the models using [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
, repeating 10 times a 10-fold stratified cross validation using a different randomization of the data in each repetition. The performance will be evaluated using [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
.

from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [RepeatedStratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

param\_grid \= \[\
    {"kernel": \["linear"\]},\
    {"kernel": \["poly"\], "degree": \[2, 3\]},\
    {"kernel": \["rbf"\]},\
\]

svc \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(random\_state\=0)

cv \= [RepeatedStratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
(n\_splits\=10, n\_repeats\=10, random\_state\=0)

search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(estimator\=svc, param\_grid\=param\_grid, scoring\="roc\_auc", cv\=cv)
search.fit(X, y)

Copy to clipboard

GridSearchCV(cv=RepeatedStratifiedKFold(n\_repeats=10, n\_splits=10, random\_state=0),
             estimator=SVC(random\_state=0),
             param\_grid=\[{'kernel': \['linear'\]},\
                         {'degree': \[2, 3\], 'kernel': \['poly'\]},\
                         {'kernel': \['rbf'\]}\],
             scoring='roc\_auc')

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | SVC(random\_state=0) |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | \[{'kernel': \['linear'\]}, {'degree': \[2, 3\], 'kernel': \['poly'\]}, ...\] |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | 'roc\_auc' |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | RepeatedStrat...andom\_state=0) |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | SVC | SVC(random\_state=0) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(3) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'kernel': 'rbf'} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the best\_estimator  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.  <br>  <br>This attribute is not available if \`\`refit\`\` is a function.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_score_,-float) | float64 | 0.94 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0., 0., 0., 0.\]), 'me...me': array(\[0., 0., 0., 0.\]), 'me...re': array(\[0.93, ..., 0.9 , 0.94\]), 'pa...ee': masked\_array(...\_value=999999), ...} |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 100 |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 0.001296 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | \_Scorer | make\_scorer(r...edict\_proba')) |

best\_estimator\_: SVC

SVC(random\_state=0)

SVC

[?Documentation for SVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>probability estimates. Ignored when \`probability\` is False.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive. The penalty  <br>is a squared l2 penalty. For an intuitive visualization of the effects  <br>of scaling the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |
|     | [kernel kernel: {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'} or callable, default='rbf'  <br>  <br>Specifies the kernel type to be used in the algorithm. If  <br>none is given, 'rbf' will be used. If a callable is given it is used to  <br>pre-compute the kernel matrix from data matrices; that matrix should be  <br>an array of shape \`\`(n\_samples, n\_samples)\`\`. For an intuitive  <br>visualization of different kernel types see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_kernels.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=kernel,-%7B%27linear%27%2C%20%27poly%27%2C%20%27rbf%27%2C%20%27sigmoid%27%2C%20%27precomputed%27%7D%20or%20callable%2C%20%20%20%20%20%20%20%20%20%20default%3D%27rbf%27) | 'rbf' |
|     | [degree degree: int, default=3  <br>  <br>Degree of the polynomial kernel function ('poly').  <br>Must be non-negative. Ignored by all other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=degree,-int%2C%20default%3D3) | 3   |
|     | [gamma gamma: {'scale', 'auto'} or float, default='scale'  <br>  <br>Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.  <br>  <br>\- if \`\`gamma='scale'\`\` (default) is passed then it uses  <br>1 / (n\_features \* X.var()) as value of gamma,  <br>\- if 'auto', uses 1 / n\_features  <br>\- if float, must be non-negative.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`gamma\`\` changed from 'auto' to 'scale'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=gamma,-%7B%27scale%27%2C%20%27auto%27%7D%20or%20float%2C%20default%3D%27scale%27) | 'scale' |
|     | [coef0 coef0: float, default=0.0  <br>  <br>Independent term in kernel function.  <br>It is only significant in 'poly' and 'sigmoid'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=coef0,-float%2C%20default%3D0.0) | 0.0 |
|     | [shrinking shrinking: bool, default=True  <br>  <br>Whether to use the shrinking heuristic.  <br>See the :ref:\`User Guide <shrinking\_svm>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=shrinking,-bool%2C%20default%3DTrue) | True |
|     | [probability probability: bool, default=False  <br>  <br>Whether to enable probability estimates. This must be enabled prior  <br>to calling \`fit\`, will slow down that method as it internally uses  <br>5-fold cross-validation, and \`predict\_proba\` may be inconsistent with  <br>\`predict\`. Read more in the :ref:\`User Guide <scores\_probabilities>\`.  <br>  <br>..deprecated:: 1.9  <br>The \`probability\` parameter is deprecated and will be removed in 1.11.  <br>Use \`CalibratedClassifierCV(SVC(), ensemble=False)\` instead of  <br>\`SVC(probability=True)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probability,-bool%2C%20default%3DFalse) | 'deprecated' |
|     | [tol tol: float, default=1e-3  <br>  <br>Tolerance for stopping criterion.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=tol,-float%2C%20default%3D1e-3) | 0.001 |
|     | [cache\_size cache\_size: float, default=200  <br>  <br>Specify the size of the kernel cache (in MB).](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=cache_size,-float%2C%20default%3D200) | 200 |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Set the parameter C of class i to class\_weight\[i\]\*C for  <br>SVC. If not given, all classes are supposed to have  <br>weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>Enable verbose output. Note that this setting takes advantage of a  <br>per-process runtime setting in libsvm that, if enabled, may not work  <br>properly in a multithreaded context.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |
|     | [max\_iter max\_iter: int, default=-1  <br>  <br>Hard limit on iterations within solver, or -1 for no limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=max_iter,-int%2C%20default%3D-1) | \-1 |
|     | [decision\_function\_shape decision\_function\_shape: {'ovo', 'ovr'}, default='ovr'  <br>  <br>Whether to return a one-vs-rest ('ovr') decision function of shape  <br>(n\_samples, n\_classes) as all other classifiers, or the original  <br>one-vs-one ('ovo') decision function of libsvm which has shape  <br>(n\_samples, n\_classes \* (n\_classes - 1) / 2). However, note that  <br>internally, one-vs-one ('ovo') is always used as a multi-class strategy  <br>to train models; an ovr matrix is only constructed from the ovo matrix.  <br>The parameter is ignored for binary classification.  <br>  <br>.. versionchanged:: 0.19  <br>decision\_function\_shape is 'ovr' by default.  <br>  <br>.. versionadded:: 0.17  <br>\*decision\_function\_shape='ovr'\* is recommended.  <br>  <br>.. versionchanged:: 0.17  <br>Deprecated \*decision\_function\_shape='ovo' and None\*.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=decision_function_shape,-%7B%27ovo%27%2C%20%27ovr%27%7D%2C%20default%3D%27ovr%27) | 'ovr' |
|     | [break\_ties break\_ties: bool, default=False  <br>  <br>If true, \`\`decision\_function\_shape='ovr'\`\`, and number of classes > 2,  <br>:term:\`predict\` will break ties according to the confidence values of  <br>:term:\`decision\_function\`; otherwise the first class among the tied  <br>classes is returned. Please note that breaking ties comes at a  <br>relatively high computational cost compared to a simple predict. See  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_tie\_breaking.py\` for an  <br>example of its usage with \`\`decision\_function\_shape='ovr'\`\`.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=break_ties,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [class\_weight\_ class\_weight\_: ndarray of shape (n\_classes,)  <br>  <br>Multipliers of parameter C for each class.  <br>Computed based on the \`\`class\_weight\`\` parameter.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=class_weight_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[float64\](2,) | \[1.,1.\] |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [dual\_coef\_ dual\_coef\_: ndarray or sparse array/matrix of shape (n\_classes -1, n\_SV)  <br>  <br>Dual coefficients of the support vector in the decision  <br>function (see :ref:\`sgd\_mathematical\_formulation\`), multiplied by  <br>their targets.  <br>For multiclass, coefficient for all 1-vs-1 classifiers.  <br>The layout of the coefficients in the multiclass case is somewhat  <br>non-trivial. See the :ref:\`multi-class section of the User Guide  <br><svm\_multi\_class>\` for details.  <br>If \`X\` is sparse, these will also be sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=dual_coef_,-ndarray%20or%20sparse%20array/matrix%20of%20shape%20%28n_classes%20-1%2C%20n_SV%29) | ndarray\[float64\](1, 48) | \[\[-1. ,-0.09,-1. ,..., 1. , 1. , 0.19\]\] |
| [fit\_status\_ fit\_status\_: int  <br>  <br>0 if correctly fitted, 1 otherwise (will raise warning)](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=fit_status_,-int) | int | 0   |
| [intercept\_ intercept\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2,)  <br>  <br>Constants in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=intercept_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%2C%29) | ndarray\[float64\](1,) | \[0.01\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_iter\_ n\_iter\_: ndarray of shape (n\_classes \* (n\_classes - 1) // 2,)  <br>  <br>Number of iterations run by the optimization routine to fit the model.  <br>The shape of this attribute depends on the number of models optimized  <br>which in turn depends on the number of classes.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_iter_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20//%202%2C%29) | ndarray\[int32\](1,) | \[47\] |
| [n\_support\_ n\_support\_: ndarray of shape (n\_classes,), dtype=int32  <br>  <br>Number of support vectors for each class.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_support_,-ndarray%20of%20shape%20%28n_classes%2C%29%2C%20dtype%3Dint32) | ndarray\[int32\](2,) | \[24,24\] |
| [probA\_ probA\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2)  <br>  <br>If \`probability=True\`, it corresponds to the parameters learned in  <br>Platt scaling to produce probability estimates from decision values.  <br>If \`probability=False\`, it's an empty array. Platt scaling uses the  <br>logistic function](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probA_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%29) | ndarray\[float64\](0,) | \[\] |
| [probB\_ probB\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2)  <br>  <br>If \`probability=True\`, it corresponds to the parameters learned in  <br>Platt scaling. Platt scaling uses the logistic function  <br>\`\`1 / (1 + exp(decision\_value \* probA\_ + probB\_))\`\`  <br>where \`\`probA\_\`\` and \`\`probB\_\`\` are learned from the dataset \[2\]\_. For  <br>more information on the multiclass case and training procedure see  <br>section 8 of \[1\]\_.  <br>  <br>.. deprecated:: 1.9  <br>The attributes \`probA\_\` and \`probB\_\` are deprecated in version 1.9 and will  <br>be removed in 1.11.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probB_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%29) | ndarray\[float64\](0,) | \[\] |
| [shape\_fit\_ shape\_fit\_: tuple of int of shape (n\_dimensions\_of\_X,)  <br>  <br>Array dimensions of training vector \`\`X\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=shape_fit_,-tuple%20of%20int%20of%20shape%20%28n_dimensions_of_X%2C%29) | tuple | (100, 2) |
| [support\_ support\_: ndarray of shape (n\_SV)  <br>  <br>Indices of support vectors.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=support_,-ndarray%20of%20shape%20%28n_SV%29) | ndarray\[int32\](48,) | \[ 2, 6,20,...,89,93,97\] |
| [support\_vectors\_ support\_vectors\_: ndarray or sparse array/matrix of shape (n\_SV, n\_features)  <br>  <br>Support vectors. An empty array if kernel is precomputed.  <br>If \`X\` is sparse, these will also be sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=support_vectors_,-ndarray%20or%20sparse%20array/matrix%20of%20shape%20%28n_SV%2C%20n_features%29) | ndarray\[float64\](48, 2) | \[\[-0.27, 0.07\], \[-1.14, 1.21\], \[ 0.45, 0.06\], ..., \[ 1.36,-0.15\], \[ 1.26,-0.14\], \[ 0.52,-1.45\]\] |

  
  

We can now inspect the results of our search, sorted by their `mean_test_score`:

import pandas as pd

results\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(search.cv\_results\_)
results\_df \= results\_df.sort\_values(by\=\["rank\_test\_score"\])
results\_df \= results\_df.set\_index(
    results\_df\["params"\].apply(lambda x: "\_".join(str(val) for val in x.values()))
).rename\_axis("kernel")
results\_df\[\["params", "rank\_test\_score", "mean\_test\_score", "std\_test\_score"\]\]

Copy to clipboard

|     | params | rank\_test\_score | mean\_test\_score | std\_test\_score |
| --- | --- | --- | --- | --- |
| kernel |     |     |     |     |
| --- | --- | --- | --- | --- |
| rbf | {'kernel': 'rbf'} | 1   | 0.9400 | 0.079297 |
| linear | {'kernel': 'linear'} | 2   | 0.9300 | 0.077846 |
| 3\_poly | {'degree': 3, 'kernel': 'poly'} | 3   | 0.9044 | 0.098776 |
| 2\_poly | {'degree': 2, 'kernel': 'poly'} | 4   | 0.6852 | 0.169106 |

  
  

We can see that the estimator using the `'rbf'` kernel performed best, closely followed by `'linear'`. Both estimators with a `'poly'` kernel performed worse, with the one using a two-degree polynomial achieving a much lower performance than all other models.

Usually, the analysis just ends here, but half the story is missing. The output of [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 does not provide information on the certainty of the differences between the models. We don’t know if these are **statistically** significant. To evaluate this, we need to conduct a statistical test. Specifically, to contrast the performance of two models we should statistically compare their AUC scores. There are 100 samples (AUC scores) for each model as we repreated 10 times a 10-fold cross-validation.

However, the scores of the models are not independent: all models are evaluated on the **same** 100 partitions, increasing the correlation between the performance of the models. Since some partitions of the data can make the distinction of the classes particularly easy or hard to find for all models, the models scores will co-vary.

Let’s inspect this partition effect by plotting the performance of all models in each fold, and calculating the correlation between models across folds:

\# create df of model scores ordered by performance
model\_scores \= results\_df.filter(regex\=r"split\\d\*\_test\_score")

\# plot 30 examples of dependency between cv fold and AUC scores
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[sns.lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")
(
    data\=model\_scores.transpose().iloc\[:30\],
    dashes\=False,
    palette\="Set1",
    marker\="o",
    alpha\=0.5,
    ax\=ax,
)
ax.set\_xlabel("CV test fold", size\=12, labelpad\=10)
ax.set\_ylabel("Model AUC", size\=12)
ax.tick\_params(bottom\=True, labelbottom\=False)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

\# print correlation of AUC scores across folds
print(f"Correlation of models:\\n {model\_scores.transpose().corr()}")

Copy to clipboard

![plot grid search stats](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_002.png)

Correlation of models:
 kernel       rbf    linear    3\_poly    2\_poly
kernel
rbf     1.000000  0.882561  0.783392  0.351390
linear  0.882561  1.000000  0.746492  0.298688
3\_poly  0.783392  0.746492  1.000000  0.355440
2\_poly  0.351390  0.298688  0.355440  1.000000

Copy to clipboard

We can observe that the performance of the models highly depends on the fold.

As a consequence, if we assume independence between samples we will be underestimating the variance computed in our statistical tests, increasing the number of false positive errors (i.e. detecting a significant difference between models when such does not exist) [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id10)
.

Several variance-corrected statistical tests have been developed for these cases. In this example we will show how to implement one of them (the so called Nadeau and Bengio’s corrected t-test) under two different statistical frameworks: frequentist and Bayesian.

Comparing two models: frequentist approach[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#comparing-two-models-frequentist-approach "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can start by asking: “Is the first model significantly better than the second model (when ranked by `mean_test_score`)?”

To answer this question using a frequentist approach we could run a paired t-test and compute the p-value. This is also known as Diebold-Mariano test in the forecast literature [\[5\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id14)
. Many variants of such a t-test have been developed to account for the ‘non-independence of samples problem’ described in the previous section. We will use the one proven to obtain the highest replicability scores (which rate how similar the performance of a model is when evaluating it on different random partitions of the same dataset) while maintaining a low rate of false positives and false negatives: the Nadeau and Bengio’s corrected t-test [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id11)
 that uses a 10 times repeated 10-fold cross validation [\[3\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id12)
.

This corrected paired t-test is computed as:

t\=1k⋅r∑i\=1k∑j\=1rxij(1k⋅r+ntestntrain)σ^2

where k is the number of folds, r the number of repetitions in the cross-validation, x is the difference in performance of the models, ntest is the number of samples used for testing, ntrain is the number of samples used for training, and σ^2 represents the variance of the observed differences.

Let’s implement a corrected right-tailed paired t-test to evaluate if the performance of the first model is significantly better than that of the second model. Our null hypothesis is that the second model performs at least as good as the first model.

import numpy as np
from scipy.stats import [t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t "scipy.stats.t")

def corrected\_std(differences, n\_train, n\_test):
    """Corrects standard deviation using Nadeau and Bengio's approach.

    Parameters
    ----------
    differences : ndarray of shape (n\_samples,)
        Vector containing the differences in the score metrics of two models.
    n\_train : int
        Number of samples in the training set.
    n\_test : int
        Number of samples in the testing set.

    Returns
    -------
    corrected\_std : float
        Variance-corrected standard deviation of the set of differences.
    """
    \# kr = k times r, r times repeated k-fold crossvalidation,
    \# kr equals the number of times the model was evaluated
    kr \= len(differences)
    corrected\_var \= [np.var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
(differences, ddof\=1) \* (1 / kr + n\_test / n\_train)
    corrected\_std \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(corrected\_var)
    return corrected\_std

def compute\_corrected\_ttest(differences, df, n\_train, n\_test):
    """Computes right-tailed paired t-test with corrected variance.

    Parameters
    ----------
    differences : array-like of shape (n\_samples,)
        Vector containing the differences in the score metrics of two models.
    df : int
        Degrees of freedom.
    n\_train : int
        Number of samples in the training set.
    n\_test : int
        Number of samples in the testing set.

    Returns
    -------
    t\_stat : float
        Variance-corrected t-statistic.
    p\_val : float
        Variance-corrected p-value.
    """
    mean \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(differences)
    std \= corrected\_std(differences, n\_train, n\_test)
    t\_stat \= mean / std
    p\_val \= [t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t "scipy.stats.t")
.sf(np.abs(t\_stat), df)  \# right-tailed t-test
    return t\_stat, p\_val

Copy to clipboard

model\_1\_scores \= model\_scores.iloc\[0\].values  \# scores of the best model
model\_2\_scores \= model\_scores.iloc\[1\].values  \# scores of the second-best model

differences \= model\_1\_scores \- model\_2\_scores

n \= differences.shape\[0\]  \# number of test sets
df \= n \- 1
n\_train \= len(next(iter(cv.split(X, y)))\[0\])
n\_test \= len(next(iter(cv.split(X, y)))\[1\])

t\_stat, p\_val \= compute\_corrected\_ttest(differences, df, n\_train, n\_test)
print(f"Corrected t-value: {t\_stat:.3f}\\nCorrected p-value: {p\_val:.3f}")

Copy to clipboard

Corrected t-value: 0.750
Corrected p-value: 0.227

Copy to clipboard

We can compare the corrected t- and p-values with the uncorrected ones:

t\_stat\_uncorrected \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(differences) / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
([np.var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
(differences, ddof\=1) / n)
p\_val\_uncorrected \= [t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t "scipy.stats.t")
.sf(np.abs(t\_stat\_uncorrected), df)

print(
    f"Uncorrected t-value: {t\_stat\_uncorrected:.3f}\\n"
    f"Uncorrected p-value: {p\_val\_uncorrected:.3f}"
)

Copy to clipboard

Uncorrected t-value: 2.611
Uncorrected p-value: 0.005

Copy to clipboard

Using the conventional significance alpha level at `p=0.05`, we observe that the uncorrected t-test concludes that the first model is significantly better than the second.

With the corrected approach, in contrast, we fail to detect this difference.

In the latter case, however, the frequentist approach does not let us conclude that the first and second model have an equivalent performance. If we wanted to make this assertion we need to use a Bayesian approach.

Comparing two models: Bayesian approach[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#comparing-two-models-bayesian-approach "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can use Bayesian estimation to calculate the probability that the first model is better than the second. Bayesian estimation will output a distribution followed by the mean μ of the differences in the performance of two models.

To obtain the posterior distribution we need to define a prior that models our beliefs of how the mean is distributed before looking at the data, and multiply it by a likelihood function that computes how likely our observed differences are, given the values that the mean of differences could take.

Bayesian estimation can be carried out in many forms to answer our question, but in this example we will implement the approach suggested by Benavoli and colleagues [\[4\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id13)
.

One way of defining our posterior using a closed-form expression is to select a prior conjugate to the likelihood function. Benavoli and colleagues [\[4\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id13)
 show that when comparing the performance of two classifiers we can model the prior as a Normal-Gamma distribution (with both mean and variance unknown) conjugate to a normal likelihood, to thus express the posterior as a normal distribution. Marginalizing out the variance from this normal posterior, we can define the posterior of the mean parameter as a Student’s t-distribution. Specifically:

St(μ;n−1,x―,(1n+ntestntrain)σ^2)

where n is the total number of samples, x― represents the mean difference in the scores, ntest is the number of samples used for testing, ntrain is the number of samples used for training, and σ^2 represents the variance of the observed differences.

Notice that we are using Nadeau and Bengio’s corrected variance in our Bayesian approach as well.

Let’s compute and plot the posterior:

\# initialize random variable
t\_post \= [t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t "scipy.stats.t")
(
    df, loc\=[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(differences), scale\=corrected\_std(differences, n\_train, n\_test)
)

Copy to clipboard

Let’s plot the posterior distribution:

x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(t\_post.ppf(0.001), t\_post.ppf(0.999), 100)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, t\_post.pdf(x))
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-0.04, 0.06, 0.01))
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(x, t\_post.pdf(x), 0, facecolor\="blue", alpha\=0.2)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Probability density")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(r"Mean difference ($\\mu$)")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Posterior distribution")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Posterior distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_003.png)

We can calculate the probability that the first model is better than the second by computing the area under the curve of the posterior distribution from zero to infinity. And also the reverse: we can calculate the probability that the second model is better than the first by computing the area under the curve from minus infinity to zero.

better\_prob \= 1 \- t\_post.cdf(0)

print(
    f"Probability of {model\_scores.index\[0\]} being more accurate than "
    f"{model\_scores.index\[1\]}: {better\_prob:.3f}"
)
print(
    f"Probability of {model\_scores.index\[1\]} being more accurate than "
    f"{model\_scores.index\[0\]}: {1 \- better\_prob:.3f}"
)

Copy to clipboard

Probability of rbf being more accurate than linear: 0.773
Probability of linear being more accurate than rbf: 0.227

Copy to clipboard

In contrast with the frequentist approach, we can compute the probability that one model is better than the other.

Note that we obtained similar results as those in the frequentist approach. Given our choice of priors, we are essentially performing the same computations, but we are allowed to make different assertions.

### Region of Practical Equivalence[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#region-of-practical-equivalence "Link to this heading")

Sometimes we are interested in determining the probabilities that our models have an equivalent performance, where “equivalent” is defined in a practical way. A naive approach [\[4\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id13)
 would be to define estimators as practically equivalent when they differ by less than 1% in their accuracy. But we could also define this practical equivalence taking into account the problem we are trying to solve. For example, a difference of 5% in accuracy would mean an increase of $1000 in sales, and we consider any quantity above that as relevant for our business.

In this example we are going to define the Region of Practical Equivalence (ROPE) to be \[−0.01,0.01\]. That is, we will consider two models as practically equivalent if they differ by less than 1% in their performance.

To compute the probabilities of the classifiers being practically equivalent, we calculate the area under the curve of the posterior over the ROPE interval:

rope\_interval \= \[\-0.01, 0.01\]
rope\_prob \= t\_post.cdf(rope\_interval\[1\]) \- t\_post.cdf(rope\_interval\[0\])

print(
    f"Probability of {model\_scores.index\[0\]} and {model\_scores.index\[1\]} "
    f"being practically equivalent: {rope\_prob:.3f}"
)

Copy to clipboard

Probability of rbf and linear being practically equivalent: 0.432

Copy to clipboard

We can plot how the posterior is distributed over the ROPE interval:

x\_rope \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(rope\_interval\[0\], rope\_interval\[1\], 100)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, t\_post.pdf(x))
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-0.04, 0.06, 0.01))
[plt.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
(\[\-0.01, 0.01\], ymin\=0, ymax\=([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(t\_post.pdf(x)) + 1))
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(x\_rope, t\_post.pdf(x\_rope), 0, facecolor\="blue", alpha\=0.2)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Probability density")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(r"Mean difference ($\\mu$)")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Posterior distribution under the ROPE")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Posterior distribution under the ROPE](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_004.png)

As suggested in [\[4\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id13)
, we can further interpret these probabilities using the same criteria as the frequentist approach: is the probability of falling inside the ROPE bigger than 95% (alpha value of 5%)? In that case we can conclude that both models are practically equivalent.

The Bayesian estimation approach also allows us to compute how uncertain we are about our estimation of the difference. This can be calculated using credible intervals. For a given probability, they show the range of values that the estimated quantity, in our case the mean difference in performance, can take. For example, a 50% credible interval \[x, y\] tells us that there is a 50% probability that the true (mean) difference of performance between models is between x and y.

Let’s determine the credible intervals of our data using 50%, 75% and 95%:

cred\_intervals \= \[\]
intervals \= \[0.5, 0.75, 0.95\]

for interval in intervals:
    cred\_interval \= list(t\_post.interval(interval))
    cred\_intervals.append(\[interval, cred\_interval\[0\], cred\_interval\[1\]\])

cred\_int\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    cred\_intervals, columns\=\["interval", "lower value", "upper value"\]
).set\_index("interval")
cred\_int\_df

Copy to clipboard

|     | lower value | upper value |
| --- | --- | --- |
| interval |     |     |
| --- | --- | --- |
| 0.50 | 0.000977 | 0.019023 |
| 0.75 | \-0.005422 | 0.025422 |
| 0.95 | \-0.016445 | 0.036445 |

  
  

As shown in the table, there is a 50% probability that the true mean difference between models will be between 0.000977 and 0.019023, 70% probability that it will be between -0.005422 and 0.025422, and 95% probability that it will be between -0.016445 and 0.036445.

Pairwise comparison of all models: frequentist approach[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#pairwise-comparison-of-all-models-frequentist-approach "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We could also be interested in comparing the performance of all our models evaluated with [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
. In this case we would be running our statistical test multiple times, which leads us to the [multiple comparisons problem](https://en.wikipedia.org/wiki/Multiple_comparisons_problem)
.

There are many possible ways to tackle this problem, but a standard approach is to apply a [Bonferroni correction](https://en.wikipedia.org/wiki/Bonferroni_correction)
. Bonferroni can be computed by multiplying the p-value by the number of comparisons we are testing.

Let’s compare the performance of the models using the corrected t-test:

from itertools import [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations "itertools.combinations")
from math import [factorial](https://docs.python.org/3/library/math.html#math.factorial "math.factorial")

n\_comparisons \= [factorial](https://docs.python.org/3/library/math.html#math.factorial "math.factorial")
(len(model\_scores)) / (
    [factorial](https://docs.python.org/3/library/math.html#math.factorial "math.factorial")
(2) \* [factorial](https://docs.python.org/3/library/math.html#math.factorial "math.factorial")
(len(model\_scores) \- 2)
)
pairwise\_t\_test \= \[\]

for model\_i, model\_k in [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations "itertools.combinations")
(range(len(model\_scores)), 2):
    model\_i\_scores \= model\_scores.iloc\[model\_i\].values
    model\_k\_scores \= model\_scores.iloc\[model\_k\].values
    differences \= model\_i\_scores \- model\_k\_scores
    t\_stat, p\_val \= compute\_corrected\_ttest(differences, df, n\_train, n\_test)
    p\_val \*= n\_comparisons  \# implement Bonferroni correction
    \# Bonferroni can output p-values higher than 1
    p\_val \= 1 if p\_val \> 1 else p\_val
    pairwise\_t\_test.append(
        \[model\_scores.index\[model\_i\], model\_scores.index\[model\_k\], t\_stat, p\_val\]
    )

pairwise\_comp\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    pairwise\_t\_test, columns\=\["model\_1", "model\_2", "t\_stat", "p\_val"\]
).round(3)
pairwise\_comp\_df

Copy to clipboard

|     | model\_1 | model\_2 | t\_stat | p\_val |
| --- | --- | --- | --- | --- |
| 0   | rbf | linear | 0.750 | 1.000 |
| 1   | rbf | 3\_poly | 1.657 | 0.302 |
| 2   | rbf | 2\_poly | 4.565 | 0.000 |
| 3   | linear | 3\_poly | 1.111 | 0.807 |
| 4   | linear | 2\_poly | 4.276 | 0.000 |
| 5   | 3\_poly | 2\_poly | 3.851 | 0.001 |

  
  

We observe that after correcting for multiple comparisons, the only model that significantly differs from the others is `'2_poly'`. `'rbf'`, the model ranked first by [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, does not significantly differ from `'linear'` or `'3_poly'`.

Pairwise comparison of all models: Bayesian approach[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#pairwise-comparison-of-all-models-bayesian-approach "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using Bayesian estimation to compare multiple models, we don’t need to correct for multiple comparisons (for reasons why see [\[4\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#id13)
).

We can carry out our pairwise comparisons the same way as in the first section:

pairwise\_bayesian \= \[\]

for model\_i, model\_k in [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations "itertools.combinations")
(range(len(model\_scores)), 2):
    model\_i\_scores \= model\_scores.iloc\[model\_i\].values
    model\_k\_scores \= model\_scores.iloc\[model\_k\].values
    differences \= model\_i\_scores \- model\_k\_scores
    t\_post \= [t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t "scipy.stats.t")
(
        df, loc\=[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(differences), scale\=corrected\_std(differences, n\_train, n\_test)
    )
    worse\_prob \= t\_post.cdf(rope\_interval\[0\])
    better\_prob \= 1 \- t\_post.cdf(rope\_interval\[1\])
    rope\_prob \= t\_post.cdf(rope\_interval\[1\]) \- t\_post.cdf(rope\_interval\[0\])

    pairwise\_bayesian.append(\[worse\_prob, better\_prob, rope\_prob\])

pairwise\_bayesian\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    pairwise\_bayesian, columns\=\["worse\_prob", "better\_prob", "rope\_prob"\]
).round(3)

pairwise\_comp\_df \= pairwise\_comp\_df.join(pairwise\_bayesian\_df)
pairwise\_comp\_df

Copy to clipboard

|     | model\_1 | model\_2 | t\_stat | p\_val | worse\_prob | better\_prob | rope\_prob |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | rbf | linear | 0.750 | 1.000 | 0.068 | 0.500 | 0.432 |
| 1   | rbf | 3\_poly | 1.657 | 0.302 | 0.018 | 0.882 | 0.100 |
| 2   | rbf | 2\_poly | 4.565 | 0.000 | 0.000 | 1.000 | 0.000 |
| 3   | linear | 3\_poly | 1.111 | 0.807 | 0.063 | 0.750 | 0.187 |
| 4   | linear | 2\_poly | 4.276 | 0.000 | 0.000 | 1.000 | 0.000 |
| 5   | 3\_poly | 2\_poly | 3.851 | 0.001 | 0.000 | 1.000 | 0.000 |

  
  

Using the Bayesian approach we can compute the probability that a model performs better, worse or practically equivalent to another.

Results show that the model ranked first by [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 `'rbf'`, has approximately a 6.8% chance of being worse than `'linear'`, and a 1.8% chance of being worse than `'3_poly'`. `'rbf'` and `'linear'` have a 43% probability of being practically equivalent, while `'rbf'` and `'3_poly'` have a 10% chance of being so.

Similarly to the conclusions obtained using the frequentist approach, all models have a 100% probability of being better than `'2_poly'`, and none have a practically equivalent performance with the latter.

Take-home messages[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#take-home-messages "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

*   Small differences in performance measures might easily turn out to be merely by chance, but not because one model predicts systematically better than the other. As shown in this example, statistics can tell you how likely that is.
    
*   When statistically comparing the performance of two models evaluated in GridSearchCV, it is necessary to correct the calculated variance which could be underestimated since the scores of the models are not independent from each other.
    
*   A frequentist approach that uses a (variance-corrected) paired t-test can tell us if the performance of one model is better than another with a degree of certainty above chance.
    
*   A Bayesian approach can provide the probabilities of one model being better, worse or practically equivalent than another. It can also tell us how confident we are of knowing that the true differences of our models fall under a certain range of values.
    
*   If multiple models are statistically compared, a multiple comparisons correction is needed when using the frequentist approach.
    

References

**Total running time of the script:** (0 minutes 1.903 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_stats.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_stats.ipynb)

[`Download Jupyter notebook: plot_grid_search_stats.ipynb`](https://scikit-learn.org/stable/_downloads/2402de18d671ce5087e3760b2540184f/plot_grid_search_stats.ipynb)

[`Download Python source code: plot_grid_search_stats.py`](https://scikit-learn.org/stable/_downloads/efb3df90d4ec295fa0dafe6c8b46211b/plot_grid_search_stats.py)

[`Download zipped: plot_grid_search_stats.zip`](https://scikit-learn.org/stable/_downloads/d59ecf1ac6d8f981abe3e795cad51cbd/plot_grid_search_stats.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_thumb.png)

[Test with permutations the significance of a classification score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Test with permutations the significance of a classification score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/efb3df90d4ec295fa0dafe6c8b46211b/plot_grid_search_stats.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2402de18d671ce5087e3760b2540184f/plot_grid_search_stats.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d59ecf1ac6d8f981abe3e795cad51cbd/plot_grid_search_stats.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_stats.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_stats.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)