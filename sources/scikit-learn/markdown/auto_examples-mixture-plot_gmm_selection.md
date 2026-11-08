[Skip to main content](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/mixture/plot_gmm_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/mixture/plot_gmm_selection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/mixture/plot_gmm_selection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/mixture/plot_gmm_selection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/mixture/plot_gmm_selection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/mixture/plot_gmm_selection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#sphx-glr-download-auto-examples-mixture-plot-gmm-selection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gaussian Mixture Model Selection[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#gaussian-mixture-model-selection "Link to this heading")

===========================================================================================================================================================================

This example shows that model selection can be performed with Gaussian Mixture Models (GMM) using [information-theory criteria](https://scikit-learn.org/stable/modules/linear_model.html#aic-bic)
. Model selection concerns both the covariance type and the number of components in the model.

In this case, both the Akaike Information Criterion (AIC) and the Bayes Information Criterion (BIC) provide the right result, but we only demo the latter as BIC is better suited to identify the true model among a set of candidates. Unlike Bayesian procedures, such inferences are prior-free.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#data-generation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

We generate two components (each one containing `n_samples`) by randomly sampling the standard normal distribution as returned by `numpy.random.randn`. One component is kept spherical yet shifted and re-scaled. The other one is deformed to have a more general covariance matrix.

import numpy as np

n\_samples \= 500
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
C \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.0, \-0.1\], \[1.7, 0.4\]\])
component\_1 \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, 2), C)  \# general
component\_2 \= 0.7 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, 2) + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\-4, 1\])  \# spherical

X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[component\_1, component\_2\])

Copy to clipboard

We can visualize the different components:

import matplotlib.pyplot as plt

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(component\_1\[:, 0\], component\_1\[:, 1\], s\=0.8)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(component\_2\[:, 0\], component\_2\[:, 1\], s\=0.8)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Gaussian Mixture components")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("equal")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Gaussian Mixture components](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_001.png)

