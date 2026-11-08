[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Metric?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Metric Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#methods)
    *   [add\_variable](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#add_variable)
        
    *   [add\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#add_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#get_config)
        
    *   [reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#reset_state)
        
    *   [result](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#result)
        
    *   [stateless\_reset\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#stateless_reset_state)
        
    *   [stateless\_result](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#stateless_result)
        
    *   [stateless\_update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#stateless_update_state)
        
    *   [update\_state](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#update_state)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/Metric#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L11-L254)

Encapsulates metric logic and state.

#### View aliases

**Main aliases**

[`tf.keras.metrics.Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)

tf.keras.Metric(
        dtype=None, name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | Optional name for the metric instance. |
| `dtype` | The dtype of the metric's computations. Defaults to `None`, which means using [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br>. [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is a `"float32"` unless set to different value (via [`keras.backend.set_floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). If a [`keras.DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)<br> is provided, then the `compute_dtype` will be utilized. |

#### Example:

m = SomeMetric(...)
    for input in ...:
        m.update_state(input)
    print('Final result: ', m.result())

Usage with `compile()` API:

model = keras.Sequential()
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(10, activation='softmax'))
    
    model.compile(optimizer=keras.optimizers.RMSprop(0.01),
                  loss=keras.losses.CategoricalCrossentropy(),
                  metrics=[keras.metrics.CategoricalAccuracy()])
    
    data = np.random.random((1000, 32))
    labels = np.random.random((1000, 10))
    
    model.fit(data, labels, epochs=10)

To be implemented by subclasses:

*   `__init__()`: All state variables should be created in this method by calling `self.add_variable()` like: `self.var = self.add_variable(...)`
*   `update_state()`: Has all updates to the state variables like: `self.var.assign(...)`.
*   `result()`: Computes and returns a scalar value or a dict of scalar values for the metric from the state variables.

Example subclass implementation:

class BinaryTruePositives(Metric):
    
        def __init__(self, name='binary_true_positives', **kwargs):
            super().__init__(name=name, **kwargs)
            self.true_positives = self.add_variable(
                shape=(),
                initializer='zeros',
                name='true_positives'
            )
    
        def update_state(self, y_true, y_pred, sample_weight=None):
            y_true = ops.cast(y_true, "bool")
            y_pred = ops.cast(y_pred, "bool")
    
            values = ops.logical_and(
                ops.equal(y_true, True), ops.equal(y_pred, True))
            values = ops.cast(values, self.dtype)
            if sample_weight is not None:
                sample_weight = ops.cast(sample_weight, self.dtype)
                sample_weight = ops.broadcast_to(
                    sample_weight, ops.shape(values)
                )
                values = ops.multiply(values, sample_weight)
            self.true_positives.assign(self.true_positives + ops.sum(values))
    
        def result(self):
            return self.true_positives

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L233-L235)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L229-L231)

get_config()

Return the serializable config of the metric.

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L108-L115)

reset_state()

Reset all of the metric state variables.

This function is called between epochs/steps, when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L146-L152)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/metric.py#L117-L119)

update_state(
        *args, **kwargs
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