[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean_cosine_distance#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.mean\_cosine\_distance Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L1103-L1174)

Computes the cosine distance between the labels and predictions.

tf.compat.v1.metrics.mean_cosine_distance(
        labels,
        predictions,
        dim,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

The `mean_cosine_distance` function creates two local variables, `total` and `count` that are used to compute the average cosine distance between `predictions` and `labels`. This average is weighted by `weights`, and it is ultimately returned as `mean_distance`, which is an idempotent operation that simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `mean_distance`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | A `Tensor` of arbitrary shape. |
| `predictions` | A `Tensor` of the same shape as `labels`. |
| `dim` | The dimension along which the cosine distance is computed. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). Also, dimension `dim` must be `1`. |
| `metrics_collections` | An optional list of collections that the metric value variable should be added to. |
| `updates_collections` | An optional list of collections that the metric update ops should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `mean_distance` | A `Tensor` representing the current mean, the value of `total` divided by `count`. |
| `update_op` | An operation that increments the `total` and `count` variables appropriately. |

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