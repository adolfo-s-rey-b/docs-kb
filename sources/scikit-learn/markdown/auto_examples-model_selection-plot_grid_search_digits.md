[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_grid_search_digits.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_grid_search_digits.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_grid_search_digits.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_grid_search_digits.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_grid_search_digits.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_grid_search_digits.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#sphx-glr-download-auto-examples-model-selection-plot-grid-search-digits-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Custom refit strategy of a grid search with cross-validation[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#custom-refit-strategy-of-a-grid-search-with-cross-validation "Link to this heading")

================================================================================================================================================================================================================================================

This examples shows how a classifier is optimized by cross-validation, which is done using the [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 object on a development set that comprises only half of the available labeled data.

The performance of the selected hyper-parameters and trained model is then measured on a dedicated evaluation set that was not used during the model selection step.

More details on tools available for model selection can be found in the sections on [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 and [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

The dataset[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#the-dataset "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

We will work with the `digits` dataset. The goal is to classify handwritten digits images. We transform the problem into a binary classification for easier understanding: the goal is to identify whether a digit is `8` or not.

from sklearn import datasets

digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()

Copy to clipboard

In order to train a classifier on images, we need to flatten them into vectors. Each image of 8 by 8 pixels needs to be transformed to a vector of 64 pixels. Thus, we will get a final data array of shape `(n_images, n_pixels)`.

n\_samples \= len(digits.images)
X \= digits.images.reshape((n\_samples, \-1))
y \= digits.target \== 8
print(
    f"The number of images is {X.shape\[0\]} and each image contains {X.shape\[1\]} pixels"
)

Copy to clipboard

The number of images is 1797 and each image contains 64 pixels

Copy to clipboard

As presented in the introduction, the data will be split into a training and a testing set of equal size.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.5, random\_state\=0)

Copy to clipboard

Define our grid-search strategy[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#define-our-grid-search-strategy "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will select a classifier by searching the best hyper-parameters on folds of the training set. To do this, we need to define the scores to select the best candidate.

scores \= \["precision", "recall"\]

Copy to clipboard

We can also define a function to be passed to the `refit` parameter of the [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 instance. It will implement the custom strategy to select the best candidate from the `cv_results_` attribute of the [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
. Once the candidate is selected, it is automatically refitted by the [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 instance.

Here, the strategy is to short-list the models which are the best in terms of precision and recall. From the selected models, we finally select the fastest model at predicting. Notice that these custom choices are completely arbitrary.

import pandas as pd

def print\_dataframe(filtered\_cv\_results):
    """Pretty print for filtered dataframe"""
    for mean\_precision, std\_precision, mean\_recall, std\_recall, params in zip(
        filtered\_cv\_results\["mean\_test\_precision"\],
        filtered\_cv\_results\["std\_test\_precision"\],
        filtered\_cv\_results\["mean\_test\_recall"\],
        filtered\_cv\_results\["std\_test\_recall"\],
        filtered\_cv\_results\["params"\],
    ):
        print(
            f"precision: {mean\_precision:0.3f} (±{std\_precision:0.03f}),"
            f" recall: {mean\_recall:0.3f} (±{std\_recall:0.03f}),"
            f" for {params}"
        )
    print()

def refit\_strategy(cv\_results):
    """Define the strategy to select the best estimator.

    The strategy defined here is to filter-out all results below a precision threshold
    of 0.98, rank the remaining by recall and keep all models with one standard
    deviation of the best by recall. Once these models are selected, we can select the
    fastest model to predict.

    Parameters
    ----------
    cv\_results : dict of numpy (masked) ndarrays
        CV results as returned by the \`GridSearchCV\`.

    Returns
    -------
    best\_index : int
        The index of the best estimator as it appears in \`cv\_results\`.
    """
    \# print the info about the grid-search for the different scores
    precision\_threshold \= 0.98

    cv\_results\_ \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(cv\_results)
    print("All grid-search results:")
    print\_dataframe(cv\_results\_)

    \# Filter-out all results below the threshold
    high\_precision\_cv\_results \= cv\_results\_\[\
        cv\_results\_\["mean\_test\_precision"\] \> precision\_threshold\
    \]

    print(f"Models with a precision higher than {precision\_threshold}:")
    print\_dataframe(high\_precision\_cv\_results)

    high\_precision\_cv\_results \= high\_precision\_cv\_results\[\
        \[\
            "mean\_score\_time",\
            "mean\_test\_recall",\
            "std\_test\_recall",\
            "mean\_test\_precision",\
            "std\_test\_precision",\
            "rank\_test\_recall",\
            "rank\_test\_precision",\
            "params",\
        \]\
    \]

    \# Select the most performant models in terms of recall
    \# (within 1 sigma from the best)
    best\_recall\_std \= high\_precision\_cv\_results\["mean\_test\_recall"\].std()
    best\_recall \= high\_precision\_cv\_results\["mean\_test\_recall"\].max()
    best\_recall\_threshold \= best\_recall \- best\_recall\_std

    high\_recall\_cv\_results \= high\_precision\_cv\_results\[\
        high\_precision\_cv\_results\["mean\_test\_recall"\] \> best\_recall\_threshold\
    \]
    print(
        "Out of the previously selected high precision models, we keep all the\\n"
        "the models within one standard deviation of the highest recall model:"
    )
    print\_dataframe(high\_recall\_cv\_results)

    \# From the best candidates, select the fastest model to predict
    fastest\_top\_recall\_high\_precision\_index \= high\_recall\_cv\_results\[\
        "mean\_score\_time"\
    \].idxmin()

    print(
        "\\nThe selected final model is the fastest to predict out of the previously\\n"
        "selected subset of best models based on precision and recall.\\n"
        "Its scoring time is:\\n\\n"
        f"{high\_recall\_cv\_results.loc\[fastest\_top\_recall\_high\_precision\_index\]}"
    )

    return fastest\_top\_recall\_high\_precision\_index

Copy to clipboard

Tuning hyper-parameters[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#tuning-hyper-parameters "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once we defined our strategy to select the best model, we define the values of the hyper-parameters and create the grid-search instance:

from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

tuned\_parameters \= \[\
    {"kernel": \["rbf"\], "gamma": \[1e-3, 1e-4\], "C": \[1, 10, 100, 1000\]},\
    {"kernel": \["linear"\], "C": \[1, 10, 100, 1000\]},\
\]

grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(
    [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(), tuned\_parameters, scoring\=scores, refit\=refit\_strategy
)
grid\_search.fit(X\_train, y\_train)

Copy to clipboard

All grid-search results:
precision: 1.000 (±0.000), recall: 0.854 (±0.063), for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.257 (±0.061), for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 0.968 (±0.039), recall: 0.780 (±0.083), for {'C': 10, 'gamma': 0.0001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 0.905 (±0.058), recall: 0.889 (±0.074), for {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 0.904 (±0.058), recall: 0.890 (±0.073), for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
precision: 0.695 (±0.073), recall: 0.743 (±0.065), for {'C': 1, 'kernel': 'linear'}
precision: 0.643 (±0.066), recall: 0.757 (±0.066), for {'C': 10, 'kernel': 'linear'}
precision: 0.611 (±0.028), recall: 0.744 (±0.044), for {'C': 100, 'kernel': 'linear'}
precision: 0.618 (±0.039), recall: 0.744 (±0.044), for {'C': 1000, 'kernel': 'linear'}

Models with a precision higher than 0.98:
precision: 1.000 (±0.000), recall: 0.854 (±0.063), for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.257 (±0.061), for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}

Out of the previously selected high precision models, we keep all the
the models within one standard deviation of the highest recall model:
precision: 1.000 (±0.000), recall: 0.854 (±0.063), for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
precision: 1.000 (±0.000), recall: 0.877 (±0.069), for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}


The selected final model is the fastest to predict out of the previously
selected subset of best models based on precision and recall.
Its scoring time is:

mean\_score\_time                                            0.005937
mean\_test\_recall                                           0.877206
std\_test\_recall                                            0.069196
mean\_test\_precision                                             1.0
std\_test\_precision                                              0.0
rank\_test\_recall                                                  3
rank\_test\_precision                                               1
params                 {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
Name: 6, dtype: object

Copy to clipboard

GridSearchCV(estimator=SVC(),
             param\_grid=\[{'C': \[1, 10, 100, 1000\], 'gamma': \[0.001, 0.0001\],\
                          'kernel': \['rbf'\]},\
                         {'C': \[1, 10, 100, 1000\], 'kernel': \['linear'\]}\],
             refit=<function refit\_strategy at 0x7e1dbc1f0670>,
             scoring=\['precision', 'recall'\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | SVC() |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | \[{'C': \[1, 10, ...\], 'gamma': \[0.001, 0.0001\], 'kernel': \['rbf'\]}, {'C': \[1, 10, ...\], 'kernel': \['linear'\]}\] |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | \['precision', 'recall'\] |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | <function ref...x7e1dbc1f0670> |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | SVC | SVC(C=1000, gamma=0.001) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(6) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'} |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[bool\](2,) | \[False, True\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.0072..., 1.3658988 \]), 'me...me': array(\[0.0059..., 0.00442386\]), 'me...on': array(\[1. ..., 0.61784765\]), 'me...ll': array(\[0.8536..., 0.74411765\]), ...} |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | True |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 64  |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 0.01022 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | dict | {'pr...on': make\_scorer(p...verage=binary), 'recall': make\_scorer(r...verage=binary)} |

best\_estimator\_: SVC

SVC(C=1000, gamma=0.001)

SVC

[?Documentation for SVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive. The penalty  <br>is a squared l2 penalty. For an intuitive visualization of the effects  <br>of scaling the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1000 |
|     | [gamma gamma: {'scale', 'auto'} or float, default='scale'  <br>  <br>Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.  <br>  <br>\- if \`\`gamma='scale'\`\` (default) is passed then it uses  <br>1 / (n\_features \* X.var()) as value of gamma,  <br>\- if 'auto', uses 1 / n\_features  <br>\- if float, must be non-negative.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`gamma\`\` changed from 'auto' to 'scale'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=gamma,-%7B%27scale%27%2C%20%27auto%27%7D%20or%20float%2C%20default%3D%27scale%27) | 0.001 |
|     | [kernel kernel: {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'} or callable, default='rbf'  <br>  <br>Specifies the kernel type to be used in the algorithm. If  <br>none is given, 'rbf' will be used. If a callable is given it is used to  <br>pre-compute the kernel matrix from data matrices; that matrix should be  <br>an array of shape \`\`(n\_samples, n\_samples)\`\`. For an intuitive  <br>visualization of different kernel types see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_kernels.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=kernel,-%7B%27linear%27%2C%20%27poly%27%2C%20%27rbf%27%2C%20%27sigmoid%27%2C%20%27precomputed%27%7D%20or%20callable%2C%20%20%20%20%20%20%20%20%20%20default%3D%27rbf%27) | 'rbf' |
|     | [degree degree: int, default=3  <br>  <br>Degree of the polynomial kernel function ('poly').  <br>Must be non-negative. Ignored by all other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=degree,-int%2C%20default%3D3) | 3   |
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
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>probability estimates. Ignored when \`probability\` is False.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [class\_weight\_ class\_weight\_: ndarray of shape (n\_classes,)  <br>  <br>Multipliers of parameter C for each class.  <br>Computed based on the \`\`class\_weight\`\` parameter.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=class_weight_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[float64\](2,) | \[1.,1.\] |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[bool\](2,) | \[False, True\] |
| [dual\_coef\_ dual\_coef\_: ndarray or sparse array/matrix of shape (n\_classes -1, n\_SV)  <br>  <br>Dual coefficients of the support vector in the decision  <br>function (see :ref:\`sgd\_mathematical\_formulation\`), multiplied by  <br>their targets.  <br>For multiclass, coefficient for all 1-vs-1 classifiers.  <br>The layout of the coefficients in the multiclass case is somewhat  <br>non-trivial. See the :ref:\`multi-class section of the User Guide  <br><svm\_multi\_class>\` for details.  <br>If \`X\` is sparse, these will also be sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=dual_coef_,-ndarray%20or%20sparse%20array/matrix%20of%20shape%20%28n_classes%20-1%2C%20n_SV%29) | ndarray\[float64\](1, 160) | \[\[-0.49,-1.07,-0.3 ,..., 3.09, 1.31, 1.14\]\] |
| [fit\_status\_ fit\_status\_: int  <br>  <br>0 if correctly fitted, 1 otherwise (will raise warning)](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=fit_status_,-int) | int | 0   |
| [intercept\_ intercept\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2,)  <br>  <br>Constants in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=intercept_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%2C%29) | ndarray\[float64\](1,) | \[-1.31\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_features_in_,-int) | int | 64  |
| [n\_iter\_ n\_iter\_: ndarray of shape (n\_classes \* (n\_classes - 1) // 2,)  <br>  <br>Number of iterations run by the optimization routine to fit the model.  <br>The shape of this attribute depends on the number of models optimized  <br>which in turn depends on the number of classes.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_iter_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20//%202%2C%29) | ndarray\[int32\](1,) | \[464\] |
| [n\_support\_ n\_support\_: ndarray of shape (n\_classes,), dtype=int32  <br>  <br>Number of support vectors for each class.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=n_support_,-ndarray%20of%20shape%20%28n_classes%2C%29%2C%20dtype%3Dint32) | ndarray\[int32\](2,) | \[110, 50\] |
| [probA\_ probA\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2)  <br>  <br>If \`probability=True\`, it corresponds to the parameters learned in  <br>Platt scaling to produce probability estimates from decision values.  <br>If \`probability=False\`, it's an empty array. Platt scaling uses the  <br>logistic function](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probA_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%29) | ndarray\[float64\](0,) | \[\] |
| [probB\_ probB\_: ndarray of shape (n\_classes \* (n\_classes - 1) / 2)  <br>  <br>If \`probability=True\`, it corresponds to the parameters learned in  <br>Platt scaling. Platt scaling uses the logistic function  <br>\`\`1 / (1 + exp(decision\_value \* probA\_ + probB\_))\`\`  <br>where \`\`probA\_\`\` and \`\`probB\_\`\` are learned from the dataset \[2\]\_. For  <br>more information on the multiclass case and training procedure see  <br>section 8 of \[1\]\_.  <br>  <br>.. deprecated:: 1.9  <br>The attributes \`probA\_\` and \`probB\_\` are deprecated in version 1.9 and will  <br>be removed in 1.11.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probB_,-ndarray%20of%20shape%20%28n_classes%20%2A%20%28n_classes%20-%201%29%20/%202%29) | ndarray\[float64\](0,) | \[\] |
| [shape\_fit\_ shape\_fit\_: tuple of int of shape (n\_dimensions\_of\_X,)  <br>  <br>Array dimensions of training vector \`\`X\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=shape_fit_,-tuple%20of%20int%20of%20shape%20%28n_dimensions_of_X%2C%29) | tuple | (898, 64) |
| [support\_ support\_: ndarray of shape (n\_SV)  <br>  <br>Indices of support vectors.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=support_,-ndarray%20of%20shape%20%28n_SV%29) | ndarray\[int32\](160,) | \[ 5, 6, 21,...,758,779,849\] |
| [support\_vectors\_ support\_vectors\_: ndarray or sparse array/matrix of shape (n\_SV, n\_features)  <br>  <br>Support vectors. An empty array if kernel is precomputed.  <br>If \`X\` is sparse, these will also be sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=support_vectors_,-ndarray%20or%20sparse%20array/matrix%20of%20shape%20%28n_SV%2C%20n_features%29) | ndarray\[float64\](160, 64) | \[\[ 0., 0., 0.,..., 2., 0., 0.\], \[ 0., 0., 0.,..., 0., 0., 0.\], \[ 0., 0., 2.,..., 0., 0., 0.\], ..., \[ 0., 0., 5.,...,16., 2., 0.\], \[ 0., 0., 2.,...,10., 0., 0.\], \[ 0., 0., 0.,...,11.,15., 2.\]\] |

  
  

The parameters selected by the grid-search with our custom strategy are:

grid\_search.best\_params\_

Copy to clipboard

{'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}

Copy to clipboard

Finally, we evaluate the fine-tuned model on the left-out evaluation set: the `grid_search` object **has automatically been refit** on the full training set with the parameters selected by our custom refit strategy.

We can use the classification report to compute standard classification metrics on the left-out set:

from sklearn.metrics import [classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")

y\_pred \= grid\_search.predict(X\_test)
print([classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(y\_test, y\_pred))

Copy to clipboard

              precision    recall  f1-score   support

       False       0.99      1.00      0.99       807
        True       1.00      0.87      0.93        92

    accuracy                           0.99       899
   macro avg       0.99      0.93      0.96       899
weighted avg       0.99      0.99      0.99       899

Copy to clipboard

Note

The problem is too easy: the hyperparameter plateau is too flat and the output model is the same for precision and recall with ties in quality.

**Total running time of the script:** (0 minutes 9.882 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_digits.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_digits.ipynb)

[`Download Jupyter notebook: plot_grid_search_digits.ipynb`](https://scikit-learn.org/stable/_downloads/f4a89bf823d814fee03a693df158d83a/plot_grid_search_digits.ipynb)

[`Download Python source code: plot_grid_search_digits.py`](https://scikit-learn.org/stable/_downloads/ffc6ef5575b0aa920abd7a8113265839/plot_grid_search_digits.py)

[`Download zipped: plot_grid_search_digits.zip`](https://scikit-learn.org/stable/_downloads/5f322361bcf53bfae6ef8f25492b6bbb/plot_grid_search_digits.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_randomized_search_thumb.png)

[Comparing randomized search and grid search for hyperparameter estimation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html)

Comparing randomized search and grid search for hyperparameter estimation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ffc6ef5575b0aa920abd7a8113265839/plot_grid_search_digits.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f4a89bf823d814fee03a693df158d83a/plot_grid_search_digits.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5f322361bcf53bfae6ef8f25492b6bbb/plot_grid_search_digits.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_grid_search_digits.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_grid_search_digits.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)