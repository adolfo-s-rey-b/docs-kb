[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_breast_cancer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_breast_cancer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_breast_cancer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_breast_cancer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_breast_cancer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_breast_cancer.html)

Collapse Sidebar Expand Sidebar

load\_breast\_cancer[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#load-breast-cancer "Link to this heading")

==============================================================================================================================================================

sklearn.datasets.load\_breast\_cancer(_\*_, _return\_X\_y\=False_, _as\_frame\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L750)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "Link to this definition")

Load and return the breast cancer Wisconsin dataset (classification).

The breast cancer dataset is a classic and very easy binary classification dataset.

|     |     |
| --- | --- |
| Classes | 2   |
| Samples per class | 212(M),357(B) |
| Samples total | 569 |
| Dimensionality | 30  |
| Features | real, positive |

The copy of UCI ML Breast Cancer Wisconsin (Diagnostic) dataset is downloaded from: [https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset)
.

Parameters:

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a Bunch object. See below for more information about the `data` and `target` objects.

Added in version 0.18.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric). The target is a pandas DataFrame or Series depending on the number of target columns. If `return_X_y` is True, then (`data`, `target`) will be pandas DataFrames or Series as described below.

Added in version 0.23.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data{ndarray, dataframe} of shape (569, 30)

The data matrix. If `as_frame=True`, `data` will be a pandas DataFrame.

target{ndarray, Series} of shape (569,)

The classification target. If `as_frame=True`, `target` will be a pandas Series.

feature\_namesndarray of shape (30,)

The names of the dataset columns.

target\_namesndarray of shape (2,)

The names of target classes.

frameDataFrame of shape (569, 31)

Only present when `as_frame=True`. DataFrame with `data` and `target`.

Added in version 0.23.

DESCRstr

The full description of the dataset.

filenamestr

The path to the location of the data.

Added in version 0.20.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarrays. The first contains a 2D ndarray of shape (569, 30) with each row representing one sample and the columns representing the features. The second ndarray of shape (569,) contains the target samples. If `as_frame=True`, both arrays are pandas objects, i.e. `X` a dataframe and `y` a series.

Added in version 0.18.

Examples

Let’s say you are interested in the samples 10, 50, and 85, and want to know their class name.

\>>> from sklearn.datasets import load\_breast\_cancer
\>>> data \= load\_breast\_cancer()
\>>> data.target\[\[10, 50, 85\]\]
array(\[0, 1, 0\])
\>>> list(data.target\_names)
\[np.str\_('malignant'), np.str\_('benign')\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)

[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

Permutation Importance with Multicollinear or Correlated Features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_complexity_pruning_thumb.png)

[Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html)

Post pruning decision trees with cost complexity pruning

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)