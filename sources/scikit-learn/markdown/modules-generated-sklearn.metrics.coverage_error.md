[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.coverage_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.coverage_error.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.coverage_error.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.coverage_error.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.coverage_error.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.coverage_error.html)

Collapse Sidebar Expand Sidebar

coverage\_error[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#coverage-error "Link to this heading")

================================================================================================================================================

sklearn.metrics.coverage\_error(_y\_true_, _y\_score_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1476)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#sklearn.metrics.coverage_error "Link to this definition")

Coverage error measure.

Compute how far we need to go through the ranked scores to cover all true labels. The best value is equal to the average number of labels in `y_true` per sample.

Ties in `y_scores` are broken by giving maximal rank that would have been assigned to all tied values.

Note: Our implementation’s score is 1 greater than the one given in Tsoumakas et al., 2010. This extends it to handle the degenerate case in which an instance has 0 true labels.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#coverage-error)
.

Parameters:

**y\_true**array-like of shape (n\_samples, n\_labels)

True binary labels in [label indicator format](https://scikit-learn.org/stable/glossary.html#term-label-indicator-format)
.

**y\_score**array-like of shape (n\_samples, n\_labels)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**coverage\_error**float

The coverage error.

References

\[1\]

Tsoumakas, G., Katakis, I., & Vlahavas, I. (2010). Mining multi-label data. In Data mining and knowledge discovery handbook (pp. 667-685). Springer US.

Examples

\>>> from sklearn.metrics import coverage\_error
\>>> y\_true \= \[\[1, 0, 0\], \[0, 1, 1\]\]
\>>> y\_score \= \[\[1, 0, 0\], \[0, 1, 1\]\]
\>>> coverage\_error(y\_true, y\_score)
1.5

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)