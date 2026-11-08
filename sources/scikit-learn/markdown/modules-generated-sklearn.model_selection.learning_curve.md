[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.learning_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.learning_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.learning_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.learning_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.learning_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.learning_curve.html)

Collapse Sidebar Expand Sidebar

learning\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#learning-curve "Link to this heading")

========================================================================================================================================================

sklearn.model\_selection.learning\_curve(_estimator_, _X_, _y_, _\*_, _groups\=None_, _train\_sizes\=array(\[0.1, 0.33, 0.55, 0.78, 1.\])_, _cv\=None_, _scoring\=None_, _exploit\_incremental\_learning\=False_, _n\_jobs\=None_, _pre\_dispatch\='all'_, _verbose\=0_, _shuffle\=False_, _random\_state\=None_, _error\_score\=nan_, _return\_times\=False_, _params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_validation.py#L1755)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "Link to this definition")

Learning curve.

Determines cross-validated training and test scores for different training set sizes.

A cross-validation generator splits the whole dataset k times in training and test data. Subsets of the training set with varying sizes will be used to train the estimator and a score for each training subset size and the test set will be computed. Afterwards, the scores will be averaged over all k runs for each training subset size.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve)
.

Parameters:

**estimator**object type that implements the “fit” method

An object of that type which is cloned for each validation. It must also implement “predict” unless `scoring` is a callable that doesn’t rely on “predict” to compute a score.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs) or None

Target relative to X for classification or regression; None for unsupervised learning.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. Only used in conjunction with a “Group” [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 instance (e.g., [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
).

Changed in version 1.6: `groups` can only be passed if metadata routing is not enabled via `sklearn.set_config(enable_metadata_routing=True)`. When routing is enabled, pass `groups` alongside other metadata via the `params` argument instead. E.g.: `learning_curve(..., params={'groups': groups})`.

**train\_sizes**array-like of shape (n\_ticks,), default=np.linspace(0.1, 1.0, 5)

Relative or absolute numbers of training examples that will be used to generate the learning curve. If the dtype is float, it is regarded as a fraction of the maximum size of the training set (that is determined by the selected validation method), i.e. it has to be within (0, 1\]. Otherwise it is interpreted as absolute sizes of the training sets. Note that for classification the number of samples usually has to be big enough to contain at least one sample from each class.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross validation,
    
*   int, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For int/None inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**scoring**str or callable, default=None

Scoring method to use to evaluate the training and test sets.

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

**exploit\_incremental\_learning**bool, default=False

If the estimator supports incremental learning, this will be used to speed up fitting for different training set sizes.

**n\_jobs**int, default=None

Number of jobs to run in parallel. Training the estimator and computing the score are parallelized over the different training and test sets. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**pre\_dispatch**int or str, default=’all’

Number of predispatched jobs for parallel execution (default is all). The option can reduce the allocated memory. The str can be an expression like ‘2\*n\_jobs’.

**verbose**int, default=0

Controls the verbosity: the higher, the more messages.

**shuffle**bool, default=False

Whether to shuffle training data before taking prefixes of it based on\`\`train\_sizes\`\`.

**random\_state**int, RandomState instance or None, default=None

Used when `shuffle` is True. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**error\_score**‘raise’ or numeric, default=np.nan

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised.

Added in version 0.20.

**return\_times**bool, default=False

Whether to return the fit and score times.

**params**dict, default=None

Parameters to pass to the `fit` method of the estimator and to the scorer.

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` method of the estimator.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` method of the estimator. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
     for more details.
    

Added in version 1.6.

Returns:

**train\_sizes\_abs**array of shape (n\_unique\_ticks,)

Numbers of training examples that has been used to generate the learning curve. Note that the number of ticks might be less than n\_ticks because duplicate entries will be removed.

**train\_scores**array of shape (n\_ticks, n\_cv\_folds)

Scores on training sets.

**test\_scores**array of shape (n\_ticks, n\_cv\_folds)

Scores on test set.

**fit\_times**array of shape (n\_ticks, n\_cv\_folds)

Times spent for fitting in seconds. Only present if `return_times` is True.

**score\_times**array of shape (n\_ticks, n\_cv\_folds)

Times spent for scoring in seconds. Only present if `return_times` is True.

See also

[`LearningCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "sklearn.model_selection.LearningCurveDisplay.from_estimator")

Plot a learning curve using an estimator and data.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> from sklearn.model\_selection import learning\_curve
\>>> X, y \= make\_classification(n\_samples\=100, n\_features\=10, random\_state\=42)
\>>> tree \= DecisionTreeClassifier(max\_depth\=4, random\_state\=42)
\>>> train\_size\_abs, train\_scores, test\_scores \= learning\_curve(
...     tree, X, y, train\_sizes\=\[0.3, 0.6, 0.9\]
... )
\>>> for train\_size, cv\_train\_scores, cv\_test\_scores in zip(
...     train\_size\_abs, train\_scores, test\_scores
... ):
...     print(f"{train\_size} samples were used to train the model")
...     print(f"The average train accuracy is {cv\_train\_scores.mean():.2f}")
...     print(f"The average test accuracy is {cv\_test\_scores.mean():.2f}")
24 samples were used to train the model
The average train accuracy is 1.00
The average test accuracy is 0.85
48 samples were used to train the model
The average train accuracy is 1.00
The average test accuracy is 0.90
72 samples were used to train the model
The average train accuracy is 1.00
The average test accuracy is 0.93

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_learning_curve_thumb.png)

[Plotting Learning Curves and Checking Models’ Scalability](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html)

Plotting Learning Curves and Checking Models' Scalability

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)