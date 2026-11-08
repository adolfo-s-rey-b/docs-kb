[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.StratifiedKFold.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.StratifiedKFold.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.StratifiedKFold.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.StratifiedKFold.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.StratifiedKFold.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.StratifiedKFold.html)

Collapse Sidebar Expand Sidebar

StratifiedKFold[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#stratifiedkfold "Link to this heading")

==========================================================================================================================================================

class sklearn.model\_selection.StratifiedKFold(_n\_splits\=5_, _\*_, _shuffle\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L687)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "Link to this definition")

Class-wise stratified K-Fold cross-validator.

Provides train/test indices to split data in train/test sets.

This cross-validation object is a variation of KFold that returns stratified folds. The folds are made by preserving the percentage of samples for each class in `y` in a binary or multiclass classification setting.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#stratified-k-fold)
.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to [Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-auto-examples-model-selection-plot-cv-indices-py)

Note

Stratification on the class label solves an engineering problem rather than a statistical one. See [Cross-validation iterators with stratification based on class labels](https://scikit-learn.org/stable/modules/cross_validation.html#stratification)
 for more details.

Parameters:

**n\_splits**int, default=5

Number of folds. Must be at least 2.

Changed in version 0.22: `n_splits` default value changed from 3 to 5.

**shuffle**bool, default=False

Whether to shuffle each class’s samples before splitting into batches. Note that the samples within each split will not be shuffled.

**random\_state**int, RandomState instance or None, default=None

When `shuffle` is True, `random_state` affects the ordering of the indices, which controls the randomness of each fold for each class. Otherwise, leave `random_state` as `None`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

See also

[`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")

Repeats Stratified K-Fold n times.

Notes

The implementation is designed to:

*   Generate test sets such that all contain the same distribution of classes, or as close as possible.
    
*   Be invariant to class label: relabelling `y = ["Happy", "Sad"]` to `y = [1, 0]` should not change the indices generated.
    
*   Preserve order dependencies in the dataset ordering, when `shuffle=False`: all samples from class k in some test set were contiguous in y, or separated in y by samples from classes other than k.
    
*   Generate test sets where the smallest and largest differ by at most one sample.
    

Changed in version 0.22: The previous implementation did not follow the last constraint.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import StratifiedKFold
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[1, 2\], \[3, 4\]\])
\>>> y \= np.array(\[0, 0, 1, 1\])
\>>> skf \= StratifiedKFold(n\_splits\=2)
\>>> skf.get\_n\_splits()
2
\>>> print(skf)
StratifiedKFold(n\_splits=2, random\_state=None, shuffle=False)
\>>> for i, (train\_index, test\_index) in enumerate(skf.split(X, y)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[1 3\]
  Test:  index=\[0 2\]
Fold 1:
  Train: index=\[0 2\]
  Test:  index=\[1 3\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L414)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold.get_n_splits "Link to this definition")

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

split(_X_, _y_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L849)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold.split "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)

[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Recursive feature elimination with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_thumb.png)

[GMM covariances](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html)

GMM covariances

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_thumb.png)

[Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)

Visualizing cross-validation behavior in scikit-learn

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_thumb.png)

[Test with permutations the significance of a classification score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Test with permutations the significance of a classification score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)