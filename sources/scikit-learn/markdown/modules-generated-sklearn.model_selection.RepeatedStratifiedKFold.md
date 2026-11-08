[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html)

Collapse Sidebar Expand Sidebar

RepeatedStratifiedKFold[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#repeatedstratifiedkfold "Link to this heading")

==================================================================================================================================================================================

class sklearn.model\_selection.RepeatedStratifiedKFold(_\*_, _n\_splits\=5_, _n\_repeats\=10_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1749)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "Link to this definition")

Repeated class-wise stratified K-Fold cross validator.

Repeats Stratified K-Fold n times with different randomization in each repetition.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#repeated-k-fold)
.

Note

Stratification on the class label solves an engineering problem rather than a statistical one. See [Cross-validation iterators with stratification based on class labels](https://scikit-learn.org/stable/modules/cross_validation.html#stratification)
 for more details.

Parameters:

**n\_splits**int, default=5

Number of folds. Must be at least 2.

**n\_repeats**int, default=10

Number of times cross-validator needs to be repeated.

**random\_state**int, RandomState instance or None, default=None

Controls the generation of the random states for each repetition. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

See also

[`RepeatedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold")

Repeats K-Fold n times.

Notes

Randomized CV splitters may return different results for each call of split. You can make the results identical by setting `random_state` to an integer.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import RepeatedStratifiedKFold
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[1, 2\], \[3, 4\]\])
\>>> y \= np.array(\[0, 0, 1, 1\])
\>>> rskf \= RepeatedStratifiedKFold(n\_splits\=2, n\_repeats\=2,
...     random\_state\=36851234)
\>>> rskf.get\_n\_splits()
4
\>>> print(rskf)
RepeatedStratifiedKFold(n\_repeats=2, n\_splits=2, random\_state=36851234)
\>>> for i, (train\_index, test\_index) in enumerate(rskf.split(X, y)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
...
Fold 0:
  Train: index=\[1 2\]
  Test:  index=\[0 3\]
Fold 1:
  Train: index=\[0 3\]
  Test:  index=\[1 2\]
Fold 2:
  Train: index=\[1 3\]
  Test:  index=\[0 2\]
Fold 3:
  Train: index=\[0 2\]
  Test:  index=\[1 3\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1655)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold.get_n_splits "Link to this definition")

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

split(_X_, _y_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1824)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold.split "Link to this definition")

Generate indices to split data into training and test set.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

Note that providing `y` is sufficient to generate the splits and hence `np.zeros(n_samples)` may be used as a placeholder for `X` instead of actual training data.

**y**array-like of shape (n\_samples,)

The target variable for supervised learning problems. Stratification is done based on the y labels.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

Yields:

**train**ndarray

The training set indices for that split.

**test**ndarray

The testing set indices for that split.

Notes

Randomized CV splitters may return different results for each call of split. You can make the results identical by setting `random_state` to an integer.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_thumb.png)

[Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html)

Statistical comparison of models using grid search

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)