[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.make_scorer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.make_scorer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.make_scorer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.make_scorer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.make_scorer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.make_scorer.html)

Collapse Sidebar Expand Sidebar

make\_scorer[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#make-scorer "Link to this heading")

=======================================================================================================================================

sklearn.metrics.make\_scorer(_score\_func_, _\*_, _response\_method\='predict'_, _greater\_is\_better\=True_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_scorer.py#L662)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "Link to this definition")

Make a scorer from a performance metric or loss function.

A scorer is a wrapper around an arbitrary metric or loss function that is called with the signature `scorer(estimator, X, y_true, **kwargs)`.

It is accepted in all scikit-learn estimators or functions allowing a `scoring` parameter.

The parameter `response_method` allows to specify which method of the estimator should be used to feed the scoring/loss function.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
.

Parameters:

**score\_func**callable

Score function (or loss function) with signature `score_func(y, y_pred, **kwargs)`.

**response\_method**{“predict\_proba”, “decision\_function”, “predict”} or list/tuple of such str, default=”predict”

Specifies the response method to use get prediction from an estimator (i.e. [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
, [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 or [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
). Possible choices are:

*   if `str`, it corresponds to the name to the method to return;
    
*   if a list or tuple of `str`, it provides the method names in order of preference. The method returned corresponds to the first method in the list and which is implemented by `estimator`.
    

Added in version 1.4.

**greater\_is\_better**bool, default=True

Whether `score_func` is a score function (default), meaning high is good, or a loss function, meaning low is good. In the latter case, the scorer object will sign-flip the outcome of the `score_func`.

**\*\*kwargs**additional arguments

Additional parameters to be passed to `score_func`.

Returns:

**scorer**callable

Callable object that returns a scalar score; greater is better.

Examples

\>>> from sklearn.metrics import fbeta\_score, make\_scorer
\>>> ftwo\_scorer \= make\_scorer(fbeta\_score, beta\=2)
\>>> ftwo\_scorer
make\_scorer(fbeta\_score, response\_method='predict', beta=2)
\>>> from sklearn.model\_selection import GridSearchCV
\>>> from sklearn.svm import LinearSVC
\>>> grid \= GridSearchCV(LinearSVC(), param\_grid\={'C': \[1, 10\]},
...                     scoring\=ftwo\_scorer)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_metric_evaluation_thumb.png)

[Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html)

Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)