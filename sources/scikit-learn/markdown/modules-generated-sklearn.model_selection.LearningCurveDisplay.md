[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.LearningCurveDisplay.html)

Collapse Sidebar Expand Sidebar

LearningCurveDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#learningcurvedisplay "Link to this heading")

=========================================================================================================================================================================

class sklearn.model\_selection.LearningCurveDisplay(_\*_, _train\_sizes_, _train\_scores_, _test\_scores_, _score\_name\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_plot.py#L126)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "Link to this definition")

Learning Curve visualization.

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "sklearn.model_selection.LearningCurveDisplay.from_estimator")
 to create a [`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")
 instance. All parameters are stored as attributes.

Read more in the [User Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
 for general information about the visualization API and [detailed documentation](https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve)
 regarding the learning curve visualization.

Added in version 1.2.

Parameters:

**train\_sizes**ndarray of shape (n\_unique\_ticks,)

Numbers of training examples that has been used to generate the learning curve.

**train\_scores**ndarray of shape (n\_ticks, n\_cv\_folds)

Scores on training sets.

**test\_scores**ndarray of shape (n\_ticks, n\_cv\_folds)

Scores on test set.

**score\_name**str, default=None

The name of the score used in `learning_curve`. It will override the name inferred from the `scoring` parameter. If `score` is `None`, we use `"Score"` if `negate_score` is `False` and `"Negative score"` otherwise. If `scoring` is a string or a callable, we infer the name. We replace `_` by spaces and capitalize the first letter. We remove `neg_` and replace it by `"Negative"` if `negate_score` is `False` or just remove it otherwise.

Attributes:

**ax\_**matplotlib Axes

Axes with the learning curve.

**figure\_**matplotlib Figure

Figure containing the learning curve.

**errorbar\_**list of matplotlib Artist or None

When the `std_display_style` is `"errorbar"`, this is a list of `matplotlib.container.ErrorbarContainer` objects. If another style is used, `errorbar_` is `None`.

**lines\_**list of matplotlib Artist or None

When the `std_display_style` is `"fill_between"`, this is a list of `matplotlib.lines.Line2D` objects corresponding to the mean train and test scores. If another style is used, `line_` is `None`.

**fill\_between\_**list of matplotlib Artist or None

When the `std_display_style` is `"fill_between"`, this is a list of `matplotlib.collections.PolyCollection` objects. If another style is used, `fill_between_` is `None`.

See also

[`sklearn.model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")

Compute the learning curve.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.model\_selection import LearningCurveDisplay, learning\_curve
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> tree \= DecisionTreeClassifier(random\_state\=0)
\>>> train\_sizes, train\_scores, test\_scores \= learning\_curve(
...     tree, X, y)
\>>> display \= LearningCurveDisplay(train\_sizes\=train\_sizes,
...     train\_scores\=train\_scores, test\_scores\=test\_scores, score\_name\="Score")
\>>> display.plot()
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-model_selection-LearningCurveDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-model_selection-LearningCurveDisplay-1.png)

