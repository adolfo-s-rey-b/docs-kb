[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.check_increasing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.isotonic.check_increasing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.check_increasing.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.isotonic.check_increasing.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.isotonic.check_increasing.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.isotonic.check_increasing.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.isotonic.check_increasing.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.isotonic.check_increasing.html)

Collapse Sidebar Expand Sidebar

check\_increasing[#](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.check_increasing.html#check-increasing "Link to this heading")

=======================================================================================================================================================

sklearn.isotonic.check\_increasing(_x_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/isotonic.py#L24)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.check_increasing.html#sklearn.isotonic.check_increasing "Link to this definition")

Determine whether y is monotonically correlated with x.

y is found increasing or decreasing with respect to x based on a Spearman correlation test.

Parameters:

**x**array-like of shape (n\_samples,)

Training data.

**y**array-like of shape (n\_samples,)

Training target.

Returns:

**increasing\_bool**boolean

Whether the relationship is increasing or decreasing.

Notes

The Spearman correlation coefficient is estimated from the data, and the sign of the resulting estimate is used as the result.

In the event that the 95% confidence interval based on Fisher transform spans zero, a warning is raised.

References

Fisher transformation. Wikipedia. [https://en.wikipedia.org/wiki/Fisher\_transformation](https://en.wikipedia.org/wiki/Fisher_transformation)

Examples

\>>> from sklearn.isotonic import check\_increasing
\>>> x, y \= \[1, 2, 3, 4, 5\], \[2, 4, 6, 8, 10\]
\>>> check\_increasing(x, y)
np.True\_
\>>> y \= \[10, 8, 6, 4, 2\]
\>>> check\_increasing(x, y)
np.False\_

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)