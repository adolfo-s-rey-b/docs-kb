[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html)

Collapse Sidebar Expand Sidebar

StratifiedGroupKFold[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#stratifiedgroupkfold "Link to this heading")

=========================================================================================================================================================================

class sklearn.model\_selection.StratifiedGroupKFold(_n\_splits\=5_, _shuffle\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L892)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "Link to this definition")

Class-wise stratified K-Fold iterator variant with non-overlapping groups.

This cross-validation object is a variation of [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 that attempts to return stratified folds with non-overlapping groups. The folds are made by preserving the percentage of samples for each class in `y` in a binary or multiclass classification setting.

Each group will appear exactly once in the test set across all folds (the number of distinct groups has to be at least equal to the number of folds).

The difference between [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
 and `StratifiedGroupKFold` is that the former attempts to create balanced folds such that the number of distinct groups is approximately the same in each fold, whereas `StratifiedGroupKFold` attempts to create folds which preserve the percentage of samples from each class as much as possible given the constraint of non-overlapping groups between splits.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#stratified-group-k-fold)
.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to [Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-auto-examples-model-selection-plot-cv-indices-py)

Note

Stratification on the class label solves an engineering problem rather than a statistical one. See [Cross-validation iterators with stratification based on class labels](https://scikit-learn.org/stable/modules/cross_validation.html#stratification)
 for more details.

Parameters:

**n\_splits**int, default=5

Number of folds. Must be at least 2.

**shuffle**bool, default=False

Whether to shuffle each class’s samples before splitting into batches. Note that the samples within each split will not be shuffled. This implementation can only shuffle groups that have approximately the same `y` class distribution, no global shuffle will be performed.

**random\_state**int or RandomState instance, default=None

When `shuffle` is True, `random_state` affects the ordering of the indices, which controls the randomness of each fold for each class. Otherwise, leave `random_state` as `None`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

See also

[`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")

Takes class information into account to build folds which retain class distributions (for binary or multiclass classification tasks).

[`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")

K-fold iterator variant with non-overlapping groups.

Notes

The implementation is designed to:

*   Mimic the behavior of [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     as much as possible for trivial groups (e.g. when each group contains only one sample).
    
*   Be invariant to class label: relabelling `y = ["Happy", "Sad"]` to `y = [1, 0]` should not change the indices generated.
    
*   Stratify based on samples as much as possible while keeping non-overlapping groups constraint. That means that in some cases when there is a small number of groups containing a large number of samples the stratification will not be possible and the behavior will be close to [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
    .
    

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import StratifiedGroupKFold
\>>> X \= np.ones((17, 2))
\>>> y \= np.array(\[0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0\])
\>>> groups \= np.array(\[1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8\])
\>>> sgkf \= StratifiedGroupKFold(n\_splits\=3)
\>>> sgkf.get\_n\_splits()
3
\>>> print(sgkf)
StratifiedGroupKFold(n\_splits=3, random\_state=None, shuffle=False)
\>>> for i, (train\_index, test\_index) in enumerate(sgkf.split(X, y, groups)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"         group={groups\[train\_index\]}")
...     print(f"  Test:  index={test\_index}")
...     print(f"         group={groups\[test\_index\]}")
Fold 0:
  Train: index=\[ 0  1  2  3  7  8  9 10 11 15 16\]
         group=\[1 1 2 2 4 5 5 5 5 8 8\]
  Test:  index=\[ 4  5  6 12 13 14\]
         group=\[3 3 3 6 6 7\]
Fold 1:
  Train: index=\[ 4  5  6  7  8  9 10 11 12 13 14\]
         group=\[3 3 3 4 5 5 5 5 6 6 7\]
  Test:  index=\[ 0  1  2  3 15 16\]
         group=\[1 1 2 2 8 8\]
Fold 2:
  Train: index=\[ 0  1  2  3  4  5  6 12 13 14 15 16\]
         group=\[1 1 2 2 3 3 3 6 6 7 8 8\]
  Test:  index=\[ 7  8  9 10 11\]
         group=\[4 5 5 5 5\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L414)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold.get_n_splits "Link to this definition")

Returns the number of splitting iterations as set with the `n_splits` param when instantiating the cross-validator.

Parameters:

**X**array-like of shape (n\_samples, n\_features), default=None

Always ignored, exists for API compatibility.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

Returns:

**n\_splits**int

Returns the number of splitting iterations in the cross-validator.

set\_split\_request(_\*_, _groups: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [StratifiedGroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection._split.StratifiedGroupKFold")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold.set_split_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `split` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `split` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `split`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**groups**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `groups` parameter in `split`.

Returns:

**self**object

The updated object.

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L377)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold.split "Link to this definition")

Generate indices to split data into training and test set.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,), default=None

The target variable for supervised learning problems.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set.

Yields:

**train**ndarray

The training set indices for that split.

**test**ndarray

The testing set indices for that split.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_thumb.png)

[Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)

Visualizing cross-validation behavior in scikit-learn

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)