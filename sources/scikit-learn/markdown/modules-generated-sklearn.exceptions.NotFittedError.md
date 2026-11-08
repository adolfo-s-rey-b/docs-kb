[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.exceptions.NotFittedError.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.exceptions.NotFittedError.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.exceptions.NotFittedError.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.exceptions.NotFittedError.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.exceptions.NotFittedError.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.exceptions.NotFittedError.html)

Collapse Sidebar Expand Sidebar

NotFittedError[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#notfittederror "Link to this heading")

==================================================================================================================================================

exception sklearn.exceptions.NotFittedError[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/exceptions.py#L46)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "Link to this definition")

Exception class to raise if estimator is used before fitting.

This class inherits from both ValueError and AttributeError to help with exception handling and backward compatibility.

Examples

\>>> from sklearn.svm import LinearSVC
\>>> from sklearn.exceptions import NotFittedError
\>>> try:
...     LinearSVC().predict(\[\[1, 2\], \[2, 3\], \[3, 4\]\])
... except NotFittedError as e:
...     print(repr(e))
NotFittedError("This LinearSVC instance is not fitted yet. Call 'fit' with
appropriate arguments before using this estimator."...)

Copy to clipboard

Changed in version 0.18: Moved from sklearn.utils.validation.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)