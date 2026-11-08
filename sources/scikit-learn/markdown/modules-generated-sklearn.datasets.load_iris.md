[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_iris.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_iris.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_iris.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_iris.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_iris.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_iris.html)

Collapse Sidebar Expand Sidebar

load\_iris[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#load-iris "Link to this heading")

==================================================================================================================================

sklearn.datasets.load\_iris(_\*_, _return\_X\_y\=False_, _as\_frame\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L621)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "Link to this definition")

Load and return the iris dataset (classification).

The iris dataset is a classic and very easy multi-class classification dataset.

|     |     |
| --- | --- |
| Classes | 3   |
| Samples per class | 50  |
| Samples total | 150 |
| Dimensionality | 4   |
| Features | real, positive |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)
.

Changed in version 0.20: Fixed two wrong data points according to Fisher’s paper. The new version is the same as in R, but not as in the UCI Machine Learning Repository.

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

data{ndarray, dataframe} of shape (150, 4)

The data matrix. If `as_frame=True`, `data` will be a pandas DataFrame.

target: {ndarray, Series} of shape (150,)

The classification target. If `as_frame=True`, `target` will be a pandas Series.

feature\_names: list

The names of the dataset columns.

target\_names: ndarray of shape (3, )

The names of target classes.

frame: DataFrame of shape (150, 5)

Only present when `as_frame=True`. DataFrame with `data` and `target`.

Added in version 0.23.

DESCR: str

The full description of the dataset.

filename: str

The path to the location of the data.

Added in version 0.20.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarrays. The first contains a 2D array of shape (150, 4) with each row representing one sample and the columns representing the features. The second ndarray of shape (150,) contains the target samples. If `as_frame=True`, both arrays are pandas objects, i.e. `X` a dataframe and `y` a series.

Added in version 0.18.

Examples

Let’s say you are interested in the samples 10, 25, and 50, and want to know their class name.

\>>> from sklearn.datasets import load\_iris
\>>> data \= load\_iris()
\>>> samples \= \[10, 25, 50\]
\>>> data.target\[samples\]
array(\[0, 0, 1\])
\>>> data.target\_names\[data.target\[samples\]\]
array(\['setosa', 'setosa', 'versicolor'\], dtype='<U10')

Copy to clipboard

See [Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-auto-examples-decomposition-plot-pca-iris-py)
 for a more detailed example of how to work with the iris dataset.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_dendrogram_thumb.png)

[Plot Hierarchical Clustering Dendrogram](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html)

Plot Hierarchical Clustering Dendrogram

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_thumb.png)

[Factor Analysis (with rotation) to visualize patterns](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html)

Factor Analysis (with rotation) to visualize patterns

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_thumb.png)

[GMM covariances](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html)

GMM covariances

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_thumb.png)

[Nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Nested versus non-nested cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_thumb.png)

[Test with permutations the significance of a classification score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Test with permutations the significance of a classification score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_thumb.png)

[Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)

Compare Stochastic learning strategies for MLPClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_unveil_tree_structure_thumb.png)

[Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html)

Understanding the decision tree structure

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)