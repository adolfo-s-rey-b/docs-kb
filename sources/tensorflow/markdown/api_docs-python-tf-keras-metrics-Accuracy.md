[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.Accuracy Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L15-L59)

Calculates how often predictions equal labels.

Inherits From: [`MeanMetricWrapper`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanMetricWrapper)
, [`Mean`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Mean)
, [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.Accuracy(
        name='accuracy', dtype=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate metrics and optimizers](https://www.tensorflow.org/guide/migrate/metrics_optimizers) | *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)<br>    <br>*   [CropNet: Cassava Disease Detection](https://www.tensorflow.org/hub/tutorials/cropnet_cassava) |

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Examples:

    m = keras.metrics.Accuracy()

    m.reset_state()

Usage with `compile()` API:

model.compile(optimizer='sgd',
                  loss='binary_crossentropy',
                  metrics=[keras.metrics.Accuracy()])

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/accuracy_metrics.py#L58-L59)

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