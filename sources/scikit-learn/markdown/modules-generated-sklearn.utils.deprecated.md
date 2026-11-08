[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.deprecated.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.deprecated.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.deprecated.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.deprecated.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.deprecated.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.deprecated.html)

Collapse Sidebar Expand Sidebar

deprecated[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#deprecated "Link to this heading")

=================================================================================================================================

class sklearn.utils.deprecated(_extra\=''_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/deprecation.py#L11)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#sklearn.utils.deprecated "Link to this definition")

Decorator to mark a function or class as deprecated.

Issue a warning when the function is called/the class is instantiated and adds a warning to the docstring.

The optional extra argument will be appended to the deprecation message and the docstring. Note: to use this with the default value for extra, put in an empty of parentheses:

Parameters:

**extra**str, default=’’

To be added to the deprecation messages.

Examples

\>>> from sklearn.utils import deprecated
\>>> deprecated()
<sklearn.utils.deprecation.deprecated object at ...>
\>>> @deprecated()
... def some\_function(): pass

Copy to clipboard

\_\_call\_\_(_obj_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/deprecation.py#L41)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#sklearn.utils.deprecated.__call__ "Link to this definition")

Call method

Parameters:

**obj**object

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)