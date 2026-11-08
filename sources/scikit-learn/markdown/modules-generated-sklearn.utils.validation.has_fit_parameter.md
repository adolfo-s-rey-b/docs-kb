[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.has_fit_parameter.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.validation.has_fit_parameter.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.has_fit_parameter.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.validation.has_fit_parameter.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.validation.has_fit_parameter.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.validation.has_fit_parameter.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.validation.has_fit_parameter.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.validation.has_fit_parameter.html)

Collapse Sidebar Expand Sidebar

has\_fit\_parameter[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.has_fit_parameter.html#has-fit-parameter "Link to this heading")

===================================================================================================================================================================

sklearn.utils.validation.has\_fit\_parameter(_estimator_, _parameter_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1488)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.has_fit_parameter.html#sklearn.utils.validation.has_fit_parameter "Link to this definition")

Check whether the estimator’s fit method supports the given parameter.

Parameters:

**estimator**object

An estimator to inspect.

**parameter**str

The searched parameter.

Returns:

**is\_parameter**bool

Whether the parameter was found to be a named parameter of the estimator’s fit method.

Examples

\>>> from sklearn.svm import SVC
\>>> from sklearn.utils.validation import has\_fit\_parameter
\>>> has\_fit\_parameter(SVC(), "sample\_weight")
True

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)