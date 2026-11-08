[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.LeaveOneOut.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.LeaveOneOut.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.LeaveOneOut.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.LeaveOneOut.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.LeaveOneOut.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.LeaveOneOut.html)

Collapse Sidebar Expand Sidebar

LeaveOneOut[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#leaveoneout "Link to this heading")

==============================================================================================================================================

class sklearn.model\_selection.LeaveOneOut[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L171)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "Link to this definition")

Leave-One-Out cross-validator.

Provides train/test indices to split data in train/test sets. Each sample is used once as a test set (singleton) while the remaining samples form the training set.

Note: `LeaveOneOut()` is equivalent to `KFold(n_splits=n)` and `LeavePOut(p=1)` where `n` is the number of samples.

Due to the high number of test sets (which is the same as the number of samples) this cross-validation method can be very costly. For large datasets one should favor [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
, [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
 or [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#leave-one-out)
.

See also

[`LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut")

For splitting the data according to explicit, domain-specific grouping of the dataset.

[`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")

K-fold iterator variant with non-overlapping groups.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import LeaveOneOut
\>>> X \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> y \= np.array(\[1, 2\])
\>>> loo \= LeaveOneOut()
\>>> loo.get\_n\_splits(X)
2
\>>> print(loo)
LeaveOneOut()
\>>> for i, (train\_index, test\_index) in enumerate(loo.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[1\]
  Test:  index=\[0\]
Fold 1:
  Train: index=\[0\]
  Test:  index=\[1\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L225)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut.get_n_splits "Link to this definition")

Returns the number of splitting iterations in the cross-validator.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

Returns:

**n\_splits**int

Returns the number of splitting iterations in the cross-validator.

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L62)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut.split "Link to this definition")

Generate indices to split data into training and test set.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,), default=None

The target variable for supervised learning problems.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

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