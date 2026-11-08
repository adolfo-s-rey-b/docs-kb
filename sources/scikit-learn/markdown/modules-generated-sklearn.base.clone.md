[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.clone.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.clone.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.clone.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.clone.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.clone.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.clone.html)

Collapse Sidebar Expand Sidebar

clone[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#clone "Link to this heading")

=================================================================================================================

sklearn.base.clone(_estimator_, _\*_, _safe\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L46)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "Link to this definition")

Construct a new unfitted estimator with the same parameters.

Clone does a deep copy of the model in an estimator without actually copying attached data. It returns a new estimator with the same parameters that has not been fitted on any data.

Changed in version 1.3: Delegates to `estimator.__sklearn_clone__` if the method exists.

Parameters:

**estimator**{list, tuple, set} of estimator instance or a single estimator instance

The estimator or group of estimators to be cloned.

**safe**bool, default=True

If safe is False, clone will fall back to a deep copy on objects that are not estimators. Ignored if `estimator.__sklearn_clone__` exists.

Returns:

**estimator**object

The deep copy of the input, an estimator if input is an estimator.

Notes

If the estimator’s `random_state` parameter is an integer (or if the estimator doesn’t have a `random_state` parameter), an _exact clone_ is returned: the clone and the original estimator will give the exact same results. Otherwise, _statistical clone_ is returned: the clone might return different results from the original estimator. More details can be found in [Controlling randomness](https://scikit-learn.org/stable/common_pitfalls.html#randomness)
.

Examples

\>>> from sklearn.base import clone
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X \= \[\[\-1, 0\], \[0, 1\], \[0, \-1\], \[1, 0\]\]
\>>> y \= \[0, 0, 1, 1\]
\>>> classifier \= LogisticRegression().fit(X, y)
\>>> cloned\_classifier \= clone(classifier)
\>>> hasattr(classifier, "classes\_")
True
\>>> hasattr(cloned\_classifier, "classes\_")
False
\>>> classifier is cloned\_classifier
False

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)