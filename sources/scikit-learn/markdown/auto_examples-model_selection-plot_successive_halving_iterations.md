[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_successive_halving_iterations.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_successive_halving_iterations.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_successive_halving_iterations.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_successive_halving_iterations.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_successive_halving_iterations.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_successive_halving_iterations.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html#sphx-glr-download-auto-examples-model-selection-plot-successive-halving-iterations-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Successive Halving Iterations[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html#successive-halving-iterations "Link to this heading")

=============================================================================================================================================================================================

This example illustrates how a successive halving search ([`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 and [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
) iteratively chooses the best parameter combination out of multiple candidates.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")

from sklearn import datasets
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.experimental import enable\_halving\_search\_cv  \# noqa: F401
from sklearn.model\_selection import [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")

Copy to clipboard

We first define the parameter space and train a [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
 instance.

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

X, y \= [datasets.make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=400, n\_features\=12, random\_state\=rng)

clf \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(n\_estimators\=20, random\_state\=rng)

param\_dist \= {
    "max\_depth": \[3, None\],
    "max\_features": [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")
(1, 6),
    "min\_samples\_split": [randint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint")
(2, 11),
    "bootstrap": \[True, False\],
    "criterion": \["gini", "entropy"\],
}

rsh \= [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
(
    estimator\=clf, param\_distributions\=param\_dist, factor\=2, random\_state\=rng
)
rsh.fit(X, y)

Copy to clipboard

HalvingRandomSearchCV(estimator=RandomForestClassifier(n\_estimators=20,
                                                       random\_state=RandomState(MT19937) at 0x7E1DF5B93940),
                      factor=2,
                      param\_distributions={'bootstrap': \[True, False\],
                                           'criterion': \['gini', 'entropy'\],
                                           'max\_depth': \[3, None\],
                                           'max\_features': <scipy.stats.\_distn\_infrastructure.rv\_discrete\_frozen object at 0x7e1db436e650>,
                                           'min\_samples\_split': <scipy.stats.\_distn\_infrastructure.rv\_discrete\_frozen object at 0x7e1d94a0cb00>},
                      random\_state=RandomState(MT19937) at 0x7E1DF5B93940)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

HalvingRandomSearchCV

[?Documentation for HalvingRandomSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=estimator,-estimator%20object) | RandomForestC...x7E1DF5B93940) |
|     | [param\_distributions param\_distributions: dict or list of dicts  <br>  <br>Dictionary with parameters names (\`str\`) as keys and distributions  <br>or lists of parameters to try. Distributions must provide a \`\`rvs\`\`  <br>method for sampling (such as those from scipy.stats.distributions).  <br>If a list is given, it is sampled uniformly.  <br>If a list of dicts is given, first a dict is sampled uniformly, and  <br>then a parameter is sampled using that dict as above.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=param_distributions,-dict%20or%20list%20of%20dicts) | {'bootstrap': \[True, False\], 'criterion': \['gini', 'entropy'\], 'max\_depth': \[3, None\], 'max\_features': <scipy.stats....x7e1db436e650>, ...} |
|     | [factor factor: int or float, default=3  <br>  <br>The 'halving' parameter, which determines the proportion of candidates  <br>that are selected for each subsequent iteration. For example,  <br>\`\`factor=3\`\` means that only one third of the candidates are selected.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=factor,-int%20or%20float%2C%20default%3D3) | 2   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo random number generator state used for subsampling the dataset  <br>when \`resources != 'n\_samples'\`. Also used for random uniform  <br>sampling from lists of possible values instead of scipy.stats  <br>distributions.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | RandomState(M...0x7E1DF5B93940 |
|     | [n\_candidates n\_candidates: "exhaust" or int, default="exhaust"  <br>  <br>The number of candidate parameters to sample, at the first  <br>iteration. Using 'exhaust' will sample enough candidates so that the  <br>last iteration uses as many resources as possible, based on  <br>\`min\_resources\`, \`max\_resources\` and \`factor\`. In this case,  <br>\`min\_resources\` cannot be 'exhaust'.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_candidates,-%22exhaust%22%20or%20int%2C%20default%3D%22exhaust%22) | 'exhaust' |
|     | [resource resource: \`\`'n\_samples'\`\` or str, default='n\_samples'  <br>  <br>Defines the resource that increases with each iteration. By default,  <br>the resource is the number of samples. It can also be set to any  <br>parameter of the base estimator that accepts positive integer  <br>values, e.g. 'n\_iterations' or 'n\_estimators' for a gradient  <br>boosting estimator. In this case \`\`max\_resources\`\` cannot be 'auto'  <br>and must be set explicitly.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=resource,-%27n_samples%27%20or%20str%2C%20default%3D%27n_samples%27) | 'n\_samples' |
|     | [max\_resources max\_resources: int, default='auto'  <br>  <br>The maximum number of resources that any candidate is allowed to use  <br>for a given iteration. By default, this is set \`\`n\_samples\`\` when  <br>\`\`resource='n\_samples'\`\` (default), else an error is raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=max_resources,-int%2C%20default%3D%27auto%27) | 'auto' |
|     | [min\_resources min\_resources: {'exhaust', 'smallest'} or int, default='smallest'  <br>  <br>The minimum amount of resource that any candidate is allowed to use  <br>for a given iteration. Equivalently, this defines the amount of  <br>resources \`r0\` that are allocated for each candidate at the first  <br>iteration.  <br>  <br>\- 'smallest' is a heuristic that sets \`r0\` to a small value:  <br>  <br>\- \`\`n\_splits \* 2\`\` when \`\`resource='n\_samples'\`\` for a regression problem  <br>\- \`\`n\_classes \* n\_splits \* 2\`\` when \`\`resource='n\_samples'\`\` for a  <br>classification problem  <br>\- \`\`1\`\` when \`\`resource != 'n\_samples'\`\`  <br>  <br>\- 'exhaust' will set \`r0\` such that the \*\*last\*\* iteration uses as  <br>much resources as possible. Namely, the last iteration will use the  <br>highest value smaller than \`\`max\_resources\`\` that is a multiple of  <br>both \`\`min\_resources\`\` and \`\`factor\`\`. In general, using 'exhaust'  <br>leads to a more accurate estimator, but is slightly more time  <br>consuming. 'exhaust' isn't available when \`n\_candidates='exhaust'\`.  <br>  <br>Note that the amount of resources used at each iteration is always a  <br>multiple of \`\`min\_resources\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=min_resources,-%7B%27exhaust%27%2C%20%27smallest%27%7D%20or%20int%2C%20default%3D%27smallest%27) | 'smallest' |
|     | [aggressive\_elimination aggressive\_elimination: bool, default=False  <br>  <br>This is only relevant in cases where there isn't enough resources to  <br>reduce the remaining candidates to at most \`factor\` after the last  <br>iteration. If \`\`True\`\`, then the search process will 'replay' the  <br>first iteration for as long as needed until the number of candidates  <br>is small enough. This is \`\`False\`\` by default, which means that the  <br>last iteration may evaluate more than \`\`factor\`\` candidates. See  <br>:ref:\`aggressive\_elimination\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=aggressive_elimination,-bool%2C%20default%3DFalse) | False |
|     | [cv cv: int, cross-validation generator or an iterable, default=5  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. note::  <br>Due to implementation details, the folds produced by \`cv\` must be  <br>the same across multiple calls to \`cv.split()\`. For  <br>built-in \`scikit-learn\` iterators, this can be achieved by  <br>deactivating shuffling (\`shuffle=False\`), or by setting the  <br>\`cv\`'s \`random\_state\` parameter to an integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3D5) | 5   |
|     | [scoring scoring: str or callable, default=None  <br>  <br>Scoring method to use to evaluate the predictions on the test set.  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=scoring,-str%20or%20callable%2C%20default%3DNone) | None |
|     | [refit refit: bool or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`HalvingRandomSearchCV\`\` instance.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=refit,-bool%20or%20callable%2C%20default%3DTrue) | True |
|     | [error\_score error\_score: 'raise' or numeric  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error. Default is \`\`np.nan\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=True  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DTrue) | True |
|     | [n\_jobs n\_jobs: int or None, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_jobs,-int%20or%20None%2C%20default%3DNone) | None |
|     | [verbose verbose: int  <br>  <br>Controls the verbosity: the higher, the more messages.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=verbose,-int) | 0   |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator or dict  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data, in the last halving iteration.  <br>Not available if \`\`refit=False\`\`.  <br>  <br>.. note::  <br>\`\`best\_estimator\_\`\` reflects the winner of the final iteration  <br>only. \`\`cv\_results\_\`\` may contain candidates with a higher  <br>\`\`rank\_test\_score\`\`, but those scores were obtained with fewer  <br>resources and are less reliable. To inspect final-iteration results  <br>explicitly, filter \`\`cv\_results\_\`\` by  <br>\`\`cv\_results\_\['iter'\] == n\_iterations\_ - 1\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=best_estimator_,-estimator%20or%20dict) | RandomForestClassifier | RandomForestC...x7E1D96201D40) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(39) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data in  <br>the last halving iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=best_params_,-dict) | dict | {'bo...ap': False, 'cr...on': 'entropy', 'ma...th': None, 'ma...es': 4, ...} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the \`\`best\_estimator\_\`\`, computed over  <br>the candidates from the last halving iteration only.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=best_score_,-float) | float64 | 0.8875 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`. It contains lots of information  <br>for analysing the results of a search.  <br>Please refer to the :ref:\`User guide<successive\_halving\_cv\_results>\`  <br>for details.  <br>For an example of analysing \`\`cv\_results\_\`\`,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'iter': array(\[0, 0, ..., 3, 3, 4, 4\]), 'me...me': array(\[0.02, ..., 0.02, 0.03\]), 'me...me': array(\[0., 0...., 0., 0., 0.\]), 'me...re': array(\[0.65, ..., 0.88, 0.89\]), ...} |
| [max\_resources\_ max\_resources\_: int  <br>  <br>The maximum number of resources that any candidate is allowed to use  <br>for a given iteration. Note that since the number of resources used at  <br>each iteration must be a multiple of \`\`min\_resources\_\`\`, the actual  <br>number of resources used at the last iteration may be smaller than  <br>\`\`max\_resources\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=max_resources_,-int) | int | 400 |
| [min\_resources\_ min\_resources\_: int  <br>  <br>The amount of resources that are allocated for each candidate at the  <br>first iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=min_resources_,-int) | int | 20  |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_candidates\_ n\_candidates\_: list of int  <br>  <br>The number of candidate parameters that were evaluated at each  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_candidates_,-list%20of%20int) | list | \[20, 10, 5, 3, ...\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_features_in_,-int) | int | 12  |
| [n\_iterations\_ n\_iterations\_: int  <br>  <br>The actual number of iterations that were run. This is equal to  <br>\`\`n\_required\_iterations\_\`\` if \`\`aggressive\_elimination\`\` is \`\`True\`\`.  <br>Else, this is equal to \`\`min(n\_possible\_iterations\_,  <br>n\_required\_iterations\_)\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_iterations_,-int) | int | 5   |
| [n\_possible\_iterations\_ n\_possible\_iterations\_: int  <br>  <br>The number of iterations that are possible starting with  <br>\`\`min\_resources\_\`\` resources and without exceeding  <br>\`\`max\_resources\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_possible_iterations_,-int) | int | 5   |
| [n\_remaining\_candidates\_ n\_remaining\_candidates\_: int  <br>  <br>The number of candidate parameters that are left after the last  <br>iteration. It corresponds to \`ceil(n\_candidates\[-1\] / factor)\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_remaining_candidates_,-int) | int | 1   |
| [n\_required\_iterations\_ n\_required\_iterations\_: int  <br>  <br>The number of iterations that are required to end up with less than  <br>\`\`factor\`\` candidates at the last iteration, starting with  <br>\`\`min\_resources\_\`\` resources. This will be smaller than  <br>\`\`n\_possible\_iterations\_\`\` when there isn't enough resources.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_required_iterations_,-int) | int | 5   |
| [n\_resources\_ n\_resources\_: list of int  <br>  <br>The amount of resources used at each iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_resources_,-list%20of%20int) | list | \[20, 40, 80, 160, ...\] |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=refit_time_,-float) | float | 0.03565 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | \_PassthroughScorer | RandomForestClassifier.score |

best\_estimator\_: RandomForestClassifier

RandomForestClassifier(bootstrap=False, criterion='entropy', max\_features=4,
                       min\_samples\_split=5, n\_estimators=20,
                       random\_state=RandomState(MT19937) at 0x7E1D96201D40)

RandomForestClassifier

[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 20  |
|     | [criterion criterion: {"gini", "entropy", "log\_loss"}, default="gini"  <br>  <br>The function to measure the quality of a split. Supported criteria are  <br>"gini" for the Gini impurity and "log\_loss" and "entropy" both for the  <br>Shannon information gain, see :ref:\`tree\_mathematical\_formulation\`.  <br>Note: This parameter is tree-specific.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'entropy' |
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 5   |
|     | [max\_features max\_features: {"sqrt", "log2", None}, int or float, default="sqrt"  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>.. versionchanged:: 1.1  <br>The default of \`max\_features\` changed from \`"auto"\` to \`"sqrt"\`.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D%22sqrt%22) | 4   |
|     | [bootstrap bootstrap: bool, default=True  <br>  <br>Whether bootstrap samples are used when building trees. If False, the  <br>whole dataset is used to build each tree.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | False |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | RandomState(M...0x7E1D96201D40 |
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |
|     | [oob\_score oob\_score: bool or callable, default=False  <br>  <br>Whether to use out-of-bag samples to estimate the generalization score.  <br>By default, :func:\`~sklearn.metrics.accuracy\_score\` is used.  <br>Provide a callable with signature \`metric(y\_true, y\_pred)\` to use a  <br>custom metric. Only available if \`bootstrap=True\`.  <br>  <br>For an illustration of out-of-bag (OOB) error estimation, see the example  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_ensemble\_oob.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`predict\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,) or a list of such arrays  <br>  <br>The classes labels (single output problem), or a list of arrays of  <br>class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20a%20list%20of%20such%20arrays) | ndarray\[int64\](2,) | \[0,1\] |
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeClassifier\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeClassifier) | DecisionTreeClassifier | DecisionTreeClassifier() |
| [estimators\_ estimators\_: list of DecisionTreeClassifier  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_,-list%20of%20DecisionTreeClassifier) | list | \[DecisionTreeC...ate=214286498), DecisionTreeC...ate=631739714), DecisionTreeC...te=1554730159), DecisionTreeC...tate=25323325), ...\] |
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[ 0, ..., dtype=int32), array(\[ 0, ..., dtype=int32), array(\[ 0, ..., dtype=int32), array(\[ 0, ..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](12,) | \[0.15,0.22,0.02,...,0.02,0.02,0.02\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 2   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 12  |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
We can now use the `cv_results_` attribute of the search estimator to inspect and plot the evolution of the search.\
\
results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(rsh.cv\_results\_)\
results\["params\_str"\] \= results.params.apply(str)\
results.drop\_duplicates(subset\=("params\_str", "iter"), inplace\=True)\
mean\_scores \= results.pivot(\
    index\="iter", columns\="params\_str", values\="mean\_test\_score"\
)\
ax \= mean\_scores.plot(legend\=False, alpha\=0.6)\
\
labels \= \[\
    f"iter={i}\\nn\_samples={rsh.n\_resources\_\[i\]}\\nn\_candidates={rsh.n\_candidates\_\[i\]}"\
    for i in range(rsh.n\_iterations\_)\
\]\
\
ax.set\_xticks(range(rsh.n\_iterations\_))\
ax.set\_xticklabels(labels, rotation\=45, multialignment\="left")\
ax.set\_title("Scores of candidates over iterations")\
ax.set\_ylabel("mean test score", fontsize\=15)\
ax.set\_xlabel("iterations", fontsize\=15)\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![Scores of candidates over iterations](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_iterations_001.png)\
\
Number of candidates and amount of resource at each iteration[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html#number-of-candidates-and-amount-of-resource-at-each-iteration "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
At the first iteration, a small amount of resources is used. The resource here is the number of samples that the estimators are trained on. All candidates are evaluated.\
\
At the second iteration, only the best half of the candidates is evaluated. The number of allocated resources is doubled: candidates are evaluated on twice as many samples.\
\
This process is repeated until the last iteration, where only 2 candidates are left. The best candidate is the candidate that has the best score at the last iteration.\
\
**Total running time of the script:** (0 minutes 5.886 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_successive_halving_iterations.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_successive_halving_iterations.ipynb)\
\
[`Download Jupyter notebook: plot_successive_halving_iterations.ipynb`](https://scikit-learn.org/stable/_downloads/23fb33f64b3c23edf25165a3a4f04237/plot_successive_halving_iterations.ipynb)\
\
[`Download Python source code: plot_successive_halving_iterations.py`](https://scikit-learn.org/stable/_downloads/49fae0b4f6ab58738dcbf62236756548/plot_successive_halving_iterations.py)\
\
[`Download zipped: plot_successive_halving_iterations.zip`](https://scikit-learn.org/stable/_downloads/20f62896d2f883bba3587708f3e8a82a/plot_successive_halving_iterations.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_randomized_search_thumb.png)\
\
[Comparing randomized search and grid search for hyperparameter estimation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html)\
\
Comparing randomized search and grid search for hyperparameter estimation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)\
\
Release Highlights for scikit-learn 0.24\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)\
\
[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)\
\
Comparison between grid search and successive halving\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)\
\
[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)\
\
Analysis of the convergence of penalized logistic regression models\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/49fae0b4f6ab58738dcbf62236756548/plot_successive_halving_iterations.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/23fb33f64b3c23edf25165a3a4f04237/plot_successive_halving_iterations.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/20f62896d2f883bba3587708f3e8a82a/plot_successive_halving_iterations.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_successive_halving_iterations.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_successive_halving_iterations.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)