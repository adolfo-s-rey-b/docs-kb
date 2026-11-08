[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.mutual_info_classif.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.mutual_info_classif.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.mutual_info_classif.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.mutual_info_classif.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.mutual_info_classif.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.mutual_info_classif.html)

Collapse Sidebar Expand Sidebar

mutual\_info\_classif[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#mutual-info-classif "Link to this heading")

==========================================================================================================================================================================

sklearn.feature\_selection.mutual\_info\_classif(_X_, _y_, _\*_, _discrete\_features\='auto'_, _n\_neighbors\=3_, _copy\=True_, _random\_state\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_mutual_info.py#L453)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "Link to this definition")

Estimate mutual information for a discrete target variable.

Mutual information (MI) [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#r50b872b699c4-1)
 between two random variables is a non-negative value, which measures the dependency between the variables. It is equal to zero if and only if two random variables are independent, and higher values mean higher dependency.

The function relies on nonparametric methods based on entropy estimation from k-nearest neighbors distances as described in [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#r50b872b699c4-2)
 and [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#r50b872b699c4-3)
. Both methods are based on the idea originally proposed in [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#r50b872b699c4-4)
.

It can be used for univariate features selection, read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Feature matrix.

**y**array-like of shape (n\_samples,)

Target vector.

**discrete\_features**‘auto’, bool or array-like, default=’auto’

If bool, then determines whether to consider all features discrete or continuous. If array, then it should be either a boolean mask with shape (n\_features,) or array with indices of discrete features. If ‘auto’, it is assigned to False for dense `X` and to True for sparse `X`.

**n\_neighbors**int, default=3

Number of neighbors to use for MI estimation for continuous variables, see [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#r50b872b699c4-2)
 and [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#r50b872b699c4-3)
. Higher values reduce variance of the estimation, but could introduce a bias.

**copy**bool, default=True

Whether to make a copy of the given data. If set to False, the initial data will be overwritten.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for adding small noise to continuous variables in order to remove repeated values. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int, default=None

The number of jobs to use for computing the mutual information. The parallelization is done on the columns of `X`. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Added in version 1.5.

Returns:

**mi**ndarray, shape (n\_features,)

Estimated mutual information between each feature and the target in nat units.

Notes

1.  The term “discrete features” is used instead of naming them “categorical”, because it describes the essence more accurately. For example, pixel intensities of an image are discrete features (but hardly categorical) and you will get better results if mark them as such. Also note, that treating a continuous variable as discrete and vice versa will usually give incorrect results, so be attentive about that.
    
2.  True mutual information can’t be negative. If its estimate turns out to be negative, it is replaced by zero.
    

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#id1)\
\]

[Mutual Information](https://en.wikipedia.org/wiki/Mutual_information)
 on Wikipedia.

\[2\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#id2)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#id5)
)

A. Kraskov, H. Stogbauer and P. Grassberger, “Estimating mutual information”. Phys. Rev. E 69, 2004.

\[3\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#id3)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#id6)
)

B. C. Ross “Mutual Information between Discrete and Continuous Data Sets”. PLoS ONE 9(2), 2014.

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#id4)\
\]

L. F. Kozachenko, N. N. Leonenko, “Sample Estimate of the Entropy of a Random Vector:, Probl. Peredachi Inf., 23:2 (1987), 9-16

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.feature\_selection import mutual\_info\_classif
\>>> X, y \= make\_classification(
...     n\_samples\=100, n\_features\=10, n\_informative\=2, n\_clusters\_per\_class\=1,
...     shuffle\=False, random\_state\=42
... )
\>>> mutual\_info\_classif(X, y)
array(\[0.589, 0.107, 0.196, 0.0968 , 0.,\
       0.   , 0.   , 0.   , 0.     , 0.\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)