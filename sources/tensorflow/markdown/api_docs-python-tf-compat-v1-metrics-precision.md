[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.precision Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/precision#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L2136-L2228)

Computes the precision of the predictions with respect to the labels.

tf.compat.v1.metrics.precision(
        labels,
        predictions,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings) |

The `precision` function creates two local variables, `true_positives` and `false_positives`, that are used to compute the precision. This value is ultimately returned as `precision`, an idempotent operation that simply divides `true_positives` by the sum of `true_positives` and `false_positives`.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `precision`. `update_op` weights each prediction by the corresponding value in `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth values, a `Tensor` whose dimensions must match `predictions`. Will be cast to `bool`. |
| `predictions` | The predicted values, a `Tensor` of arbitrary dimensions. Will be cast to `bool`. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |
| `metrics_collections` | An optional list of collections that `precision` should be added to. |
| `updates_collections` | An optional list of collections that `update_op` should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `precision` | Scalar float `Tensor` with the value of `true_positives` divided by the sum of `true_positives` and `false_positives`. |
| `update_op` | `Operation` that increments `true_positives` and `false_positives` variables appropriately and whose value matches `precision`. |

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