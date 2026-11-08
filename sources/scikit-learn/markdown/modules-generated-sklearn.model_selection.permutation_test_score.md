[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.permutation_test_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.permutation_test_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.permutation_test_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.permutation_test_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.permutation_test_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.permutation_test_score.html)

Collapse Sidebar Expand Sidebar

permutation\_test\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#permutation-test-score "Link to this heading")

=================================================================================================================================================================================

sklearn.model\_selection.permutation\_test\_score(_estimator_, _X_, _y_, _\*_, _groups\=None_, _cv\=None_, _n\_permutations\=100_, _n\_jobs\=None_, _random\_state\=0_, _verbose\=0_, _scoring\=None_, _params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_validation.py#L1461)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "Link to this definition")

Evaluate the significance of a cross-validated score with permutations.

Permutes targets to generate ‘randomized data’ and compute the empirical p-value against the null hypothesis that features and targets are independent.

The p-value represents the fraction of randomized data sets where the estimator performed as well or better than on the original data. A small p-value suggests that there is a real dependency between features and targets which has been used by the estimator to give good predictions. A large p-value may be due to lack of real dependency between features and targets or the estimator was not able to use the dependency to give good predictions.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#permutation-test-score)
.

Parameters:

**estimator**estimator object implementing ‘fit’

The object to use to fit the data.

**X**array-like of shape at least 2D

The data to fit.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs) or None

The target variable to try to predict in the case of supervised learning.

**groups**array-like of shape (n\_samples,), default=None

Labels to constrain permutation within groups, i.e. `y` values are permuted among samples with the same group identifier. When not specified, `y` values are permuted among all samples.

When a grouped cross-validator is used, the group labels are also passed on to the `split` method of the cross-validator. The cross-validator uses them for grouping the samples while splitting the dataset into train/test set.

Changed in version 1.6: `groups` can only be passed if metadata routing is not enabled via `sklearn.set_config(enable_metadata_routing=True)`. When routing is enabled, pass `groups` alongside other metadata via the `params` argument instead. E.g.: `permutation_test_score(..., params={'groups': groups})`.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   `None`, to use the default 5-fold cross validation,
    
*   int, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For `int`/`None` inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if `None` changed from 3-fold to 5-fold.

**n\_permutations**int, default=100

Number of times to permute `y`.

**n\_jobs**int, default=None

Number of jobs to run in parallel. Training the estimator and computing the cross-validated score are parallelized over the permutations. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance or None, default=0

Pass an int for reproducible output for permutation of `y` values among samples. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**verbose**int, default=0

The verbosity level.

**scoring**str or callable, default=None

Scoring method to use to evaluate the predictions on the validation set.

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`, which should return only a single value. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

**params**dict, default=None

Parameters to pass to the `fit` method of the estimator, the scorer and the cv splitter.

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` method of the estimator.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` method of the estimator, `cv` object and `scorer`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
     for more details.
    

Added in version 1.6.

Returns:

**score**float

The true score without permuting targets.

**permutation\_scores**array of shape (n\_permutations,)

The scores obtained for each permutations.

**pvalue**float

The p-value, which approximates the probability that the score would be obtained by chance. This is calculated as:

`(C + 1) / (n_permutations + 1)`

Where C is the number of permutations whose score >= the true score.

The best possible p-value is 1/(n\_permutations + 1), the worst is 1.0.

Notes

This function implements Test 1 in:

Ojala and Garriga. [Permutation Tests for Studying Classifier Performance](http://www.jmlr.org/papers/volume11/ojala10a/ojala10a.pdf)
. The Journal of Machine Learning Research (2010) vol. 11

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.model\_selection import permutation\_test\_score
\>>> X, y \= make\_classification(random\_state\=0)
\>>> estimator \= LogisticRegression()
\>>> score, permutation\_scores, pvalue \= permutation\_test\_score(
...     estimator, X, y, random\_state\=0
... )
\>>> print(f"Original Score: {score:.3f}")
Original Score: 0.810
\>>> print(
...     f"Permutation Scores: {permutation\_scores.mean():.3f} +/- "
...     f"{permutation\_scores.std():.3f}"
... )
Permutation Scores: 0.505 +/- 0.057
\>>> print(f"P-value: {pvalue:.3f}")
P-value: 0.010

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_thumb.png)

[Test with permutations the significance of a classification score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Test with permutations the significance of a classification score

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)