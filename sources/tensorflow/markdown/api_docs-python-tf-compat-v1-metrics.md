[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.metrics Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics#functions)
    

Public API for tf.\_api.v2.metrics namespace

Functions
---------

[`accuracy(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy)
: Calculates how often `predictions` matches `labels`.

[`auc(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/auc)
: Computes the approximate AUC via a Riemann sum. (deprecated)

[`average_precision_at_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/average_precision_at_k)
: Computes average precision@k of predictions with respect to sparse labels.

[`false_negatives(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/false_negatives)
: Computes the total number of false negatives.

[`false_negatives_at_thresholds(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/false_negatives_at_thresholds)
: Computes false negatives at provided threshold values.

[`false_positives(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/false_positives)
: Sum the weights of false positives.

[`false_positives_at_thresholds(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/false_positives_at_thresholds)
: Computes false positives at provided threshold values.

[`mean(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean)
: Computes the (weighted) mean of the given values.

[`mean_absolute_error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error)
: Computes the mean absolute error between the labels and predictions.

[`mean_cosine_distance(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_cosine_distance)
: Computes the cosine distance between the labels and predictions.

[`mean_iou(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_iou)
: Calculate per-step mean Intersection-Over-Union (mIOU).

[`mean_per_class_accuracy(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_per_class_accuracy)
: Calculates the mean of the per-class accuracies.

[`mean_relative_error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_relative_error)
: Computes the mean relative error by normalizing with the given values.

[`mean_squared_error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_squared_error)
: Computes the mean squared error between the labels and predictions.

[`mean_tensor(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_tensor)
: Computes the element-wise (weighted) mean of the given tensors.

[`percentage_below(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below)
: Computes the percentage of values less than the given threshold.

[`precision(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision)
: Computes the precision of the predictions with respect to the labels.

[`precision_at_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_k)
: Computes precision@k of the predictions with respect to sparse labels.

[`precision_at_thresholds(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds)
: Computes precision values for different `thresholds` on `predictions`.

[`precision_at_top_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_top_k)
: Computes precision@k of the predictions with respect to sparse labels.

[`recall(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall)
: Computes the recall of the predictions with respect to the labels.

[`recall_at_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_k)
: Computes recall@k of the predictions with respect to sparse labels.

[`recall_at_thresholds(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_thresholds)
: Computes various recall values for different `thresholds` on `predictions`.

[`recall_at_top_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/recall_at_top_k)
: Computes recall@k of top-k predictions with respect to sparse labels.

[`root_mean_squared_error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/root_mean_squared_error)
: Computes the root mean squared error between the labels and predictions.

[`sensitivity_at_specificity(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity)
: Computes the specificity at a given sensitivity.

[`sparse_average_precision_at_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sparse_average_precision_at_k)
: Renamed to `average_precision_at_k`, please use that method instead. (deprecated)

[`sparse_precision_at_k(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sparse_precision_at_k)
: Renamed to `precision_at_k`, please use that method instead. (deprecated)

[`specificity_at_sensitivity(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/specificity_at_sensitivity)
: Computes the specificity at a given sensitivity.

[`true_negatives(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/true_negatives)
: Sum the weights of true\_negatives.

[`true_negatives_at_thresholds(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/true_negatives_at_thresholds)
: Computes true negatives at provided threshold values.

[`true_positives(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/true_positives)
: Sum the weights of true\_positives.

[`true_positives_at_thresholds(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/true_positives_at_thresholds)
: Computes true positives at provided threshold values.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.