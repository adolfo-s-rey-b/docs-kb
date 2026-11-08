[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html)

Collapse Sidebar Expand Sidebar

LeaveOneGroupOut[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#leaveonegroupout "Link to this heading")

=============================================================================================================================================================

class sklearn.model\_selection.LeaveOneGroupOut[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1330)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "Link to this definition")

Leave One Group Out cross-validator.

Provides train/test indices to split data such that each training set is comprised of all samples except ones belonging to one specific group. Arbitrary domain-specific group information is provided as an array of integers that encodes the group of each sample.

For instance the groups could be the year of collection of the samples and thus allow for cross-validation against time-based splits.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#leave-one-group-out)
.

See also

[`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")

K-fold iterator variant with non-overlapping groups.

Notes

Splits are ordered according to the index of the group left out. The first split has testing set consisting of the group whose index in `groups` is lowest, and so on.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import LeaveOneGroupOut
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\], \[7, 8\]\])
\>>> y \= np.array(\[1, 2, 1, 2\])
\>>> groups \= np.array(\[1, 1, 2, 2\])
\>>> logo \= LeaveOneGroupOut()
\>>> logo.get\_n\_splits(groups\=groups)
2
\>>> print(logo)
LeaveOneGroupOut()
\>>> for i, (train\_index, test\_index) in enumerate(logo.split(X, y, groups)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}, group={groups\[train\_index\]}")
...     print(f"  Test:  index={test\_index}, group={groups\[test\_index\]}")
Fold 0:
  Train: index=\[2 3\], group=\[2 2\]
  Test:  index=\[0 1\], group=\[1 1\]
Fold 1:
  Train: index=\[0 1\], group=\[1 1\]
  Test:  index=\[2 3\], group=\[2 2\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1393)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut.get_n_splits "Link to this definition")

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
 \= '$UNCHANGED$'_) → [LeaveOneGroupOut](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection._split.LeaveOneGroupOut")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut.set_split_request "Link to this definition")

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

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1420)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut.split "Link to this definition")

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