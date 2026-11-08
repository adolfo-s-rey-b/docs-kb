[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.PredefinedSplit.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.PredefinedSplit.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.PredefinedSplit.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.PredefinedSplit.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.PredefinedSplit.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.PredefinedSplit.html)

Collapse Sidebar Expand Sidebar

PredefinedSplit[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#predefinedsplit "Link to this heading")

==========================================================================================================================================================

class sklearn.model\_selection.PredefinedSplit(_test\_fold_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2520)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit "Link to this definition")

Predefined split cross-validator.

Provides train/test indices to split data into train/test sets using a predefined scheme specified by the user with the `test_fold` parameter.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#predefined-split)
.

Added in version 0.16.

Parameters:

**test\_fold**array-like of shape (n\_samples,)

The entry `test_fold[i]` represents the index of the test set that sample `i` belongs to. It is possible to exclude sample `i` from any test set (i.e. include sample `i` in every training set) by setting `test_fold[i]` equal to -1.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import PredefinedSplit
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[1, 2\], \[3, 4\]\])
\>>> y \= np.array(\[0, 0, 1, 1\])
\>>> test\_fold \= \[0, 1, \-1, 1\]
\>>> ps \= PredefinedSplit(test\_fold)
\>>> ps.get\_n\_splits()
2
\>>> print(ps)
PredefinedSplit(test\_fold=array(\[ 0,  1, -1,  1\]))
\>>> for i, (train\_index, test\_index) in enumerate(ps.split()):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[1 2 3\]
  Test:  index=\[0\]
Fold 1:
  Train: index=\[0 2\]
  Test:  index=\[1 3\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2622)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit.get_n_splits "Link to this definition")

Returns the number of splitting iterations in the cross-validator.

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

split(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2568)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit.split "Link to this definition")

Generate indices to split data into training and test set.

Parameters:

**X**array-like of shape (n\_samples, n\_features), default=None

Always ignored, exists for API compatibility.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

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