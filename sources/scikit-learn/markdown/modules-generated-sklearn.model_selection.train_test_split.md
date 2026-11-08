[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.train_test_split.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.train_test_split.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.train_test_split.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.train_test_split.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.train_test_split.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.train_test_split.html)

Collapse Sidebar Expand Sidebar

train\_test\_split[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#train-test-split "Link to this heading")

===============================================================================================================================================================

sklearn.model\_selection.train\_test\_split(_\*arrays_, _test\_size\=None_, _train\_size\=None_, _random\_state\=None_, _shuffle\=True_, _stratify\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L2779)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "Link to this definition")

Split arrays or matrices into random train and test subsets.

Quick utility that wraps input validation, `next(ShuffleSplit().split(X, y))`, and application to input data into a single call for splitting (and optionally subsampling) data into a one-liner.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
.

Parameters:

**\*arrays**sequence of array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Indexable data-structures can be arrays, lists, dataframes, scipy sparse matrices or pandas dataframes with consistent first dimension.

**test\_size**float or int, default=None

If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If `train_size` is also None, it will be set to 0.25.

**train\_size**float or int, default=None

If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. If int, represents the absolute number of train samples. If None, the value is automatically set to the complement of the test size.

**random\_state**int, RandomState instance or None, default=None

Controls the shuffling applied to the data before applying the split. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**shuffle**bool, default=True

Whether or not to shuffle the data before splitting. If shuffle=False then stratify must be None.

**stratify**array-like of shape (n\_samples,), default=None

If not None, data is split in a stratified fashion, using this as the class labels. Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#stratification)
.

Returns:

**splitting**list, length=2 \* len(arrays)

List containing train-test split of inputs.

Added in version 0.16: If the input is sparse, the output will be a `scipy.sparse.csr_matrix`. Else, output type is the same as the input type.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import train\_test\_split
\>>> X, y \= np.arange(10).reshape((5, 2)), range(5)
\>>> X
array(\[\[0, 1\],\
       \[2, 3\],\
       \[4, 5\],\
       \[6, 7\],\
       \[8, 9\]\])
\>>> list(y)
\[0, 1, 2, 3, 4\]

Copy to clipboard

\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, test\_size\=0.33, random\_state\=42)
...
\>>> X\_train
array(\[\[4, 5\],\
       \[0, 1\],\
       \[6, 7\]\])
\>>> y\_train
\[2, 0, 3\]
\>>> X\_test
array(\[\[2, 3\],\
       \[8, 9\]\])
\>>> y\_test
\[1, 4\]

Copy to clipboard

\>>> train\_test\_split(y, shuffle\=False)
\[\[0, 1, 2\], \[3, 4\]\]

Copy to clipboard

\>>> from sklearn import datasets
\>>> iris \= datasets.load\_iris(as\_frame\=True)
\>>> X, y \= iris\['data'\], iris\['target'\]
\>>> X.head()
    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
\>>> y.head()
0    0
1    0
2    0
3    0
4    0
...

Copy to clipboard

\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
... X, y, test\_size\=0.33, random\_state\=42)
...
\>>> X\_train.head()
    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
96                 5.7               2.9                4.2               1.3
105                7.6               3.0                6.6               2.1
66                 5.6               3.0                4.5               1.5
0                  5.1               3.5                1.4               0.2
122                7.7               2.8                6.7               2.0
\>>> y\_train.head()
96     1
105    2
66     1
0      0
122    2
...
\>>> X\_test.head()
    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
73                 6.1               2.8                4.7               1.2
18                 5.7               3.8                1.7               0.3
118                7.7               2.6                6.9               2.3
78                 6.0               2.9                4.5               1.5
76                 6.8               2.8                4.8               1.4
\>>> y\_test.head()
73     1
18     0
118    2
78     1
76     1
...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_thumb.png)

[Prediction Latency](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html)

Prediction Latency

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)

[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Classifier comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_cross_decomposition_thumb.png)

[Compare cross decomposition methods](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)

Compare cross decomposition methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_thumb.png)

[Principal Component Regression vs Partial Least Squares Regression](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)

Principal Component Regression vs Partial Least Squares Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_thumb.png)

[Kernel PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html)

Kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_multiclass_thumb.png)

[Multi-class AdaBoosted Decision Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html)

Multi-class AdaBoosted Decision Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_thumb.png)

[Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

Feature importances with a forest of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)

[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Early stopping in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_oob_thumb.png)

[Gradient Boosting Out-of-Bag estimates](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html)

Gradient Boosting Out-of-Bag estimates

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)

[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Gradient Boosting regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_thumb.png)

[IsolationForest example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html)

IsolationForest example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_regression_multioutput_thumb.png)

[Comparing random forests and the multi-output meta estimator](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)

Comparing random forests and the multi-output meta estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_thumb.png)

[Failure of Machine Learning to infer causal effects](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html)

Failure of Machine Learning to infer causal effects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)

[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

Permutation Importance with Multicollinear or Correlated Features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scalable_poly_kernels_thumb.png)

[Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html)

Scalable learning with polynomial kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nnls_thumb.png)

[Non-negative least squares](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html)

Non-negative least squares

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_thumb.png)

[Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html)

Early stopping of Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_thumb.png)

[ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

ROC Curve with Visualization API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_likelihood_ratios_thumb.png)

[Class Likelihood Ratios to measure classification performance](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html)

Class Likelihood Ratios to measure classification performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_thumb.png)

[Multilabel classification using a classifier chain](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Multilabel classification using a classifier chain

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_thumb.png)

[Dimensionality Reduction with Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)

Dimensionality Reduction with Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mnist_filters_thumb.png)

[Visualization of MLP weights on MNIST](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html)

Visualization of MLP weights on MNIST

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_map_data_to_normal_thumb.png)

[Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html)

Map data to a normal distribution

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_cross_val_thumb.png)

[Target Encoder’s Internal Cross fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html)

Target Encoder's Internal Cross fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)

[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Semi-supervised Classification on a Text Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_complexity_pruning_thumb.png)

[Post pruning decision trees with cost complexity pruning](https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html)

Post pruning decision trees with cost complexity pruning

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