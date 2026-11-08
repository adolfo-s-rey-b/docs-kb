[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.isotonic.isotonic_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.isotonic.isotonic_regression.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.isotonic.isotonic_regression.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.isotonic.isotonic_regression.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.isotonic.isotonic_regression.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.isotonic.isotonic_regression.html)

Collapse Sidebar Expand Sidebar

isotonic\_regression[#](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html#isotonic-regression "Link to this heading")

================================================================================================================================================================

sklearn.isotonic.isotonic\_regression(_y_, _\*_, _sample\_weight\=None_, _y\_min\=None_, _y\_max\=None_, _increasing\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/isotonic.py#L100)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html#sklearn.isotonic.isotonic_regression "Link to this definition")

Solve the isotonic regression model.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/isotonic.html#isotonic)
.

Parameters:

**y**array-like of shape (n\_samples,)

The data.

**sample\_weight**array-like of shape (n\_samples,), default=None

Weights on each point of the regression. If None, weight is set to 1 (equal weights).

**y\_min**float, default=None

Lower bound on the lowest predicted value (the minimum value may still be higher). If not set, defaults to -inf.

**y\_max**float, default=None

Upper bound on the highest predicted value (the maximum may still be lower). If not set, defaults to +inf.

**increasing**bool, default=True

Whether to compute `y_` is increasing (if set to True) or decreasing (if set to False).

Returns:

**y\_**ndarray of shape (n\_samples,)

Isotonic fit of y.

References

“Active set algorithms for isotonic regression; A unifying framework” by Michael J. Best and Nilotpal Chakravarti, section 3.

Examples

\>>> from sklearn.isotonic import isotonic\_regression
\>>> isotonic\_regression(\[5, 3, 1, 2, 8, 10, 7, 9, 6, 4\])
array(\[2.75   , 2.75   , 2.75   , 2.75   , 7.33,\
       7.33, 7.33, 7.33, 7.33, 7.33\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)