Model training and selection[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#model-training-and-selection "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

We vary the number of components from 1 to 6 and the type of covariance parameters to use:

*   `"full"`: each component has its own general covariance matrix.
    
*   `"tied"`: all components share the same general covariance matrix.
    
*   `"diag"`: each component has its own diagonal covariance matrix.
    
*   `"spherical"`: each component has its own single variance.
    

We score the different models and keep the best model (the lowest BIC). This is done by using [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 and a user-defined score function which returns the negative BIC score, as [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 is designed to **maximize** a score (maximizing the negative BIC is equivalent to minimizing the BIC).

The best set of parameters and estimator are stored in `best_parameters_` and `best_estimator_`, respectively.

from sklearn.mixture import [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")

def gmm\_bic\_score(estimator, X):
    """Callable to pass to GridSearchCV that will use the BIC score."""
    \# Make it negative since GridSearchCV expects a score to maximize
    return \-estimator.bic(X)

param\_grid \= {
    "n\_components": range(1, 7),
    "covariance\_type": \["spherical", "tied", "diag", "full"\],
}
grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(), param\_grid\=param\_grid, scoring\=gmm\_bic\_score
)
grid\_search.fit(X)

Copy to clipboard

GridSearchCV(estimator=GaussianMixture(),
             param\_grid={'covariance\_type': \['spherical', 'tied', 'diag',\
                                             'full'\],
                         'n\_components': range(1, 7)},
             scoring=<function gmm\_bic\_score at 0x7e1dbc12afb0>)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | GaussianMixture() |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | {'covariance\_type': \['spherical', 'tied', ...\], 'n\_components': range(1, 7)} |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | <function gmm...x7e1dbc12afb0> |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | GaussianMixture | GaussianMixtu...\_components=2) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(19) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'co...pe': 'full', 'n\_...ts': 2} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the best\_estimator  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.  <br>  <br>This attribute is not available if \`\`refit\`\` is a function.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_score_,-float) | float64 | \-1047 |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.0021..., 0.01674428\]), 'me...me': array(\[0.0003..., 0.00050821\]), 'me...re': array(\[-1728....179.97789043\]), 'pa...pe': masked\_array(... dtype=object), ...} |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 0.005431 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | function | <function gmm...x7e1dbc12afb0> |

best\_estimator\_: GaussianMixture

GaussianMixture(n\_components=2)

GaussianMixture

[?Documentation for GaussianMixture](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_components n\_components: int, default=1  <br>  <br>The number of mixture components.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=n_components,-int%2C%20default%3D1) | 2   |
|     | [covariance\_type covariance\_type: {'full', 'tied', 'diag', 'spherical'}, default='full'  <br>  <br>String describing the type of covariance parameters to use.  <br>Must be one of:  <br>  <br>\- 'full': each component has its own general covariance matrix.  <br>\- 'tied': all components share the same general covariance matrix.  <br>\- 'diag': each component has its own diagonal covariance matrix.  <br>\- 'spherical': each component has its own single variance.  <br>  <br>For an example of using \`covariance\_type\`, refer to  <br>:ref:\`sphx\_glr\_auto\_examples\_mixture\_plot\_gmm\_selection.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=covariance_type,-%7B%27full%27%2C%20%27tied%27%2C%20%27diag%27%2C%20%27spherical%27%7D%2C%20default%3D%27full%27) | 'full' |
|     | [tol tol: float, default=1e-3  <br>  <br>The convergence threshold. EM iterations will stop when the  <br>lower bound average gain is below this threshold.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=tol,-float%2C%20default%3D1e-3) | 0.001 |
|     | [reg\_covar reg\_covar: float, default=1e-6  <br>  <br>Non-negative regularization added to the diagonal of covariance.  <br>Allows to assure that the covariance matrices are all positive.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=reg_covar,-float%2C%20default%3D1e-6) | 1e-06 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The number of EM iterations to perform.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [n\_init n\_init: int, default=1  <br>  <br>The number of initializations to perform. The best results are kept.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=n_init,-int%2C%20default%3D1) | 1   |
|     | [init\_params init\_params: {'kmeans', 'k-means++', 'random', 'random\_from\_data'}, default='kmeans'  <br>  <br>The method used to initialize the weights, the means and the  <br>precisions.  <br>String must be one of:  <br>  <br>\- 'kmeans' : responsibilities are initialized using kmeans.  <br>\- 'k-means++' : use the k-means++ method to initialize.  <br>\- 'random' : responsibilities are initialized randomly.  <br>\- 'random\_from\_data' : initial means are randomly selected data points.  <br>  <br>.. versionchanged:: v1.1  <br>\`init\_params\` now accepts 'random\_from\_data' and 'k-means++' as  <br>initialization methods.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=init_params,-%7B%27kmeans%27%2C%20%27k-means%2B%2B%27%2C%20%27random%27%2C%20%27random_from_data%27%7D%2C%20%20%20%20%20default%3D%27kmeans%27) | 'kmeans' |
|     | [weights\_init weights\_init: array-like of shape (n\_components, ), default=None  <br>  <br>The user-provided initial weights.  <br>If it is None, weights are initialized using the \`init\_params\` method.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=weights_init,-array-like%20of%20shape%20%28n_components%2C%20%29%2C%20default%3DNone) | None |
|     | [means\_init means\_init: array-like of shape (n\_components, n\_features), default=None  <br>  <br>The user-provided initial means,  <br>If it is None, means are initialized using the \`init\_params\` method.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=means_init,-array-like%20of%20shape%20%28n_components%2C%20n_features%29%2C%20default%3DNone) | None |
|     | [precisions\_init precisions\_init: array-like, default=None  <br>  <br>The user-provided initial precisions (inverse of the covariance  <br>matrices).  <br>If it is None, precisions are initialized using the 'init\_params'  <br>method.  <br>The shape depends on 'covariance\_type'::  <br>  <br>(n\_components,) if 'spherical',  <br>(n\_features, n\_features) if 'tied',  <br>(n\_components, n\_features) if 'diag',  <br>(n\_components, n\_features, n\_features) if 'full'](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=precisions_init,-array-like%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the random seed given to the method chosen to initialize the  <br>parameters (see \`init\_params\`).  <br>In addition, it controls the generation of random samples from the  <br>fitted distribution (see the method \`sample\`).  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>If 'warm\_start' is True, the solution of the last fitting is used as  <br>initialization for the next call of fit(). This can speed up  <br>convergence when fit is called several times on similar problems.  <br>In that case, 'n\_init' is ignored and only a single initialization  <br>occurs upon the first call.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [verbose verbose: int, default=0  <br>  <br>Enable verbose output. If 1 then it prints the current  <br>initialization and each iteration step. If greater than 1 then  <br>it prints also the log probability and the time needed  <br>for each step.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [verbose\_interval verbose\_interval: int, default=10  <br>  <br>Number of iteration done before the next print.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=verbose_interval,-int%2C%20default%3D10) | 10  |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [converged\_ converged\_: bool  <br>  <br>True when convergence of the best fit of EM was reached, False otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=converged_,-bool) | bool | True |
| [covariances\_ covariances\_: array-like  <br>  <br>The covariance of each mixture component.  <br>The shape depends on \`covariance\_type\`::  <br>  <br>(n\_components,) if 'spherical',  <br>(n\_features, n\_features) if 'tied',  <br>(n\_components, n\_features) if 'diag',  <br>(n\_components, n\_features, n\_features) if 'full'  <br>  <br>For an example of using covariances, refer to  <br>:ref:\`sphx\_glr\_auto\_examples\_mixture\_plot\_gmm\_covariances.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=covariances_,-array-like) | ndarray\[float64\](2, 2, 2) | \[\[\[ 2.89, 0.68\], \[ 0.68, 0.17\]\], \[\[ 0.47,-0.01\], \[-0.01, 0.46\]\]\] |
| [lower\_bound\_ lower\_bound\_: float  <br>  <br>Lower bound value on the log-likelihood (of the training data with  <br>respect to the model) of the best fit of EM.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=lower_bound_,-float) | float64 | \-2.233 |
| [lower\_bounds\_ lower\_bounds\_: array-like of shape (\`n\_iter\_\`,)  <br>  <br>The list of lower bound values on the log-likelihood from each  <br>iteration of the best fit of EM.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=lower_bounds_,-array-like%20of%20shape%20%28n_iter_%2C%29) | list | \[np.float64(-2...0495624935283), np.float64(-2...4448492771387), np.float64(-2...5645944775564), np.float64(-2...8322149565912), ...\] |
| [means\_ means\_: array-like of shape (n\_components, n\_features)  <br>  <br>The mean of each mixture component.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=means_,-array-like%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float64\](2, 2) | \[\[-0.04,-0. \], \[-3.99, 1. \]\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_iter\_ n\_iter\_: int  <br>  <br>Number of step used by the best fit of EM to reach the convergence.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=n_iter_,-int) | int | 5   |
| [precisions\_ precisions\_: array-like  <br>  <br>The precision matrices for each component in the mixture. A precision  <br>matrix is the inverse of a covariance matrix. A covariance matrix is  <br>symmetric positive definite so the mixture of Gaussian can be  <br>equivalently parameterized by the precision matrices. Storing the  <br>precision matrices instead of the covariance matrices makes it more  <br>efficient to compute the log-likelihood of new samples at test time.  <br>The shape depends on \`covariance\_type\`::  <br>  <br>(n\_components,) if 'spherical',  <br>(n\_features, n\_features) if 'tied',  <br>(n\_components, n\_features) if 'diag',  <br>(n\_components, n\_features, n\_features) if 'full'](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=precisions_,-array-like) | ndarray\[float64\](2, 2, 2) | \[\[\[ 6.18,-24.84\], \[-24.84,105.76\]\], \[\[ 2.15, 0.04\], \[ 0.04, 2.19\]\]\] |
| [precisions\_cholesky\_ precisions\_cholesky\_: array-like  <br>  <br>The Cholesky decomposition of the precision matrices of each mixture  <br>component. A precision matrix is the inverse of a covariance matrix.  <br>A covariance matrix is symmetric positive definite so the mixture of  <br>Gaussian can be equivalently parameterized by the precision matrices.  <br>Storing the precision matrices instead of the covariance matrices makes  <br>it more efficient to compute the log-likelihood of new samples at test  <br>time. The shape depends on \`covariance\_type\`::  <br>  <br>(n\_components,) if 'spherical',  <br>(n\_features, n\_features) if 'tied',  <br>(n\_components, n\_features) if 'diag',  <br>(n\_components, n\_features, n\_features) if 'full'](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=precisions_cholesky_,-array-like) | ndarray\[float64\](2, 2, 2) | \[\[\[ 0.59,-2.42\], \[ 0. ,10.28\]\], \[\[ 1.46, 0.02\], \[ 0. , 1.48\]\]\] |
| [weights\_ weights\_: array-like of shape (n\_components,)  <br>  <br>The weights of each mixture components.](https://scikit-learn.org/1.9/modules/generated/sklearn.mixture.GaussianMixture.html#:~:text=weights_,-array-like%20of%20shape%20%28n_components%2C%29) | ndarray\[float64\](2,) | \[0.5,0.5\] |

  
  

Plot the BIC scores[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#plot-the-bic-scores "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

To ease the plotting we can create a `pandas.DataFrame` from the results of the cross-validation done by the grid search. We re-inverse the sign of the BIC score to show the effect of minimizing it.

import pandas as pd

df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(grid\_search.cv\_results\_)\[\
    \["param\_n\_components", "param\_covariance\_type", "mean\_test\_score"\]\
\]
df\["mean\_test\_score"\] \= \-df\["mean\_test\_score"\]
df \= df.rename(
    columns\={
        "param\_n\_components": "Number of components",
        "param\_covariance\_type": "Type of covariance",
        "mean\_test\_score": "BIC score",
    }
)
df.sort\_values(by\="BIC score").head()

Copy to clipboard

|     | Number of components | Type of covariance | BIC score |
| --- | --- | --- | --- |
| 19  | 2   | full | 1046.829429 |
| 20  | 3   | full | 1084.038689 |
| 21  | 4   | full | 1114.517272 |
| 22  | 5   | full | 1148.512281 |
| 23  | 6   | full | 1179.977890 |

  
  

import seaborn as sns

[sns.catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")
(
    data\=df,
    kind\="bar",
    x\="Number of components",
    y\="BIC score",
    hue\="Type of covariance",
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot gmm selection](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_002.png)

In the present case, the model with 2 components and full covariance (which corresponds to the true generative model) has the lowest BIC score and is therefore selected by the grid search.

Plot the best model[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#plot-the-best-model "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

We plot an ellipse to show each Gaussian component of the selected model. For such purpose, one needs to find the eigenvalues of the covariance matrices as returned by the `covariances_` attribute. The shape of such matrices depends on the `covariance_type`:

*   `"full"`: (`n_components`, `n_features`, `n_features`)
    
*   `"tied"`: (`n_features`, `n_features`)
    
*   `"diag"`: (`n_components`, `n_features`)
    
*   `"spherical"`: (`n_components`,)
    

from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
from scipy import linalg

color\_iter \= [sns.color\_palette](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
("tab10", 2)\[::\-1\]
Y\_ \= grid\_search.predict(X)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

for i, (mean, cov, color) in enumerate(
    zip(
        grid\_search.best\_estimator\_.means\_,
        grid\_search.best\_estimator\_.covariances\_,
        color\_iter,
    )
):
    v, w \= [linalg.eigh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html#scipy.linalg.eigh "scipy.linalg.eigh")
(cov)
    if not [np.any](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
(Y\_ \== i):
        continue
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[Y\_ \== i, 0\], X\[Y\_ \== i, 1\], 0.8, color\=color)

    angle \= [np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
(w\[0\]\[1\], w\[0\]\[0\])
    angle \= 180.0 \* angle / [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
  \# convert to degrees
    v \= 2.0 \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(2.0) \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(v)
    ellipse \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(mean, v\[0\], v\[1\], angle\=180.0 + angle, color\=color)
    ellipse.set\_clip\_box(fig.bbox)
    ellipse.set\_alpha(0.5)
    ax.add\_artist(ellipse)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    f"Selected GMM: {grid\_search.best\_params\_\['covariance\_type'\]} model, "
    f"{grid\_search.best\_params\_\['n\_components'\]} components"
)
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("equal")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Selected GMM: full model, 2 components](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_003.png)

**Total running time of the script:** (0 minutes 1.528 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm_selection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm_selection.ipynb)

[`Download Jupyter notebook: plot_gmm_selection.ipynb`](https://scikit-learn.org/stable/_downloads/ed5e2dba642062278ab833dd7617cfe0/plot_gmm_selection.ipynb)

[`Download Python source code: plot_gmm_selection.py`](https://scikit-learn.org/stable/_downloads/61adcadacdb5cfe445011b0b0d065d44/plot_gmm_selection.py)

[`Download zipped: plot_gmm_selection.zip`](https://scikit-learn.org/stable/_downloads/4eaf86254084752c8a966ae3e3b83708/plot_gmm_selection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_thumb.png)

[Gaussian Mixture Model Ellipsoids](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)

Gaussian Mixture Model Ellipsoids

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lars_ic_thumb.png)

[Lasso model selection via information criteria](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars_ic.html)

Lasso model selection via information criteria

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_thumb.png)

[Linear and Quadratic Discriminant Analysis with covariance ellipsoid](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)

Linear and Quadratic Discriminant Analysis with covariance ellipsoid

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_sin_thumb.png)

[Gaussian Mixture Model Sine Curve](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html)

Gaussian Mixture Model Sine Curve

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/61adcadacdb5cfe445011b0b0d065d44/plot_gmm_selection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ed5e2dba642062278ab833dd7617cfe0/plot_gmm_selection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4eaf86254084752c8a966ae3e3b83708/plot_gmm_selection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm_selection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm_selection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)