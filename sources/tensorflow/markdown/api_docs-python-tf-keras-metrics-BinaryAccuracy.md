[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.BinaryAccuracy Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryAccuracy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L72-L125)

Calculates how often predictions match binary labels.

Inherits From: [`MeanMetricWrapper`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanMetricWrapper)
, [`Mean`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Mean)
, [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.BinaryAccuracy(
        name='binary_accuracy', dtype=None, threshold=0.5
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning)<br>    <br>*   [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)<br>    <br>*   [TensorFlow Constrained Optimization Example Using CelebA Dataset](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)<br>    <br>*   [TFX Keras Component Tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/components_keras) |

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `threshold` | (Optional) Float representing the threshold for deciding whether prediction values are 1 or 0. |

#### Example:

    m = keras.metrics.BinaryAccuracy()

    m.reset_state()

Usage with `compile()` API:

model.compile(optimizer='sgd',
                  loss='binary_crossentropy',
                  metrics=[keras.metrics.BinaryAccuracy()])

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dtype` |     |
| `variables` |     |

Methods
-------

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L192-L209)

add_variable(
        shape, initializer, dtype=None, aggregation='sum', name=None
    )

### `add_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L211-L215)

add_weight(
        shape=(), initializer=None, dtype=None, name=None
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L215-L219)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L120-L125)

get_config()

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L151-L153)

reset_state()

Reset all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L155-L158)

result()

Compute the current metric value.

|     |
| --- |
| Returns |     |
| A scalar tensor, or a dictionary of scalar tensors. |     |

### `stateless_reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L170-L183)

stateless_reset_state()

### `stateless_result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L154-L168)

stateless_result(
        metric_variables
    )

### `stateless_update_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L121-L144)

stateless_update_state(
        metric_variables, *args, **kwargs
    )

### `update_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/reduction_metrics.py#L201-L207)

update_state(
        y_true, y_pred, sample_weight=None
    )

Accumulate statistics for the metric.

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L224-L227)

__call__(
        *args, **kwargs
    )

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.