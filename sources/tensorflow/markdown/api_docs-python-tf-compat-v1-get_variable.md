[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fget_variable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_variable Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1549-L1581)

Gets an existing variable with these parameters or create a new one.

tf.compat.v1.get_variable(
        name,
        shape=None,
        dtype=None,
        initializer=None,
        regularizer=None,
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

Migrate to TF2
--------------

Although it is a legacy [`compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
 api, [`tf.compat.v1.get_variable`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable)
 is mostly compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 but only if you combine it with the `tf.compat.v1.keras.utils.track_tf1_style_variables` decorator. (Though it will behave as if reuse is always set to `AUTO_REUSE`.)

See the [model migration guide](https://www.tensorflow.org/guide/migrate/model_mapping)
 for more info.

If you do not combine it with `tf.compat.v1.keras.utils.track_tf1_style_variables`, `get_variable` will create a brand new variable every single time it is called and will never reuse variables, regardless of variable names or `reuse` arguments.

The TF2 equivalent of this symbol would be [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
, but note that when using [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 you must make sure you track your variables (and regularizer arguments) either manually or via [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 or [`tf.keras.layers.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
 mechanisms.

A section of the [migration guide](https://www.tensorflow.org/guide/migrate/model_mapping#incremental_migration_to_native_tf2)
 provides more details on incrementally migrating these usages to [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 as well.

Description
-----------

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping) | *   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

This function prefixes the name with the current variable scope and performs reuse checks. See the [Variable Scope How To](https://tensorflow.org/guide/variables)
 for an extensive description of how reusing works. Here is a basic example:

def foo():
      with tf.variable_scope("foo", reuse=tf.AUTO_REUSE):
        v = tf.get_variable("v", [1])
      return v
    
    v1 = foo()  # Creates v.
    v2 = foo()  # Gets the same, existing v.
    assert v1 == v2

If initializer is `None` (the default), the default initializer passed in the variable scope will be used. If that one is `None` too, a `glorot_uniform_initializer` will be used. The initializer can also be a Tensor, in which case the variable is initialized to this value and shape.

Similarly, if the regularizer is `None` (the default), the default regularizer passed in the variable scope will be used (if that is `None` too, then by default no regularization is performed).

If a partitioner is provided, a `PartitionedVariable` is returned. Accessing this object as a `Tensor` returns the shards concatenated along the partition axis.

Some useful partitioners are available. See, e.g., `variable_axis_size_partitioner` and `min_max_variable_partitioner`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | The name of the new or existing variable. |
| `shape` | Shape of the new or existing variable. |
| `dtype` | Type of the new or existing variable (defaults to `DT_FLOAT`). |
| `initializer` | Initializer for the variable if one is created. Can either be an initializer object or a Tensor. If it's a Tensor, its shape must be known unless validate\_shape is False. |
| `regularizer` | A (Tensor -> Tensor or None) function; the result of applying it on a newly created variable will be added to the collection `tf.GraphKeys.REGULARIZATION_LOSSES` and can be used for regularization. |
| `trainable` | If `True` also add the variable to the graph collection `GraphKeys.TRAINABLE_VARIABLES` (see [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>). |
| `collections` | List of graph collections keys to add the Variable to. Defaults to `[GraphKeys.GLOBAL_VARIABLES]` (see [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>). |
| `caching_device` | Optional device string or function describing where the Variable should be cached for reading. Defaults to the Variable's device. If not `None`, caches on another device. Typical use is to cache on the device where the Ops using the Variable reside, to deduplicate copying through `Switch` and other conditional statements. |
| `partitioner` | Optional callable that accepts a fully defined `TensorShape` and `dtype` of the Variable to be created, and returns a list of partitions for each axis (currently only one axis can be partitioned). |
| `validate_shape` | If False, allows the variable to be initialized with a value of unknown shape. If True, the default, the shape of initial\_value must be known. For this to be used the initializer must be a Tensor and not an initializer object. |
| `use_resource` | If False, creates a regular Variable. If true, creates an experimental ResourceVariable instead with well-defined semantics. Defaults to False (will later change to True). When eager execution is enabled this argument is always forced to be True. |
| `custom_getter` | Callable that takes as a first argument the true getter, and allows overwriting the internal get\_variable method. The signature of `custom_getter` should match that of this method, but the most future-proof version will allow for changes: `def custom_getter(getter, *args, **kwargs)`. Direct access to all `get_variable` parameters is also allowed: `def custom_getter(getter, name, *args, **kwargs)`. A simple identity custom getter that simply creates variables with modified names is:<br><br>def custom_getter(getter, name, *args, **kwargs):<br>      return getter(name + '_suffix', *args, **kwargs) |
| `constraint` | An optional projection function to be applied to the variable after being updated by an `Optimizer` (e.g. used to implement norm constraints or value constraints for layer weights). The function must take as input the unprojected Tensor representing the value of the variable and return the Tensor for the projected value (which must have the same shape). Constraints are not safe to use when doing asynchronous distributed training. |
| `synchronization` | Indicates when a distributed a variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableSynchronization`](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization)<br>. By default the synchronization is set to `AUTO` and the current `DistributionStrategy` chooses when to synchronize. |
| `aggregation` | Indicates how a distributed variable will be aggregated. Accepted values are constants defined in the class [`tf.VariableAggregation`](https://www.tensorflow.org/api_docs/python/tf/VariableAggregation)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The created or existing `Variable` (or `PartitionedVariable`, if a partitioner was used). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | when creating a new variable and shape is not declared, when violating reuse during variable creation, or when `initializer` dtype and `dtype` don't match. Reuse is set inside `variable_scope`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.