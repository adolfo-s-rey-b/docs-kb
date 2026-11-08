[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html)

Collapse Sidebar Expand Sidebar

compute\_sample\_weight[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html#compute-sample-weight "Link to this heading")

=================================================================================================================================================================================

sklearn.utils.class\_weight.compute\_sample\_weight(_class\_weight_, _y_, _\*_, _indices\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/class_weight.py#L125)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html#sklearn.utils.class_weight.compute_sample_weight "Link to this definition")

Estimate sample weights by class for unbalanced datasets.

Parameters:

**class\_weight**dict, list of dicts, “balanced”, or None

Weights associated with classes in the form `{class_label: weight}`. If not given, all classes are supposed to have weight one. For multi-output problems, a list of dicts can be provided in the same order as the columns of y.

Note that for multioutput (including multilabel) weights should be defined for each class of every column in its own dict. For example, for four-class multilabel classification weights should be `[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}]` instead of `[{1:1}, {2:5}, {3:1}, {4:1}]`.

The `"balanced"` mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data: `n_samples / (n_classes * np.bincount(y))`.

For multi-output, the weights of each column of y will be multiplied.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_outputs)

Array of original class labels per sample.

**indices**array-like of shape (n\_subsample,), default=None

Array of indices to be used in a subsample. Can be of length less than `n_samples` in the case of a subsample, or equal to `n_samples` in the case of a bootstrap subsample with repeated indices. If `None`, the sample weight will be calculated over the full sample. Only `"balanced"` is supported for `class_weight` if this is provided.

Returns:

**sample\_weight\_vect**ndarray of shape (n\_samples,)

Array with sample weights as applied to the original `y`.

Examples

\>>> from sklearn.utils.class\_weight import compute\_sample\_weight
\>>> y \= \[1, 1, 1, 1, 0, 0\]
\>>> compute\_sample\_weight(class\_weight\="balanced", y\=y)
array(\[0.75, 0.75, 0.75, 0.75, 1.5 , 1.5 \])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)