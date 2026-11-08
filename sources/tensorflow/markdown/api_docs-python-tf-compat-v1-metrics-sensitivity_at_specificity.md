[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.sensitivity\_at\_specificity Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/sensitivity_at_specificity#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L2989-L3089)

Computes the specificity at a given sensitivity.

tf.compat.v1.metrics.sensitivity_at_specificity(
        labels,
        predictions,
        specificity,
        weights=None,
        num_thresholds=200,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

The `sensitivity_at_specificity` function creates four local variables, `true_positives`, `true_negatives`, `false_positives` and `false_negatives` that are used to compute the sensitivity at the given specificity value. The threshold for the given specificity value is computed and used to evaluate the corresponding sensitivity.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `sensitivity`. `update_op` increments the `true_positives`, `true_negatives`, `false_positives` and `false_negatives` counts with the weight of each case found in the `predictions` and `labels`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

For additional information about specificity and sensitivity, see the following: [https://en.wikipedia.org/wiki/Sensitivity\_and\_specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth values, a `Tensor` whose dimensions must match `predictions`. Will be cast to `bool`. |
| `predictions` | A floating point `Tensor` of arbitrary shape and whose values are in the range `[0, 1]`. |
| `specificity` | A scalar value in range `[0, 1]`. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |
| `num_thresholds` | The number of thresholds to use for matching the given specificity. |
| `metrics_collections` | An optional list of collections that `sensitivity` should be added to. |
| `updates_collections` | An optional list of collections that `update_op` should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `sensitivity` | A scalar `Tensor` representing the sensitivity at the given `specificity` value. |
| `update_op` | An operation that increments the `true_positives`, `true_negatives`, `false_positives` and `false_negatives` variables appropriately and whose value matches `sensitivity`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `predictions` and `labels` have mismatched shapes, if `weights` is not `None` and its shape doesn't match `predictions`, or if `specificity` is not between 0 and 1, or if either `metrics_collections` or `updates_collections` are not a list or tuple. |
| `RuntimeError` | If eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.