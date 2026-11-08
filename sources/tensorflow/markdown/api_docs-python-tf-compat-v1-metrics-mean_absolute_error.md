[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fmetrics%2Fmean_absolute_error&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.mean\_absolute\_error Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_absolute_error#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L1042-L1100)

Computes the mean absolute error between the labels and predictions.

tf.compat.v1.metrics.mean_absolute_error(
        labels,
        predictions,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

The `mean_absolute_error` function creates two local variables, `total` and `count` that are used to compute the mean absolute error. This average is weighted by `weights`, and it is ultimately returned as `mean_absolute_error`: an idempotent operation that simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `mean_absolute_error`. Internally, an `absolute_errors` operation computes the absolute value of the differences between `predictions` and `labels`. Then `update_op` increments `total` with the reduced sum of the product of `weights` and `absolute_errors`, and it increments `count` with the reduced sum of `weights`

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | A `Tensor` of the same shape as `predictions`. |
| `predictions` | A `Tensor` of arbitrary shape. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |
| `metrics_collections` | An optional list of collections that `mean_absolute_error` should be added to. |
| `updates_collections` | An optional list of collections that `update_op` should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `mean_absolute_error` | A `Tensor` representing the current mean, the value of `total` divided by `count`. |
| `update_op` | An operation that increments the `total` and `count` variables appropriately and whose value matches `mean_absolute_error`. |

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