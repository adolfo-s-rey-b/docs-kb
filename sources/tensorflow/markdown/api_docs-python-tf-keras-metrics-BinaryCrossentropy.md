[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fmetrics%2FBinaryCrossentropy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.BinaryCrossentropy Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/BinaryCrossentropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L101-L168)

Computes the crossentropy metric between the labels and predictions.

Inherits From: [`MeanMetricWrapper`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanMetricWrapper)
, [`Mean`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Mean)
, [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.BinaryCrossentropy(
        name='binary_crossentropy',
        dtype=None,
        from_logits=False,
        label_smoothing=0
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Overfit and underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)<br>    <br>*   [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)<br>    <br>*   [Unified Embedding Tables (UET)](https://www.tensorflow.org/recommenders/examples/uet) |

This is the crossentropy metric class to be used when there are only two label classes (0 and 1).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `from_logits` | (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution. |
| `label_smoothing` | (Optional) Float in `[0, 1]`. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. e.g. `label_smoothing=0.2` means that we will use a value of 0.1 for label "0" and 0.9 for label "1". |

#### Examples:

    m = keras.metrics.BinaryCrossentropy()

    m.reset_state()

Usage with `compile()` API:

model.compile(
        optimizer='sgd',
        loss='mse',
        metrics=[keras.metrics.BinaryCrossentropy()])

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L162-L168)

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

Last updated 2026-11-05 UTC.