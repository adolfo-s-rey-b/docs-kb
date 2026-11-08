[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataConversionWarning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.exceptions.DataConversionWarning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataConversionWarning.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.exceptions.DataConversionWarning.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.exceptions.DataConversionWarning.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.exceptions.DataConversionWarning.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.exceptions.DataConversionWarning.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.exceptions.DataConversionWarning.html)

Collapse Sidebar Expand Sidebar

DataConversionWarning[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataConversionWarning.html#dataconversionwarning "Link to this heading")

=======================================================================================================================================================================

exception sklearn.exceptions.DataConversionWarning[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/exceptions.py#L76)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataConversionWarning.html#sklearn.exceptions.DataConversionWarning "Link to this definition")

Warning used to notify implicit data conversions happening in the code.

This warning occurs when some input data needs to be converted or interpreted in a way that may not match the user’s expectations.

For example, this warning may occur when the user

*   passes an integer array to a function which expects float input and will convert the input
    
*   requests a non-copying operation, but a copy is required to meet the implementation’s data-type expectations;
    
*   passes an input whose shape can be interpreted ambiguously.
    

Changed in version 0.18: Moved from sklearn.utils.validation.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)