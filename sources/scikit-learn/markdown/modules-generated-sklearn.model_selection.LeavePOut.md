[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.LeavePOut.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.LeavePOut.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.LeavePOut.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.LeavePOut.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.LeavePOut.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.LeavePOut.html)

Collapse Sidebar Expand Sidebar

LeavePOut[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#leavepout "Link to this heading")

========================================================================================================================================

class sklearn.model\_selection.LeavePOut(_p_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L250)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut "Link to this definition")

Leave-P-Out cross-validator.

Provides train/test indices to split data in train/test sets. This results in testing on all distinct samples of size p, while the remaining n - p samples form the training set in each iteration.

Note: `LeavePOut(p)` is NOT equivalent to `KFold(n_splits=n_samples // p)` which creates non-overlapping test sets.

Due to the high number of iterations which grows combinatorically with the number of samples this cross-validation method can be very costly. For large datasets one should favor [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 or [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#leave-p-out)
.

Parameters:

**p**int

Size of the test sets. Must be strictly less than the number of samples.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import LeavePOut
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\], \[7, 8\]\])
\>>> y \= np.array(\[1, 2, 3, 4\])
\>>> lpo \= LeavePOut(2)
\>>> lpo.get\_n\_splits(X)
6
\>>> print(lpo)
LeavePOut(p=2)
\>>> for i, (train\_index, test\_index) in enumerate(lpo.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[2 3\]
  Test:  index=\[0 1\]
Fold 1:
  Train: index=\[1 3\]
  Test:  index=\[0 2\]
Fold 2:
  Train: index=\[1 2\]
  Test:  index=\[0 3\]
Fold 3:
  Train: index=\[0 3\]
  Test:  index=\[1 2\]
Fold 4:
  Train: index=\[0 2\]
  Test:  index=\[1 3\]
Fold 5:
  Train: index=\[0 1\]
  Test:  index=\[2 3\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L322)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut.get_n_splits "Link to this definition")

Returns the number of splitting iterations in the cross-validator.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L62)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut.split "Link to this definition")

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