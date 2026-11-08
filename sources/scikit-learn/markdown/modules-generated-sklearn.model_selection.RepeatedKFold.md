[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.RepeatedKFold.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.RepeatedKFold.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.RepeatedKFold.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.RepeatedKFold.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.RepeatedKFold.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.RepeatedKFold.html)

Collapse Sidebar Expand Sidebar

RepeatedKFold[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#repeatedkfold "Link to this heading")

====================================================================================================================================================

class sklearn.model\_selection.RepeatedKFold(_\*_, _n\_splits\=5_, _n\_repeats\=10_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1683)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "Link to this definition")

Repeated K-Fold cross validator.

Repeats K-Fold `n_repeats` times with different randomization in each repetition.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#repeated-k-fold)
.

Parameters:

**n\_splits**int, default=5

Number of folds. Must be at least 2.

**n\_repeats**int, default=10

Number of times cross-validator needs to be repeated.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of each repeated cross-validation instance. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

See also

[`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")

Repeats Stratified K-Fold n times.

Notes

Randomized CV splitters may return different results for each call of split. You can make the results identical by setting `random_state` to an integer.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import RepeatedKFold
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[1, 2\], \[3, 4\]\])
\>>> y \= np.array(\[0, 0, 1, 1\])
\>>> rkf \= RepeatedKFold(n\_splits\=2, n\_repeats\=2, random\_state\=2652124)
\>>> rkf.get\_n\_splits()
4
\>>> print(rkf)
RepeatedKFold(n\_repeats=2, n\_splits=2, random\_state=2652124)
\>>> for i, (train\_index, test\_index) in enumerate(rkf.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
...
Fold 0:
  Train: index=\[0 1\]
  Test:  index=\[2 3\]
Fold 1:
  Train: index=\[2 3\]
  Test:  index=\[0 1\]
Fold 2:
  Train: index=\[1 2\]
  Test:  index=\[0 3\]
Fold 3:
  Train: index=\[0 3\]
  Test:  index=\[1 2\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1655)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold.get_n_splits "Link to this definition")

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

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L62)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold.split "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)