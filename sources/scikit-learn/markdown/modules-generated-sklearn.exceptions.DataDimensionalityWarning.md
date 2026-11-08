[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html)

Collapse Sidebar Expand Sidebar

DataDimensionalityWarning[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html#datadimensionalitywarning "Link to this heading")

===================================================================================================================================================================================

exception sklearn.exceptions.DataDimensionalityWarning[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/exceptions.py#L94)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html#sklearn.exceptions.DataDimensionalityWarning "Link to this definition")

Custom warning to notify potential issues with data dimensionality.

For example, in random projection, this warning is raised when the number of components, which quantifies the dimensionality of the target projection space, is higher than the number of features, which quantifies the dimensionality of the original source space, to imply that the dimensionality of the problem will not be reduced.

Changed in version 0.18: Moved from sklearn.utils.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)