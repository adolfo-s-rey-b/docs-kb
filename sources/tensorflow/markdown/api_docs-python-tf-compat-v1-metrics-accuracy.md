[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.metrics.accuracy Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/metrics_impl.py#L481-L634)

Calculates how often `predictions` matches `labels`.

tf.compat.v1.metrics.accuracy(
        labels,
        predictions,
        weights=None,
        metrics_collections=None,
        updates_collections=None,
        name=None
    )

Migrate to TF2
--------------

[`tf.compat.v1.metrics.accuracy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/metrics/accuracy)
 is not compatible with eager execution or [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. Please use [`tf.keras.metrics.Accuracy`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy)
 instead for TF2 migration. After instantiating a [`tf.keras.metrics.Accuracy`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy)
 object, you can first call the `update_state()` method to record the prediction/labels, and then call the `result()` method to get the accuracy eagerly. You can also attach it to a Keras model when calling the `compile` method. Please refer to [this guide](https://www.tensorflow.org/guide/migrate#new-style_metrics_and_losses)
 for more details.

#### Structural Mapping to Native TF2

Before:

accuracy, update_op = tf.compat.v1.metrics.accuracy(
      labels=labels,
      predictions=predictions,
      weights=weights,
      metrics_collections=metrics_collections,
      update_collections=update_collections,
      name=name)

After:

 m = tf.keras.metrics.Accuracy(
       name=name,
       dtype=None)
    
     m.update_state(
     y_true=labels,
     y_pred=predictions,
     sample_weight=weights)
    
     accuracy = m.result()

#### How to Map Arguments

| TF1 Arg Name | TF2 Arg Name | Note |
| --- | --- | --- |
| `label` | `y_true` | In `update_state()` method |
| `predictions` | `y_true` | In `update_state()` method |
| `weights` | `sample_weight` | In `update_state()` method |
| `metrics_collections` | Not supported | Metrics should be tracked explicitly or with Keras APIs, for example, [add\_metric](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#add_metric)<br>, instead of via collections |
| `updates_collections` | Not supported | \-  |
| `name` | `name` | In constructor |

#### Before & After Usage Example

Before:

    g = tf.Graph()

After:

    m = tf.keras.metrics.Accuracy()

# Used within Keras model
    model.compile(optimizer='sgd',
                  loss='mse',
                  metrics=[tf.keras.metrics.Accuracy()])

Description
-----------

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate metrics and optimizers](https://www.tensorflow.org/guide/migrate/metrics_optimizers) | *   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

The `accuracy` function creates two local variables, `total` and `count` that are used to compute the frequency with which `predictions` matches `labels`. This frequency is ultimately returned as `accuracy`: an idempotent operation that simply divides `total` by `count`.

For estimation of the metric over a stream of data, the function creates an `update_op` operation that updates these variables and returns the `accuracy`. Internally, an `is_correct` operation computes a `Tensor` with elements 1.0 where the corresponding elements of `predictions` and `labels` match and 0.0 otherwise. Then `update_op` increments `total` with the reduced sum of the product of `weights` and `is_correct`, and it increments `count` with the reduced sum of `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `labels` | The ground truth values, a `Tensor` whose shape matches `predictions`. |
| `predictions` | The predicted values, a `Tensor` of any shape. |
| `weights` | Optional `Tensor` whose rank is either 0, or the same rank as `labels`, and must be broadcastable to `labels` (i.e., all dimensions must be either `1`, or the same as the corresponding `labels` dimension). |
| `metrics_collections` | An optional list of collections that `accuracy` should be added to. |
| `updates_collections` | An optional list of collections that `update_op` should be added to. |
| `name` | An optional variable\_scope name. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `accuracy` | A `Tensor` representing the accuracy, the value of `total` divided by `count`. |
| `update_op` | An operation that increments the `total` and `count` variables appropriately and whose value matches `accuracy`. |

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