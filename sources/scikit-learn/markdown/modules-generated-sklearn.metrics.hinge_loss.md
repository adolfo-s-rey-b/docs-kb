[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.hinge_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.hinge_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.hinge_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.hinge_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.hinge_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.hinge_loss.html)

Collapse Sidebar Expand Sidebar

hinge\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#hinge-loss "Link to this heading")

====================================================================================================================================

sklearn.metrics.hinge\_loss(_y\_true_, _pred\_decision_, _\*_, _labels\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L3461)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#sklearn.metrics.hinge_loss "Link to this definition")

Average hinge loss (non-regularized).

In [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 class case, assuming labels in `y_true` are encoded with +1 and -1, when a prediction mistake is made, `margin = y_true * pred_decision` is always negative (since the signs are opposite), implying `1 - margin` is always greater than 1. The cumulated hinge loss is therefore an upper bound of the number of mistakes made by the classifier.

In [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 case, the function expects that either all the labels are present in `y_true` or an optional `labels` argument is provided which contains all the labels. The multiclass margin is calculated according to Crammer-Singer’s method. As in the binary case, the cumulated hinge loss is an upper bound of the number of mistakes made by the classifier.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#hinge-loss)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True target. For [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 data, it should only contain two unique values, with the positive label being greater than the negative label. For [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 data, all labels should be present, or provided via `labels`.

**pred\_decision**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

Predicted decisions, as output by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 (floats).

**labels**array-like, default=None

Contains all the labels for the problem. Used in multiclass hinge loss.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**loss**float

Average hinge loss.

References

\[1\]

[Wikipedia entry on the Hinge loss](https://en.wikipedia.org/wiki/Hinge_loss)
.

\[2\]

[Koby Crammer, Yoram Singer. On the Algorithmic Implementation of Multiclass Kernel-based Vector Machines. Journal of Machine Learning Research 2, (2001), 265-292](https://jmlr.csail.mit.edu/papers/volume2/crammer01a/crammer01a.pdf)
.

\[3\]

[L1 and L2 Regularization for Multiclass Hinge Loss Models by Robert C. Moore, John DeNero](https://www.isca-archive.org/mlslp_2011/moore11_mlslp.pdf)
.

Examples

\>>> from sklearn import svm
\>>> from sklearn.metrics import hinge\_loss
\>>> X \= \[\[0\], \[1\]\]
\>>> y \= \[\-1, 1\]
\>>> est \= svm.LinearSVC(random\_state\=0)
\>>> est.fit(X, y)
LinearSVC(random\_state=0)
\>>> pred\_decision \= est.decision\_function(\[\[\-2\], \[3\], \[0.5\]\])
\>>> pred\_decision
array(\[-2.18,  2.36,  0.09\])
\>>> hinge\_loss(\[\-1, 1, 1\], pred\_decision)
0.30

Copy to clipboard

In the multiclass case:

\>>> import numpy as np
\>>> X \= np.array(\[\[0\], \[1\], \[2\], \[3\]\])
\>>> Y \= np.array(\[0, 1, 2, 3\])
\>>> labels \= np.array(\[0, 1, 2, 3\])
\>>> est \= svm.LinearSVC()
\>>> est.fit(X, Y)
LinearSVC()
\>>> pred\_decision \= est.decision\_function(\[\[\-1\], \[2\], \[3\]\])
\>>> y\_true \= \[0, 2, 3\]
\>>> hinge\_loss(y\_true, pred\_decision, labels\=labels)
0.56

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_thumb.png)

[Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html)

Plot classification boundaries with different SVM Kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)