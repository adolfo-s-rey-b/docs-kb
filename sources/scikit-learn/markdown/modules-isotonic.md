[Skip to main content](https://scikit-learn.org/stable/modules/isotonic.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/isotonic.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/isotonic.html)
[1.8.0](https://scikit-learn.org/1.8/modules/isotonic.html)
[1.7.2](https://scikit-learn.org/1.7/modules/isotonic.html)
[1.6.1](https://scikit-learn.org/1.6/modules/isotonic.html)
[1.5.2](https://scikit-learn.org/1.5/modules/isotonic.html)
[1.4.2](https://scikit-learn.org/1.4/modules/isotonic.html)

Collapse Sidebar Expand Sidebar

1.15. Isotonic regression[#](https://scikit-learn.org/stable/modules/isotonic.html#isotonic-regression "Link to this heading")

===============================================================================================================================

The class [`IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
 fits a non-decreasing real function to 1-dimensional data. It solves the following problem:

min∑iwi(yi−y^i)2

subject to y^i≤y^j whenever Xi≤Xj, where the weights wi are strictly positive, and both `X` and `y` are arbitrary real quantities.

The `increasing` parameter changes the constraint to y^i≥y^j whenever Xi≤Xj. Setting it to ‘auto’ will automatically choose the constraint based on [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
.

[`IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
 produces a series of predictions y^i for the training data which are the closest to the targets y in terms of mean squared error. These predictions are interpolated for predicting to unseen data. The predictions of [`IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
 thus form a function that is piecewise linear:

[![../_images/sphx_glr_plot_isotonic_regression_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_isotonic_regression_001.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html)

Examples

*   [Isotonic Regression](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html#sphx-glr-auto-examples-miscellaneous-plot-isotonic-regression-py)
    

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)