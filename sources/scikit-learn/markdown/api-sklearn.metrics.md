[Skip to main content](https://scikit-learn.org/stable/api/sklearn.metrics.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.metrics.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.metrics.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.metrics.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.metrics.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.metrics.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.metrics.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.metrics.html)

Collapse Sidebar Expand Sidebar

sklearn.metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "Link to this heading")

===========================================================================================================================

Score functions, performance metrics, pairwise metrics and distance computations.

**User guide.** See the [Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation)
 and [Pairwise metrics, Affinities and Kernels](https://scikit-learn.org/stable/modules/metrics.html#metrics)
 sections for further details.

Model selection interface[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#model-selection-interface "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

**User guide.** See the [The scoring parameter: defining model evaluation rules](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
 section for further details.

|     |     |
| --- | --- |
| [`check_scoring`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "sklearn.metrics.check_scoring") | Determine scorer from user options. |
| [`get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer") | Get a scorer from string. |
| [`get_scorer_names`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#sklearn.metrics.get_scorer_names "sklearn.metrics.get_scorer_names") | Get the names of all available scorers. |
| [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer") | Make a scorer from a performance metric or loss function. |

Classification metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#classification-metrics "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

**User guide.** See the [Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
 section for further details.

|     |     |
| --- | --- |
| [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score") | Accuracy classification score. |
| [`auc`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc") | Compute Area Under the Curve (AUC) using the trapezoidal rule. |
| [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score") | Compute average precision (AP) from prediction scores. |
| [`balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score") | Compute the balanced accuracy. |
| [`brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss") | Compute the Brier score loss. |
| [`class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios") | Compute binary classification positive and negative likelihood ratios. |
| [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report") | Build a text report showing the main classification metrics. |
| [`cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score") | Compute Cohen's kappa: a statistic that measures inter-annotator agreement. |
| [`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix") | Compute confusion matrix to evaluate the accuracy of a classification. |
| [`confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds") | Calculate [binary](https://scikit-learn.org/stable/glossary.html#term-binary)<br> confusion matrix terms per classification threshold. |
| [`d2_brier_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "sklearn.metrics.d2_brier_score") | D2 score function, fraction of Brier score explained. |
| [`d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score") | D2 score function, fraction of log loss explained. |
| [`dcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#sklearn.metrics.dcg_score "sklearn.metrics.dcg_score") | Compute Discounted Cumulative Gain. |
| [`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve") | Compute Detection Error Tradeoff (DET) for different probability thresholds. |
| [`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score") | Compute the F1 score, also known as balanced F-score or F-measure. |
| [`fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score") | Compute the F-beta score. |
| [`hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss") | Compute the average Hamming loss. |
| [`hinge_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#sklearn.metrics.hinge_loss "sklearn.metrics.hinge_loss") | Average hinge loss (non-regularized). |
| [`jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score") | Jaccard similarity coefficient score. |
| [`log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss") | Log loss, aka logistic loss or cross-entropy loss. |
| [`matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef") | Compute the Matthews correlation coefficient (MCC). |
| [`metric_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html#sklearn.metrics.metric_at_thresholds "sklearn.metrics.metric_at_thresholds") | Compute `metric_func` per threshold for [binary](https://scikit-learn.org/stable/glossary.html#term-binary)<br> data. |
| [`multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix") | Compute a confusion matrix for each class or sample. |
| [`ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score") | Compute Normalized Discounted Cumulative Gain. |
| [`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve") | Compute precision-recall pairs for different probability thresholds. |
| [`precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support") | Compute precision, recall, F-measure and support for each class. |
| [`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score") | Compute the precision. |
| [`recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score") | Compute the recall. |
| [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score") | Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores. |
| [`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve") | Compute Receiver operating characteristic (ROC). |
| [`top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "sklearn.metrics.top_k_accuracy_score") | Top-k Accuracy classification score. |
| [`zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss") | Zero-one classification loss. |

Regression metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#regression-metrics "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

**User guide.** See the [Regression metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)
 section for further details.

|     |     |
| --- | --- |
| [`d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score") | D2 regression score function, fraction of absolute error explained. |
| [`d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score") | D2 regression score function, fraction of pinball loss explained. |
| [`d2_tweedie_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "sklearn.metrics.d2_tweedie_score") | D2 regression score function, fraction of Tweedie deviance explained. |
| [`explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score") | Explained variance regression score function. |
| [`max_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "sklearn.metrics.max_error") | The max\_error metric calculates the maximum residual error. |
| [`mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error") | Mean absolute error regression loss. |
| [`mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error") | Mean absolute percentage error (MAPE) regression loss. |
| [`mean_gamma_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "sklearn.metrics.mean_gamma_deviance") | Mean Gamma deviance regression loss. |
| [`mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss") | Pinball loss for quantile regression. |
| [`mean_poisson_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance") | Mean Poisson deviance regression loss. |
| [`mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error") | Mean squared error regression loss. |
| [`mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error") | Mean squared logarithmic error regression loss. |
| [`mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance") | Mean Tweedie deviance regression loss. |
| [`median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error") | Median absolute error regression loss. |
| [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score") | R2 (coefficient of determination) regression score function. |
| [`root_mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error") | Root mean squared error regression loss. |
| [`root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error") | Root mean squared logarithmic error regression loss. |

Multilabel ranking metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#multilabel-ranking-metrics "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

**User guide.** See the [Multilabel ranking metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#multilabel-ranking-metrics)
 section for further details.

|     |     |
| --- | --- |
| [`coverage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#sklearn.metrics.coverage_error "sklearn.metrics.coverage_error") | Coverage error measure. |
| [`label_ranking_average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "sklearn.metrics.label_ranking_average_precision_score") | Compute ranking-based average precision. |
| [`label_ranking_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html#sklearn.metrics.label_ranking_loss "sklearn.metrics.label_ranking_loss") | Compute Ranking loss measure. |

Clustering metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics.cluster "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Evaluation metrics for cluster analysis results.

*   Supervised evaluation uses a ground truth class values for each sample.
    
*   Unsupervised evaluation does not use ground truths and measures the “quality” of the model itself.
    

**User guide.** See the [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
 section for further details.

|     |     |
| --- | --- |
| [`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score") | Adjusted Mutual Information between two clusterings. |
| [`adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score") | Rand index adjusted for chance. |
| [`calinski_harabasz_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score "sklearn.metrics.calinski_harabasz_score") | Compute the Calinski and Harabasz score. |
| [`cluster.contingency_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html#sklearn.metrics.cluster.contingency_matrix "sklearn.metrics.cluster.contingency_matrix") | Build a contingency matrix describing the relationship between labels. |
| [`cluster.pair_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#sklearn.metrics.cluster.pair_confusion_matrix "sklearn.metrics.cluster.pair_confusion_matrix") | Pair confusion matrix arising from two clusterings. |
| [`completeness_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score") | Compute completeness metric of a cluster labeling given a ground truth. |
| [`davies_bouldin_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html#sklearn.metrics.davies_bouldin_score "sklearn.metrics.davies_bouldin_score") | Compute the Davies-Bouldin score. |
| [`fowlkes_mallows_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#sklearn.metrics.fowlkes_mallows_score "sklearn.metrics.fowlkes_mallows_score") | Measure the similarity of two clusterings of a set of points. |
| [`homogeneity_completeness_v_measure`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html#sklearn.metrics.homogeneity_completeness_v_measure "sklearn.metrics.homogeneity_completeness_v_measure") | Compute the homogeneity and completeness and V-Measure scores at once. |
| [`homogeneity_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score") | Homogeneity metric of a cluster labeling given a ground truth. |
| [`mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score") | Mutual Information between two clusterings. |
| [`normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score") | Normalized Mutual Information between two clusterings. |
| [`rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score "sklearn.metrics.rand_score") | Rand index. |
| [`silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples") | Compute the Silhouette Coefficient for each sample. |
| [`silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score") | Compute the mean Silhouette Coefficient of all samples. |
| [`v_measure_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score") | V-measure cluster labeling given a ground truth. |

Biclustering metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#biclustering-metrics "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

**User guide.** See the [Biclustering evaluation](https://scikit-learn.org/stable/modules/biclustering.html#biclustering-evaluation)
 section for further details.

|     |     |
| --- | --- |
| [`consensus_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score") | The similarity of two sets of biclusters. |

Distance metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#distance-metrics "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric") | Uniform interface for fast distance metric functions. |

Pairwise metrics[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics.pairwise "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Metrics for pairwise distances and affinity of sets of samples.

**User guide.** See the [Pairwise metrics, Affinities and Kernels](https://scikit-learn.org/stable/modules/metrics.html#metrics)
 section for further details.

|     |     |
| --- | --- |
| [`pairwise.additive_chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#sklearn.metrics.pairwise.additive_chi2_kernel "sklearn.metrics.pairwise.additive_chi2_kernel") | Compute the additive chi-squared kernel between observations in X and Y. |
| [`pairwise.chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.chi2_kernel.html#sklearn.metrics.pairwise.chi2_kernel "sklearn.metrics.pairwise.chi2_kernel") | Compute the exponential chi-squared kernel between X and Y. |
| [`pairwise.cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "sklearn.metrics.pairwise.cosine_distances") | Compute cosine distance between samples in X and Y. |
| [`pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity") | Compute cosine similarity between samples in X and Y. |
| [`pairwise.distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics") | Valid metrics for pairwise\_distances. |
| [`pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances") | Compute the distance matrix between each pair from a feature array X and Y. |
| [`pairwise.haversine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html#sklearn.metrics.pairwise.haversine_distances "sklearn.metrics.pairwise.haversine_distances") | Compute the Haversine distance between samples in X and Y. |
| [`pairwise.kernel_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#sklearn.metrics.pairwise.kernel_metrics "sklearn.metrics.pairwise.kernel_metrics") | Valid metrics for pairwise\_kernels. |
| [`pairwise.laplacian_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#sklearn.metrics.pairwise.laplacian_kernel "sklearn.metrics.pairwise.laplacian_kernel") | Compute the laplacian kernel between X and Y. |
| [`pairwise.linear_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html#sklearn.metrics.pairwise.linear_kernel "sklearn.metrics.pairwise.linear_kernel") | Compute the linear kernel between X and Y. |
| [`pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances") | Compute the L1 distances between the vectors in X and Y. |
| [`pairwise.nan_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#sklearn.metrics.pairwise.nan_euclidean_distances "sklearn.metrics.pairwise.nan_euclidean_distances") | Calculate the euclidean distances in the presence of missing values. |
| [`pairwise.paired_cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_cosine_distances.html#sklearn.metrics.pairwise.paired_cosine_distances "sklearn.metrics.pairwise.paired_cosine_distances") | Compute the paired cosine distances between X and Y. |
| [`pairwise.paired_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "sklearn.metrics.pairwise.paired_distances") | Compute the paired distances between X and Y. |
| [`pairwise.paired_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_euclidean_distances.html#sklearn.metrics.pairwise.paired_euclidean_distances "sklearn.metrics.pairwise.paired_euclidean_distances") | Compute the paired euclidean distances between X and Y. |
| [`pairwise.paired_manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#sklearn.metrics.pairwise.paired_manhattan_distances "sklearn.metrics.pairwise.paired_manhattan_distances") | Compute the paired L1 distances between X and Y. |
| [`pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels") | Compute the kernel between arrays X and optional array Y. |
| [`pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel") | Compute the polynomial kernel between X and Y. |
| [`pairwise.rbf_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel") | Compute the rbf (gaussian) kernel between X and Y. |
| [`pairwise.sigmoid_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#sklearn.metrics.pairwise.sigmoid_kernel "sklearn.metrics.pairwise.sigmoid_kernel") | Compute the sigmoid kernel between X and Y. |
| [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances") | Compute the distance matrix from a feature array X and optional Y. |
| [`pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin") | Compute minimum distances between one point and a set of points. |
| [`pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min") | Compute minimum distances between one point and a set of points. |
| [`pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked") | Generate a distance matrix chunk by chunk with optional reduction. |

Plotting[#](https://scikit-learn.org/stable/api/sklearn.metrics.html#plotting "Link to this heading")

------------------------------------------------------------------------------------------------------

**User guide.** See the [Visualizations](https://scikit-learn.org/stable/visualizations.html#visualizations)
 section for further details.

|     |     |
| --- | --- |
| [`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay") | Confusion Matrix visualization. |
| [`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay") | Detection Error Tradeoff (DET) curve visualization. |
| [`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay") | Precision Recall visualization. |
| [`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay") | Visualization of the prediction error of a regression model. |
| [`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay") | ROC Curve visualization. |