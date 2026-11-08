[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.get_tags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.get_tags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.get_tags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.get_tags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.get_tags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.get_tags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.get_tags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.get_tags.html)

Collapse Sidebar Expand Sidebar

get\_tags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.get_tags.html#get-tags "Link to this heading")

============================================================================================================================

sklearn.utils.get\_tags(_estimator_) → [Tags](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "sklearn.utils._tags.Tags")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L250)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.get_tags.html#sklearn.utils.get_tags "Link to this definition")

Get estimator tags.

`BaseEstimator` provides the estimator tags machinery.

For scikit-learn built-in estimators, we should still rely on `self.__sklearn_tags__()`. `get_tags(est)` should be used when we are not sure where `est` comes from: typically `get_tags(self.estimator)` where `self` is a meta-estimator, or in the common checks.

Added in version 1.6.

Parameters:

**estimator**estimator object

The estimator from which to get the tag.

Returns:

**tags**[`Tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "sklearn.utils.Tags")

The estimator tags.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)