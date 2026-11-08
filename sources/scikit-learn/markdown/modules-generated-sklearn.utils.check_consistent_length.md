[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.check_consistent_length.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.check_consistent_length.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.check_consistent_length.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.check_consistent_length.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.check_consistent_length.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.check_consistent_length.html)

Collapse Sidebar Expand Sidebar

check\_consistent\_length[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#check-consistent-length "Link to this heading")

==========================================================================================================================================================================

sklearn.utils.check\_consistent\_length(_\*arrays_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L439)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#sklearn.utils.check_consistent_length "Link to this definition")

Check that all arrays have consistent first dimensions.

Checks whether all objects in arrays have the same shape or length.

Parameters:

**\*arrays**list or tuple of input objects.

Objects that will be checked for consistent length.

Examples

\>>> from sklearn.utils.validation import check\_consistent\_length
\>>> a \= \[1, 2, 3\]
\>>> b \= \[2, 3, 4\]
\>>> check\_consistent\_length(a, b)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)