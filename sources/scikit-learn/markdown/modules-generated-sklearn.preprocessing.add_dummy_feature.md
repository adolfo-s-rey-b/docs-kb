[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.add_dummy_feature.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

add\_dummy\_feature[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.add_dummy_feature.html#add-dummy-feature "Link to this heading")

================================================================================================================================================================

sklearn.preprocessing.add\_dummy\_feature(_X_, _value\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L2605)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.add_dummy_feature.html#sklearn.preprocessing.add_dummy_feature "Link to this definition")

Augment dataset with an additional dummy feature.

This is useful for fitting an intercept term with implementations which cannot otherwise fit it directly.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

**value**float

Value to use for the dummy feature.

Returns:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features + 1)

Same data with dummy feature added as first column.

Examples

\>>> from sklearn.preprocessing import add\_dummy\_feature
\>>> add\_dummy\_feature(\[\[0, 1\], \[1, 0\]\])
array(\[\[1., 0., 1.\],\
       \[1., 1., 0.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)