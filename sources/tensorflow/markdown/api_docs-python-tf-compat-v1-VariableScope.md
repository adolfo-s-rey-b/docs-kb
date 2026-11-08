[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#methods)
    *   [get\_collection](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#get_collection)
        
    *   [get\_variable](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#get_variable)
        
    *   [global\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#global_variables)
        
    *   [local\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#local_variables)
        
    *   [reuse\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#reuse_variables)
        
    *   [set\_caching\_device](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_caching_device)
        
    *   [set\_custom\_getter](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_custom_getter)
        
    *   [set\_dtype](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_dtype)
        
    *   [set\_initializer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_initializer)
        
    *   [set\_partitioner](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_partitioner)
        
    *   [set\_regularizer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_regularizer)
        
    *   [set\_use\_resource](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_use_resource)
        
    *   [trainable\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#trainable_variables)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.VariableScope Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#methods)
    *   [get\_collection](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#get_collection)
        
    *   [get\_variable](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#get_variable)
        
    *   [global\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#global_variables)
        
    *   [local\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#local_variables)
        
    *   [reuse\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#reuse_variables)
        
    *   [set\_caching\_device](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_caching_device)
        
    *   [set\_custom\_getter](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_custom_getter)
        
    *   [set\_dtype](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_dtype)
        
    *   [set\_initializer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_initializer)
        
    *   [set\_partitioner](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_partitioner)
        
    *   [set\_regularizer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_regularizer)
        
    *   [set\_use\_resource](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#set_use_resource)
        
    *   [trainable\_variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/VariableScope#trainable_variables)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1058-L1366)

Variable scope object to carry defaults to provide to `get_variable`.

tf.compat.v1.VariableScope(
        reuse,
        name='',
        initializer=None,
        regularizer=None,
        caching_device=None,
        partitioner=None,
        custom_getter=None,
        name_scope='',
        dtype=tf.dtypes.float32,
        use_resource=None,
        constraint=None
    )

Many of the arguments we need for `get_variable` in a variable store are most easily handled with a context. This object is used for the defaults.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `name` | name of the current scope, used as prefix in get\_variable. |
| `initializer` | default initializer passed to get\_variable. |
| `regularizer` | default regularizer passed to get\_variable. |
| `reuse` | Boolean, None, or tf.compat.v1.AUTO\_REUSE, setting the reuse in get\_variable. When eager execution is enabled this argument is always forced to be False. |
| `caching_device` | string, callable, or None: the caching device passed to get\_variable. |
| `partitioner` | callable or `None`: the partitioner passed to `get_variable`. |
| `custom_getter` | default custom getter passed to get\_variable. |
| `name_scope` | The name passed to [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)<br>. |
| `dtype` | default type passed to get\_variable (defaults to DT\_FLOAT). |
| `use_resource` | if False, create a normal Variable; if True create an experimental ResourceVariable with well-defined semantics. Defaults to False (will later change to True). When eager execution is enabled this argument is always forced to be True. |
| `constraint` | An optional projection function to be applied to the variable after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected Tensor representing the value of the variable and return the Tensor for the projected value (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training. |
| `original_name_scope` |     |

Methods
-------

### `get_collection`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1204-L1207)

get_collection(
        name
    )

Get this scope's variables.

### `get_variable`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1221-L1291)

get_variable(
        var_store,
        name,
        shape=None,
        dtype=None,
        initializer=None,
        regularizer=None,
        reuse=None,
        trainable=None,
        collections=None,
        caching_device=None,
        partitioner=None,
        validate_shape=True,
        use_resource=None,
        custom_getter=None,
        constraint=None,
        synchronization=tf.VariableSynchronization.AUTO,
        aggregation=tf.compat.v1.VariableAggregation.NONE
    )

Gets an existing variable with this name or create a new one.

### `global_variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1213-L1215)

global_variables()

Get this scope's global variables.

### `local_variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1217-L1219)

local_variables()

Get this scope's local variables.

### `reuse_variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1166-L1168)

reuse_variables()

Reuse variables in this scope.

### `set_caching_device`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1189-L1194)

set_caching_device(
        caching_device
    )

Set caching\_device for this scope.

### `set_custom_getter`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1200-L1202)

set_custom_getter(
        custom_getter
    )

Set custom getter for this scope.

### `set_dtype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1174-L1176)

set_dtype(
        dtype
    )

Set data type for this scope.

### `set_initializer`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1170-L1172)

set_initializer(
        initializer
    )

Set initializer for this scope.

### `set_partitioner`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1196-L1198)

set_partitioner(
        partitioner
    )

Set partitioner for this scope.

### `set_regularizer`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1185-L1187)

set_regularizer(
        regularizer
    )

Set regularizer for this scope.

### `set_use_resource`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1178-L1183)

set_use_resource(
        use_resource
    )

Sets whether to use ResourceVariables for this scope.

### `trainable_variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1209-L1211)

trainable_variables()

Get this scope's trainable variables.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.