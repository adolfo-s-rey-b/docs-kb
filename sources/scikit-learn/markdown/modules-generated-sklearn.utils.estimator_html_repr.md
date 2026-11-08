[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.estimator_html_repr.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.estimator_html_repr.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.estimator_html_repr.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.estimator_html_repr.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.estimator_html_repr.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.estimator_html_repr.html)

Collapse Sidebar Expand Sidebar

estimator\_html\_repr[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#estimator-html-repr "Link to this heading")

==============================================================================================================================================================

sklearn.utils.estimator\_html\_repr(_estimator_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_repr_html/estimator.py#L482)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "Link to this definition")

Build an HTML representation of an estimator.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/compose.html#visualizing-composite-estimators)
.

Parameters:

**estimator**estimator object

The estimator to visualize.

Returns:

html: str

HTML representation of estimator.

Examples

\>>> from sklearn.utils.\_repr\_html.estimator import estimator\_html\_repr
\>>> from sklearn.linear\_model import LogisticRegression
\>>> estimator\_html\_repr(LogisticRegression())
'<style>.sk-global...'

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)