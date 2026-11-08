[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.svm.l1_min_c.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.svm.l1_min_c.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.svm.l1_min_c.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.svm.l1_min_c.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.svm.l1_min_c.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.svm.l1_min_c.html)

Collapse Sidebar Expand Sidebar

l1\_min\_c[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#l1-min-c "Link to this heading")

===========================================================================================================================

sklearn.svm.l1\_min\_c(_X_, _y_, _\*_, _loss\='squared\_hinge'_, _fit\_intercept\=True_, _intercept\_scaling\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_bounds.py#L16)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#sklearn.svm.l1_min_c "Link to this definition")

Return the lowest bound for `C`.

The lower bound for `C` is computed such that for `C` in `(l1_min_C, infinity)` the model is guaranteed not to be empty. This applies to l1 penalized classifiers, such as [`sklearn.svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 with penalty=’l1’ and [`sklearn.linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 with `l1_ratio=1`.

This value is valid if `class_weight` parameter in `fit()` is not set.

For an example of how to use this function, see [Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#sphx-glr-auto-examples-linear-model-plot-logistic-path-py)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target vector relative to X.

**loss**{‘squared\_hinge’, ‘log’}, default=’squared\_hinge’

Specifies the loss function. With ‘squared\_hinge’ it is the squared hinge loss (a.k.a. L2 loss). With ‘log’ it is the loss of logistic regression models.

**fit\_intercept**bool, default=True

Specifies if the intercept should be fitted by the model. It must match the fit() method parameter.

**intercept\_scaling**float, default=1.0

When fit\_intercept is True, instance vector x becomes \[x, intercept\_scaling\], i.e. a “synthetic” feature with constant value equals to intercept\_scaling is appended to the instance vector. It must match the fit() method parameter.

Returns:

**l1\_min\_c**float

Minimum value for C.

Examples

\>>> from sklearn.svm import l1\_min\_c
\>>> from sklearn.datasets import make\_classification
\>>> X, y \= make\_classification(n\_samples\=100, n\_features\=20, random\_state\=42)
\>>> print(f"{l1\_min\_c(X, y, loss\='squared\_hinge', fit\_intercept\=True):.4f}")
0.0044

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)