[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#methods)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#add_loss)
        
    *   [add\_update](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#add_update)
        
    *   [get\_current\_value](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#get_current_value)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#__exit__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.StatelessScope Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#methods)
    *   [add\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#add_loss)
        
    *   [add\_update](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#add_update)
        
    *   [get\_current\_value](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#get_current_value)
        
    *   [\_\_enter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#__enter__)
        
    *   [\_\_exit\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope#__exit__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L5-L97)

Scope to prevent any update to Keras Variables.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.StatelessScope`](https://www.tensorflow.org/api_docs/python/tf/keras/StatelessScope)

tf.keras.StatelessScope(
        state_mapping=None, collect_losses=False, initialize_variables=True
    )

The values of variables to be used inside the scope should be passed via the `state_mapping` argument, a list of tuples `(k, v)` where `k` is a `Variable` and `v` is the intended value for this variable (a backend tensor).

Updated values can be collected on scope exit via `value = scope.get_current_value(variable)`. No updates will be applied in-place to any variables for the duration of the scope.

#### Example:

state_mapping = [(k, ops.ones(k.shape, k.dtype)) for k in model.weights]
    with keras.StatelessScope(state_mapping) as scope:
        outputs = model.some_function(inputs)
    
    # All model variables remain unchanged. Their new values can be
    # collected via:
    for k in model.weights:
        new_value = scope.get_current_value(k)
        print(f"New value for {k}: {new_value})

Methods
-------

### `add_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L75-L76)

add_loss(
        loss
    )

### `add_update`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L78-L80)

add_update(
        update
    )

### `get_current_value`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L82-L83)

get_current_value(
        variable
    )

### `__enter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L70-L73)

__enter__()

### `__exit__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L85-L97)

__exit__(
        *args, **kwargs
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.