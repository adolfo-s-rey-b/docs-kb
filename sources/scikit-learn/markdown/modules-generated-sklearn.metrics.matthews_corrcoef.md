[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.matthews_corrcoef.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.matthews_corrcoef.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.matthews_corrcoef.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.matthews_corrcoef.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.matthews_corrcoef.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.matthews_corrcoef.html)

Collapse Sidebar Expand Sidebar

matthews\_corrcoef[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#matthews-corrcoef "Link to this heading")

=========================================================================================================================================================

sklearn.metrics.matthews\_corrcoef(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L1244)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "Link to this definition")

Compute the Matthews correlation coefficient (MCC).

The Matthews correlation coefficient is used in machine learning as a measure of the quality of binary and multiclass classifications. It takes into account true and false positives and negatives and is generally regarded as a balanced measure which can be used even if the classes are of very different sizes. The MCC is in essence a correlation coefficient value between -1 and +1. A coefficient of +1 represents a perfect prediction, 0 an average random prediction and -1 an inverse prediction. The statistic is also known as the phi coefficient. \[source: Wikipedia\]

Binary and multiclass labels are supported. Only in the binary case does this relate to information about true and false positives and negatives. See references below.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#matthews-corrcoef)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,)

Estimated targets as returned by a classifier.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Added in version 0.18.

Returns:

**mcc**float

The Matthews correlation coefficient (+1 represents a perfect prediction, 0 an average random prediction and -1 and inverse prediction).

References

\[1\]

[Baldi, Brunak, Chauvin, Andersen and Nielsen, (2000). Assessing the accuracy of prediction algorithms for classification: an overview.](https://doi.org/10.1093/bioinformatics/16.5.412)

\[2\]

[Wikipedia entry for the Matthews Correlation Coefficient (phi coefficient)](https://en.wikipedia.org/wiki/Phi_coefficient)
.

\[3\]

[Gorodkin, (2004). Comparing two K-category assignments by a K-category correlation coefficient](https://www.sciencedirect.com/science/article/pii/S1476927104000799)
.

\[4\]

[Jurman, Riccadonna, Furlanello, (2012). A Comparison of MCC and CEN Error Measures in MultiClass Prediction](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0041882)
.

Examples

\>>> from sklearn.metrics import matthews\_corrcoef
\>>> y\_true \= \[+1, +1, +1, \-1\]
\>>> y\_pred \= \[+1, \-1, +1, +1\]
\>>> matthews\_corrcoef(y\_true, y\_pred)
\-0.33

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)