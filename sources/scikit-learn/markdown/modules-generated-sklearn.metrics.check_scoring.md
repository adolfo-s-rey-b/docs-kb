[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.check_scoring.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.check_scoring.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.check_scoring.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.check_scoring.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.check_scoring.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.check_scoring.html)

Collapse Sidebar Expand Sidebar

check\_scoring[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#check-scoring "Link to this heading")

=============================================================================================================================================

sklearn.metrics.check\_scoring(_estimator\=None_, _scoring\=None_, _\*_, _allow\_none\=False_, _raise\_exc\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_scorer.py#L930)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "Link to this definition")

Determine scorer from user options.

A TypeError will be thrown if the estimator cannot be scored.

Parameters:

**estimator**estimator object implementing ‘fit’ or None, default=None

The object to use to fit the data. If `None`, then this function may error depending on `allow_none`.

**scoring**str, callable, list, tuple, set, or dict, default=None

Scorer to use. If `scoring` represents a single score, one can use:

*   a single string (see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
    );
    
*   a callable (see [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
    ) that returns a single value;
    
*   `None`, the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

If `scoring` represents multiple scores, one can use:

*   a list, tuple or set of unique strings;
    
*   a callable returning a dictionary where the keys are the metric names and the values are the metric scorers;
    
*   a dictionary with metric names as keys and callables as values. The callables need to have the signature `callable(estimator, X, y)`.
    

**allow\_none**bool, default=False

Whether to return None or raise an error if no `scoring` is specified and the estimator has no `score` method.

**raise\_exc**bool, default=True

Whether to raise an exception (if a subset of the scorers in multimetric scoring fails) or to return an error code.

*   If set to `True`, raises the failing scorer’s exception.
    
*   If set to `False`, a formatted string of the exception details is passed as result of the failing scorer(s).
    

This applies if `scoring` is list, tuple, set, or dict. Ignored if `scoring` is a str or a callable.

Added in version 1.6.

Returns:

**scoring**callable

A scorer callable object / function with signature `scorer(estimator, X, y)`.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.metrics import check\_scoring
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> classifier \= DecisionTreeClassifier(max\_depth\=2).fit(X, y)
\>>> scorer \= check\_scoring(classifier, scoring\='accuracy')
\>>> scorer(classifier, X, y)
0.96...

Copy to clipboard

\>>> from sklearn.metrics import make\_scorer, accuracy\_score, mean\_squared\_log\_error
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> y \*= \-1
\>>> clf \= DecisionTreeClassifier().fit(X, y)
\>>> scoring \= {
...     "accuracy": make\_scorer(accuracy\_score),
...     "mean\_squared\_log\_error": make\_scorer(mean\_squared\_log\_error),
... }
\>>> scoring\_call \= check\_scoring(estimator\=clf, scoring\=scoring, raise\_exc\=False)
\>>> scores \= scoring\_call(clf, X, y)
\>>> scores
{'accuracy': 1.0, 'mean\_squared\_log\_error': 'Traceback ...'}

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)