[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.SparseCategoricalCrossentropy Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/SparseCategoricalCrossentropy#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L258-L345)

Computes the crossentropy metric between the labels and predictions.

Inherits From: [`MeanMetricWrapper`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanMetricWrapper)
, [`Mean`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Mean)
, [`Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.metrics.SparseCategoricalCrossentropy(
        name='sparse_categorical_crossentropy',
        dtype=None,
        from_logits=False,
        ignore_class=None,
        axis=-1
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate early stopping](https://www.tensorflow.org/guide/migrate/early_stopping) | *   [Working with tff's ClientData.](https://www.tensorflow.org/federated/tutorials/working_with_client_data) |

Use this crossentropy metric when there are two or more label classes. It expects labels to be provided as integers. If you want to provide labels that are one-hot encoded, please use the `CategoricalCrossentropy` metric instead.

There should be `num_classes` floating point values per feature for `y_pred` and a single floating point value per feature for `y_true`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `from_logits` | (Optional) Whether output is expected to be a logits tensor. By default, we consider that output encodes a probability distribution. |
| `ignore_class` | (Optional) Integer. Class to ignore. If `None`, no class is ignored. |
| `axis` | (Optional) Defaults to `-1`. The dimension along which entropy is computed. |

#### Examples:

    # y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]]

    m.reset_state()

Usage with `compile()` API:

model.compile(
        optimizer='sgd',
        loss='mse',
        metrics=[keras.metrics.SparseCategoricalCrossentropy()])

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/probabilistic_metrics.py#L338-L345)

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