[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.percentage\_below Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/percentage_below#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L1600-L1652)

Computes the percentage of values less than the given threshold.

tf.compat.v1.metrics.percentage_below(
        values,
        threshold,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

The `percentage_below` function creates two local variables, `total` and `count` that are used to compute the percentage of `values` that fall below `threshold`. This rate is weighted by `weights`, and it is ultimately returned as `percentage` which is an idempotent operation that simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `percentage`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A numeric `Tensor` of arbitrary size. |
| `threshold` | A scalar threshold. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `values`, and must be broadcastable to `values` (i.e., all dimensions must be either `1`, or the same as the corresponding `values` dimension). |
| `metrics_collections` | An optional list of collections that the metric value variable should be added to. |
| `updates_collections` | An optional list of collections that the metric update ops should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `percentage` | A `Tensor` representing the current mean, the value of `total` divided by `count`. |
| `update_op` | An operation that increments the `total` and `count` variables appropriately. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `weights` is not `None` and its shape doesn't match `values`, or if either `metrics_collections` or `updates_collections` are not a list or tuple. |
| `RuntimeError` | If eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.