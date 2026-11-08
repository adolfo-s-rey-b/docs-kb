[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.cross_val_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.cross_val_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.cross_val_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.cross_val_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.cross_val_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.cross_val_score.html)

Collapse Sidebar Expand Sidebar

cross\_val\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#cross-val-score "Link to this heading")

============================================================================================================================================================

sklearn.model\_selection.cross\_val\_score(_estimator_, _X_, _y\=None_, _\*_, _groups\=None_, _scoring\=None_, _cv\=None_, _n\_jobs\=None_, _verbose\=0_, _params\=None_, _pre\_dispatch\='2\*n\_jobs'_, _error\_score\=nan_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_validation.py#L496)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "Link to this definition")

Evaluate a score by cross-validation.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
.

Parameters:

**estimator**estimator object implementing ‘fit’

The object to use to fit the data.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to fit. Can be for example a list, or an array.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

The target variable to try to predict in the case of supervised learning.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. Only used in conjunction with a “Group” [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 instance (e.g., [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
).

Changed in version 1.4: `groups` can only be passed if metadata routing is not enabled via `sklearn.set_config(enable_metadata_routing=True)`. When routing is enabled, pass `groups` alongside other metadata via the `params` argument instead. E.g.: `cross_val_score(..., params={'groups': groups})`.

**scoring**str or callable, default=None

Strategy to evaluate the performance of the `estimator` across cross-validation splits.

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`, which should return only a single value. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

Similar to the use of `scoring` in [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 but only a single metric is permitted.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   `None`, to use the default 5-fold cross validation,
    
*   int, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   An iterable that generates (train, test) splits as arrays of indices.
    

For `int`/`None` inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if `None` changed from 3-fold to 5-fold.

**n\_jobs**int, default=None

Number of jobs to run in parallel. Training the estimator and computing the score are parallelized over the cross-validation splits. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int, default=0

The verbosity level.

**params**dict, default=None

Parameters to pass to the underlying estimator’s `fit`, the scorer, and the CV splitter.

Added in version 1.4.

**pre\_dispatch**int or str, default=’2\*n\_jobs’

Controls the number of jobs that get dispatched during parallel execution. Reducing this number can be useful to avoid an explosion of memory consumption when more jobs get dispatched than CPUs can process. This parameter can be:

*   `None`, in which case all the jobs are immediately created and spawned. Use this for lightweight and fast-running jobs, to avoid delays due to on-demand spawning of the jobs
    
*   An int, giving the exact number of total jobs that are spawned
    
*   A str, giving an expression as a function of n\_jobs, as in ‘2\*n\_jobs’
    

**error\_score**‘raise’ or numeric, default=np.nan

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised.

Added in version 0.20.

Returns:

**scores**ndarray of float of shape=(len(list(cv)),)

Array of scores of the estimator for each run of the cross validation.

See also

[`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

To run cross-validation on multiple metrics and also to return train scores, fit times and score times.

[`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")

Get predictions from each split of cross-validation for diagnostic purposes.

[`sklearn.metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")

Make a scorer from a performance metric or loss function.

Examples

\>>> from sklearn import datasets, linear\_model
\>>> from sklearn.model\_selection import cross\_val\_score
\>>> diabetes \= datasets.load\_diabetes()
\>>> X \= diabetes.data\[:150\]
\>>> y \= diabetes.target\[:150\]
\>>> lasso \= linear\_model.Lasso()
\>>> print(cross\_val\_score(lasso, X, y, cv\=3))
\[0.3315057  0.08022103 0.03531816\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_thumb.png)

[Model selection with Probabilistic PCA and Factor Analysis (FA)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)

Model selection with Probabilistic PCA and Factor Analysis (FA)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_thumb.png)

[Nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Nested versus non-nested cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_underfitting_overfitting_thumb.png)

[Underfitting vs. Overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)

Underfitting vs. Overfitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)