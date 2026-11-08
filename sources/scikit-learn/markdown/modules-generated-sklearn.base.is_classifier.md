[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.is_classifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.is_classifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.is_classifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.is_classifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.is_classifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.is_classifier.html)

Collapse Sidebar Expand Sidebar

is\_classifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#is-classifier "Link to this heading")

==========================================================================================================================================

sklearn.base.is\_classifier(_estimator_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1245)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "Link to this definition")

Return True if the given estimator is (probably) a classifier.

Parameters:

**estimator**estimator instance

Estimator object to test.

Returns:

**out**bool

True if estimator is a classifier and False otherwise.

Examples

\>>> from sklearn.base import is\_classifier
\>>> from sklearn.cluster import KMeans
\>>> from sklearn.svm import SVC, SVR
\>>> classifier \= SVC()
\>>> regressor \= SVR()
\>>> kmeans \= KMeans()
\>>> is\_classifier(classifier)
True
\>>> is\_classifier(regressor)
False
\>>> is\_classifier(kmeans)
False

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)