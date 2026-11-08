[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.LeavePGroupsOut.html)

Collapse Sidebar Expand Sidebar

LeavePGroupsOut[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#leavepgroupsout "Link to this heading")

==========================================================================================================================================================

class sklearn.model\_selection.LeavePGroupsOut(_n\_groups_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1447)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "Link to this definition")

Leave P Group(s) Out cross-validator.

Provides train/test indices to split data according to a third-party provided group. This group information can be used to encode arbitrary domain-specific groupings of the samples as integers.

For instance the groups could be the year of collection of the samples and thus allow for cross-validation against time-based splits.

The difference between LeavePGroupsOut and LeaveOneGroupOut is that the former builds the test sets with all the samples assigned to `p` different values of the groups while the latter uses samples all assigned the same groups.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#leave-p-groups-out)
.

Parameters:

**n\_groups**int

Number of groups (`p`) to leave out in the test split.

See also

[`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")

K-fold iterator variant with non-overlapping groups.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import LeavePGroupsOut
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
\>>> y \= np.array(\[1, 2, 1\])
\>>> groups \= np.array(\[1, 2, 3\])
\>>> lpgo \= LeavePGroupsOut(n\_groups\=2)
\>>> lpgo.get\_n\_splits(groups\=groups)
3
\>>> print(lpgo)
LeavePGroupsOut(n\_groups=2)
\>>> for i, (train\_index, test\_index) in enumerate(lpgo.split(X, y, groups)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}, group={groups\[train\_index\]}")
...     print(f"  Test:  index={test\_index}, group={groups\[test\_index\]}")
Fold 0:
  Train: index=\[2\], group=\[3\]
  Test:  index=\[0 1\], group=\[1 2\]
Fold 1:
  Train: index=\[1\], group=\[2\]
  Test:  index=\[0 2\], group=\[1 3\]
Fold 2:
  Train: index=\[0\], group=\[1\]
  Test:  index=\[1 2\], group=\[2 3\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1524)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut.get_n_splits "Link to this definition")

Returns the number of splitting iterations in the cross-validator.

Parameters:

**X**array-like of shape (n\_samples, n\_features), default=None

Always ignored, exists for API compatibility.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. This ‘groups’ parameter must always be specified to calculate the number of splits, though the other parameters can be omitted.

Returns:

**n\_splits**int

Returns the number of splitting iterations in the cross-validator.

set\_split\_request(_\*_, _groups: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LeavePGroupsOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection._split.LeavePGroupsOut")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut.set_split_request "Link to this definition")

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

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1551)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut.split "Link to this definition")

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

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)