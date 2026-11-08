[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.cohen_kappa_score.html)

Collapse Sidebar Expand Sidebar

cohen\_kappa\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#cohen-kappa-score "Link to this heading")

==========================================================================================================================================================

sklearn.metrics.cohen\_kappa\_score(_y1_, _y2_, _\*_, _labels\=None_, _weights\=None_, _sample\_weight\=None_, _replace\_undefined\_by\=nan_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L875)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "Link to this definition")

Compute Cohen’s kappa: a statistic that measures inter-annotator agreement.

This function computes Cohen’s kappa [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#r219a3b9132e1-1)
, a score that expresses the level of agreement between two annotators on a classification problem. It is defined as

κ\=(po−pe)/(1−pe)

where po is the empirical probability of agreement on the label assigned to any sample (the observed agreement ratio), and pe is the expected agreement when both annotators assign labels randomly. pe is estimated using a per-annotator empirical prior over the class labels [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#r219a3b9132e1-2)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#cohen-kappa)
.

Parameters:

**y1**array-like of shape (n\_samples,)

Labels assigned by the first annotator.

**y2**array-like of shape (n\_samples,)

Labels assigned by the second annotator. The kappa statistic is symmetric, so swapping `y1` and `y2` doesn’t change the value.

**labels**array-like of shape (n\_classes,), default=None

List of labels to index the matrix. This may be used to select a subset of labels. If `None`, all labels that appear at least once in `y1` or `y2` are used. Note that at least one label in `labels` must be present in `y1`, even though this function is otherwise agnostic to the order of `y1` and `y2`.

**weights**{‘linear’, ‘quadratic’}, default=None

Weighting type to calculate the score. `None` means not weighted; “linear” means linear weighting; “quadratic” means quadratic weighting.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**replace\_undefined\_by**np.nan, float in \[-1.0, 1.0\], default=np.nan

Sets the return value when the metric is undefined. This can happen when no label of interest (as defined in the `labels` param) is assigned by the second annotator, or when both `y1` and ``y2`only have one label in common that is also in `labels``. In these cases, an [`UndefinedMetricWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.UndefinedMetricWarning.html#sklearn.exceptions.UndefinedMetricWarning "sklearn.exceptions.UndefinedMetricWarning")
 is raised. Can take the following values:

*   `np.nan` to return `np.nan`
    
*   a floating point value in the range of \[-1.0, 1.0\] to return a specific value
    

Added in version 1.9.

Returns:

**kappa**float

The kappa statistic, which is a number between -1.0 and 1.0. The maximum value means complete agreement; the minimum value means complete disagreement; 0.0 indicates no agreement beyond what would be expected by chance.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#id1)\
\]

[J. Cohen (1960). “A coefficient of agreement for nominal scales”. Educational and Psychological Measurement 20(1):37-46.](https://doi.org/10.1177/001316446002000104)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#id2)\
\]

[R. Artstein and M. Poesio (2008). “Inter-coder agreement for computational linguistics”. Computational Linguistics 34(4):555-596](https://www.mitpressjournals.org/doi/pdf/10.1162/coli.07-034-R2)
.

\[3\]

[Wikipedia entry for the Cohen’s kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa)
.

Examples

\>>> from sklearn.metrics import cohen\_kappa\_score
\>>> y1 \= \["negative", "positive", "negative", "neutral", "positive"\]
\>>> y2 \= \["negative", "positive", "negative", "neutral", "negative"\]
\>>> cohen\_kappa\_score(y1, y2)
0.6875

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)