[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.d2_brier_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.d2_brier_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.d2_brier_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.d2_brier_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.d2_brier_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.d2_brier_score.html)

Collapse Sidebar Expand Sidebar

d2\_brier\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#d2-brier-score "Link to this heading")

=================================================================================================================================================

sklearn.metrics.d2\_brier\_score(_y\_true_, _y\_proba_, _\*_, _sample\_weight\=None_, _pos\_label\=None_, _labels\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L3983)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "Link to this definition")

D2 score function, fraction of Brier score explained.

This is also known as Brier Skill Score (BSS) and scaled Brier score.

Best possible score is 1.0 and it can be negative because the model can be arbitrarily worse than the null model. The null model, also known as the optimal intercept model, is a model that constantly predicts the per-class proportions of `y_true`, disregarding the input features. The null model gets a D^2 score of 0.0.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#d2-score-classification)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True targets.

**y\_proba**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

Predicted probabilities. If `y_proba.shape = (n_samples,)` the probabilities provided are assumed to be that of the positive class. If `y_proba.shape = (n_samples, n_classes)` the columns in `y_proba` are assumed to correspond to the labels in alphabetical order, as done by [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**pos\_label**int, float, bool or str, default=None

Label of the positive class. `pos_label` will be inferred in the following manner:

*   if `y_true` in {-1, 1} or {0, 1}, `pos_label` defaults to 1;
    
*   else if `y_true` contains string, an error will be raised and `pos_label` should be explicitly specified;
    
*   otherwise, `pos_label` defaults to the greater label, i.e. `np.unique(y_true)[-1]`.
    

**labels**array-like of shape (n\_classes,), default=None

Class labels when `y_proba.shape = (n_samples, n_classes)`. If not provided, labels will be inferred from `y_true`.

Returns:

**d2**float

The D^2 score.

References

\[1\]

[Wikipedia entry for the Brier Skill Score (BSS)](https://en.wikipedia.org/wiki/Brier_score)
.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)