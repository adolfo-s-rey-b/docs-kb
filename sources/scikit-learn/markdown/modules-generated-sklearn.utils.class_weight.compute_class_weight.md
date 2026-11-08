[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.class_weight.compute_class_weight.html)

Collapse Sidebar Expand Sidebar

compute\_class\_weight[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#compute-class-weight "Link to this heading")

==============================================================================================================================================================================

sklearn.utils.class\_weight.compute\_class\_weight(_class\_weight_, _\*_, _classes_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/class_weight.py#L21)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "Link to this definition")

Estimate class weights for unbalanced datasets.

Parameters:

**class\_weight**dict, “balanced” or None

If “balanced”, class weights will be given by `n_samples / (n_classes * np.bincount(y))` or their weighted equivalent if `sample_weight` is provided. If a dictionary is given, keys are classes and values are corresponding class weights. If `None` is given, the class weights will be uniform.

**classes**ndarray

Array of the classes occurring in the data, as given by `np.unique(y_org)` with `y_org` the original class labels.

**y**array-like of shape (n\_samples,)

Array of original class labels per sample.

**sample\_weight**array-like of shape (n\_samples,), default=None

Array of weights that are assigned to individual samples. Only used when `class_weight='balanced'`.

Returns:

**class\_weight\_vect**ndarray of shape (n\_classes,)

Array with `class_weight_vect[i]` the weight for i-th class.

References

The “balanced” heuristic is inspired by Logistic Regression in Rare Events Data, King, Zen, 2001.

Examples

\>>> import numpy as np
\>>> from sklearn.utils.class\_weight import compute\_class\_weight
\>>> y \= \[1, 1, 1, 1, 0, 0\]
\>>> compute\_class\_weight(class\_weight\="balanced", classes\=np.unique(y), y\=y)
array(\[1.5 , 0.75\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)