classmethod from\_estimator(_estimator_, _X_, _y_, _\*_, _groups\=None_, _train\_sizes\=array(\[0.1, 0.33, 0.55, 0.78, 1.\])_, _cv\=None_, _scoring\=None_, _exploit\_incremental\_learning\=False_, _n\_jobs\=None_, _pre\_dispatch\='all'_, _verbose\=0_, _shuffle\=False_, _random\_state\=None_, _error\_score\=nan_, _fit\_params\=None_, _ax\=None_, _negate\_score\=False_, _score\_name\=None_, _score\_type\='both'_, _std\_display\_style\='fill\_between'_, _line\_kw\=None_, _fill\_between\_kw\=None_, _errorbar\_kw\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_plot.py#L286)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "Link to this definition")

Create a learning curve display from an estimator.

Read more in the [User Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
 for general information about the visualization API and [detailed documentation](https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve)
 regarding the learning curve visualization.

Parameters:

**estimator**object type that implements the “fit” and “predict” methods

An object of that type which is cloned for each validation.

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs) or None

Target relative to X for classification or regression; None for unsupervised learning.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. Only used in conjunction with a “Group” [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 instance (e.g., [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
).

**train\_sizes**array-like of shape (n\_ticks,), default=np.linspace(0.1, 1.0, 5)

Relative or absolute numbers of training examples that will be used to generate the learning curve. If the dtype is float, it is regarded as a fraction of the maximum size of the training set (that is determined by the selected validation method), i.e. it has to be within (0, 1\]. Otherwise it is interpreted as absolute sizes of the training sets. Note that for classification the number of samples usually have to be big enough to contain at least one sample from each class.

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

**scoring**str or callable, default=None

The scoring method to use when calculating the learning curve. Options:

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

Whether to shuffle training data before taking prefixes of it based on\`train\_sizes\`.

**random\_state**int, RandomState instance or None, default=None

Used when `shuffle` is True. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**error\_score**‘raise’ or numeric, default=np.nan

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised.

**fit\_params**dict, default=None

Parameters to pass to the fit method of the estimator.

**ax**matplotlib Axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**negate\_score**bool, default=False

Whether or not to negate the scores obtained through [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
. This is particularly useful when using the error denoted by `neg_*` in `scikit-learn`.

**score\_name**str, default=None

The name of the score used to decorate the y-axis of the plot. It will override the name inferred from the `scoring` parameter. If `score` is `None`, we use `"Score"` if `negate_score` is `False` and `"Negative score"` otherwise. If `scoring` is a string or a callable, we infer the name. We replace `_` by spaces and capitalize the first letter. We remove `neg_` and replace it by `"Negative"` if `negate_score` is `False` or just remove it otherwise.

**score\_type**{“test”, “train”, “both”}, default=”both”

The type of score to plot. Can be one of `"test"`, `"train"`, or `"both"`.

**std\_display\_style**{“errorbar”, “fill\_between”} or None, default=”fill\_between”

The style used to display the score standard deviation around the mean score. If `None`, no representation of the standard deviation is displayed.

**line\_kw**dict, default=None

Additional keyword arguments passed to the `plt.plot` used to draw the mean score.

**fill\_between\_kw**dict, default=None

Additional keyword arguments passed to the `plt.fill_between` used to draw the score standard deviation.

**errorbar\_kw**dict, default=None

Additional keyword arguments passed to the `plt.errorbar` used to draw mean score and standard deviation score.

Returns:

**display**[`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")

Object that stores computed values.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.model\_selection import LearningCurveDisplay
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> tree \= DecisionTreeClassifier(random\_state\=0)
\>>> LearningCurveDisplay.from\_estimator(tree, X, y)
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-model_selection-LearningCurveDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-model_selection-LearningCurveDisplay-2.png)

plot(_ax\=None_, _\*_, _negate\_score\=False_, _score\_name\=None_, _score\_type\='both'_, _std\_display\_style\='fill\_between'_, _line\_kw\=None_, _fill\_between\_kw\=None_, _errorbar\_kw\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_plot.py#L211)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.plot "Link to this definition")

Plot visualization.

Parameters:

**ax**matplotlib Axes, default=None

Axes object to plot on. If `None`, a new figure and axes is created.

**negate\_score**bool, default=False

Whether or not to negate the scores obtained through [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
. This is particularly useful when using the error denoted by `neg_*` in `scikit-learn`.

**score\_name**str, default=None

The name of the score used to decorate the y-axis of the plot. It will override the name inferred from the `scoring` parameter. If `score` is `None`, we use `"Score"` if `negate_score` is `False` and `"Negative score"` otherwise. If `scoring` is a string or a callable, we infer the name. We replace `_` by spaces and capitalize the first letter. We remove `neg_` and replace it by `"Negative"` if `negate_score` is `False` or just remove it otherwise.

**score\_type**{“test”, “train”, “both”}, default=”both”

The type of score to plot. Can be one of `"test"`, `"train"`, or `"both"`.

**std\_display\_style**{“errorbar”, “fill\_between”} or None, default=”fill\_between”

The style used to display the score standard deviation around the mean score. If None, no standard deviation representation is displayed.

**line\_kw**dict, default=None

Additional keyword arguments passed to the `plt.plot` used to draw the mean score.

**fill\_between\_kw**dict, default=None

Additional keyword arguments passed to the `plt.fill_between` used to draw the score standard deviation.

**errorbar\_kw**dict, default=None

Additional keyword arguments passed to the `plt.errorbar` used to draw mean score and standard deviation score.

Returns:

**display**[`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")

Object that stores computed values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_thumb.png)

[Comparison of kernel ridge regression and SVR](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)

Comparison of kernel ridge regression and SVR

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_learning_curve_thumb.png)

[Plotting Learning Curves and Checking Models’ Scalability](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html)

Plotting Learning Curves and Checking Models' Scalability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)