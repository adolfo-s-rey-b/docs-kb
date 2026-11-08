[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.GroupShuffleSplit.html)

Collapse Sidebar Expand Sidebar

GroupShuffleSplit[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#groupshufflesplit "Link to this heading")

================================================================================================================================================================

class sklearn.model\_selection.GroupShuffleSplit(_n\_splits\=5_, _\*_, _test\_size\=None_, _train\_size\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2087)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "Link to this definition")

Shuffle-Group(s)-Out cross-validation iterator.

Provides randomized train/test indices to split data according to a third-party provided group. This group information can be used to encode arbitrary domain-specific groupings of the samples as integers.

For instance the groups could be the year of collection of the samples and thus allow for cross-validation against time-based splits.

The difference between [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
 and `GroupShuffleSplit` is that the former generates splits using all subsets of size `p` unique groups, whereas `GroupShuffleSplit` generates a user-determined number of random test splits, each with a user-determined fraction of unique groups.

For example, a less computationally intensive alternative to `LeavePGroupsOut(p=10)` would be `GroupShuffleSplit(test_size=10, n_splits=100)`.

Contrary to other cross-validation strategies, the random splits do not guarantee that test sets across all folds will be mutually exclusive, and might include overlapping samples. However, this is still very likely for sizeable datasets.

Note: The parameters `test_size` and `train_size` refer to groups, and not to samples as in [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#group-shuffle-split)
.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to [Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-auto-examples-model-selection-plot-cv-indices-py)

Parameters:

**n\_splits**int, default=5

Number of re-shuffling & splitting iterations.

**test\_size**float, int, default=None

If float, should be between 0.0 and 1.0 and represent the proportion of groups to include in the test split (rounded up). If int, represents the absolute number of test groups. If None, the value is set to the complement of the train size. If `train_size` is also None, it will be set to 0.2.

**train\_size**float or int, default=None

If float, should be between 0.0 and 1.0 and represent the proportion of the groups to include in the train split. If int, represents the absolute number of train groups. If None, the value is automatically set to the complement of the test size.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of the training and testing indices produced. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

See also

[`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")

Shuffles samples to create independent test/train sets.

[`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")

Train set leaves out all possible subsets of `p` groups.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import GroupShuffleSplit
\>>> X \= np.ones(shape\=(8, 2))
\>>> y \= np.ones(shape\=(8, 1))
\>>> groups \= np.array(\[1, 1, 2, 2, 2, 3, 3, 3\])
\>>> print(groups.shape)
(8,)
\>>> gss \= GroupShuffleSplit(n\_splits\=2, train\_size\=.7, random\_state\=42)
\>>> gss.get\_n\_splits()
2
\>>> print(gss)
GroupShuffleSplit(n\_splits=2, random\_state=42, test\_size=None, train\_size=0.7)
\>>> for i, (train\_index, test\_index) in enumerate(gss.split(X, y, groups)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}, group={groups\[train\_index\]}")
...     print(f"  Test:  index={test\_index}, group={groups\[test\_index\]}")
Fold 0:
  Train: index=\[2 3 4 5 6 7\], group=\[2 2 2 3 3 3\]
  Test:  index=\[0 1\], group=\[1 1\]
Fold 1:
  Train: index=\[0 1 5 6 7\], group=\[1 1 3 3 3\]
  Test:  index=\[2 3 4\], group=\[2 2 2\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1956)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit.get_n_splits "Link to this definition")

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
 \= '$UNCHANGED$'_) → [GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection._split.GroupShuffleSplit")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit.set_split_request "Link to this definition")

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

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2200)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit.split "Link to this definition")

Generate indices to split data into training and test set.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,), default=None

The target variable for supervised learning problems.

**groups**array-like of shape (n\_samples,)

Group labels for the samples used while splitting the dataset into train/test set.

Yields:

**train**ndarray

The training set indices for that split.

**test**ndarray

The testing set indices for that split.

Notes

Randomized CV splitters may return different results for each call of split. You can make the results identical by setting `random_state` to an integer.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

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