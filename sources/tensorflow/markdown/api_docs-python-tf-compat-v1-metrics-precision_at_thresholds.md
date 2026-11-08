[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.precision\_at\_thresholds Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision_at_thresholds#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L2231-L2309)

Computes precision values for different `thresholds` on `predictions`.

tf.compat.v1.metrics.precision_at_thresholds(
        labels,
        predictions,
        thresholds,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

The `precision_at_thresholds` function creates four local variables, `true_positives`, `true_negatives`, `false_positives` and `false_negatives` for various values of thresholds. `precision[i]` is defined as the total weight of values in `predictions` above `thresholds[i]` whose corresponding entry in `labels` is `True`, divided by the total weight of values in `predictions` above `thresholds[i]` (`true_positives[i] / (true_positives[i] + false_positives[i])`).

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `precision`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth values, a `Tensor` whose dimensions must match `predictions`. Will be cast to `bool`. |
| `predictions` | A floating point `Tensor` of arbitrary shape and whose values are in the range `[0, 1]`. |
| `thresholds` | A python list or tuple of float thresholds in `[0, 1]`. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |
| `metrics_collections` | An optional list of collections that `auc` should be added to. |
| `updates_collections` | An optional list of collections that `update_op` should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `precision` | A float `Tensor` of shape `[len(thresholds)]`. |
| `update_op` | An operation that increments the `true_positives`, `true_negatives`, `false_positives` and `false_negatives` variables that are used in the computation of `precision`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `predictions` and `labels` have mismatched shapes, or if `weights` is not `None` and its shape doesn't match `predictions`, or if either `metrics_collections` or `updates_collections` are not a list or tuple. |
| `RuntimeError` | If eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.