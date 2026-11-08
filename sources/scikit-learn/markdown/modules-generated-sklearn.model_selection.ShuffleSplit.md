[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.ShuffleSplit.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.ShuffleSplit.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.ShuffleSplit.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.ShuffleSplit.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.ShuffleSplit.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.ShuffleSplit.html)

Collapse Sidebar Expand Sidebar

ShuffleSplit[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#shufflesplit "Link to this heading")

=================================================================================================================================================

class sklearn.model\_selection.ShuffleSplit(_n\_splits\=10_, _\*_, _test\_size\=None_, _train\_size\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1982)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "Link to this definition")

Random permutation cross-validator.

Yields indices to split data into training and test sets.

Note: contrary to other cross-validation strategies, random splits do not guarantee that test sets across all folds will be mutually exclusive, and might include overlapping samples. However, this is still very likely for sizeable datasets.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#shufflesplit)
.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to [Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-auto-examples-model-selection-plot-cv-indices-py)

Parameters:

**n\_splits**int, default=10

Number of re-shuffling & splitting iterations.

**test\_size**float or int, default=None

If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If `train_size` is also None, it will be set to 0.1.

**train\_size**float or int, default=None

If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. If int, represents the absolute number of train samples. If None, the value is automatically set to the complement of the test size.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of the training and testing indices produced. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import ShuffleSplit
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\], \[7, 8\], \[3, 4\], \[5, 6\]\])
\>>> y \= np.array(\[1, 2, 1, 2, 1, 2\])
\>>> rs \= ShuffleSplit(n\_splits\=5, test\_size\=.25, random\_state\=0)
\>>> rs.get\_n\_splits()
5
\>>> print(rs)
ShuffleSplit(n\_splits=5, random\_state=0, test\_size=0.25, train\_size=None)
\>>> for i, (train\_index, test\_index) in enumerate(rs.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[1 3 0 4\]
  Test:  index=\[5 2\]
Fold 1:
  Train: index=\[4 0 2 5\]
  Test:  index=\[1 3\]
Fold 2:
  Train: index=\[1 2 4 0\]
  Test:  index=\[3 5\]
Fold 3:
  Train: index=\[3 4 1 0\]
  Test:  index=\[5 2\]
Fold 4:
  Train: index=\[3 5 1 0\]
  Test:  index=\[2 4\]
\>>> \# Specify train and test size
\>>> rs \= ShuffleSplit(n\_splits\=5, train\_size\=0.5, test\_size\=.25,
...                   random\_state\=0)
\>>> for i, (train\_index, test\_index) in enumerate(rs.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[1 3 0\]
  Test:  index=\[5 2\]
Fold 1:
  Train: index=\[4 0 2\]
  Test:  index=\[1 3\]
Fold 2:
  Train: index=\[1 2 4\]
  Test:  index=\[3 5\]
Fold 3:
  Train: index=\[3 4 1\]
  Test:  index=\[5 2\]
Fold 4:
  Train: index=\[3 5 1\]
  Test:  index=\[2 4\]

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1956)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit.get_n_splits "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit.split "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_thumb.png)

[Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)

Visualizing cross-validation behavior in scikit-learn

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_learning_curve_thumb.png)

[Plotting Learning Curves and Checking Models’ Scalability](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html)

Plotting Learning Curves and Checking Models' Scalability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)