[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.mean Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L315-L478)

Computes the (weighted) mean of the given values.

tf.compat.v1.metrics.mean(
        values,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

Migrate to TF2
--------------

[`tf.compat.v1.metrics.mean`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/mean)
 is not compatible with eager execution or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. Please use [`tf.keras.metrics.Mean`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Mean)
 instead for TF2 migration. After instantiating a [`tf.keras.metrics.Mean`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Mean)
 object, you can first call the `update_state()` method to record the new values, and then call the `result()` method to get the mean eagerly. You can also attach it to a Keras model with the `add_metric` method. Please refer to the [migration guide](https://www.tensorflow.org/guide/migrate#new-style_metrics_and_losses)
 for more details.

#### Structural Mapping to TF2

Before:

mean, update_op = tf.compat.v1.metrics.mean(
      values=values,
      weights=weights,
      metrics_collections=metrics_collections,
      update_collections=update_collections,
      name=name)

After:

 m = tf.keras.metrics.Mean(
       name=name)
    
     m.update_state(
       values=values,
       sample_weight=weights)
    
     mean = m.result()

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `values` | `values` | In `update_state()` method |
| `weights` | `sample_weight` | In `update_state()` method |
| `metrics_collections` | Not supported | Metrics should be tracked explicitly or with Keras APIs, for example, [add\_metric](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#add_metric)<br>, instead of via collections |
| `updates_collections` | Not supported | \-  |
| `name` | `name` | In constructor |

#### Before & After Usage Example

Before:

    g = tf.Graph()

After:

    m = tf.keras.metrics.Mean()

# Used within Keras model
    model.add_metric(tf.keras.metrics.Mean()(values))

Description
-----------

The `mean` function creates two local variables, `total` and `count` that are used to compute the average of `values`. This average is ultimately returned as `mean` which is an idempotent operation that simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `mean`. `update_op` increments `total` with the reduced sum of the product of `values` and `weights`, and it increments `count` with the reduced sum of `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A `Tensor` of arbitrary dimensions. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `values`, and must be broadcastable to `values` (i.e., all dimensions must be either `1`, or the same as the corresponding `values` dimension). |
| `metrics_collections` | An optional list of collections that `mean` should be added to. |
| `updates_collections` | An optional list of collections that `update_op` should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `mean` | A `Tensor` representing the current mean, the value of `total` divided by `count`. |
| `update_op` | An operation that increments the `total` and `count` variables appropriately and whose value matches `mean_value`. |

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