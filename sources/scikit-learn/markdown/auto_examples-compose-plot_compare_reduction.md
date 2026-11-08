[Skip to main content](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/compose/plot_compare_reduction.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/compose/plot_compare_reduction.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/compose/plot_compare_reduction.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/compose/plot_compare_reduction.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/compose/plot_compare_reduction.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/compose/plot_compare_reduction.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#sphx-glr-download-auto-examples-compose-plot-compare-reduction-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Selecting dimensionality reduction with Pipeline and GridSearchCV[#](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#selecting-dimensionality-reduction-with-pipeline-and-gridsearchcv "Link to this heading")

=================================================================================================================================================================================================================================================

This example constructs a pipeline that does dimensionality reduction followed by prediction with a support vector classifier. It demonstrates the use of `GridSearchCV` and `Pipeline` to optimize over different classes of estimators in a single CV run – unsupervised `PCA` and `NMF` dimensionality reductions are compared to univariate feature selection during the grid search.

Additionally, `Pipeline` can be instantiated with the `memory` argument to memoize the transformers within the pipeline, avoiding to fit again the same transformers over and over.

Note that the use of `memory` to enable caching becomes interesting when the fitting of a transformer is costly.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Illustration of `Pipeline` and `GridSearchCV`[#](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#illustration-of-pipeline-and-gridsearchcv "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.decomposition import [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
, [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.feature\_selection import [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
, [mutual\_info\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

X, y \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)

pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("scaling", [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
()),\
        \# the reduce\_dim stage is populated by the param\_grid\
        ("reduce\_dim", "passthrough"),\
        ("classify", [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(dual\=False, max\_iter\=10000)),\
    \]
)

N\_FEATURES\_OPTIONS \= \[2, 4, 8\]
C\_OPTIONS \= \[1, 10, 100, 1000\]
param\_grid \= \[\
    {\
        "reduce\_dim": \[[PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(iterated\_power\=7), [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")\
(max\_iter\=1\_000)\],\
        "reduce\_dim\_\_n\_components": N\_FEATURES\_OPTIONS,\
        "classify\_\_C": C\_OPTIONS,\
    },\
    {\
        "reduce\_dim": \[[SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")\
([mutual\_info\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")\
)\],\
        "reduce\_dim\_\_k": N\_FEATURES\_OPTIONS,\
        "classify\_\_C": C\_OPTIONS,\
    },\
\]
reducer\_labels \= \["PCA", "NMF", "KBest(mutual\_info\_classif)"\]

grid \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(pipe, n\_jobs\=1, param\_grid\=param\_grid)
grid.fit(X, y)

Copy to clipboard

GridSearchCV(estimator=Pipeline(steps=\[('scaling', MinMaxScaler()),\
                                       ('reduce\_dim', 'passthrough'),\
                                       ('classify',\
                                        LinearSVC(dual=False,\
                                                  max\_iter=10000))\]),
             n\_jobs=1,
             param\_grid=\[{'classify\_\_C': \[1, 10, 100, 1000\],\
                          'reduce\_dim': \[PCA(iterated\_power=7),\
                                         NMF(max\_iter=1000)\],\
                          'reduce\_dim\_\_n\_components': \[2, 4, 8\]},\
                         {'classify\_\_C': \[1, 10, 100, 1000\],\
                          'reduce\_dim': \[SelectKBest(score\_func=<function mutual\_info\_classif at 0x7e1df67f2f00>)\],\
                          'reduce\_dim\_\_k': \[2, 4, 8\]}\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...iter=10000))\]) |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | \[{'classify\_\_C': \[1, 10, ...\], 'reduce\_dim': \[PCA(iterated\_power=7), NMF(max\_iter=1000)\], 'reduce\_dim\_\_n\_components': \[2, 4, ...\]}, {'classify\_\_C': \[1, 10, ...\], 'reduce\_dim': \[SelectKBest(s...7e1df67f2f00>)\], 'reduce\_dim\_\_k': \[2, 4, ...\]}\] |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | 1   |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | None |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | Pipeline | Pipeline(step...iter=10000))\]) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(2) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'cl...\_C': 1, 're...im': PCA(iterated\_power=7), 're...ts': 8} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the best\_estimator  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.  <br>  <br>This attribute is not available if \`\`refit\`\` is a function.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_score_,-float) | float64 | 0.8576 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](10,) | \[0,1,2,...,7,8,9\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.01, ..., 0.76, 0.78\]), 'me...me': array(\[0., 0.... 0., 0.\]), 'me...re': array(\[0.52, ..., 0.5 , 0.72\]), 'pa...\_C': masked\_array(...\_value=999999), ...} |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 64  |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 0.0123 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | \_PassthroughScorer | Pipeline.score |

best\_estimator\_: Pipeline

MinMaxScaler

[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[ 0., 8.,16.,...,16.,16.,16.\] |
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[0.,0.,0.,...,0.,0.,0.\] |
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[ 0., 8.,16.,...,16.,16.,16.\] |
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[0.,0.,0.,...,0.,0.,0.\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 64  |
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 1797 |
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[1. ,0.12,0.06,...,0.06,0.06,0.06\] |

64 features

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

PCA

[?Documentation for PCA](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_components n\_components: int, float or 'mle', default=None  <br>  <br>Number of components to keep.  <br>if n\_components is not set all components are kept::  <br>  <br>n\_components == min(n\_samples, n\_features)  <br>  <br>If \`\`n\_components == 'mle'\`\` and \`\`svd\_solver == 'full'\`\`, Minka's  <br>MLE is used to guess the dimension. Use of \`\`n\_components == 'mle'\`\`  <br>will interpret \`\`svd\_solver == 'auto'\`\` as \`\`svd\_solver == 'full'\`\`.  <br>  <br>If \`\`0 < n\_components < 1\`\` and \`\`svd\_solver == 'full'\`\`, select the  <br>number of components such that the amount of variance that needs to be  <br>explained is greater than the percentage specified by n\_components.  <br>  <br>If \`\`svd\_solver == 'arpack'\`\`, the number of components must be  <br>strictly less than the minimum of n\_features and n\_samples.  <br>  <br>Hence, the None case results in::  <br>  <br>n\_components == min(n\_samples, n\_features) - 1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components,-int%2C%20float%20or%20%27mle%27%2C%20default%3DNone) | 8   |
|     | [iterated\_power iterated\_power: int or 'auto', default='auto'  <br>  <br>Number of iterations for the power method computed by  <br>svd\_solver == 'randomized'.  <br>Must be of range \[0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=iterated_power,-int%20or%20%27auto%27%2C%20default%3D%27auto%27) | 7   |\
|     | [copy copy: bool, default=True  <br>  <br>If False, data passed to fit are overwritten and running  <br>fit(X).transform(X) will not yield the expected results,  <br>use fit\_transform(X) instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [whiten whiten: bool, default=False  <br>  <br>When True (False by default) the \`components\_\` vectors are multiplied  <br>by the square root of n\_samples and then divided by the singular values  <br>to ensure uncorrelated outputs with unit component-wise variances.  <br>  <br>Whitening will remove some information from the transformed signal  <br>(the relative variance scales of the components) but can sometime  <br>improve the predictive accuracy of the downstream estimators by  <br>making their data respect some hard-wired assumptions.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=whiten,-bool%2C%20default%3DFalse) | False |\
|     | [svd\_solver svd\_solver: {'auto', 'full', 'covariance\_eigh', 'arpack', 'randomized'}, default='auto'  <br>  <br>"auto" :  <br>The solver is selected by a default 'auto' policy is based on \`X.shape\` and  <br>\`n\_components\`: if the input data has fewer than 1000 features and  <br>more than 10 times as many samples, then the "covariance\_eigh"  <br>solver is used. Otherwise, if the input data is larger than 500x500  <br>and the number of components to extract is lower than 80% of the  <br>smallest dimension of the data, then the more efficient  <br>"randomized" method is selected. Otherwise the exact "full" SVD is  <br>computed and optionally truncated afterwards.  <br>"full" :  <br>Run exact full SVD calling the standard LAPACK solver via  <br>\`scipy.linalg.svd\` and select the components by postprocessing  <br>"covariance\_eigh" :  <br>Precompute the covariance matrix (on centered data), run a  <br>classical eigenvalue decomposition on the covariance matrix  <br>typically using LAPACK and select the components by postprocessing.  <br>This solver is very efficient for n\_samples >> n\_features and small  <br>n\_features. It is, however, not tractable otherwise for large  <br>n\_features (large memory footprint required to materialize the  <br>covariance matrix). Also note that compared to the "full" solver,  <br>this solver effectively doubles the condition number and is  <br>therefore less numerical stable (e.g. on input data with a large  <br>range of singular values).  <br>"arpack" :  <br>Run SVD truncated to \`n\_components\` calling ARPACK solver via  <br>\`scipy.sparse.linalg.svds\`. It requires strictly  <br>\`0 < n\_components < min(X.shape)\`  <br>"randomized" :  <br>Run randomized SVD by the method of Halko et al.  <br>  <br>.. versionadded:: 0.18.0  <br>  <br>.. versionchanged:: 1.5  <br>Added the 'covariance\_eigh' solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=svd_solver,-%7B%27auto%27%2C%20%27full%27%2C%20%27covariance_eigh%27%2C%20%27arpack%27%2C%20%27randomized%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27auto%27) | 'auto' |\
|     | [tol tol: float, default=0.0  <br>  <br>Tolerance for singular values computed by svd\_solver == 'arpack'.  <br>Must be of range \[0.0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=tol,-float%2C%20default%3D0.0) | 0.0 |\
|     | [n\_oversamples n\_oversamples: int, default=10  <br>  <br>This parameter is only relevant when \`svd\_solver="randomized"\`.  <br>It corresponds to the additional number of random vectors to sample the  <br>range of \`X\` so as to ensure proper conditioning. See  <br>:func:\`~sklearn.utils.extmath.randomized\_svd\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_oversamples,-int%2C%20default%3D10) | 10  |\
|     | [power\_iteration\_normalizer power\_iteration\_normalizer: {'auto', 'QR', 'LU', 'none'}, default='auto'  <br>  <br>Power iteration normalizer for randomized SVD solver.  <br>Not used by ARPACK. See :func:\`~sklearn.utils.extmath.randomized\_svd\`  <br>for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=power_iteration_normalizer,-%7B%27auto%27%2C%20%27QR%27%2C%20%27LU%27%2C%20%27none%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Used when the 'arpack' or 'randomized' solvers are used. Pass an int  <br>for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Principal axes in feature space, representing the directions of  <br>maximum variance in the data. Equivalently, the right singular  <br>vectors of the centered input data, parallel to its eigenvectors.  <br>The components are sorted by decreasing \`\`explained\_variance\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float64\](8, 64) | \[\[ 0. ,-0.04,-0.23,...,-0.08,-0.04,-0.01\], \[ 0. , 0.02, 0.03,...,-0.17,-0.01, 0.01\], \[ 0. ,-0.04,-0.12,...,-0.24,-0.17,-0.03\], ..., \[ 0. , 0.02, 0.08,...,-0.16,-0.14,-0.02\], \[ 0. , 0.01, 0.04,...,-0.08,-0.22,-0.11\], \[ 0. ,-0.05,-0.21,..., 0.3 , 0.13, 0.01\]\] |\
| [explained\_variance\_ explained\_variance\_: ndarray of shape (n\_components,)  <br>  <br>The amount of variance explained by each of the selected components.  <br>The variance estimation uses \`n\_samples - 1\` degrees of freedom.  <br>  <br>Equal to n\_components largest eigenvalues  <br>of the covariance matrix of X.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=explained_variance_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](8,) | \[0.71,0.65,0.56,...,0.23,0.2 ,0.18\] |\
| [explained\_variance\_ratio\_ explained\_variance\_ratio\_: ndarray of shape (n\_components,)  <br>  <br>Percentage of variance explained by each of the selected components.  <br>  <br>If \`\`n\_components\`\` is not set then all components are stored and the  <br>sum of the ratios is equal to 1.0.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=explained_variance_ratio_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](8,) | \[0.15,0.14,0.12,...,0.05,0.04,0.04\] |\
| [mean\_ mean\_: ndarray of shape (n\_features,)  <br>  <br>Per-feature empirical mean, estimated from the training set.  <br>  <br>Equal to \`X.mean(axis=0)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](64,) | \[0. ,0.04,0.33,...,0.42,0.13,0.02\] |\
| [n\_components\_ n\_components\_: int  <br>  <br>The estimated number of components. When n\_components is set  <br>to 'mle' or a number between 0 and 1 (with svd\_solver == 'full') this  <br>number is estimated from input data. Otherwise it equals the parameter  <br>n\_components, or the lesser value of n\_features and n\_samples  <br>if n\_components is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components_,-int) | int | 8   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_features_in_,-int) | int | 64  |\
| [n\_samples\_ n\_samples\_: int  <br>  <br>Number of samples in the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_samples_,-int) | int | 1797 |\
| [noise\_variance\_ noise\_variance\_: float  <br>  <br>The estimated noise covariance following the Probabilistic PCA model  <br>from Tipping and Bishop 1999. See "Pattern Recognition and  <br>Machine Learning" by C. Bishop, 12.2.1 p. 574 or  <br>http://www.miketipping.com/papers/met-mppca.pdf. It is required to  <br>compute the estimated data covariance and score samples.  <br>  <br>Equal to the average of (min(n\_features, n\_samples) - n\_components)  <br>smallest eigenvalues of the covariance matrix of X.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=noise_variance_,-float) | float64 | 0.02823 |\
| [singular\_values\_ singular\_values\_: ndarray of shape (n\_components,)  <br>  <br>The singular values corresponding to each of the selected components.  <br>The singular values are equal to the 2-norms of the \`\`n\_components\`\`  <br>variables in the lower-dimensional space.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=singular_values_,-ndarray%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](8,) | \[35.64,34.05,31.68,...,20.39,19.09,17.75\] |\
\
8 features\
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
\
LinearSVC\
\
[?Documentation for LinearSVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [dual dual: "auto" or bool, default="auto"  <br>  <br>Select the algorithm to either solve the dual or primal  <br>optimization problem. Prefer dual=False when n\_samples > n\_features.  <br>\`dual="auto"\` will choose the value of the parameter automatically,  <br>based on the values of \`n\_samples\`, \`n\_features\`, \`loss\`, \`multi\_class\`  <br>and \`penalty\`. If \`n\_samples\` < \`n\_features\` and optimizer supports  <br>chosen \`loss\`, \`multi\_class\` and \`penalty\`, then dual will be set to True,  <br>otherwise it will be set to False.  <br>  <br>.. versionchanged:: 1.3  <br>The \`"auto"\` option is added in version 1.3 and will be the default  <br>in version 1.5.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=dual,-%22auto%22%20or%20bool%2C%20default%3D%22auto%22) | False |\
|     | [max\_iter max\_iter: int, default=1000  <br>  <br>The maximum number of iterations to be run.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=max_iter,-int%2C%20default%3D1000) | 10000 |\
|     | [penalty penalty: {'l1', 'l2'}, default='l2'  <br>  <br>Specifies the norm used in the penalization. The 'l2'  <br>penalty is the standard used in SVC. The 'l1' leads to \`\`coef\_\`\`  <br>vectors that are sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%7D%2C%20default%3D%27l2%27) | 'l2' |\
|     | [loss loss: {'hinge', 'squared\_hinge'}, default='squared\_hinge'  <br>  <br>Specifies the loss function. 'hinge' is the standard SVM loss  <br>(used e.g. by the SVC class) while 'squared\_hinge' is the  <br>square of the hinge loss. The combination of \`\`penalty='l1'\`\`  <br>and \`\`loss='hinge'\`\` is not supported.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=loss,-%7B%27hinge%27%2C%20%27squared_hinge%27%7D%2C%20default%3D%27squared_hinge%27) | 'squared\_hinge' |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive.  <br>For an intuitive visualization of the effects of scaling  <br>the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1   |\
|     | [multi\_class multi\_class: {'ovr', 'crammer\_singer'}, default='ovr'  <br>  <br>Determines the multi-class strategy if \`y\` contains more than  <br>two classes.  <br>\`\`"ovr"\`\` trains n\_classes one-vs-rest classifiers, while  <br>\`\`"crammer\_singer"\`\` optimizes a joint objective over all classes.  <br>While \`crammer\_singer\` is interesting from a theoretical perspective  <br>as it is consistent, it is seldom used in practice as it rarely leads  <br>to better accuracy and is more expensive to compute.  <br>If \`\`"crammer\_singer"\`\` is chosen, the options loss, penalty and dual  <br>will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=multi_class,-%7B%27ovr%27%2C%20%27crammer_singer%27%7D%2C%20default%3D%27ovr%27) | 'ovr' |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether or not to fit an intercept. If set to True, the feature vector  <br>is extended to include an intercept term: \`\[x\_1, ..., x\_n, 1\]\`, where  <br>1 corresponds to the intercept. If set to False, no intercept will be  <br>used in calculations (i.e. data is expected to be already centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1.0  <br>  <br>When \`fit\_intercept\` is True, the instance vector x becomes \`\`\[x\_1,  <br>..., x\_n, intercept\_scaling\]\`\`, i.e. a "synthetic" feature with a  <br>constant value equal to \`intercept\_scaling\` is appended to the instance  <br>vector. The intercept becomes intercept\_scaling \* synthetic feature  <br>weight. Note that liblinear internally penalizes the intercept,  <br>treating it like any other term in the feature vector. To reduce the  <br>impact of the regularization on the intercept, the \`intercept\_scaling\`  <br>parameter can be set to a value greater than 1; the higher the value of  <br>\`intercept\_scaling\`, the lower the impact of regularization on it.  <br>Then, the weights become \`\[w\_x\_1, ..., w\_x\_n,  <br>w\_intercept\*intercept\_scaling\]\`, where \`w\_x\_1, ..., w\_x\_n\` represent  <br>the feature weights and the intercept weight is scaled by  <br>\`intercept\_scaling\`. This scaling allows the intercept term to have a  <br>different regularization behavior compared to the other features.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=intercept_scaling,-float%2C%20default%3D1.0) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Set the parameter C of class i to \`\`class\_weight\[i\]\*C\`\` for  <br>SVC. If not given, all classes are supposed to have  <br>weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Enable verbose output. Note that this setting takes advantage of a  <br>per-process runtime setting in liblinear that, if enabled, may not work  <br>properly in a multithreaded context.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>the dual coordinate descent (if \`\`dual=True\`\`). When \`\`dual=False\`\` the  <br>underlying implementation of :class:\`LinearSVC\` is not random and  <br>\`\`random\_state\`\` has no effect on the results.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The unique classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](10,) | \[0,1,2,...,7,8,9\] |\
| [coef\_ coef\_: ndarray of shape (1, n\_features) if n\_classes == 2 else (n\_classes, n\_features)  <br>  <br>Weights assigned to the features (coefficients in the primal  <br>problem).  <br>  <br>\`\`coef\_\`\` is a readonly property derived from \`\`raw\_coef\_\`\` that  <br>follows the internal memory layout of liblinear.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=coef_,-ndarray%20of%20shape%20%281%2C%20n_features%29%20if%20n_classes%20%3D%3D%202%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](10, 8) | \[\[ 0.41,-1.87, 0.37,..., 1.09, 0.04, 0.56\], \[ 0.09, 1.02,-0.23,..., 0.78,-0.2 , 0.49\], \[-1.19, 0.56,-1.81,..., 0.5 ,-2.05, 0.98\], ..., \[-0.21, 1.09, 1.37,...,-0.65, 0.19,-0.74\], \[-0.22, 0.13,-0.11,..., 0.31, 0.98, 1.17\], \[-0.58,-0.48, 0.7 ,...,-0.05, 0.61, 0.14\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) if n\_classes == 2 else (n\_classes,)  <br>  <br>Constants in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20if%20n_classes%20%3D%3D%202%20else%20%28n_classes%2C%29) | ndarray\[float64\](10,) | \[-2.84,-1.82,-3.04,...,-2.35,-1.19,-1.38\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=n_features_in_,-int) | int | 8   |\
| [n\_iter\_ n\_iter\_: int  <br>  <br>Maximum number of iterations run across all classes.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=n_iter_,-int) | int | 9   |\
\
  \
  \
\
import pandas as pd\
\
mean\_scores \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(grid.cv\_results\_\["mean\_test\_score"\])\
\# scores are in the order of param\_grid iteration, which is alphabetical\
mean\_scores \= mean\_scores.reshape(len(C\_OPTIONS), \-1, len(N\_FEATURES\_OPTIONS))\
\# select score for best C\
mean\_scores \= mean\_scores.max(axis\=0)\
\# create a dataframe to ease plotting\
mean\_scores \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    mean\_scores.T, index\=N\_FEATURES\_OPTIONS, columns\=reducer\_labels\
)\
\
ax \= mean\_scores.plot.bar()\
ax.set\_title("Comparing feature reduction techniques")\
ax.set\_xlabel("Reduced number of features")\
ax.set\_ylabel("Digit classification accuracy")\
ax.set\_ylim((0, 1))\
ax.legend(loc\="upper left")\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![Comparing feature reduction techniques](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_001.png)\
\
Caching transformers within a `Pipeline`[#](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#caching-transformers-within-a-pipeline "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
It is sometimes worthwhile storing the state of a specific transformer since it could be used again. Using a pipeline in `GridSearchCV` triggers such situations. Therefore, we use the argument `memory` to enable caching.\
\
Warning\
\
Note that this example is, however, only an illustration since for this specific case fitting PCA is not necessarily slower than loading the cache. Hence, use the `memory` constructor parameter when the fitting of a transformer is costly.\
\
from shutil import [rmtree](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")\
\
from joblib import [Memory](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory "joblib.Memory")\
\
\# Create a temporary folder to store the transformers of the pipeline\
location \= "cachedir"\
memory \= [Memory](https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html#joblib.Memory "joblib.Memory")\
(location\=location, verbose\=10)\
cached\_pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    \[("reduce\_dim", [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
()), ("classify", [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(dual\=False, max\_iter\=10000))\],\
    memory\=memory,\
)\
\
\# This time, a cached pipeline will be used within the grid search\
\
\# Delete the temporary cache before exiting\
memory.clear(warn\=False)\
[rmtree](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")\
(location)\
\
Copy to clipboard\
\
The `PCA` fitting is only computed at the evaluation of the first configuration of the `C` parameter of the `LinearSVC` classifier. The other configurations of `C` will trigger the loading of the cached `PCA` estimator data, leading to save processing time. Therefore, the use of caching the pipeline using `memory` is highly beneficial when fitting a transformer is costly.\
\
**Total running time of the script:** (0 minutes 50.255 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_compare_reduction.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_compare_reduction.ipynb)\
\
[`Download Jupyter notebook: plot_compare_reduction.ipynb`](https://scikit-learn.org/stable/_downloads/e38f4849bd47832b7b365f2fa9d31dd6/plot_compare_reduction.ipynb)\
\
[`Download Python source code: plot_compare_reduction.py`](https://scikit-learn.org/stable/_downloads/f30499f1e20a3d5f0f83bb90cd6ff348/plot_compare_reduction.py)\
\
[`Download zipped: plot_compare_reduction.zip`](https://scikit-learn.org/stable/_downloads/7d91d0d0f33d92090d8ca10243f0562b/plot_compare_reduction.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)\
\
[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)\
\
Incremental PCA\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)\
\
[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)\
\
Concatenating multiple feature extraction methods\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)\
\
[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)\
\
Feature agglomeration vs. univariate selection\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)\
\
[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)\
\
Caching nearest neighbors\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/f30499f1e20a3d5f0f83bb90cd6ff348/plot_compare_reduction.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e38f4849bd47832b7b365f2fa9d31dd6/plot_compare_reduction.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/7d91d0d0f33d92090d8ca10243f0562b/plot_compare_reduction.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_compare_reduction.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_compare_reduction.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)